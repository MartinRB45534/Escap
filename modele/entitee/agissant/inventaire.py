"""L'inventaire"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from warnings import warn
import random
import carte as crt


# Imports utilisés dans le code (il y en a beaucoup !!!)
from ...commons import EtatsItems
from ..item import Item, Potion, Parchemin, Cle, Equippement, Arme, Bouclier, Armure, Heaume, Anneau, Projectile, Ingredient, Cadavre, Oeuf

# Imports utilisés pour les paramètres par défaut
from ...labyrinthe.absent import CASE_ABSENTE

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .agissant import Agissant
    from ...labyrinthe.case import Case

class Inventaire:
    """L'inventaire d'un agissant. Contient tous les items qu'il possède."""
    def __init__(self,possesseur:Agissant,nb_doigts:int):
        self.possesseur = possesseur #On classe les possessions d'un agissant selon les usages qu'il peut en faire :

        self.items:set[Item] = set()

        self.arme:Optional[Arme] = None #L'arme équipée
        self.bouclier:Optional[Bouclier] = None #Le bouclier équipé
        self.armure:Optional[Armure] = None #L'armure équipée
        self.heaume:Optional[Heaume] = None #Le heaume équipé
        self.anneau:list[Anneau] = [] #Les anneaux équipés
        self.doigts = nb_doigts #Le nombre d'anneaux que l'on peut équiper

    # Les items peuvent être de plusieurs catégories :

    @property
    def potions(self) -> set[Potion]:
        """Les potions peuvent se boire (sans coût de mana)"""
        print("I'm not useless !! !!!")
        return {item for item in self.items if isinstance(item,Potion)}

    @property
    def parchemins(self) -> set[Parchemin]:
        """Les parchemins peuvent s'activer avec du mana"""
        return {item for item in self.items if isinstance(item,Parchemin)}

    @property
    def cles(self) -> set[Cle]:
        """Les clés ouvrent ou ferment les portes"""
        return {item for item in self.items if isinstance(item,Cle)}

    @property
    def equippements(self) -> set[Item]:
        """L'équipement regroupe les armes, les boucliers, les armures, les heaumes et les anneaux"""
        return {item for item in self.items if isinstance(item,Equippement)}

    @property
    def armes(self) -> set[Arme]:
        """Les armes sont utilisées pour attaquer"""
        return {item for item in self.items if isinstance(item,Arme)}

    @property
    def boucliers(self) -> set[Bouclier]:
        """Les boucliers sont utilisés pour se défendre"""
        return {item for item in self.items if isinstance(item,Bouclier)}

    @property
    def armures(self) -> set[Armure]:
        """Les armures ont des effets passifs"""
        return {item for item in self.items if isinstance(item,Armure)}

    @property
    def heaumes(self) -> set[Heaume]:
        """Les heaumes ont des effets passifs"""
        return {item for item in self.items if isinstance(item,Heaume)}

    @property
    def anneaux(self) -> set[Anneau]:
        """Les anneaux ont des effets passifs"""
        return {item for item in self.items if isinstance(item,Anneau)}

    @property
    def projectiles(self) -> set[Projectile]:
        """Les projectiles se lancent (on peut lancer n'importe quoi, techniquement...)"""
        return {item for item in self.items if isinstance(item,Projectile)}

    @property
    def ingredients(self) -> set[Ingredient]:
        """Les ingrédients sont utilisés pour l'alchimie"""
        return {item for item in self.items if isinstance(item,Ingredient)}

    @property
    def cadavres(self) -> set[Cadavre]:
        """Oui, on peut récupérer des cadavres, et alors, circulez, y'a rien à voir..."""
        return {item for item in self.items if isinstance(item,Cadavre)}

    @property
    def oeufs(self) -> set[Oeuf]:
        """Vous n'allez quand même pas me dire que c'est l'oeuf qui vous choque ! Il y a marqué cadavre juste au dessus !"""
        return {item for item in self.items if isinstance(item,Oeuf)}

    def ajoute(self,item:Item):
        #Comme la précédente, mais c'est l'item et non son ID qui est passé en paramètre
        if item.position != crt.POSITION_ABSENTE:
            item.labyrinthe.position_case[item.position].items.remove(item)
            item.position = crt.POSITION_ABSENTE
        self.items.add(item)

    def peut_fournir(self,items:dict[type[Ingredient],int]):
        for item in items:
            if self.quantite(item) < items[item]:
                return False
        return True

    def quantite(self,classe:type[Ingredient]):
        """Indique la quantité d'items correspondants à une classe voulue.""" #Pour les ingrédients des recettes
        res=0
        for item in self.ingredients:
            if isinstance(item,classe) and item.etat == EtatsItems.INTACT:
                res+=1
        return res

    def consomme(self,classe:type[Ingredient]):
        """Consomme un ingrédient lors d'une opération d'alchimie.""" #/!\ Rien à voir avec les consommables !
        for item in self.ingredients:
            if isinstance(item,classe) and item.etat == EtatsItems.INTACT:
                item.etat = EtatsItems.BRISE
                break

    def get_items_visibles(self) -> set[Item]:
        items_visibles:set[Item] = set()
        if self.arme is not None:
            items_visibles.add(self.arme)
        if self.bouclier is not None:
            items_visibles.add(self.bouclier)
        if self.armure is not None:
            items_visibles.add(self.armure)
        if self.heaume is not None:
            items_visibles.add(self.heaume)
        return items_visibles

    def get_arme(self) -> Optional[Arme]:
        return self.arme

    def set_arme(self,arme:Arme):
        self.arme = arme

    def get_bouclier(self) -> Optional[Bouclier]:
        return self.bouclier

    def set_bouclier(self,bouclier:Bouclier):
        self.bouclier = bouclier

    def get_armure(self) -> Optional[Armure]:
        return self.armure

    def set_armure(self,armure:Armure):
        self.armure = armure

    def get_heaume(self) -> Optional[Heaume]:
        return self.heaume

    def set_heaume(self,heaume:Heaume):
        self.heaume = heaume

    def get_anneau(self) -> set[Anneau]:
        return {*self.anneau}

    def set_anneau(self,anneau:Anneau):
        if anneau in self.anneau:
            warn("L'anneau est déjà équipé !")
        else:
            self.anneau.append(anneau)
            if len(self.anneau) > self.doigts:
                self.anneau.pop(0)

    def get_equippement(self) -> set[Item]:
        equippement:set[Item] = {*self.anneau}
        if self.arme is not None:
            equippement.add(self.arme)
        if self.bouclier is not None:
            equippement.add(self.bouclier)
        if self.armure is not None:
            equippement.add(self.armure)
        if self.heaume is not None:
            equippement.add(self.heaume)
        return equippement

    def equippe(self,equippement:set[Item]):
        for item in equippement:
            self.items.add(item)
            if isinstance(item,Arme):
                self.set_arme(item)
            elif isinstance(item,Bouclier):
                self.set_bouclier(item)
            elif isinstance(item,Armure):
                self.set_armure(item)
            elif isinstance(item,Heaume):
                self.set_heaume(item)
            elif isinstance(item,Anneau):
                self.set_anneau(item)

    def desequippe(self,equippement:list[Item]):
        for item in equippement:
            if item is self.arme:
                self.arme = None
            elif item is self.bouclier:
                self.bouclier = None
            elif item is self.armure:
                self.armure = None
            elif item is self.heaume:
                self.heaume = None
            elif item in self.anneau:
                self.anneau.remove(item)

    def get_clees(self) -> set[str]:
        clees:set[str] = set()
        for cle in self.cles:
            for code in cle.codes:
                clees.add(code)
        return clees

    def get_clee(self,code:str) -> Optional[Cle]:
        for cle in self.cles:
            if code in cle.codes:
                return cle

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for item in self.items:
            if item.position != crt.POSITION_ABSENTE or item.etat == EtatsItems.BRISE: #S'il a été lancé ou n'est plus en état
                self.items.remove(item)
                if self.arme is item :
                    self.arme = None
                elif self.bouclier is item :
                    self.bouclier = None
                elif self.armure is item :
                    self.armure = None
                elif self.heaume is item :
                    self.heaume = None
                elif item in self.anneau :
                    self.anneau.remove(item)

    def drop_all(self,case:Case):
        for item in self.items:
            self.drop(item,case)

    def drop(self,item:Item,case:Case=CASE_ABSENTE):
        for item in self.items:
            
            item.position = case.position
            case.items.add(item)
            self.items.remove(item)
            if self.arme is item :
                self.arme = None
            elif self.bouclier is item :
                self.bouclier = None
            elif self.armure is item : 
                self.armure = None
            elif self.heaume is item :
                self.heaume = None
            elif item in self.anneau :
                self.anneau.remove(item)                    

    def drop_random(self,case:Case):
        item = random.choice(list(self.items))
        self.drop(item,case)

    def debut_tour(self):
        for item in self.items:
            item.debut_tour()
        #On ne manipule pas les cadavres
        # for oeuf in self.oeufs: #Mais les oeufs incubent !
        #     hatch:Optional[Hatching] = trouve_skill(oeuf.agissant.classe_principale,Hatching)
        #     if hatch is not None:
        #         if hatch.utilise(): #Et peuvent même éclore !
        #             self.controleur.fait_eclore(oeuf,self.possesseur)# /!\ À coder !

    def pseudo_debut_tour(self):
        for item in self.items :
            item.pseudo_debut_tour()

    def fin_tour(self):
        for item in self.items :
            item.fin_tour() #Moins de choses à faire à la fin du tour.
        self.nettoie_item()

    def a_parchemin_vierge(self):
        for parchemin in self.parchemins:
            if parchemin.impregne is not None:
                return True
        return False

    def get_parchemin_vierge(self):
        for parchemin in self.parchemins:
            if parchemin.impregne is not None:
                return parchemin
        return None
