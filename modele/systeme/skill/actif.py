from __future__ import annotations
from typing import TYPE_CHECKING, Any
from modele.action import ActionSkill

# Imports des classes parentes
from .skill import Skill, SkillExtraGenerique, SkillExtraArme, SkillIntrasecGenerique
from ...commons import TypesCompetencesGeneriques, TypesCompetencesArmes, TypesCompetencesIntrasequesGeneriques

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...action import Magie, ActionSkill, Derobe, Blocage, Alchimie, Attaque, Marche, Ramasse, LancerItem

class Actif(Skill):
    """
    Les skills qui genèrent les actions.
    """
    def fait(self, nom:str="") -> type[ActionSkill]:
        """Fait l'action"""
        raise NotImplementedError

class SkillsOffensifs(Actif, SkillExtraGenerique):
    """
    Un skill qui genère une attaque (hors attaque magique).
    """
    type_competence = TypesCompetencesGeneriques.OFFENSIF
    attaques: list[dict[str, type[Attaque]]]
    def fait(self, nom:str="") -> type[Attaque]:
        """Fait l'attaque"""
        return self.attaques[self.niveau - 1][nom]
    
class SkillOffensifArme(Actif, SkillExtraArme):
    """
    Un skill qui genère une attaque (hors attaque magique) avec une arme.
    """
    type_competence = TypesCompetencesArmes.OFFENSIF
    attaques: list[dict[str, type[Attaque]]]
    def fait(self, nom:str="") -> type[Attaque]:
        """Fait l'attaque"""
        return self.attaques[self.niveau - 1][nom]

class SkillsProjectiles(Actif, SkillExtraGenerique):
    """
    Un skill qui lance un objet.
    """
    type_competence = TypesCompetencesGeneriques.PROJECTILE
    lancers: list[dict[str, type[LancerItem]]]
    def fait(self, nom:str="") -> type[LancerItem]:
        """Utilise le skill, et renvoie l'objet lancé"""
        return self.lancers[self.niveau - 1][nom]

class SkillsMagiques(Actif, SkillExtraGenerique):
    """
    Un skill qui permet de lancer des magies.
    """
    type_competence = TypesCompetencesGeneriques.MAGIQUE
    magies: list[dict[str, type[Magie]]]
    def fait(self, nom:str="") -> type[Magie]:
        """Fait la magie"""
        return self.magies[self.niveau - 1][nom]

class SkillDeplacement(Actif, SkillIntrasecGenerique):
    """
    Un skill qui permet de se déplacer vers une case adjacente.
    """
    type_competence = TypesCompetencesIntrasequesGeneriques.DEPLACEMENT
    deplacements: list[dict[str, type[Marche]]]
    def fait(self, nom:str="") -> type[Marche]:
        """Fait le déplacement"""
        return self.deplacements[self.niveau - 1][nom]

class SkillRamasse(Actif, SkillIntrasecGenerique):
    """
    Un skill qui permet de ramasser des objets sur sa case.
    """
    type_competence = TypesCompetencesIntrasequesGeneriques.RAMASSE
    ramasses: list[dict[str, type[Ramasse]]]
    def fait(self, nom:str="") -> type[Ramasse]:
        """Fait le ramassage"""
        return self.ramasses[self.niveau - 1][nom]
    
class SkillDerobe(Actif, SkillExtraGenerique):
    """
    Un skill qui permet de voler un objet à un autre agissant.
    """
    type_competence = TypesCompetencesGeneriques.VOL
    derobes: list[dict[str, type[Derobe]]]
    def fait(self, nom:str="") -> type[Derobe]:
        """Fait le dérobage"""
        return self.derobes[self.niveau - 1][nom]
    
class SkillBlocage(Actif, SkillExtraGenerique):
    """
    Un skill qui permet de bloquer les attaques avec un bouclier.
    """
    type_competence = TypesCompetencesGeneriques.BLOQUE
    blocages: list[dict[str, type[Blocage]]]
    def fait(self, nom:str="") -> type[Blocage]:
        """Fait le blocage"""
        return self.blocages[self.niveau - 1][nom]
    
class SkillAlchimie(Actif, SkillExtraGenerique):
    """
    Un skill qui permet de fabriquer des objets.
    """
    type_competence = TypesCompetencesGeneriques.ALCHIMIE
    alchimies: list[dict[str, type[Alchimie]]]
    def fait(self, nom:str="") -> type[Alchimie]:
        """Fait l'alchimie"""
        return self.alchimies[self.niveau - 1][nom]

# TODO : réfléchir aux skills des slimes
# class SkillMerge(Actif):
#     """
#     Un skill qui permet à deux groupes de fusionner. Unique aux slimes.
#     """
#     def __init__(self):
#         Actif.__init__(self)
#         self.nom="Fusion de slimes"

#     # /!\ À compléter

# class SkillAbsorb(Actif):
#     """Un skill qui permet d'absorber un cadavre (le ramasser et récupérer un skill). Unique aux slimes."""
#     def __init__(self):
#         Actif.__init__(self)
#         self.nom="Absorption de cadavre"

# class SkillDivide(Actif):
#     """Un skill qui permet à un agissant de se séparer en deux. Unique aux slimes."""
#     def __init__(self):
#         Actif.__init__(self)
#         self.nom="Division"

class SkillIssue(Actif):
    """The absence of a skill."""
    def __equal__(self, other:Any):
        return isinstance(other, SkillIssue)
    
    def fait(self, nom:str="") -> type[ActionSkill]:
        """Fait l'action"""
        raise NotImplementedError

SKILL_ISSUE = SkillIssue()
