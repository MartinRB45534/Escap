from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Systeme.Skill.Actif import Actif

# Imports des classes parentes
from Old_Jeu.Action.Magie.Magie import Magie, Magie_cout
from Old_Jeu.Action.Magie.Magies_attaque.Attaques_corps_a_corps import Magie_attaque_corp_a_corp

class Magie_reserve(Magie_cout):
    """La magie qui fait une réserve de mana."""
    nom = "magie reserve"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_reserve[niveau-1],0,latence_reserve[niveau-1],niveau)

    def action(self):
        self.agissant.effets.append(Reserve_mana(self.cout*taux_reserve[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_RESERVE

    def get_titre(self,observation=0):
        return f"Magie de réserve (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de réserve","Stocke des PMs, en surplus de la limite de PMs.","Les PMs stocké sont utilisés lorsque les PMs standard sont épuisés. La quantité de PMs dans la réserve dépend de la quantité dépensée lors du lancement du sort.",f"Taux de stockage : {taux_reserve[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_investissement(Magie_cout):
    """La magie qui crée un investissement."""
    nom = "magie investissement"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie.__init__(self,skill,agissant,gain_xp_investissement[niveau-1],0,latence_investissement[niveau-1],niveau)

    def action(self):
        self.agissant.effets.append(Investissement_mana(duree_investissement[self.niveau-1],self.cout*taux_investissement[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_INVESTISSEMENT

    def get_titre(self,observation=0):
        return f"Magie d'investissement (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'investissement","Rend après un certain temps plus de PMs qu'il n'en a été dépensés pour lancer le sort.",f"Taux de rendement : {taux_investissement[self.niveau-1]}",f"Temps d'attente : {duree_investissement[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_explosion_de_mana(Magie_cout,Magie_attaque_corp_a_corp):
    """La magie qui crée une explosion de mana."""
    nom = "magie explosion de mana"
    def __init__(self,skill:Actif,agissant:Agissant,niveau:int):
        Magie_attaque_corp_a_corp.__init__(self,skill,agissant,gain_xp_explosion_de_mana[niveau-1],0,portee_explosion_de_mana[niveau-1],0,TERRE,"C__S___",latence_explosion_de_mana[niveau-1],niveau)

    def set_cout(self,cout:float):
        super().set_cout(cout)
        self.degats = cout*taux_degats_explosion_de_mana[self.niveau-1]

    def get_image(self):
        return SKIN_MAGIE_EXPLOSION_DE_MANA

    def get_titre(self,observation=0):
        return f"Magie d'explosion de mana (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés à proximité.","Les dégats dépendent des PMs dépensés pour lancer le sort",f"Taux de dégats : {taux_degats_explosion_de_mana[self.niveau-1]}",f"Portee de l'attaque : {portee_explosion_de_mana[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Old_Jeu.Effet.Effets_divers import Reserve_mana,Investissement_mana
from Old_Jeu.Constantes import *
from Old_Jeu.Systeme.Constantes_magies.Magies import *
from Old_Affichage.Skins.Skins import SKIN_MAGIE_RESERVE,SKIN_MAGIE_INVESTISSEMENT,SKIN_MAGIE_EXPLOSION_DE_MANA