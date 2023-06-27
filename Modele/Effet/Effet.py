from __future__ import annotations

# Pas d'imports utilisés uniquement dans les annotations

# Pas de classe parente

class Effet :
    """Les effets regroupent des choses qui arrivent à des éléments du système. Ils peuvent cibler une case, un mur, un agissant, un étage, etc. et sont souvent limités dans le temps ou par d'autres conditions. Ils sont évalués par le controleur dans différentes circonstances."""
    def termine(self) -> bool:
        """Idique si l'effet est terminé."""
        return True

class On_tick(Effet) :
    """La classe des effets appelés à chaque tour."""
    def execute(self) -> None:
        """execute() est appelée à chaque tour."""
        raise NotImplementedError
    
    def action(self) -> None:
        """action() est appelée par execute() lorsque c'est approprié."""
        raise NotImplementedError

class One_shot(Effet):
    """Classe des effets qui n'ont à être appelés qu'une seule fois."""

    def execute(self): # Vraiment nécessaire ?
        self.action()

    def action(self) -> None:
        """action() est appelée une seule fois."""
        raise NotImplementedError

class Evenement(On_tick):
    """La classe des effets limités par le temps, appelés une seule fois par tour."""
    def __init__(self,temps_restant:float):
        self.temps_restant=temps_restant

    def execute(self):
        self.temps_restant -= 1
        self.action()

    def termine(self) -> bool:
        return self.temps_restant <= 0