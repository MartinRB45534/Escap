"""
Les divers types de murs.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Type, Callable
import affichage as af
import carte as crt
from modele.commons.passage import Passage

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.entitee import Entitee
    from ..commons.passage import Passage

class Mur(crt.Mur):
    """Les murs des cases du labyrinthe. Ils peuvent être cassés, ouverts, fermés, etc."""
    def __init__(self,niveau:int):
        super().__init__()
        self.niveau = niveau

    def casser(self):
        """Casse le mur."""

    def peut_passer(self,_entitee:Entitee):
        """Renvoie True si l'entitée peut passer à travers le mur."""
        if not self.ferme :
            return True
        return False

    def passage(self,passage:Passage) -> bool:
        """Renvoie True si le passage est possible."""
        raise NotImplementedError("La méthode passage n'est pas implémentée pour cette classe")

class MurImpassable(Mur):
    """Les bords du labyrinthe par exemple."""
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.ferme = True

    def casser(self) -> None:
        raise NotImplementedError("Impossible de casser un mur impassable")

    def peut_passer(self,_entitee:Entitee) -> bool:
        return False

    def passage(self,passage:Passage):
        return False

class MurPlein(Mur):
    """Les murs normaux, qui peuvent être cassés (ou même naturellement ouverts)."""
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.casse = False

    @property
    def ferme(self):
        """Renvoie True si le mur est fermé, False sinon."""
        return not self.casse

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
    """Une porte qui peut être ouverte ou fermée avec une clé."""
    def __init__(self,niveau:int,code:str):
        super().__init__(niveau)
        self.code = code
        self.ouvert = False
        self.casse = False

    @property
    def ferme(self):
        return not(self.ouvert or self.casse)

    def casser(self):
        self.casse = True

    def ouvrir(self, agissant:Agissant):
        """Ouvre la porte si l'agissant a la clé."""
        if self.code in agissant.clees:
            self.ouvert = True

    def fermer(self, agissant:Agissant):
        """Ferme la porte si l'agissant a la clé."""
        if self.code in agissant.clees:
            self.ouvert = False

    def passage(self, passage: Passage):
        return passage.mur or passage.porte or not self.ferme or self.code in passage.codes

class MurOuvert(Mur):
    """Un non-mur, en quelque sorte."""
    @property
    def ferme(self):
        """Renvoie True si le mur est fermé, False sinon."""
        return False

    def casser(self):
        pass

    def peut_passer(self,_entitee:Entitee) -> bool:
        return True

    def passage(self,passage:Passage) -> bool:
        return True

class Barriere(MurOuvert):
    """Un mur qui peut être traversé sous certaines conditions."""
    def __init__(self,niveau:int,condition:Callable[[Entitee],bool]):
        super().__init__(niveau)
        self.condition = condition

    def peut_passer(self,entitee:Entitee):
        return self.condition(entitee) # Si la condition est remplie, on peut passer

    def passage(self,passage:Passage):
        return passage.barriere

class Teleporteur(MurOuvert): # Presque comme un mur ouvert, mais pas tout à fait
    """Un mur qui téléporte les entitées qui le traversent (avec de la magie)."""
    def passage(self,passage:Passage):
        return passage.teleporteur

# Quelques murs pas symétriques

class MurAsymetrique(Mur): # Hérite vraiment ?
    """Un mur pas symétrique."""
    def __init__(self,niveau:int,autre_mur:MurAsymetrique|Type[MurAsymetrique],mur:Mur):
        Mur.__init__(self,niveau)
        self.mur = mur
        if isinstance(autre_mur,MurAsymetrique):
            self.autre_mur = autre_mur
        else :
            self.autre_mur = autre_mur(niveau,self,mur)

    @property
    def ferme(self):
        """Renvoie True si le mur est fermé, False sinon."""
        return self.mur.ferme

    def casser(self):
        self.mur.casser()

    def peut_passer(self,entitee:Entitee):
        return self.mur.peut_passer(entitee)

    def passage(self, passage: Passage) -> bool:
        return self.mur.passage(passage)

class PorteALoquet(MurAsymetrique, Porte):
    """Une porte qui peut s'ouvrir sans clé de l'autre côté"""
    def __init__(self, niveau: int, autre_mur: PorteALoquet | Type[PorteALoquet], mur: Porte, loquet: bool = False):
        self.mur = mur
        if isinstance(autre_mur,PorteALoquet):
            self.autre_mur = autre_mur
        else :
            self.autre_mur = autre_mur(niveau,self,mur,not loquet)
        self.loquet = loquet

    @property
    def ouvert(self):
        """Renvoie True si le mur est ouvert, False sinon."""
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

class Escalier(MurAsymetrique, MurOuvert):
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