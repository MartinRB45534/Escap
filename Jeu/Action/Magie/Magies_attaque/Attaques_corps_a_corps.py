from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Systeme.Classe import Skill_intrasec

# Imports des classes parentes
from Jeu.Action.Magie.Magie import Magie,Magie_dirigee,Magies_offensives

class Magie_laser(Magie_dirigee,Magies_offensives):
    """La magie qui crée une attaque de laser."""
    nom = "magie laser"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_laser[niveau-1],cout_pm_laser[niveau-1],latence_laser[niveau-1])
        self.niveau = niveau
        self.direction = None
        self.temps = 10000

    def action(self):
        self.agissant.effets.append(Attaque_magique(self.agissant,degats_laser[self.niveau-1],TERRE,'proximité',portee_laser[self.niveau-1],"R__T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_LASER

    def get_titre(self,observation=0):
        return f"Magie de laser (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés en ligne droite et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_laser[self.niveau-1]}",f"Portee de l'attaque : {portee_laser[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_brasier(Magies_offensives):
    """La magie qui crée une attaque de brasier."""
    nom = "magie brasier"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_brasier[niveau-1],cout_pm_brasier[niveau-1],latence_brasier[niveau-1])
        self.niveau = niveau

    def action(self):
        self.agissant.effets.append(Attaque_magique(self.agissant,degats_brasier[self.niveau-1],FEU,"proximité",portee_brasier[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation=0):
        return f"Magie de brasier (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité.",f"Coût : {self.cout}",f"Degats : {degats_brasier[self.niveau-1]}",f"Portee de l'attaque : {portee_brasier[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_avalanche(Magie_dirigee,Magies_offensives):
    """La magie qui crée une attaque d'avalanche."""
    nom = "magie avalanche"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_avalanche[niveau-1],cout_pm_avalanche[niveau-1],latence_avalanche[niveau-1])
        self.niveau = niveau
        self.direction = None
        self.temps = 10000

    def action(self):
        self.agissant.effets.append(Attaque_magique(self.agissant,degats_avalanche[self.niveau-1],TERRE,"proximité",portee_avalanche[self.niveau-1],"S__S_Pb",self.direction))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation=0):
        return f"Magie d'avalanche (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants devant et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_avalanche[self.niveau-1]}",f"Portee de l'attaque : {portee_avalanche[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_purification(Magies_offensives):
    """La magie qui crée un effet de purification sur un agissant."""
    nom = "magie purification"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_purification[niveau-1],cout_pm_purification[niveau-1],latence_purification[niveau-1])
        self.niveau = niveau

    def action(self):
        self.agissant.effets.append(Purification_lumineuse(self.agissant,degats_purification[self.niveau-1],portee_purification[self.niveau-1])) #Ajouter une direction ?

    def get_image(self):
        return SKIN_MAGIE_PURIFICATION

    def get_titre(self,observation=0):
        return f"Magie de purification (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de purification","Inflige des dégats aux agissants à proximité du lanceur.","Les dégats sont inversement proportionnels à l'affinité à l'ombre.","La purification n'est pas une attaque, mais se comporte comme telle.",f"Coût : {self.cout}",f"Dégats : {degats_purification[self.niveau-1]}",f"Portée : {portee_purification[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Effet.Attaque.Attaque import Attaque_magique, Purification_lumineuse
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Constantes import *
from Affichage.Skins.Skins import *