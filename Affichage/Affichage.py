from typing import List
import pygame
from Jeu.Constantes import *
from Jeu.Labyrinthe.Structure_spatiale.Direction import *
from Jeu.Controleur import *
from Jeu.Skins.Skins import *

from math import ceil

class Affichable:
    """Un élément qui s'affiche. Apparaît à l'écran."""
    def __init__(self):
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_tailles(self,tailles):
        self.tailles = tailles

    def get_tailles(self,tailles): #Certains utilisent les tailles en entrée ici
        return self.tailles

    def set_position(self,position):
        self.position = position

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]

    def affiche(self,screen,frame=1,frame_par_tour=1):
        pass

    def touche(self,position):
        return position[0]>=self.position[0] and position[1]>=self.position[1] and position[0]<self.position[0]+self.tailles[0] and position[1]<self.position[1]+self.tailles[1]

    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res

    def scroll(self,position,x,y):
        return False

    def navigue(self,direction:Direction|int):
        # /!\ À implémenter dans les sous-classes
        # Renvoie un truthy si l'élément a traité la navigation
        # (True si il n'y a rien à faire, ou l'objet nécessaire à la navigation, de façon identique à la méthode clique)
        # Renvoie False si l'élément n'a pas traité la navigation
        raise NotImplementedError

    def update(self):
        pass

    def remove_unpickables(self):
        pass

