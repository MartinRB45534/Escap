from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Type, List, Dict, Set

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Item.Item import Item

# Pas de classe parente

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Inventaire:

    def __init__(self,possesseur:Agissant,nb_doigts:int,controleur:Controleur):
        self.possesseur = possesseur #On classe les possessions d'un agissant selon les usages qu'il peut en faire :

        self.potions:Set[Potion] = set() #Les potions peuvent se boire
        self.parchemins:Set[Parchemin] = set() #Les parchemins peuvent s'activer avec du mana
        self.cles:Set[Cle] = set() #Les clés ouvrent les portes
        self.armes:Set[Arme] = set() #Les armes s'équippent et sont utilisées pour attaquer
        self.boucliers:Set[Bouclier] = set() #Les boucliers s'équippent et sont utilisés pour se défendre
        self.armures:Set[Armure] = set() #Les armures s'équippent et ont des effets passifs
        self.haumes:Set[Haume] = set() #Les haumes s'équippent et ont des effets passifs
        self.anneaux:Set[Anneau] = set() #Les anneaux s'équippent et ont des effets passifs
        self.projectiles:Set[Projectile] = set() #Les projectiles se lancent (on peut lancer n'importe quoi, techniquement...)
        self.ingredients:Set[Ingredient] = set() #Les ingrédients sont utilisés pour les recettes
        self.cadavres:Set[Cadavre] = set() #Oui, on peut récupérer des cadavres, et alors, circluez, ya rien à voir...
        self.oeufs:Set[Oeuf] = set() #Vous allez quand même pas me dire que c'est l'oeuf qui vous choque ! Il y a marqué cadavre juste au dessus !

        self.items:Dict[Type[Potion|Parchemin|Cle|Arme|Bouclier|Armure|Haume|Anneau|Projectile|Ingredient|Cadavre|Oeuf],Set] = {
            Potion:self.potions,
            Parchemin:self.parchemins,
            Cle:self.cles,
            Arme:self.armes,
            Bouclier:self.boucliers,
            Armure:self.armures,
            Haume:self.haumes,
            Anneau:self.anneaux,
            Projectile:self.projectiles,
            Ingredient:self.ingredients,
            Cadavre:self.cadavres,
            Oeuf:self.oeufs,
        }
        # self.kiiz:List[Type[Potion|Parchemin|Cle|Arme|Bouclier|Armure|Haume|Anneau|Projectile|Ingredient|Cadavre|Oeuf]] = [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient,Cadavre,Oeuf]
        self.arme:Optional[Arme] = None #L'arme équipée
        self.bouclier:Optional[Bouclier] = None #Le bouclier équipé
        self.armure:Optional[Armure] = None #L'armure équipée
        self.haume:Optional[Haume] = None #Le haume équipé
        self.anneau:List[Anneau] = [] #Les anneaux équipés
        self.doigts = nb_doigts #Le nombre d'anneaux que l'on peut équiper
        self.controleur = controleur

    def ajoute(self,item:Item):
        #Comme la précédente, mais c'est l'item et non son ID qui est passé en paramètre
        item.position = ABSENT
        classe = item.get_classe()
        if classe in self.items:
            self.items[classe].add(item)

    def peut_fournir(self,items:Dict[Type[Ingredient],int]):
        for item in items:
            if self.quantite(item) < items[item]:
                return False
        return True

    def quantite(self,classe:Type[Ingredient]):
        """Indique la quantité d'items correspondants à une classe voulue.""" #Pour les ingrédients des recettes
        res=0
        for item in self.ingredients:
            if isinstance(item,classe) and item.etat == "intact":
                res+=1
        return res

    def consomme(self,classe:Type[Ingredient]):
        """Consomme un ingrédient lors d'une opération d'alchimie.""" #/!\ Rien à voir avec les consommables !
        for item in self.ingredients:
            if isinstance(item,classe) and item.etat == "intact":
                item.etat = "brisé"
                break
    
    def get_item_courant(self) -> Item:
        raise NotImplementedError

    def get_items_visibles(self) -> Set[Item]:
        items_visibles:Set[Item] = set()
        if self.arme is not None:
            items_visibles.add(self.arme)
        if self.bouclier is not None:
            items_visibles.add(self.bouclier)
        if self.armure is not None:
            items_visibles.add(self.armure)
        if self.haume is not None:
            items_visibles.add(self.haume)
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

    def get_haume(self) -> Optional[Haume]:
        return self.haume

    def set_haume(self,haume:Haume):
        self.haume = haume

    def get_anneau(self) -> Set[Anneau]:
        return {*self.anneau}

    def set_anneau(self,anneau:Anneau):
        if anneau in self.anneau:
            warn("L'anneau est déjà équipé !")
        else:
            self.anneau.append(anneau)
            if len(self.anneau) > self.doigts:
                self.anneau.pop(0)

    def get_equippement(self) -> Set[Item]:
        equippement:Set[Item] = {*self.anneau}
        if self.arme is not None:
            equippement.add(self.arme)
        if self.bouclier is not None:
            equippement.add(self.bouclier)
        if self.armure is not None:
            equippement.add(self.armure)
        if self.haume is not None:
            equippement.add(self.haume)
        return equippement

    def equippe(self,equippement:Set[Item]):
        for item in equippement:
            if isinstance(item,Arme):
                self.armes.add(item)
                self.set_arme(item)
            elif isinstance(item,Bouclier):
                self.boucliers.add(item)
                self.set_bouclier(item)
            elif isinstance(item,Armure):
                self.armures.add(item)
                self.set_armure(item)
            elif isinstance(item,Haume):
                self.haumes.add(item)
                self.set_haume(item)
            elif isinstance(item,Anneau):
                self.anneaux.add(item)
                self.set_anneau(item)

    def desequippe(self,equippement:List[Item]):
        for item in equippement:
            if isinstance(item,Arme):
                if item is self.arme:
                    self.arme = None
            elif isinstance(item,Bouclier):
                if item is self.bouclier:
                    self.bouclier = None
            elif isinstance(item,Armure):
                if item is self.armure:
                    self.armure = None
            elif isinstance(item,Haume):
                if item is self.haume:
                    self.haume = None
            elif isinstance(item,Anneau):
                if item in self.anneau:
                    self.anneau.remove(item)

    def get_clees(self) -> Set[str]:
        clees:Set[str] = set()
        for cle in self.cles:
            for code in cle.codes:
                clees.add(code)
        return clees

    def get_clee(self,code:str) -> Optional[Cle]:
        for cle in self.cles:
            if code in cle.codes:
                return cle

    def get_items(self):
        items:Set[Item] = set()
        for item_set in self.items.values():
            items|=item_set            
        return items

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for classe in self.items:
            for item in self.items[classe]:
                assert isinstance(item,classe)
                if item.position != ABSENT or item.etat == "brisé": #S'il a été lancé ou n'est plus en état
                    self.items[classe].remove(item)
                    if self.arme is item :
                        self.arme = None
                    elif self.bouclier is item :
                        self.bouclier = None
                    elif self.armure is item :
                        self.armure = None
                    elif self.haume is item :
                        self.haume = None
                    elif item in self.anneau :
                        self.anneau.remove(item)

    def drop_all(self,position:Position):
        for classe in self.items:
            for item in self.items[classe]:
                self.drop(position,item)

    def drop(self,position:Position,item:Item):
        for cat_item in self.items:
            if item in self.items[cat_item]:
                self.controleur.items_courants.add(item)
                item.position = position
                self.items[cat_item].remove(item)
                if self.arme is item :
                    self.arme = None
                elif self.bouclier is item :
                    self.bouclier = None
                elif self.armure is item : 
                    self.armure = None
                elif self.haume is item :
                    self.haume = None
                elif item in self.anneau :
                    self.anneau.remove(item)                    

    def drop_random(self,position:Position):
        items = self.get_items()
        item = random.choice(list(items))
        self.drop(position,item)

    def debut_tour(self):
        for classe in self.items:
            for item in self.items[classe]:
                item.debut_tour()
        #On ne manipule pas les cadavres
        # for oeuf in self.oeufs: #Mais les oeufs incubent !
        #     hatch:Optional[Hatching] = trouve_skill(oeuf.agissant.classe_principale,Hatching)
        #     if hatch is not None:
        #         if hatch.utilise(): #Et peuvent même éclore !
        #             self.controleur.fait_eclore(oeuf,self.possesseur)# /!\ À coder !

    def pseudo_debut_tour(self):
        items:Set[Item] = set()
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items |= self.items[cat_item]
        for item in items :
            item.pseudo_debut_tour()

    def fin_tour(self):
        items:Set[Item] = set()
        for item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items |= self.items[item]
        for item in items :
            item.fin_tour() #Moins de choses à faire à la fin du tour.
        self.nettoie_item()

    def a_parchemin_vierge(self):
        for parchemin in self.items[Parchemin]:
            if isinstance(parchemin,Parchemin_vierge) and isinstance(parchemin.action_portee,Impregne) and parchemin.action_portee.magie is None:
                return True
        return False
    
    def get_parchemin_vierge(self):
        for parchemin in self.items[Parchemin]:
            if isinstance(parchemin,Parchemin_vierge) and isinstance(parchemin.action_portee,Impregne) and parchemin.action_portee.magie is None:
                return parchemin
        return None

    # def consomme_parchemin_vierge(self):
    #     for parchemin in self.items[Parchemin]:
    #         if isinstance(parchemin,Parchemin_vierge):
    #             parchemin.etat = "brisé"
    #             return True
    #     return False

# Imports utilisés dans le code (il y en a beaucoup !!!)
from Jeu.Action.Non_skill import Impregne
from Jeu.Entitee.Item.Item import Item
from Jeu.Entitee.Item.Potion.Potion import Potion
from Jeu.Entitee.Item.Parchemin.Parchemin import Parchemin
from Jeu.Entitee.Item.Cle import Cle
from Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme
from Jeu.Entitee.Item.Equippement.Degainable.Bouclier.Bouclier import Bouclier
from Jeu.Entitee.Item.Equippement.Armure.Armure import Armure
from Jeu.Entitee.Item.Equippement.Haume.Haume import Haume
from Jeu.Entitee.Item.Equippement.Anneau.Anneau import Anneau
from Jeu.Entitee.Item.Projectile.Projectile import Projectile
from Jeu.Entitee.Item.Item import Ingredient
from Jeu.Entitee.Item.Cadavre import Cadavre
from Jeu.Entitee.Item.Oeuf import Oeuf
from Jeu.Entitee.Item.Parchemin.Parchemins import Parchemin_vierge

from Jeu.Systeme.Classe.Classes import trouve_skill
# from Jeu.Systeme.Skill.Skills import Hatching
from warnings import warn
import random