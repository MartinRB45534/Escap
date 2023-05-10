from Jeu.Effet.Effet import *
from Jeu.Constantes import *

class Reanimation(On_fin_tour):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,taux,esprit):
        self.phase = "démarrage"
        self.taux = taux
        self.esprit = esprit
        self.affiche = False

    def action(self,porteur):
        porteur.pv = porteur.pv_max*self.taux
        porteur.etat = "vivant"
        if self.esprit is not None:
            esprit_porteur = porteur.controleur.get_esprit(porteur)
            if esprit_porteur is not None:
                esprit_porteur.retire_corp(porteur)
            self.esprit.ajoute_corp(porteur)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()
