from __future__ import annotations
from typing import TYPE_CHECKING, Type
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Item import Item
    from ..Labyrinthe.Case import Case
    from ..Action.Attaque import Attaque
    from ..Action.Magie.Magie import Magie

# Imports des classes parentes
from ..Effet.Effet import On_need, One_shot, On_debut_tour, Evenement, Time_limited, On_post_action, On_fin_tour

class Investissement_mana(Evenement,On_debut_tour):
    """Le joueur met du mana de côté, et en a plus après !"""
    def __init__(self,temps_restant:float,mana:float):
        self.phase = "démarrage"
        self.affiche = False
        self.temps_restant = temps_restant
        self.mana = mana
        self.phase = "en cours"

    def action(self,agissant:Agissant):
        if self.phase == "terminé":
            agissant.statistiques.pm += self.mana

class Reserve_mana(On_need):
    """Effet qui correspond à une réserve de mana pour le joueur qui peut piocher dedans lorsqu'il en a besoin, mais ce mana n'est pas compté dans le calcul de son mana max."""
    def __init__(self,mana:float):
        self.phase = "démarrage"
        self.affiche = False
        self.mana = mana
        self.phase = "en cours"

    def action(self,mana:float):
        if self.phase == "en cours":
            self.mana -= mana

    def execute(self,mana:float):
        if self.phase == "en cours" :
            self.action(mana)
        if self.mana <= 0 :
            self.termine()

class Obscurite(Evenement,On_debut_tour):
    """Evenement d'obscurité."""
    def __init__(self,duree:int,gain_opacite:float):
        self.affiche = False
        self.temps_restant = duree
        self.phase = "démarrage"
        self.gain_opacite = gain_opacite

    def action(self,case:Case): #La case affectée devient plus impénétrable à la lumière
        if self.phase == "démarrage" :
            case.opacite += self.gain_opacite
        elif self.phase == "terminé":
            case.opacite -= self.gain_opacite

class Blizzard(Evenement,On_post_action):
    """Evenement de blizzard."""
    def __init__(self,duree:int,gain_latence:float):
        self.affiche = False
        self.temps_restant = duree
        self.phase = "démarrage"
        self.gain_latence = gain_latence

    def action(self,case:Case):
        if self.phase == "en cours":
            occupants = case.items | {case.agissant} if case.agissant is not None else case.items
            for occupant in occupants :
                if occupant.action is not None:
                    occupant.action.latence -= self.gain_latence

    def execute(self,case:Case):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case)

class Teleportation(One_shot,On_post_action):
    """Effet qui déplace une entitée."""
    def __init__(self,position:crt.Position):
        self.affiche = True
        self.phase = "démarrage"
        self.position = position

    def action(self,porteur:Agissant|Item):
        porteur.position = self.position

class Enseignement(One_shot,On_fin_tour):
    """Effet qui enseigne une magie au joueur."""
    def __init__(self,magie:Type[Magie]):
        self.affiche = False
        self.magie = magie
        self.phase = "démarrage"

    def action(self,porteur:Agissant):
        if isinstance(porteur,Mage):
            skill = porteur.get_skill_magique()
            skill.ajoute(self.magie)

class Dopage(One_shot,Time_limited):
    """Effet qui "dope" la prochaine attaque du joueur."""
    def __init__(self,responsable:Agissant,taux_degats:float,duree:float):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.taux_degats = taux_degats
        self.temps_restant = duree

    def action(self,attaque:Attaque):
        if self.phase == "démarrage" :
            attaque.taux *= self.taux_degats

class Instakill(One_shot,On_post_action):
    """L'effet d'instakill. S'il réussit, la victime voit ses PV descendre à 0. Sinon, rien.""" #Comment retirer aussi les PM, si la victime a la persévérance (essence magique) ?
    def __init__(self,responsable:Agissant,priorite:float):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite

    def action(self,porteur:Agissant):
        if porteur.priorite < self.priorite :
            porteur.instakill(self.responsable)
        else :
            pass
            # porteur.echape_instakill(self.responsable)

    def execute(self,porteur:Agissant):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

# Imports utilisés dans le code
from ..Entitee.Agissant.Role.Mage import Mage