class Affichage(Affichable):
    """Un élément de l'affichage. Peut contenir des sous-éléments."""
    def __init__(self):
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
        self.objets = [] #La liste des objets à afficher

    def set_objets(self,objets):
        self.objets = objets

    def set_position(self,position):
        self.decale([position[0]-self.position[0],position[1]-self.position[1]])

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)

    def affiche(self,screen,frame=1,frame_par_tour=1):
        #Fait afficher ses objets
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self #/!\ Est-ce que je veux faire ça comme ça ?
        for objet in self.objets:
            res_objet = objet.clique(position)
            if res_objet:
                res = res_objet
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
        self.tailles = [0,0]
        self.position = [0,0]
        self.proportions = proportions

    def get_tailles(self,tailles):
        return [min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[0],min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[1]]

    def set_tailles(self,tailles):
        self.tailles = [min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[0],min(tailles[0]//self.proportions[0],tailles[1]//self.proportions[1])*self.proportions[1]]


class Marge(Affichable):
    """Un espace vide."""
    def __init__(self):
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_tailles(self,tailles):
        self.tailles = tailles

    def get_tailles(self,tailles):
        return tailles

    def set_position(self,position):
        self.position = position

    def touche(self,position):
        return False

    def affiche(self,screen,frame=1,frame_par_tour=1):
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
    def __init__(self,position:Position,taille,skin,direction=0):
        self.tailles = [taille,taille]
        self.position = position
        self.skin = skin
        self.direction = direction

    def set_tailles(self,tailles):
        if tailles != self.tailles:
            print(f"Tu ne peux pas modifier la taille d'une vignette ! Vérifie où tu as rangé {self}.")

    def affiche(self,screen,frame=1,frame_par_tour=1):
        self.skin.dessine_toi(screen,self.position,self.tailles[0],frame,frame_par_tour,self.direction)

class Vignette_image(Vignette):
    def __init__(self,position:Position,tailles,skin,direction=0):
        self.tailles = tailles
        self.position = position
        self.skin = skin
        self.direction = direction

    def affiche(self,screen,frame=1,frame_par_tour=1):
        self.skin.dessine_toi(screen,self.position,self.tailles,frame,frame_par_tour,0)

class Conteneur(Affichable):
    """Un élément qui peut en 'contenir' d'autres, c'est-à-dire qu'il va les afficher 'à l'interieur' et ils ne pourront pas déborder."""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.courant = False #L'objet actif (sélectionné)
        self.fond = (0,0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
    
    def set_contenu(self,contenu):
        self.contenu = contenu

    def set_fond(self,fond):
        self.fond = fond

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)
    
    def affiche(self,screen,frame=1,frame_par_tour=1):
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        for contenu in self.contenu:
            contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.clique(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position)
            if res_objet:
                res = res_objet
        self.courant = res
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
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:Affichable = None #L'objet qu'il 'contient'
        self.courant = False
        self.fond = (0,0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
    
    def set_contenu(self,contenu):
        self.contenu = contenu

    def set_fond(self,fond):
        self.fond = fond

    def decale(self,decalage):
        self.position = [self.position[0] + decalage[0],self.position[1] + decalage[1]]
        for objet in self.objets:
            objet.decale(decalage)

    def set_tailles(self,tailles):
        # print("Set_taille")
        # print(self)
        self.tailles = tailles
        self.contenu.set_tailles(tailles)

    def get_tailles(self,tailles):
        # print("Get_taille")
        # print(self)
        if self.contenu == None:
            print(f"{self} n'a pas de contenu !")
            return [0,0]
        return self.contenu.get_tailles(tailles)

    def affiche(self,screen,frame=1,frame_par_tour=1):
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        self.contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            self.courant = clique
        else:
            self.courant = False
        if clique:
            return self
        return False

    def survol(self,position):
        survol = self.survol_wrapper(position)
        if survol is self:
            self.courant = True
        elif survol:
            self.courant = survol
        else:
            self.courant = False
        if survol:
            return self
        return False

    def clique_wrapper(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self #La plupart des trucs qu'on veut pouvoir cliquer sont les Wrapper, pas les listes et pavages intermédiaires
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.contenu.clique(pos_rel)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position)
            if res_objet:
                res = res_objet
        return res

    def survol_wrapper(self,position):
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
        self.contenu.update()
        for objet in self.objets:
            objet.update()

    def remove_unpickables(self):
        self.contenu.remove_unpickables()
        for objet in self.objets:
            objet.remove_unpickables()

class Pavage(Conteneur):
    """Contient des objets, qui s'adaptent au pavage"""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.repartition = [] #La répartition des objets contenus
        self.fond = (0,0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_contenu(self,contenu,repartition):
        if len(contenu) != len(repartition):
            print("Hey, vérifie ton contenu et ses répartitions")
            print(contenu)
            print(repartition)
        else:
            self.contenu = contenu
            self.repartition = repartition

class Pavage_horizontal(Pavage):
    def set_tailles(self,tailles):
        # print("Pavage_horizontal.set_tailles")
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            print("Je ne peux pas faire rentrer tout ça là-dedans !")
            # print(self.contenu)
            # print(tailles)
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            if nb_portions != 0: #Dans le cas contraire, on n'a pas besoin de définir portion
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
        # print("<get p h>")
        # print(tailles)
        somme = 0
        maxi = 0
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        # print("libre")
        if libre < 0:
            print("Je ne peux pas faire rentrer tout ça là-dedans !")
            # print(self.contenu)
            # print(tailles)
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            if nb_portions != 0: #Dans le cas contraire, on n'a pas besoin de définir portion
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
    def set_tailles(self,tailles):
        # print("Pavage_vertical.set_tailles")
        libre = tailles[1] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].get_tailles(tailles)[1] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre < 0:
            print("Je ne peux pas faire rentrer tout ça là-dedans !")
            # print(self.contenu)
            # print(tailles)
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            if nb_portions != 0: #Dans le cas contraire, on n'a pas besoin de définir portion
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
            print("Je ne peux pas faire rentrer tout ça là-dedans !")
            # print(self.contenu)
            # print(tailles)
        else:
            nb_portions = sum(taille for taille in self.repartition if taille<0)
            if nb_portions != 0: #Dans le cas contraire, on n'a pas besoin de définir portion
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

class Liste(Conteneur):
    """Contient des objets, et les affiche à la suite."""
    def __init__(self):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = [] #Les objets qu'il 'contient'
        self.repartition = []
        self.courant = 0 #L'élément 'courant' de la liste
        self.decalage = 0
        self.fond = (0,0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_contenu(self,contenu:List[Affichable],repartition:List[float],courant=0):
        self.contenu = contenu
        self.repartition = repartition

    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for i in range(len(self.contenu)):
                res_contenu = self.contenu[i].clique(pos_rel)
                if res_contenu:
                    res = res_contenu
                    self.courant = i
                    self.ajuste(res)
        for objet in self.objets:
            res_objet = objet.clique(position)
            if res_objet:
                res = res_objet
        return res

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
        if decalage != 0:
            for contenu in self.contenu:
                contenu.decale([0,decalage])
            self.decalage += decalage

    def get_tailles(self,tailles):
        # print("<get l v>")
        # print(tailles)
        return [max(contenu.get_tailles(tailles)[0] for contenu in self.contenu),tailles[1]]#[max(contenu.get_tailles(tailles)[0] for contenu in self.contenu),min(tailles[1],sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(tailles)[1] for i in range(len(self.repartition))))]

    def scroll(self,position,x,y):
        if self.scroll_liste(position,x,y): #Un de nos éléments a scrollé
            return True
        elif self.touche(position) and y != 0: #Personne n'a scrollé, peut-être qu'on peut le faire
            taille_contenu = sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(self.tailles)[1] for i in range(len(self.repartition)))
            if taille_contenu > self.tailles[1]: # On ne scrolle pas si on ne peut même pas remplir tout l'espace disponible
                if y<0:
                    decalage = max(y,self.tailles[1] - taille_contenu - self.decalage)
                else:
                    decalage = min(y,-self.decalage)
                if decalage != 0:
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
        if decalage != 0:
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
        if decalage != 0:
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
        elif self.touche(position) and x != 0: #Personne n'a scrollé, peut-être qu'on peut le faire
            taille_contenu = sum(self.repartition[i] if self.repartition[i] else self.contenu[i].get_tailles(self.tailles)[0] for i in range(len(self.repartition)))
            if taille_contenu > self.tailles[0]: # On ne scrolle pas si on ne peut même pas remplir tout l'espace disponible
                if x<0:
                    decalage = max(x,self.tailles[0] - taille_contenu - self.decalage)
                else:
                    decalage = min(x,-self.decalage)
                if decalage != 0:
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
        if decalage != 0:
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

class Liste_menu(Wrapper):
    """Une liste sur plusieurs lignes"""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:List[Affichable] = []
        self.liste = None
        self.courant = False
        self.fond = (0,0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_fond(self,fond):
        self.fond = fond

    def set_contenu(self,contenu):
        self.contenu = contenu
        self.courant = contenu[0]

    def set_tailles(self,tailles):
        self.tailles = tailles
        listes=[]
        ligne=[]
        longueur_ligne=5
        for i in range(len(self.contenu)):
            if self.contenu[i].get_tailles(self.tailles)[0] + 10 >tailles[0]:
                print(f"Je n'ai même pas la place d'afficher {self.contenu[i]} !")
                break
            elif longueur_ligne + self.contenu[i].get_tailles(self.tailles)[0] + 5 > tailles[0]:
                liste = Liste_horizontale()
                liste.set_contenu([ligne[j//2] if j//2 == 0 else Marge_verticale() for j in range(-1,2*len(ligne))],[0 if j//2 == 0 else 5 for j in range(-1,2*len(ligne))])
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
        liste.set_contenu([ligne[j//2] if j//2 == 0 else Marge_verticale() for j in range(-1,2*len(ligne))],[0 if j//2 == 0 else 5 for j in range(-1,2*len(ligne))])
        listes.append(liste)
        if ligne == ligne_courante:
            liste_courante = liste
        self.liste = Liste_verticale()
        self.liste.set_contenu([listes[j//2] if j//2 == 0 else Marge_horizontale() for j in range(-1,2*len(listes))],[0 if j//2 == 0 else 5 for j in range(-1,2*len(listes))])
        self.liste.set_tailles(self.tailles)
        self.liste.ajuste(liste_courante)

    def get_tailles(self,tailles):
        return tailles

    def affiche(self,screen,frame=1,frame_par_tour=1):
        surf = pygame.Surface(self.tailles,pygame.SRCALPHA)
        surf.fill(self.fond)
        self.liste.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            for contenu in self.contenu:
                res_contenu = contenu.clique(pos_rel)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position)
            if res_objet:
                res = res_objet
        self.courant = res
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

    def clique_wrapper(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self #La plupart des trucs qu'on veut pouvoir cliquer sont les Wrapper, pas les listes et pavages intermédiaires
            pos_rel = [position[0]-self.position[0],position[1]-self.position[1]]
            res_contenu = self.liste.clique(pos_rel)
            if res_contenu:
                res = res_contenu
        for objet in self.objets:
            res_objet = objet.clique(position)
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

class Survolable(Affichable):
    """Un élément qui réagit au survol"""
    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = Affichable.survol(self,position)
        if res:
            self.highlight()
        else:
            self.unhighlight()
        return res

    def highlight(self):
        #Change l'apparence pour indiquer que la souris était là.
        pass

    def unhighlight(self):
        #Change l'apparence pour indiquer que la souris n'était plus là.
        pass

    def get_description(self,observation=0):
        return ["Hey, je réagis au passage de la souris !","C'est cool, non ?","",f"P.S. Si tu croises Martin, dit lui qu'il y a un problème avec la description de {self} !"]

class Cliquable(Survolable): #Il faut être survolable pour être cliquable
    """Un élément qui réagit aux cliques"""
    def clique(self): #Lui donner un autre paramètre ? Le joueur par exemple ?
        pass #À voir sur les cas particuliers

class Texte(Affichable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self,texte):
        self.tailles = [0,0]
        self.position = [0,0]
        self.texte=texte

    def affiche(self,screen,frame=1,frame_par_tour=1):
        texte=POLICE20.render(self.texte,True,(0,0,0))
        screen.blit(texte,self.position)

    def get_tailles(self,tailles):
        # print([POLICE20.size(self.texte)[0],20])
        return [POLICE20.size(self.texte)[0],20]

class Pave(Taille_variable):
    """Un élément avec beaucoup de texte. S'adapte sur plusieurs lignes si besoin"""
    def __init__(self,texte):
        self.tailles = [0,0]
        self.position = [0,0]
        self.texte=texte
        self.couleur = (0,0,0)

    def get_tailles(self,tailles):
        mots = self.texte.split() #On explose sur les espaces
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
        mots = self.texte.split() #On explose sur les espaces
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

    def affiche(self,screen,frame,frame_par_tour):
        hauteur = 0
        """Fonction qui prend en entrée une chaine de caractère et renvoie les surfaces des lignes successives du texte."""
        mots = self.texte.split() #On explose sur les espaces
        i = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            screen.blit(POLICE20.render(ligne,True,self.couleur),[self.position[0],self.position[1]+hauteur*20])
            hauteur += 1

class Paves(Taille_variable):
    """Un pavé avec plusieurs lignes"""
    def __init__(self,textes):
        self.tailles = [0,0]
        self.position = [0,0]
        self.textes=textes
        self.couleur = (0,0,0)

    def get_tailles(self,tailles):
        hauteur = 0
        for texte in self.textes:
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
        for texte in self.textes:
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

    def affiche(self,screen,frame,frame_par_tour):
        hauteur = 0
        for texte in self.textes:
            mots = texte.split() #On explose sur les espaces
            i = 0
            while i < len(mots):
                ligne = mots[i]
                i+=1
                while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                    ligne = ligne + " " + mots[i]
                    i+=1
                screen.blit(POLICE20.render(ligne,True,self.couleur),[self.position[0],self.position[1]+hauteur*20])
                hauteur += 1

class Final(Cliquable):
    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
        return res

    def survol(self, position):
        res = False
        if self.touche(position):
            res = self
            self.highlight()
        else:
            self.unhighlight()
        return res

class Bouton(Final,Wrapper):
    def __init__(self,skin,texte,fond_non_highlight=(0,0,0),fond_highlight=(50,50,50)):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu:Affichable = None #Les objets qu'il 'contient'
        self.courant = False
        self.fond = fond_non_highlight
        self.fond_non_highlight = fond_non_highlight
        self.fond_highlight = fond_highlight
        self.skin = skin
        self.texte = texte
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),Vignette([0,0],20,self.skin),Marge_verticale(),Texte(self.texte),Marge_verticale()],[5,0,5,0,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5])
        self.contenu = contenu

    def highlight(self):
        self.fond = self.fond_highlight

    def unhighlight(self):
        self.fond = self.fond_non_highlight

    def survol(self, position):
        res = False
        if self.touche(position):
            res = self
            self.highlight()
        else:
            self.unhighlight()
        return res

class Vignette_categorie(Final,Affichage):
    def __init__(self,categorie,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.categorie = categorie
        self.objets.append(Vignette([0,0],taille,categorie.get_image()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))

class Vignette_recette(Final,Affichage):
    def __init__(self,recette,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.recette = recette
        self.objets.append(Vignette([0,0],taille,eval(recette["produit"])(None).get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))

class Vignette_ingredient(Final,Affichage):
    def __init__(self,ingredient:Item,quantite_necessaire,quantite_disponible,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.ingredient = ingredient
        self.objets.append(Vignette([0,0],taille,ingredient.get_skin()))
        if shade or invalide or quantite_disponible < quantite_necessaire:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide or quantite_disponible < quantite_necessaire:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        texte = Texte(f"{quantite_disponible}/{quantite_necessaire}")
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.position[0]+self.tailles[0]-tailles_texte[0],self.position[1]+self.tailles[1]-tailles_texte[1]])

class Vignette_vente(Final,Affichage):
    def __init__(self,item:Item,taille,prix,description,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.item = item
        self.prix = prix
        self.description = description
        self.objets.append(Vignette([0,0],taille,item.get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        texte = Texte(f"{prix} €")
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.position[0]+self.tailles[0]-tailles_texte[0],self.position[1]+self.tailles[1]-tailles_texte[1]])

class Vignette_achat(Final,Affichage):
    def __init__(self,item:Item,taille,prix,description,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.item = item
        self.prix = prix
        self.description = description
        self.objets.append(Vignette([0,0],taille,item.get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        texte = Texte(f"{prix} €")
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.position[0]+self.tailles[0]-tailles_texte[0],self.position[1]+self.tailles[1]-tailles_texte[1]])

class Vignette_magie(Final,Affichage):
    def __init__(self,magie:Magie,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.magie = magie
        self.objets.append(Vignette([0,0],taille,magie.get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))

class Vignette_item(Final,Affichage):
    def __init__(self,position,item:Item,taille,direction=None,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = position
        self.item = item
        if direction == None:
            direction = item.get_direction()
        self.objets.append(Vignette(position,taille,item.get_skin(),direction)) #Avoir éventuellement la tête dans une autre direction ?
        for effet in item.effets:
            if effet.affiche:
                self.objets.append(Vignette(position,taille,effet.get_skin(),direction))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Vignettes_agissant(Final,Affichage):
    def __init__(self,position,agissant:Agissant,taille):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        direction = agissant.get_direction()
        arme = agissant.inventaire.arme
        if arme != None:
            self.objets.append(Vignette_item(position,agissant.controleur[arme],taille,direction))
        self.objets.append(Vignette(position,taille,agissant.get_skin(),direction))
        armure = agissant.inventaire.armure
        if armure != None:
            self.objets.append(Vignette_item(position,agissant.controleur[armure],taille,direction))
        bouclier = agissant.inventaire.bouclier
        if bouclier != None:
            self.objets.append(Vignette_item(position,agissant.controleur[bouclier],taille,direction))
        haume = agissant.inventaire.haume
        self.objets.append(Vignette(position,taille,agissant.get_skin_tete(),direction)) #Avoir éventuellement la tête dans une autre direction ?
        if haume != None:
            self.objets.append(Vignette_item(position,agissant.controleur[haume],taille,direction))
        for effet in agissant.effets:
            if effet.affiche:
                self.objets.append(Vignette(position,taille,effet.get_skin(),direction))
        esprit = agissant.controleur.get_esprit(agissant.controleur.joueur.esprit)
        position_pv = [position[0]+ceil(taille*(2/19)),position[1]+ceil(taille*(2/19))]
        tailles_pv = [ceil(taille*((15*agissant.pv)/(19*agissant.pv_max))),ceil(taille*(15/19))]
        if agissant.ID in esprit.ennemis.keys():
            image = IMAGE_PV_ENNEMI
        elif agissant.ID in esprit.corps.keys():
            image = IMAGE_PV_ALLIE
        else:
            image = IMAGE_PV_NEUTRE
        self.objets.append(Vignette_image(position_pv,tailles_pv,image))
        if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif au-dessus des effets ?
            self.objets.append(Vignette(position,taille,SKIN_DIALOGUE))

class Vignettes_position(Final,Affichage):
    def __init__(self,position,joueur,vue,pos,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.pos = pos
        self.invalide = invalide
        if pos in vue:
            self.objets.append(Vignette_case(position,joueur,vue,pos,taille))
            if vue[pos][1]>0:
                entitees = vue[pos][6]
                agissant = None
                for ID_entitee in entitees:
                    entitee = joueur.controleur[ID_entitee]
                    if issubclass(entitee.get_classe(),Item):
                        self.objets.append(Vignette_item(position,entitee,taille)) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                    elif issubclass(entitee.get_classe(),Decors):
                        self.objets.append(Vignette(position,taille,entitee.get_skin()))
                    else:
                        agissant = entitee
                if agissant != None: #Enfin l'agissant (s'il y en a un)
                    self.objets.append(Vignettes_agissant(position,agissant,taille))
                if vue[pos][7] != []:
                    esprit = joueur.controleur.get_esprit(joueur.esprit)
                    if any([effet[2] in esprit.corps.keys() for effet in vue[pos][7]]):
                        self.objets.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE_ALLIE))
                    else:
                        self.objets.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE))
        else:
            self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Vignette_case(Final,Affichage):
    def __init__(self,position,joueur,vue,pos,taille):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        if pos in vue:
            vue_case = vue[pos]
            if vue_case[1]==0:
                self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
            elif vue_case[1]==-1: #On a affaire à une case accessible mais pas vue
                self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
                for i in DIRECTIONS:
                    if vue_case[5][i][0]:
                        pos_voisin = vue_case[0]+i
                        if pos_voisin in vue and vue[pos_voisin][1]>0:
                            self.objets.append(Vignette(position,taille,SKIN_MUR_BROUILLARD,i))
            else:
                if vue_case[4]==0: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE)) #La case en premier, donc en bas
                elif vue_case[4]==1: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_1)) #La case en premier, donc en bas
                elif vue_case[4]==2: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_2)) #La case en premier, donc en bas
                elif vue_case[4]==3: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_3)) #La case en premier, donc en bas
                elif vue_case[4]==4: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_4)) #La case en premier, donc en bas
                elif vue_case[4]==5: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_5)) #La case en premier, donc en bas
                elif vue_case[4]==6: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_6)) #La case en premier, donc en bas
                elif vue_case[4]==7: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_7)) #La case en premier, donc en bas
                elif vue_case[4]==8: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette([0,0],taille,SKIN_CASE_8)) #La case en premier, donc en bas
                case = joueur.controleur[vue_case[0]]
                for i in DIRECTIONS:
                    mur = case.get_mur_dir(i)
                    for effet in mur.effets:
                        if effet.affiche:
                            if isinstance(effet,Porte) :
                                self.objets.append(Vignette(position,taille,effet.get_skin(joueur.get_clees()),i))
                            elif isinstance(effet,(Mur_plein,Mur_impassable)) :
                                self.objets.append(Vignette(position,taille,effet.get_skin(vue_case[4]),i))
                            else :
                                self.objets.append(Vignette(position,taille,effet.get_skin(),i))
                for effet in case.effets:
                    if effet.affiche:
                        self.objets.append(Vignette(position,taille,effet.get_skin()))
        else:
            self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))

