from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Attaque.Attaque import *

class Magie_poing_magique(Magie_dirigee,Magies_offensives): #À modifier selon l'espèce qui l'utilise
    """La magie qui crée une attaque de poing magique."""
    nom = "magie poing magique"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_magique[niveau-1]
        self.cout_pm = cout_pm_poing_magique[niveau-1]
        self.latence = latence_poing_magique[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_poing_magique[self.niveau-1],TERRE,"contact",portee_poing_magique[self.niveau-1],"Sd_T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation):
        return f"Magie de poing magique (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_poing_magique[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_magique[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_ardent(Magie_dirigee,Magies_offensives): #L'attaque de mélée de la bombe atomique
    """La magie qui crée une attaque de poing ardent."""
    nom = "magie poing ardent"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_ardent[niveau-1]
        self.cout_pm = cout_pm_poing_ardent[niveau-1]
        self.latence = latence_poing_ardent[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_poing_ardent[self.niveau-1],FEU,"contact",portee_poing_ardent[self.niveau-1],"Sd_T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation):
        return f"Magie de poing ardent (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_poing_ardent[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_ardent[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_sombre(Magie_dirigee,Magies_offensives):
    """La magie qui crée une attaque de poing sombre."""
    nom = "magie poing sombre"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_sombre[niveau-1]
        self.cout_pm = cout_pm_poing_sombre[niveau-1]
        self.latence = latence_poing_sombre[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_poing_sombre[self.niveau-1],OMBRE,"contact",portee_poing_sombre[self.niveau-1],"Sd_T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation):
        return f"Magie de poing sombre (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_poing_sombre[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_sombre[self.niveau-1]}",f"Latence : {self.latence}"]
