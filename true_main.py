import pygame
import copy

pygame.init()
screen = pygame.display.set_mode((1350, 690))

global GLOBALS
GLOBALS = {"controleur":None}

from Jeu import * #Nécessaire ?
from Jeu.Général import *
from Jeu.Constantes import *

global controleur #Pour pouvoir y accéder depuis l'extérieur / À remplacer par global main autre part

class Main: #Modifier le nom plus tard pour plus de cohérence
    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.controleurs = []
        self.controleur = None
        self.agissants_courants = []
        self.items_courants = []
        self.labs_courants = []
        self.esprits_courants = []
        self.run = False

    def debut_tour(self):
        """La fonction qui fait la première moitiée de chaque tour"""

        #On récupère les intervenants du tour
        self.agissants_courants,self.items_courants,self.labs_courants,self.esprits_courants = self.controleur.get_agissants_items_labs_esprits()
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['reste'] += duree
        constantes_temps['courant'] = new_courant

        for agissant in self.agissants_courants :
            self.controleur.make_vue(agissant)
            agissant.debut_tour()
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['agissants.debut_tour'] += duree
        constantes_temps['courant'] = new_courant
        for item in self.items_courants :
            item.debut_tour()
        for lab in self.labs_courants:
            lab.debut_tour()
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['reste'] += duree
        constantes_temps['courant'] = new_courant
        for esprit in self.esprits_courants:
            esprit.debut_tour() #Des décisions sont prises ici
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['esprits'] += duree
        constantes_temps['courant'] = new_courant

    def pseudo_debut_tour(self):
        """La fonction qui fait la première moitiée de chaque tour"""

        #On récupère les intervenants du tour
        self.agissants_courants,self.items_courants,self.labs_courants,self.esprits_courants = self.controleur.get_agissants_items_labs_esprits()

        for agissant in self.agissants_courants :
            self.controleur.make_vue(agissant)
            agissant.pseudo_debut_tour()
        for item in self.items_courants :
            item.pseudo_debut_tour()
        for lab in self.labs_courants:
            lab.pseudo_debut_tour()
        for esprit in self.esprits_courants:
            esprit.pseudo_debut_tour()

    def fin_tour(self):
        """La fonction qui fait la deuxième moitiée de chaque tour"""

        #On a quelques effets supplémentaires...
        for agissant in self.agissants_courants :
            agissant.post_decision()

        #Les agissants méritent leur nom :
        for agissant in self.agissants_courants :
            while agissant.latence <= 0 and agissant.skill_courant != None : #Certains peuvent jouer plusieurs fois par tour !
                self.controleur.fait_agir(agissant)
                agissant.on_action()
            agissant.on_action() #Pour les magies de parchemins

        for item in self.items_courants :
            while item.hauteur > 0 and item.latence <= 0:
                self.controleur.fait_voler(item)

        #On agit sur les actions (principalement des boosts sur les attaques, puis les attaques elles-mêmes sont lancées)
        for agissant in self.agissants_courants :
            agissant.post_action()

        #Le lab agit sur les actions (principalement sur les attaques, pour protéger les occupants de certaines cases)
        for lab in self.labs_courants:
            lab.post_action()

        #Les agissants agissent sur les attaques (s'en protègent, puis les subissent)
        for agissant in self.agissants_courants :
            agissant.pre_attack()

        #On termine le tour
        for agissant in self.agissants_courants :
            agissant.fin_tour()
        for item in self.items_courants :
            item.fin_tour()
        for lab in self.labs_courants:
            lab.fin_tour()
        for esprit in self.esprits_courants:
            esprit.fin_tour()

    def pseudo_fin_tour(self):
        """La fonction qui fait la deuxième moitiée de chaque tour"""

        joueur = self.controleur.entitees[2]
        joueur.inventaire.nettoie_item()
        joueur.affichage.dessine(joueur)

    def complement(self):
        #On doit complémenter une magie

        #Il y a plein de types de magies différentes

        #Il y a aussi une limite de temps

        #Un affichage à gérer

        #On va laisser tout ça au joueur...

        self.controleur.entitees[2].complement() #Ça, c'est pour vérifier que le temps n'est pas écoulé

    def complement_parchemin(self):
        #On doit complémenter une magie lancée depuis un parchemin

        #Il y a plein de types de magies différentes

        #Il y a aussi une limite de temps

        #Un affichage à gérer

        #On va laisser tout ça au joueur...

        self.controleur.entitees[2].complement_parchemin() #Ça, c'est pour vérifier que le temps n'est pas écoulé

    def complement_menu(self):
        #On doit choisir un élément d'un menu

        #Sans limite de temps

        #On va aussi laisser ça au joueur

        pass #Rien à faire ici ?

    def touches(self):
        #On doit changer les touches du joueur

        #On va aussi laisser ça au joueur

        #self.controleur.entitees[2].change_touches()

        pass #Rien à faire ici ?

    def evenement(self):
        #On va encore laisser ça au joueur

        self.controleur.entitees[2].evenement()

    def affichage(self):
        pygame.display.flip()

    def patiente(self):
        self.clock.tick(self.controleur.tour_par_seconde)

    def input(self): #À appeler régulièrement !
        """Fonction qui traite tous les inputs"""

        #On récupère les évènements :
        events = pygame.event.get()
        for event in events :
            if event.type == pygame.QUIT :
                self.quitte() #Sauvegarde la partie en cours et ferme la fenêtre
            elif (event.type == pygame.ACTIVEEVENT and event.state == 1) and (event.gain == 0 and not self.controleur.pause):
                self.controleur.toogle_pause()
            elif event.type == pygame.VIDEORESIZE :
                self.controleur.entitees[2].affichage.recalcule_zones()
            elif event.type == pygame.KEYDOWN :
                self.controleur.entitees[2].controle(event.key)

    def quitte(self):
        """Fonction qui quitte le jeu, en sauvegardant le controleur"""
        self.run = False
        #Insérer la sauvegarde ici

    def boucle(self):
        """Fonction qui gère tout, agrège les autres"""

        self.run = True
        constantes_temps['courant'] = pygame.time.get_ticks()
        while self.run : #Devient faux quand on quitte
            constantes_temps['tours']+=1
            if self.controleur.phase == TOUR :
                self.debut_tour()
            else :
                self.pseudo_debut_tour() #Quelques trucs d'affichage

            self.input()
            if self.controleur.phase == TOUR : #On continue un tour normal
                if self.controleur.pause: #Enfin, sauf si on est en pause
                    self.pseudo_fin_tour()
                else:
                    self.fin_tour()
            elif self.controleur.phase  in [COMPLEMENT_CIBLE,COMPLEMENT_COUT,COMPLEMENT_DIR] : #Le joueur complète son choix d'action
                self.complement()
            elif self.controleur.phase == COMPLEMENT_MENU : #Le joueur modifie ses touches
                self.complement_menu()
            elif self.controleur.phase  in [COMPLEMENT_CIBLE_PARCHEMIN,COMPLEMENT_COUT_PARCHEMIN,COMPLEMENT_DIR_PARCHEMIN] : #Le joueur complète son choix d'action
                self.complement_parchemin()
            elif self.controleur.phase == TOUCHE : #Le joueur modifie ses touches
                self.touches()
            elif self.controleur.phase == EVENEMENT : #Un événement (montée de niveau, dialogue...) interrompt le jeu et le joueur doit réagir
                self.evenement()
            self.affichage()
            self.patiente()
            new_courant = pygame.time.get_ticks()
            duree = new_courant - constantes_temps['courant']
            constantes_temps['reste'] += duree
            constantes_temps['courant'] = new_courant

    def clear(self):
        """Fonction qui enlève tous les éléments superflus avant une sauvegarde."""
        #On veut juste conserver le (les, bientôt j'espère) controleur
        self.screen = None
        self.clock = None
        for controleur in self.controleurs:
            controleur.entitees[2].affichage.clear()

    def charge(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        for controleur in self.controleurs:
            controleur.entitees[2].affichage.unclear(screen)

    def ouvre(self):
        run = True

        global ID_MAX

        while run:
            boutons = [[f"Partie n°{i}",[50,30*i],["Un 'controleur'",f"Le joueur est au niveau {self.controleurs[i].entitees[2].niveau},",f"et a atteint l'étage {self.controleurs[i].entitees[2].position[0]}"],self.controleurs[i]] for i in range(len(self.controleurs))] + [
             ["Nouveau",[50,30*len(self.controleurs)],["Lancer une nouvelle partie"],"ctrln"],
             ["Coller",[50,30*len(self.controleurs)+30],["Ajouter à ce joueur un 'controleur'","Pour transférer une partie d'un joueur à l'autre","Ou pour conserver une sauvegarde"],"ctrlv"],
             ["Quitter",[50,30*len(self.controleurs)+60],["Quitter le 'joueur' et revenir à la liste des joueur"],True]]
            res = menu(boutons,screen)
            if res == False:
                run = False
            elif res == "ctrln":
                boutons = [["Tutoriel",[50,30],["Un nouveau tutoriel","Les autres tutoriels en cours ne seront pas effacés","","Découvrez le monde d'Escap et rencontrez les pnjs"],"tuto"],
                           ["Nouvelle salle",[50,60],["Une salle de test","N'y faites pas attention"],"new"],
                           ["Quitter",[50,90],["Quitter le menu de création de partie et revenir à la liste des parties en cours"],True]]
                res = menu(boutons,screen)
                if res == False:
                    run = False
                elif res == "new":
                    ID_MAX.set_id_max(10)
                    self.controleur = Controleur()
                    self.controleurs.append(self.controleur)
                    self.controleur.jeu(screen)
                    self.boucle()
                elif res == "tuto":
                    ID_MAX.set_id_max(10)
                    self.controleur = Controleur()
                    self.controleurs.append(self.controleur)
                    self.controleur.tuto(screen)
                    self.boucle()
            elif res == "ctrlv":
                if GLOBALS["controleur"] != None:
                    self.controleurs.append(copy.deepcopy(GLOBALS["controleur"]))
            elif isinstance(res,Controleur):
                boutons = [["Ouvrir",[50,30],["Reprendre cette partie où vous l'aviez laissée","","La partie sera automatiquement en pause"],"ctrlo"],
                           ["Copier",[50,60],["Copier cette partie dans le presse-papier,","Pour pouvoir la coller autre-part"],"ctrlc"],
                           ["Supprimer",[50,90],["Supprimer définitivement cette partie"],"supr"],
                           ["Quitter",[50,120],["Quitter le menu d'ouverture de partie et revenir à la liste des parties en cours"],True]]
                nres = menu(boutons,screen)
                if nres == False:
                    run = False
                elif nres == "ctrlo":
                    self.controleur = res
                    ID_MAX.set_id_max(max(self.controleur.entitees.keys()))
                    self.controleur.entitees[2].affichage.unclear(screen)
                    self.boucle()
                    run = False
                elif nres == "ctrlc":
                    res.entitees[2].affichage.clear()
                    GLOBALS["controleur"] = res
                elif nres == "supr":
                    self.controleurs.remove(res)
            else:
                print("Erreur menu true_main, res non reconnu")
                print(res)

def menu(boutons,screen):
    res = False
    curseur = 0
    clock = pygame.time.Clock()
    while not(res):
        #Récupération / traitement des inputs :
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                res = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    res = boutons[curseur][3]
                elif event.key == pygame.K_UP:
                    if curseur == 0:
                        curseur = len(boutons)
                    curseur -= 1
                elif event.key == pygame.K_DOWN:
                    curseur += 1
                    if curseur == len(boutons):
                        curseur = 0
                
                

        #Affichage :
        screen.fill((0,0,0))
        for i in range(len(boutons)) :
            if i == curseur:
                pygame.draw.rect(screen,(155,155,155),(boutons[i][1][0]-2,boutons[i][1][1]-2,104,22))
                descr = boutons[i][2]
            pygame.draw.rect(screen,(255,255,255),(boutons[i][1][0],boutons[i][1][1],100,18))
            text = POLICE20.render(boutons[i][0],True,(0,0,0))
            screen.blit(text,(boutons[i][1][0]+4,boutons[i][1][1]+2))

        y = 20
        for tex in descr :
            line = POLICE20.render(tex,True,(255,255,255))
            screen.blit(line,(150,y))
            y += 30

        pygame.display.flip()
        clock.tick(20)
    if res == True:
        res = False
    return res

##global main
##main = Main(screen)
##main.start_game()
