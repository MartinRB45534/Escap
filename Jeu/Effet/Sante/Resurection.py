from Jeu.Effet.Effet import *
from Jeu.Constantes import *

class Resurection(On_fin_tour):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,porteur):
        porteur.pv = porteur.pv_max
        porteur.etat = "vivant"

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()
