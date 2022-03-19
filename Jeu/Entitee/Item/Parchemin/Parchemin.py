from Jeu.Entitee.Item.Item import *

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,position,effet,cout):
        Item.__init__(self,position)
        self.effet = effet
        self.cout = cout

    def get_titre(self,observation):
        return "Parchemin"

    def get_description(self,observation):
        return ["Un parchemin","C'est quoi ces gribouillis ?"]

    def utilise(self,agissant):
        if agissant.peut_payer(self.cout) :
            agissant.paye(self.cout)
            agissant.ajoute_effet(self.effet)
            self.etat = "brisé"
        elif agissant.ID==2:
            agissant.affichage.message("Tu n'as pas assez de mana pour utiliser ce parchemin.")

    def get_classe(self):
        return Parchemin

    def get_skin(self):
        return SKIN_PARCHEMIN

    def get_image():
        return SKIN_PARCHEMIN

class Poly_de_cours(Parchemin):
    """Un parchemin qui enseigne une magie."""
    def __init__(self,position,magie,cout):
        Parchemin.__init__(self,position,Enseignement(magie),cout)

    def get_description(self,observation):
        return["Un parchemin de cours","Probablement perdu par un élève.","D'après les tâches de sang, il fuyait un monstre."]

from Jeu.Effet.Effets_divers import Enseignement