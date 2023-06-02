from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Projectile.Projectile import Projectile

# Pas de classe parente

# Valeurs par défaut des paramètres
from Jeu.Entitee.Item.Item import Item

class Cree_item:
    """La classe des créateurs d'item."""
    def __init__(self,classe_item = Item):
        self.item = classe_item

    def cree_item(self,agissant:Agissant) -> Projectile:
        raise NotImplementedError

class Cree_fleche_de_base_skill(Cree_item):
    """La classe des créateurs de fleche de base, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_de_base
        self.nom = "Flèche de base"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_FLECHE_DE_BASE

class Cree_fleche_percante_skill(Cree_item):
    """La classe des créateurs de fleche percante, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_de_base #Pour l'instant les flèches perçantes n'existent pas
        self.nom = "Flèche percante"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_FLECHE_DE_BASE

class Cree_fleche_fantome_skill(Cree_item):
    """La classe des créateurs de fleche fantome, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_fantome
        self.nom = "Flèche fantome"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_FLECHE_FANTOME

class Cree_fleche_lourde_skill(Cree_item):
    """La classe des créateurs de fleche lourde, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_lourde
        self.nom = "Flèche lourde"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_FLECHE_LOURDE

class Cree_fleche_legere_skill(Cree_item):
    """La classe des créateurs de fleche legere, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_legere
        self.nom = "Flèche legere"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_FLECHE_LEGERE

class Cree_fleche_explosive_skill(Cree_item):
    """La classe des créateurs de fleche lourde, associé au skill de création de fleche ou d'explosif."""
    def __init__(self):
        self.item = Fleche_explosive
        self.nom = "Flèche explosive"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill_fleche = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        skill_explosif = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill_fleche is not None:
            if skill_explosif is not None:
                if skill_fleche.niveau > skill_explosif.niveau :
                    niveau = skill_fleche.utilise(0.01) #L'xp gagné. En faire une variable /!\
                    item = self.item(agissant.controleur,niveau)
                    agissant.controleur.ajoute_entitee(item)
                else:
                    niveau = skill_explosif.utilise(0.01) #L'xp gagné. En faire une variable /!\
                    item = self.item(agissant.controleur,niveau)
                    agissant.controleur.ajoute_entitee(item)
            else:
                niveau = skill_fleche.utilise(0.01) #L'xp gagné. En faire une variable /!\
                item = self.item(agissant.controleur,niveau)
                agissant.controleur.ajoute_entitee(item)
        elif skill_explosif is not None:
            niveau = skill_explosif.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        else:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        return item

    def get_image(self):
        return SKIN_CREE_FLECHE_EXPLOSIVE

class Cree_charge_de_base_skill(Cree_item):
    """La classe des créateurs de charge lourde, associé au skill de création d'explosif."""
    def __init__(self):
        self.item = Charge_de_base
        self.nom = "Charge de base"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_CHARGE_DE_BASE

class Cree_charge_lourde_skill(Cree_item):
    """La classe des créateurs de charge lourde, associé au skill de création d'explosif."""
    def __init__(self):
        self.item = Charge_lourde
        self.nom = "Charge lourde"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_CHARGE_LOURDE

class Cree_charge_etendue_skill(Cree_item):
    """La classe des créateurs de charge étendue, associé au skill de création d'explosif."""
    def __init__(self):
        self.item = Charge_etendue
        self.nom = "Charge etendue"

    def cree_item(self,agissant:Agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill is None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire une variable /!\
            item = self.item(agissant.controleur,niveau)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_image(self):
        return SKIN_CREE_CHARGE_ETENDUE

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_CREE_CHARGE_DE_BASE, SKIN_CREE_CHARGE_ETENDUE, SKIN_CREE_CHARGE_LOURDE, SKIN_CREE_FLECHE_EXPLOSIVE, SKIN_CREE_FLECHE_LEGERE, SKIN_CREE_FLECHE_LOURDE, SKIN_CREE_FLECHE_DE_BASE, SKIN_CREE_FLECHE_FANTOME
from Jeu.Entitee.Item.Projectile.Projectiles import Fleche_explosive, Fleche_legere, Fleche_lourde, Charge_de_base, Charge_lourde, Charge_etendue, Fleche_de_base, Fleche_fantome

from Jeu.Systeme.Classe.Classes import trouve_skill
from Jeu.Systeme.Skill.Skills import Skill_creation_d_explosifs, Skill_creation_de_fleches