from .Affichable import Affichable

class Survolable(Affichable):
    """Un élément qui réagit au survol"""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.marque_survol = False #Est-ce que la souris est dessus ?

    def survol(self,position):
        survol = Affichable.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False