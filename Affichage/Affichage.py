from typing import List
from warnings import warn
import pygame
from Jeu.Controleur import *
from Affichage.Skins.Skins import *

from math import ceil

class Affichable:
    """Un élément qui s'affiche. Apparaît à l'écran."""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_tailles(self,tailles):
        self.tailles = tailles

    def get_tailles(self,tailles): #Certains utilisent les tailles en entrée ici
        return self.tailles

    def set_position(self,position):
        self.position = position

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        pass

    def touche(self,position):
        return position[0]>=self.position[0] and position[1]>=self.position[1] and position[0]<self.position[0]+self.tailles[0] and position[1]<self.position[1]+self.tailles[1]

    def clique(self,position: List[int], droit: bool = False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res
    
    def clique_placeholder(self,placeheldholder,droit: bool = False):
        return False

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res

    def scroll(self,position,x,y):
        return False

    def update(self):
        pass

    def remove_unpickables(self):
        pass

class Affichage(Affichable):
    """Un élément de l'affichage. Peut contenir des sous-éléments."""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.objets:List[Affichable] = [] #La liste des objets à afficher

    def set_objets(self,objets:List[Affichable]):
        self.objets = objets

    def set_position(self,position):
        self.decale([position[0]-self.position[0],position[1]-self.position[1]])

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        #Fait afficher ses objets
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position: List[int], droit: bool = False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res
    
    def clique_placeholder(self,placeheldholder,droit: bool = False):
        res = False
        for objet in self.objets:
            if objet.clique_placeholder(placeheldholder,droit):
                res = objet
        return res

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        res = False
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        for objet in self.objets:
            objet.update()

    def remove_unpickables(self):
        for objet in self.objets:
            objet.remove_unpickables()

class Taille_variable(Affichable):
    """Les éléments dont la taille réelle dépend de la taille qu'on leur attribut, de façon compliquée."""

class Proportionnel(Affichable):
    def __init__(self,proportions):
        self.tailles = (0,0)
        self.position = (0,0)
        self.proportions = proportions

    def get_tailles(self,tailles):
        return [min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[0],min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[1]]

    def set_tailles(self,tailles):
        self.tailles = [min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[0],min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[1]]

class Marge(Affichable):
    """Un espace vide."""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_tailles(self,tailles):
        self.tailles = tailles

    def get_tailles(self,tailles):
        return tailles

    def set_position(self,position):
        self.position = position

    def touche(self,position):
        return False

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        pass

class Marge_verticale(Marge):
    """Un espace vide, placé verticalement."""

    def get_tailles(self,tailles):
        return [tailles[0],0]

class Marge_horizontale(Marge):
    """Un espace vide, placé verticalement."""

    def get_tailles(self,tailles):
        return [0,tailles[1]]

class Vignette(Affichable):
    """Un élément qui est juste une image."""
    def __init__(self,position,taille,skin:Skin,direction:int|Direction=0):
        self.tailles = [taille,taille]
        self.position = position
        self.skin = skin
        self.direction = direction

    def set_tailles(self,tailles):
        if tailles != self.tailles:
            print(f"Tu ne peux pas modifier la taille d'une vignette ! Vérifie où tu as rangé {self}.")

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        self.skin.dessine_toi(screen,self.position,self.tailles[0],frame,frame_par_tour,self.direction)

class Vignette_image(Vignette):
    def __init__(self,position,tailles,skin:Image,direction:int|Direction=0):
        self.tailles = tailles
        self.position = position
        self.skin = skin
        self.direction = direction

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        self.skin.dessine_toi(screen,self.position,self.tailles,frame,frame_par_tour,0)

class Survolable(Affichable):
    """Un élément qui réagit au survol"""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.marque_survol = False #Est-ce que la souris est dessus ?

    def survol(self,position):
        survol = Affichable.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False

class Cliquable(Survolable): #Il faut être survolable pour être cliquable
    """Un élément qui réagit aux clics"""
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.marque_survol = False #Est-ce que la souris est dessus ?
        self.marque_actif = False #Est-ce que c'est l'élément actif  de la hiérarchie ?
        self.marque_courant = False #Est-ce que c'est l'élément courant de l'élément actif ?
        self.est_courant = False #Est-ce que c'est l'élément courant de son élément parent ? #TODO : à renseigner par l'élément parent (comment ?)
        self.actif = True #Est-ce que l'élément est actif ?

    def trouve_actif(self):
        if self.actif:
            self.marque_actif = True
        else:
            warn(f"Erreur : on a atteint {self} qui n'est pas actif, mais n'est qu'un pauvre cliquable !")

    def set_actif(self):
        self.actif = True

    def unset_actif(self):
        self.actif = False

    def clique(self,position:List[int], droit:bool=False):
        clique = Affichable.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def navigue(self,direction: Direction | int):
        if self.actif: #On est à ce niveau
            if direction == IN:
                return self
            return False
        else:
            warn(f"Erreur : on a atteint {self} qui n'est pas actif, mais ne navigue pas !")

class Knot(Cliquable):
    def __init__(self):
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
        self.marque_survol = False #Est-ce que la souris est dessus ?
        self.marque_actif = False #Est-ce que c'est l'élément actif  de la hiérarchie ?
        self.marque_courant = False #Est-ce que c'est l'élément courant de l'élément actif ?
        self.est_courant = False #Est-ce que c'est l'élément courant de son élément parent ? #TODO : à renseigner par l'élément parent (comment ?)
        self.actif = False #Est-ce que l'élément est actif ?
        self.courant = None #Quel est l'élément suivant dans la hiérarchie ?

    def trouve_actif(self):
        if self.actif:
            self.marque_actif = True
            if self.courant is not None:
                self.courant.marque_courant = True
        elif self.courant is not None:
            self.courant.trouve_actif()
        else:
            warn(f"Erreur : on a atteint {self} qui n'est pas actif, mais n'a pas de courant dénini !")

    def select(self, selection: Affichable, droit:bool=False):
        if isinstance(selection, Cliquable) and not droit:
            self.set_courant(selection)

    def clique(self,position: List[int],droit:bool=False):
        clique = Affichable.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif clique:
            self.select(clique,droit)
            self.unset_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def survol(self,position):
        survol = Affichable.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False

    def navigue(self,direction: Direction | int):
        if self.actif: #On est à ce niveau
            return self.navigue_in(direction)
        elif self.courant is None: # On est à un niveau inférieur, mais on est monté jusqu'ici quand même
            warn("Knot.navigue : On est à un niveau inférieur, mais on est monté jusqu'ici quand même avec self.courant qui vaut None")
            return False
        else:
            nav = self.courant.navigue(direction)
            if nav:
                self.select(nav)
                return self
            else:
                return self.navigue_through(direction)
    
    def set_default_courant(self):
        self.set_courant(None)
        self.unset_actif()

    def set_courant(self,element: Optional[Cliquable]):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, Knot):
            element.set_courant(element.courant) # Assure qu'il y aura un self.actif True quelque part
        elif isinstance(element, Cliquable):
            element.set_actif()
        else:
            warn(f"Knot.set_courant : {self} a reçu {element}")

    def navigue_in(self,direction: Direction | int): # On est l'élément actif
        if direction == IN:
            return self.in_in()
        elif direction ==  OUT:
            return self.in_out()
        elif direction ==  PREVIOUS:
            return self.in_previous()
        elif direction ==  NEXT:
            return self.in_next()
        elif direction ==  GAUCHE:
            return self.in_left()
        elif direction ==  DROITE:
            return self.in_right()
        elif direction ==  HAUT:
            return self.in_up()
        elif direction ==  BAS:
            return self.in_down()
        else:
            warn(f"Knot.navigue_in : Direction inconnue : {direction}")
            return self

    def navigue_through(self,direction: Direction | int): # On est sur le chemin de l'élément actif
        if direction == IN:
            return self.through_in()
        elif direction ==  OUT:
            return self.through_out()
        elif direction ==  PREVIOUS:
            return self.through_previous()
        elif direction ==  NEXT:
            return self.through_next()
        elif direction ==  GAUCHE:
            return self.through_left()
        elif direction ==  DROITE:
            return self.through_right()
        elif direction ==  HAUT:
            return self.through_up()
        elif direction ==  BAS:
            return self.through_down()
        else:
            warn(f"Knot.navigue_through : Direction inconnue : {direction}")
            return self
    
    def in_in(self): # On veut aller plus profond
        if self.courant is None:
            self.set_default_courant()
        self.unset_actif()
        if self.courant is not None:
            self.courant.set_actif()
        return self

    def in_out(self): # On veut ressortir
        self.unset_actif()
        return False
    
    def in_previous(self): # On veut aller au précédent de l'élément actuel
        return False # On laisse faire l'élément parent
    
    def in_next(self): # On veut aller au suivant de l'élément actuel
        return False
    
    def in_left(self): # On veut déplacer notre curseur (self.courant) vers la gauche
        return False # On ne fait rien par défaut
    
    def in_right(self): # On veut déplacer notre curseur (self.courant) vers la droite
        return False # On ne fait rien par défaut
    
    def in_up(self): # On veut déplacer notre curseur (self.courant) vers le haut
        return False # On ne fait rien par défaut
    
    def in_down(self): # On veut déplacer notre curseur (self.courant) vers le bas
        return False # On ne fait rien par défaut
    
    def through_in(self): # On veut aller plus profond, ça ne nous concerne pas
        return False
    
    def through_out(self): # On veut revenir ici
        if self.courant is None:
            raise RuntimeError("Knot.through_out : self.courant is None")
        self.courant.unset_actif()
        self.set_actif()
        return self
    
    def through_previous(self): # On veut aller au précédent de notre élément actuel
        return False # On ne fait rien par défaut
    
    def through_next(self): # On veut aller au suivant de notre élément actuel
        return False # On ne fait rien par défaut
    
    def through_left(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
    
    def through_right(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
    
    def through_up(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False
    
    def through_down(self): # On veut déplacer le curseur, ça ne nous concerne pas
        return False

class Knot_vertical(Knot):
    """Un élément dont le contenu est disposé verticalement (donc next et previous correspondent à haut et bas)."""
    def through_previous(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_up()
        self.courant.set_actif()
        return res
    
    def through_next(self):
        if self.courant is None:
            raise RuntimeError("Knot.through_next : self.courant is None")
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_down()
        self.courant.set_actif()
        return res

class Knot_vertical_profondeur_agnostique(Knot):
    """Un knot_vertical qui ne fait pas de différence entre in et through (pour haut et bas)."""
    def through_up(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_up()
        self.courant.set_actif()
        return res
    
    def through_down(self):
        assert self.courant is not None
        self.courant.unset_actif()
        res = self.in_down()
        self.courant.set_actif()
        return res
    
class Knot_horizontal(Knot):
    """Un élément dont le contenu est disposé horizontalement (donc next et previous correspondent à gauche et droite)."""
    def through_previous(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_left()
        self.courant.set_actif()
        return res
    
    def through_next(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_right()
        self.courant.set_actif()
        return res
    
class Knot_horizontal_profondeur_agnostique(Knot):
    """Un knot_horizontal qui ne fait pas de différence entre in et through (pour gauche et droite)."""
    def through_left(self):
        assert self.courant is not None
        self.courant.unset_actif() # Devrait être inutile
        res = self.in_left()
        self.courant.set_actif()
        return res
    
    def through_right(self):
        assert self.courant is not None
        self.courant.unset_actif()
        res = self.in_right()
        self.courant.set_actif()
        return res

class Knot_hierarchique_sinistre(Knot):
    """Un élément dont le contenu est hiérarchique de gauche à droite (donc gauche et droite correspondent à out et in)."""
    def in_left(self):
        return self.in_out()
    
    def through_left(self):
        return self.through_out()
    
    def in_right(self):
        return self.in_in()
    
class Knot_hierarchique_sinistre_sommet(Knot):
    """Au sommet de la hiérarchie (donc il n'y a rien à gauche)"""
    def through_left(self):
        return self.through_out()
    
    def in_right(self):
        return self.in_in()
    
class Knot_hierarchique_sinistre_base(Knot):
    """En bas de la hiérarchie (donc il n'y a rien à droite)"""
    def in_left(self):
        return self.in_out()
    
class Knot_hierarchique_dextre(Knot):
    """Un élément dont le contenu est hiérarchique de droite à gauche (donc gauche et droite correspondent à in et out)."""
    def in_left(self):
        return self.in_in()
    
    def through_right(self):
        return self.through_out()
    
    def in_right(self):
        return self.in_out()
    
class Knot_hierarchique_dextre_sommet(Knot):
    """Au sommet de la hiérarchie (donc il n'y a rien à droite)"""
    def through_right(self):
        return self.through_out()
    
    def in_left(self):
        return self.in_in()
    
class Knot_hierarchique_dextre_base(Knot):
    """En bas de la hiérarchie (donc il n'y a rien à gauche)"""
    def in_right(self):
        return self.in_out()

class Knot_bloque(Knot):
    """Un élément bloqué (pas de navigation, ni d'effets pour les clics)."""
    def navigue(self, direction: Direction | int):
        if self.actif:
            if direction == IN:
                if self.courant is None:
                    raise(NotImplementedError("Un Knot_bloque doit avoir un élément courant."))
                else:
                    self.unset_actif()
                    self.courant.set_actif()
                    return self
            elif direction == OUT:
                self.unset_actif()
                return False
            elif direction == PREVIOUS:
                self.unset_actif()
                return False
            elif direction == NEXT:
                self.unset_actif()
                return False
        elif self.courant is None:
            raise(NotImplementedError("Un Wrapper_bloque doit avoir un élément courant."))
        else:
            nav = self.courant.navigue(direction)
            if nav:
                self.select(nav)
                return self
            else:
                if direction == OUT:
                    self.set_actif()
                    return self
            return self
            
    def select(self, selection: Affichable, droit: bool = False):
        pass

class Affichage_knot(Affichage,Knot):
    def __init__(self):
        Knot.__init__(self)
        
        self.objets:List[Affichable] = [] #La liste des objets à afficher

    def clique(self,position:List[int],droit:bool=False):
        clique = Affichage.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif isinstance(clique, Placeheldholder):
            res = self.clique_placeholder(clique,droit)
            if not res:
                self.unset_actif()
                return clique
        elif clique:
            assert isinstance(clique,Cliquable)
            self.select(clique,droit)
            self.unset_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def clique_placeholder(self,placeheldholder,droit:bool=False):
        res = Affichable.clique_placeholder(self,placeheldholder,droit)
        if res:
            self.select(res,droit)
            return self
        return False

    def survol(self,position):
        survol = Affichage.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False
    
    def select(self,selection:Cliquable,droit:bool=False):
        if isinstance(selection,Knot) and not droit:
            self.set_courant(selection)

class Conteneur(Affichable):
    """Un élément qui peut en 'contenir' d'autres, c'est-à-dire qu'il va les afficher 'à l'interieur' et ils ne pourront pas déborder."""
    def __init__(self):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
    
    def set_contenu(self,contenu):
        self.contenu = contenu

    def set_fond(self,fond):
        self.fond = fond

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)
    
    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        for contenu in self.contenu:
            contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:List[int],droit:bool=False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.clique(pos_rel,droit)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res

    def clique_placeholder(self,placeheldholder,droit:bool=False):
        res = False
        for contenu in self.contenu:
            res_contenu = contenu.clique_placeholder(placeheldholder,droit)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                if contenu.scroll(pos_rel,x,y):
                    res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        for contenu in self.contenu:
            contenu.update()
        for objet in self.objets:
            objet.update()

    def remove_unpickables(self):
        for contenu in self.contenu:
            contenu.remove_unpickables()
        for objet in self.objets:
            objet.remove_unpickables()

class Wrapper(Conteneur):
    """Un conteneur avec un unique élément"""
    def __init__(self):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:Optional[Affichable] = None #L'objet qu'il 'contient'
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)
    
    def set_contenu(self,contenu:Optional[Affichable]):
        self.contenu = contenu

    def set_fond(self,fond:Tuple[int,int,int,int]|Tuple[int,int,int]):
        self.fond = fond

    def decale(self,decalage:Tuple[int,int]):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)

    def set_tailles(self,tailles:Tuple[int,int]):
        assert self.contenu is not None
        self.tailles = tailles
        self.contenu.set_tailles(tailles)

    def get_tailles(self,tailles:Tuple[int,int]):
        if self.contenu is None:
            print(f"{self} n'a pas de contenu !")
            return (0,0)
        return self.contenu.get_tailles(tailles)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        assert self.contenu is not None
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:List[int],droit:bool=False):
        assert self.contenu is not None
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self #La plupart des trucs qu'on veut pouvoir cliquer sont les Wrapper, pas les listes et pavages intermédiaires
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.contenu.clique(pos_rel,droit)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res
    
    def clique_placeholder(self,placeheldholder,droit:bool=False):
        assert self.contenu is not None
        res = False
        res_contenu = self.contenu.clique_placeholder(placeheldholder,droit)
        if res_contenu:
            res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position):
        assert self.contenu is not None
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.contenu.survol(pos_rel)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        assert self.contenu is not None
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            if self.contenu.scroll(pos_rel,x,y):
                res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        assert self.contenu is not None
        self.contenu.update()
        for objet in self.objets:
            objet.update()

    def remove_unpickables(self):
        assert self.contenu is not None
        self.contenu.remove_unpickables()
        for objet in self.objets:
            objet.remove_unpickables()

class Wrapper_test(Wrapper):
    pass
    # Same, but allows me to test some stuff
    # def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
    #     self.fond = (34, 139, 34)
    #     print(self, self.contenu)
    #     print(self.tailles)
    #     print(self.position)
    #     print(screen.get_size())
    #     return super().affiche(screen, frame, frame_par_tour)

class Wrapper_cliquable(Wrapper,Cliquable):
    """Un wrapper qui peut être cliqué"""
    def __init__(self):
        Cliquable.__init__(self)

        self.objets:List[Affichable] = []
        self.contenu:Optional[Affichable] = None #L'objet qu'il 'contient'
        self.fond = (0,0,0,0)

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        assert self.contenu is not None
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        # On ajoute un contour
        if self.marque_survol:
            self.marque_survol = False
            surf.fill((228,35,19,255)) #Rouge
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.marque_actif:
            self.marque_actif = False
            surf.fill((51,153,0,255)) #Vert
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.marque_courant:
            self.marque_courant = False
            surf.fill((255,192,0,255)) #Jaune
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.est_courant:
            self.est_courant = False
            surf.fill((238,238,238,255)) #Gris
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.actif:
            surf.fill((238,238,238,255)) #Gris
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        else:
            surf.fill(self.fond)
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position:List[int],droit:bool=False):
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False

    def survol(self,position):
        survol = Wrapper.survol(self,position)
        if survol is self:
            self.marque_survol = True
        else:
            self.marque_survol = False
        if survol:
            return self
        return False

class Wrapper_knot(Wrapper_cliquable,Knot):
    """Un wrapper_cliquable qui a des enfants""" #Constitue la majorité de mon affichage
    def __init__(self):
        Knot.__init__(self)

        self.objets:List[Affichable] = []
        self.contenu:Optional[Affichable] = None #L'objet qu'il 'contient'
        self.fond:Tuple = (0,0,0,0)

    def clique(self,position, droit:bool=False):
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif isinstance(clique, Placeheldholder):
            res = self.clique_placeholder(clique, droit)
            if not res:
                self.unset_actif()
                return clique
        elif clique:
            self.select(clique, droit)
            self.unset_actif()
        else:
            self.unset_actif()
        if clique:
            return self
        return False
    
    def clique_placeholder(self,placeheldholder, droit:bool=False):
        res = Wrapper.clique_placeholder(self,placeheldholder, droit)
        if res:
            self.select(res, droit)
            return self
        return False
    
class Wrapper_knot_bloque(Knot_bloque,Wrapper_knot):
    pass

class Placeheldholder(Wrapper_knot):
    """L'élément où le placeheld du placeholder est placé."""
    def clique(self,position, droit:bool=False):
        clique = Wrapper.clique(self,position,droit)
        if clique is self:
            self.set_actif()
        elif isinstance(clique, Placeheldholder):
            res = self.clique_placeholder(clique, droit)
            if not res:
                self.unset_actif()
                return clique
        elif clique:
            self.select(clique, droit)
            self.unset_actif()
        # else:
        #     self.unset_actif()
        if clique:
            return self
        return False

    def set_actif(self):
        if isinstance(self.contenu,Cliquable):
            self.contenu.set_actif()

    def unset_actif(self):
        if isinstance(self.contenu,Cliquable):
            self.contenu.unset_actif()

    def trouve_actif(self):
        if isinstance(self.contenu,Cliquable):
            self.contenu.trouve_actif()

class Placeholder(Knot):
    """Un élément qui lie à un autre, ailleurs."""
    def __init__(self, placeheldholder:Placeheldholder, placeheld:Optional[Cliquable], placeheldholder_ajuster:Optional[Affichable]=None):
        Knot.__init__(self)
        self.placeheldholder = placeheldholder
        self.placeheldholder_ajuster = placeheldholder_ajuster if placeheldholder_ajuster else placeheldholder # L'élément le plus proche dans la parenté du placeheldholder dont la taille n'est pas affectée par la taille du placeheldholder (celui jusqu'auquel il faut remonter pour ajuster la taille du placeheldholder)
        self.set_courant(placeheld)

    def set_courant(self,element: Optional[Cliquable]):
        self.courant = element
        self.set_actif()

    def set_actif(self):
        assert self.courant is not None
        super().set_actif()
        self.placeheldholder.set_contenu(self.courant)
        if self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)
        self.courant.set_actif()

    def unset_actif(self):
        assert self.courant is not None
        super().unset_actif()
        self.courant.unset_actif()

    def trouve_actif(self):
        assert self.courant is not None
        self.marque_actif = True
        self.courant.trouve_actif()

    def clique(self, position: List[int], droit:bool=False):
        return Cliquable.clique(self, position, droit) # On ne veut pas que le clique soit propagé

    def clique_placeholder(self,placeheldholder:Placeheldholder, droit:bool=False):
        if placeheldholder is self.placeheldholder and self.courant is placeheldholder.contenu:
            return self

    def survol(self, position: List[int]):
        return Cliquable.survol(self, position)
    
    def navigue(self, direction: Direction | int):
        assert self.courant is not None
        res = self.courant.navigue(direction)
        self.actif = self.courant.actif
        return res

    def update(self):
        assert self.courant is not None
        super().update()
        self.courant.update()
        if self.placeheldholder.courant is self.courant and self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)

