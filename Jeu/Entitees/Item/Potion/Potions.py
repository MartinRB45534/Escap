from Jeu.Entitees.Item.Potion.Potion import *
from Jeu.Systeme.Constantes_items.Items import *

class Potion_empoisonnee(Potion):
    """Une potion pas très bonne pour la santé."""
    def __init__(self,position):
        Potion.__init__(self,position,Poison(1,1,0.0101))

    def get_titre(self,observation):
        return "Potion empoisonnée"

    def get_description(self,observation):
        return ["Une potion","Elle n'a pas l'air très apétissante..."]

    def get_skin(self):
        return SKIN_POTION_POISON

class Potion_antidote(Potion):
    """Une potion qui élimine les poisons."""
    def __init__(self,position):
        Potion.__init__(self,position,Antidote())

    def get_titre(self,observation):
        return "Antidote"

    def get_description(self,observation):
        return ["Une potion","Elle a probablement un effet bénéfique."]

class Potion_medicament(Potion):
    """Une potion qui élimine les maladies."""
    def __init__(self,position):
        Potion.__init__(self,position,Medicament())

    def get_titre(self,observation):
        return "Médicament"

    def get_description(self,observation):
        return ["Une potion","Elle a probablement un effet bénéfique."]

class Potion_soin(Potion):
    """Une potion qui restaure les PVs."""
    def __init__(self,position,pv):
        Potion.__init__(self,position,Soin(0,pv))

    def get_titre(self,observation):
        return "Potion de soin"

    def get_description(self,observation):
        return ["Une potion","Soigne les blessures. J'espère."]

class Potion_hypokute(Potion_soin):
    """Une potion qui restaure les PVs."""
    def __init__(self,position):
        Potion_soin.__init__(self,position,soin_potion_hypokute)

class Potion_force(Potion):
    """Une potion qui augmente les dégats infligés."""
    def __init__(self,position):
        Potion.__init__(self,position,Enchantement_force(1.5,100))

    def get_titre(self,observation):
        return "Potion de force"

    def get_description(self,observation):
        return ["Une potion","Augmente la force (et donc les dégats infligés)."]

#class Potion_defense(Potion):
#    """Une potion qui protège des attaques."""
#    def __init__(self,position,pv):
#        Potion.__init__(self,position,Enchantement_defense(duree,)) #/!\ Qu'est-ce qui m'est arrivé ici ?
#
#    def get_titre(self,observation):
#        return "Potion de defense"
#
#    def get_description(self,observation):
#        return ["Une potion","Protège des attaques."]

class Potion_vitesse(Potion):
    """Une potion qui augmente temporairement la vitesse."""
    def __init__(self,position,duree,vitesse):
        Potion.__init__(self,position,Enchantement_vitesse(duree,vitesse))

    def get_titre(self,observation):
        return "Potion de vitesse"

    def get_description(self,observation):
        return ["Une potion","Augmente temporairement la vitesse de l'utilisateur. À utiliser au début d'un échange de coups ou lors d'une fuite."]

from Jeu.Effet.Magies import *
from Jeu.Effet.Maladies import *