class Vignette_allie(Final,Affichage):
    def __init__(self,position,agissant:Agissant,esprit,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.shades:List[Affichable] = []
        if shade or invalide:
            self.shades.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.shades.append(Vignette(position,taille,SKIN_SHADE))
        
    def update(self):
        self.objets:List[Affichable] = []
        self.objets.append(Vignettes_agissant(self.position,self.agissant,self.tailles[0]))
        for statut in self.agissant.get_skins_statuts():
            self.objets.append(Vignette(self.position,self.tailles[0],statut))
        self.objets+=self.shades

class Vignette_ennemi(Final,Affichage):
    def __init__(self,position,agissant:Agissant,esprit,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.shades:List[Affichable] = []
        if shade or invalide:
            self.shades.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.shades.append(Vignette(position,taille,SKIN_SHADE))
        
    def update(self):
        self.objets:List[Affichable] = []
        self.objets.append(Vignettes_agissant(self.position,self.agissant,self.tailles[0]))
        for statut in self.agissant.get_skins_statuts():
            self.objets.append(Vignette(self.position,self.tailles[0],statut))
        self.objets+=self.shades

class Vignette_neutre(Final,Affichage):
    def __init__(self,position,agissant:Agissant,esprit,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.shades:List[Affichable] = []
        if shade or invalide:
            self.shades.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.shades.append(Vignette(position,taille,SKIN_SHADE))
        
    def update(self):
        self.objets:List[Affichable] = []
        self.objets.append(Vignettes_agissant(self.position,self.agissant,self.tailles[0]))
        for statut in self.agissant.get_skins_statuts():
            self.objets.append(Vignette(self.position,self.tailles[0],statut))
        self.objets+=self.shades
