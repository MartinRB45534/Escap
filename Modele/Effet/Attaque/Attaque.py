from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Entitee.Agissant.Agissant import Agissant
    from ...Labyrinthe.Case import Case
    from ...Systeme.Elements import Element

# Imports des classes parentes
from ..Effet import One_shot, Delaye

class Attaque_case(One_shot):
    """L'effet d'attaque dans sa version intermédiaire. Créée par une attaque (version générale), chargé d'attacher une attaque particulière aux agissants de la case, en passant d'abord les défenses de la case. Attachée à la case."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="contact",direction:Optional[crt.Direction] = None,autre:Optional[str]=None,taux_autre:Optional[float]=None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.autre = autre
        self.taux_autre = taux_autre
        self.distance = distance

    def action(self,case:Case):
        victime_potentielle = case.agissant
        if victime_potentielle is not None and victime_potentielle not in self.responsable.esprit.get_corps():
            if self.autre is None :
                victime_potentielle.effets.append(Attaque_particulier(self.responsable,self.degats,self.element,self.distance,self.direction))
            elif self.autre == "piercing":
                if self.taux_autre is not None:
                    victime_potentielle.effets.append(Attaque_percante(self.responsable,self.degats,self.element,self.distance,self.direction,self.taux_autre))
                else:
                    warn("L'attaque est percante mais le taux de percement n'est pas défini !")

    def execute(self,case):
        if self.phase == "démarrage":
            self.action(case)
            self.termine()

    def get_skin(self):
        if self.element == Element.TERRE:
            return SKIN_ATTAQUE_TERRE
        elif self.element == Element.FEU:
            return SKIN_ATTAQUE_FEU
        elif self.element == Element.GLACE:
            return SKIN_ATTAQUE_GLACE
        elif self.element == Element.OMBRE:
            return SKIN_ATTAQUE_OMBRE
        else:
            raise ValueError(f"L'élément {self.element} n'a pas de skin associé !")

class Attaque_case_delayee(Attaque_case,Delaye):
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="distance",direction:Optional[crt.Direction] = None,autre:Optional[str]=None,taux_autre:Optional[float]=None):
        Attaque_case.__init__(self,responsable,degats,element,distance,direction,autre,taux_autre)
        self.affiche = False

    def execute(self,case:Case):
        if self.phase == "démarrage":
            pass
        elif self.phase == "en cours":
            self.affiche = True
            self.action(case)
            self.termine()

class Attaque_particulier(One_shot):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="contact",direction:Optional[crt.Direction] = None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.distance = distance

    def action(self,victime:Agissant):
        victime.subit(self.responsable,self.degats,self.distance,self.element)

    def get_skin(self):
        return SKIN_BLESSURE

class Attaque_percante(Attaque_particulier): #Attention ! Perçant pour une attaque signifie qu'elle traverse les defenses. C'est totalement différend pour un item !
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version générale), chargé d'infligé les dégats, en passant d'abord les défenses de la case puis celles de l'agissant. Attachée à la victime. En prime, une partie de ses dégats ne sont pas bloquables."""
    def __init__(self,responsable:Agissant,degats:float,element:Element,distance:str="contact",direction:Optional[crt.Direction] = None,taux_perce:float = 0):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats * taux_perce
        self.degats_imbloquables = degats - self.degats #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction
        self.distance = distance

    def action(self,victime:Agissant):
        self.degats += self.degats_imbloquables
        victime.subit(self.responsable,self.degats,self.distance,self.element)

class Attaque_lumineuse_case(Attaque_case):
    """L'effet de purification. Une attaque de 'lumière'."""
    """L'effet d'attaque dans sa version intermédiaire. Créée par une attaque (version générale), chargé d'attacher une attaque particulière aux agissants de la case, en passant d'abord les défenses de la case. Attachée à la case."""
    def __init__(self,responsable:Agissant,degats:float):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats

    def action(self,case:Case):
        victime_potentielle = case.agissant
        if victime_potentielle is not None and victime_potentielle not in self.responsable.esprit.get_corps():
            if self.autre is None :
                victime_potentielle.effets.append(Attaque_lumineuse_particulier(self.responsable,self.degats))
            else:
                warn("L'attaque lumineuse n'est pas censée avoir d'effet autre !")

    def execute(self,case):
        if self.phase == "démarrage":
            self.action(case)
            self.termine()

    def get_skin(self):
        return SKIN_VIDE
        # Créer le skin de l'attaque lumineuse

class Attaque_lumineuse_particulier(Attaque_particulier):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable:Agissant,degats:float):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats

    def action(self,victime:Agissant):
        victime.subit(self.responsable,self.degats*victime.get_aff(Element.OMBRE)**2,"proximité",Element.OMBRE)

    def get_skin(self):
        return SKIN_BLESSURE

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_BLESSURE, SKIN_ATTAQUE_TERRE, SKIN_ATTAQUE_FEU, SKIN_ATTAQUE_GLACE, SKIN_ATTAQUE_OMBRE, SKIN_VIDE
from warnings import warn