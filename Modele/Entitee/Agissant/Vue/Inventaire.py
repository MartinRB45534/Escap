from __future__ import annotations
from typing import TYPE_CHECKING, List, Dict, Set, Type, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Inventaire import Inventaire
    from ..Agissant import Agissant
    from ...Item.Potion.Potion import Potion
    from ...Item.Parchemin.Parchemin import Parchemin
    from ...Item.Cle import Cle
    from ...Item.Equippement.Degainable.Degainable import Arme
    from ...Item.Equippement.Degainable.Bouclier.Bouclier import Bouclier
    from ...Item.Equippement.Armure.Armure import Armure
    from ...Item.Equippement.Haume.Haume import Haume
    from ...Item.Equippement.Anneau.Anneau import Anneau
    from ...Item.Projectile.Projectile import Projectile
    from ...Item.Item import Ingredient
    from ...Item.Cadavre import Cadavre
    from ...Item.Oeuf import Oeuf
    from .Item import Item_vu

class Inventaire_vu:
    def __init__(self, items:Dict[Type[Potion|Parchemin|Cle|Arme|Bouclier|Armure|Haume|Anneau|Projectile|Ingredient|Cadavre|Oeuf],Set[Item_vu]], arme:Optional[Item_vu] = None, bouclier:Optional[Item_vu] = None, armure:Optional[Item_vu] = None, haume:Optional[Item_vu] = None, anneau:List[Item_vu] = [], nb_doigts:Optional[int] = None):
        self.items = items
        self.arme = arme #L'arme équipée
        self.bouclier = bouclier #Le bouclier équipé
        self.armure = armure #L'armure équipée
        self.haume = haume #Le haume équipé
        self.anneau = anneau #Les anneaux équipés
        self.doigts = nb_doigts #Le nombre d'anneaux que l'on peut équiper

def voit_inventaire(inventaire:Inventaire) -> Inventaire_vu:
    return Inventaire_vu(
        {items:{voit_item(item) for item in inventaire.items[items] if item in inventaire.get_equippement()} for items in inventaire.items},
        voit_item(inventaire.arme) if inventaire.arme else None,
        voit_item(inventaire.bouclier) if inventaire.bouclier else None,
        voit_item(inventaire.armure) if inventaire.armure else None,
        voit_item(inventaire.haume) if inventaire.haume else None,
        [voit_item(item) for item in inventaire.anneau],
        None, # Par défaut, on ne voit pas le nombre de doigts (non pas que ça ait une grande importance)
    )

from .Item import voit_item