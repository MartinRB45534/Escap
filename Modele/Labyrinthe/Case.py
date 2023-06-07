from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Set, Dict
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Effet.Effet import Effet
    from ..Effet.Auras import Aura
    from ..Entitee.Entitee import Entitee, Mobile
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Item.Item import Item
    from ..Entitee.Decors.Decor import Decors
    from .Mur import Mur

# Valeurs par défaut des paramètres
from ..Systeme.Elements import Element

class Case(crt.Case):
    def __init__(self,position:crt.Position, opacite = 1, niveau = 1, element = Element.TERRE):
        # Par défaut, pas de murs.
        self.position = position
        self.opacite = opacite
        self.opacite_bonus:float = 0
        self.clarte:float = 0
        self.niveau = niveau
        self.element = element
        self.code = 0
        self.repoussante = False
        self.agissant:Optional[Agissant] = None #On peut avoir un agissant sur la case, qui peut être un monstre, un joueur, etc.
        self.decors:Optional[Decors] = None #On peut avoir un décors (mais pas les deux ? à voir)
        self.items:Set[Item] = set() #On peut avoir des items sur la case
        self.effets:Set[Effet] = set() #Les cases ont aussi des effets ! Les auras, par exemple.
        self.auras:Set[Aura] = set() #Les auras sont des effets qui s'appliquent à la case, et qui peuvent être de plusieurs types.
        if self.element == Element.TERRE:
            self.auras.add(Terre_permanente(self.niveau*2))
        elif self.element == Element.FEU:
            self.auras.add(Feu_permanent(self.niveau,self.niveau*5))
        elif self.element == Element.GLACE:
            self.auras.add(Glace_permanente(self.niveau,self.niveau/10))
        elif self.element == Element.OMBRE:
            self.auras.add(Ombre_permanente(self.niveau,self.niveau/2))

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
        self.code = 0
        priorite_max = 0
        IDmax = 0
        auras:Dict[int,List[Aura_elementale]] = {}

        for aura in self.auras:
            if isinstance(aura,Aura_elementale):
                ID = aura.responsable
                if ID in auras : # On a déjà une aura de ce type
                    auras[ID].append(aura)
                else:
                    auras[ID]=[aura]
                prio = aura.priorite
                if prio > priorite_max : # On a un nouveau gagnant !
                    IDmax = ID
                    priorite_max = prio

        for aura in auras[IDmax]:
            if isinstance(aura,(Terre,Terre_permanente)):
                self.code += 1
            elif isinstance(aura,(Feu,Feu_permanent)):
                self.code += 2
            elif isinstance(aura,(Glace,Glace_permanente)):
                self.code += 4
            elif isinstance(aura,(Ombre,Ombre_permanente)):
                self.code += 8

    #Certains agissants particulièrement tapageurs font un concours de celui qui aura la plus grosse aura (comment ça, cette phrase particulièrement compliquée aura juste servi à faire un jeu de mot sur aura ?)
    def ajoute_aura(self,aura:Aura):
        """Fonction qui ajoute un effet d'aura. On décidera de ceux qui s'exécutent plus tard."""
        self.auras.add(aura)
        if isinstance(aura,Aura_elementale): #On a besoin de savoir quelle aura prévaudra
            aura.priorite += self.clarte/2 #La clarté vient d'être utilisée pour déterminer la portée de l'aura, et n'est normalement pas encore réinitialisée
            if isinstance(aura,Feu):
                resp = aura.responsable
                for aura_bis in self.effets:
                    if isinstance(aura_bis,Feu) and aura_bis.responsable == resp :
                        aura_bis.phase = "terminé"

    def step_out(self,entitee:Entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_out):
                effet.execute(entitee)

    def step_in(self,entitee:Entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_in):
                effet.execute(entitee) #On agit sur les agissants qui arrivent (pièges, téléportation, etc.)

    #Tout le monde a fini de se déplacer.
    def post_action(self):
        self.opacite_bonus = 0 # On reset ça à chaque tour, sinon ça va devenir tout noir
        self.code = 0
        on_attaques:Set[On_attack] = set()
        attaques:Set[Attaque_case] = set()
        priorite_max = 0
        IDmax = 0
        auras:Dict[int,List[Aura_elementale]] = {}

        for aura in self.auras:
            if isinstance(aura,Aura_elementale):
                ID = aura.responsable
                if ID in auras : # On a déjà une aura de ce type
                    auras[ID].append(aura)
                else:
                    auras[ID]=[aura]
                prio = aura.priorite
                if prio > priorite_max : # On a un nouveau gagnant !
                    IDmax = ID
                    priorite_max = prio
        for effet in self.effets:
            if isinstance(effet,On_attack):
                on_attaques.add(effet)
            elif (isinstance(effet,Attaque_case_delayee) and effet.delai > 0):
                effet.execute(self) #On diminue le délai
            elif isinstance(effet,Attaque_case):
                attaques.add(effet)
            elif isinstance(effet,On_post_action): #Les auras non-élémentales sont aussi des On_post_action
                effet.execute(self)

        for aura in auras[IDmax]:
            aura.execute(self)

        for attaque in attaques:
            for protection in on_attaques:
                protection.execute(attaque)
            attaque.execute(self)

    def fin_tour(self):
        for effet in self.effets:
            if effet.phase == "terminé":
                self.effets.remove(effet)

    #Le tour se termine gentiment, et on recommence !

    def get_opacite(self):
        return self.opacite + self.opacite_bonus

    def get_infos(self,clees:Set[str]): #Est-ce que ce serait plus clair sous forme de dictionnaire ? Ou d'objet ?
        return Representation_case(self, self.clarte, self.calcule_code(), self.get_cibles_fermes(clees), self.agissant, self.decors, self.items.copy(), self.get_codes_effets(), self.repoussante)

    def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
        return self.code

    def get_codes_effets(self) -> List[List[int]]:
        effets=[]
        for effet in self.effets:
            if isinstance(effet,Attaque_case_delayee):
                effets.append([effet.responsable,effet.delai,effet.degats])
        return effets

# Imports utilisés dans le code
from .Labyrinthe.Vue import Representation_case
from .Effet.Auras import Terre_permanente, Feu_permanent, Glace_permanente, Ombre_permanente, Aura_elementale, Terre, Feu, Glace, Ombre
from .Effet.Effet import On_debut_tour, Time_limited, On_attack, On_post_action, On_step_in, On_step_out
from .Effet.Attaque.Attaque import Attaque_case, Attaque_case_delayee