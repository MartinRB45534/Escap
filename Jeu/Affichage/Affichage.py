from calendar import c
import pygame
from Jeu.Constantes import *

class Affichage:
    """Un élément de l'affichage. Peut contenir des sous-éléments."""
    def __init__(self):
        self.objets = [] #La liste des objets à afficher

    def set_objets(self,objets):
        self.objets = objets

    def affiche(self,screen,frame=1,frame_par_tour=1):
        #Fait afficher ses objets
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

class Affichable:
    """Un élément qui s'affiche. Apparaît à l'écran."""
    def __init__(self):
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_tailles(self,tailles):
        self.tailles = tailles

    def set_position(self,position):
        self.position = position

    def affiche(self,screen,frame=1,frame_par_tour=1):
        pass

class Marge(Affichable):
    """Un espace vide."""
    def __init__(self):
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_tailles(self,tailles):
        self.tailles = tailles

    def set_position(self,position):
        self.position = position

    def affiche(self,screen,frame=1,frame_par_tour=1):
        pass

class Vignette(Affichable):
    """Un élément qui est juste une image."""
    def __init__(self,position,tailles,skin):
        self.tailles = tailles
        self.position = position
        self.skin = skin

    def set_tailles(self,tailles):
        print(f"Tu ne peux pas modifier la taille d'une vignette ! Vérifie où tu as rangé {self}.")

    def affiche(self,screen,frame=1,frame_par_tour=1):
        self.skin.dessine_toi(screen,self.position,self.tailles[0],frame,frame_par_tour,0)

