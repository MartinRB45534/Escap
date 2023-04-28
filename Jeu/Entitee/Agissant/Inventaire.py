from __future__ import annotations
from typing import Type, TYPE_CHECKING
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Entitee import Entitee
    from Jeu.Entitee.Item.Item import Item
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

from Jeu.Entitee.Item.Items import Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient,Cadavre,Oeuf,Consommable,Parchemin_vierge
from Jeu.Systeme.Classe import *

class Inventaire:

    def __init__(self,ID_possesseur:int,nb_doigts:int):
        self.possesseur = ID_possesseur #On classe les possessions d'un agissant selon les usages qu'il peut en faire :
        self.items = {Potion:[], #Une potion peut se boire
                      Parchemin:[], #Un parchemin peut s'activer avec du mana
                      Cle:[], #Les clés ouvrent les portes
                      Arme:[], #Les armes s'équippent et sont utilisées pour attaquer
                      Bouclier:[], #Les boucliers s'équippent et sont utilisés pour se défendre
                      Armure:[], #Les armures s'équippent et ont des effets passifs
                      Haume:[], #Les haumes s'équippent et ont des effets passifs
                      Anneau:[], #Les anneaux s'équippent et ont des effets passifs
                      Projectile:[], #Les projectiles se lancent (on peut lancer n'importe quoi, techniquement...)
                      Ingredient:[],
                      Cadavre:[], #Oui, on peut récupérer des cadavres, et alors, circluez, ya rien à voir...
                      Oeuf:[] #Vous allez quand même pas me dire que c'est l'oeuf qui vous choque ! Il y a marqué cadavre juste au dessus !
                      }
        self.kiiz:List[Type[Item]] = [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient,Cadavre,Oeuf]
        self.arme = None #L'arme équipée
        self.bouclier = None #Le bouclier équipé
        self.armure = None #L'armure équipée
        self.haume = None #Le haume équipé
        self.anneau = [None]*nb_doigts #Les anneaux équipés
        self.controleur = None

    def active(self,controleur: Controleur):
        self.controleur = controleur
        for key in self.items.keys():
            for item in self.items[key]:
                self.controleur[item].active(controleur)

    def desactive(self):
        for key in self.items.keys():
            for item in self.items[key]:
                self.controleur[item].desactive()
        self.controleur = None
        
    def ramasse_item(self,ID_item: int):
        """
        Fonction qui gère le ramassage d'un item
        Entrée:
            -l'ID de l'item à ramasser
        """
        item = self.controleur[ID_item]
        item.position = None
        self.items[item.get_classe()].append(ID_item)

    def ajoute(self,item:Item):
        #Comme la précédente, mais c'est l'item et non son ID qui est passé en paramètre
        item.position = None
        self.items[item.get_classe()].append(item.ID)

    def utilise_item(self,ID_item:int):
        """Appelé en appuyant sur la touche espace, utilise l'item actuellement sélectionné."""
        ###L'utilisation varie beaucoup selon le type d'item :
        if ID_item != None:
            item:Item = self.controleur[ID_item]
            if isinstance(item,Consommable): #Un consommable se consomme (si c'est un parchemin, l'activation peut échouer)
                item.utilise(self.controleur[self.possesseur])
            elif isinstance(item,Arme): #Un équipable s'équipe. Il y a certaines conditions.
                self.set_arme(ID_item)
            elif isinstance(item,Bouclier):
                self.set_bouclier(ID_item)
            elif isinstance(item,Armure):
                self.set_armure(ID_item)
            elif isinstance(item,Haume):
                self.set_haume(ID_item)
            elif isinstance(item,Anneau):
                self.set_anneau(ID_item)

    def peut_fournir(self,items:List):
        for item in items:
            if self.quantite(item) < items[item]:
                return False
        return True

    def quantite(self,classe:Type):
        """Indique la quantité d'items correspondants à une classe voulue.""" #Pour les ingrédients des recettes
        res=0
        for ID in self.items[Ingredient]:
            item:Item = self.controleur[ID]
            if isinstance(item,classe) and item.etat == "intact":
                res+=1
        return res

    def consomme(self,classe):
        """Consomme un ingrédient lors d'une opération d'alchimie.""" #/!\ Rien à voir avec les consommables !
        for ID in self.items[Ingredient]:
            item:Item = self.controleur[ID]
            if isinstance(item,classe) and item.etat == "intact":
                item.etat = "brisé"
                break

    def get_items_visibles(self):
        items_visibles:List[int] = []
        if self.arme != None:
            items_visibles.append(self.arme)
        if self.bouclier != None:
            items_visibles.append(self.bouclier)
        if self.armure != None:
            items_visibles.append(self.armure)
        if self.haume != None:
            items_visibles.append(self.haume)
        return items_visibles

    def get_arme(self):
        return self.arme

    def set_arme(self,ID:int):
        item:Item = self.controleur[ID]
        if isinstance(item,Arme):
            self.arme = ID

    def get_bouclier(self):
        return self.bouclier

    def set_bouclier(self,ID:int):
        item:Item = self.controleur[ID]
        if isinstance(item,Bouclier):
            self.bouclier = ID

    def get_armure(self):
        return self.armure

    def set_armure(self,ID:int):
        item:Item = self.controleur[ID]
        if isinstance(item,Armure):
            self.armure = ID

    def get_haume(self):
        return self.haume

    def set_haume(self,ID:int):
        item:Item = self.controleur[ID]
        if isinstance(item,Haume):
            self.haume = ID

    def get_anneau(self):
        return self.anneau

    def set_anneau(self,ID:int):
        item:Item = self.controleur[ID]
        if isinstance(item,Anneau):
            if ID in self.anneau:
                self.anneau.remove(ID)
                self.anneau.append(None)
            else :
                for i in range(len(self.anneau)-1,0,-1):
                    self.anneau[i]=self.anneau[i-1]
                self.anneau[0]=ID

    def get_equippement(self):
        equippement = []
        if self.arme != None:
            equippement.append(self.arme)
        if self.bouclier != None:
            equippement.append(self.bouclier)
        if self.armure != None:
            equippement.append(self.armure)
        if self.haume != None:
            equippement.append(self.haume)
        for anneau in self.anneau:
            if anneau != None:
                equippement.append(anneau)
        return equippement

    def equippe(self,equippement:List[Item]):
        for item in equippement:
            ID = item.ID
            if isinstance(item,Arme):
                if not ID in self.items[Arme]:
                    self.items[Arme].append(ID)
                self.arme = ID
            elif isinstance(item,Bouclier):
                if not ID in self.items[Bouclier]:
                    self.items[Bouclier].append(ID)
                self.bouclier = ID
            elif isinstance(item,Armure):
                if not ID in self.items[Armure]:
                    self.items[Armure].append(ID)
                self.armure = ID
            elif isinstance(item,Haume):
                if not ID in self.items[Haume]:
                    self.items[Haume].append(ID)
                self.haume = ID
            elif isinstance(item,Anneau):
                if not ID in self.items[Anneau]:
                    self.items[Anneau].append(ID)
                if not ID in self.anneau:
                    for i in range(len(self.anneau)-1,0,-1):
                        self.anneau[i]=self.anneau[i-1]
                    self.anneau[0]=ID

    def desequippe(self,equippement:List[Item]):
        for item in equippement:
            ID = item.ID
            if isinstance(item,Arme):
                if ID == self.arme:
                    self.arme = None
            elif isinstance(item,Bouclier):
                if ID == self.bouclier:
                    self.bouclier = None
            elif isinstance(item,Armure):
                if ID == self.armure:
                    self.armure = None
            elif isinstance(item,Haume):
                if ID == self.haume:
                    self.haume = None
            elif isinstance(item,Anneau):
                if ID in self.anneau:
                    self.anneau.remove(ID)
                    self.anneau.append(None)

    def get_clees(self):
        clees:List[int] = []
        for ID_cle in self.items[Cle]:
            cle:Cle = self.controleur[ID_cle]
            for code in cle.codes:
                clees.append(code)
        return clees

    def get_clee(self,code):
        cle = None
        for ID_cle in self.items[Cle]:
            if code in self.controleur[ID_cle].codes:
                cle = ID_cle
        return cle

    def get_items(self):
        items:List[Entitee] = []
        for kii in self.kiiz:
            for ID in self.items[kii]:
                items.append(self.controleur[ID])
        return items

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for cat in range(10): #On parcourt les catégories
            items = self.items[self.kiiz[cat]]
            for nb_item in range(len(items)-1,-1,-1): #On parcourt les items
                ID_item = items[nb_item]
                item:Item = self.controleur[ID_item]
                if item.position != None or item.etat == "brisé": #S'il a été lancé ou n'est plus en état
                    items.remove(ID_item)

                    if self.arme == ID_item :
                        self.arme = None
                    elif self.bouclier == ID_item :
                        self.bouclier = None
                    elif self.armure == ID_item :
                        self.armure = None
                    elif self.haume == ID_item :
                        self.haume = None
                    else :
                        for doigt in range(len(self.anneau)):
                            if self.anneau[doigt] == ID_item :
                                self.anneau[doigt] = None #Quel genre d'imbécile briserait ou lancerait son équippement ? Enfin...

    def drop_all(self,position:Position):
        for cat_item in self.kiiz : #On drop aussi les cadavres et les oeufs
            for ID_item in self.items[cat_item]:
                self.drop(position,ID_item)
                item:Item = self.controleur[ID_item]
                self.controleur.entitees_courantes.append(ID_item)
                item.position = position
            self.items[cat_item]=[]
        self.arme = None
        self.bouclier = None
        self.armure = None
        self.haume = None
        self.anneau = [None] * len(self.anneau)

    def drop(self,position:Position,ID_item:int):
        for cat_item in self.kiiz :
            if ID_item in self.items[cat_item]:
                item:Item = self.controleur[ID_item]
                self.controleur.entitees_courantes.append(ID_item)
                item.position = position
                self.items[cat_item].remove(ID_item)
                if self.arme == ID_item :
                    self.arme = None
                elif self.bouclier == ID_item :
                    self.bouclier = None
                elif self.armure == ID_item :
                    self.armure = None
                elif self.haume == ID_item :
                    self.haume = None
                else :
                    for doigt in range(len(self.anneau)):
                        if self.anneau[doigt] == ID_item :
                            self.anneau[doigt] = None

    def debut_tour(self):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item:Item = self.controleur[ID_item]
            item.debut_tour()
            if item.etat == "suspens":
                item.utilise(self.controleur[self.possesseur])
        #On ne manipule pas les cadavres
        for ID_oeuf in self.items[Oeuf]: #Mais les oeufs incubent !
            oeuf:Agissant = self.controleur[ID_oeuf]
            hatch:Hatching = trouve_skill(oeuf.classe_principale,Hatching)
            if hatch != None:
                if hatch.utilise(): #Et peuvent même éclore !
                    self.controleur.fait_eclore(oeuf,self.possesseur)# /!\ À coder !

    def pseudo_debut_tour(self):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item:Item = self.controleur[ID_item]
            item.pseudo_debut_tour()

    def fin_tour(self):
        items = []
        for item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items += self.items[item]
        for ID_item in items :
            item:Item = self.controleur[ID_item]
            item.fin_tour() #Moins de choses à faire à la fin du tour.
        self.nettoie_item()

    def a_parchemin_vierge(self):
        for ID_parch in self.items[Parchemin]:
            if isinstance(self.controleur[ID_parch],Parchemin_vierge):
                return True
        return False

    def consomme_parchemin_vierge(self):
        for ID_parch in self.items[Parchemin]:
            parch:Parchemin = self.controleur[ID_parch]
            if isinstance(parch,Parchemin_vierge):
                parch.etat = "brisé"
                return True
        return False

from Jeu.Entitee.Item.Items import Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient,Cadavre,Oeuf,Consommable,Parchemin_vierge
from Jeu.Systeme.Classe import *