class Pavage(Conteneur):
    """Contient des objets, qui s'adaptent au pavage"""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.repartition = [] #La répartition des objets contenus
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_contenu(self,contenu,repartition):
        if all(taille >= 0 for taille in repartition):
            warn("Il n'y a pas d'élément ajustable dans ce pavage !?")
        if len(contenu) != len(repartition):
            warn(f"Hey, {contenu} et {repartition} ne sont pas de même taille !")
        else:
            self.contenu = contenu
            self.repartition = repartition

class Pavage_horizontal(Pavage):
    def set_contenu(self, contenu, repartition):
        if any(isinstance(objet,Marge_horizontale) for objet in contenu):
            warn("Il y a une marge horizontale dans un pavage horizontal !")
        return super().set_contenu(contenu, repartition)

    def set_tailles(self,tailles):
        # print("Pavage_horizontal.set_tailles")
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            if tailles == (0,0):
                warn(f"Tailles nulles pour {self} !")
            else:
                raise RuntimeError(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[0]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            somme = 0
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[0]
                self.contenu[i].set_tailles([int(taille),tailles[1]])
                self.contenu[i].set_position([somme,0])
                somme += taille
        self.tailles = tailles

    def get_tailles(self,tailles):
        somme = 0
        maxi = 0
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        # print("libre")
        if libre < 0:
            warn(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[0]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[0]
                tailles_effectives = self.contenu[i].get_tailles([int(taille),tailles[1]])
                # print("effectives")
                somme += tailles_effectives[0]
                maxi = max(maxi,tailles_effectives[1])
        # print("</get p>")
        # print([somme,maxi])
        return [somme,maxi]

class Pavage_vertical(Pavage):
    def set_contenu(self, contenu, repartition):
        if any(isinstance(objet,Marge_verticale) for objet in contenu):
            warn("Il y a une marge verticale dans un pavage vertical !")
        return super().set_contenu(contenu, repartition)

    def set_tailles(self,tailles):
        # print("Pavage_vertical.set_tailles")
        libre = tailles[1] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            if tailles == (0,0):
                warn(f"Tailles nulles pour {self} !")
            else:
                raise RuntimeError(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[1]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            somme = 0
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[1]
                self.contenu[i].set_tailles([tailles[0],int(taille)])
                self.contenu[i].set_position([0,somme])
                somme += taille
        self.tailles = tailles

    def get_tailles(self,tailles):
        # print("<get p v>")
        # print(tailles)
        somme = 0
        maxi = 0
        libre = tailles[1] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        # print("libre")
        if libre < 0:
            warn(f"Je ne peux pas faire rentrer {self.contenu} ({[self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.contenu))]}) en {self.repartition} ({tailles[1]}) dans {self} !")
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            portion = 0
            if nb_portions: #Dans le cas contraire, on n'a pas besoin de définir portion
                portion = libre/nb_portions
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille < 0:
                    taille*=portion
                elif not taille:
                    taille=self.contenu[i].get_tailles(tailles)[1]
                tailles_effectives = self.contenu[i].get_tailles([tailles[0],int(taille)])
                # print("effectives")
                somme += tailles_effectives[1]
                maxi = max(maxi,tailles_effectives[0])
        # print("</get p>")
        # print([maxi,somme])
        return [maxi,somme]
    
class Pavage_vertical_test(Pavage_vertical):
    def get_tailles(self, tailles):
        res = super().get_tailles(tailles)
        print(f"get_tailles_v({tailles}) = {res}")
        return res
    
class Pavage_horizontal_test(Pavage_horizontal):
    def get_tailles(self, tailles):
        res = super().get_tailles(tailles)
        print(f"get_tailles_h({tailles}) = {res}")
        print(self.contenu[1].get_tailles(tailles))
        print(self.contenu[1])
        return res

class Liste(Conteneur):
    """Contient des objets, et les affiche à la suite."""
    def __init__(self):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.repartition = []
        self.courant = 0 #L'élément 'courant' de la liste TODO : trouver un meilleur nom (ça risque de prêter à confusion)
        self.decalage = 0
        self.fond = (0,0,0,0)
        self.tailles = (0,0) #La largeur et la hauteur (ou l'inverse ?)
        self.position = (0,0)

    def set_contenu(self,contenu:List[Affichable],repartition:List[float],courant=0):
        # On vérifie qu'il n'y a pas de nombres négatifs dans la répartition
        if any(taille<0 for taille in repartition):
            warn("Les tailles doivent être positives dans les listes !")
        # On vérifie qu'il y a autant d'éléments dans la répartition que dans le contenu
        elif len(contenu) != len(repartition):
            warn(f"Hoy, {contenu} et {repartition} ne sont pas de même taille !")
        else:
            self.contenu = contenu
            self.repartition = repartition
            self.courant = courant

    def clique(self,position:List[int],droit:bool=False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for i in range(len(self.contenu)):
                res_contenu = self.contenu[i].clique(pos_rel,droit)
                if res_contenu:
                    res = res_contenu
                    self.courant = i
                    self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res

    def clique_placeholder(self,placeheldholder,droit:bool=False):
        res = False
        for i in range(len(self.contenu)):
            res_contenu = self.contenu[i].clique_placeholder(placeheldholder,droit)
            if res_contenu:
                res = res_contenu
                self.courant = i
                self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for i in range(len(self.contenu)):
                res_contenu = self.contenu[i].survol(pos_rel)
                if res_contenu:
                    res = res_contenu
                    self.courant = i
                    self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res
    
    def ajuste(self,objet):
        pass

    def scroll_liste(self,position,x,y):
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                if contenu.scroll(pos_rel,x,y):
                    res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

class Liste_verticale(Liste):
    def set_tailles(self,tailles):
        self.tailles = tailles
        #occupe = sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(tailles)[1] for i in range(len(self.repartition)))
        somme = self.decalage
        for i in range(len(self.repartition)):
            contenu = self.contenu[i]
            contenu.set_position([0,somme])
            if self.repartition[i]:
                tailles_contenu = contenu.get_tailles([tailles[0],self.repartition[i]])
            else:
                tailles_contenu = contenu.get_tailles(tailles)
            contenu.set_tailles(tailles_contenu) #Certains adaptent leur taille en fonction de ce qu'on leur accorde
            somme += tailles_contenu[1]
        decalage = 0
        if somme < tailles[1]:
            decalage += tailles[1]-somme
        if self.decalage + decalage > 0:
            decalage = -self.decalage
        if decalage:
            for contenu in self.contenu:
                contenu.decale([0,decalage])
            self.decalage += decalage

    def get_tailles(self,tailles):
        return [max(contenu.get_tailles(tailles)[0] for contenu in self.contenu),tailles[1]]#[max(contenu.get_tailles(tailles)[0] for contenu in self.contenu),min(tailles[1],sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(tailles)[1] for i in range(len(self.repartition))))]

    def scroll(self,position,x,y):
        if self.scroll_liste(position,x,y): #Un de nos éléments a scrollé
            return True
        elif self.touche(position) and y: #Personne n'a scrollé, peut-être qu'on peut le faire
            taille_contenu = sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(self.tailles)[1] for i in range(len(self.repartition)))
            if taille_contenu > self.tailles[1]: # On ne scrolle pas si on ne peut même pas remplir tout l'espace disponible
                if y<0:
                    decalage = max(y,self.tailles[1] - taille_contenu - self.decalage)
                else:
                    decalage = min(y,-self.decalage)
                if decalage:
                    for contenu in self.contenu:
                        contenu.decale([0,decalage])
                    self.decalage += decalage
                    return True
        return False

    def ajuste(self,element:Affichable):
        decalage = 0
        if element.position[1] < 0:
            decalage = -element.position[1]
        elif element.position[1]+element.tailles[1] > self.tailles[1]:
            decalage = self.tailles[1]-element.position[1]-element.tailles[1]
        if decalage:
            for contenu in self.contenu:
                contenu.decale([0,decalage])
            self.decalage += decalage

    def pop(self,i):
        contenu = self.contenu.pop(i)
        rep = self.repartition.pop(i)
        if i < self.courant:
            self.courant -= 1
            self.decalage += rep if rep else contenu.tailles[1]
        self.set_tailles(self.tailles)

    def insert(self,i,contenu:Affichable,rep:int):
        self.contenu.insert(i,contenu)
        self.repartition.insert(i,rep)
        if i < self.courant:
            self.courant += 1
            self.decalage -= rep if rep else contenu.get_tailles(self.tailles)[1]
        self.set_tailles(self.tailles)

    def replace(self,i,contenu:Affichable,rep:int):
        ancien_contenu = self.contenu[i]
        ancienne_rep = self.repartition[i]
        self.contenu[i] = contenu
        self.repartition[i] = rep
        if i < self.courant:
            self.decalage += ancienne_rep if ancienne_rep else ancien_contenu.get_tailles(self.tailles)[1] - rep if rep else contenu.get_tailles(self.tailles)[1]
        self.set_tailles(self.tailles)

class Liste_horizontale(Liste):
    def set_tailles(self,tailles):
        self.tailles = tailles
        #occupe = sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(tailles)[0] for i in range(len(self.repartition)))
        somme = self.decalage
        for i in range(len(self.repartition)):
            contenu = self.contenu[i]
            contenu.set_position([somme,0])
            if self.repartition[i]:
                tailles_contenu = contenu.get_tailles([self.repartition[i],tailles[1]])
            else:
                tailles_contenu = contenu.get_tailles(tailles)
            contenu.set_tailles(tailles_contenu) #Certains adaptent leur taille en fonction de ce qu'on leur accorde
            somme += tailles_contenu[0]
        decalage = 0
        if somme < tailles[0]:
            decalage += tailles[0]-somme
        if self.decalage + decalage > 0:
            decalage = -self.decalage
        if decalage:
            for contenu in self.contenu:
                contenu.decale([decalage,0])
            self.decalage += decalage

    def get_tailles(self,tailles):
        # print("<get l h>")
        # print(tailles)
        return [tailles[0],max(contenu.get_tailles(tailles)[1] for contenu in self.contenu)]#[min(tailles[0],sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(tailles)[0] for i in range(len(self.repartition)))),max(contenu.get_tailles(tailles)[1] for contenu in self.contenu)]

    def scroll(self,position,x,y):
        if self.scroll_liste(position,x,y): #Un de nos éléments a scrollé
            return True
        elif self.touche(position) and x: #Personne n'a scrollé, peut-être qu'on peut le faire
            taille_contenu = sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(self.tailles)[0] for i in range(len(self.repartition)))
            if taille_contenu > self.tailles[0]: # On ne scrolle pas si on ne peut même pas remplir tout l'espace disponible
                if x<0:
                    decalage = max(x,self.tailles[0] - taille_contenu - self.decalage)
                else:
                    decalage = min(x,-self.decalage)
                if decalage:
                    for contenu in self.contenu:
                        contenu.decale([decalage,0])
                    self.decalage += decalage
                    return True
        return False

    def ajuste(self,element:Affichable):
        decalage = 0
        if element.position[0] < 0:
            decalage = -element.position[0]
        elif element.position[0]+element.tailles[0] > self.tailles[0]:
            decalage = self.tailles[0]-element.position[0]-element.tailles[0]
        if decalage:
            for contenu in self.contenu:
                contenu.decale([decalage,0])
            self.decalage += decalage

    def pop(self,i):
        contenu = self.contenu.pop(i)
        rep = self.repartition.pop(i)
        if i < self.courant:
            self.courant -= 1
            self.decalage += rep if rep else contenu.tailles[0]
        self.set_tailles(self.tailles)

    def insert(self,i,contenu:Affichable,rep:int):
        self.contenu.insert(i,contenu)
        self.repartition.insert(i,rep)
        if i < self.courant:
            self.courant += 1
            self.decalage -= rep if rep else contenu.get_tailles(self.tailles)[0]
        self.set_tailles(self.tailles)

    def replace(self,i,contenu:Affichable,rep:int):
        ancien_contenu = self.contenu[i]
        ancienne_rep = self.repartition[i]
        self.contenu[i] = contenu
        self.repartition[i] = rep
        if i < self.courant:
            self.decalage += ancienne_rep if ancienne_rep else ancien_contenu.get_tailles(self.tailles)[0] - rep if rep else contenu.get_tailles(self.tailles)[0]
        self.set_tailles(self.tailles)

class Liste_menu(Wrapper_knot):
    """Une liste sur plusieurs lignes"""
    def __init__(self):
        Wrapper_knot.__init__(self)
        self.contenu:List[Cliquable] = []
        
        self.liste = Liste_verticale()

    def set_fond(self,fond):
        self.fond = fond

    def set_contenu(self,contenu:List[Cliquable]):
        self.contenu = contenu
        self.set_courant(contenu[0])

    def set_tailles(self,tailles):
        self.tailles = tailles
        listes=[]
        ligne=[]
        ligne_courante=[]
        liste_courante=Liste_horizontale()
        longueur_ligne=5
        for i in range(len(self.contenu)):
            if self.contenu[i].get_tailles(self.tailles)[0] + 10 >tailles[0]:
                print(f"Je n'ai même pas la place d'afficher {self.contenu[i]} !")
                break
            elif longueur_ligne + self.contenu[i].get_tailles(self.tailles)[0] + 5 > tailles[0]:
                liste = Liste_horizontale()
                liste.set_contenu([ligne[j//2] if j%2 == 0 else Marge_verticale() for j in range(-1,2*len(ligne))],[0 if j%2 == 0 else 5 for j in range(-1,2*len(ligne))])
                listes.append(liste)
                if ligne == ligne_courante:
                    liste_courante = liste
                ligne=[self.contenu[i]]
                if self.contenu[i] == self.courant:
                    ligne_courante = ligne
                longueur_ligne = self.contenu[i].tailles[0] + 10
            else:
                ligne.append(self.contenu[i])
                longueur_ligne += self.contenu[i].tailles[0] + 5
                if self.contenu[i] == self.courant:
                    ligne_courante = ligne
        liste = Liste_horizontale()
        liste.set_contenu([ligne[j//2] if j%2 == 0 else Marge_verticale() for j in range(-1,2*len(ligne))],[0 if j%2 == 0 else 5 for j in range(-1,2*len(ligne))])
        listes.append(liste)
        if ligne == ligne_courante:
            liste_courante = liste
        self.liste.set_contenu([listes[j//2] if j%2 == 0 else Marge_horizontale() for j in range(-1,2*len(listes))],[0 if j%2 == 0 else 5 for j in range(-1,2*len(listes))])
        self.liste.set_tailles(self.tailles)
        self.liste.ajuste(liste_courante)

    def get_tailles(self,tailles):
        return tailles

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        if self.marque_survol:
            self.marque_survol = False
            surf.fill((228,35,19,255)) #Rouge
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.marque_actif:
            self.marque_actif = False
            surf.fill((51,153,0,255)) #Vert
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.marque_courant:
            self.marque_courant = False
            surf.fill((255,192,0,255)) #Jaune
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.est_courant:
            self.est_courant = False
            surf.fill((238,238,238,255)) #Gris
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        elif self.actif:
            surf.fill((238,238,238,255)) #Gris
            surf.fill(self.fond,pygame.Rect(2,2,self.tailles[0]-4,self.tailles[1]-4))
        else:
            surf.fill(self.fond)
        self.liste.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position,droit:bool=False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.clique(pos_rel,droit)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        assert res is None or isinstance(res,Cliquable)
        self.set_courant(res)
        return res

    def clique_placeholder(self,placeheldholder,droit:bool=False):
        res = False
        for contenu in self.contenu:
            res_contenu = contenu.clique_placeholder(placeheldholder,droit)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def survol_wrapper(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.liste.survol(pos_rel)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position,x,y):
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            if self.liste.scroll(pos_rel,x,y):
                res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

    def update(self):
        self.liste.update()
        for objet in self.objets:
            objet.update()

    def remove_unpickables(self):
        self.liste.remove_unpickables()
        for objet in self.objets:
            objet.remove_unpickables()

class Texte(Cliquable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self,texte:str, texte_marque_survol:Optional[str]=None, texte_marque_actif:Optional[str]=None, texte_marque_courant:Optional[str]=None, texte_est_courant:Optional[str]=None, texte_actif:Optional[str]=None):
        Cliquable.__init__(self)
        # Élément le plus important : le texte "normal"
        self.texte=texte
        # Second élément le plus important : le texte survolé (pour montrer au joueur qu'il peut cliquer dessus et que c'est interactif, que le jeu a pas planté, etc.)
        self.texte_marque_survol=texte_marque_survol if texte_marque_survol else self.texte
        # Troisième élément le plus important : le texte actif (pour montrer au joueur que c'est le texte qui est actuellement sélectionné)
        self.texte_marque_actif=texte_marque_actif if texte_marque_actif else self.texte_marque_survol
        # Élément aussi non-négligeable : le texte courant (pour montrer au joueur que c'est le texte qui est actuellement presque sélectionné, mais pas encore)
        self.texte_marque_courant=texte_marque_courant if texte_marque_courant else self.texte_marque_actif
        # Élément moins important : le texte courant (pour montrer au joueur que s'il revient dans le dialogue, c'est le texte qui sera sélectionné)
        self.texte_est_courant=texte_est_courant if texte_est_courant else self.texte
        # Élément pas très important non plus : le texte actif (pour montrer au joueur que s'il revient dans le dialogue, le texte sera actif)
        self.texte_actif=texte_actif if texte_actif else self.texte_est_courant
    
    def get_texte(self,reset=False) -> str:
        if self.marque_survol:
            if reset:
                self.marque_survol = False
            return self.texte_marque_survol
        elif self.marque_actif:
            if reset:
                self.marque_actif = False
            return self.texte_marque_actif
        elif self.marque_courant:
            if reset:
                self.marque_courant = False
            return self.texte_marque_courant
        elif self.est_courant:
            if reset:
                self.est_courant = False
            return self.texte_est_courant
        elif self.actif:
            return self.texte_actif
        else:
            return self.texte

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        texte=POLICE20.render(self.get_texte(True),True,(0,0,0))
        screen.blit(texte,self.position)

    def get_tailles(self,tailles):
        return [POLICE20.size(self.get_texte())[0],20]

class Pave(Taille_variable,Texte):
    """Un élément avec beaucoup de texte. S'adapte sur plusieurs lignes si besoin"""

    def get_tailles(self,tailles):
        mots = self.get_texte().split() # Peut-être voir à couper mieux un jour (espaces insécables, etc.)
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            hauteur += 1
        return [tailles[0],20*hauteur]

    def set_tailles(self,tailles):
        mots = self.get_texte().split()
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            hauteur += 1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
        self.tailles = [tailles[0],20*hauteur]

    def affiche(self,screen:pygame.Surface,frame:int,frame_par_tour:int):
        """Fonction qui prend en entrée une chaine de caractère et renvoie les surfaces des lignes successives du texte."""
        hauteur = 0
        mots = self.get_texte(True).split()
        i = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            screen.blit(POLICE20.render(ligne,True,(0,0,0)),[self.position[0],self.position[1]+hauteur*20])
            hauteur += 1

class Paves(Pave):
    """Un pavé avec plusieurs lignes"""
    def __init__(self, textes:List[str], textes_marques_survol:Optional[List[str]]=None, textes_marques_actifs:Optional[List[str]]=None, textes_marque_courant:Optional[List[str]]=None, textes_est_courant:Optional[List[str]]=None, textes_actifs:Optional[List[str]]=None):
        Cliquable.__init__(self)
        self.textes=textes
        self.textes_marques_survol=textes_marques_survol if textes_marques_survol else self.textes
        self.textes_marques_actifs=textes_marques_actifs if textes_marques_actifs else self.textes_marques_survol
        self.textes_marque_courant=textes_marque_courant if textes_marque_courant else self.textes_marques_actifs
        self.textes_est_courant=textes_est_courant if textes_est_courant else self.textes
        self.textes_actifs=textes_actifs if textes_actifs else self.textes_est_courant

    def get_textes(self,reset=False) -> List[str]:
        if self.marque_survol:
            if reset:
                self.marque_survol = False
            return self.textes_marques_survol
        elif self.marque_actif:
            if reset:
                self.marque_actif = False
            return self.textes_marques_actifs
        elif self.marque_courant:
            if reset:
                self.marque_courant = False
            return self.textes_marque_courant
        elif self.est_courant:
            if reset:
                self.est_courant = False
            return self.textes_est_courant
        elif self.actif:
            return self.textes_actifs
        else:
            return self.textes

    def get_tailles(self,tailles):
        hauteur = 0
        textes = self.get_textes()
        for texte in textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                hauteur += 1
        return [tailles[0],20*hauteur]

    def set_tailles(self,tailles):
        hauteur = 0
        textes = self.get_textes()
        for texte in textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            hauteur = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                hauteur += 1
        self.tailles = [tailles[0],20*hauteur]

    def affiche(self,screen:pygame.Surface,frame:int,frame_par_tour:int):
        hauteur = 0
        textes = self.get_textes()
        for texte in textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                screen.blit(POLICE20.render(ligne,True,(0,0,0)),[self.position[0],self.position[1]+hauteur*20])
                hauteur += 1

class Center_texte(Wrapper_knot_bloque):
    def __init__(self, texte:str):

        Wrapper_knot.__init__(self)
        self.texte = Texte(texte)
        self.set_courant(self.texte)
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [-1, 0, -1])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [-1, 0, -1])
        self.set_contenu(contenu)

class Margin_texte(Wrapper_knot_bloque):
    def __init__(self, texte:str):
        Wrapper_knot.__init__(self)

        self.texte = Texte(texte)
        self.set_courant(self.texte)
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [5, 0, 5])
        self.set_contenu(contenu)

class Center_horizontal_texte(Center_texte, Margin_texte):
    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [-1, 0, -1])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [5, 0, 5])
        self.set_contenu(contenu)

class Center_horizontal_texte_test(Center_texte, Margin_texte):
    def init(self):
        contenu = Pavage_vertical_test()
        monotique = Pavage_horizontal_test()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [-2, 0, -1])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [5, 0, 5])
        self.set_contenu(contenu)

    def get_tailles(self, tailles):
        print("texte :", self.texte.get_tailles(tailles))
        return super().get_tailles(tailles)

class Center_vertical_texte(Center_texte, Margin_texte):
    def init(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(), self.texte, Marge_verticale()], [5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), monotique, Marge_horizontale()], [-1, 0, -1])
        self.set_contenu(contenu)

class Bouton(Wrapper_cliquable):
    def __init__(self, skin, texte, fond=(255,255,255), fond_marque_survol=(200,200,200), fond_marque_actif=None, fond_marque_courant=None, fond_est_courant=None, fond_actif=None):
        Wrapper_cliquable.__init__(self)

        self.fond = fond
        self.fond_marque_survol = fond_marque_survol if fond_marque_survol else self.fond
        self.fond_marque_actif = fond_marque_actif if fond_marque_actif else self.fond_marque_survol
        self.fond_marque_courant = fond_marque_courant if fond_marque_courant else self.fond_marque_actif
        self.fond_est_courant = fond_est_courant if fond_est_courant else self.fond
        self.fond_actif = fond_actif if fond_actif else self.fond_marque_courant

        self.skin = skin
        self.texte = texte
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),Vignette((0,0),20,self.skin),Marge_verticale(),Texte(self.texte),Marge_verticale()],[5,0,5,0,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5])
        self.set_contenu(contenu)

    def get_fond(self):
        if self.marque_survol:
            return self.fond_marque_survol
        elif self.marque_actif:
            return self.fond_marque_actif
        elif self.marque_courant:
            return self.fond_marque_courant
        elif self.est_courant:
            return self.fond_est_courant
        elif self.actif:
            return self.fond_actif
        else:
            return self.fond

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        assert self.contenu is not None
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.get_fond())
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

