from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Agissant import Agissant
    from ...Labyrinthe.Case import Case

# Imports des classes parentes
from ..Effet import On_fin_tour, One_shot, On_post_action

class Antidote(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur:Agissant):
        for effet in porteur.effets:
            if isinstance(effet,Poison):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Medicament(One_shot,On_fin_tour):
    """Effet qui supprime les effets de maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur:Agissant):
        for effet in porteur.effets:
            if isinstance(effet,Maladie): # Créer des médicaments différents selon les maladies ?
                effet.phase = "terminé" # Rajouter une condition de priorite

class Purification(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison ou maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur:Agissant):
        for effet in porteur.effets:
            if isinstance(effet,(Maladie,Poison)):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Soin_case(On_post_action):
    """Un effet de soin. À répercuter sur les occupants éventuels de la case."""
    def __init__(self,gain_pv,responsable:Agissant,cible="alliés"):
        self.phase = "démarrage"
        self.gain_pv = gain_pv
        self.responsable = responsable
        self.cible = cible
        self.affiche = True

    def action(self,case:Case):
        cible_potentielle = case.agissant
        if cible_potentielle is not None:
            if self.responsable == 0: #Pas de responsable. Sérieusement ?
                cible_potentielle.effets.append(Soin(self.responsable,self.gain_pv))
            else:
                esprit = self.responsable.esprit
                if esprit is None: #Pas d'esprit ? Sérieusement ?
                    cible_potentielle.effets.append(Soin(self.responsable,self.gain_pv))
                elif self.cible == "alliés" and cible_potentielle in esprit.corps:
                    cible_potentielle.effets.append(Soin(self.responsable,self.gain_pv))
                elif self.cible == "neutres" and not cible_potentielle in esprit.corps:
                    cible_potentielle.effets.append(Soin(self.responsable,self.gain_pv))

    def execute(self,case:Case):
        if self.phase == "démarrage" :
            self.action(case)
            self.termine()

class Soin(On_fin_tour):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    def __init__(self,responsable,gain_pv):
        self.phase = "démarrage"
        self.responsable = responsable
        self.gain_pv = gain_pv
        self.affiche = True

    def action(self,porteur:Agissant):
        porteur.soigne(self.gain_pv)

    def execute(self,porteur:Agissant):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

# Imports utilisés dans le code
from .Maladies.Maladie import Maladie
from .Poison import Poison