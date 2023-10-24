from __future__ import annotations
from typing import TYPE_CHECKING, Type, Callable
import affichage as af
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.entitee import Entitee
    from .passage import Passage

class Mur(crt.Mur):
    """Les murs des cases du labyrinthe. Ils peuvent être cassés, ouverts, fermés, etc."""
    def __init__(self,niveau:int):
        super().__init__()
        self.niveau = niveau

    def casser(self):
        pass

    def peut_passer(self,entitee:Entitee):
        if not self.ferme :
            return True
        return False
    
    def passage(self,passage:Passage) -> bool:
        raise NotImplementedError("La méthode passage n'est pas implémentée pour cette classe")

class MurImpassable(Mur):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.ferme = True

    def casser(self):
        raise Exception("Impossible de casser un mur impassable")

    def peut_passer(self,entitee:Entitee):
        return False
    
    def passage(self,passage:Passage):
        return False

class MurPlein(Mur):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.casse = False
        
    @property
    def ferme(self):
        return not(self.casse)
    
    def casser(self):
        self.casse = True

    def peut_passer(self,entitee:Entitee):
        if not self.ferme :
            return True # Si le mur est ouvert (détruit), on peut passer
        elif isinstance(entitee,Fantome):
            return True # Les fantômes peuvent passer à travers les murs
        else :
            ecrasement = None
            if isinstance(entitee,Agissant):
                ecrasement = trouve_skill(entitee.classe_principale,SkillEcrasement)   # ou l'écraser.
            if ecrasement is not None :
                passage = ecrasement.utilise(self.niveau,entitee.get_priorite())
                if passage :
                    self.casser()
                return passage
            else :
                return False
    
    def passage(self,passage:Passage):
        return passage.mur or not self.ferme

class Porte(MurPlein):
    def __init__(self,niveau:int,code:str):
        super().__init__(niveau)
        self.code = code
        self.ouvert = False
        self.casse = False

    @property
    def ferme(self):
        return not(self.ouvert) and not(self.casse)
    
    def casser(self):
        self.casse = True

    def ouvrir(self, agissant:Agissant):
        if self.code in agissant.clees:
            self.ouvert = True

    def fermer(self, agissant:Agissant):
        if self.code in agissant.clees:
            self.ouvert = False

    def passage(self, passage: Passage):
        return passage.mur or passage.porte or not self.ferme or self.code in passage.codes

class MurOuvert(Mur):
    def __init__(self,niveau:int):
        super().__init__(niveau)

    @property
    def ferme(self):
        return False
    
    def casser(self):
        pass

    def peut_passer(self,entitee:Entitee) -> bool:
        return True
    
    def passage(self,passage:Passage) -> bool:
        return True

class Barriere(MurOuvert):
    def __init__(self,niveau:int,condition:Callable[[Entitee],bool]):
        super().__init__(niveau)
        self.condition = condition

    def peut_passer(self,entitee:Entitee):
        return self.condition(entitee) # Si la condition est remplie, on peut passer
    
    def passage(self,passage:Passage):
        return passage.barriere
    
class Teleporteur(MurOuvert): # La seule différence avec un mur ouvert est que les téléporteurs sont affichés différemment
    def __init__(self,niveau:int):
        super().__init__(niveau)

    def passage(self,passage:Passage):
        return passage.teleporteur

# Quelques murs pas symétriques

class MurAsymétrique(Mur): # Hérite vraiment ?
    def __init__(self,niveau:int,autre_mur:MurAsymétrique|Type[MurAsymétrique],mur:Mur):
        self.mur = mur
        if isinstance(autre_mur,MurAsymétrique):
            self.autre_mur = autre_mur
        else :
            self.autre_mur = autre_mur(niveau,self,mur)

    @property
    def ferme(self):
        return self.mur.ferme

    def casser(self):
        self.mur.casser()

    def peut_passer(self,entitee:Entitee):
        return self.mur.peut_passer(entitee)
    
class PorteALoquet(MurAsymétrique, Porte):
    """Une porte qui peut s'ouvrir sans clé de l'autre côté"""
    def __init__(self, niveau: int, autre_mur: PorteALoquet | Type[PorteALoquet], mur: Porte, loquet: bool = False):
        self.mur = mur
        if isinstance(autre_mur,PorteALoquet):
            self.autre_mur = autre_mur
        else :
            self.autre_mur = autre_mur(niveau,self,mur,not(loquet))
        self.loquet = loquet

    @property
    def ouvert(self):
        return self.mur.ouvert
    
    def ouvrir(self, agissant:Agissant):
        if self.loquet:
            self.mur.ouvert = True
        else :
            self.mur.ouvrir(agissant)

    def fermer(self, agissant:Agissant):
        if self.loquet:
            self.mur.ouvert = False
        else :
            self.mur.fermer(agissant)

class Escalier(MurAsymétrique, MurOuvert):
    """Un téléporteur avec une notion graphique de haut et de bas"""
    def __init__(self, niveau: int, autre_mur: Escalier | Type[Escalier], mur: MurOuvert, direction: af.DirectionAff = af.DirectionAff.NEXT):
        self.mur = mur
        if isinstance(autre_mur,Escalier):
            self.autre_mur = autre_mur
        else :
            self.autre_mur = autre_mur(niveau,self,mur,direction.oppose)
        self.direction = direction

    def passage(self, passage: Passage):
        return passage.escalier

# Imports utilisés dans le code
from ..entitee.entitee import Fantome
from ..entitee.agissant.agissant import Agissant
from ..systeme.classe.classes import trouve_skill
from ..systeme.skill.passif import SkillEcrasement