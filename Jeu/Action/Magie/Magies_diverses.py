from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Systeme.Skill.Actif import Actif

# Imports des classes parentes
from Jeu.Action.Action import Non_repetable
from Jeu.Action.Magie.Magie import Magie, Cible_agissant, Cible_agissants, Cible_cases

class Magie_blizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_blizzard[niveau-1],cout_pm_blizzard[niveau-1],latence_blizzard[niveau-1],niveau)

    def action(self):
        cases = self.agissant.controleur.get_cases_touches(self.agissant.position,portee_blizzard[self.niveau-1])
        for case in cases:
            case.effets.append(Blizzard(self.niveau))

    def get_image(self):
        return SKIN_MAGIE_BLIZZARD

    def get_titre(self,observation=0):
        return f"Magie de blizzard (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de blizzard","Affecte les cases à proximité du lanceur.","Le blizzard augmente à chaque tour le latence de l'agissant sur la case. Si la vitesse de l'agissant n'est pas suffisante pour compenser la latence supplémentaire, l'agissant sur la case est immobilisé. Le lanceur est affecté par le blizzard.",f"Coût : {self.cout}",f"Portee de la magie : {portee_blizzard[self.niveau-1]}",f"Latence supplémentaire : {gain_latence_blizzard[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_obscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_obscurite[niveau-1],cout_pm_obscurite[niveau-1],latence_obscurite[niveau-1],niveau)

    def action(self):
        cases = self.agissant.controleur.get_cases_touches(self.agissant.position,portee_obscurite[self.niveau-1])
        for case in cases:
            case.effets.append(Obscurite(self.niveau))

    def get_image(self):
        return SKIN_MAGIE_OBSCURITE

    def get_titre(self,observation=0):
        return f"Magie d'obscurité (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'obscurité","Affecte les cases à proximité du lanceur.","L'obscurité augmente l'opacité des cases, rendant plus difficile de voir au travers.",f"Coût : {self.cout}",f"Portee de la magie : {portee_obscurite[self.niveau-1]}",f"Opacité supplémentaire : {gain_opacite_obscurite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_instakill(Cible_agissant, Non_repetable):
    """La magie qui crée un effet d'instakill sur un agissant."""
    nom = "magie instakill"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,cible:Optional[Agissant]=None):
        Magie.__init__(self,skill,agissant,gain_xp_instakill[niveau-1],cout_pm_instakill[niveau-1],latence_instakill[niveau-1],niveau)
        Cible_agissant.__init__(self,cible)

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(Instakill(self.agissant,self.agissant.priorite - superiorite_instakill[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_INSTAKILL

    def get_titre(self,observation=0):
        return f"Magie de mort instantannée (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de mort instantannée","Affecte un agissant en vue du lanceur.","L'agissant meurt instantannément. S'il est immortel, ses PVs et ses PMs sont réduits à 0.","Le sort peut échouer si la priorité de l'agissant est trop élevée comparée à celle du lanceur.",f"Coût : {self.cout}",f"Différence de priorité : {superiorite_instakill[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_protection_sacree(Cible_agissants):
    """La magie qui crée un effet de protection sacrée sur des agissants."""
    nom = "magie protection sacrée"
    def __init__(self,skill:Actif,agissant:Agissant,cible:List[Agissant],niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_protection_sacree[niveau-1],cout_pm_protection_sacree[niveau-1],latence_protection_sacree[niveau-1],niveau)
        Cible_agissants.__init__(self,cible)

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            for cible in self.cible:
                cible.effets.append(Protection_sacree(duree_protection_sacree[self.niveau-1],pv_protection_sacree[self.niveau-1])) #Ajouter une direction ?

    def get_image(self):
        return SKIN_MAGIE_PROTECTION_SACREE

    def get_titre(self,observation=0):
        return f"Magie de protection sacrée (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de protection","Bloque les dégats des attaques entrantes jusqu'à une certaine somme.","Les dégats d'ombre sont plus affectés.",f"Coût : {self.cout}",f"Dégats absorbables : {pv_protection_sacree[self.niveau-1]}",f"Durée : {duree_protection_sacree[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_teleportation(Cible_cases, Non_repetable):
    """La magie qui téléporte des entitées."""
    nom = "magie téléportation"
    def __init__(self,skill:Actif,agissant:Agissant,cases:List[Position],niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_teleportation[niveau-1],cout_pm_teleportation[niveau-1],latence_teleportation[niveau-1],niveau)
        Cible_cases.__init__(self,cases)

    def action(self):
        if self.cible == []:
            self.interrompt()
        else:
            for i in range(len(self.cible)):
                for agissant in self.agissant.controleur.trouve_occupants(self.cible[i]):
                    agissant.effets.append(Teleport(self.cible[i-1]))

    def get_image(self):
        return SKIN_MAGIE_TELEPORTATION

    def get_titre(self,observation=0):
        return f"Magie de téléportation (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de téléportation","Affecte les entitées sur les cases sélectionnées.","Les entitées de chaque case sont déplacées sur la case précédente. Les entitées de la première case sont envoyées sur la dernière case.",f"Coût : {self.cout}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Effet.Effets_mouvement.Deplacements import Teleport
from Jeu.Effet.Effets_divers import Instakill, Blizzard, Obscurite
from Jeu.Effet.Effets_protection import Protection_sacree
from Affichage.Skins.Skins import SKIN_MAGIE_INSTAKILL, SKIN_MAGIE_PROTECTION_SACREE, SKIN_MAGIE_TELEPORTATION, SKIN_MAGIE_BLIZZARD, SKIN_MAGIE_OBSCURITE