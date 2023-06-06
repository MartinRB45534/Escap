from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position, ABSENT
    from Old_Jeu.Systeme.Skill.Actif import Actif
    from Old_Jeu.Effet.Attaque.Attaque import Attaque_case_delayee

# Imports des classes parentes
from Old_Jeu.Action.Magie.Magie import Magie,Cible_case,Magies_offensives

class Magie_attaque_distance(Cible_case,Magies_offensives):
    """Les magies qui créent une attaque à distance."""
    def __init__(self,skill:Actif,agissant:Agissant,cible:Optional[Position],gain_xp:float,cout_pm:float,portee:float,degats:float,element:int,latence:float,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence,niveau)
        self.cible = cible
        self.effets:List[Attaque_case_delayee] = []
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self):
        if self.cible is None:
            self.interrompt()
        elif self.effets == []:
            for case in self.agissant.controleur.get_pos_touches(self.cible,self.portee,responsable=self.agissant):
                effet = Attaque_case_delayee(self.agissant,self.degats,self.element,"distance")
                self.agissant.controleur.case_from_position(case).effets.append(effet)
                self.effets.append(effet)
        else:
            for effet in self.effets:
                effet.phase = "en cours"

class Magie_volcan(Magie_attaque_distance):
    """La magie qui crée une attaque de feu à un autre endroit."""
    nom = "magie volcan"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,cible:Optional[Position]=None):
        Magie_attaque_distance.__init__(self,skill,agissant,cible,gain_xp_volcan[niveau-1],cout_pm_volcan[niveau-1],portee_volcan[niveau-1],degats_volcan[niveau-1],FEU,latence_volcan[niveau-1],niveau)
        
    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation=0):
        return f"Magie de volcan (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout}",f"Dégats : {degats_volcan[self.niveau-1]}",f"Portée : {portee_volcan[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_secousse(Magie_attaque_distance):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie secousse"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,cible:Optional[Position]=None):
        Magie_attaque_distance.__init__(self,skill,agissant,cible,gain_xp_secousse[niveau-1],cout_pm_secousse[niveau-1],portee_secousse[niveau-1],degats_secousse[niveau-1],TERRE,latence_secousse[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation=0):
        return f"Magie de secousse (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout}",f"Dégats : {degats_secousse[self.niveau-1]}",f"Portée : {portee_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_petite_secousse(Magie_attaque_distance):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie petite secousse"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,cible:Optional[Position]=None):
        Magie_attaque_distance.__init__(self,skill,agissant,cible,gain_xp_petite_secousse[niveau-1],cout_pm_petite_secousse[niveau-1],portee_petite_secousse[niveau-1],degats_petite_secousse[niveau-1],TERRE,latence_petite_secousse[niveau-1],niveau)

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation=0):
        return f"Magie de petite secousse (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout}",f"Dégats : {degats_petite_secousse[self.niveau-1]}",f"Portée : {portee_petite_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Old_Jeu.Systeme.Constantes_magies.Magies import *
from Old_Affichage.Skins.Skins import *
from Old_Jeu.Constantes import *
