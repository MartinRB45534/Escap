from __future__ import annotations
from typing import TYPE_CHECKING, Type, Callable
import Affichage as af
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Entitee import Entitee
    from .Passage import Passage

class Mur(crt.Mur):
    def __init__(self,niveau:int):
        self.niveau = niveau
        self.ferme = False

    def casser(self):
        pass

    def peut_passer(self,entitee:Entitee):
        if not self.ferme :
            return True
        return False
    
    def passage(self,passage:Passage):
        raise NotImplementedError("La méthode passage n'est pas implémentée pour cette classe")

class Mur_impassable(Mur):
    def __init__(self,niveau:int):
        super().__init__(niveau)
        self.ferme = True

    def casser(self):
        raise Exception("Impossible de casser un mur impassable")

    def peut_passer(self,entitee:Entitee):
        return False
    
    def passage(self,passage:Passage):
        return False

class Mur_plein(Mur):
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
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)   # ou l'écraser.
            if ecrasement is not None :
                passage = ecrasement.utilise(self.niveau,entitee.get_priorite())
                if passage :
                    self.casser()
                return passage
            else :
                return False
    
    def passage(self,passage:Passage):
        return passage.mur or not self.ferme

class Porte(Mur_plein):
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

class Mur_ouvert(Mur):
    def __init__(self,niveau:int):
        super().__init__(niveau)

    @property
    def ferme(self):
        return False
    
    def casser(self):
        pass

    def peut_passer(self,entitee:Entitee):
        return True
    
    def passage(self,passage:Passage):
        return True

class Barriere(Mur_ouvert):
    def __init__(self,niveau:int,condition:Callable[[Entitee],bool]):
        super().__init__(niveau)
        self.condition = condition

    def peut_passer(self,entitee:Entitee):
        return self.condition(entitee) # Si la condition est remplie, on peut passer
    
    def passage(self,passage:Passage):
        return passage.barriere
    
class Teleporteur(Mur_ouvert): # La seule différence avec un mur ouvert est que les téléporteurs sont affichés différemment
    def __init__(self,niveau:int):
        super().__init__(niveau)

    def passage(self,passage:Passage):
        return passage.teleporteur

# Quelques murs pas symétriques

class Mur_asymétrique(Mur): # Hérite vraiment ?
    def __init__(self,niveau:int,autre_mur:Mur_asymétrique|Type[Mur_asymétrique],mur:Mur):
        self.mur = mur
        if isinstance(autre_mur,Mur_asymétrique):
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
    
class Porte_a_loquet(Mur_asymétrique, Porte):
    """Une porte qui peut s'ouvrir sans clé de l'autre côté"""
    def __init__(self, niveau: int, autre_mur: Porte_a_loquet | Type[Porte_a_loquet], mur: Porte, loquet: bool = False):
        self.mur = mur
        if isinstance(autre_mur,Porte_a_loquet):
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

class Escalier(Mur_asymétrique, Mur_ouvert):
    """Un téléporteur avec une notion graphique de haut et de bas"""
    def __init__(self, niveau: int, autre_mur: Escalier | Type[Escalier], mur: Mur_ouvert, direction: af.Direction_aff = af.Direction_aff.NEXT):
        self.mur = mur
        if isinstance(autre_mur,Escalier):
            self.autre_mur = autre_mur
        else :
            self.autre_mur = autre_mur(niveau,self,mur,direction.oppose)
        self.direction = direction

    def passage(self, passage: Passage):
        return passage.escalier

# Imports utilisés dans le code
from ..Entitee.Entitee import Fantome
from ..Entitee.Agissant.Agissant import Agissant
from ..Systeme.Classe.Classes import trouve_skill
from ..Systeme.Skill.Passif import Skill_ecrasement