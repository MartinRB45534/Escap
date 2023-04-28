from Affichage.Skins.Skins import *
from Jeu.Entitee.Decors.Decor import *
from Jeu.Systeme.Constantes_decors.Decors import *

class Chaudron_gobelin(Ustensile):
    """Un chaudron, trouvé en général dans un camp de gobelins."""
    def __init__(self,position:Position):
        Ustensile.__init__(self,position,recettes_chaudron_gobelin) # Remplacer par autre chose, et faire un fichier avec une constante globale pour cette recette

    def get_description(self,observation=0):
        return ["Un chaudron","Il y a des recettes accrochées à côté.","Ça pu le gobelin..."]

    def get_skin(self):
        if self.etat == "intact":
            return SKIN_CHAUDRON_GOBELIN
        else:
            return SKIN_CHAUDRON_GOBELIN_BRISE # Pour le skill d'écrasement