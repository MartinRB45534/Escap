from __future__ import annotations
from typing import TYPE_CHECKING, List, Dict
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ....Systeme.Classe.Classe_principale import Classe_principale
    from ....Entitee.Agissant.Inventaire import Inventaire
    from ..Agissant import Agissant

# Valeurs par défaut des paramètres
from ....Systeme.Elements import Element

class Agissant_vu:
    def __init__(self, identite:str, pv_max:float, pv:float, pm_max:float, pm:float, force:float, priorite:float, vitesse:float, affinites:Dict[Element,float], immunites:List[Element], especes:List[str], classe:Classe_principale, niveau:int, inventaire:Inventaire, dir_regard:crt.Direction):
        self.identite = identite
        self.pv_max = pv_max
        self.pv = pv
        self.pm_max = pm_max
        self.pm = pm
        self.force = force
        self.priorite = priorite
        self.vitesse = vitesse
        self.affinites = affinites
        self.immunites = immunites
        self.especes = especes
        self.classe = classe
        self.niveau = niveau
        self.inventaire = inventaire
        self.dir_regard = dir_regard

def voit_agissant(agissant:Agissant) -> Agissant_vu:
    return Agissant_vu(
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

