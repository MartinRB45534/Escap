from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Tuple, Type, Dict
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee.agissant.agissant import Agissant
    from ...effet.action.magie.magie import Magie
    from ...entitee.item.equippement.degainable.degainable import Arme
    from ...effet.action.action_skill import Action_skill, Derobe, Blocage, Ramasse, Alchimie
    from ...effet.action.attaque import Attaque, AttaqueArme
    from ...effet.action.deplacement import Marche
    from ...effet.action.action_skill import Ramasse

# Imports des classes parentes
from .skill import Skill

class Actif(Skill):
    """
    Les skills qui genèrent les actions.
    """
    def fait(self,agissant:Agissant) -> Action_skill:
        """Fait l'action"""
        raise NotImplementedError

class SkillsOffensifs(Actif):
    """
    Un skill qui genère une attaque (hors attaque magique).
    """
    def fait(self,agissant:Agissant) -> Attaque:
        """Fait l'attaque"""
        raise NotImplementedError

class SkillsProjectiles(Actif): #/!\ Retravailler un jour
    """
    Un skill qui lance un objet.
    """

    def utilise(self) -> Tuple[float, float, float]:
        """Utilise le skill, et renvoie l'objet lancé"""
        raise NotImplementedError

class SkillsMagiques(Actif):
    """
    Un skill qui permet de lancer des magies.
    """
    def __init__(self): #On précise les magies directement disponibles. D'autres peuvent être acquisent en cours de jeu dans le cas du joueur. magies est un dictionnaire, les clées sont les noms des magies.
        self.magies:Dict[str,Type[Magie]]={}
        self.latence = 0 #La latence dépend du sort utilisé
        self.gain_xp = 0 #L'xp dépend du sort utilisé et du mana dépensé

    def ajoute(self,magie:Type[Magie]):
        """Ajoute une magie au skill"""
        self.magies[magie.nom]=magie

    def menu_magie(self) -> List[Magie]:
        """Renvoie la liste des magies que le skill peut lancer"""
        res:List[Magie] = []
        for nom in self.magies:
            type_magie = self.magies[nom]
            magie = type_magie(self.niveau) # Qu'est-ce que je voulais faire là ?
            res.append(magie)
        return res
    
    def fait(self,agissant:Agissant,nom:str) -> Magie:
        """Fait la magie nommée nom"""
        return self.magies[nom](self,agissant,self.niveau)

class SkillDeplacement(Actif):
    """
    Un skill qui permet de se déplacer vers une case adjacente.
    """
    
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Actif.__init__(self)
        self.nom="Deplacement"

    def evo(self,nb_evo:int=1):
        for _ in range(nb_evo):
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau

    def fait(self,agissant:Agissant,direction:Optional[crt.Direction]=None,course:bool=False) -> Marche:
        """Fait le déplacement"""
        raise NotImplementedError

class SkillRamasse(Actif):
    """
    Un skill qui permet de ramasser des objets sur sa case.
    """
    def __init__(self):
        Actif.__init__(self)
        self.nom="Ramassage"

    def fait(self, agissant: Agissant) -> Ramasse:
        """Fait le ramassage"""
        raise NotImplementedError

class SkillMerge(Actif):
    """
    Un skill qui permet à deux groupes de fusionner. Unique aux slimes.
    """
    def __init__(self):
        Actif.__init__(self)
        self.nom="Fusion de slimes"

    # /!\ À compléter

class SkillAbsorb(Actif):
    """Un skill qui permet d'absorber un cadavre (le ramasser et récupérer un skill). Unique aux slimes."""
    def __init__(self):
        Actif.__init__(self)
        self.nom="Absorption de cadavre"

class SkillDivide(Actif):
    """Un skill qui permet à un agissant de se séparer en deux. Unique aux slimes."""
    def __init__(self):
        Actif.__init__(self)
        self.nom="Division"

class SkillAttaque(SkillsOffensifs):
    """Un skill qui permet d'attaquer."""
    def __init__(self):
        SkillsOffensifs.__init__(self)
        self.nom = "Attaque"

    def fait(self,agissant:Agissant, direction:Optional[crt.Direction] = None) -> Attaque:
        """Fait l'attaque"""
        raise NotImplementedError
    
class SkillAttaqueArme(SkillsOffensifs):
    """Un skill qui permet d'attaquer avec une arme."""
    def __init__(self):
        SkillsOffensifs.__init__(self)
        self.nom = "Attaque avec arme"

    def fait(self,agissant:Agissant, arme:Optional[Arme]=None, direction:Optional[crt.Direction] = None) -> AttaqueArme:
        """Fait l'attaque"""
        raise NotImplementedError

class SkillVol(Actif):
    """Permet de dérober les drops d'un ennemi (sans devoir le tuer ni même le combattre). Nécessite le skill d'observation pour savoir ce qu'on peut voler.""" #Evolue vers les autres skills de vol ? Les offre au fur et à mesure de sa montée de niveau ? Les inclus à partir de certains niveaux ?
    def __init__(self):
        Actif.__init__(self)
        self.nom = "Vol"

    def fait(self, agissant: Agissant) -> Derobe:
        """Fait le vol"""
        raise NotImplementedError

class SkillBlocage(Actif):
    """Permet de se cacher derrière son bouclier."""
    def __init__(self):
        Skill.__init__(self)
        self.nom = "Blocage"

    def fait(self,agissant:Agissant) -> Blocage:
        """Fait le blocage"""
        raise NotImplementedError

class SkillAlchimie(Actif):
    """Permet de créer divers items. C'est un skill semi-passif au sens où son utilisation ne prend pas de temps."""
    def __init__(self):
        Skill.__init__(self)
        self.nom = "Alchimie"

    def fait(self,agissant:Agissant,recette:str) -> Alchimie:
        """Fait l'alchimie"""
        raise NotImplementedError
