from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position, ABSENT
    from Jeu.Systeme.Classe import Skill_intrasec

# Imports des classes parentes
from Jeu.Action.Magie.Magie import Magie,Cible_case,Magies_offensives

class Magie_volcan(Cible_case,Magies_offensives):
    """La magie qui crée une attaque de feu à un autre endroit."""
    nom = "magie volcan"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_volcan[niveau-1],cout_pm_volcan[niveau-1],latence_volcan[niveau-1])
        self.niveau = niveau
        self.cible:Position = ABSENT
        self.temps = 10000

    def action(self):
        self.agissant.effets.append(Attaque_decentree_delayee(self.cible,delai_volcan[self.niveau-1],self.agissant,degats_volcan[self.niveau-1],FEU,"distance",portee_volcan[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation=0):
        return f"Magie de volcan (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout}",f"Dégats : {degats_volcan[self.niveau-1]}",f"Portée : {portee_volcan[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_secousse(Cible_case,Magies_offensives):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie secousse"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_secousse[niveau-1],cout_pm_secousse[niveau-1],latence_secousse[niveau-1])
        self.niveau = niveau
        self.cible:Position = ABSENT
        self.temps = 10000

    def action(self):
        self.agissant.effets.append(Attaque_decentree_delayee(self.cible,delai_secousse[self.niveau-1],self.agissant,degats_secousse[self.niveau-1],TERRE,"distance",portee_secousse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation=0):
        return f"Magie de secousse (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout}",f"Dégats : {degats_secousse[self.niveau-1]}",f"Portée : {portee_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_petite_secousse(Cible_case,Magies_offensives):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie petite secousse"
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_petite_secousse[niveau-1],cout_pm_petite_secousse[niveau-1],latence_petite_secousse[niveau-1])
        self.niveau = niveau
        self.cible:Position = ABSENT
        self.temps = 10000

    def action(self):
        self.agissant.effets.append(Attaque_decentree_delayee(self.cible,delai_petite_secousse[self.niveau-1],self.agissant,degats_petite_secousse[self.niveau-1],TERRE,"distance",portee_petite_secousse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation=0):
        return f"Magie de petite secousse (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout}",f"Dégats : {degats_petite_secousse[self.niveau-1]}",f"Portée : {portee_petite_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Effet.Attaque.Attaque import Attaque_decentree_delayee
from Jeu.Systeme.Constantes_magies.Magies import *
from Affichage.Skins.Skins import *
from Jeu.Constantes import *
