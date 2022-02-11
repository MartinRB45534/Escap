import pygame
import copy

pygame.init()
screen = pygame.display.set_mode((1350, 690),pygame.RESIZABLE)

global GLOBALS
GLOBALS = {"controleur":None}

from Menus import *
from Jeu import * #Nécessaire ?
from Jeu.Général import *
from Jeu.Constantes import *

SKIN_ESCAP.dessine_toi(screen,(0,0))

class True_joueur:
    """Un "joueur". Correspondrait idéalement à une personne, à un compte. Pourrait nécessiter un mot de passe.
       Contient les parties, les accomplissements (et skills globaux) et les paramètres de base."""
    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.parametres = {"cat_touches":{pygame.K_UP:"directionelle", #Les touches directionnelles tournent le joueur
                                          pygame.K_DOWN:"directionelle",
                                          pygame.K_LEFT:"directionelle",
                                          pygame.K_RIGHT:"directionelle",
                                          pygame.K_q:"zone", #Les touches de zone déplacent le curseur sur l'affichage
                                          pygame.K_z:"zone",
                                          pygame.K_d:"zone",
                                          pygame.K_s:"zone",
                                          pygame.K_a:"zone",
                                          pygame.K_e:"zone",
                                          pygame.K_p:"skill", #Les skills simples ont leur touche attribuée
                                          pygame.K_w:"skill",
                                          pygame.K_x:"skill",
                                          pygame.K_m:"skill",
                                          pygame.K_r:"skill",
                                          pygame.K_SPACE:"courant", #La barre espace sélectionne, valide, etc. l'objet courant. Elle ne peut pas être modifiée
                                          pygame.K_BACKSPACE:"pause", #La touche d'effacement active/désactive la pause. Elle ne peut pas être modifiée
                                          pygame.K_RETURN:"touches"}, #La touche Entrée confirme certains choix, ou peut modifier les touches. Elle ne peut pas être modifiée
                           "dir_touches":{pygame.K_UP:HAUT, #Les touches associées à une direction
                                          pygame.K_DOWN:BAS,
                                          pygame.K_LEFT:GAUCHE,
                                          pygame.K_RIGHT:DROITE,
                                          pygame.K_q:GAUCHE,
                                          pygame.K_z:HAUT,
                                          pygame.K_d:DROITE,
                                          pygame.K_s:BAS,
                                          pygame.K_a:IN,
                                          pygame.K_e:OUT},
                           "skill_touches":{pygame.K_p:Skill_stomp, #Les touches associées à un skill.
                                            pygame.K_m:Skill_ramasse,
                                            pygame.K_w:Skill_deplacement,
                                            pygame.K_x:Skill_attaque,
                                            pygame.K_r:Skill_course}, #Rajouter un moyen de changer les paramètres du joueur
                           "tours_par_seconde":6}
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
        for lab in self.labs_courants:
            lab.pseudo_debut_tour()

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
            elif event.type == pygame.KEYUP :
                self.controleur.entitees[2].decontrole(event.key)

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
            if self.controleur.phase == TOUR and not self.controleur.pause:
                self.debut_tour()
            else :
                self.pseudo_debut_tour() #Quelques trucs d'affichage

            self.input()
            if self.controleur.phase == TOUR : #On continue un tour normal
                if self.controleur.pause: #Enfin, sauf si on est en pause
                    self.pseudo_fin_tour()
                else:
                    self.fin_tour()
            else:
                if self.controleur.phase  in [COMPLEMENT_CIBLE,COMPLEMENT_COUT,COMPLEMENT_DIR] : #Le joueur complète son choix d'action
                    self.complement()
                elif self.controleur.phase == COMPLEMENT_MENU : #Le joueur modifie ses touches
                    self.complement_menu()
                elif self.controleur.phase  in [COMPLEMENT_CIBLE_PARCHEMIN,COMPLEMENT_COUT_PARCHEMIN,COMPLEMENT_DIR_PARCHEMIN] : #Le joueur complète son choix d'action
                    self.complement_parchemin()
                elif self.controleur.phase == TOUCHE : #Le joueur modifie ses touches
                    self.touches()
                elif self.controleur.phase == EVENEMENT : #Un événement (montée de niveau, dialogue...) interrompt le jeu et le joueur doit réagir
                    self.evenement()
                joueur = self.controleur.entitees[2]
                joueur.inventaire.nettoie_item()
            self.affichage()
            self.patiente()
            new_courant = pygame.time.get_ticks()
            duree = new_courant - constantes_temps['courant']
            constantes_temps['reste'] += duree
            constantes_temps['courant'] = new_courant

    def start(self):
        """Fonction qui commence une partie."""
        clock = pygame.time.Clock()
        panneau = 1
        screen.fill((0,0,0))
        largeur,hauteur = screen.get_size()
        marge_haut = int(hauteur//2 - 345)
        marge_gauche = int(largeur//2 - 675)
        screen.blit(pygame.image.load("Instructions1.png"),(marge_gauche,marge_haut))
        screen.blit(POLICE40.render("Échappez-vous du labyrinthe !",True,(255,255,255)),(marge_gauche+80,marge_haut+325))
        screen.blit(POLICE40.render("Ne vous faites pas",True,(255,255,255)),(marge_gauche+372,marge_haut+450))
        screen.blit(POLICE40.render("tuer par les monstres.",True,(255,255,255)),(marge_gauche+350,marge_haut+490))
        screen.blit(POLICE40.render("Retrouvez les autres humains",True,(255,255,255)),(marge_gauche+832,marge_haut+40))
        screen.blit(POLICE40.render("pour vous échapper tous ensemble.",True,(255,255,255)),(marge_gauche+800,marge_haut+80))
        while panneau != 0:
            events = pygame.event.get()
            for event in events :
                if event.type == pygame.QUIT :
                    self.quitte() #Sauvegarde la partie en cours et ferme la fenêtre
                elif event.type == pygame.VIDEORESIZE :
                    self.controleur.entitees[2].affichage.recalcule_zones()
                elif event.type == pygame.KEYDOWN :
                    screen.fill((0,0,0))
                    largeur,hauteur = screen.get_size()
                    marge_haut = int(hauteur//2 - 345)
                    marge_gauche = int(largeur//2 - 675)
                    if event.key == pygame.K_LEFT and panneau > 1:
                        panneau-=1
                    elif event.key == pygame.K_RIGHT and panneau < 5:
                        panneau+=1
                    elif event.key == pygame.K_BACKSPACE:
                        panneau = 0
                    if panneau == 1:
                        screen.blit(pygame.image.load("Instructions1.png"),(marge_gauche,marge_haut))
                        screen.blit(POLICE40.render("Échappez-vous du labyrinthe !",True,(255,255,255)),(marge_gauche+80,marge_haut+325))
                        screen.blit(POLICE40.render("Ne vous faites pas",True,(255,255,255)),(marge_gauche+372,marge_haut+450))
                        screen.blit(POLICE40.render("tuer par les monstres.",True,(255,255,255)),(marge_gauche+350,marge_haut+490))
                        screen.blit(POLICE40.render("Retrouvez les autres humains",True,(255,255,255)),(marge_gauche+832,marge_haut+40))
                        screen.blit(POLICE40.render("pour vous échapper tous ensemble.",True,(255,255,255)),(marge_gauche+800,marge_haut+80))
                    elif panneau == 2:
                        screen.blit(pygame.image.load("Instructions2.png"),(marge_gauche,marge_haut))
                        screen.blit(POLICE40.render("Déplacez le curseur",True,(255,255,255)),(marge_gauche+60,marge_haut+60))
                        screen.blit(POLICE40.render("avec les touches de zone",True,(255,255,255)),(marge_gauche+60,marge_haut+100))
                        screen.blit(POLICE40.render(f"{self.get_touches_zones()}",True,(255,255,255)),(marge_gauche+60,marge_haut+140))
                        screen.blit(POLICE40.render("(modifiables)",True,(255,255,255)),(marge_gauche+60,marge_haut+180))
                        screen.blit(POLICE40.render(f"{self.get_touche_zone(IN)}",True,(255,255,255)),(marge_gauche+140,marge_haut+500))
                        screen.blit(POLICE40.render(f"{self.get_touche_zone(HAUT)}",True,(255,255,255)),(marge_gauche+230,marge_haut+500))
                        screen.blit(POLICE40.render(f"{self.get_touche_zone(OUT)}",True,(255,255,255)),(marge_gauche+320,marge_haut+500))
                        screen.blit(POLICE40.render(f"{self.get_touche_zone(GAUCHE)}",True,(255,255,255)),(marge_gauche+165,marge_haut+590))
                        screen.blit(POLICE40.render(f"{self.get_touche_zone(BAS)}",True,(255,255,255)),(marge_gauche+255,marge_haut+590))
                        screen.blit(POLICE40.render(f"{self.get_touche_zone(DROITE)}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
                        screen.blit(POLICE20.render(f"Les touches {self.get_touche_zone(HAUT)} et {self.get_touche_zone(BAS)} permettent de",True,(0,255,0)),(marge_gauche+600,marge_haut+80))
                        screen.blit(POLICE20.render("déplacer le curseur verticalement.",True,(0,255,0)),(marge_gauche+600,marge_haut+100))
                        screen.blit(POLICE20.render(f"Les touches {self.get_touche_zone(GAUCHE)} et {self.get_touche_zone(DROITE)} permettent de",True,(255,0,0)),(marge_gauche+775,marge_haut+320))
                        screen.blit(POLICE20.render("déplacer le curseur horizontalement.",True,(255,0,0)),(marge_gauche+775,marge_haut+340))
                        screen.blit(POLICE20.render(f"Les touches {self.get_touche_zone(IN)} et {self.get_touche_zone(OUT)} permettent",True,(0,0,255)),(marge_gauche+1000,marge_haut+220))
                        screen.blit(POLICE20.render("d'entrer dans un élément séléctionné",True,(0,0,255)),(marge_gauche+1000,marge_haut+240))
                        screen.blit(POLICE20.render("et de ressortir vers une zone supérieure.",True,(0,0,255)),(marge_gauche+1000,marge_haut+260))
                    elif panneau == 3:
                        screen.blit(pygame.image.load("Instructions3.png"),(marge_gauche,marge_haut))
                        screen.blit(POLICE40.render("Les flèches directionnelles permettent de diriger le joueur,",True,(255,255,255)),(marge_gauche+280,marge_haut+60))
                        screen.blit(POLICE40.render("et de se déplacer dans tous les menus qui n'utilisent pas les touches de zone.",True,(255,255,255)),(marge_gauche+140,marge_haut+100))
                        screen.blit(POLICE20.render("Les flèches directionnelles ne permettent PAS au joueur de se déplacer,",True,(255,255,255)),(marge_gauche+430,marge_haut+140))
                        screen.blit(POLICE20.render("elles servent seulement à s'orienter (aussi pour les attaque etc.).",True,(255,255,255)),(marge_gauche+450,marge_haut+160))

                        screen.blit(POLICE20.render("Les différentes actions du jeu correspondent généralement à l'utilisation d'un 'skill'.",True,(255,255,255)),(marge_gauche+410,marge_haut+300))
                        screen.blit(POLICE20.render("Les commandes des skills sont explicitées en temps voulu par les personnages humains.",True,(255,255,255)),(marge_gauche+390,marge_haut+320))
                        screen.blit(POLICE40.render("Il est donc fortement conseillé aux nouveaux joueurs de discuter poliment avec les humains.",True,(255,255,255)),(marge_gauche+50,marge_haut+340))
                        screen.blit(POLICE20.render("Les humains qui ont un point d'exclamation à côté de la tête requièrent un dialogue,",True,(255,255,255)),(marge_gauche+410,marge_haut+380))
                        screen.blit(POLICE20.render("mais il est aussi possible de dialoguer de l'initiative du joueur.",True,(255,255,255)),(marge_gauche+450,marge_haut+400))
                    elif panneau == 4:
                        screen.blit(pygame.image.load("Instructions4.png"),(marge_gauche,marge_haut))
                        screen.blit(POLICE20.render("La touche espace est utilisée pour valider certains choix",True,(255,255,255)),(marge_gauche+40,marge_haut+240))
                        screen.blit(POLICE20.render("(choix de la réplique au cours d'un dialogue par exemple),",True,(255,255,255)),(marge_gauche+40,marge_haut+260))
                        screen.blit(POLICE20.render("séléctionner une option parmi plusieurs",True,(255,255,255)),(marge_gauche+40,marge_haut+280))
                        screen.blit(POLICE20.render("(choix des cibles d'une magie par exemple),",True,(255,255,255)),(marge_gauche+40,marge_haut+300))
                        screen.blit(POLICE20.render("interagir avec l'environnement (dialoguer)",True,(255,255,255)),(marge_gauche+40,marge_haut+320))
                        screen.blit(POLICE20.render("et utiliser l'élément sélectionné par les touches de zone",True,(255,255,255)),(marge_gauche+40,marge_haut+340))
                        screen.blit(POLICE20.render("(appeler un allié humain lorsqu'il est loin,",True,(255,255,255)),(marge_gauche+40,marge_haut+360))
                        screen.blit(POLICE20.render("utiliser/équipper un item, utiliser un skill).",True,(255,255,255)),(marge_gauche+40,marge_haut+380))
                        screen.blit(POLICE20.render("La touche entrée est utilisée pour valider certains choix",True,(255,255,255)),(marge_gauche+700,marge_haut+400))
                        screen.blit(POLICE20.render("(valider la sélection des cibles d'une magie par exemple).",True,(255,255,255)),(marge_gauche+700,marge_haut+420))
                        screen.blit(POLICE20.render("Elle ouvre le menu des touches,",True,(255,255,255)),(marge_gauche+700,marge_haut+440))
                        screen.blit(POLICE20.render("qui permet de consulter/modifier les touches de zone et de skill.",True,(255,255,255)),(marge_gauche+700,marge_haut+460))
                        screen.blit(POLICE20.render("La touche retour permet de mettre le jeu en pause et de le remettre en marche.",True,(255,255,255)),(marge_gauche+830,marge_haut+40))
                        screen.blit(POLICE20.render("Le jeu est automatiquement mis en pause lorsque la fenètre passe en arrière-plan.",True,(255,255,255)),(marge_gauche+830,marge_haut+60))
                        screen.blit(POLICE20.render("Lorsqu'il est en pause, le jeu répond toujours aux commandes.",True,(255,255,255)),(marge_gauche+830,marge_haut+80))
                        screen.blit(POLICE20.render("On peut choisir sa prochaine action, utiliser/équipper un item,",True,(255,255,255)),(marge_gauche+830,marge_haut+100))
                        screen.blit(POLICE20.render("donner des consignes aux alliés, et simplement observer la situation.",True,(255,255,255)),(marge_gauche+830,marge_haut+120))
                    elif panneau == 5:
                        screen.blit(pygame.image.load("Instructions5.png"),(marge_gauche,marge_haut))
                        screen.blit(POLICE40.render("Les touches à retenir :",True,(255,255,255)),(marge_gauche+540,marge_haut+200))
                        screen.blit(POLICE40.render("La touche entrée pour consulter/modifier les touches paramétrables.",True,(255,255,255)),(marge_gauche+220,marge_haut+240))
                        screen.blit(POLICE40.render("La touche espace pour dialoguer, sélectionner, utiliser.",True,(255,255,255)),(marge_gauche+280,marge_haut+280))
                        screen.blit(POLICE40.render("La touche retour pour sortir de la pause, et pour quitter/sauter ces explications.",True,(255,255,255)),(marge_gauche+140,marge_haut+320))
                        screen.blit(POLICE40.render("Bon jeu !",True,(255,255,255)),(marge_gauche+620,marge_haut+360))

            pygame.display.flip()
            clock.tick(20)
        self.boucle()

    def get_touches_zones(self):
        return f"{self.get_touche_zone(IN)}, {self.get_touche_zone(OUT)}, {self.get_touche_zone(HAUT)}, {self.get_touche_zone(BAS)}, {self.get_touche_zone(GAUCHE)} et {self.get_touche_zone(DROITE)}"

    def get_touche_zone(self,direction):
        for key in self.parametres["dir_touches"].keys():
            if self.parametres["cat_touches"][key] == "zone" and self.parametres["dir_touches"][key] == direction:
                return pygame.key.name(key).upper()
        return 0

    def set_parametres(self):
        #Fonction qui modifie les paramètres.
        self.parametres = {"cat_touches":{pygame.K_SPACE:"courant",
                                          pygame.K_BACKSPACE:"pause",
                                          pygame.K_RETURN:"touches"},
                           "dir_touches":{pygame.K_UP:HAUT,
                                          pygame.K_DOWN:BAS,
                                          pygame.K_LEFT:GAUCHE,
                                          pygame.K_RIGHT:DROITE},
                           "skill_touches":{},
                           "tours_par_seconde":0}
        #On parcours les paramètres un par un.
        screen.fill((0,0,0))
        largeur,hauteur = screen.get_size()
        marge_haut = int(hauteur//2 - 345)
        marge_gauche = int(largeur//2 - 675)

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "zone"
                            self.parametres["dir_touches"][key] = IN
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementA.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+140,marge_haut+500))
            #Rajouter un texte explicatif sur le role de la touche A

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "zone"
                            self.parametres["dir_touches"][key] = OUT
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementE.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+320,marge_haut+500))
            #Rajouter un texte explicatif sur le role de la touche E

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "zone"
                            self.parametres["dir_touches"][key] = HAUT
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementZ.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+230,marge_haut+500))
            #Rajouter un texte explicatif sur le role de la touche Z

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "zone"
                            self.parametres["dir_touches"][key] = BAS
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementS.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+255,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche S

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "zone"
                            self.parametres["dir_touches"][key] = GAUCHE
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementQ.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+165,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche Q

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "zone"
                            self.parametres["dir_touches"][key] = DROITE
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementD.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche D

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "skill"
                            self.parametres["dir_touches"][key] = Skill_deplacement
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementW.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche W

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "skill"
                            self.parametres["dir_touches"][key] = Skill_course
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementR.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche R

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "skill"
                            self.parametres["dir_touches"][key] = Skill_ramasse
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementM.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche M

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "skill"
                            self.parametres["dir_touches"][key] = Skill_stomp
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementP.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche P

        run = True
        key = None
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if key != None:
                            run = False
                            self.parametres["cat_touches"][key] = "skill"
                            self.parametres["dir_touches"][key] = Skill_attaque
                    elif not(event.key in self.parametres["cat_touches"].keys()):
                        key = event.key
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("RemplacementX.png"),(marge_gauche,marge_haut))
            if key != None:
                screen.blit(POLICE40.render(f"{pygame.key.name(key).upper()}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur le role de la touche X

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.parametres["tours_par_seconde"]>0:
                            run = False
                    elif event.key == pygame.K_UP:
                        self.parametres["tours_par_seconde"] += 1
                    elif event.key == pygame.K_DOWN:
                        self.parametres["tours_par_seconde"] -= 1
                elif event.type == pygame.QUIT:
                    self.parametres = {"cat_touches":{pygame.K_UP:"directionelle",pygame.K_DOWN:"directionelle",pygame.K_LEFT:"directionelle",pygame.K_RIGHT:"directionelle",pygame.K_q:"zone",pygame.K_z:"zone",pygame.K_d:"zone", pygame.K_s:"zone",pygame.K_a:"zone",pygame.K_e:"zone", pygame.K_p:"skill",pygame.K_w:"skill",pygame.K_x:"skill",pygame.K_m:"skill",pygame.K_r:"skill",pygame.K_SPACE:"courant",pygame.K_BACKSPACE:"pause",pygame.K_RETURN:"touches"},"dir_touches":{pygame.K_UP:HAUT,pygame.K_DOWN:BAS,pygame.K_LEFT:GAUCHE,pygame.K_RIGHT:DROITE,pygame.K_q:GAUCHE,pygame.K_z:HAUT,pygame.K_d:DROITE,pygame.K_s:BAS,pygame.K_a:IN,pygame.K_e:OUT},"skill_touches":{pygame.K_p:Skill_stomp,pygame.K_m:Skill_ramasse,pygame.K_w:Skill_deplacement,pygame.K_x:Skill_attaque,pygame.K_r:Skill_course},"tours_par_seconde":6}
                    return

            screen.blit(pygame.image.load("Remplacementtours.png"),(marge_gauche,marge_haut))
            screen.blit(POLICE40.render(f"{self.parametres['tours_par_seconde']}",True,(255,255,255)),(marge_gauche+345,marge_haut+590))
            #Rajouter un texte explicatif sur les tours par seconde
        return True

    def clear(self):
        """Fonction qui enlève tous les éléments superflus avant une sauvegarde."""
        #On veut juste conserver le (les, bientôt j'espère) controleur
        self.screen = None
        self.clock = None
        for controleur in self.controleurs:
            controleur.entitees[2].affichage.clear()
        self.controleur = None

    def charge(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        for controleur in self.controleurs:
            controleur.entitees[2].affichage.unclear(screen)

    def ouvre(self):
        run = True

        global ID_MAX

        while run:
            boutons = [[f"Partie n°{i}",[f"Le joueur est au niveau {self.controleurs[i].entitees[2].niveau},",f"et a atteint l'étage {self.controleurs[i].entitees[2].position[0]}"],self.controleurs[i]] for i in range(len(self.controleurs))] + [
             ["Nouveau",["Lancer une nouvelle partie"],"ctrln"],
             ["Coller",["Ajouter à ce joueur un 'controleur'","Pour transférer une partie d'un joueur à l'autre","Ou pour conserver une sauvegarde"],"ctrlv"],
             ["Contrôles",["Modifier les touches par défaut","Pour modifier les touches d'une partie déjà commencée, appuyer sur Entrée dans la partie (ne fonctionne pas pendant les cinématiques, les dialogues, et les divers menus de sélection."],"ctrl"],
             ["Quitter",["Quitter le 'joueur' et revenir à la liste des joueur"],True]]
            res = menu(boutons,screen)
            if res == False:
                run = False
            elif res == "ctrln":
                boutons = [["Tutoriel",["Un nouveau tutoriel","Les autres tutoriels en cours ne seront pas effacés","","Découvrez le monde d'Escap et rencontrez les pnjs"],"tuto"],
                           ["Nouvelle salle",["Une salle de test","N'y faites pas attention"],"new"],
                           ["Quitter",["Quitter le menu de création de partie et revenir à la liste des parties en cours"],True]]
                res = menu(boutons,screen)
                if res == False:
                    run = False
                elif res == "new":
                    ID_MAX.set_id_max(10)
                    self.controleur = Controleur(self.parametres,self.screen)
                    self.controleurs.append(self.controleur)
                    self.controleur.jeu(screen)
                    self.start()
                elif res == "tuto":
                    ID_MAX.set_id_max(10)
                    self.controleur = Controleur(self.parametres,self.screen)
                    self.controleurs.append(self.controleur)
                    self.controleur.tuto(screen)
                    self.start()
            elif res == "ctrlv":
                if GLOBALS["controleur"] != None:
                    self.controleurs.append(copy.deepcopy(GLOBALS["controleur"]))
            elif res == "ctrl":
                if not self.set_parametres():
                    run = False
            elif isinstance(res,Controleur):
                boutons = [["Ouvrir",["Reprendre cette partie où vous l'aviez laissée","","La partie sera automatiquement en pause"],"ctrlo"],
                           ["Copier",["Copier cette partie dans le presse-papier,","Pour pouvoir la coller autre-part"],"ctrlc"],
                           ["Supprimer",["Supprimer définitivement cette partie"],"supr"],
                           ["Quitter",["Quitter le menu d'ouverture de partie et revenir à la liste des parties en cours"],True]]
                nres = menu(boutons,screen)
                if nres == False:
                    run = False
                elif nres == "ctrlo":
                    self.controleur = res
                    ID_MAX.set_id_max(max(self.controleur.entitees.keys()))
                    self.controleur.entitees[2].affichage.unclear(screen)
                    self.controleur.entitees[2].affichage.recalcule_zones()
                    self.controleur.pause = True
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
