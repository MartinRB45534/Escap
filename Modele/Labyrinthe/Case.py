from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Set, Type
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Effet.Effet import Effet
    from ..Effet.Auras import Aura
    from ..Entitee.Entitee import Mobile, Non_superposable
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Item import Item
    from ..Entitee.Decors.Decors import Decors

class Case(crt.Case):
    def __init__(self,position:crt.Position, aura_elementale: Type[Aura_permanente], opacite:float = 1, niveau:int = 1):
        self.position = position
        self.opacite = opacite
        self.clarte:float = 0
        self.niveau = niveau
        self.repoussante = False
        self.agissant:Optional[Agissant] = None #On peut avoir un agissant sur la case, qui peut être un monstre, un joueur, etc.
        self.decors:Optional[Decors] = None #On peut avoir un décors (mais pas les deux ? à voir)
        self.items:Set[Item] = set() #On peut avoir des items sur la case
        self.effets:Set[Effet] = set() #Les cases ont aussi des effets ! Les auras, par exemple.
        self.auras:Set[Aura] = set() #Les auras sont des effets qui s'appliquent à la case, et qui peuvent être de plusieurs types.
        self.aura_elementale = aura_elementale(self.niveau) #L'aura élémentale est une aura particulière, qui s'applique à la case et qui peut être de plusieurs types.
    #Découvrons le déroulé d'un tour, avec case-chan :

    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! On commence par activer les effets réguliers :
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()
            if effet.phase == "affichage":
                self.effets.remove(effet)
                

    def pseudo_debut_tour(self):
        pass

    #Certains agissants particulièrement tapageurs font un concours de celui qui aura la plus grosse aura (comment ça, cette phrase particulièrement compliquée aura juste servi à faire un jeu de mot sur aura ?)
    def ajoute_aura(self,auras:Set[Aura]=set(),auras_elementales:Set[Aura_elementale]=set()):
        """Fonction qui ajoute un effet d'aura. On décidera de ceux qui s'exécutent plus tard."""
        # Les auras non élémentales s'appliquent si personne n'a d'aura élémentale sur la case (même si l'aura de base de la case a plus de priorité)
        if {aura for aura in self.auras if isinstance(aura, Aura_elementale)} == {self.aura_elementale}:
            self.auras.update(auras)
        # Les auras élémentales s'appliquent si la priorité de la plus importante est supérieure à la priorité de l'aura élémentale en place la plus importante
        if max({aura.priorite for aura in auras_elementales}) > max({aura.priorite for aura in self.auras if isinstance(aura, Aura_elementale)}):
            self.auras = auras | auras_elementales # On vire aussi les auras non élémentales qui appartiennent à d'autres gens

    def arrive(self,entitee:Mobile):
        if isinstance(entitee,Item):
            entitee.set_position(self.position) #Un item passe quoi qu'il arrive
            if isinstance(self.agissant,Non_superposable):
                entitee.heurte_non_superposable(self.agissant) #Mais il heurte les occupants
            elif isinstance(self.decors,Non_superposable):
                entitee.heurte_non_superposable(self.decors)
            self.items.add(entitee)
            return True
        elif isinstance(entitee,Agissant):
            if self.agissant is not None: # On a déjà un agissant sur la case
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement) #On peut peut-être l'écraser
                if ecrasement is not None:
                    if not ecrasement.utilise(self.agissant.get_priorite(),entitee.get_priorite()):
                        return False
                else:
                    return False
            elif isinstance(self.decors,Non_superposable):
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement) #On peut peut-être l'écraser
                if ecrasement is not None:
                    if not ecrasement.utilise(self.decors.get_priorite(),entitee.get_priorite()):
                        return False
                else:
                    return False
            self.agissant = entitee
            entitee.set_position(self.position)
            return True
        raise TypeError("On ne peut pas ajouter un objet de type "+str(type(entitee))+" sur une case !")
    
    def part(self,entitee:Mobile):
        if isinstance(entitee,Item):
            self.items.remove(entitee)
        elif isinstance(entitee,Agissant):
            if self.agissant is not entitee:
                raise ValueError("L'entité "+str(entitee)+" n'est pas sur la case "+str(self))
            self.agissant = None
            return True
        raise TypeError("On ne peut pas enlever un objet de type "+str(type(entitee))+" d'une case !")

    #Tout le monde a fini de se déplacer.
    def post_action(self):
        on_attaques:Set[On_attack] = set()
        attaques:Set[Attaque_case] = set()

        for effet in self.effets:
            if isinstance(effet,On_attack):
                on_attaques.add(effet)
            elif (isinstance(effet,Attaque_case_delayee) and effet.delai > 0):
                effet.execute(self) #On diminue le délai
            elif isinstance(effet,Attaque_case):
                attaques.add(effet)
            elif isinstance(effet,On_post_action): #Les auras non-élémentales sont aussi des On_post_action
                effet.execute(self)

        for aura in self.auras:
            aura.execute(self)

        for attaque in attaques:
            for protection in on_attaques:
                protection.execute(attaque)
            attaque.execute(self)

    def fin_tour(self):
        for effet in self.effets | self.auras:
            if effet.phase == "terminé":
                self.effets.remove(effet)
        if {aura for aura in self.auras if isinstance(aura, Aura_elementale)} == set() or max({aura.priorite for aura in self.auras if isinstance(aura, Aura_elementale)}) < self.aura_elementale.priorite: # Les auras de feu durent plusieurs tours, mais peuvent aussi être arrivée juste grâce à l'aide d'une aura de terre
            self.auras = {self.aura_elementale} # On remet l'aura de base pour le tour suivant

    #Le tour se termine gentiment, et on recommence !

    def get_opacite(self):
        opacite = self.opacite
        for aura in self.auras:
            if isinstance(aura, Modification_opacite):
                opacite *= aura.coef_opacite
        return opacite

    # def get_infos(self,clees:Set[str]): #Est-ce que ce serait plus clair sous forme de dictionnaire ? Ou d'objet ?
    #     return Representation_case(self, self.clarte, self.calcule_code(), self.get_cibles_fermes(clees), self.agissant, self.decors, self.items.copy(), self.get_codes_effets(), self.repoussante)

    # def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
    #     return self.code

    # def get_codes_effets(self) -> List[List[int]]:
    #     effets=[]
    #     for effet in self.effets:
    #         if isinstance(effet,Attaque_case_delayee):
    #             effets.append([effet.responsable,effet.delai,effet.degats])
    #     return effets

# Imports utilisés dans le code
from ..Effet.Auras import Aura_elementale, Aura_permanente, Modification_opacite
from ..Effet.Effet import On_debut_tour, Time_limited, On_attack, On_post_action
from ..Effet.Attaque.Attaque import Attaque_case, Attaque_case_delayee
from ..Systeme.Classe.Classes import trouve_skill
from ..Systeme.Skill.Passif import Skill_ecrasement