class Conteneur(Affichable):
    """Un élément qui peut en 'contenir' d'autres, c'est-à-dire qu'il va les afficher 'à l'interieur' et ils ne pourront pas déborder."""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu = [] #Les objets qu'il 'contient'
        self.fond = (0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
    
    def set_contenu(self,contenu):
        self.contenu = contenu

    def set_fond(self,fond):
        self.fond = fond

    def decale(self,decalage):
        self.position[0] += decalage[0]
        self.position[1] += decalage[1]
        for objet in self.objets:
            objet.decale(decalage)
    
    def affiche(self,screen,frame=1,frame_par_tour=1):
        surf = pygame.Surface(self.tailles)
        surf.fill(self.fond)
        for contenu in self.contenu:
            contenu.affiche(surf,frame,frame_par_tour)
        screen.blit(surf,self.position)
        for objet in self.objets:
            objet.affiche(screen,frame,frame_par_tour)

    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if position[0]>=self.position[0] and position[1]>=self.position[1] and position[0]<self.position[0]+self.tailles[0] and position[1]<self.position[1]+self.tailles[1]:
            for contenu in self.contenu:
                res_contenu = contenu.survol(position)
                if res_contenu:
                    res = res_contenu
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

class Pavage(Conteneur):
    """Contient des objets, qui s'adaptent au pavage"""
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu = [] #Les objets qu'il 'contient'
        self.repartition = [] #La répartition des objets contenus
        self.fond = (0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_contenu(self,contenu,repartition):
        if len(contenu) != len(repartition):
            print("Hey, vérifie ton contenu et ses répartitions")
        else:
            self.contenu = contenu
            self.repartition = repartition

class Pavage_horizontal(Pavage):
    def set_tailles(self,tailles):
        libre = tailles[0] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].tailles[0] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre <= 0:
            print("Je ne pas faire rentrer tout ça là-dedans !")
        else:
            portion = libre/sum(taille for taille in self.repartition if taille<0) # Attention aux divisions par 0
            somme = 0
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille > 0:
                    self.contenu[i].set_tailles([taille,tailles[1]]) #Alternativement, la taille pourrait être décidée par le contenu
                    self.contenu[i].set_position([somme,0])
                    somme += taille
                else:
                    self.contenu[i].set_tailles([taille*portion,tailles[1]])
                    self.contenu[i].set_position([somme,0])
                    somme += taille*portion

class Pavage_vertical(Pavage):
    def set_tailles(self,tailles):
        libre = tailles[1] - sum(self.repartition[i] if self.repartition[i]>0 else self.contenu[i].tailles[1] if not(self.repartition[i]) else 0 for i in range(len(self.repartition)))
        if libre <= 0:
            print("Je ne pas faire rentrer tout ça là-dedans !")
        else:
            portion = libre/sum(taille for taille in self.repartition if taille<0) # Attention aux divisions par 0
            somme = 0
            for i in range(len(self.repartition)):
                taille = self.repartition[i]
                if taille > 0:
                    self.contenu[i].set_tailles([tailles[0],taille])
                    self.contenu[i].set_position([0,somme])
                    somme += taille
                else:
                    self.contenu[i].set_tailles([tailles[0],taille*portion])
                    self.contenu[i].set_position([0,somme])
                    somme += taille*portion

class Liste(Conteneur):
    """Contient des objets, et les affiche à la suite."""
    def set_contenu(self,contenu,courant):
        self.contenu = contenu
        self.courant = courant

class Liste_verticale(Liste):
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu = [] #Les objets qu'il 'contient'
        self.courant = 0 #L'élément 'courant' de la liste
        self.fond = (0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_tailles(self,tailles):
        self.tailles = tailles
        occupe = sum(contenu.tailles[1] for contenu in self.contenu)
        if occupe < tailles[1]:
            somme = 0
        else:
            somme = tailles[1]//2 - sum(contenu.tailles[1] for contenu in self.contenu[:self.courant]) + self.contenu[self.courant].tailles[1]//2
        for contenu in self.contenu:
            contenu.set_position([0,somme])
            somme += contenu.tailles[1]

class Liste_horizontale(Liste):
    def __init__(self):
        self.objets = [] #Il peut quand même avoir des objets 'normaux'
        self.contenu = [] #Les objets qu'il 'contient'
        self.courant = 0 #L'élément 'courant' de la liste
        self.fond = (0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def set_tailles(self,tailles):
        self.tailles = tailles
        occupe = sum(contenu.tailles[0] for contenu in self.contenu)
        if occupe < tailles[0]:
            somme = 0
        else:
            somme = tailles[0]//2 - sum(contenu.tailles[0] for contenu in self.contenu[:self.courant]) + self.contenu[self.courant].tailles[0]//2
        for contenu in self.contenu:
            contenu.set_position([somme,0])
            somme += contenu.tailles[0]

class Liste_menu(Liste):
    """Une liste en plusieurs lignes"""
    def set_tailles(self,tailles):
        self.tailles = tailles
        i=0
        lignes=[]
        ligne=[]
        longueur_ligne=0
        hauteurs_ligne=[]
        ligne_courant=0
        for i in range(len(self.contenu)):
            if self.contenu[i].tailles[0]>tailles[0]:
                print(f"Je n'ai même pas la place d'afficher {self.contenu[i]} !")
                break
            elif longueur_ligne + self.contenu[i].tailles[0] > tailles[0]:
                lignes.append(ligne)
                ligne=[self.contenu[i]]
                longueur_ligne = self.contenu[i].tailles[0]
                hauteurs_ligne.append(self.contenu[i].tailles[1])
            else:
                ligne.append(self.contenu[i])
                longueur_ligne+=self.contenu[i].tailles[0]
                if hauteurs_ligne[-1]<self.contenu[i].tailles[1]:
                    hauteurs_ligne[-1]=self.contenu[i].tailles[1]
            if i==self.courant:
                ligne_courant=len(hauteurs_ligne)-1
        occupe = sum(hauteurs_ligne)
        if occupe < tailles[1]:
            somme = 0
        else:
            somme = tailles[1]//2 - sum(hauteurs_ligne[:ligne_courant]) + hauteurs_ligne[ligne_courant]//2
        for i in len(lignes):
            ligne = lignes[i]
            somme_horizontale = 0
            for contenu in ligne:
                contenu.set_position([somme_horizontale,somme])
                somme_horizontale += contenu.tailles[0]
            somme += hauteurs_ligne[i]

class Survolable(Affichable):
    """Un élément qui réagit au survol"""
    def survol(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if position[0]>=self.position[0] and position[1]>=self.position[1] and position[0]<self.position[0]+self.tailles[0] and position[1]<self.position[1]+self.tailles[1]:
            res=self
        for objet in self.objets:
            res_objet = objet.survol(position)
            if res_objet:
                res = res_objet
        return res

    def highlight(self):
        #Change l'apparence pour indiquer que la souris était là.
        pass

    def get_description(self,observation):
        return ["Hey, je réagis au passage de la souris !",f"C'est cool, non ?","","P.S. Si tu croises Martin, dit lui qu'il y a un problème avec la description de {self} !"]

class Cliquable(Survolable): #Il faut être survolable pour être cliquable
    """Un élément qui réagit aux cliques"""
    def clique(self): #Lui donner un autre paramètre ? Le joueur par exemple ?
        pass #À voir sur les cas particuliers

class Texte(Affichable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self,position,tailles,texte):
        self.tailles = tailles
        self.position = position
        self.texte=texte

    def affiche(self,screen,frame=1,frame_par_tour=1):
        texte=POLICE20.render(self.texte,True,(0,0,0))
        screen.blit(texte,self.position)