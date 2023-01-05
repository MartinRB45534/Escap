from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Effets_divers import *
from Jeu.Effet.Effets_protection import *

class Magie_blizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_blizzard[niveau-1]
        self.cout_pm = cout_pm_blizzard[niveau-1]
        self.latence = latence_blizzard[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,portee_blizzard[self.niveau-1])
        for case in cases:
            case.effets.append(Blizzard(self.niveau))

    def get_image(self):
        return SKIN_MAGIE_BLIZZARD

    def get_titre(self,observation=0):
        return f"Magie de blizzard (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de blizzard","Affecte les cases à proximité du lanceur.","Le blizzard augmente à chaque tour le latence de l'agissant sur la case. Si la vitesse de l'agissant n'est pas suffisante pour compenser la latence supplémentaire, l'agissant sur la case est immobilisé. Le lanceur est affecté par le blizzard.",f"Coût : {self.cout_pm}",f"Portee de la magie : {portee_blizzard[self.niveau-1]}",f"Latence supplémentaire : {gain_latence_blizzard[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_obscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_obscurite[niveau-1]
        self.cout_pm = cout_pm_obscurite[niveau-1]
        self.latence = latence_obscurite[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,portee_obscurite[self.niveau-1])
        for case in cases:
            case.effets.append(Obscurite(self.niveau))

    def get_image(self):
        return SKIN_MAGIE_OBSCURITE

    def get_titre(self,observation=0):
        return f"Magie d'obscurité (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'obscurité","Affecte les cases à proximité du lanceur.","L'obscurité augmente l'opacité des cases, rendant plus difficile de voir au travers.",f"Coût : {self.cout_pm}",f"Portee de la magie : {portee_obscurite[self.niveau-1]}",f"Opacité supplémentaire : {gain_opacite_obscurite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_instakill(Magie_cible):
    """La magie qui crée un effet d'instakill sur un agissant."""
    nom = "magie instakill"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_instakill[niveau-1]
        self.cout_pm = cout_pm_instakill[niveau-1]
        self.latence = latence_instakill[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur[self.cible].effets.append(Instakill(porteur.ID,porteur.priorite - superiorite_instakill[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_INSTAKILL

    def get_titre(self,observation=0):
        return f"Magie de mort instantannée (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de mort instantannée","Affecte un agissant en vue du lanceur.","L'agissant meurt instantannément. S'il est immortel, ses PVs et ses PMs sont réduits à 0.","Le sort peut échouer si la priorité de l'agissant est trop élevée comparée à celle du lanceur.",f"Coût : {self.cout_pm}",f"Différence de priorité : {superiorite_instakill[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_protection_sacree(Multi_cible,Cible_agissant):
    """La magie qui crée un effet de protection sacrée sur des agissants."""
    nom = "magie protection sacrée"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_protection_sacree[niveau-1]
        self.cout_pm = cout_pm_protection_sacree[niveau-1]
        self.latence = latence_protection_sacree[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        for ID in self.cible:
            porteur.controleur[ID].effets.append(Protection_sacree(duree_protection_sacree[self.niveau-1],pv_protection_sacree[self.niveau-1])) #Ajouter une direction ?

    def get_image(self):
        return SKIN_MAGIE_PROTECTION_SACREE

    def get_titre(self,observation=0):
        return f"Magie de protection sacrée (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de protection","Bloque les dégats des attaques entrantes jusqu'à une certaine somme.","Les dégats d'ombre sont plus affectés.",f"Coût : {self.cout_pm}",f"Dégats absorbables : {pv_protection_sacree[self.niveau-1]}",f"Durée : {duree_protection_sacree[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_teleportation(Multi_cible,Cible_case):
    """La magie qui téléporte des entitées."""
    nom = "magie téléportation"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_teleportation[niveau-1]
        self.cout_pm = cout_pm_teleportation[niveau-1]
        self.latence = latence_teleportation[niveau-1]
        self.cible = None
        self.temps = 100000
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        for i in range(len(self.cible)):
            for ID in porteur.controleur.trouve_occupants(self.cible[i]):
                porteur.controleur[ID].effets.append(Teleportation(self.cible[i-1]))

    def get_image(self):
        return SKIN_MAGIE_TELEPORTATION

    def get_titre(self,observation=0):
        return f"Magie de téléportation (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de téléportation","Affecte les entitées sur les cases sélectionnées.","Les entitées de chaque case sont déplacées sur la case précédente. Les entitées de la première case sont envoyées sur la dernière case.",f"Coût : {self.cout_pm}",f"Latence : {self.latence}"]