class Bouton_test(Bouton):
    def get_tailles(self, tailles):
        assert self.contenu is not None
        print(f"bouton : tailles {tailles} ; {self.contenu.get_tailles(tailles)} ({super().get_tailles(tailles)})")
        return super().get_tailles(tailles)

class Vignette_composee(Cliquable,Affichage):
    def __init__(self,vignettes:List[Affichable],taille,shade=False,invalide=False):
        Cliquable.__init__(self)
        self.tailles = [taille,taille]
        self.objets = vignettes
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))

class Vignette_placeholder(Vignette_composee, Placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Optional[Cliquable],placeheldholder_ajuster:Optional[Affichable],vignettes:List[Affichable],taille,shade=False,invalide=False):
        Placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster)
        self.tailles = [taille,taille]
        self.objets = vignettes
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        if self.marque_actif or self.marque_courant or self.marque_survol:
            self.decale((2,2)) # /!\ Trouver un meilleur moyen de marquer l'activité
        super().affiche(screen, frame, frame_par_tour)
        if self.marque_actif or self.marque_courant or self.marque_survol:
            self.decale((-2,-2))
            self.marque_actif = False
            self.marque_courant = False
            self.marque_survol = False

class Vignette_composee_texte(Vignette_composee):
    def __init__(self,vignettes:List[Affichable],texte,taille,shade=False,invalide=False):
        Vignette_composee.__init__(self,vignettes,taille,shade,invalide)
        texte = Texte(texte)
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]])

    def set_tailles(self, tailles):
        Vignette_composee.set_tailles(self,tailles)
        for objet in self.objets:
            if isinstance(objet,Texte):
                tailles_texte = objet.get_tailles(self.tailles)
                objet.set_position([self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]])

