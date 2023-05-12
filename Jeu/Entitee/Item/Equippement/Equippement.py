from Jeu.Entitee.Item.Item import *
from typing import Dict

class Equipement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.taux_stats:Dict[str,float] = {}

    def equippe(self,agissant:Agissant):
        pass

    def desequippe(self):
        for cause in self.taux_stats:
            if cause == "incompatibilité porteur":
                self.taux_stats.pop(cause)
