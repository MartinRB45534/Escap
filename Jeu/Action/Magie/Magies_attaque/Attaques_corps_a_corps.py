from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Systeme.Skill.Actif import Actif

# Imports des classes parentes
from Jeu.Action.Magie.Magie import Magie,Magie_dirigee,Magies_offensives

class Magie_attaque_corp_a_corp(Magies_offensives):
    """Les magies qui créent une attaque au corp à corp."""
    def __init__(self,skill:Actif,agissant:Agissant,gain_xp:float,cout_pm:float,portee:float,degats:float,element:int,propagation:str,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.degats = degats
        self.element = element
        self.propagation = propagation

    def action(self):
        for case in self.agissant.controleur.get_pos_touches(self.agissant.position,self.portee,self.propagation,responsable=self.agissant):
            self.agissant.controleur.case_from_position(case).effets.append(Attaque_case(self.agissant,self.degats,self.element,"proximité"))

class Magie_attaque_corp_a_corp_dirigee(Magie_dirigee,Magie_attaque_corp_a_corp):
    def __init__(self,skill:Actif,agissant:Agissant,direction:Optional[Direction],gain_xp:float,cout_pm:float,portee:float,degats:float,element:int,propagation:str,latence:float,niveau:int):
        Magie_attaque_corp_a_corp.__init__(self,skill,agissant,gain_xp,cout_pm,portee,degats,element,propagation,latence,niveau)
        self.direction = direction

    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for case in self.agissant.controleur.get_pos_touches(self.agissant.position,self.portee,self.propagation,self.direction,responsable=self.agissant):
                self.agissant.controleur.case_from_position(case).effets.append(Attaque_case(self.agissant,self.degats,self.element,"proximité",self.direction))

class Magie_laser(Magie_attaque_corp_a_corp_dirigee):
    """La magie qui crée une attaque de laser."""
    nom = "magie laser"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,direction:Optional[Direction]=None):
        Magie_attaque_corp_a_corp_dirigee.__init__(self,skill,agissant,direction,gain_xp_laser[niveau-1],cout_pm_laser[niveau-1],portee_laser[niveau-1],degats_laser[niveau-1],TERRE,"R__T___",latence_laser[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_LASER

    def get_titre(self,observation=0):
        return f"Magie de laser (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés en ligne droite et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_laser[self.niveau-1]}",f"Portee de l'attaque : {portee_laser[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_brasier(Magie_attaque_corp_a_corp):
    """La magie qui crée une attaque de brasier."""
    nom = "magie brasier"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie_attaque_corp_a_corp.__init__(self,skill,agissant,gain_xp_brasier[niveau-1],cout_pm_brasier[niveau-1],portee_brasier[niveau-1],degats_brasier[niveau-1],FEU,"proximité",latence_brasier[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation=0):
        return f"Magie de brasier (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité.",f"Coût : {self.cout}",f"Degats : {degats_brasier[self.niveau-1]}",f"Portee de l'attaque : {portee_brasier[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_avalanche(Magie_attaque_corp_a_corp_dirigee):
    """La magie qui crée une attaque d'avalanche."""
    nom = "magie avalanche"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,direction:Optional[Direction]=None):
        Magie_attaque_corp_a_corp_dirigee.__init__(self,skill,agissant,direction,gain_xp_avalanche[niveau-1],cout_pm_avalanche[niveau-1],portee_avalanche[niveau-1],degats_avalanche[niveau-1],TERRE,"S__S_Pb",latence_avalanche[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation=0):
        return f"Magie d'avalanche (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants devant et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_avalanche[self.niveau-1]}",f"Portee de l'attaque : {portee_avalanche[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_purification(Magie_attaque_corp_a_corp):
    """La magie qui crée un effet de purification sur un agissant."""
    nom = "magie purification"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie_attaque_corp_a_corp.__init__(self,skill,agissant,gain_xp_purification[niveau-1],cout_pm_purification[niveau-1],portee_purification[niveau-1],degats_purification[niveau-1],-1,"proximité",latence_purification[niveau-1],niveau)

    def action(self):
        for case in self.agissant.controleur.get_pos_touches(self.agissant.position,self.portee,self.propagation,responsable=self.agissant):
            self.agissant.controleur.case_from_position(case).effets.append(Attaque_lumineuse_case(self.agissant,self.degats))

    def get_image(self):
        return SKIN_MAGIE_PURIFICATION

    def get_titre(self,observation=0):
        return f"Magie de purification (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de purification","Inflige des dégats aux agissants à proximité du lanceur.","Les dégats sont inversement proportionnels à l'affinité à l'ombre.","La purification n'est pas une attaque, mais se comporte comme telle.",f"Coût : {self.cout}",f"Dégats : {degats_purification[self.niveau-1]}",f"Portée : {portee_purification[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Effet.Attaque.Attaque import Attaque_case,Attaque_lumineuse_case
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Constantes import *
from Affichage.Skins.Skins import *