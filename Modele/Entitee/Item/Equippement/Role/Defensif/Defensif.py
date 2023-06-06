from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Effet.Attaque.Attaque import Attaque_particulier

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Equippement.Equippement import Equipement

class Defensif(Equipement):
    """La classe des équipements défensifs. Réduit les dégats."""

    def intercepte(self,attaque:Attaque_particulier):
        pass
