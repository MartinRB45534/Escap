from __future__ import annotations
from typing import List
from warnings import warn
import pygame

from .Affichable import Affichable
from .Conteneur import Conteneur
from .Cliquable import Cliquable
from .Wrapper_noeud import Wrapper_noeud
from .Marge import Marge_horizontale, Marge_verticale
from .Placeholder import Placeheldholder

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

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
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

class Liste_menu(Wrapper_noeud):
    """Une liste sur plusieurs lignes"""
    def __init__(self):
        Wrapper_noeud.__init__(self)
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
                warn(f"Je n'ai même pas la place d'afficher {self.contenu[i]} !")
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

    def clique_placeholder(self,placeheldholder:Placeheldholder,droit:bool=False):
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
