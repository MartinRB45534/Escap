from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Effets_divers import *

class Magie_dopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_dopage[niveau-1]
        self.cout_pm = cout_pm_dopage[niveau-1]
        self.latence = latence_dopage[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Dopage(porteur.ID,taux_dopage[self.niveau-1],duree_dopage[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation=0):
        return f"Magie de dopage (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de boost","Affecte le lanceur.","Les dégats de la prochaine attaque du lanceur sont augentés.",f"Coût : {self.cout_pm}",f"Taux de dégats : {taux_dopage[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_boost(Cible_agissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    nom = "magie boost"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_boost[niveau-1]
        self.cout_pm = cout_pm_boost[niveau-1]
        self.latence = latence_boost[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur[self.cible].effets.append(Dopage(porteur.ID,taux_boost[self.niveau-1],duree_boost[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation=0):
        return f"Magie de boost (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de boost","Affecte un agissant en vue du lanceur.","Les dégats de la prochaine attaque de l'agissant sont augentés.",f"Coût : {self.cout_pm}",f"Taux de dégats : {taux_boost[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_multi_boost(Cible_agissant,Multi_cible):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    nom = "magie multi boost"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_multi_boost[niveau-1]
        self.cout_pm = cout_pm_multi_boost[niveau-1]
        self.latence = latence_multi_boost[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        for cible in self.cible:
            porteur.controleur.entitees[cible].effets.append(Dopage(porteur.ID,taux_multi_boost[self.niveau-1],duree_multi_boost[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation=0):
        return f"Magie de multi-boost (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de boost","Affecte un ou plusieurs agissants en vue du lanceur.","Les dégats de la prochaine attaque des agissants sont augentés.",f"Coût : {self.cout_pm}",f"Taux de dégats : {taux_multi_boost[self.niveau-1]}",f"Latence : {self.latence}"]
