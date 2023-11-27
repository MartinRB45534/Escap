"""
Contient la classe Liste, qui permet d'afficher des objets à la suite, et de les faire défiler.
"""

from __future__ import annotations
from typing import List, Tuple, Optional, Sequence
import pygame

from .affichable import Affichable
from .conteneur import Conteneur
from .cliquable import Cliquable
from .wrapper_noeud import WrapperNoeud
from .marge import MargeHorizontale, MargeVerticale
from .placeholder import Placeheldholder

from .erreur import DisplayError

from ._ensure_pygame import transparency_flag

class Liste(Conteneur):
    """Contient des objets, et les affiche à la suite."""
    def __init__(self, shrink: bool = False):
        Conteneur.__init__(self)
        self.contenu:List[Affichable]
        self.repartition = []
        self.courant = 0 #L'élément 'courant' de la liste
        self.decalage = 0
        self.shrink = shrink

    def set_contenu(self,contenu:List[Affichable],
                    repartition:Optional[List[int]]=None,courant:int=0):
        if repartition is None:
            repartition = [0]*len(contenu)
        # On vérifie qu'il n'y a pas de nombres négatifs dans la répartition
        if any(taille<0 for taille in repartition):
            raise ValueError("Les tailles doivent être positives dans les listes !")
        # On vérifie qu'il y a autant d'éléments dans la répartition que dans le contenu
        elif len(contenu) != len(repartition):
            raise ValueError(f"Hoy, {contenu} et {repartition} ne sont pas de même taille !")
        else:
            self.contenu = contenu
            self.repartition = repartition
            self.courant = courant

    def clique(self,position:Tuple[int,int],droit:bool=False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            for i, contenu in enumerate(self.contenu):
                res_contenu = contenu.clique(pos_rel,droit)
                if res_contenu:
                    res = res_contenu
                    self.courant = i
                    self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.clique(position,droit)
            if res_objet:
                res = res_objet
        return res

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
        res = False
        for i, contenu in enumerate(self.contenu):
            res_contenu = contenu.clique_placeholder(placeheldholder,droit)
            if res_contenu:
                res = res_contenu
                self.courant = i
                self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                res = res_objet
        return res

    def survol(self,position:Tuple[int,int]):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            for i, contenu in enumerate(self.contenu):
                res_contenu = contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
                    self.courant = i
                    self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def ajuste(self,element:Affichable):
        """Ajuste la liste pour que l'élément soit visible."""

    def scroll_liste(self,position:Tuple[int,int],x:int,y:int):
        """Scroll la liste, si possible."""
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            for contenu in self.contenu:
                if contenu.scroll(pos_rel,x,y):
                    res = True
        for objet in self.objets:
            if objet.scroll(position,x,y):
                res = True
        return res

class ListeVerticale(Liste):
    """Une liste disposée verticalement."""
    def set_tailles(self,tailles:Tuple[int,int]):
        self.tailles = tailles
        somme = self.decalage
        for i, contenu in enumerate(self.contenu):
            contenu.set_position((0,somme))
            if self.repartition[i]:
                tailles_contenu = contenu.get_tailles((tailles[0],self.repartition[i]))
            else:
                tailles_contenu = contenu.get_tailles(tailles)
            contenu.set_tailles(tailles_contenu)
            somme += tailles_contenu[1]
        decalage = 0
        if somme < tailles[1]:
            decalage += tailles[1]-somme
        if self.decalage + decalage > 0:
            decalage = -self.decalage
        if decalage:
            for contenu in self.contenu:
                contenu.decale((0,decalage))
            self.decalage += decalage

    def get_tailles(self,tailles:Tuple[int,int]):
        return (max(contenu.get_tailles(tailles)[0] for contenu in self.contenu),
                tailles[1] if not self.shrink else
                min(sum(self.repartition[i] if self.repartition[i] else
                        self.contenu[i].get_tailles(tailles)[1]
                        for i in range(len(self.repartition))),tailles[1])
                ) if self.contenu else (0,0)

    def scroll(self,position:Tuple[int,int],x:int,y:int):
        if self.scroll_liste(position,x,y): #Un de nos éléments a scrollé
            return True
        elif self.touche(position) and y: #Personne n'a scrollé, peut-être qu'on peut le faire
            taille_contenu = sum(self.repartition[i] if self.repartition[i] else
                                 self.contenu[i].get_tailles(self.tailles)[1]
                                 for i in range(len(self.repartition)))
            if taille_contenu > self.tailles[1]:
                # On ne scrolle pas si on ne peut même pas remplir tout l'espace disponible
                if y<0:
                    decalage = max(y,self.tailles[1] - taille_contenu - self.decalage)
                else:
                    decalage = min(y,-self.decalage)
                if decalage:
                    for contenu in self.contenu:
                        contenu.decale((0,decalage))
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
                contenu.decale((0,decalage))
            self.decalage += decalage

    def pop(self,i:int=0):
        """Remove and return item at index (default last)."""
        contenu = self.contenu.pop(i)
        rep = self.repartition.pop(i)
        if i < self.courant:
            self.courant -= 1
            self.decalage += rep if rep else contenu.tailles[1]
        self.set_tailles(self.tailles)

    def insert(self,i:int,contenu:Affichable,rep:int):
        """Insert object before index."""
        self.contenu.insert(i,contenu)
        self.repartition.insert(i,rep)
        if i < self.courant:
            self.courant += 1
            self.decalage -= rep if rep else contenu.get_tailles(self.tailles)[1]
        self.set_tailles(self.tailles)

    def replace(self,i:int,contenu:Affichable,rep:int):
        """Replace object at index with object."""
        ancien_contenu = self.contenu[i]
        ancienne_rep = self.repartition[i]
        self.contenu[i] = contenu
        self.repartition[i] = rep
        if i < self.courant:
            self.decalage += ancienne_rep if ancienne_rep else ancien_contenu.get_tailles(
                self.tailles)[1] - rep if rep else contenu.get_tailles(self.tailles)[1]
        self.set_tailles(self.tailles)

class ListeHorizontale(Liste):
    """Une liste disposée horizontalement."""
    def set_tailles(self,tailles:Tuple[int,int]):
        self.tailles = tailles
        somme = self.decalage
        for i, contenu in enumerate(self.contenu):
            contenu.set_position((somme,0))
            if self.repartition[i]:
                tailles_contenu = contenu.get_tailles((self.repartition[i],tailles[1]))
            else:
                tailles_contenu = contenu.get_tailles(tailles)
            contenu.set_tailles(tailles_contenu)
            somme += tailles_contenu[0]
        decalage = 0
        if somme < tailles[0]:
            decalage += tailles[0]-somme
        if self.decalage + decalage > 0:
            decalage = -self.decalage
        if decalage:
            for contenu in self.contenu:
                contenu.decale((decalage,0))
            self.decalage += decalage

    def get_tailles(self,tailles:Tuple[int,int]):
        return (tailles[0] if not self.shrink else
                min(sum(self.repartition[i] if self.repartition[i] else
                        self.contenu[i].get_tailles(tailles)[0]
                        for i in range(len(self.repartition))),tailles[0]),
                max(contenu.get_tailles(tailles)[1]
                    for contenu in self.contenu))if self.contenu else (0,0)

    def scroll(self,position:Tuple[int,int],x:int,y:int):
        if self.scroll_liste(position,x,y): #Un de nos éléments a scrollé
            return True
        elif self.touche(position) and x: #Personne n'a scrollé, peut-être qu'on peut le faire
            taille_contenu = sum(self.repartition[i] if self.repartition[i] else
                                 self.contenu[i].get_tailles(self.tailles)[0]
                                 for i in range(len(self.repartition)))
            if taille_contenu > self.tailles[0]:
                # On ne scrolle pas si on ne peut même pas remplir tout l'espace disponible
                if x<0:
                    decalage = max(x,self.tailles[0] - taille_contenu - self.decalage)
                else:
                    decalage = min(x,-self.decalage)
                if decalage:
                    for contenu in self.contenu:
                        contenu.decale((decalage,0))
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
                contenu.decale((decalage,0))
            self.decalage += decalage

    def pop(self,i:int=0):
        """Remove and return item at index (default last)."""
        contenu = self.contenu.pop(i)
        rep = self.repartition.pop(i)
        if i < self.courant:
            self.courant -= 1
            self.decalage += rep if rep else contenu.tailles[0]
        self.set_tailles(self.tailles)

    def insert(self,i:int,contenu:Affichable,rep:int):
        """Insert object before index."""
        self.contenu.insert(i,contenu)
        self.repartition.insert(i,rep)
        if i < self.courant:
            self.courant += 1
            self.decalage -= rep if rep else contenu.get_tailles(self.tailles)[0]
        self.set_tailles(self.tailles)

    def replace(self,i:int,contenu:Affichable,rep:int):
        """Replace object at index with object."""
        ancien_contenu = self.contenu[i]
        ancienne_rep = self.repartition[i]
        self.contenu[i] = contenu
        self.repartition[i] = rep
        if i < self.courant:
            self.decalage += ancienne_rep if ancienne_rep else ancien_contenu.get_tailles(
                self.tailles)[0] - rep if rep else contenu.get_tailles(self.tailles)[0]
        self.set_tailles(self.tailles)

class ListeMarge(Liste):
    """Une liste avec des marges automatiques."""
    def __init__(self, marge: int = 5, shrink: bool = False):
        Liste.__init__(self, shrink)
        self.marge = marge

    def set_contenu(self, contenu: Sequence[Affichable],
                    repartition: Optional[List[int]] = None, courant: int = 0):
        if repartition is None:
            repartition = [0] * len(contenu)
        # On vérifie qu'il n'y a pas de nombres négatifs dans la répartition
        if any(taille < 0 for taille in repartition):
            raise ValueError("Les tailles doivent être positives dans les listes !")
        # On vérifie qu'il y a autant d'éléments dans la répartition que dans le contenu
        elif len(contenu) != len(repartition):
            raise ValueError(f"Hoy, {contenu} et {repartition} ne sont pas de même taille !")
        else:
            self.contenu = [
                (MargeHorizontale() if isinstance(self, ListeVerticale) else MargeVerticale())
                if i % 2 else contenu[i // 2] for i in range(2 * len(contenu) - 1)]
            self.repartition = [self.marge
                                if i%2 else repartition[i//2] for i in range(2*len(repartition)-1)]
            self.courant = courant

class ListeMargeVerticale(ListeVerticale, ListeMarge):
    """Une liste disposée verticalement avec des marges automatiques."""

class ListeMargeHorizontale(ListeHorizontale, ListeMarge):
    """Une liste disposée horizontalement avec des marges automatiques."""

class ListeMenu(WrapperNoeud):
    """Une liste sur plusieurs lignes"""
    def __init__(self):
        WrapperNoeud.__init__(self)
        self.items:List[Cliquable] = []
        self.liste = ListeMargeVerticale()

    def set_fond(self,fond:Tuple[int,int,int,int]|Tuple[int,int,int]):
        self.fond = fond

    def set_items(self,items:List[Cliquable]):
        """Change le contenu du conteneur."""
        self.items = items
        self.set_courant(items[0])

    def set_tailles(self,tailles:Tuple[int,int]):
        self.tailles = tailles
        listes:List[Affichable] = []
        ligne:List[Affichable] = []
        ligne_courante:List[Affichable] = []
        liste_courante=ListeMargeHorizontale()
        longueur_ligne=5
        for contenu in self.items:
            if contenu.get_tailles(self.tailles)[0] + 10 >tailles[0]:
                raise DisplayError(f"Je n'ai même pas la place d'afficher {contenu} !")
            elif longueur_ligne + contenu.get_tailles(self.tailles)[0] + 5 > tailles[0]:
                liste = ListeMargeHorizontale()
                liste.set_contenu(ligne)
                listes.append(liste)
                if ligne == ligne_courante:
                    liste_courante = liste
                ligne=[contenu]
                if contenu == self.courant:
                    ligne_courante = ligne
                longueur_ligne = contenu.tailles[0] + 10
            else:
                ligne.append(contenu)
                longueur_ligne += contenu.tailles[0] + 5
                if contenu == self.courant:
                    ligne_courante = ligne
        liste = ListeMargeHorizontale()
        liste.set_contenu(ligne)
        listes.append(liste)
        if ligne == ligne_courante:
            liste_courante = liste
        self.liste.set_contenu(listes)
        self.liste.set_tailles(self.tailles)
        self.liste.ajuste(liste_courante)

    def get_tailles(self,tailles:Tuple[int,int]):
        return tailles

    def affiche(self,screen:pygame.Surface,frame:int=1,frame_par_tour:int=1):
        surf = pygame.Surface(self.tailles,transparency_flag)
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

    def clique(self,position:Tuple[int,int],droit:bool=False):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            for contenu in self.items:
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

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
        res = False
        for contenu in self.items:
            res_contenu = contenu.clique_placeholder(placeheldholder,droit)
            if res_contenu:
                assert isinstance(res_contenu,Cliquable)
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique_placeholder(placeheldholder,droit)
            if res_objet:
                assert isinstance(res_objet,Cliquable)
                res = res_objet
        return res

    def survol(self,position:Tuple[int,int]):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            for contenu in self.items:
                res_contenu = contenu.survol(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                assert isinstance(res_objet,Cliquable)
                res = res_objet
        return res

    def survol_wrapper(self,position:Tuple[int,int]):
        """Trouve l'élément survolé par la souris et le renvoie"""
        res = False
        if self.touche(position):
            res = self
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
            res_contenu = self.liste.survol(pos_rel)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def scroll(self,position:Tuple[int,int],x:int,y:int):
        res = False
        if self.touche(position):
            pos_rel = (position[0]-self.position[0],position[1]-self.position[1])
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
