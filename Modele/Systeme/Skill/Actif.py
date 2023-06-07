from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Tuple, Type

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Labyrinthe.Structure_spatiale.Direction import Direction
    from ..Action.Magie.Magie import Magie
    from ..Entitee.Item.Equippement.Degainable.Degainable import Arme
    from ..Action.Action_skill import Action_skill, Derobe, Blocage, Ramasse, Alchimie
    from ..Action.Attaque import Attaque, Attaque_arme
    from ..Action.Deplacement import Marche
    from ..Action.Action_skill import Ramasse

# Imports des classes parentes
from ..Systeme.Skill.Skill import Skill

class Actif(Skill):
    """
    Les skills qui genèrent les actions.
    """
    def fait(self,agissant:Agissant) -> Action_skill:
        """Fait l'action"""
        raise NotImplementedError

class Skills_offensifs(Actif):
    """
    Un skill qui genère une attaque (hors attaque magique).
    """
    def fait(self,agissant:Agissant) -> Attaque:
        """Fait l'attaque"""
        raise NotImplementedError

class Skills_projectiles(Actif): #/!\ Retravailler un jour
    """
    Un skill qui lance un objet.
    """

    def utilise(self) -> Tuple[float, float, float]:
        """Utilise le skill, et renvoie l'objet lancé"""
        raise NotImplementedError

class Skills_magiques(Actif):
    """
    Un skill qui permet de lancer des magies.
    """
    def __init__(self): #On précise les magies directement disponibles. D'autres peuvent être acquisent en cours de jeu dans le cas du joueur. magies est un dictionnaire, les clées sont les noms des magies.
        self.magies={}
        self.latence = 0 #La latence dépend du sort utilisé
        self.gain_xp = 0 #L'xp dépend du sort utilisé et du mana dépensé

    def ajoute(self,magie:Type[Magie]):
        """Ajoute une magie au skill"""
        self.magies[magie.nom]=magie

    def menu_magie(self) -> List[Magie]:
        """Renvoie la liste des magies que le skill peut lancer"""
        res = []
        for nom in self.magies:
            type_magie = self.magies[nom]
            magie = type_magie(self.niveau)
            res.append(magie)
        return res
    
    def fait(self,agissant:Agissant,nom:str) -> Magie:
        """Fait la magie nommée nom"""
        return self.magies[nom](self,agissant,self.niveau)

class Skill_deplacement(Actif):
    """
    Un skill qui permet de se déplacer vers une case adjacente.
    """
    
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Actif.__init__(self)
        self.nom="Deplacement"

    def get_skin(self):
        return SKIN_SKILL_DEPLACEMENT

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau

    def fait(self,agissant:Agissant,direction:Optional[Direction]=None,course:bool=False) -> Marche:
        """Fait le déplacement"""
        raise NotImplementedError

class Skill_ramasse(Actif):
    """
    Un skill qui permet de ramasser des objets sur sa case.
    """
    def __init__(self):
        Actif.__init__(self)
        self.nom="Ramassage"

    def get_skin(self):
        return SKIN_SKILL_RAMASSE

    def fait(self, agissant: Agissant) -> Ramasse:
        """Fait le ramassage"""
        raise NotImplementedError

class Skill_merge(Actif):
    """
    Un skill qui permet à deux groupes de fusionner. Unique aux slimes.
    """
    def __init__(self):
        Actif.__init__(self)
        self.nom="Fusion de slimes"

    # /!\ À compléter

class Skill_absorb(Actif):
    """Un skill qui permet d'absorber un cadavre (le ramasser et récupérer un skill). Unique aux slimes."""
    def __init__(self):
        Actif.__init__(self)
        self.nom="Absorption de cadavre"

class Skill_divide(Actif):
    """Un skill qui permet à un agissant de se séparer en deux. Unique aux slimes."""
    def __init__(self):
        Actif.__init__(self)
        self.nom="Division"

class Skill_attaque(Skills_offensifs):
    """Un skill qui permet d'attaquer."""
    def __init__(self):
        Skills_offensifs.__init__(self)
        self.nom = "Attaque"

    def fait(self,agissant:Agissant, direction:Optional[Direction] = None) -> Attaque:
        """Fait l'attaque"""
        raise NotImplementedError
    
class Skill_attaque_arme(Skills_offensifs):
    """Un skill qui permet d'attaquer avec une arme."""
    def __init__(self):
        Skills_offensifs.__init__(self)
        self.nom = "Attaque avec arme"

    def fait(self,agissant:Agissant, arme:Optional[Arme]=None, direction:Optional[Direction] = None) -> Attaque_arme:
        """Fait l'attaque"""
        raise NotImplementedError

class Skill_vol(Actif):
    """Permet de dérober les drops d'un ennemi (sans devoir le tuer ni même le combattre). Nécessite le skill d'observation pour savoir ce qu'on peut voler.""" #Evolue vers les autres skills de vol ? Les offre au fur et à mesure de sa montée de niveau ? Les inclus à partir de certains niveaux ?
    def __init__(self):
        Actif.__init__(self)
        self.nom = "Vol"

    def fait(self, agissant: Agissant) -> Derobe:
        """Fait le vol"""
        raise NotImplementedError

class Skill_blocage(Actif):
    """Permet de se cacher derrière son bouclier."""
    def __init__(self):
        Skill.__init__(self)
        self.nom = "Blocage"

    def fait(self,agissant:Agissant) -> Blocage:
        """Fait le blocage"""
        raise NotImplementedError

class Skill_alchimie(Actif):
    """Permet de créer divers items. C'est un skill semi-passif au sens où son utilisation ne prend pas de temps."""
    def __init__(self):
        Skill.__init__(self)
        self.nom = "Alchimie"

    def fait(self,agissant:Agissant,recette:str) -> Alchimie:
        """Fait l'alchimie"""
        raise NotImplementedError

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_SKILL_DEPLACEMENT, SKIN_SKILL_RAMASSE