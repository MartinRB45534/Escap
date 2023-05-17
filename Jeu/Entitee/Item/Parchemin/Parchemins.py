from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Jeu.Entitee.Item.Parchemin.Parchemin import Parchemin

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Parchemin_purification(Parchemin):
    """Un parchemin qui soigne poisons et maladies."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Parchemin.__init__(self,controleur,Purification(),50,position)

    def get_description(self,observation=0):
        return ["Un parchemin","Soignera poisons et maladies."]

class Parchemin_vierge(Parchemin):
    """Un parchemin qui peut être imprégné d'une magie."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Parchemin.__init__(self,controleur,Impregnation(),10,position)

    def get_description(self,observation=0):
        return ["Un parchemin vierge","On peut y appliquer une magie."]

class Parchemin_impregne(Parchemin):
    """Un parchemin imprégné d'une magie."""
    def __init__(self,controleur:Controleur,magie:Magie,cout:float,position:Position=ABSENT): #Le cout dépend du niveau du parchemin d'imprégnation
        Item.__init__(self,controleur,position)
        self.effet = magie
        self.cout = cout

    # def utilise(self,agissant:Agissant):
    #     if self.etat == "suspens": #On l'a suspendu précédemment, ça devrait être bon maintenant
    #         if agissant.peut_payer(self.cout):
    #             agissant.paye(self.cout)
    #             self.etat = "brisé"
    #             magie = self.effet
    #             agissant.effets.append(magie)
    #             reussite = True
    #             if isinstance(magie,Magie_cible) :
    #                 agissant.controleur.select_cible_parchemin(magie,agissant)
    #             if isinstance(magie,Magie_dirigee) :
    #                 agissant.controleur.select_direction_parchemin(magie,agissant)
    #             if isinstance(magie,Magie_cout) :
    #                 agissant.controleur.select_cout_parchemin(magie,agissant)
    #             if not reussite :
    #                 magie.miss_fire(agissant)
    #     else:
    #         if agissant is agissant.controleur.joueur:
    #             if isinstance(self.effet,Cible_agissant):
    #                 agissant.magie_parchemin = self.effet
    #                 agissant.controleur.set_phase(AGISSANT_PARCHEMIN)
    #                 self.etat = "suspens"
    #             if isinstance(self.effet,Cible_case):
    #                 agissant.magie_parchemin = self.effet
    #                 agissant.controleur.set_phase(CASE_PARCHEMIN)
    #                 self.etat = "suspens"
    #             if isinstance(self.effet,Magie_cout):
    #                 agissant.magie_parchemin = self.effet
    #                 agissant.controleur.set_phase(COUT_PARCHEMIN)
    #                 self.etat = "suspens"
    #             if isinstance(self.effet,Magie_dirigee):
    #                 agissant.magie_parchemin = self.effet
    #                 agissant.controleur.set_phase(DIRECTION_PARCHEMIN)
    #                 self.etat = "suspens"
    #         if self.etat != "suspens": #On n'a pas eu besoin de le suspendre, on peut directement le lancer
    #             if agissant.peut_payer(self.cout) :
    #                 agissant.paye(self.cout)
    #                 self.etat = "brisé"
    #                 magie = self.effet
    #                 agissant.effets.append(magie)
    #                 reussite = True
    #                 if isinstance(magie,Magie_cible) :
    #                     agissant.controleur.select_cible_parchemin(magie,agissant)
    #                 if isinstance(magie,Magie_dirigee) :
    #                     agissant.controleur.select_direction_parchemin(magie,agissant)
    #                 if isinstance(magie,Magie_cout) :
    #                     agissant.controleur.select_cout_parchemin(magie,agissant)
    #                 if not reussite :
    #                     magie.miss_fire(agissant)

    def get_description(self,observation=0):
        return["Un parchemin",f"Imprégné d'une magie ({self.effet.nom})"]

class Parchemin_protection(Parchemin):
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Parchemin.__init__(self,controleur,Protection_groupe(500,200),75,position)

    def get_description(self,observation=0):
        return["Un parchemin","Permet de protéger tous ses alliés"]

# Imports utilisés dans le code
from Jeu.Effet.Magie.Magie import Magie, Magie_cible, Magie_dirigee, Magie_cout, Cible_agissant, Cible_case
from Jeu.Effet.Effets_protection import Protection_groupe
from Jeu.Effet.Effets_divers import Impregnation
from Jeu.Effet.Sante.Soins import Purification
from Jeu.Entitee.Item.Item import Item
from Jeu.Constantes import AGISSANT_PARCHEMIN, CASE_PARCHEMIN, COUT_PARCHEMIN, DIRECTION_PARCHEMIN