import pygame
import copy

pygame.init()
screen = pygame.display.set_mode((1350, 690),pygame.RESIZABLE)

# global GLOBALS
GLOBALS = {"controleur":None}

from Menus import *
from Modifiers import *
from Jeu.Controleur import *
from Affichage.Nouveaux_affichages import *

SKIN_ESCAP.dessine_toi(screen,(0,0))

class Joueur:
    """Un "joueur". Correspondrait idéalement à une personne, à un compte. Pourrait nécessiter un mot de passe.
       Contient les parties, les accomplissements (et skills globaux) et les paramètres de base."""
    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.parametres = {
            # "meta-touches":{ #Quelques touches spéciales, à part
            #     pygame.K_m:"courant", #La barre espace sélectionne, valide, etc. l'objet courant. Elle ne peut pas être modifiée
            #     pygame.K_SPACE:"pause", #La touche d'effacement active/désactive la pause. Elle ne peut pas être modifiée
            # },
            "touches":{
                #Les nouveaux contrôles :
                "effets":{
                    ():{
                        pygame.K_SPACE:"pause",
                        pygame.K_UP:"navigation",
                        pygame.K_RIGHT:"navigation",
                        pygame.K_DOWN:"navigation",
                        pygame.K_LEFT:"navigation",
                        pygame.K_RETURN:"navigation",
                        pygame.K_BACKSPACE:"navigation",
                        pygame.K_TAB:"navigation",
                        pygame.K_e:"interraction",
                    },
                    (pygame.KMOD_LSHIFT):{
                        pygame.K_TAB:"navigation",
                        pygame.K_SPACE:"touches",
                        pygame.K_RETURN:"touches",
                    },
                },
                "directions":{
                    ():{
                        pygame.K_UP:HAUT,
                        pygame.K_RIGHT:DROITE,
                        pygame.K_DOWN:BAS,
                        pygame.K_LEFT:GAUCHE,
                        pygame.K_RETURN:IN,
                        pygame.K_BACKSPACE:OUT,
                        pygame.K_TAB:NEXT,
                    },
                    (pygame.KMOD_SHIFT):{
                        pygame.K_TAB:PREVIOUS,
                    },
                },
                #Les anciens contrôles (à garder pour référence)
                # ():{ #Les touches qui n'ont pas de modificateur
                #     "direction":{
                #         pygame.K_z:HAUT,
                #         pygame.K_d:DROITE,
                #         pygame.K_s:BAS,
                #         pygame.K_q:GAUCHE,
                #     },
                #     "dir_zone":{
                #         pygame.K_UP:HAUT,
                #         pygame.K_RIGHT:DROITE,
                #         pygame.K_DOWN:BAS,
                #         pygame.K_LEFT:GAUCHE,
                #         pygame.K_RETURN:IN,
                #         pygame.K_BACKSPACE:OUT,
                #     },
                #     "skill":{
                #         pygame.K_z:Skill_deplacement,
                #         pygame.K_d:Skill_deplacement,
                #         pygame.K_s:Skill_deplacement,
                #         pygame.K_q:Skill_deplacement,
                #         pygame.K_x:Skill_stomp, 
                #         pygame.K_c:Skill_ramasse,
                #     },
                # },
                # (pygame.KMOD_LSHIFT,):{ #L'ordre des modificateurs est très important ! (Et la virgule aussi, ne me demandez pas pourquoi...)
                #     "direction":{
                #         pygame.K_z:HAUT,
                #         pygame.K_d:DROITE,
                #         pygame.K_s:BAS,
                #         pygame.K_q:GAUCHE,
                #     },
                #     "dir_zone":{},
                #     "skill":{
                #         pygame.K_z:Skill_course,
                #         pygame.K_d:Skill_course,
                #         pygame.K_s:Skill_course,
                #         pygame.K_q:Skill_course,
                #         pygame.K_x:Skill_attaque,
                #     },
                # },
                # (pygame.KMOD_LCTRL,):{ #L'ordre des modificateurs est très important ! (Et la virgule aussi, ne me demandez pas pourquoi...)
                #     "direction":{
                #         pygame.K_z:HAUT,
                #         pygame.K_d:DROITE,
                #         pygame.K_s:BAS,
                #         pygame.K_q:GAUCHE,
                #     },
                #     "dir_zone":{},
                #     "skill":{},
                # },
            },
            "tours_par_seconde":6,
        }
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
        self.affichage.update()
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['update'] += duree
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
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['reste'] += duree
        constantes_temps['courant'] = new_courant
        self.affichage.update()
        new_courant = pygame.time.get_ticks()
        duree = new_courant - constantes_temps['courant']
        constantes_temps['update'] += duree
        constantes_temps['courant'] = new_courant
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

        joueur = self.controleur.joueur
        joueur.inventaire.nettoie_item()
        # joueur.affichage.dessine(joueur)

    # def complement(self):
    #     self.controleur.joueur.complement() #Ça, c'est pour vérifier que le temps n'est pas écoulé

    # def complement_parchemin(self):
    #     self.controleur.joueur.complement_parchemin() #Ça, c'est pour vérifier que le temps n'est pas écoulé

    # def evenement(self):
    #     self.controleur.joueur.evenement()

    def affiche(self,frame,frame_par_tour):
        pygame.display.flip()
        self.patiente(frame_par_tour)

    def patiente(self,frame_par_tour):
        self.clock.tick(self.controleur.tour_par_seconde*frame_par_tour)

    def old_input(self): #À appeler régulièrement !
        """Fonction qui traite tous les inputs"""

        #On récupère les évènements :
        events = pygame.event.get()
        for event in events :
            if event.type == pygame.QUIT : #On a fermé la fenêtre
                self.quitte() #Sauvegarde la partie en cours et ferme la fenêtre
            elif (event.type == pygame.ACTIVEEVENT and event.state == 1) and (event.gain == 0 and not self.controleur.pause):
                self.controleur.toogle_pause()
            elif event.type == pygame.VIDEORESIZE :
                self.controleur.joueur.affichage.recalcule_zones()
            elif event.type == pygame.KEYDOWN :
                self.controleur.joueur.controle(event.key,get_modifiers(event.mod))
            elif event.type == pygame.KEYUP :
                self.controleur.joueur.decontrole(event.key)
            elif event.type in [pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,pygame.MOUSEWHEEL]:
                self.affichage.bouge_souris(event)

    def input(self): #À appeler régulièrement !
        """Fonction qui traite tous les inputs"""
        #On récupère les évènements :
        events = pygame.event.get()
        for event in events :
            if event.type == pygame.QUIT : #On a fermé la fenêtre
                self.quitte() #Sauvegarde la partie en cours et ferme la fenêtre /!\ Modifier ça /!\
            elif (event.type == pygame.ACTIVEEVENT and event.state == 1) and (event.gain == 0 and not self.controleur.pause): #On est passé sur une autre fenêtre. Je vais mettre le jeu en pause pour toi, de rien.
                self.controleur.toogle_pause() #/!\ Rajouter une option pour désactiver la pause auto (afk farm)
            elif event.type == pygame.VIDEORESIZE :
                self.affichage.set_tailles([event.w,event.h])
            elif event.type == pygame.KEYDOWN :
                self.controle(event.key,get_modifiers(event.mod))
            elif event.type == pygame.KEYUP : #Les touches de skill peuvent être maintenues
                self.decontrole(event.key)
            elif event.type in [pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,pygame.MOUSEWHEEL]:
                self.affichage.bouge_souris(event)
        self.recontrole()

    def controle(self,touche,mods=()):
        # Les effets d'une touche dépendent de la situation

        #Certaines touches sont gérées directement ici (actions spécifiques au personnage controllé par le joueur)
        effet = self.parametres["touches"]["effets"].get(mods,{}).get(touche)
        if effet == "pause": # La touche de pause (Espace ?)
            self.controleur.toogle_pause()
        elif effet == "touches" : # On veut changer les touches (Maj + Espace ? Ou Maj + Entrée ?)
            self.start_change_touches() #Peut-être à faire faire par l'affichage ?
        #Rajouter mute etc.

        #Les éléments de navigation
        elif effet == "navigation" : # Les déplacements dans l'affichage (Flèches directionnelles & Return & Backspace & Tabs ?)
            self.affichage.navigue(self.parametres["touches"]["directions"].get(mods,{}).get(touche)) #Fait aussi l'exécution d'actions (équivalent de l'ancien 'courant') par moment

        if self.controleur.phase == TOUR:
            #Les interractions avec l'environnement
            if effet == "interraction" : # Utiliser/sélectionner l'élément courant (E ?) /!\ Gérer ça directement chez le joueur ?
                self.controleur.joueur.interagit()

            #Sinon, c'est qu'on veut controler les actions du perso (comme l'esprit le ferait pour les autres)
            #Vu qu'on a fait les interractions ainsi que tous les choix depuis l'affichage au-dessus, il ne reste plus que les skills et leurs éventuelles précisions
            self.controle_joueur(touche,mods)
            self.controleur.joueur.nouvel_ordre = True

        elif self.controleur.phase == TOUCHE:
            #On veut modifier les touches
            self.continue_change_touche(touche)

    def controle_joueur(self,touche,mods):
        touches = self.controleur.joueur.touches
        effets = touches["effets"].get(mods,{}).get(touche,[]) #Regardons les effets que la touche a
        if "directions" in effets: #La touche a un effet sur la direction du joueur (entre autres)
            self.controleur.joueur.regarde(touches["directions"].get(mods,{}).get(touche))
        if "skills" in effets: #La touche est liée à un skill (entre autres)
            skill = touches["skills"].get(mods,{}).get(touche)
            if skill != None:
                self.controleur.joueur.skill_courant = skill
                if issubclass(skill,Skills_offensifs): # Les skills qui correspondent à un statut d'attaque
                    self.controleur.joueur.statut = "attaque"
                elif issubclass(skill,Skills_projectiles) : # Les skills qui lancent un projectile
                    self.controleur.joueur.projectile_courant = touches["projectiles"].get(touche)
                    self.controleur.joueur.statut = "lancer"
                elif issubclass(skill,Skills_magiques) : # Les skills qui utilisent de la magie
                    self.controleur.joueur.magie_courante = touches["magies"].get(touche) #self.magie_courante n'est que le nom de la magie
                    skill = self.controleur.joueur.get_skill_magique()
                    self.controleur.joueur.magie = skill.magies[self.magie_courante](skill.niveau) #Ici on a une magie similaire (juste pour l'initialisation du choix, oubliée après parce que le skill fournira la vrai magie avec utilise())
                    if isinstance(self.magie,Magies_offensives):
                        self.controleur.joueur.statut = "attaque"
                    #On a éventuellement besoin d'informations supplémentaires sur cette magie
                    if self.controleur.joueur.nouvel_ordre:
                        if isinstance(self.magie,Cible_agissant):
                            self.controleur.set_phase(AGISSANT_MAGIE)
                        if isinstance(self.magie,Cible_case):
                            self.controleur.set_phase(CASE_MAGIE)
                        if isinstance(self.magie,Magie_cout):
                            self.controleur.set_phase(COUT_MAGIE)
                        if isinstance(self.magie,Magie_dirigee):
                            self.controleur.set_phase(DIRECTION_MAGIE)

    def decontrole(self,touche):
        """Fonction qui désélectionne le skill courant si on en relache la touche"""
        if self.controleur.phase == TOUR:
            if not self.controleur.joueur.nouvel_ordre: #On ne veut pas désélectionner un skill qui n'a pas encore été utilisé au moins une fois
                for touches_skills in self.controleur.joueur.touches["skills"].values(): #On ne sait pas quels modificateurs étaient actifs lorsque la touche a été pressée
                    if touches_skills.get(touche) == self.controleur.joueur.skill_courant: #La touche relachée est celle du skill courant
                        self.controleur.joueur.statut = "joueur" #/!\ Vraiment ?
                        self.controleur.joueur.skill_courant = None

    def recontrole(self):
        """La fonction qui réagit aux touches maintenues."""
        # On ne veut pas interférer avec les touches nouvellement descendues :
        if not self.controleur.joueur.nouvel_ordre :
            # On commence par trouver à quelle catégorie appartient la touche :
            mods = get_modifiers(pygame.key.get_mods())
            pressees = pygame.key.get_pressed()
            for key in range(len(pressees)):
                if pressees[key]:
                    self.controle_joueur(key,mods)

    def quitte(self):
        """Fonction qui quitte le jeu, en sauvegardant le controleur"""
        self.run = False
        #Insérer la sauvegarde ici

    def boucle(self):
        """Fonction qui gère tout, agrège les autres"""

        self.run = True
        self.affichage = Affichage_principal(self.controleur,[self.screen.get_width(),self.screen.get_height()])
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
                self.controleur.joueur.inventaire.nettoie_item()
            new_courant = pygame.time.get_ticks()
            duree = new_courant - constantes_temps['courant']
            constantes_temps['reste'] += duree
            constantes_temps['courant'] = new_courant
            self.affichage.affiche(self.screen,1,1)
            new_courant = pygame.time.get_ticks()
            duree = new_courant - constantes_temps['courant']
            constantes_temps['affichage'] += duree
            constantes_temps['courant'] = new_courant
            pygame.display.flip()
            self.patiente(1)
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
                    self.controleur.joueur.affichage.recalcule_zones()
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
        self.affichage = None
        self.controleur = None
        self.agissants_courants = []
        self.items_courants = []
        self.labs_courants = []
        self.esprits_courants = []

    def charge(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        # for controleur in self.controleurs:
        #     controleur.joueur.affichage.unclear(screen)

    def ouvre(self):
        run = True

        # global ID_MAX

        while run:
            boutons = [[f"Partie n°{i}",[f"Le joueur est au niveau {self.controleurs[i][2].niveau},",f"et a atteint l'étage {self.controleurs[i][2].position.lab}"],self.controleurs[i]] for i in range(len(self.controleurs))] + [
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
                    self.controleur.jeu()
                    self.boucle()
                elif res == "tuto":
                    ID_MAX.set_id_max(10)
                    self.controleur = Controleur(self.parametres,self.screen)
                    self.controleurs.append(self.controleur)
                    self.controleur.tuto()
                    self.boucle()
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
                    # self.controleur.joueur.affichage.unclear(screen)
                    # self.controleur.joueur.affichage.recalcule_zones()
                    self.controleur.pause = True
                    self.boucle()
                    run = False
                elif nres == "ctrlc":
                    # res[2].affichage.clear()
                    GLOBALS["controleur"] = res
                elif nres == "supr":
                    self.controleurs.remove(res)
            else:
                print("Erreur menu true_main, res non reconnu")
                print(res)