class Vignette_placeholder_texte(Vignette_composee_texte,Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Optional[Cliquable],placeheldholder_ajuster:Optional[Affichage],vignettes:List[Affichable],texte,taille,shade=False,invalide=False):
        Vignette_placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster,vignettes,taille,shade,invalide)
        texte = Texte(texte)
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.tailles[0]-tailles_texte[0],self.tailles[1]-tailles_texte[1]])

class Vignette_placeholder_updatable(Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,placeheldholder_ajuster:Affichable,vignettes:List[Affichable],taille,shade=False,invalide=False):
        Vignette_placeholder.__init__(self,placeheldholder,placeheld,placeheldholder_ajuster,vignettes,taille,shade,invalide)

        self.shades:List[Affichable] = []
        if shade or invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
            self.shades.append(Vignette((0,0),taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette((0,0),taille,SKIN_SHADE))
            self.shades.append(Vignette((0,0),taille,SKIN_SHADE))

class Vignette_categorie(Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,categorie:Type[Potion|Parchemin|Cle|Arme|Bouclier|Armure|Haume|Anneau|Projectile|Ingredient|Cadavre|Oeuf],taille,shade=False,invalide=False):
        vignettes:List[Affichable] = [Vignette((0,0),taille,categorie.get_image())]

        Vignette_placeholder.__init__(self,placeheldholder,placeheld,None,vignettes,taille,shade,invalide)

class Vignette_recette(Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,recette,taille,shade=False,invalide=False):
        self.recette = recette
        vignettes:List[Affichable] = [Vignette((0,0),taille,eval(recette["produit"])(None).get_skin())]

        Vignette_placeholder.__init__(self,placeheldholder,placeheld,None,vignettes,taille,shade,invalide)

class Vignette_ingredient(Vignette_placeholder_texte):
    def __init__(self,placeheldholder:Placeheldholder,ingredient:Item,quantite_necessaire,quantite_disponible,taille,shade=False,invalide=False):
        self.ingredient = ingredient
        placeheld = Paves(ingredient.get_description())
        vignettes:List[Affichable] = [Vignette((0,0),taille,ingredient.get_skin())]

        Vignette_placeholder_texte.__init__(self,placeheldholder,placeheld,None,vignettes,f"{quantite_disponible}/{quantite_necessaire}",taille,shade,invalide or quantite_disponible < quantite_necessaire)

class Vignette_vente(Vignette_placeholder_texte):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,item:Item,taille,prix,description,shade=False,invalide=False):
        self.item = item
        self.prix = prix
        self.description = description
        vignettes:List[Affichable] = [Vignette((0,0),taille,item.get_skin())]

        Vignette_placeholder_texte.__init__(self,placeheldholder,placeheld,None,vignettes,f"{prix} €",taille,shade,invalide)

