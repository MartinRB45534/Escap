from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Sante.Soins import *
from Jeu.Effet.Sante.Resurection import *
from Jeu.Effet.Sante.Reanimation import *
from Jeu.Entitee.Item.Item import *

class Magie_soin(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie soin"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin[niveau-1]
        self.cout_pm = cout_pm_soin[niveau-1]
        self.latence = latence_soin[niveau-1]
        self.gain_pv = gain_pv_soin[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        agissant_cible = lanceur.controleur[self.cible]
        agissant_cible.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_SOIN

    def get_titre(self,observation=0):
        return f"Magie de soin (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de soin","Elle affecte un agissant à portée de vue du lanceur.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_multi_soin(Cible_agissant,Multi_cible):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""
    nom = "magie multi soin"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_multi_soin[niveau-1]
        self.cout_pm = cout_pm_multi_soin[niveau-1]
        self.latence = latence_multi_soin[niveau-1]
        self.gain_pv = gain_pv_multi_soin[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        for cible in self.cible:
            agissant_cible = lanceur.controleur[cible]
            agissant_cible.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_SOIN

    def get_titre(self,observation=0):
        return f"Magie de multi-soin (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de soin","Elle affecte un ou plusieurs agissants à portée de vue du lanceur.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_soin_superieur(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie_soin_superieur"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_superieur[niveau-1]
        self.cout_pm = cout_pm_soin_superieur[niveau-1]
        self.latence = latence_soin_superieur[niveau-1]
        self.gain_pv = gain_pv_soin_superieur[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        agissant_cible = lanceur.controleur[self.cible]
        agissant_cible.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_SOIN_SUPERIEUR

    def get_titre(self,observation=0):
        return f"Magie de soin avancée (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de soin","Elle affecte un agissant à portée de vue du lanceur.","Plus efficace et moins couteuse que la version classique.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_soin_de_zone(Cible_case):
    """La magie qui invoque un effet de soin sur une zone."""
    nom = "magie zone de soin"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_zone[niveau-1]
        self.cout_pm = cout_pm_soin_zone[niveau-1]
        self.latence = latence_soin_zone[niveau-1]
        self.gain_pv = gain_pv_soin_zone[niveau-1]
        self.portee = portee_soin_zone[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        poss = lanceur.controleur.get_pos_touches(self.cible,self.portee)
        for pos in poss:
            lanceur.controleur[pos].effets.append(Soin_case(self.gain_pv,lanceur.ID))

    def get_image(self):
        return SKIN_MAGIE_SOIN_ZONE

    def get_titre(self,observation=0):
        return f"Magie de soin de zone (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de soin","Elle affecte une zone à proximité du lanceur.","La zone de soin peut s'étendre au-delà de la vue du lanceur.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_auto_soin(Magie):
    """La magie qui invoque un effet de soin sur son lanceur."""
    nom = "magie auto soin"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_auto[niveau-1]
        self.cout_pm = cout_pm_soin_auto[niveau-1]
        self.latence = latence_soin_auto[niveau-1]
        self.gain_pv = gain_pv_soin_auto[niveau-1]
        self.affiche = True

    def action(self,lanceur):
        lanceur.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_AUTO_SOIN

    def get_titre(self,observation=0):
        return f"Magie d'auto-soin (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de soin","Elle affecte uniquement le lanceur.","Plus efficace et moins couteuse que la version classique.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]



class Magie_resurection(Magie):
    """La magie qui invoque un effet de resurection."""
    nom = "magie resurection"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_resurection[niveau-1]
        self.cout_pm = cout_pm_resurection[niveau-1]
        self.latence = latence_resurection[niveau-1]
        self.affiche = True

    def action(self,lanceur):
        ID_cadavre = lanceur.inventaire.get_item_courant()
        cadavre = lanceur.controleur[ID_cadavre]
        if cadavre.get_classe() == Cadavre:
            lanceur.inventaire.drop(lanceur.position)
            cadavre.effets.append(Resurection())

    def get_image(self):
        return SKIN_MAGIE_RESURECTION

    def get_titre(self,observation=0):
        return f"Magie de résurection (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de résurection","Elle ramène un cadavre à la vie.","Le cadavre doit être dans l'inventaire du lanceur.","L'agissant rescussité récupère l'intégralité de ses PVs, mais pas ses PMs. Il ne récupère pas son équippement, son argent ou ses effets, même permanents. Il ne rejoint pas le responsable de la resurection.",f"Coût : {self.cout_pm} PMs",f"Latence : {self.latence}"]

class Magie_reanimation_de_zone(Cible_case,Portee_limitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    nom = "magie reanimation"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_reanimation[niveau-1]
        self.cout_pm = cout_pm_reanimation[niveau-1]
        self.latence = latence_reanimation[niveau-1]
        self.taux_pv = taux_pv_reanimation[niveau-1]
        self.portee = portee_reanimation[niveau-1]
        self.portee_limite = portee_limite_reanimation[niveau-1]
        self.superiorite = superiorite_reanimation[niveau-1]
        self.temps = 10000
        self.cible = None
        self.affiche = True

    def action(self,porteur):
        cadavres = porteur.controleur.get_cadavres_touches(self.cible,self.portee)
        esprit = porteur.controleur.get_esprit(porteur.get_esprit())
        for cadavre in cadavres:
            if cadavre.get_priorite()+self.superiorite < porteur.get_priorite():
                cadavre.effets.append(Reanimation(self.taux_pv,esprit))

    def get_image(self):
        return SKIN_MAGIE_REANIMATION_ZONE

    def get_titre(self,observation=0):
        return f"Magie de réanimation (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de réanimation","Elle affecte tous les cadavres dans une zone à proximité du lanceur.","L'agissant rescussité récupère une partie de ses PVs, mais pas ses PMs. Il ne récupère pas son équippement, son argent ou ses effets, même permanents. Il rejoint le responsable de la réanimation. La réanimation échoue si la priorité de l'agissant est trop haut par rapport au responsable.",f"Coût : {self.cout_pm} PMs",f"PVs rendus : {self.taux_pv} des PVs max",f"Différence de priorité : {self.superiorite}",f"Portée de la zone de réanimation : {self.portee}",f"Portée du centre de la zone (par rapport au joueur) : {self.portee_limite}",f"Latence : {self.latence}"]
