from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Systeme.Skill.Actif import Actif
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Old_Jeu.Action.Magie.Magie import Magie, Magie_dirigee, Magies_offensives

class Magie_attaque_contact(Magie_dirigee,Magies_offensives):
    """Les magies qui créent une attaque au contact."""
    def __init__(self,skill:Actif,agissant:Agissant,direction:Optional[Direction],gain_xp:float,cout_pm:float,portee:float,degats:float,element:int,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.portee = portee
        self.degats = degats
        self.element = element
        self.direction = direction

    def action(self):
        if self.direction is None:
            self.interrompt()
        else:
            for case in self.agissant.controleur.get_pos_touches(self.agissant.position,self.portee,"Sd_T___",self.direction,responsable=self.agissant):
                self.agissant.controleur.case_from_position(case).effets.append(Attaque_case(self.agissant,self.degats,self.element,"contact",self.direction))

class Magie_poing_magique(Magie_attaque_contact): #À modifier selon l'espèce qui l'utilise
    """La magie qui crée une attaque de poing magique."""
    nom = "magie poing magique"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,direction:Optional[Direction]=None):
        Magie_attaque_contact.__init__(self,skill,agissant,direction,gain_xp_poing_magique[niveau-1],cout_pm_poing_magique[niveau-1],portee_poing_magique[niveau-1],degats_poing_magique[niveau-1],TERRE,latence_poing_magique[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation=0):
        return f"Magie de poing magique (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_poing_magique[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_magique[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_ardent(Magie_attaque_contact): #L'attaque de mélée de la bombe atomique
    """La magie qui crée une attaque de poing ardent."""
    nom = "magie poing ardent"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,direction:Optional[Direction]=None):
        Magie_attaque_contact.__init__(self,skill,agissant,direction,gain_xp_poing_ardent[niveau-1],cout_pm_poing_ardent[niveau-1],portee_poing_ardent[niveau-1],degats_poing_ardent[niveau-1],FEU,latence_poing_ardent[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation=0):
        return f"Magie de poing ardent (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_poing_ardent[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_ardent[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_sombre(Magie_attaque_contact):
    """La magie qui crée une attaque de poing sombre."""
    nom = "magie poing sombre"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,direction:Optional[Direction]=None):
        Magie_attaque_contact.__init__(self,skill,agissant,direction,gain_xp_poing_sombre[niveau-1],cout_pm_poing_sombre[niveau-1],portee_poing_sombre[niveau-1],degats_poing_sombre[niveau-1],TERRE,latence_poing_sombre[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation=0):
        return f"Magie de poing sombre (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout}",f"Degats : {degats_poing_sombre[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_sombre[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Old_Jeu.Effet.Attaque.Attaque import Attaque_case
from Old_Jeu.Systeme.Constantes_magies.Magies import *
from Old_Jeu.Constantes import *
from Old_Affichage.Skins.Skins import SKIN_MAGIE_POING_MAGIQUE