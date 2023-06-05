import pygame

class Illustration:
    path = "Affichage/assets/"
    def __init__(self,nom_fichier):
        try:
            self.image = pygame.image.load(self.path+nom_fichier).convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load(self.path+"/vide.png").convert_alpha()
            print(f"N'a pas pu charger {nom_fichier}, remplacé par vide.png")
        except pygame.error as message:
            print("N'oubliez pas d'initialiser pygame avant d'importer l'affichage !")
            raise message

    def dessine_toi(self,screen,position,frame=1,frame_par_tour=1):
        screen.blit(self.image,position)

class Image(Illustration):
    def dessine_toi(self,screen,position,tailles=(40,40),frame=1,frame_par_tour=1,direction=0):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,int(direction)*-90),tailles),position)

class Skin(Illustration):
    def dessine_toi(self,screen,position,taille=40,frame=1,frame_par_tour=1,direction=0):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,int(direction)*-90),(taille,taille)),position)
