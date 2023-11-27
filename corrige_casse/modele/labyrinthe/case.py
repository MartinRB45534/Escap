"""Ce module contient la classe Case, qui représente une case du labyrinthe."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set, Type
import carte as crt

# Imports utilisés dans le code
from ..effet import AttaqueCase, AttaqueCaseDelayee, Opacite, AuraElementale, AuraPermanente, ProtectionCase, OnDebutTourCase, OnPostActionCase, TimeLimited #, OnFinTourCase

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..effet.effet import Effet
    from ..effet.case.aura.aura import Aura
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.item import Item
    from ..entitee.decors.decors import Decors

class Case(crt.Case):
    """Une case du labyrinthe. Elle peut contenir un agissant, un décors, des items, des effets, des auras, et une aura élémentale."""
    def __init__(self,position:crt.Position, aura_elementale: Type[AuraPermanente], opacite:float, niveau:int, responsable:Agissant):
        super().__init__(position)
        self.opacite = opacite
        self.clarte:float = 0
        self.niveau = niveau
        self.repoussante = False
        self.agissant:Optional[Agissant] = None #On peut avoir un agissant sur la case, qui peut être un monstre, un joueur, etc.
        self.decors:Optional[Decors] = None #On peut avoir un décors (mais pas les deux ? à voir)
        self.items:Set[Item] = set() #On peut avoir des items sur la case
        self.effets:Set[Effet] = set() #Les cases ont aussi des effets ! Les auras, par exemple.
        self.auras:Set[Aura] = set() #Les auras sont des effets qui s'appliquent à la case, et qui peuvent être de plusieurs types.
        self.aura_elementale = aura_elementale(self.niveau,responsable) #L'aura élémentale est une aura particulière, qui s'applique à la case et qui peut être de plusieurs types.
    #Découvrons le déroulé d'un tour, avec case-chan :

    def debut_tour(self):
        """Fonction qui s'exécute au début du tour."""
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! On commence par activer les effets réguliers :
        for effet in self.effets:
            if isinstance(effet,TimeLimited):
                effet.wait()
            if isinstance(effet,OnDebutTourCase):
                effet.debut_tour(self) #On exécute divers effets

        for aura in self.auras:
            if isinstance(aura,TimeLimited):
                aura.wait()
            if isinstance(aura,OnDebutTourCase):
                aura.debut_tour(self)

    def pseudo_debut_tour(self): #À quoi ça sert déjà ?
        """Un faux début de tour"""

    #Certains agissants particulièrement tapageurs font un concours de celui qui aura la plus grosse aura (comment ça, cette phrase particulièrement compliquée aura juste servi à faire un jeu de mot sur aura ?)
    def ajoute_aura(self,auras:Set[Aura],auras_elementales:Set[AuraElementale]):
        """Fonction qui ajoute un effet d'aura. On décidera de ceux qui s'exécutent plus tard."""
        # Les auras non élémentales s'appliquent si personne n'a d'aura élémentale sur la case (même si l'aura de base de la case a plus de priorité)
        if {aura for aura in self.auras if isinstance(aura, AuraElementale)} == {self.aura_elementale}:
            self.auras.update(auras)
        # Les auras élémentales s'appliquent si la priorité de la plus importante est supérieure à la priorité de l'aura élémentale en place la plus importante
        if max({aura.priorite for aura in auras_elementales}) > max({aura.priorite for aura in self.auras if isinstance(aura, AuraElementale)}):
            self.auras = auras | auras_elementales # On vire aussi les auras non élémentales qui appartiennent à d'autres gens

    def agissant_arrive(self,entitee:Agissant):
        """Une entitée mobile arrive sur la case."""
        if self.agissant: # On a déjà un agissant sur la case
            if not entitee.arrive_agissant(self.agissant):
                return False
        elif self.decors:
            if not entitee.arrive_decors(self.decors):
                return False
        self.agissant = entitee
        entitee.set_position(self.position)
        return True

    def item_arrive(self,entitee:Item):
        """Une entitée mobile arrive sur la case."""
        entitee.set_position(self.position) #Un item passe quoi qu'il arrive
        if self.agissant:
            entitee.heurte_agissant() #Mais il heurte les occupants
        elif self.decors:
            entitee.heurte_decors()
        self.items.add(entitee)
        return True

    #Tout le monde a fini de se déplacer.
    def post_action(self):
        """Fonction qui s'exécute après les actions des agissants, puis passe aux attaques."""
        on_attaques:Set[ProtectionCase] = set()
        attaques:Set[AttaqueCase] = set()

        for effet in self.effets:
            if isinstance(effet,ProtectionCase):
                on_attaques.add(effet)
            elif isinstance(effet,AttaqueCaseDelayee) and effet.attente:
                pass #On attend, pour l'instant
            elif isinstance(effet,AttaqueCase):
                attaques.add(effet)
            elif isinstance(effet,OnPostActionCase):
                effet.post_action(self)

        for attaque in attaques:
            for protection in on_attaques:
                protection.protege(attaque)
            attaque.attaque(self)

    def fin_tour(self):
        """Fonction qui s'exécute à la fin du tour."""
        for effet in self.effets | self.auras:
            if effet.termine():
                self.effets.remove(effet)
        if {aura for aura in self.auras if isinstance(aura, AuraElementale)} == set() or max({aura.priorite for aura in self.auras if isinstance(aura, AuraElementale)}) < self.aura_elementale.priorite: # Les auras de feu durent plusieurs tours, mais peuvent aussi être arrivée juste grâce à l'aide d'une aura de terre
            self.auras = {self.aura_elementale} # On remet l'aura de base pour le tour suivant

    #Le tour se termine gentiment, et on recommence !

    def get_opacite(self):
        """Calcule l'opacité effective de la case."""
        opacite = self.opacite
        for aura in self.auras:
            if isinstance(aura, Opacite):
                opacite *= aura.gain_opacite # On pourrait additionner
        return opacite

    # def get_infos(self,clees:Set[str]): #Est-ce que ce serait plus clair sous forme de dictionnaire ? Ou d'objet ?
    #     return Representation_case(self, self.clarte, self.calcule_code(), self.get_cibles_fermes(clees), self.agissant, self.decors, self.items.copy(), self.get_codes_effets(), self.repoussante)

    # def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
    #     return self.code

    # def get_codes_effets(self) -> List[List[int]]:
    #     effets=[]
    #     for effet in self.effets:
    #         if isinstance(effet,AttaqueCaseDelayee):
    #             effets.append([effet.responsable,effet.delai,effet.degats])
    #     return effets
