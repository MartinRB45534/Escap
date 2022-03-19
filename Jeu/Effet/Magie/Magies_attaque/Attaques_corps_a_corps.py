from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Attaque.Attaque import *
from Jeu.Effet.Effets_divers import *

class Magie_laser(Magie_dirigee):
    """La magie qui crée une attaque de laser."""
    nom = "magie laser"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_laser[niveau-1]
        self.cout_pm = cout_pm_laser[niveau-1]
        self.latence = latence_laser[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_laser[self.niveau-1],TERRE,'proximité',portee_laser[self.niveau-1],"R__T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_LASER

    def get_titre(self,observation):
        return f"Magie de laser (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés en ligne droite et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_laser[self.niveau-1]}",f"Portee de l'attaque : {portee_laser[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_brasier(Magie):
    """La magie qui crée une attaque de brasier."""
    nom = "magie brasier"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_brasier[niveau-1]
        self.cout_pm = cout_pm_brasier[niveau-1]
        self.latence = latence_brasier[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_brasier[self.niveau-1],FEU,"proximité",portee_brasier[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation):
        return f"Magie de brasier (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_brasier[self.niveau-1]}",f"Portee de l'attaque : {portee_brasier[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_avalanche(Magie_dirigee):
    """La magie qui crée une attaque d'avalanche."""
    nom = "magie avalanche"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_avalanche[niveau-1]
        self.cout_pm = cout_pm_avalanche[niveau-1]
        self.latence = latence_avalanche[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_avalanche[self.niveau-1],TERRE,"proximité",portee_avalanche[self.niveau-1],"S__S_Pb",self.direction))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation):
        return f"Magie d'avalanche (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants devant et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_avalanche[self.niveau-1]}",f"Portee de l'attaque : {portee_avalanche[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_purification(Magie):
    """La magie qui crée un effet de purification sur un agissant."""
    nom = "magie purification"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_purification[niveau-1]
        self.cout_pm = cout_pm_purification[niveau-1]
        self.latence = latence_purification[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Purification_lumineuse(porteur.ID,degats_purification[self.niveau-1],portee_purification[self.niveau-1])) #Ajouter une direction ?

    def get_image(self):
        return SKIN_MAGIE_PURIFICATION

    def get_titre(self,observation):
        return f"Magie de purification (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de purification","Inflige des dégats aux agissants à proximité du lanceur.","Les dégats sont inversement proportionnels à l'affinité à l'ombre.","La purification n'est pas une attaque, mais se comporte comme telle.",f"Coût : {self.cout_pm}",f"Dégats : {degats_purification[self.niveau-1]}",f"Portée : {portee_purification[self.niveau-1]}",f"Latence : {self.latence}"]
