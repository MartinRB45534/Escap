from Jeu.Entitee.Item.Parchemin.Parchemin import *
from Jeu.Effet.Effets_divers import *
from Jeu.Effet.Sante.Maladies.Maladies import *
from Jeu.Effet.Magie.Magie import *
from Jeu.Effet.Effets_protection import *
from Jeu.Entitee.Item.Parchemin.Polys import *
from Jeu.Systeme.Constantes_items.Items import *

class Parchemin_purification(Parchemin):
    """Un parchemin qui soigne poisons et maladies."""
    def __init__(self,position:Position):
        Parchemin.__init__(self,position,Purification(),50)

    def get_description(self,observation=0):
        return ["Un parchemin","Soignera poisons et maladies."]

class Parchemin_vierge(Parchemin):
    """Un parchemin qui peut être imprégné d'une magie."""
    def __init__(self,position:Position):
        Parchemin.__init__(self,position,Impregnation(),10)

    def get_description(self,observation=0):
        return ["Un parchemin vierge","On peut y appliquer une magie."]

class Parchemin_impregne(Parchemin):
    """Un parchemin imprégné d'une magie."""
    def __init__(self,position:Position,magie:Magie,cout:float): #Le cout dépend du niveau du parchemin d'imprégnation
        Parchemin.__init__(self,position,magie,cout)

    def utilise(self,agissant:Agissant):
        if self.etat == "suspens": #On l'a suspendu précédemment, ça devrait être bon maintenant
            if agissant.peut_payer(self.cout):
                agissant.paye(self.cout)
                self.etat = "brisé"
                magie = self.effet
                agissant.effets.append(magie)
                reussite = True
                if isinstance(magie,Magie_cible) :
                    agissant.controleur.select_cible_parchemin(magie,agissant)
                if isinstance(magie,Magie_dirigee) :
                    agissant.controleur.select_direction_parchemin(magie,agissant)
                if isinstance(magie,Magie_cout) :
                    agissant.controleur.select_cout_parchemin(magie,agissant)
                if not reussite :
                    magie.miss_fire(agissant)
        else:
            if agissant is agissant.controleur.joueur:
                if isinstance(self.effet,Cible_agissant):
                    agissant.magie_parchemin = self.effet
                    agissant.controleur.set_phase(AGISSANT_PARCHEMIN)
                    self.etat = "suspens"
                if isinstance(self.effet,Cible_case):
                    agissant.magie_parchemin = self.effet
                    agissant.controleur.set_phase(CASE_PARCHEMIN)
                    self.etat = "suspens"
                if isinstance(self.effet,Magie_cout):
                    agissant.magie_parchemin = self.effet
                    agissant.controleur.set_phase(COUT_PARCHEMIN)
                    self.etat = "suspens"
                if isinstance(self.effet,Magie_dirigee):
                    agissant.magie_parchemin = self.effet
                    agissant.controleur.set_phase(DIRECTION_PARCHEMIN)
                    self.etat = "suspens"
            if self.etat != "suspens": #On n'a pas eu besoin de le suspendre, on peut directement le lancer
                if agissant.peut_payer(self.cout) :
                    agissant.paye(self.cout)
                    self.etat = "brisé"
                    magie = self.effet
                    agissant.effets.append(magie)
                    reussite = True
                    if isinstance(magie,Magie_cible) :
                        agissant.controleur.select_cible_parchemin(magie,agissant)
                    if isinstance(magie,Magie_dirigee) :
                        agissant.controleur.select_direction_parchemin(magie,agissant)
                    if isinstance(magie,Magie_cout) :
                        agissant.controleur.select_cout_parchemin(magie,agissant)
                    if not reussite :
                        magie.miss_fire(agissant)

    def get_description(self,observation=0):
        return["Un parchemin",f"Imprégné d'une magie ({self.effet.nom})"]

class Parchemin_protection(Parchemin):
    def __init__(self,position:Position):
        Parchemin.__init__(self,position,Protection_groupe(500,200),75)

    def get_description(self,observation=0):
        return["Un parchemin","Permet de protéger tous ses alliés"]
