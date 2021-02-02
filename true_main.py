import pygame

pygame.init()
screen = pygame.display.set_mode((1350, 690))
##pygame.key.set_repeat(400,200) Ne supporte pas l'utilisation simultanée de plusieurs touches !

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

        for agissant in self.agissants_courants :
            self.controleur.make_vue(agissant)
            agissant.debut_tour()
        for item in self.items_courants :
            item.debut_tour()
        for lab in self.labs_courants:
            lab.debut_tour()
        for esprit in self.esprits_courants:
            esprit.debut_tour() #Des décisions sont prises ici

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

    def complement(self):
        #On doit complémenter une magie

        #Il y a plein de types de magies différentes

        #Il y a aussi une limite de temps

        #Un affichage à gérer

        #On va laisser tout ça au joueur...

        self.controleur.entitees[2].complement() #Ça, c'est pour vérifier que le temps n'est pas écoulé

    def touches(self):
        #On doit changer les touches du joueur

        #On va aussi laisser ça au joueur

        #self.controleur.entitees[2].change_touches()

        pass #Rien à faire ici ?

    def evenement(self):
        #On va encore laisser ça au joueur

        self.controleur.entitees[2].evenement()

    def affichage(self): #À supprimer quand je l'aurais incorporé
        pygame.display.flip()

    def patiente(self,temps): #À supprimer quand je l'aurais incorporé
        self.clock.tick(temps)

    def input(self): #À appeler régulièrement !
        """Fonction qui traite tous les inputs"""

        #On récupère les évènements :
        events = pygame.event.get()
        for event in events :
            if event.type == pygame.QUIT :
                self.quitte() #Sauvegarde la partie en cours et ferme la fenêtre
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
        while self.run : #Devient faux quand on quitte
            if self.controleur.phase == TOUR : #On fait un tour normal
                self.debut_tour()

            self.input()
            if self.controleur.phase == TOUR : #On continue un tour normal
                self.fin_tour()
            elif self.controleur.phase  in [COMPLEMENT_CIBLE,COMPLEMENT_COUT,COMPLEMENT_DIR] : #Le joueur complète son choix d'action
                self.complement()
            elif self.controleur.phase == TOUCHE : #Le joueur modifie ses touches
                self.touches()
            elif self.controleur.phase == EVENEMENT : #Un événement (montée de niveau, dialogue...) interrompt le jeu et le joueur doit réagir
                self.evenement()
            self.affichage()
            self.patiente(20)

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

        while run:
            global ID_MAX
            boutons = [[f"Partie n°{i}",[50,30*i],["Un 'controleur'",f"Le joueur est au niveau {self.controleurs[i].entitees[2].niveau},",f"et a atteint l'étage {self.controleurs[i].entitees[2].position[0]}"],self.controleurs[i]] for i in range(len(self.controleurs))] + [["Nouveau",[50,30*len(self.controleurs)],["Lancer une nouvelle partie"],"new"],["Quitter",[50,30*len(self.controleurs)+30],["Quitter le 'joueur' et revenir à la liste des joueur"],True]]
            res = menu(boutons,screen)
            if res == False:
                run = False
            elif res == "new":
                ID_MAX = 1
                self.controleur = Controleur()
                self.controleurs.append(self.controleur)
                self.controleur.jeu(screen)
                self.boucle()
            elif isinstance(res,Controleur):
                self.controleur = res
                ID_MAX = max(controleur.entitees.keys())
                self.controleur.jeu(screen)
                self.boucle()
            else:
                print("Erreur menu true_main, res non reconnu")
                print(res)

def menu(boutons,screen):
    police=pygame.font.SysFont(None, 20)
    res = False
    curseur = 0
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
                pygame.draw.rect(screen,(155,155,155),(boutons[i][1][0]-2,boutons[i][1][1]-2,54,22))
                descr = boutons[i][2]
            pygame.draw.rect(screen,(255,255,255),(boutons[i][1][0],boutons[i][1][1],50,18))
            text = police.render(boutons[i][0],True,(0,0,0))
            screen.blit(text,(boutons[i][1][0]+4,boutons[i][1][1]+2))

        y = 20
        for tex in descr :
            line = police.render(tex,True,(255,255,255))
            screen.blit(line,(150,y))
            y += 30

        pygame.display.flip()
    if res == True:
        res = False
    return res

global main
main = Main(screen)
#main.start_game()