class Vignette_achat(Vignette_placeholder_texte):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,item:Item,taille,prix,description,shade=False,invalide=False):
        self.item = item
        self.prix = prix
        self.description = description
        vignettes:List[Affichable] = [Vignette((0,0),taille,item.get_skin())]

        Vignette_placeholder_texte.__init__(self,placeheldholder,placeheld,None,vignettes,f"{prix} €",taille,shade,invalide)

class Vignette_magie(Vignette_composee):
    def __init__(self,magie:Magie,taille,shade=False,invalide=False):
        self.magie = magie
        vignettes:List[Affichable] = [Vignette((0,0),taille,magie.get_skin())]

        Vignette_composee.__init__(self,vignettes,taille,shade,invalide)

class Vignette_magie_placeholder(Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,magie:Magie,taille,shade=False,invalide=False):
        self.magie = magie
        vignettes:List[Affichable] = [Vignette((0,0),taille,magie.get_skin())]

        Vignette_placeholder.__init__(self,placeheldholder,placeheld,None,vignettes,taille,shade,invalide)

class Vignette_item(Vignette_composee):
    def __init__(self,position,item:Agissant|Item,taille,direction=None,shade=False,invalide=False):
        self.item = item
        if direction is None:
            direction = item.get_direction()
        vignettes:List[Affichable] = [Vignette(position,taille,item.get_skin(),direction)]
        for effet in item.effets:
            if effet.affiche:
                vignettes.append(Vignette(position,taille,effet.get_skin(),direction))

        Vignette_composee.__init__(self,vignettes,taille,shade,invalide)

