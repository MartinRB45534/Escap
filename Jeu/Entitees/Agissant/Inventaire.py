
class Inventaire:

    def __init__(self,ID_possesseur,nb_doigts):
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
        self.kiiz = [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient,Cadavre,Oeuf]
        self.arme = None #L'arme équipée
        self.bouclier = None #Le bouclier équipé
        self.armure = None #L'armure équipée
        self.haume = None #Le haume équipé
        self.anneau = [None]*nb_doigts #Les anneaux équipés
        self.controleur = None

    def active(self,controleur):
        self.controleur = controleur
        for key in self.items.keys():
            for item in self.items[key]:
                controleur.get_entitee(item).active(controleur)

    def desactive(self):
        for key in self.items.keys():
            for item in self.items[key]:
                self.controleur.get_entitee(item).desactive()
        self.controleur = None
        
    def ramasse_item(self,ID_item):
        """
        Fonction qui gère le ramassage d'un item
        Entrée:
            -l'ID de l'item à ramasser
        """
        item = self.controleur.get_entitee(ID_item)
        item.position = None
        self.items[item.get_classe()].append(ID_item)

    def ajoute(self,item):
        #Comme la précédente, mais c'est l'item et non son ID qui est passé en paramètre
        item.position = None
        self.items[item.get_classe()].append(item.ID)

    def utilise_item(self,ID_item):
        """Appelé en appuyant sur la touche espace, utilise l'item actuellement sélectionné."""
        ###L'utilisation varie beaucoup selon le type d'item :
        if ID_item != None:
            item = self.controleur.get_entitee(ID_item)
            if isinstance(item,Consommable): #Un consommable se consomme (si c'est un parchemin, l'activation peut échouer)
                item.utilise(self.controleur.get_entitee(self.possesseur))
            elif isinstance(item,Arme): #Un équipable s'équipe. Il y a certaines conditions.
                self.set_arme()
            elif isinstance(item,Bouclier):
                self.set_bouclier()
            elif isinstance(item,Armure):
                self.set_armure()
            elif isinstance(item,Haume):
                self.set_haume()
            elif isinstance(item,Anneau):
                self.set_anneau()

    def quantite(self,classe):
        """Indique la quantité d'items correspondants à une classe voulue.""" #Pour les ingrédients des recettes
        res=0
        for ID in self.items[Ingredient]:
            item = self.controleur.get_entitee(ID)
            if isinstance(item,classe) and item.etat == "intact":
                res+=1
        return res

    def consomme(self,classe):
        """Consomme un ingrédient lors d'une opération d'alchimie.""" #/!\ Rien à voir avec les consommables !
        for ID in self.items[Ingredient]:
            item = self.controleur.get_entitee(ID)
            if isinstance(item,classe) and item.etat == "intact":
                item.etat = "brisé"
                break

    def get_items_visibles(self):
        items_visibles = []
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

    def set_arme(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Arme):
            self.arme = ID_item

    def get_bouclier(self):
        return self.bouclier

    def set_bouclier(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Bouclier):
            self.bouclier = ID_item

    def get_armure(self):
        return self.armure

    def set_armure(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Armure):
            self.armure = ID_item

    def get_haume(self):
        return self.haume

    def set_haume(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Haume):
            self.haume = ID_item

    def get_anneau(self):
        return self.anneau

    def set_anneau(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Anneau):
            if ID_item in self.anneau:
                self.anneau.remove(ID_item)
                self.anneau.append(None)
            else :
                for i in range(len(self.anneau)-1,0,-1):
                    self.anneau[i]=self.anneau[i-1]
                self.anneau[0]=ID_item

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

    def equippe(self,equippement):
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

    def get_clees(self):
        clees = []
        for ID_cle in self.items[Cle]:
            cle = self.controleur.get_entitee(ID_cle)
            for code in cle.codes:
                clees.append(code)
        return clees

    def get_clee(self,code):
        cle = None
        for ID_cle in self.items[Cle]:
            if code in self.controleur.get_entitee(ID_cle).codes:
                cle = ID_cle
        return cle

    def get_items(self):
        items = []
        for kii in self.kiiz:
            for ID in self.items[kii]:
                items.append(self.controleur.get_entitee(ID))
        return items

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for cat in range(10): #On parcourt les catégories
            items = self.items[self.kiiz[cat]]
            for nb_item in range(len(items)-1,-1,-1): #On parcourt les items
                ID_item = items[nb_item]
                item = self.controleur.get_entitee(ID_item)
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

    def drop_all(self,position):
        items = []
        for cat_item in self.kiiz : #On drop aussi les cadavres et les oeufs
            for ID_item in self.items[cat_item]:
                self.drop(position,ID_item)

    def drop(self,position,ID_item):
        for cat_item in self.kiiz :
            if ID_item in self.items[cat_item]:
                item = self.controleur.get_entitee(ID_item)
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
                            self.anneau[doigt] = None #Quel genre d'imbécile briserait ou lancerait son équippement ? Enfin...

    def debut_tour(self):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.debut_tour()
            if item.etat == "suspens":
                item.utilise(self.controleur.get_entitee(self.possesseur))
        #On ne manipule pas les cadavres
        for ID_oeuf in self.items[Oeuf]: #Mais les oeufs incubent !
            oeuf = self.controleur.get_entitee(ID_oeuf)
            hatch = trouve_skill(oeuf.classe_principale,Hatching)
            if hatch != None:
                if hatch.utilise(): #Et peuvent même éclore !
                    self.controleur.fait_eclore(oeuf,self.possesseur)

    def pseudo_debut_tour(self):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.pseudo_debut_tour()

    def fin_tour(self):
        items = []
        for item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient] : #On sépare les 'vrais' items des faux.
            items += self.items[item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.fin_tour() #Moins de choses à faire à la fin du tour.
        self.nettoie_item()

class Sac_a_dos(Inventaire): #L'inventaire du joueur

    def __init__(self):
        Inventaire.__init__(self,2,10)
        self.cat_courante = 0
        self.deplacement = 1
        self.item_courant = 0
        self.profondeur = 0

    def complete(self):
        self.cat_courante = 0
        self.deplacement = 1
        self.item_courant = 0
        self.profondeur = 0

    def get_skin_cats(self):
        return [cat.get_image() for cat in self.kiiz]

    #La principale différence est la notion d'item courant, et tout ce qui tourne autour
    def get_item_courant(self):
        cat = self.items[self.kiiz[self.cat_courante]]
        if self.item_courant < len(cat):
            item_courant = cat[self.item_courant]
        else:
            item_courant = None
        return item_courant

    def deplace(self,direction):
        res = False
        if direction == IN and self.profondeur <= 1:
            self.profondeur += 1
        elif direction == OUT:
            if self.profondeur == 0:
                res = True
            else:
                self.profondeur -=1
        elif direction == BAS:
            if self.profondeur == 0:
                self.cat_courante += 1
                if self.cat_courante >= len(self.items):
                    self.cat_courante = 0
                self.item_courant = 0
                self.deplacement = 1
            elif self.profondeur == 1:
                self.item_courant += 1
                if self.item_courant >= len(self.items[self.kiiz[self.cat_courante]]):
                    self.item_courant = 0
        elif direction == HAUT:
            if self.profondeur == 0:
                if self.cat_courante <= 0:
                    self.cat_courante = len(self.items)
                self.cat_courante -= 1
                self.item_courant = 0
                self.deplacement = -1
            elif self.profondeur == 1:
                self.item_courant -= 1
                if self.item_courant < 0:
                    self.item_courant = len(self.items[self.kiiz[self.cat_courante]])-1
        return res

    def utilise_courant(self):
        """Appelé en appuyant sur la touche espace, utilise l'item actuellement sélectionné."""
        ID_item = self.get_item_courant()
        self.utilise_item(ID_item)

    def a_parchemin_vierge(self):
        for ID_parch in self.items[Parchemin]:
            if isinstance(self.controleur.get_entitee(ID_parch),Parchemin_vierge):
                return True
        return False

    def consomme_parchemin_vierge(self):
        for ID_parch in self.items[Parchemin]:
            if isinstance(self.controleur.get_entitee(ID_parch),Parchemin_vierge):
                self.controleur.get_entitee(ID_parch).etat = "brisé"
                return True
        return False

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for cat in range(10): #On parcourt les catégories
            items = self.items[self.kiiz[cat]]
            for nb_item in range(len(items)-1,-1,-1): #On parcourt les items
                ID_item = items[nb_item]
                item = self.controleur.get_entitee(ID_item)
                if item.position != None or item.etat == "brisé": #S'il a été lancé ou n'est plus en état
                    items.remove(ID_item)

                    if cat == self.cat_courante :
                        if nb_item < self.item_courant or nb_item == len(items) == self.item_courant :
                            self.item_courant -= 1 #On gère d'éventuels problèmes de selection

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

        if 0 == len(self.items[Potion]) == len(self.items[Parchemin]) == len(self.items[Cle]) == len(self.items[Arme]) == len(self.items[Bouclier]) == len(self.items[Armure]) == len(self.items[Haume]) == len(self.items[Anneau]) == len(self.items[Projectile]) == len(self.items[Cadavre]) == len(self.items[Oeuf]) : #Sérieusement, l'inventaire est vide ?!
            self.cat_courante = 0
            self.item_courant = 0
        else :
            while len(self.items[self.kiiz[self.cat_courante]]) == 0: #On a au moins une catégorie non vide.
                self.cat_courante = (self.cat_courante + self.deplacement) % len(self.items)
            if self.item_courant == -1 : #Ce devrait être le cas si on est passé dans la boucle précédente, et ce n'est pas très souhaitable...
                self.item_courant = 0
                self.profondeur = 0

    def drop_courant(self,position):
        cat = self.items[self.kiiz[self.cat_courante]]
        if cat != []:
            ID_item = cat[self.item_courant]
            self.drop(position,ID_item)

from Jeu.Entitees.Item.Items import Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Ingredient,Cadavre,Oeuf
from Jeu.Entitees.Item.Items import Consommable
from Jeu.Entitees.Item.Items import Parchemin_vierge
from Jeu.Systeme.Kumo_desu_ga_nanika import *