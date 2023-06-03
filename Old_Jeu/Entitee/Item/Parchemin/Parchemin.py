from __future__ import annotations
from typing import TYPE_CHECKING, Type

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Old_Jeu.Effet.Effet import Effet
    from Old_Jeu.Action.Magie.Magie import Magie

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Item import Consommable

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,controleur:Controleur,effet:Effet,cout:float,duree:float=2,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.effet = effet
        self.duree = duree
        self.cout = cout

    def get_titre(self,observation=0):
        return "Parchemin"

    def get_description(self,observation=0):
        return ["Un parchemin","C'est quoi ces gribouillis ?"]

    # def utilise(self,agissant:Agissant):
    #     if agissant.peut_payer(self.cout) :
    #         agissant.paye(self.cout)
    #         agissant.ajoute_effet(self.effet)
    #         self.etat = "brisé"

    def get_classe(self):
        return Parchemin

    def get_skin(self):
        return SKIN_PARCHEMIN

    @staticmethod
    def get_image():
        return SKIN_PARCHEMIN

class Poly_de_cours(Parchemin):
    """Un parchemin qui enseigne une magie."""
    def __init__(self,controleur:Controleur,magie:Type[Magie],cout:float,duree:float=2,position:Position=ABSENT):
        Parchemin.__init__(self,controleur,Enseignement(magie),cout,duree,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Probablement perdu par un élève.","D'après les tâches de sang, il fuyait un monstre."]

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_PARCHEMIN
from Old_Jeu.Effet.Effets_divers import Enseignement
from Old_Jeu.Entitee.Item.Item import Item