class Vignette_item_placeholder(Vignette_placeholder):
    def __init__(self,placeheldholder:Placeheldholder,placeheld:Knot,position,item:Item,taille,shade=False,invalide=False):
        self.item = item
        vignettes:List[Affichable] = [Vignette(position,taille,item.get_skin())]

        Vignette_placeholder.__init__(self,placeheldholder,placeheld,None,vignettes,taille,shade,invalide)

class Vignettes_agissant(Vignette_composee):
    def __init__(self,position,agissant:Agissant,taille):
        self.agissant = agissant
        assert agissant.controleur is not None
        direction = agissant.get_direction()
        vignettes:List[Affichable] = []
        arme = agissant.inventaire.arme
        if arme is not None:
            vignettes.append(Vignette_item(position,arme,taille,direction))
        vignettes.append(Vignette(position,taille,agissant.get_skin(),direction))
        armure = agissant.inventaire.armure
        if armure is not None:
            vignettes.append(Vignette_item(position,armure,taille,direction))
        bouclier = agissant.inventaire.bouclier
        if bouclier is not None:
            vignettes.append(Vignette_item(position,bouclier,taille,direction))
        vignettes.append(Vignette(position,taille,agissant.get_skin_tete(),direction)) #Peut-être changer la direction de la tête indépendamment de celle du corps
        haume = agissant.inventaire.haume
        if haume is not None:
            vignettes.append(Vignette_item(position,haume,taille,direction))
        for effet in agissant.effets:
            if effet.affiche:
                vignettes.append(Vignette(position,taille,effet.get_skin(),direction))
        esprit = agissant.controleur.joueur.esprit
        assert esprit is not None
        position_pv = [position[0]+ceil(taille*(2/19)),position[1]+ceil(taille*(2/19))]
        tailles_pv = [ceil(taille*((15*agissant.pv)/(19*agissant.pv_max))),ceil(taille*(15/19))]
        if agissant in esprit.ennemis:
            image = IMAGE_PV_ENNEMI
        elif agissant in esprit.corps:
            image = IMAGE_PV_ALLIE
        else:
            image = IMAGE_PV_NEUTRE
        vignettes.append(Vignette_image(position_pv,tailles_pv,image))
        if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif au-dessus des effets ?
            vignettes.append(Vignette(position,taille,SKIN_DIALOGUE))

        Vignette_composee.__init__(self,vignettes,taille)

class Vignettes_position(Vignette_composee):
    def __init__(self,position: List[int], joueur: PJ, vue: Representation_vue, pos: Position, taille: int, shade=False, invalide=False):
        assert joueur.controleur is not None
        assert joueur.esprit is not None
        self.pos = pos
        vignettes:List[Affichable] = []
        if pos in vue:
            vignettes.append(Vignette_case(position,joueur,vue,pos,taille))
            case = vue.case_from_position(pos)
            if case.clarte>0:
                for item in case.items:
                    vignettes.append(Vignette_item(position,item,taille)) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                if case.decors is not None:
                    vignettes.append(Vignette(position,taille,case.decors.get_skin()))
                if case.agissant is not None: #Enfin l'agissant (s'il y en a un)
                    vignettes.append(Vignettes_agissant(position,case.agissant,taille))
                if case.effets:
                    if any([effet[2] in joueur.esprit.corps for effet in case.effets]):
                        vignettes.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE_ALLIE))
                    else:
                        vignettes.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE))
        else:
            vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))
        
        Vignette_composee.__init__(self,vignettes,taille,shade,invalide)

        self.position = position

class Vignette_case(Vignette_composee):
    def __init__(self,position,joueur:PJ,vue:Representation_vue,pos,taille):
        assert joueur.controleur is not None
        vignettes:List[Affichable] = []
        if pos in vue:
            vue_case = vue.case_from_position(pos)
            if not(vue_case.clarte):
                vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))
            elif vue_case.clarte==-1: #On a affaire à une case accessible mais pas vue
                vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))
                for i in DIRECTIONS:
                    if vue_case.cibles[i][BASIQUE]:
                        pos_voisin = vue_case.case.position+i
                        if pos_voisin in vue and vue.case_from_position(pos_voisin).clarte>0:
                            vignettes.append(Vignette(position,taille,SKIN_MUR_BROUILLARD,i))
            else:
                vignettes.append(Vignette(position,taille,SKINS_CASES[vue_case.code])) #La case en premier, donc en bas
                case:Case = joueur.controleur.case_from_position(vue_case.case.position)
                for i in DIRECTIONS:
                    mur:Mur = case[i]
                    for effet in mur.effets:
                        if effet.affiche:
                            if isinstance(effet,Porte) :
                                vignettes.append(Vignette(position,taille,effet.get_skin(joueur.get_clees()),i))
                            elif isinstance(effet,Mur_plein|Mur_impassable) :
                                vignettes.append(Vignette(position,taille,effet.get_skin(vue_case.code),i))
                            else :
                                vignettes.append(Vignette(position,taille,effet.get_skin(),i))
                for effet in case.effets:
                    if effet.affiche:
                        vignettes.append(Vignette(position,taille,effet.get_skin()))
        else:
            vignettes.append(Vignette(position,taille,SKIN_BROUILLARD))

        Vignette_composee.__init__(self,vignettes,taille)

