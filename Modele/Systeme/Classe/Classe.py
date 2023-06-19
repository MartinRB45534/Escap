from __future__ import annotations
from typing import TYPE_CHECKING, Set
import Affichage as af

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Skill.Skill import Skill_intrasec, Skill_extra
    from ..Skill.Actif import Actif
    from ..Skill.Passif import Skill_debut_tour

# Pas de classe parente

# Valeurs par défaut des paramètres

class Classe:
    """!!! Classe != class !!! Correspond aux classes avec des niveaux, qui évoluent, contiennent des skills, etc."""
    def __init__(self,conditions_evo=[0,10,20,30,40,50,60,70,80,90],skills_intrasecs:Set[Skill_intrasec]=set(),skills:Set[Skill_extra]=set()):
        """conditions_evo : les conditions d'évolution de la classe au niveau supérieur ; si c'est un nombre, indique l'xp nécessaire à l'évolution, si c'est une chaine de caractère, indique la fonction capable d'évaluer la condition
           skills_intrasecs : les skills obtenus automatiquement avec la classe
           cadeux_evo : les récompenses d'évolution ; peuvent être des skills, des classes ou de l'xp""" #Plus vraiment, en fait... À rafraichir
        self.skills=skills
        self.skills_intrasecs=skills_intrasecs
        self.sous_classes:Set[Classe]=set() #Une classe peut posséder des sous-classes, qui contribueront à son évolution moins qu'à celle de la classe principale
        self.niveau=0 #Le niveau devrais passer à 1 lorsqu'on acquiert la classe
        self.cond_evo=conditions_evo
        self.xp=0 #L'xp commence à 0, évidemment
        self.xp_new=0 #Contabilise l'xp obtenue pendant le tour, pour la propagation
        self.propagation=0.1 #Certaines classes ont un taux de propagation plus important
        self.nom = "classe anonyme"
        
    def gagne_xp(self):
        #On récupère l'xp propagé par les skills,
        for skill in self.skills:
            self.xp_new+=skill.gagne_xp()
        #les skills intrasecs
        for skill in self.skills_intrasecs:
            self.xp_new+=skill.gagne_xp()
        #et par les sous-classes
        for classe in self.sous_classes:
            self.xp_new+=classe.gagne_xp()
        #Qu'on propage vers la classe supérieure
        res = self.xp_new*self.propagation
        #On l'ajoute aussi à son propre xp
        self.xp+=self.xp_new
        self.xp_new=0
        #On en profite pour vérifier si on peut évoluer
        self.check_evo()
        return res
        
    def vire_xp(self):
        for skill in self.skills:
            skill.xp_new = 0
        for skill in self.skills_intrasecs:
            skill.xp_new = 0
        for classe in self.sous_classes:
            classe.vire_xp()
        self.xp_new=0 #Pas nécessaire, je suppose ?

    def check_evo(self):
        """fonction qui vérifie que les conditions d'évolution sont vérifiées"""
        if self.niveau<len(self.cond_evo) and self.cond_evo[self.niveau]>0 and self.xp>=self.cond_evo[self.niveau]:
            self.evo()

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            self.niveau+=1
            for skill in self.skills_intrasecs:
                skill.evo()

    def get_skills_actifs(self) -> Set[Actif]:
        skills:Set[Actif] = set()
        for skill in self.skills | self.skills_intrasecs:
            if isinstance(skill,Actif):
                skills.add(skill) #Ne prend pas en compte la création d'items pour l'instant !
        for classe in self.sous_classes:
            skills |= classe.get_skills_actifs()
        return skills

    def debut_tour(self) -> Set[Skill_debut_tour]:
        """Fonction qui renvoie tous les skills qui ont besoin d'être appelés au début du tour (juste les auras pour l'instant)."""
        skills:Set[Skill_debut_tour] = set()
        for skill in self.skills | self.skills_intrasecs:
            if isinstance(skill,Skill_debut_tour):
                skills.add(skill)
        for classe in self.sous_classes:
            skills |= classe.debut_tour()
        return skills

    def get_skin(self):
        return af.SKIN_MYSTERE
    
# Imports utilisés dans le code
from ..Skill.Actif import Actif
from ..Skill.Passif import Skill_debut_tour
