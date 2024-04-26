from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..skill import Skill, SkillIntrasec, SkillExtra, Actif

# Pas de classe parente

# Valeurs par défaut des paramètres

class Classe:
    """Correspond aux classes avec des niveaux, qui évoluent, contiennent des skills, etc."""
    types_intrasecs:set[type[SkillIntrasec]]
    types_extrasecs:set[type[SkillExtra]]
    types_sous_classes:set[type[Classe]]
    conditions_evo: list[float|bool]
    propagation: float
    def __init__(self):
        """conditions_evo : les conditions d'évolution de la classe au niveau supérieur ; si c'est un nombre, indique l'xp nécessaire à l'évolution, si c'est une chaine de caractère, indique la fonction capable d'évaluer la condition
           skills_intrasecs : les skills obtenus automatiquement avec la classe
           cadeux_evo : les récompenses d'évolution ; peuvent être des skills, des classes ou de l'xp""" #Plus vraiment, en fait... À rafraichir
        self.skills = {skill() for skill in self.types_extrasecs}
        self.skills_intrasecs = {skill() for skill in self.types_intrasecs}
        self.sous_classes = {classe() for classe in self.types_sous_classes}
        self.niveau = 1
        self.xp: float = 0
        self.xp_new: float = 0

    def gagne_xp(self) -> float:
        """fonction qui propage l'xp accumulé au cours du tour vers la classe mère"""
        for skill in self.skills | self.skills_intrasecs:
            self.xp_new += skill.gagne_xp()
        for classe in self.sous_classes:
            self.xp_new += classe.gagne_xp()
        res = self.xp_new * self.propagation
        self.xp += self.xp_new
        self.xp_new = 0
        if self.check_evo():
            self.evo()
        return res

    def vire_xp(self):
        """fonction qui supprime l'xp accumulé au cours du tour"""
        for skill in self.skills | self.skills_intrasecs:
            skill.xp_new = 0
        for classe in self.sous_classes:
            classe.vire_xp()
        self.xp_new=0

    def check_evo(self):
        """fonction qui vérifie que les conditions d'évolution sont vérifiées"""
        condition = self.conditions_evo[self.niveau-1]
        if isinstance(condition, bool):
            return condition
        return self.xp >= condition

    def evo(self):
        """fonction qui procède à l'évolution"""
        self.niveau+=1
        for skill in self.skills_intrasecs:
            skill.niveau+=1

    def get_skills_actifs(self) -> set[Actif]:
        """Fonction qui renvoie tous les skills actifs de la classe et de ses sous-classes"""
        skills:set[Actif] = set()
        for skill in self.skills:
            if isinstance(skill,Actif):
                skills.add(skill)
        for skill in self.skills_intrasecs:
            if isinstance(skill,Actif) and skill.niveau >= skill.niveau_min: # En dessous du niveau min, on fait comme si le skill n'existait pas
                skills.add(skill)
        for classe in self.sous_classes:
            skills |= classe.get_skills_actifs()
        return skills

    # T is a type, and must be a subclass of Skill
    if TYPE_CHECKING:
        T = TypeVar('T', bound=Skill)

    def trouve_skill(self,type_skill:type[T]) -> set[T]:
        """Fonction qui renvoie le skill de la classe de type type_skill, ou None si il n'y en a pas."""
        res:set[type_skill] = set()
        for skill in self.skills:
            if isinstance(skill,type_skill): #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
                res.add(skill)
        for skill in self.skills_intrasecs:
            if isinstance(skill,type_skill) and skill.niveau > skill.niveau_min: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
                res.add(skill)
        for sous_classe in self.sous_classes: #On récurse la recherche dans les sous-classes.
            res |= sous_classe.trouve_skill(type_skill)
        return res
