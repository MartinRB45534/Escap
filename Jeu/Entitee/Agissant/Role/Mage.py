from Jeu.Entitee.Agissant.Agissant import *

class Mage(Agissant):
    """Les agissants qui lancent des sorts.
       Ont en général un sort de prédilection."""

    def peut_caster(self): # Utilisé pour déterminer leur comportement
        return False

    def caste(self):
        return None
