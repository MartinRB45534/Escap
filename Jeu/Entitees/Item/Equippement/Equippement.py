from Jeu.Entitees.Item.Item import *

class Equipement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.taux_stats = {}

    def equippe(self,agissant):
        pass

    def desequippe(self):
        for cause in self.taux_stats.keys():
            if cause == "incompatibilité porteur":
                self.taux_stats.remove(cause)