class Vignette_allie(Vignette_placeholder_updatable):
    def __init__(self,placeheldholder:Placeheldholder,placeheldholder_ajuster:Affichable,agissant:Agissant,taille,shade=False,invalide=False):
        self.agissant = agissant
        assert agissant.controleur is not None
        vignettes:List[Affichable] = [Vignettes_agissant((0,0),agissant,taille)]
        for statut in agissant.get_skins_statuts():
            vignettes.append(Vignette((0,0),taille,statut))

        Vignette_placeholder_updatable.__init__(self,placeheldholder,Description_allie(agissant.controleur,agissant),placeheldholder_ajuster,vignettes,taille,shade,invalide)

    def update(self):
        assert self.courant is not None
        self.objets:List[Affichable] = []
        self.objets.append(Vignettes_agissant(self.position,self.agissant,self.tailles[0]))
        for statut in self.agissant.get_skins_statuts():
            self.objets.append(Vignette(self.position,self.tailles[0],statut))
        self.objets+=self.shades
        self.courant.update()
        if self.placeheldholder.courant is self.courant and self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)

class Vignette_ennemi(Vignette_placeholder_updatable):
    def __init__(self,placeheldholder:Placeheldholder,placeheldholder_ajuster:Affichable,agissant:Agissant,taille,shade=False,invalide=False):
        self.agissant = agissant
        assert agissant.controleur is not None
        vignettes:List[Affichable] = [Vignettes_agissant((0,0),agissant,taille)]

        Vignette_placeholder_updatable.__init__(self,placeheldholder,Description_ennemi(agissant.controleur, agissant),placeheldholder_ajuster,vignettes,taille,shade,invalide)
        
    def update(self):
        assert self.courant is not None
        self.objets:List[Affichable] = []
        self.objets.append(Vignettes_agissant(self.position,self.agissant,self.tailles[0]))
        self.objets+=self.shades
        self.courant.update()
        if self.placeheldholder.courant is self.courant and self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)

class Vignette_neutre(Vignette_placeholder_updatable):
    def __init__(self,placeheldholder:Placeheldholder,placeheldholder_ajuster:Affichable,agissant:Agissant,taille,shade=False,invalide=False):
        self.agissant = agissant
        assert agissant.controleur is not None
        vignettes:List[Affichable] = [Vignettes_agissant((0,0),agissant,taille)]

        Vignette_placeholder_updatable.__init__(self,placeheldholder,Description_neutre(agissant.controleur, agissant),placeheldholder_ajuster,vignettes,taille,shade,invalide)
        
    def update(self):
        assert self.courant is not None
        self.objets:List[Affichable] = []
        self.objets.append(Vignettes_agissant(self.position,self.agissant,self.tailles[0]))
        self.objets+=self.shades
        self.courant.update()
        if self.placeheldholder.courant is self.courant and self.placeheldholder_ajuster.tailles != (0,0):
            self.placeheldholder_ajuster.set_tailles(self.placeheldholder_ajuster.tailles)

