from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Attaque.Attaque import *

class Magie_volcan(Cible_case,Magies_offensives):
    """La magie qui crée une attaque de feu à un autre endroit."""
    nom = "magie volcan"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_volcan[niveau-1]
        self.cout_pm = cout_pm_volcan[niveau-1]
        self.latence = latence_volcan[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_decentree_delayee(self.cible,delai_volcan[self.niveau-1],porteur.ID,degats_volcan[self.niveau-1],FEU,"distance",portee_volcan[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation):
        return f"Magie de volcan (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout_pm}",f"Dégats : {degats_volcan[self.niveau-1]}",f"Portée : {portee_volcan[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_secousse(Cible_case,Magies_offensives):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie secousse"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_secousse[niveau-1]
        self.cout_pm = cout_pm_secousse[niveau-1]
        self.latence = latence_secousse[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_decentree_delayee(self.cible,delai_secousse[self.niveau-1],porteur.ID,degats_secousse[self.niveau-1],TERRE,"distance",portee_secousse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation):
        return f"Magie de secousse (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout_pm}",f"Dégats : {degats_secousse[self.niveau-1]}",f"Portée : {portee_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_petite_secousse(Cible_case,Magies_offensives):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie petite secousse"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_petite_secousse[niveau-1]
        self.cout_pm = cout_pm_petite_secousse[niveau-1]
        self.latence = latence_petite_secousse[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_decentree_delayee(self.cible,delai_petite_secousse[self.niveau-1],porteur.ID,degats_petite_secousse[self.niveau-1],TERRE,"distance",portee_petite_secousse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation):
        return f"Magie de petite secousse (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout_pm}",f"Dégats : {degats_petite_secousse[self.niveau-1]}",f"Portée : {portee_petite_secousse[self.niveau-1]}",f"Latence : {self.latence}"]
