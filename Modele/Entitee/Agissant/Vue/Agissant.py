from __future__ import annotations
from typing import TYPE_CHECKING, List, Dict, Set, Type, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Systeme.Classe.Classe_principale import Classe_principale
    from .Inventaire import Inventaire_vu
    from ..Agissant import Agissant

# Valeurs par défaut des paramètres
from ....Systeme.Elements import Element

class Agissant_vu:
    def __init__(self, ID:int, identite:str, pv_max:Optional[float], pv:Optional[float], proportion_pv:Optional[float], pm_max:Optional[float], pm:Optional[float], proportion_pm:Optional[float], force:Optional[float], priorite:Optional[float], vitesse:Optional[float], affinites:Dict[Element,float], immunites:Dict[Element,float], especes:Set[str], classe_principale:Classe_principale, niveau:int, inventaire:Inventaire_vu, dir_regard:Optional[crt.Dir] = None):
        self.ID = ID
        self.identite = identite
        self.pv_max = pv_max
        self.pv = pv
        self.proportion_pv = proportion_pv
        self.pm_max = pm_max
        self.pm = pm
        self.proportion_pm = proportion_pm
        self.force = force
        self.priorite = priorite
        self.vitesse = vitesse
        self.affinites = affinites
        self.immunites = immunites
        self.especes = especes
        self.classe_principale = classe_principale
        self.niveau = niveau
        self.inventaire = inventaire
        self.dir_regard = dir_regard

def voit_agissant(agissant:Agissant) -> Agissant_vu:
    return Agissant_vu(
        agissant.ID,
        agissant.identite,
        agissant.pv_max,
        agissant.pv,
        agissant.pm_max,
        agissant.pm,
        agissant.force,
        agissant.priorite,
        agissant.vitesse,
        agissant.affinites,
        agissant.immunites,
        agissant.especes,
        agissant.classe_principale,
        agissant.niveau,
        agissant.inventaire,
        agissant.dir_regard
        )