class Description_allie(Wrapper_knot, Knot_horizontal_profondeur_agnostique):
    def __init__(self,controleur:Controleur,allie:Agissant):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.allie = allie
        self.fond = (200, 200, 200)

        self.paves = Paves(self.allie.get_texte_descriptif())
        boutons = [
            Bouton(SKIN_REJOINDRE, "Rejoindre"),
            Bouton(SKIN_PARLER, "Parler") if isinstance(self.allie, PNJ) else None,
            Bouton(SKIN_AIDER, "Aider"),
            Bouton(SKIN_EXCLURE, "Exclure"),
        ]

        self.boutons = [bouton for bouton in boutons if bouton is not None]

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        multiptique = Pavage_vertical()
        multiptique.set_contenu([Marge_horizontale(),self.paves] + [self.boutons[i//2] if i%2==1 else Marge_horizontale() for i in range(len(self.boutons)*2+1)], [5, 0] + [0 if i%2==1 else 5 for i in range(len(self.boutons)*2+1)])
        contenu.set_contenu([Marge_verticale(),multiptique,Marge_verticale()],[5,-1,5])
        self.set_contenu(contenu)
        self.fond = (200, 200, 200)

    def select(self, selection: Cliquable, droit: bool = False):
        if not droit:
            if isinstance(selection, Bouton):
                if selection.texte == "Rejoindre":
                    self.controleur.joueur.mouvement = 0
                    self.controleur.joueur.cible_deplacement = self.allie
                elif selection.texte == "Parler":
                    self.controleur.joueur.mouvement = 2
                    self.controleur.joueur.cible_deplacement = self.allie
                elif selection.texte == "Aider":
                    pass #TODO : Définir l'action d'aide
                elif selection.texte == "Exclure":
                    if isinstance(self.controleur.joueur.esprit, Esprit_humain):
                        self.controleur.joueur.esprit.exclus(self.allie)
        # TODO : indiquer que l'action a été effectuée

    def set_default_courant(self):
        self.set_courant(self.boutons[0])

    def in_left(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) > 0:
            self.set_courant(self.boutons[self.boutons.index(self.courant) - 1])

    def in_right(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) < len(self.boutons) - 1:
            self.set_courant(self.boutons[self.boutons.index(self.courant) + 1])

    def update(self):
        assert self.contenu is not None
        self.paves = Paves(self.allie.get_texte_descriptif())
        boutons:List[Optional[Bouton]] = [
            Bouton(SKIN_REJOINDRE, "Rejoindre"),
            Bouton(SKIN_PARLER, "Parler") if isinstance(self.allie, PNJ) else None,
            Bouton(SKIN_AIDER, "Aider"),
            Bouton(SKIN_EXCLURE, "Exclure"),
        ]

        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]

        if isinstance(self.courant, Bouton):
            if self.courant.texte in [bouton.texte for bouton in self.boutons]:
                self.set_courant(self.boutons[[bouton.texte for bouton in self.boutons].index(self.courant.texte)])
            else:
                self.set_default_courant()
        self.init()
        self.contenu.update()
        for objet in self.objets:
            objet.update()
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

class Description_neutre(Wrapper_knot, Knot_horizontal_profondeur_agnostique):
    def __init__(self,controleur:Controleur,neutre:Agissant):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.neutre = neutre
        self.fond = (200, 200, 200)

        self.paves = Paves(self.neutre.get_texte_descriptif())
        boutons:List[Optional[Bouton]] = [
            Bouton(SKIN_REJOINDRE, "Rejoindre"),
            Bouton(SKIN_PARLER, "Parler") if isinstance(self.neutre, PNJ) else None,
            Bouton(SKIN_ATTAQUER, "Attaquer"),
            Bouton(SKIN_ANTAGONISER, "Antagoniser"),
        ]

        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        multiptique = Pavage_vertical()
        multiptique.set_contenu([Marge_horizontale(),self.paves] + [self.boutons[i//2] if i%2==1 else Marge_horizontale() for i in range(len(self.boutons)*2+1)], [5, 0] + [0 if i%2==1 else 5 for i in range(len(self.boutons)*2+1)])
        contenu.set_contenu([Marge_verticale(),multiptique,Marge_verticale()],[5,-1,5])
        self.set_contenu(contenu)
        self.fond = (200, 200, 200)

    def select(self, selection: Cliquable, droit: bool = False):
        if not droit:
            if isinstance(selection, Bouton):
                if selection.texte == "Rejoindre":
                    self.controleur.joueur.mouvement = 0
                    self.controleur.joueur.cible_deplacement = self.neutre
                elif selection.texte == "Parler":
                    self.controleur.joueur.mouvement = 2
                    self.controleur.joueur.cible_deplacement = self.neutre
                elif selection.texte == "Attaquer":
                    self.controleur.joueur.mouvement = 4
                    self.controleur.joueur.cible_deplacement = self.neutre
                elif selection.texte == "Antagoniser":
                    self.controleur.joueur.esprit.ennemis[self.neutre] = {"importance": 0.01, "dangerosite":0}
        # TODO : indiquer que l'action a été effectuée

    def set_default_courant(self):
        self.set_courant(self.boutons[0])

    def in_left(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) > 0:
            self.set_courant(self.boutons[self.boutons.index(self.courant) - 1])

    def in_right(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) < len(self.boutons) - 1:
            self.set_courant(self.boutons[self.boutons.index(self.courant) + 1])

    def update(self):
        assert self.contenu is not None
        self.paves = Paves(self.neutre.get_texte_descriptif())
        boutons:List[Optional[Bouton]] = [
            Bouton(SKIN_REJOINDRE, "Rejoindre"),
            Bouton(SKIN_PARLER, "Parler") if isinstance(self.neutre, PNJ) else None,
            Bouton(SKIN_ATTAQUER, "Attaquer"),
            Bouton(SKIN_ANTAGONISER, "Antagoniser"),
        ]
        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]
        if isinstance(self.courant, Bouton):
            if self.courant.texte in [bouton.texte for bouton in self.boutons]:
                self.set_courant(self.boutons[[bouton.texte for bouton in self.boutons].index(self.courant.texte)])
            else:
                self.set_default_courant()
        self.init()
        self.contenu.update()
        for objet in self.objets:
            objet.update()
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

class Description_ennemi(Wrapper_knot, Knot_horizontal_profondeur_agnostique):
    def __init__(self,controleur:Controleur,ennemi:Agissant):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.ennemi = ennemi
        self.fond = (200, 200, 200)

        self.paves = Paves(self.ennemi.get_texte_descriptif())
        boutons:List[Optional[Bouton]] = [
            Bouton(SKIN_REJOINDRE, "Rejoindre"),
            Bouton(SKIN_PARLER, "Parler") if isinstance(self.ennemi, PNJ) else None,
            Bouton(SKIN_ATTAQUER, "Attaquer"),
            Bouton(SKIN_PRIORISER, "Prioriser"),
        ]

        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        multiptique = Pavage_vertical()
        multiptique.set_contenu([Marge_horizontale(),self.paves] + [self.boutons[i//2] if i%2==1 else Marge_horizontale() for i in range(len(self.boutons)*2+1)], [5, 0] + [0 if i%2==1 else 5 for i in range(len(self.boutons)*2+1)])
        contenu.set_contenu([Marge_verticale(),multiptique,Marge_verticale()],[5,-1,5])
        self.set_contenu(contenu)
        self.fond = (200, 200, 200)

    def select(self, selection: Cliquable, droit: bool = False):
        if not droit:
            if isinstance(selection, Bouton):
                if selection.texte == "Rejoindre":
                    self.controleur.joueur.mouvement = 0
                    self.controleur.joueur.cible_deplacement = self.ennemi
                elif selection.texte == "Parler":
                    self.controleur.joueur.mouvement = 2
                    self.controleur.joueur.cible_deplacement = self.ennemi
                elif selection.texte == "Attaquer":
                    self.controleur.joueur.mouvement = 4
                    self.controleur.joueur.cible_deplacement = self.ennemi
                elif selection.texte == "Prioriser":
                    self.controleur.joueur.esprit.ennemis[self.ennemi]["importance"] += 1
        # TODO : indiquer que l'action a été effectuée

    def set_default_courant(self):
        self.set_courant(self.boutons[0])

    def in_left(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) > 0:
            self.set_courant(self.boutons[self.boutons.index(self.courant) - 1])

    def in_right(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) < len(self.boutons) - 1:
            self.set_courant(self.boutons[self.boutons.index(self.courant) + 1])

    def update(self):
        assert self.contenu is not None
        self.paves = Paves(self.ennemi.get_texte_descriptif())
        boutons:List[Optional[Bouton]] = [
            Bouton(SKIN_REJOINDRE, "Rejoindre"),
            Bouton(SKIN_PARLER, "Parler") if isinstance(self.ennemi, PNJ) else None,
            Bouton(SKIN_ATTAQUER, "Attaquer"),
            Bouton(SKIN_PRIORISER, "Prioriser"),
        ]
        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]
        if isinstance(self.courant, Bouton):
            if self.courant.texte in [bouton.texte for bouton in self.boutons]:
                self.set_courant(self.boutons[[bouton.texte for bouton in self.boutons].index(self.courant.texte)])
            else:
                self.set_default_courant()
        self.init()
        self.contenu.update()
        for objet in self.objets:
            objet.update()
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

class Description_item(Wrapper_knot, Knot_vertical_profondeur_agnostique):
    def __init__(self,controleur:Controleur,item:Item):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.item:Item = item
        self.fond = (200, 200, 200)

        self.paves = Paves(self.item.get_description())
        boutons:List[Optional[Bouton]] = [
            None if not isinstance(self.item,Equipement) else 
            (Bouton(SKIN_DESEQUIPER_ANNEAU, "Desequiper") if isinstance(self.item, Anneau) else
             Bouton(SKIN_DESEQUIPER_ARME, "Desequiper") if isinstance(self.item, Arme) else
             Bouton(SKIN_DESEQUIPER_ARMURE, "Desequiper") if isinstance(self.item, Armure) else
             Bouton(SKIN_DESEQUIPER_BOUCLIER, "Desequiper") if isinstance(self.item, Bouclier) else
             Bouton(SKIN_DESEQUIPER_CASQUE, "Desequiper") if isinstance(self.item, Haume) else None
             ) if self.item in self.controleur.joueur.inventaire.get_equippement() else 
            (Bouton(SKIN_EQUIPER_ANNEAU, "Equiper") if isinstance(self.item, Anneau) else
             Bouton(SKIN_EQUIPER_ARMURE, "Equiper") if isinstance(self.item, Armure) else
             Bouton(SKIN_EQUIPER_BOUCLIER, "Equiper") if isinstance(self.item, Bouclier) else
             Bouton(SKIN_EQUIPER_CASQUE, "Equiper") if isinstance(self.item, Haume) else
             Bouton(SKIN_EQUIPER_EPEE, "Equiper") if isinstance(self.item, Epee) else
             Bouton(SKIN_EQUIPER_LANCE, "Equiper") if isinstance(self.item, Lance) else None
             ),
            Bouton(SKIN_LANCER, "Lancer", fond=(255, 255, 255) if isinstance(self.item, Projectile) else (100, 100, 100)) if trouve_skill(self.controleur.joueur.classe_principale, Skills_projectiles) is not None else None,
            Bouton(SKIN_BOIRE, "Boire") if isinstance(self.item, Potion) else None,
            Bouton(SKIN_UTILISER, "Utiliser") if isinstance(self.item, Parchemin) else None,
            Bouton(SKIN_JETER, "Jeter"),
        ]

        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]
        self.set_default_courant()

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        multiptique = Pavage_vertical()
        multiptique.set_contenu([Marge_horizontale(),self.paves] + [self.boutons[i//2] if i%2==1 else Marge_horizontale() for i in range(len(self.boutons)*2+1)], [5, 0] + [0 if i%2==1 else 5 for i in range(len(self.boutons)*2)]+[-1])
        contenu.set_contenu([Marge_verticale(),multiptique,Marge_verticale()],[5,-1,5])
        self.set_contenu(contenu)
        self.fond = (200, 200, 200)

    def select(self, selection: Cliquable, droit: bool = False):
        if not droit:
            if isinstance(selection, Bouton):
                print("bouton")
                print(selection.texte)
                if selection.texte == "Equiper":
                    self.controleur.joueur.inventaire.equippe({self.item})
                elif selection.texte == "Desequiper":
                    self.controleur.joueur.inventaire.desequippe([self.item])
                elif selection.texte == "Lancer":
                    print("Hey, tu as oublié de coder le lancer de projectile !")
                    # skill = trouve_skill(self.controleur.joueur.classe_principale, Skills_projectiles)
                    # assert skill is not None
                    # self.controleur.joueur.utilise(type(skill))
                    # assert isinstance(self.item, Projectile)
                    # self.controleur.joueur.projectile_courant = self.item #/!\ Qu'est-ce qu'est exactement le projectile courant ? /!\
                elif selection.texte == "Boire" or selection.texte == "Utiliser":
                    assert isinstance (self.item, Consommable)
                    if isinstance (self.item, Parchemin_vierge):
                        self.controleur.joueur.fait(self.item.action_portee)
                    elif isinstance (self.item, Parchemin):
                        self.controleur.joueur.fait(Lit_effet_initial(self.controleur.joueur, self.item.duree, self.item, self.item.effet))
                    elif isinstance (self.item, Potion):
                        self.controleur.joueur.fait(Boit(self.controleur.joueur, self.item.duree, self.item, self.item.effet))
                elif selection.texte == "Jeter":
                    assert self.controleur.joueur.position is not None
                    self.controleur.joueur.inventaire.drop(self.controleur.joueur.position, self.item)
        self.update()
        # TODO : indiquer que l'action a été effectuée

    def set_default_courant(self):
        self.set_courant(self.boutons[0])

    def in_up(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) > 0:
            self.set_courant(self.boutons[self.boutons.index(self.courant) - 1])

    def in_down(self):
        if self.courant in self.boutons and self.boutons.index(self.courant) < len(self.boutons) - 1:
            self.set_courant(self.boutons[self.boutons.index(self.courant) + 1])

    def update(self):
        assert self.contenu is not None
        self.paves = Paves(self.item.get_description())
        boutons:List[Optional[Bouton]] = [
            None if not isinstance(self.item,Equipement) else
            (Bouton(SKIN_DESEQUIPER_ANNEAU, "Desequiper") if isinstance(self.item, Anneau) else
                Bouton(SKIN_DESEQUIPER_ARME, "Desequiper") if isinstance(self.item, Arme) else
                Bouton(SKIN_DESEQUIPER_ARMURE, "Desequiper") if isinstance(self.item, Armure) else
                Bouton(SKIN_DESEQUIPER_BOUCLIER, "Desequiper") if isinstance(self.item, Bouclier) else
                Bouton(SKIN_DESEQUIPER_CASQUE, "Desequiper") if isinstance(self.item, Haume) else None
                ) if self.item in self.controleur.joueur.inventaire.get_equippement() else
            (Bouton(SKIN_EQUIPER_ANNEAU, "Equiper") if isinstance(self.item, Anneau) else
                Bouton(SKIN_EQUIPER_ARMURE, "Equiper") if isinstance(self.item, Armure) else
                Bouton(SKIN_EQUIPER_BOUCLIER, "Equiper") if isinstance(self.item, Bouclier) else
                Bouton(SKIN_EQUIPER_CASQUE, "Equiper") if isinstance(self.item, Haume) else
                Bouton(SKIN_EQUIPER_EPEE, "Equiper") if isinstance(self.item, Epee) else
                Bouton(SKIN_EQUIPER_LANCE, "Equiper") if isinstance(self.item, Lance) else None
                ),
            Bouton(SKIN_LANCER, "Lancer", fond=(255, 255, 255) if isinstance(self.item, Projectile) else (100, 100, 100)) if trouve_skill(self.controleur.joueur.classe_principale, Skills_projectiles) is not None else None,
            Bouton(SKIN_BOIRE, "Boire") if isinstance(self.item, Potion) else None,
            Bouton(SKIN_UTILISER, "Utiliser") if isinstance(self.item, Parchemin) else None,
            Bouton(SKIN_JETER, "Jeter"),
        ]
        self.boutons:List[Bouton] = [bouton for bouton in boutons if bouton is not None]
        if isinstance(self.courant, Bouton):
            if self.courant.texte in [bouton.texte for bouton in self.boutons]:
                self.set_courant(self.boutons[[bouton.texte for bouton in self.boutons].index(self.courant.texte)])
            else:
                self.set_default_courant()
        self.init()
        self.contenu.update()
        for objet in self.objets:
            objet.update()
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)
