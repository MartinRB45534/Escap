from __future__ import annotations
from typing import TYPE_CHECKING, List, Literal, Optional, Set, Type
from enum import Enum
import Carte as crt
import Affichage as af

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Effet.Effet import Effet
    from ..Effet.Effets_mouvement.Deplacements import Teleport, Escalier
    from ..Entitee.Entitee import Entitee

# Valeurs par défaut des paramètres
from ..Effet.Effets_mouvement.Deplacements import Teleport, Escalier
from ..Effet.Effets_mouvement.Blocages import Porte

class Blocage(Enum):
    """Enumération des types de blocages"""
    IMPASSABLE = "Impassable"
    PLEIN = "Plein"
    PORTE_BARRIERE = "Porte barrière"
    PORTE = "Porte"
    BARRIERE = "Barrière"
    ESCALIER = "Escalier"
    TELEPORTEUR = "Téléporteur"
    AUCUN = "Aucun"


class Mur(crt.Mur):
    def __init__(self,cible:crt.Position,niveau:int):
        self.teleport: Optional[Teleport] = Teleport(cible) if cible is not crt.POSITION_ABSENTE else None
        self.blocage: Optional[On_try_through] = None
        self.effets: Set[Effet] = set()
        self.niveau = niveau
        self.controleur = None

    @property
    def ferme(self):
        return self.get_blocage(set()) not in [Blocage.AUCUN,Blocage.ESCALIER,Blocage.TELEPORTEUR]

    def is_ferme(self,clees:List[str]=[]):
        return self.ferme or (isinstance(self.blocage,Porte) and not(self.blocage.code in clees))

    def get_blocage(self,clees:Set[str]):
        if isinstance(self.blocage,Mur_impassable):
            return Blocage.IMPASSABLE
        elif isinstance(self.blocage,Mur_plein) and not(self.blocage.casse):
            return Blocage.PLEIN
        elif isinstance(self.blocage,Porte_barriere) and self.blocage.ferme and not(self.blocage.code in clees):
            return Blocage.PORTE_BARRIERE
        elif isinstance(self.blocage,Porte) and self.blocage.ferme and not(self.blocage.code in clees):
            return Blocage.PORTE
        elif isinstance(self.blocage,Barriere):
            return Blocage.BARRIERE
        elif isinstance(self.teleport,Escalier):
            return Blocage.ESCALIER
        elif isinstance(self.teleport,Teleport) and self.teleport.affiche:
            return Blocage.TELEPORTEUR
        else:
            return Blocage.AUCUN

    @property
    def touchable(self):
        return not isinstance(self.blocage,Mur_impassable)

    def veut_passer(self,intrus:Entitee):
        if self.blocage is not None:
            if self.blocage.execute(self,intrus) #On vérifie que rien n'empêche le passage de l'intrus
                if self.teleport is not None:
                    self.teleport.execute(intrus) #Il est conseillé d'avoir un seul effet de déplacement, comme un seul effet d'autorisation de passage...
        elif isinstance(intrus,Item):
            intrus.heurte_mur()

    @property
    def porte(self):
        assert isinstance(self.blocage,Porte)
        return self.blocage

    @property
    def peut_voir(self):
        visible = True
        for effet in self.effets :
            if (isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and effet.ferme)) or (isinstance(effet,Teleport) and effet.affiche):
                visible = False
        return visible

    def interdit(self):
        self.blocage = Mur_impassable(self.niveau)

    def construit(self):
        self.blocage = Mur_plein(self.niveau)

    def detruit(self):
        self.blocage = None

    def brise(self):
        if not isinstance(self.blocage,Mur_impassable):
            self.blocage = None

    def cree_porte(self,code:str,porte:Type[Porte]=Porte):
        self.brise()
        if self.blocage is None:
            self.blocage = porte(code,self.niveau)

    def get_trajet(self):
        if isinstance(self.teleport,Escalier):
            if self.teleport.sens is af.Direction_aff.NEXT:
                return "Escalier montant"
            else:
                return "Escalier descendant"
        elif isinstance(self.teleport,Teleport):
            return"Téléporteur"
        else:
            return "Aucun"

    def get_cible(self):
        if self.teleport is not None:
            return self.teleport.position
        else:
            return crt.POSITION_ABSENTE

    def get_cible_ferme(self,clees:Set[str]) -> List[crt.Position|Literal[False]]:
        return [self.get_cible_ferme_simple(),self.get_cible_ferme_portes(clees),self.get_cible_ferme_portails(),self.get_cible_ferme_portes_portails(clees),self.get_cible_ferme_escaliers(clees)]

    def get_cible_ferme_simple(self):
        """Renvoie la position de la case d'arrivée si on est un mur ouvert sans téléporteur, False sinon"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not effet.affiche :
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and effet.ferme):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portes(self,clees:Set[str]):
        """Renvoie aussi la position si le mur est une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not effet.affiche :
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portails(self):
        """Renvoie aussi la position si le mur est un téléporteur (mais pas s'il est une porte)"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not isinstance(effet,Escalier):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and effet.ferme):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portes_portails(self,clees:Set[str]):
        """Renvoie aussi la position si le mur est un téléporteur ou une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not isinstance(effet,Escalier):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_escaliers(self,clees:Set[str]):
        """Renvoie aussi la position si le mur est un téléporteur ou une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def set_cible(self,position:crt.Position,surnaturel=False,portail:Type[Teleport]=Teleport):
        self.teleport = portail(position,surnaturel)

    def set_escalier(self,position:crt.Position,sens:af.Direction_aff,escalier:Type[Escalier]=Escalier):
        self.teleport = escalier(position,sens)

# Imports utilisés dans le code
from ..Effet.Effet import On_try_through
from ..Effet.Effets_mouvement.Blocages import Mur_impassable, Mur_plein, Porte, Porte_barriere, Barriere
from ..Effet.Effets_mouvement.Deplacements import Teleport
from ..Entitee.Item.Item import Item