from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Systeme.Classe import Skill_intrasec

# Imports des classes parentes
from Jeu.Action.Magie.Magie import Magie, Cible_agissant, Multi_cible

class Magie_dopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_dopage[niveau-1],cout_pm_dopage[niveau-1],latence_dopage[niveau-1],niveau)

    def action(self):
        self.agissant.effets.append(Dopage(self.agissant,taux_dopage[self.niveau-1],duree_dopage[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation=0):
        return f"Magie de dopage (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de boost","Affecte le lanceur.","Les dégats de la prochaine attaque du lanceur sont augentés.",f"Coût : {self.cout}",f"Taux de dégats : {taux_dopage[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_boost(Cible_agissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    nom = "magie boost"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int,cible:Optional[Agissant]=None):
        Magie.__init__(self,skill,agissant,gain_xp_boost[niveau-1],cout_pm_boost[niveau-1],latence_boost[niveau-1],niveau)
        self.cible:Optional[Agissant] = cible

    def action(self):
        if self.cible is None:
            self.interrompt()
        else:
            self.cible.effets.append(Dopage(self.agissant,taux_boost[self.niveau-1],duree_boost[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation=0):
        return f"Magie de boost (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de boost","Affecte un agissant en vue du lanceur.","Les dégats de la prochaine attaque de l'agissant sont augentés.",f"Coût : {self.cout}",f"Taux de dégats : {taux_boost[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_multi_boost(Cible_agissant,Multi_cible):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    nom = "magie multi boost"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_multi_boost[niveau-1],cout_pm_multi_boost[niveau-1],latence_multi_boost[niveau-1],niveau)
        self.cible:List[Agissant] = []

    def action(self):
        for cible in self.cible:
            cible.effets.append(Dopage(self.agissant,taux_multi_boost[self.niveau-1],duree_multi_boost[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation=0):
        return f"Magie de multi-boost (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de boost","Affecte un ou plusieurs agissants en vue du lanceur.","Les dégats de la prochaine attaque des agissants sont augentés.",f"Coût : {self.cout}",f"Taux de dégats : {taux_multi_boost[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Effet.Effets_divers import Dopage
from Jeu.Systeme.Constantes_magies.Magies import *
from Affichage.Skins.Skins import SKIN_MAGIE_DOPAGE