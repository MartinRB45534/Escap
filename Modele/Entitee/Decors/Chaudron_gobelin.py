from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Controleur import Controleur
    from ..Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from ..Entitee.Decors.Decor import Ustensile

# Valeurs par défaut des paramètres
from ..Labyrinthe.Structure_spatiale.Position import ABSENT

class Chaudron_gobelin(Ustensile):
    """Un chaudron, trouvé en général dans un camp de gobelins."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Ustensile.__init__(self,controleur,recettes_chaudron_gobelin,position) # Remplacer par autre chose, et faire un fichier avec une constante globale pour cette recette

    def get_description(self,observation=0):
        return ["Un chaudron","Il y a des recettes accrochées à côté.","Ça pu le gobelin..."]

    def get_skin(self):
        if self.etat == "intact":
            return SKIN_CHAUDRON_GOBELIN
        else:
            return SKIN_CHAUDRON_GOBELIN_BRISE # Pour le skill d'écrasement

# Imports utilisés dans le code
from ..Systeme.Constantes_decors.Decors import recettes_chaudron_gobelin
from Old_Affichage.Skins.Skins import SKIN_CHAUDRON_GOBELIN,SKIN_CHAUDRON_GOBELIN_BRISE