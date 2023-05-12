# coding=utf-8

import time
import pygame
import pickle
import os

pygame.init()

screen = pygame.display.set_mode((1350, 690),pygame.RESIZABLE)

from Joueur import *

SKIN_ESCAP.dessine_toi(screen,(0,0))
pygame.display.flip()

class Main():
    """Parce que sans ça on a plein de problèmes avec les variables globales."""
    def __init__(self):
        self.mains:Dict[str, Joueur] = {}
    def observe(self):
        """Fonction qui observe le répertoire courant et cherche des Main à ouvrir, puis les ouvre
           En entrée : rien
           En sortie : rien"""
        #On récupère notre chemin :
        chemin = os.path.abspath(".")
        fichiers = os.listdir(chemin)
        for nom_fichier in fichiers :
            if nom_fichier [-2:] == ".p":
                print(f"Chargement de {nom_fichier}")
                fichier = open(nom_fichier,'rb')
                try:
                    main_potentiel = pickle.load(fichier)
                except EOFError:
                    print("Le fichier est vide. Création d'un nouvel utilisateur.")
                    self.mains[nom_fichier[:-2]]=Joueur(screen)
                except pickle.UnpicklingError:
                    print("Le fichier ne peut pas être décodé ?")
                else:
                    if isinstance(main_potentiel,Joueur):
                        self.mains[nom_fichier[:-2]]=main_potentiel
                        main_potentiel.charge(screen)
                        print("Chargement réussi !")
                    else:
                        print("Le contenu de ce fichier n'a pas pu être interprêté comme un main ! Pourquoi ?")
                finally:
                    fichier.close()

    def sauve(self,nom):
        """Fonction qui sauvegarde un main dans le répertoire courant
           En entrée : le nom du main à sauvegarder
           En sortie : rien"""
        #On ne peut pas pickler les pygame.Surface (c'est à dire les images). Comme les skins ne sont pas directement modifiés par le jeu, on peut s'en délester :
        print(f"Sauvegarde de {nom}.p")
        main = self.mains[nom]
        main.clear()
        #On récupère notre chemin :
        chemin = os.path.abspath(".")
        fichier = open(chemin+"/"+nom+".p",'wb')
        pickle.dump(main,fichier)
        fichier.close()
        print("Sauvegarde réussie")
                
    def quitte(self):
        """Fonction qui sauvegarde et ferme la fenêtre
           En entrée : rien
           En sortie : rien"""

        print("Début de la sauvegarde...")
        for nom in self.mains:
            self.sauve(nom)
        print("Sauvegarde terminée")

    def ouvre(self,nom):
        return self.mains[nom].ouvre()

    def alll(self):
        #On boucle, avec input pour ouvrir un main
        run = True

        while run:
            boutons = [[nom,[nom,"Un 'joueur'",f"Il a {len(self.mains[nom].controleurs)} parties en cours"],self.mains[nom]] for nom in self.mains] + [["Charger",["Charger un nouveau 'joueur' depuis le dossier courant","Pour créer un nouveau 'joueur', placer un fichier 'nom_du_joueur.p' vide dans le dossier courant"],"new"],["Quitter",["Quitter le jeu et fermer la fenêtre"],True]]
            res = menu(boutons,screen)
            if res == False:
                run = False
            elif res == "new":
                self.quitte()
                self.observe()
            elif isinstance(res,Joueur):
                res.ouvre()
            else:
                print("Erreur menu main, res non reconnu")
                print(res)
        self.quitte()

main = Main()
main.observe()
while False:
    try:
        main.alll()
    except KeyboardInterrupt:
        # On print les zones de l'esprit du joueur
        main.mains[0][2].controleur.esprits["heros"].print_zones()
        # On attends une seconde
        time.sleep(1)

main.alll()