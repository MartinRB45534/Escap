"""Contient les classes des anneaux."""

from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports des classes parentes
from .anneau import Anneau
from ..role.reparateur.reparateurs import RenforceRegenPV
from ..role.reparateur_magique.reparateurs_magiques import RenforceRegenPM

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .....labyrinthe.labyrinthe import Labyrinthe

class AnneauMagique(Anneau,RenforceRegenPM):
    """Un anneau magique : augmente la régénération des pm."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_regen:float,position:crt.Position=crt.POSITION_ABSENTE):
        Anneau.__init__(self,labyrinthe,poids,frottements,position)
        RenforceRegenPM.__init__(self,labyrinthe,position,taux_regen)
        self.poids = poids
        self.frottements = frottements

class AnneauDeVitalite(Anneau,RenforceRegenPV):
    """Un anneau un peu moins magique : augmente la régénération des pv."""
    def __init__(self,labyrinthe:Labyrinthe,poids:float,frottements:float,taux_regen:float,position:crt.Position=crt.POSITION_ABSENTE):
        Anneau.__init__(self,labyrinthe,poids,frottements,position)
        RenforceRegenPV.__init__(self,labyrinthe,position,taux_regen)
        self.poids = poids
        self.frottements = frottements
