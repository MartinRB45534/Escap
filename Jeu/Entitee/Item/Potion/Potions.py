from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Entitee.Item.Potion.Potion import Potion

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Potion_empoisonnee(Potion):
    """Une potion pas très bonne pour la santé."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Potion.__init__(self,controleur,Poison(NoOne(),1,0.0101),position)

    def get_titre(self,observation=0):
        return "Potion empoisonnée"

    def get_description(self,observation=0):
        return ["Une potion","Elle n'a pas l'air très apétissante..."]

    def get_skin(self):
        return SKIN_POTION_POISON

class Potion_antidote(Potion):
    """Une potion qui élimine les poisons."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Potion.__init__(self,controleur,Antidote(),position)

    def get_titre(self,observation=0):
        return "Antidote"

    def get_description(self,observation=0):
        return ["Une potion","Elle a probablement un effet bénéfique."]

class Potion_medicament(Potion):
    """Une potion qui élimine les maladies."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Potion.__init__(self,controleur,Medicament(),position)

    def get_titre(self,observation=0):
        return "Médicament"

    def get_description(self,observation=0):
        return ["Une potion","Elle a probablement un effet bénéfique."]

class Potion_soin(Potion):
    """Une potion qui restaure les PVs."""
    def __init__(self,controleur:Controleur,pv:float,position:Position=ABSENT):
        Potion.__init__(self,controleur,Soin(0,pv),position)

    def get_titre(self,observation=0):
        return "Potion de soin"

    def get_description(self,observation=0):
        return ["Une potion","Soigne les blessures. J'espère."]

class Potion_hypokute(Potion_soin):
    """Une potion qui restaure les PVs."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Potion_soin.__init__(self,controleur,soin_potion_hypokute,position)

class Potion_force(Potion):
    """Une potion qui augmente les dégats infligés."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Potion.__init__(self,controleur,Enchantement_force(1.5,100),position)

    def get_titre(self,observation=0):
        return "Potion de force"

    def get_description(self,observation=0):
        return ["Une potion","Augmente la force (et donc les dégats infligés)."]

#class Potion_defense(Potion):
#    """Une potion qui protège des attaques."""
#    def __init__(self,position:Optional[Position]=None,pv):
#        Potion.__init__(self,position,Enchantement_defense(duree,)) #/!\ Qu'est-ce qui m'est arrivé ici ?
#
#    def get_titre(self,observation=0):
#        return "Potion de defense"
#
#    def get_description(self,observation=0):
#        return ["Une potion","Protège des attaques."]

class Potion_vitesse(Potion):
    """Une potion qui augmente temporairement la vitesse."""
    def __init__(self,controleur:Controleur,duree,vitesse,position:Position=ABSENT):
        Potion.__init__(self,controleur,Enchantement_vitesse(duree,vitesse),position)

    def get_titre(self,observation=0):
        return "Potion de vitesse"

    def get_description(self,observation=0):
        return ["Une potion","Augmente temporairement la vitesse de l'utilisateur. À utiliser au début d'un échange de coups ou lors d'une fuite."]

# Imports utilisés dans le code
from Jeu.Effet.Sante.Poison import Poison
from Jeu.Effet.Sante.Soins import Soin, Antidote, Medicament
from Jeu.Effet.Enchantements import Enchantement_force, Enchantement_vitesse
from Jeu.Entitee.Agissant.Agissant import NoOne
from Jeu.Systeme.Constantes_items.Items import soin_potion_hypokute
from Affichage.Skins.Skins import SKIN_POTION_POISON