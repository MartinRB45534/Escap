from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Controleur import Controleur

from Jeu.Entitee.Agissant.Humain.Humain import *
from Jeu.Entitee.Decors.Decors import *
# from Jeu.Entitee.Agissant.Inventaire import Sac_a_dos
from Jeu.Effet.Effets import *
from Jeu.Systeme.Classe import *
from Modifiers import *

class Heros(Humain,Stratege,Multi_mage): #Le premier humain du jeu, avant l'étage 1 (évidemment, c'est le personnage principal !)
    """La classe du joueur."""
    def __init__(self,controleur:Controleur,position:Position,parametres,screen):

        self.identite = 'heros'
        self.place = 0

        Humain.__init__(self,controleur,position,self.identite,1,2)

        self.apreciations = [0,0,0,0,0,0,0,0,0,0]
        self.role = "independant"
        self.resolution = 4
        # self.inventaire.__class__ = Sac_a_dos
        # self.inventaire.complete()

        self.first_kill_=True
        self.magic_kill_=True
        self.third_kill_=True
        self.first_step_=True
        self.first_door_=True
        self.first_teleport_=True

        # #Il doit afficher tout ce qu'il voit...
        # #print("Initialisation du joueur")
        # self.affichage = Faux_affichage(screen)
        # self.event = None
        # self.etage = 0
        # self.arbre = True
        # self.courant = 0
        # self.choix_elems = []
        # self.options_menu = []
        # # print("Affichage : check")
        # self.curseur = "carré" #... et sélectionner un certain nombre de trucs
        self.highest = 0 #Le plus haut où l'on soit allé.

        #Il peut aussi monter de niveau, et a plusieurs choix lorsqu'il le fait :
        self.choix_niveaux = {CLASSIQUE:{1:None, #Le niveau 1 prendra la valeur physique ou magique
                                         2:None, #Le niveau 2 prendra la valeur corps à corps, distance, magie_infinie ou essence magique
                                         3:None, #Les propositions pour les niveaux suivants dépendent grandement du choix aux niveaux 1 et 2
                                         4:None,
                                         5:None,
                                         6:None,
                                         7:None,
                                         8:None,
                                         9:None,
                                         10:None},
                              ELEMENTAL:{TERRE:{affinite:False, #Les choix disponibles pour les éléments dépendent des choix précédents dans les éléments de façon assez complexe
                                                aura:False,
                                                MAGIE:False,
                                                elemental:False},
                                         FEU:{affinite:False,
                                              aura:False,
                                              MAGIE:False,
                                              elemental:False},
                                         GLACE:{affinite:False,
                                                aura:False,
                                                MAGIE:False,
                                                elemental:False},
                                         OMBRE:{affinite:False,
                                                aura:False,
                                                MAGIE:False,
                                                elemental:False}}}
        self.choix_dispos = [] #Modifié au moment de la montée de niveau, ne concerne que l'arbre classique
        self.choix_elem = []
        self.prem_terre = None
        self.prem_feu = None
        self.prem_glace = None
        self.prem_ombre = None

        self.touches = {
            "effets":{
                ():{
                    pygame.K_z:["skills","directions"],
                    pygame.K_d:["skills","directions"],
                    pygame.K_s:["skills","directions"],
                    pygame.K_q:["skills","directions"],
                    pygame.K_x:["skills"],
                    pygame.K_c:["skills"],
                },
                (pygame.KMOD_LSHIFT,):{
                    pygame.K_z:["skills","directions"],
                    pygame.K_d:["skills","directions"],
                    pygame.K_s:["skills","directions"],
                    pygame.K_q:["skills","directions"],
                    pygame.K_x:["skills"],
                    pygame.K_c:["skills"],
                },
                (pygame.KMOD_LCTRL,):{
                    pygame.K_z:["directions"],
                    pygame.K_d:["directions"],
                    pygame.K_s:["directions"],
                    pygame.K_q:["directions"],
                },
            },
            "skills":{
                ():{
                    pygame.K_z:Skill_deplacement,
                    pygame.K_d:Skill_deplacement,
                    pygame.K_s:Skill_deplacement,
                    pygame.K_q:Skill_deplacement,
                    pygame.K_x:Skill_stomp,
                    pygame.K_c:Skill_ramasse_light,
                },
                (pygame.KMOD_LSHIFT,):{
                    pygame.K_z:Skill_course,
                    pygame.K_d:Skill_course,
                    pygame.K_s:Skill_course,
                    pygame.K_q:Skill_course,
                    pygame.K_x:Skill_attaque,
                    pygame.K_c:Skill_ramasse,
                },
            },
            "directions":{
                ():{
                    pygame.K_z:HAUT,
                    pygame.K_d:DROITE,
                    pygame.K_s:BAS,
                    pygame.K_q:GAUCHE,
                },
                (pygame.KMOD_LSHIFT,):{
                    pygame.K_z:HAUT,
                    pygame.K_d:DROITE,
                    pygame.K_s:BAS,
                    pygame.K_q:GAUCHE,
                },
                (pygame.KMOD_LCTRL,):{
                    pygame.K_z:HAUT,
                    pygame.K_d:DROITE,
                    pygame.K_s:BAS,
                    pygame.K_q:GAUCHE,
                },
            },
            "projectiles":{},
            "magies":{},
        }

        #À retirer plus tard
        # self.meta_touches = copy.deepcopy(parametres["meta-touches"])
        # self.touches = copy.deepcopy(parametres["touches"])

        # self.magies = {} #Le skill magie contient beaucoup de magie. La touche est associée à la fois au skill magie et à la magie correspondante.
        # self.too_late = 0
        # self.methode_courante = None
        # magie = Magie_explosion_de_mana
        # skill = trouve_skill(self.classe_principale,Skill_magie)
        # skill.ajoute(magie)
        self.nouvel_ordre = False

        # self.projectiles = {} #Le skill lancer peut s'utiliser de plusieurs façon : en le combinant à un skill de création de projectile, les touches sont associées comme pour les magies# sur l'item courant de l'inventaire, par le biais d'une touche du skill lancer ou, si l'item est un projectile, directement depuis l'inventaire

    def get_skin_tete(self):
        return SKIN_TETE_HEROS

    def get_texte_descriptif(self):
        return [f"Un humain (niveau {self.niveau})",f"ID : {self.ID}","Nom : Arvel","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un humain récemment arrivé dans le labyrinthe."]

    def fuite(self,degats=0):
        return False #À modifier pour quand on prend le controle de Dev

    def debut_tour(self):
        # self.affichage.dessine(self)
        if self.latence <= 0:
            self.nouvel_ordre = False
        Agissant.debut_tour(self)
        if self.get_etage_courant() > self.highest:
            self.highest = self.get_etage_courant()
            if self.highest == 1:
                self.interagit()
            elif self.highest == 2:
                self.interagit()

    def first_kill(self,position):
        """Fonction appelée lorsque le premier gobelin meurt. Déclenche un dialogue de circonstance."""
        if self.first_kill_:
            self.first_kill_=False
            #On vérifie que le dialogue a lieu d'être : le joueur n'a pas rencontré d'autre monstre et il a assisté à la mort du gobelin
            if self.highest == 3 and (self.get_etage_courant() == 3 and self.vue[position][2] > 0):
                #On cherche un PNJ volontaire pour aller taper la causette :
                paume:Humain = self.controleur[4]
                if paume.esprit == "heros" and (paume.get_etage_courant() == 3 and paume.statut_humain in ["exploration","proximite","en chemin"]):
                    paume.mouvement = 2
                    paume.cible_deplacement = 2
                    paume.dialogue = 2
                else:
                    peureuse:Humain = self.controleur[5]
                    if peureuse.esprit == "heros" and (peureuse.get_etage_courant() == 3 and peureuse.statut_humain in ["exploration","proximite","en chemin"]):
                        peureuse.mouvement = 2
                        peureuse.cible_deplacement = 2
                        peureuse.dialogue = 2

    def magic_kill(self,position):
        """Fonction appelée lorsque le premier mage gobelin meurt. Déclenche un dialogue de circonstance."""
        if self.magic_kill_:
            self.magic_kill_=False
            #On vérifie que le dialogue a lieu d'être : le joueur a assisté à la mort du mage gobelin (et donc probablement à ses attaques)
            if self.highest == 4 and (self.get_etage_courant() == 4 and self.vue[position][2] > 0):
                #On cherche un PNJ volontaire pour aller taper la causette :
                peureuse:Humain = self.controleur[5]
                if peureuse.esprit == "heros" and (peureuse.get_etage_courant() == 4 and peureuse.statut_humain in ["exploration","proximite","en chemin"]):
                    peureuse.mouvement = 2
                    peureuse.cible_deplacement = 2
                    peureuse.dialogue = 3
                else:
                    paume:Humain = self.controleur[4]
                    if paume.esprit == "heros" and (paume.get_etage_courant() == 4 and paume.statut_humain in ["exploration","proximite","en chemin"]):
                        paume.mouvement = 2
                        paume.cible_deplacement = 2
                        paume.dialogue = 3

    def third_kill(self):
        """Fonction appelée lorsque le troisième gobelin meurt. Déclenche un dialogue d'explications."""
        if self.third_kill_:
            self.third_kill_=False
            #On vérifie que le dialogue a lieu d'être : le joueur n'est pas encore passé à l'étage suivant
            if self.highest == 4 :
                #On cherche un PNJ volontaire pour aller taper la causette :
                peureuse:Humain = self.controleur[5]
                if peureuse.esprit == "heros" and (peureuse.get_etage_courant() == 4 and peureuse.statut_humain in ["exploration","proximite","en chemin"]):
                    peureuse.mouvement = 2
                    peureuse.cible_deplacement = 2
                    peureuse.dialogue = 4

    def first_step(self):
        """Fonction appelée quand on entre dans la prison. Déclenche un dialogue d'explications."""
        if self.first_step_:
            self.first_step_=False
            #On cherche un PNJ volontaire pour aller taper la causette :
            peureuse:Humain = self.controleur[5]
            if peureuse.esprit == "heros" and peureuse.statut_humain in ["exploration","proximite","en chemin"]:
                peureuse.mouvement = 2
                peureuse.cible_deplacement = 2
                peureuse.dialogue = 5
            else:
                paume:Humain = self.controleur[4]
                if paume.esprit == "heros" and paume.statut_humain in ["exploration","proximite","en chemin"]:
                    paume.mouvement = 2
                    paume.cible_deplacement = 2
                    paume.dialogue = 4

    def first_door(self):
        """Fonction appelée quand on passe la première porte de la prison. Déclenche un dialogue d'explications."""
        if self.first_door_:
            self.first_door_=False
            #La porte qui lance le dialogue certifie qu'on y passe pour la première fois
            #On cherche un PNJ volontaire pour aller taper la causette :
            peureuse:Humain = self.controleur[5]
            if peureuse.esprit == "heros" and peureuse.statut_humain in ["exploration","proximite","en chemin"]:
                peureuse.mouvement = 2
                peureuse.cible_deplacement = 2
                peureuse.dialogue = 6

    def first_teleport(self):
        """Fonction appelée quand on passe le premier téléporteur. Déclenche un dialogue d'explications."""
        if self.first_teleport_:
            self.first_teleport_=False
            #On cherche un PNJ volontaire pour aller taper la causette :
            alchimiste:Humain = self.controleur[7]
            if alchimiste.esprit == "heros" and alchimiste.statut_humain in ["exploration","proximite","en chemin"]:
                alchimiste.mouvement = 2
                alchimiste.dialogue = 2
            else:
                peureuse:Humain = self.controleur[5]
                if peureuse.esprit == "heros" and peureuse.statut_humain in ["exploration","proximite","en chemin"]:
                    peureuse.mouvement = 2
                    peureuse.cible_deplacement = 2
                    peureuse.dialogue = 7
                else:
                    encombrant:Humain = self.controleur[6]
                    if encombrant.esprit == "heros" and encombrant.statut_humain in ["exploration","proximite","en chemin"]:
                        encombrant.mouvement = 2
                        encombrant.cible_deplacement = 2
                        encombrant.dialogue = 2
                    else:
                        paume:Humain = self.controleur[4]
                        if paume.esprit == "heros" and paume.statut_humain in ["exploration","proximite","en chemin"]:
                            paume.mouvement = 2
                            paume.cible_deplacement = 2
                            paume.dialogue = 5

    def get_portee_vue(self):
        skill:Skill_vision = trouve_skill(self.classe_principale,Skill_vision)
        if skill == None:
            print("Oups, je n'ai pas de skill vision ! Pourquoi ?")
            print(self.ID)
            portee = 0
        else :
            portee = skill.utilise()
            portee *= self.get_aff(OMBRE) #Puisque c'est le manque de lumière qui réduit le champ de vision !
        return portee + 2 #Petit cadeau, rien que pour le joueur !

    def get_impact(self):
        if self.skill_courant in [Skill_stomp,Skill_attaque]:
            return Agissant.get_impact(self)
        elif self.skill_courant == Skill_magie:
            magie:Magie = self.get_skill_magique().magies[self.magie_courante]
            if isinstance(magie,Cible_agissant):
                return self.controleur[self.cible_magie].position
            elif isinstance(magie,Cible_case):
                return self.cible_magie
            return self.position
        return self.position

    # def a_parchemin_vierge(self):
    #     return self.inventaire.a_parchemin_vierge()

    # def consomme_parchemin_vierge(self):
    #     return self.inventaire.consomme_parchemin_vierge()

    def interagit(self):
        #On cherche la personne :
        self.interlocuteur = None #Normalement c'est déjà le cas
        for i in [0,-1,1,2]:
            if self.peut_voir(self.dir_regard+i):
                pos = self.position+(self.dir_regard+i)
                interactifs = self.controleur.trouve_interactifs_courants(pos)
                if interactifs!=[]:
                    interactif = self.controleur[interactifs[0]] # Est-ce que je continue à appeler ça un interlocuteur ?
                    if isinstance(interactif,Humain):
                        self.interlocuteur = interactif
                        self.controleur.set_phase(DIALOGUE)
                        interactif.start_dialogue()
                        self.dir_regard+=i
                        interactif.dir_regard = self.dir_regard+2
                    elif isinstance(interactif,Decors_interactif):
                        self.interlocuteur = interactif
                        self.dir_regard+=i
                        if isinstance(interactif,Ustensile):
                            self.controleur.set_phase(RECETTE)
                    break

#/!\ À conserver pour s'y référer (surtout la partie level up) /!\

    # def controle(self,touche,mods=()):
    #     if self.controleur.phase == TOUR:
    #         meta = self.meta_touches.get(touche) #Certaines touches ont un meta-effet, indépendant des modificateurs
    #         if meta == "pause": # La touche de pause
    #             self.controleur.toogle_pause()
    #         elif meta == "courant" : # On a affaire à la touche qui utilise le skill ou l'objet courant
    #             self.utilise_courant()
    #         elif meta == "touches" : # On veut changer les touches
    #             self.start_change_touches()
    #         if mods in self.touches.keys(): #mods est une liste des touches de modifications (Ctrl, Maj, Alt etc.) tenues lors de l'appui de la touche
    #             touches = self.touches[mods] #Si on a des touches enregistrées avec ce modificateur, on peut rechercher si celle qu'on veut y est
    #             direction = touches["direction"].get(touche)
    #             self.regarde(direction)
    #             dir_zone = touches["dir_zone"].get(touche)
    #             self.change_zone(dir_zone)
    #             skill = touches["skill"].get(touche)
    #             if skill != None:
    #                 self.nouvel_ordre = True
    #                 self.skill_courant = skill
    #                 if self.skill_courant == Skill_stomp :
    #                     self.statut = "attaque"
    #                 elif self.skill_courant == Skill_attaque :
    #                     self.statut = "attaque"
    #                 elif self.skill_courant == Skill_lancer : # Le skill lancer contient beaucoup d'objets différends
    #                     self.projectile_courant = touches["projectile"].get(touche)
    #                     self.statut = "lancer"
    #                 elif self.skill_courant == Skill_magie : # Le skill magie contient beaucoup de magies différentes !
    #                     self.magie_courante = touches["magie"].get(touche) #self.magie_courante n'est que le nom de la magie
    #                     skill = trouve_skill(self.classe_principale,Skill_magie)
    #                     self.magie = skill.magies[self.magie_courante](skill.niveau) #Ici on a une magie similaire (juste pour l'initialisation du choix, oubliée après parce que le skill fournira la vrai magie avec utilise())
    #                     if isinstance(self.magie,Magie_cible):
    #                         self.controleur.set_phase(COMPLEMENT_CIBLE)
    #                     if isinstance(self.magie,Magie_cout):
    #                         self.controleur.set_phase(COMPLEMENT_COUT)
    #                     if isinstance(self.magie,Magie_dirigee):
    #                         self.controleur.set_phase(COMPLEMENT_DIR)
    #                     if self.magie_courante in LISTE_EXHAUSTIVE_DES_MAGIES_OFFENSIVES:
    #                         self.statut = "attaque"
    #     elif self.controleur.phase in [COMPLEMENT_CIBLE,COMPLEMENT_COUT,COMPLEMENT_DIR,COMPLEMENT_MENU,COMPLEMENT_CIBLE_PARCHEMIN,COMPLEMENT_COUT_PARCHEMIN,COMPLEMENT_DIR_PARCHEMIN,COMPLEMENT_ALCHIMIE,COMPLEMENT_CUISINE]:
    #         #Les touches servent alors à choisir le complément
    #         self.methode_courante(touche)
    #     elif self.controleur.phase == TOUCHE:
    #         #On veut modifier les touches
    #         self.continue_change_touche(touche)
    #     elif self.controleur.phase == EVENEMENT:
    #         #Il se passe quelque chose !
    #         #Option 1 : une cinématique. On ignore tous les inputs SAUF celui pour passer la cinématique
    #         #Option 2 : un dialogue. Les inputs servent à choisir les réponses et déclenche la réplique suivante/la fin du dialogue
    #         #Option 3 : un choix d'évolution (montée de niveau de la classe principale ou autre avec cadeaux à la clé)
    #         #Option 4 : un choix d'évolution (possibilité de réorganisation des skills/classes)
    #         #Option 5 : une information d'évolution/accomplissement/etc. (est-ce vraiment un évènement ? est-ce une cinématique ?)
    #         #Pour l'instant, on se contente d'implémenter le choix d'évolution :
    #         if self.event == LEVELUP:
    #             self.choisi_cadeau(touche)
    #         elif self.event == DIALOGUE:
    #             self.discute(touche)
    #         elif self.event == COMPLEMENT_DIALOGUE:
    #             self.methode_courante(touche)

    # def recontrole(self):
    #     """La fonction qui réagit aux touches maintenues."""
    #     # On ne veut pas interférer avec les touches nouvellement descendues :
    #     if not self.nouvel_ordre :
    #         # On commence par trouver à quelle catégorie appartient la touche :
    #         mods = get_modifiers(pygame.key.get_mods())
    #         touches = self.touches.get(mods)
    #         if touches != None:
    #             pressees = pygame.key.get_pressed()
    #             for touche in touches["skill"].keys():
    #                 if pressees[touche]:
    #                     skill = touches["skill"].get(touche)
    #                     self.skill_courant = skill
    #                     if self.skill_courant == Skill_stomp :
    #                         self.statut = "attaque"
    #                     elif self.skill_courant == Skill_attaque :
    #                         self.statut = "attaque"
    #                     elif self.skill_courant == Skill_magie : # Le skill magie contient beaucoup de magies différentes !
    #                         self.magie_courante = self.magies[touche]
    #                         skill = trouve_skill(self.classe_principale,Skill_magie)
    #                         self.magie = skill.magies[self.magie_courante](skill.niveau) #Ici on a une magie similaire (juste pour l'initialisation du choix, oubliée après parce que le skill fournira la vrai magie avec utilise())
    #                         if self.magie_courante in LISTE_EXHAUSTIVE_DES_MAGIES_OFFENSIVES:
    #                             self.statut = "attaque"
    #                     elif self.skill_courant == Skill_lancer : # Le skill lancer contient beaucoup d'objets différends
    #                         self.projectile_courant = self.projectiles[touche]
    #                         self.statut = "lancer"

    # def decontrole(self,touche):
    #     #Une touche s'est relevée
    #     if not self.nouvel_ordre: #Le skill courant actuel ne vient pas d'une touche récente
    #         if self.controleur.phase == TOUR:
    #             for touches in self.touches.values():
    #                 if touche in touches["skill"].keys():
    #                     if touches["skill"].get(touche) == self.skill_courant: #La touche relachée est celle du skill courant
    #                         self.statut = "joueur"
    #                         self.skill_courant = None
    #                         self.recontrole()

# #     def complement(self):
# #         """Appelée une fois par tour pendant le choix des complements
# #            Gère le temps et l'affichage"""
# #         if self.methode_courante == None :
# #             if self.controleur.phase == COMPLEMENT_DIR:
# #                 self.start_select_direction(self.magie)
# #             elif self.controleur.phase == COMPLEMENT_COUT:
# #                 self.start_select_cout(self.magie)
# #             elif self.controleur.phase == COMPLEMENT_CIBLE:
# #                 self.start_select_cible(self.magie)
# #         current_time = pygame.time.get_ticks()
# #         if current_time > self.too_late :
# #             #Le temps est écoulé !
# #             self.methode_courante = None
# #             self.start_time = 0
# #             self.too_late = 0
# #             self.precision_cout_magie = 0
# #             self.choix_cout_magie = 0
# #             self.element_courant = 0
# #             #Etc.
# #             self.controleur.unset_phase(self.controleur.phase)
# #         else :
# #             proportion_ecoulee = (current_time - self.start_time)/self.temps
# #             if self.methode_courante == self.continue_select_direction:
# #                 self.affichage.redraw_magie_dir(self,proportion_ecoulee)
# #             elif self.methode_courante == self.continue_select_cout:
# #                 self.affichage.redraw_magie_cout(self,proportion_ecoulee)
# #             elif self.methode_courante == self.continue_select_cible:
# #                 self.affichage.redraw_magie_cible(self,proportion_ecoulee)
# #             elif self.methode_courante == self.continue_select_case:
# #                 self.affichage.redraw_magie_case(self,proportion_ecoulee)

# #     def start_select_direction(self,magie):
# #         self.methode_courante = self.continue_select_direction #Est-ce que ça fonctionnera avec le self comme ça ? Hum...
# #         self.affichage.draw_magie_dir(self)
# #         self.temps = magie.temps
# #         self.start_time = pygame.time.get_ticks()
# #         self.too_late = self.start_time + self.temps

# #     def continue_select_direction(self,touche):
# #         if touche == pygame.K_UP :
# #             self.dir_regard = HAUT
# #         elif touche == pygame.K_DOWN :
# #             self.dir_regard = BAS
# #         elif touche == pygame.K_LEFT :
# #             self.dir_regard = GAUCHE
# #         elif touche == pygame.K_RIGHT :
# #             self.dir_regard = DROITE
# #         elif touche == pygame.K_RETURN :
# #             self.dir_magie = self.dir_regard
# #             self.controleur.unset_phase(COMPLEMENT_DIR)
# #             self.methode_courante = None

# #     def start_select_cout(self,magie):
# #         self.methode_courante = self.continue_select_cout #Est-ce que ça fonctionnera avec le self comme ça ? Hum...
# #         self.precision_cout_magie = 10
# #         self.choix_cout_magie = 0
# #         self.affichage.draw_magie_cout(self)
# #         self.temps = magie.temps
# #         self.start_time = pygame.time.get_ticks()
# #         self.too_late = self.start_time + self.temps

# #     def continue_select_cout(self,touche):
# #         if touche == pygame.K_UP and self.choix_cout_magie + self.precision_cout_magie <= self.get_total_pm() :
# #             self.choix_cout_magie += self.precision_cout_magie
# #         elif touche == pygame.K_DOWN and self.choix_cout_magie - self.precision_cout_magie >= 0:
# #             self.choix_cout_magie -= self.precision_cout_magie
# #         elif touche == pygame.K_LEFT and self.precision_cout_magie > 0:
# #             self.precision_cout_magie -= 1
# #         elif touche == pygame.K_RIGHT :
# #             self.precision_cout_magie += 1
# #         elif touche == pygame.K_RETURN :
# #             self.cout_magie = self.choix_cout_magie
# #             self.controleur.unset_phase(COMPLEMENT_COUT)
# #             self.methode_courante = None

# #     def start_select_cible(self,magie):
# #         if isinstance(magie,Multi_cible):
# #             self.multi = True
# #         else:
# #             self.multi = False
# #         if isinstance(magie,Cible_agissant):
# #             self.methode_courante = self.continue_select_cible
# #             self.cibles = self.controleur.get_cibles_potentielles_agissants(magie,self)
# #             self.element_courant = 0 #Je recycle
# #             self.cible = []
# #             self.affichage.draw_magie_cible(self)
# #             self.temps = magie.temps
# #             self.start_time = pygame.time.get_ticks()
# #             self.too_late = self.start_time + self.temps
# #         elif isinstance(magie,Cible_item):
# #             self.methode_courante = self.continue_select_cible
# #             self.cibles = self.controleur.get_cibles_potentielles_items(magie,self)
# #             self.element_courant = 0 #Je recycle
# #             self.cible = []
# #             self.affichage.draw_magie_cible(self)
# #             self.temps = magie.temps
# #             self.start_time = pygame.time.get_ticks()
# #             self.too_late = self.start_time + self.temps
# #         elif isinstance(magie,Cible_case):
# #             self.start_select_cible_case(magie)

# #     def continue_select_cible(self,touche):
# #         if touche == pygame.K_UP :
# #             if self.element_courant == 0:
# #                 self.element_courant = len(self.cibles)
# #             self.element_courant -= 1
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant += 1
# #             if self.element_courant == len(self.cibles):
# #                 self.element_courant = 0
# #         elif touche == pygame.K_SPACE :
# #             new_cible = self.cibles[self.element_courant]
# #             if self.multi : #Si jamais une magie peut cibler plusieurs cibles.
# #                 if new_cible in self.cible :
# #                     self.cible.remove(new_cible)
# #                 else :
# #                     self.cible.append(new_cible)
# #             else:
# #                 self.cible = [new_cible]
# #         elif touche == pygame.K_RETURN and self.cible != [] :
# #             if self.multi :
# #                 self.cible_magie = self.cible
# #             elif self.cible != []:
# #                 self.cible_magie = self.cible[0]
# #             self.controleur.unset_phase(COMPLEMENT_CIBLE)
# #             self.methode_courante = None

# #     def start_select_cible_case(self,magie):
# #         self.methode_courante = self.continue_select_case
# #         self.cibles = self.controleur.get_cibles_potentielles_cases(magie,self)
# #         self.element_courant = self.position #Je recycle
# #         self.cible = []
# #         self.affichage.draw_magie_case(self)
# #         self.temps = magie.temps
# #         self.start_time = pygame.time.get_ticks()
# #         self.too_late = self.start_time + self.temps

# #     def continue_select_case(self,touche):
# #         if touche == pygame.K_UP :
# #             self.element_courant = self.element_courant + HAUT
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant = self.element_courant + BAS
# #         elif touche == pygame.K_LEFT :
# #             self.element_courant = self.element_courant + GAUCHE
# #         elif touche == pygame.K_RIGHT :
# #             self.element_courant = self.element_courant + DROITE
# #         elif touche == pygame.K_SPACE and self.element_courant in self.cibles:
# #             if self.multi : #Si jamais une magie peut cibler plusieurs cibles.
# #                 if self.element_courant in self.cible :
# #                     self.cible.remove(self.element_courant)
# #                 else :
# #                     self.cible.append(self.element_courant)
# #             else:
# #                 self.cible = [self.element_courant]
# #         elif touche == pygame.K_RETURN and self.cible != [] :
# #             if self.multi :
# #                 self.cible_magie = self.cible
# #             else:
# #                 self.cible_magie = self.cible[0]
# #             self.controleur.unset_phase(COMPLEMENT_CIBLE)
# #             self.methode_courante = None

# #     def start_select_agissant_dialogue(self):
# #         self.methode_courante = self.continue_select_cible_dialogue
# #         self.cibles = self.controleur.get_esprit(self.esprit).get_agissants_vus(self)
# #         self.element_courant = 0 #Je recycle
# #         self.cible = []
# #         self.affichage.draw_magie_cible(self)
# #         self.multi = False

# #     def continue_select_cible_dialogue(self,touche):
# #         if touche == pygame.K_UP :
# #             if self.element_courant == 0:
# #                 self.element_courant = len(self.cibles)
# #             self.element_courant -= 1
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant += 1
# #             if self.element_courant == len(self.cibles):
# #                 self.element_courant = 0
# #         elif touche == pygame.K_SPACE :
# #             new_cible = self.cibles[self.element_courant]
# #             self.cible = [new_cible]
# #         elif touche == pygame.K_RETURN and self.cible != [] :
# #             self.interlocuteur.set_cible(self.cible[0])
# #             self.event = DIALOGUE
# #             self.methode_courante = None

# #     def start_select_case_dialogue(self):
# #         self.methode_courante = self.continue_select_case_dialogue
# #         self.cibles = self.controleur.get_esprit(self.esprit).get_cases_vues(self)
# #         self.element_courant = self.position #Je recycle
# #         self.cible = []
# #         self.affichage.draw_magie_case(self)
# #         self.multi = False

# #     def continue_select_case_dialogue(self,touche):
# #         if touche == pygame.K_UP :
# #             self.element_courant = self.element_courant + HAUT
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant = self.element_courant + BAS
# #         elif touche == pygame.K_LEFT :
# #             self.element_courant = self.element_courant + GAUCHE
# #         elif touche == pygame.K_RIGHT :
# #             self.element_courant = self.element_courant + DROITE
# #         elif touche == pygame.K_SPACE and self.element_courant in self.cibles:
# #             self.cible = [self.element_courant]
# #         elif touche == pygame.K_RETURN and self.cible != [] :
# #             self.interlocuteur.set_cible(self.cible[0])
# #             self.event = DIALOGUE
# #             self.methode_courante = None

# #     def complement_parchemin(self):
# #         """Appelée une fois par tour pendant le choix des complements
# #            Gère le temps et l'affichage"""
# #         if self.methode_courante == None :
# #             if self.controleur.phase == COMPLEMENT_DIR_PARCHEMIN:
# #                 self.start_select_direction_parchemin(self.magie_parchemin)
# #             elif self.controleur.phase == COMPLEMENT_COUT_PARCHEMIN:
# #                 self.start_select_cout_parchemin(self.magie_parchemin)
# #             elif self.controleur.phase == COMPLEMENT_CIBLE_PARCHEMIN:
# #                 self.start_select_cible_parchemin(self.magie_parchemin)
# #         current_time = pygame.time.get_ticks()
# #         if current_time > self.too_late :
# #             #Le temps est écoulé !
# #             self.methode_courante = None
# #             self.start_time = 0
# #             self.too_late = 0
# #             self.precision_cout_magie = 0
# #             self.choix_cout_magie = 0
# #             self.element_courant = 0
# #             #Etc.
# #             self.controleur.unset_phase(self.controleur.phase)
# #         else :
# #             proportion_ecoulee = (current_time - self.start_time)/self.temps
# #             if self.methode_courante == self.continue_select_direction_parchemin:
# #                 self.affichage.redraw_magie_dir(self,proportion_ecoulee)
# #             elif self.methode_courante == self.continue_select_cout_parchemin:
# #                 self.affichage.redraw_magie_cout(self,proportion_ecoulee)
# #             elif self.methode_courante == self.continue_select_cible_parchemin:
# #                 self.affichage.redraw_magie_cible(self,proportion_ecoulee)
# #             elif self.methode_courante == self.continue_select_case_parchemin:
# #                 self.affichage.redraw_magie_case(self,proportion_ecoulee)

# #     def start_select_direction_parchemin(self,magie):
# #         self.methode_courante = self.continue_select_direction_parchemin #Est-ce que ça fonctionnera avec le self comme ça ? Hum...
# #         self.affichage.draw_magie_dir(self)
# #         self.temps = magie.temps
# #         self.start_time = pygame.time.get_ticks()
# #         self.too_late = self.start_time + self.temps

# #     def continue_select_direction_parchemin(self,touche):
# #         if touche == pygame.K_UP :
# #             self.dir_regard = HAUT
# #         elif touche == pygame.K_DOWN :
# #             self.dir_regard = BAS
# #         elif touche == pygame.K_LEFT :
# #             self.dir_regard = GAUCHE
# #         elif touche == pygame.K_RIGHT :
# #             self.dir_regard = DROITE
# #         elif touche == pygame.K_RETURN :
# #             self.dir_magie_parchemin = self.dir_regard
# #             self.controleur.unset_phase(COMPLEMENT_DIR_PARCHEMIN)
# #             self.methode_courante = None

# #     def start_select_cout_parchemin(self,magie):
# #         self.methode_courante = self.continue_select_cout_parchemin #Est-ce que ça fonctionnera avec le self comme ça ? Hum...
# #         self.precision_cout_magie = 10
# #         self.choix_cout_magie = 0
# #         self.affichage.draw_magie_cout(self)
# #         self.temps = magie.temps
# #         self.start_time = pygame.time.get_ticks()
# #         self.too_late = self.start_time + self.temps

# #     def continue_select_cout_parchemin(self,touche):
# #         if touche == pygame.K_UP and self.choix_cout_magie + self.precision_cout_magie <= self.get_total_pm() :
# #             self.choix_cout_magie += self.precision_cout_magie
# #         elif touche == pygame.K_DOWN and self.choix_cout_magie - self.precision_cout_magie >= 0:
# #             self.choix_cout_magie -= self.precision_cout_magie
# #         elif touche == pygame.K_LEFT and self.precision_cout_magie > 0:
# #             self.precision_cout_magie -= 1
# #         elif touche == pygame.K_RIGHT :
# #             self.precision_cout_magie += 1
# #         elif touche == pygame.K_RETURN :
# #             self.cout_magie_parchemin = self.choix_cout_magie
# #             self.controleur.unset_phase(COMPLEMENT_COUT_PARCHEMIN)
# #             self.methode_courante = None

# #     def start_select_cible_parchemin(self,magie):
# #         if isinstance(magie,Multi_cible):
# #             self.multi = True
# #         else:
# #             self.multi = False
# #         if isinstance(magie,Cible_agissant):
# #             self.methode_courante = self.continue_select_cible_parchemin
# #             self.cibles = self.controleur.get_cibles_potentielles_agissants(magie,self)
# #             self.element_courant = 0 #Je recycle
# #             self.cible = []
# #             self.affichage.draw_magie_cible(self)
# #             self.temps = magie.temps
# #             self.start_time = pygame.time.get_ticks()
# #             self.too_late = self.start_time + self.temps
# #         elif isinstance(magie,Cible_item):
# #             self.methode_courante = self.continue_select_cible_parchemin
# #             self.cibles = self.controleur.get_cibles_potentielles_items(magie,self)
# #             self.element_courant = 0 #Je recycle
# #             self.cible = []
# #             self.affichage.draw_magie_cible(self)
# #             self.temps = magie.temps
# #             self.start_time = pygame.time.get_ticks()
# #             self.too_late = self.start_time + self.temps
# #         elif isinstance(magie,Cible_case):
# #             self.start_select_cible_case_parchemin(magie)

# #     def continue_select_cible_parchemin(self,touche):
# #         if touche == pygame.K_UP :
# #             if self.element_courant == 0:
# #                 self.element_courant = len(self.cibles)
# #             self.element_courant -= 1
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant += 1
# #             if self.element_courant == len(self.cibles):
# #                 self.element_courant = 0
# #         elif touche == pygame.K_SPACE :
# #             new_cible = self.cibles[self.element_courant]
# #             if self.multi : #Si jamais une magie peut cibler plusieurs cibles.
# #                 if new_cible in self.cible :
# #                     self.cible.remove(new_cible)
# #                 else :
# #                     self.cible.append(new_cible)
# #             else:
# #                 self.cible = [new_cible]
# #         elif touche == pygame.K_RETURN and self.cible != [] :
# #             if self.multi :
# #                 self.cible_magie_parchemin = self.cible
# #             elif self.cible != []:
# #                 self.cible_magie_parchemin = self.cible[0]
# #             self.controleur.unset_phase(COMPLEMENT_CIBLE_PARCHEMIN)
# #             self.methode_courante = None

# #     def start_select_cible_case_parchemin(self,magie):
# #         self.methode_courante = self.continue_select_case_parchemin
# #         self.cibles = self.controleur.get_cibles_potentielles_cases(magie,self)
# #         self.element_courant = self.position #Je recycle
# #         self.cible = []
# #         self.affichage.draw_magie_case(self)
# #         self.temps = magie.temps
# #         self.start_time = pygame.time.get_ticks()
# #         self.too_late = self.start_time + self.temps

# #     def continue_select_case_parchemin(self,touche):
# #         if touche == pygame.K_UP :
# #             self.element_courant = self.element_courant + HAUT
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant = self.element_courant + BAS
# #         elif touche == pygame.K_LEFT :
# #             self.element_courant = self.element_courant + GAUCHE
# #         elif touche == pygame.K_RIGHT :
# #             self.element_courant = self.element_courant + DROITE
# #         elif touche == pygame.K_SPACE and self.element_courant in self.cibles:
# #             if self.multi : #Si jamais une magie peut cibler plusieurs cibles.
# #                 if self.element_courant in self.cible :
# #                     self.cible.remove(self.element_courant)
# #                 else :
# #                     self.cible.append(self.element_courant)
# #             else:
# #                 self.cible = [self.element_courant]
# #         elif touche == pygame.K_RETURN and self.cible != [] :
# #             if self.multi :
# #                 self.cible_magie_parchemin = self.cible
# #             else:
# #                 self.cible_magie_parchemin = self.cible[0]
# #             self.controleur.unset_phase(COMPLEMENT_CIBLE_PARCHEMIN)
# #             self.methode_courante = None

# #     def start_menu(self):
# #         self.controleur.set_phase(COMPLEMENT_MENU)
# #         self.element_courant = 0
# #         self.cible = None
# #         self.methode_courante = self.continue_menu
# #         self.affichage.draw_menu(self)

# #     def continue_menu(self,touche):
# #         if touche == pygame.K_UP : #Ne fonctionne pas pour le coin /!\
# #             elements_par_ligne = (self.affichage.largeur_exploitable-20)//50 #On veut exactement les même calculs ici que dans l'affichage, source potentielle d'erreurs /!\
# #             elements_par_colone = len(self.options_menu)//elements_par_ligne
# #             if len(self.options_menu)%elements_par_ligne != 0:
# #                 elements_par_colone += 1
# #             self.element_courant -= elements_par_ligne
# #             if self.element_courant < 0: #On était sur la première ligne. Aller plus haut, c'est revenir en haut de la colone précédente
# #                 self.element_courant += elements_par_ligne*elements_par_colone-1
# #                 if self.element_courant >= len(self.options_menu):
# #                     self.element_courant -= elements_par_ligne
# #         elif touche == pygame.K_DOWN : #Ne fonctionne pas pour le coin /!\
# #             elements_par_ligne = (self.affichage.largeur_exploitable-20)//50 #On veut exactement les même calculs ici que dans l'affichage, source potentielle d'erreurs /!\
# #             elements_par_colone = len(self.options_menu)//elements_par_ligne
# #             if len(self.options_menu)%elements_par_ligne != 0:
# #                 elements_par_colone += 1
# #             self.element_courant += elements_par_ligne
# #             if self.element_courant >= len(self.options_menu): #On était sur la dernière ligne. Aller plus bas, c'est revenir en bas de la colone suivante
# #                 self.element_courant -= elements_par_ligne*elements_par_colone-1
# #                 if self.element_courant < 0:
# #                     self.element_courant += elements_par_ligne
# #         elif touche == pygame.K_LEFT :
# #             if self.element_courant == 0:
# #                 self.element_courant = len(self.options_menu)
# #             self.element_courant -= 1
# #         elif touche == pygame.K_RIGHT :
# #             self.element_courant += 1
# #             if self.element_courant == len(self.options_menu):
# #                 self.element_courant = 0
# #         elif touche == pygame.K_SPACE :
# #             self.cible = self.element_courant
# #         elif touche == pygame.K_RETURN and self.cible != None :
# #             self.methode_fin(self.options_menu[self.cible])
# #             self.controleur.unset_phase(COMPLEMENT_MENU)
# #             self.methode_courante = None
# #         self.affichage.draw_menu(self)

# #     def fin_menu_magie(self,choix): #Le menu servait à choisir une magie à lancer
# #         self.controleur.unset_phase(COMPLEMENT_MENU)
# #         self.methode_courante = None
# #         self.methode_fin = None
# #         self.magie_courante = choix.nom
# #         self.magie = choix #Ici on a une magie similaire (juste pour l'initialisation du choix, oubliée après parce que le skill fournira la vrai magie avec utilise())
# #         if isinstance(self.magie,Magie_cible):
# #             self.controleur.set_phase(COMPLEMENT_CIBLE)
# #         if isinstance(self.magie,Magie_cout):
# #             self.controleur.set_phase(COMPLEMENT_COUT)
# #         if isinstance(self.magie,Magie_dirigee):
# #             self.controleur.set_phase(COMPLEMENT_DIR)
# #         if self.magie_courante in LISTE_EXHAUSTIVE_DES_MAGIES_OFFENSIVES:
# #             self.statut = "attaque"

# #     def fin_menu_item(self,choix): #Le menu servait à choisir un item à lancer
# #         self.controleur.unset_phase(COMPLEMENT_MENU)
# #         self.methode_courante = None
# #         self.methode_fin = None
# #         self.projectile_courant = choix.ID

# #     def fin_menu_auto_impregnation(self,choix): #Le menu servait à choisir une magie du joueur à imprégner sur un parchemin
# #         skill = trouve_skill(self.classe_principale,Skill_magie)
# #         latence,magie = skill.utilise(choix.nom)
# #         self.latence += latence
# #         cout = magie.cout_pm
# #         if self.peut_payer(cout):
# #             self.controleur.unset_phase(COMPLEMENT_MENU)
# #             self.methode_courante = None
# #             self.methode_fin = None
# #             self.paye(cout)
# #             parch = Parchemin_impregne(None,magie,cout//2)
# #             self.controleur.ajoute_entitee(parch)
# #             self.inventaire.ajoute(parch)
# #         else:
# #             self.affichage.message("Tu n'as pas assez de mana pour utiliser ça !")

# #     def fin_menu_impregnation(self,choix): #Le menu servait à choisir une magie d'un PNJ à imprégner sur un parchemin
# #         self.controleur.unset_phase(COMPLEMENT_MENU)
# #         self.methode_courante = None
# #         self.methode_fin = None
# #         self.interlocuteur.impregne(choix.nom)

# #     def fin_menu_vente(self,choix): #Le menu servait à choisir un item à vendre au marchand
# #         self.controleur.unset_phase(COMPLEMENT_MENU)
# #         self.methode_courante = None
# #         self.methode_fin = None
# #         self.interlocuteur.vend(choix.ID)

# #     def fin_menu_achat(self,choix): #Le menu servait à choisir un item à acheter au marchand
# #         self.controleur.unset_phase(COMPLEMENT_MENU)
# #         self.methode_courante = None
# #         self.methode_fin = None
# #         self.interlocuteur.achete(choix.ID)

# #     def start_menu_cuisine(self):
# #         self.controleur.set_phase(COMPLEMENT_CUISINE)
# #         self.element_courant = 0
# #         self.cible = None
# #         self.methode_courante = self.continue_menu_cuisine
# #         self.affichage.draw_menu_cuisine(self)

# #     def continue_menu_cuisine(self,touche):
# #         if touche == pygame.K_UP :
# #             if self.element_courant == 0:
# #                 self.element_courant = len(self.objet_interactif.recettes)
# #             self.element_courant -= 1
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant += 1
# #             if self.element_courant == len(self.objet_interactif.recettes):
# #                 self.element_courant = 0
# #         elif touche == pygame.K_SPACE :
# #             if self.cible!=None and self.cible == self.element_courant:
# #                 self.cible = None
# #             else:
# #                 self.cible = self.element_courant
# #         elif touche == pygame.K_RETURN :
# #             if self.cible == None:
# #                 # Maybe have an exit option instead ?
# #                 self.controleur.unset_phase(COMPLEMENT_CUISINE)
# #                 self.methode_courante = None
# #                 # Et informer que la cuisine n'a pas été faite
# #             else:
# #                 recette = self.objet_interactif.recettes[self.cible]
# #                 if not (False in [(self.inventaire.quantite(eval(ingredient))>=recette["ingredients"][ingredient])for ingredient in recette["ingredients"].keys()]):
# #                     for ingredient in recette["ingredients"].keys():
# #                         for i in range(recette["ingredients"][ingredient]):
# #                             self.inventaire.consomme(eval(ingredient))
# #                     produit = eval(recette["produit"])(None)
# #                     self.controleur.ajoute_entitee(produit)
# #                     self.inventaire.ajoute(produit)
# #                 self.controleur.unset_phase(COMPLEMENT_CUISINE)
# #                 self.methode_courante = None
# #         self.affichage.draw_menu_cuisine(self)

# #     def start_menu_alchimie(self):
# #         self.event = COMPLEMENT_DIALOGUE
# #         self.element_courant = 0
# #         self.cible = None
# #         self.methode_courante = self.continue_menu_alchimie
# #         self.affichage.draw_menu_alchimie(self)

# #     def continue_menu_alchimie(self,touche):
# #         if touche == pygame.K_UP :
# #             if self.element_courant == 0:
# #                 self.element_courant = len(trouve_skill(self.interlocuteur.classe_principale,Skill_alchimie).recettes)
# #             self.element_courant -= 1
# #         elif touche == pygame.K_DOWN :
# #             self.element_courant += 1
# #             if self.element_courant == len(trouve_skill(self.interlocuteur.classe_principale,Skill_alchimie).recettes):
# #                 self.element_courant = 0
# #         elif touche == pygame.K_SPACE :
# #             if self.cible!=None and self.cible == self.element_courant:
# #                 self.cible = None
# #             else:
# #                 self.cible = self.element_courant
# #         elif touche == pygame.K_RETURN :
# #             if self.cible == None:
# #                 # Peut-être plutôt avoir une option de sortie ?
# #                 self.interlocuteur.replique = "dialogue-1phrase1.3.1"
# #                 self.interlocuteur.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
# #                 if self.a_parchemin_vierge():
# #                     self.interlocuteur.repliques.append("dialogue-1reponse1.3")
# #                 self.interlocuteur.repliques += ["dialogue-1reponse1.4","dialogue-1reponse1.5"]
# #                 self.event = DIALOGUE
# #                 self.methode_courante = None
# #             else:
# #                 alchimie = trouve_skill(self.interlocuteur.classe_principale,Skill_alchimie)
# #                 recette = alchimie.recettes[self.cible]
# #                 if not (False in [(self.inventaire.quantite(eval(ingredient))>=recette["ingredients"][ingredient])for ingredient in recette["ingredients"].keys()]):
# #                     for ingredient in recette["ingredients"].keys():
# #                         for i in range(recette["ingredients"][ingredient]):
# #                             self.inventaire.consomme(eval(ingredient))
# #                     produit = eval(recette["produit"])(None)
# #                     self.controleur.ajoute_entitee(produit)
# #                     self.inventaire.ajoute(produit)
# #                     alchimie.utilise(recette["xp"])
# #                 self.event = DIALOGUE
# #                 self.methode_courante = None
# #                 if self.cible == "Parchemin_vierge":
# #                     self.interlocuteur.replique = "dialogue-1phrase1.4"
# #                     self.interlocuteur.repliques = ["dialogue-1reponse1.4.1"]
# #                 else:
# #                     self.interlocuteur.replique = "dialogue-1phrase1.3.1"
# #                     self.interlocuteur.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"]
# #                     if self.a_parchemin_vierge():
# #                         self.interlocuteur.repliques.append("dialogue-1reponse1.3")
# #                     self.interlocuteur.repliques += ["dialogue-1reponse1.4","dialogue-1reponse1.5"]
# #         self.affichage.draw_menu_alchimie(self)

# #     def start_change_touches(self,etage = -1,element_courant = 0): #On commence le changement de touches
# #         self.controleur.set_phase(TOUCHE)
# #         self.etage = etage #Pour pouvoir commencer directement sur le skill ou la magie qu'on vient d'acquérir
# #         self.element_courant = element_courant
# #         self.suspens = False
# #         zones,skills,magies,lancer = self.get_touches_courantes()
# #         self.affichage.choix_touche(self,zones,skills,magies,lancer)

# #     def continue_change_touche(self,touche,modificateurs=()):
# #         zones,skills,magies,lancer = self.get_touches_courantes()
# #         touches = self.touches[modificateurs]
# #         self.controleur.unset_phase(TOUCHE)
# #         self.affichage.message("Désolé, pas de modification des touches pour l'instant.")
# #         return
# #         if self.suspens:
# #             if touche == pygame.K_RETURN : # On ne souhaite pas attribuer de nouvelle touche
# #                 self.suspens = False
# #             elif True:# touche in touches["direction"].keys() : # La touche est déjà attribuée !
# #                 self.affichage.message("Cette touche est déjà utilisée ! (Ou pas. Mais pour l'instant, pas de modification des touches, désolé.)")
# #             else :
# #                 if self.etage == 0 :
# #                     self.cat_touches[touche] = "zone"
# #                     self.dir_touches[touche] = zones[self.element_courant]
# #                 elif self.etage == 1 :
# #                     self.cat_touches[touche] = "skill"
# #                     self.skill_touches[touche] = type(skills[self.element_courant])
# #                 elif self.etage == 2 :
# #                     self.cat_touches[touche] = "skill"
# #                     self.skill_touches[touche] = Skill_magie
# #                     self.magies[touche] = magies[self.element_courant].nom
# #                 elif self.etage == 3 :
# #                     self.cat_touches[touche] = "skill"
# #                     self.skill_touches[touche] = Skill_lancer
# #                     self.projectiles[touche] = lancer[self.element_courant]
# #                 self.affichage.message("La nouvelle touche a bien été définie.")
# #                 self.suspens = False
# #         elif touche == pygame.K_UP and self.etage != -1 :
# #             self.element_courant = self.etage
# #             self.etage = -1
# #         elif touche == pygame.K_DOWN and self.etage == -1 :
# #             if self.element_courant != 4:
# #                 self.etage = self.element_courant
# #                 self.element_courant = 0
# #         elif touche == pygame.K_RIGHT :
# #             self.element_courant += 1
# #             if self.etage == -1 and self.element_courant > 4 :
# #                 self.element_courant = 0
# #             elif self.etage == 0 and self.element_courant > len(zones) :
# #                 self.element_courant = 0
# #             elif self.etage == 1 and self.element_courant > len(skills) :
# #                 self.element_courant = 0
# #             elif self.etage == 2 and self.element_courant > len(magies) :
# #                 self.element_courant = 0
# #             elif self.etage == 3 and self.element_courant > len(lancer) :
# #                 self.element_courant = 0
# #         elif touche == pygame.K_LEFT :
# #             self.element_courant -= 1
# #             if self.etage == -1 and self.element_courant < 0 :
# #                 self.element_courant = 4
# #             elif self.etage == 0 and self.element_courant < 0 :
# #                 self.element_courant = len(zones)
# #             elif self.etage == 1 and self.element_courant < 0 :
# #                 self.element_courant = len(skills)
# #             elif self.etage == 2 and self.element_courant < 0 :
# #                 self.element_courant = len(magies)
# #             elif self.etage == 3 and self.element_courant < 0 :
# #                 self.element_courant = len(lancer)
# #         elif touche == pygame.K_RETURN :
# #             if (self.etage == -1 and self.element_courant == 4) or (self.etage == 0 and self.element_courant == len(zones)) or (self.etage == 1 and self.element_courant == len(skills)) or (self.etage == 2 and self.element_courant == len(magies)) or (self.etage == 3 and self.element_courant == len(lancer)):
# #                 if self.check_touches():
# #                     self.controleur.unset_phase(TOUCHE)
# #             else :
# #                 if self.etage != -1 and (self.etage != 1 or not isinstance(skills[self.element_courant],(Skill_magie,Skill_lancer))):
# #                     self.suspens = True
# #                 if self.etage == 0 :
# #                     touche = None
# #                     for key in self.dir_touches.keys():
# #                         if self.dir_touches[key] == zones[self.element_courant] and self.cat_touches[key] == "zone":
# #                             touche = key
# #                     if touche !=  None:
# #                         self.cat_touches.pop(touche)
# #                         self.dir_touches.pop(touche)
# #                 elif self.etage == 1 :
# #                     touche = None
# #                     for key in self.skill_touches.keys():
# #                         if self.skill_touches[key] == type(skills[self.element_courant]):
# #                             touche = key
# #                     if touche !=  None:
# #                         self.cat_touches.pop(touche)
# #                         self.skill_touches.pop(touche)
# #                 elif self.etage == 2 :
# #                     touche = None
# #                     for key in self.magies.keys():
# #                         if self.magies[key] == magies[self.element_courant].nom:
# #                             touche = key
# #                     if touche !=  None:
# #                         self.cat_touches.pop(touche)
# #                         self.skill_touches.pop(touche)
# #                         self.magies.pop(touche)
# #                 elif self.etage == 3 :
# #                     touche = None
# #                     for key in self.projectiles.keys():
# #                         if self.projectiles[key] == lancer[self.element_courant]:
# #                             touche = key
# #                     if touche !=  None:
# #                         self.cat_touches.pop(touche)
# #                         self.skill_touches.pop(touche)
# #                         self.projectiles.pop(touche)
# #         self.affichage.choix_touche(self,zones,skills,magies,lancer)

# #     def check_touches(self):
# #         # On vérifie que les touches indispensables sont bien pourvues
# #         ok = True
# #         if len(self.dir_touches) != 10 : #Il faut impérativement pourvoir les 6 touches de zones et les touches directionnelles
# #             ok = False
# #             self.affichage.message("Les touches directionnelles et les touches de zones sont indispensables !")
# #         if not Skill_deplacement in self.skill_touches.values():
# #             self.affichage.message("Vous n'avez pas de touche pour le déplacement...")
# #         if not Skill_ramasse in self.skill_touches.values():
# #             self.affichage.message("Vous n'avez pas de touche pour ramasser les items...")
# #         return ok

# #     def get_touches_courantes(self):
# #         #Renvoie les éléments susceptibles d'avoir une touche attitrée
# #         zones = [0,1,2,3,4,5]
# #         skills = self.classe_principale.get_skills_actifs()
# #         magies = []
# #         lancer = [] #Pour lancer l'item courant, plutôt qu'un item créé
# #         magie = trouve_skill(self.classe_principale,Skill_magie)
# #         if magie != None:
# #             for mag in magie.magies.values():
# #                 magies.append(mag(magie.niveau))
# #         Lancer = trouve_skill(self.classe_principale,Skill_lancer)
# #         if Lancer != None:
# #             lancer = [None]
# #             fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
# #             if fleche != None:
# #                 for fle in fleche.fleches:
# #                     lancer.append(fle)
# #             explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
# #             if explosif != None:
# #                 for expl in explosif.explosifs:
# #                     lancer.append(expl)
# #         return zones,skills,magies,lancer

# #     def change_zone(self,direction):
# #         # On change de zone : HAUT pour remonter à la zone supérieure, BAS pour descendre dans les détails de la zone courante, GAUCHE et DROITE pour passer aux zones voisines
# #         if self.curseur == "carré" :
# #             if direction == DROITE:
# #                 self.curseur = "rectangle_d"
# #             elif direction == GAUCHE:
# #                 self.curseur = "rectangle_g"
# #             elif direction == IN:
# #                 self.curseur = "liste_d"
# #         elif self.curseur == "rectangle_d":
# #             if direction == DROITE:
# #                 self.curseur = "rectangle_g"
# #             elif direction == GAUCHE:
# #                 self.curseur = "carré"
# #             elif direction == IN:
# #                 self.curseur = "in_esprit"
# #         elif self.curseur == "rectangle_g":
# #             if direction == DROITE:
# #                 self.curseur = "carré"
# #             elif direction == GAUCHE:
# #                 self.curseur = "rectangle_d"
# #             elif direction == IN:
# #                 self.curseur = "inventaire"
# #         elif self.curseur == "stats":
# #             if direction == BAS:
# #                 self.curseur = "inventaire"
# #             elif direction == HAUT:
# #                 self.curseur = "classe"
# #             elif direction == IN:
# #                 self.curseur = "in_stats"
# #             elif direction == OUT:
# #                 self.curseur = "rectangle_g"
# #         elif self.curseur == "inventaire":
# #             if direction == BAS:
# #                 self.curseur = "classe"
# #             elif direction == HAUT:
# #                 self.curseur = "stats"
# #             elif direction == IN:
# #                 self.curseur = "in_inventaire"
# #             elif direction == OUT:
# #                 self.curseur = "rectangle_g"
# #         elif self.curseur == "classe":
# #             if direction == BAS:
# #                 self.curseur = "stats"
# #             elif direction == HAUT:
# #                 self.curseur = "inventaire"
# #             elif direction == IN:
# #                 self.curseur = "in_classe"
# #             elif direction == OUT:
# #                 self.curseur = "rectangle_g"
# #         elif self.curseur == "liste_d":
# #             if direction == DROITE:
# #                 self.curseur = "cases"
# #             elif direction == GAUCHE:
# #                 self.curseur = "cases"
# #             elif direction == IN:
# #                 self.curseur = "in_liste"
# #             elif direction == OUT:
# #                 self.curseur = "carré"
# #         elif self.curseur == "cases":
# #             if direction == DROITE:
# #                 self.curseur = "liste_d"
# #             elif direction == GAUCHE:
# #                 self.curseur = "liste_d"
# #             elif direction == IN:
# #                 self.curseur = "in_cases"
# #             elif direction == OUT:
# #                 self.curseur = "carré"
# #         elif self.curseur == "messages":
# #             if direction == IN:
# #                 self.curseur = "in_messages"
# #             elif direction == OUT:
# #                 self.curseur = "rectangle_d"
# #         elif self.curseur == "in_stats":
# #             if self.affichage.deplace_stats(direction):
# #                 self.curseur = "stats"
# #         elif self.curseur == "in_inventaire":
# #             if self.inventaire.deplace(direction):
# #                 self.curseur = "inventaire"
# #         elif self.curseur == "in_classe":
# #             if self.classe_principale.deplace(direction):
# #                 self.curseur = "classe"
# #         elif self.curseur == "in_esprit":
# #             if self.controleur.get_esprit(self.esprit).deplace(direction):
# #                 self.curseur = "rectangle_d"
# # ##        elif self.curseur == "in_liste":
# # ##            if self.affichage.deplace_liste(direction):
# # ##                self.curseur = "liste_d"
# # ##        elif self.curseur == "in_cases":
# # ##            if self.affichage.deplace_cases(direction):
# # ##                self.curseur = "cases"
# # ##        elif self.curseur == "in_messages":
# # ##            if self.affichage.deplace_messages(direction):
# # ##                self.curseur = "messages"

# #     def level_up(self):
# #         """La fonction qui augmente le niveau du joueur. Augmente les stats, et offre un cadeau d'évolution au choix."""
# #         #Insérer toute l'augmentation des stats ici
# #         self.trouve_choix_possibles() #On actualise les choix possibles de l'arbre classique
# #         self.trouve_choix_elems() #On actualise les choix possibles de l'arbre élémentaire
# #         self.arbre = CLASSIQUE
# #         self.element_courant = 0
# #         self.courant = 0
# #         self.etage = 0
# #         self.event = LEVELUP
# #         self.controleur.set_phase(EVENEMENT)

# #     def evenement(self):
# #         """La fonction qui est appelée à chaque tour au cours d'un événement"""
# #         if self.event == LEVELUP:
# #             self.affichage.choix_niveau(self)
# #         elif self.event == DIALOGUE:
# #             self.affichage.dialogue(self)
# #         elif self.event == COMPLEMENT_DIALOGUE:
# #             if self.methode_courante == self.continue_select_cible_dialogue:
# #                 self.affichage.redraw_magie_cible(self,0)
# #             elif self.methode_courante == self.continue_select_case_dialogue:
# #                 self.affichage.redraw_magie_case(self,0)

#     def trouve_choix_possibles(self):
#         """La fonction qui détermine les options disponibles au choix."""
#         niveau = self.niveau+1
#         if niveau == 1:
#             self.choix_dispos = [REGEN_HP,REGEN_MP]

#         elif niveau == 2:
#             if self.choix_niveaux[CLASSIQUE][1] == MAGIE:
#                 self.choix_dispos = [ESSENCE_MAGIQUE,MAGIE_INFINIE]
#             else:
#                 self.choix_dispos = [DEFENSE,LANCER]

#         elif niveau == 3:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_PRIORITE,BOOST_PV,BOOST_DE_PRIORITE_D_ATTAQUE]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [CREATION_FLECHES,BOOST_PV,SORT_ACCELERATION]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [BOOST_AURA,BOOST_PM,ONDE_DE_CHOC]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [SORT_DE_SOIN_SUPERIEUR,ENCHANTEMENT_FORCE,PROJECTION_ENERGIE]

#         elif niveau == 4:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [ECRASEMENT,OBSERVATION,MANIPULATION_EPEE]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [BOOST_PORTEE,SORT_VISION,CREATION_EXPLOSIF]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [ELEMENTALISTE,RAYON_THERMIQUE,REGEN_MP]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [RAYON_THERMIQUE,ENCHANTEMENT_DEFENSE,REGEN_PM]

#         elif niveau == 5:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_PRIORITE,ANALYSE,VOL,BOOST_ATTAQUE_EPEE]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [FLECHE_PERCANTE,OBSERVATION,FLECHE_EXPLOSIVE]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [IMMORTALITE,BOOST_DEGATS_MAGIQUES,BOOST_PRIORITE_MAGIQUE]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [ENCHANTEMENT_FAIBLESSE,EPEISTE,BOOST_RESTAURATIONS]

#         elif niveau == 6:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [MANIPULATION_BOUCLIER,BOOST_PRIORITE_OBSERVATION,SORT_AUTO_SOIN]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [BOOST_DEGATS_FLECHES,CHARGE_LOURDE,CHARGE_ETENDUE]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [INHUMANITE,MAGICIEN,BOOST_DE_PORTEE]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_ATTAQUE_EPEE,BOOST_SOIN,ONDE_DE_CHOC]

#         elif niveau == 7:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [SORT_DE_VUE,VOL_PRIORITE,BOOST_ATTAQUE_LANCE]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [BOOST_PRIORITE_FLECHES,FLECHE_EXPLOSIVE,ARTIFICIER]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [FANTOME,INSTAKILL,JET_DE_MANA]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [ENCHANTEMENT_RENFORCEMENT,SORT_DE_PROTECTION,BOOST_PM]

#         elif niveau == 8:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_ATTAQUE,DEFENSE,BOOST_PRIORITE]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [ARCHER,FLECHE_FANTOME,BOOST_DEGAT,CHARGE_ETENDUE]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [NECROMANCIEN,BOOST_AURA,BOOST_PRIORITE]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [ENCHANTEMENT_DEFENSIF,ENCHANTEUR,SOUTIEN]

#         elif niveau == 9:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_PRIORITE_DEPLACEMENT,BOOST_PRIORITE_ANALYSE,BOOST_PV]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [FLECHE_FANTOME,BOOST_PRIORITE_EXPLOSIF,BOOST_VITESSE_EXPLOSIF]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [BOOST_PRIORITE_AURA,AURA_MORTELLE,ASSASSIN]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_DE_ZONE_DE_RESTAURATION,ANGE,ENCHANTEMENT_ROUILLE]

#         elif niveau == 10:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 self.choix_dispos = [MANIPULATION_ARME,BOOST_PV,DEFENSE]
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 self.choix_dispos = [FLECHES_LOURDE_LEGERE,BOOST_PRIORITE,BOOST_PORTEE_EXPLOSIFS]
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 self.choix_dispos = [ECLAIR_NOIR,BOOST_DEGATS_PROJECTILES,BOOST_PM]
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 self.choix_dispos = [BOOST_ENCHANTEMENT,RESURECTION,ECLAIR_NOIR]

#     def trouve_choix_elems(self):
#         """La fonction qui détermine les options disponibles au choix."""
#         #On vérifie si on a une contrainte élémentaire (incompatibilité entre l'ombre et les autres éléments) :
#         if self.choix_niveaux[ELEMENTAL][OMBRE][elemental] :
#             self.choix_elems = []
#             #On bloque tout (les autres éléments sont incompatibles, et on a atteint le summum de l'ombre)
#         elif self.choix_niveaux[ELEMENTAL][OMBRE][affinite] and self.choix_niveaux[ELEMENTAL][OMBRE][aura] and self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] :
#             self.choix_elems = [elemental_ombre]
#         elif self.choix_niveaux[ELEMENTAL][OMBRE][affinite] and self.choix_niveaux[ELEMENTAL][OMBRE][aura] :
#             #On n'a donc pas la magie d'ombre
#             self.choix_elems = [magie_ombre]
#         elif self.choix_niveaux[ELEMENTAL][OMBRE][aura] and self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] :
#             #On n'a donc pas l'affinité
#             self.choix_elems = [affinite_ombre]
#         elif self.choix_niveaux[ELEMENTAL][OMBRE][affinite] or self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] :
#             #On n'a donc pas l'aura
#             self.choix_elems = [aura_ombre]
#         #Si aucun des choix précédents n'est le bon, on n'a pas d'ombre
#         elif self.choix_niveaux[ELEMENTAL][TERRE][elemental] and self.choix_niveaux[ELEMENTAL][FEU][elemental] and self.choix_niveaux[ELEMENTAL][GLACE][elemental]:
#             self.choix_elems = []
#             #On bloque tout (l'ombre est incompatible, et on a atteint le summum de la terre, du feu et de la glace)
#         elif self.choix_niveaux[ELEMENTAL][TERRE][affinite] and self.choix_niveaux[ELEMENTAL][TERRE][aura] and self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] :
#             self.choix_elems = [elemental_terre]
#             #L'affinité à la terre bloque les autres éléments
#         elif self.choix_niveaux[ELEMENTAL][FEU][affinite] and self.choix_niveaux[ELEMENTAL][FEU][aura] and self.choix_niveaux[ELEMENTAL][FEU][MAGIE] :
#             self.choix_elems = [elemental_feu]
#             #L'affinité à la feu bloque les autres éléments
#         elif self.choix_niveaux[ELEMENTAL][GLACE][affinite] and self.choix_niveaux[ELEMENTAL][GLACE][aura] and self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] :
#             self.choix_elems = [elemental_glace]
#             #L'affinité à la glace bloque les autres éléments
#         elif self.choix_niveaux[ELEMENTAL][TERRE][affinite] and self.choix_niveaux[ELEMENTAL][TERRE][aura] :
#             self.choix_elems = [magie_terre]
#             #L'affinité à la terre bloque les autres éléments et il manque la magie
#         elif self.choix_niveaux[ELEMENTAL][FEU][affinite] and self.choix_niveaux[ELEMENTAL][FEU][aura] :
#             self.choix_elems = [magie_feu]
#             #L'affinité à la feu bloque les autres éléments et il manque la magie
#         elif self.choix_niveaux[ELEMENTAL][GLACE][affinite] and self.choix_niveaux[ELEMENTAL][GLACE][aura] :
#             self.choix_elems = [magie_glace]
#             #L'affinité à la glace bloque les autres éléments et il manque la magie
#         elif self.choix_niveaux[ELEMENTAL][TERRE][affinite] :
#             self.choix_elems = [aura_terre]
#             #L'affinité à la terre bloque les autres éléments et il manque l'aura
#         elif self.choix_niveaux[ELEMENTAL][FEU][affinite] :
#             self.choix_elems = [aura_feu]
#             #L'affinité à la feu bloque les autres éléments et il manque l'aura
#         elif self.choix_niveaux[ELEMENTAL][GLACE][affinite] :
#             self.choix_elems = [aura_glace]
#             #L'affinité à la glace bloque les autres éléments et il manque l'aura
#         #Si aucun des choix précédents, on n'a pas d'affinité, donc pas d'incompatibilité (à part avec l'ombre éventuellement)
#         elif self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] or self.choix_niveaux[ELEMENTAL][FEU][MAGIE] or self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] or self.choix_niveaux[ELEMENTAL][TERRE][elemental] or self.choix_niveaux[ELEMENTAL][FEU][elemental] or self.choix_niveaux[ELEMENTAL][GLACE][elemental]:
#             #L'ombre est indisponible
#             self.choix_elems = []
#             #On parcours les éléments un par un
#             if self.choix_niveaux[ELEMENTAL][TERRE][elemental] :
#                 pass
#                 #On a atteint le summum de la terre, pas d'autre choix ici
#             elif self.choix_niveaux[ELEMENTAL][TERRE][aura] :
#                 #On n'a pas l'affinité (évidemment)
#                 self.choix_elems.append(affinite_terre)
#             elif self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] :
#                 #On n'a pas l'aura non plus
#                 self.choix_elems.append(aura_terre)
#             else :
#                 #On n'a ni l'affinité, ni la magie
#                 self.choix_elems.append(affinite_terre)
#                 self.choix_elems.append(magie_terre)
#             if self.choix_niveaux[ELEMENTAL][FEU][elemental] :
#                 pass
#                 #On a atteint le summum du feu, pas d'autre choix ici
#             elif self.choix_niveaux[ELEMENTAL][FEU][aura] :
#                 #On n'a pas l'affinité (évidemment)
#                 self.choix_elems.append(affinite_feu)
#             elif self.choix_niveaux[ELEMENTAL][FEU][MAGIE] :
#                 #On n'a pas l'aura non plus
#                 self.choix_elems.append(aura_feu)
#             else :
#                 #On n'a ni l'affinité, ni la magie
#                 self.choix_elems.append(affinite_feu)
#                 self.choix_elems.append(magie_feu)
#             if self.choix_niveaux[ELEMENTAL][GLACE][elemental] :
#                 pass
#                 #On a atteint le summum de la glace, pas d'autre choix ici
#             elif self.choix_niveaux[ELEMENTAL][GLACE][aura] :
#                 #On n'a pas l'affinité (évidemment)
#                 self.choix_elems.append(affinite_glace)
#             elif self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] :
#                 #On n'a pas l'aura non plus
#                 self.choix_elems.append(aura_glace)
#             else :
#                 #On n'a ni l'affinité, ni la magie
#                 self.choix_elems.append(affinite_glace)
#                 self.choix_elems.append(magie_glace)
#         else :
#             #On n'a encore fait aucun choix, donc tous les éléments sont ouverts
#             self.choix_elems = [affinite_terre,magie_terre,affinite_feu,magie_feu,affinite_glace,magie_glace,affinite_ombre,magie_ombre]
#         #On cherchera à raccourcir tout ça une autre fois (si si, j'y penserai !)

#     def choisi_cadeau(self,touche):
#         if touche == pygame.K_UP :
#             if self.arbre and self.etage == 0:
#                 self.etage = 1
#             elif not(self.arbre) and self.etage == 0:
#                 if len(self.choix_elems) != 0: #Attention au cas où on n'a plus de choix élémentaux valides
#                     self.etage = 1
#         elif touche == pygame.K_DOWN :
#             if self.etage == 1:
#                 self.etage = 0
#         elif touche == pygame.K_RIGHT :
#             if self.etage == 0:
#                 self.arbre = not(self.arbre)
#             elif self.etage == 1:
#                 if self.arbre :
#                     self.courant += 1
#                     if self.courant == len(self.choix_dispos):
#                         self.courant = 0
#                 else :
#                     self.element_courant += 1
#                     if self.element_courant == len(self.choix_elems):
#                         self.element_courant = 0
#         elif touche == pygame.K_LEFT :
#             if self.etage == 0:
#                 self.arbre = not(self.arbre)
#             elif self.etage == 1:
#                 if self.arbre :
#                     if self.courant == 0:
#                         self.courant = len(self.choix_dispos)
#                     self.courant -= 1
#                 else :
#                     if self.element_courant == 0:
#                         self.element_courant = len(self.choix_elems)
#                     self.element_courant -= 1
#         elif touche == pygame.K_SPACE :
#             if self.etage == 1:
#                 if self.arbre :
#                     choix = self.choix_dispos[self.courant]
#                 else :
#                     choix = self.choix_elems[self.element_courant]
#                 self.controleur.unset_phase(EVENEMENT)
#                 self.prend_cadeau(choix)

#     def prend_cadeau(self,choix):
#         """Fonction qui prend le cadeau choisi"""
#         niveau = self.niveau + 1
#         if niveau == 1:
#             if choix == REGEN_HP:
#                 self.regen_pv += 1 #La quantité ajouté devrait être une constante, du fichier du même nom
#                 self.choix_niveaux[CLASSIQUE][1] = PHYSIQUE
#             elif choix == REGEN_MP:
#                 self.regen_pm += 1 #Même remarque ici
#                 self.choix_niveaux[CLASSIQUE][1] = MAGIE
#             else:
#                 self.choix_niveaux[CLASSIQUE][1] = PHYSIQUE_PAR_DEFAUT

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 2:
#             if choix == DEFENSE:
#                 skill = Skill_defense() #On crée un skill à donner au joueur
#                 skill.evo() #Au niveau 1, le skill, c'est mieux
#                 self.classe_principale.skills.append(skill)
#                 self.choix_niveaux[CLASSIQUE][2] = DEFENSE
#             elif choix == LANCER:
#                 skill = Skill_lancer() #On crée un skill à donner au joueur
#                 skill.evo() #Au niveau 1, le skill, c'est mieux
#                 self.classe_principale.skills.append(skill)
#                 self.choix_niveaux[CLASSIQUE][2] = LANCER
#             elif choix == ESSENCE_MAGIQUE:
#                 skill = Skill_essence_magique() #On crée un skill à donner au joueur
#                 skill.evo() #Au niveau 1, le skill, c'est mieux
#                 self.classe_principale.skills.append(skill)
#                 self.choix_niveaux[CLASSIQUE][2] = ESSENCE_MAGIQUE
#             elif choix == MAGIE_INFINIE:
#                 skill = Skill_magie_infinie() #On crée un skill à donner au joueur
#                 skill.evo() #Au niveau 1, le skill, c'est mieux
#                 self.classe_principale.skills.append(skill)
#                 self.choix_niveaux[CLASSIQUE][2] = MAGIE_INFINIE
#             elif self.choix_niveaux[CLASSIQUE][1] == MAGIE:
#                 self.choix_niveaux[CLASSIQUE][2] = MAGIE_INFINIE_PAR_DEFAUT
#             else:
#                 self.choix_niveaux[CLASSIQUE][2] = DEFENSE_PAR_DEFAUT

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 3:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == BOOST_PRIORITE:
#                     self.priorite += 1 #Hum, est-ce que c'est assez ? Trop ? En faire une constante pour pouvoir la modifier plus facilement
#                     self.choix_niveaux[CLASSIQUE][3] = BOOST_PRIORITE
#                 elif choix == BOOST_PV:
#                     self.pv_max += 100 #Même questions et remarque que plus haut
#                     self.choix_niveaux[CLASSIQUE][3] = BOOST_PV
#                 elif choix == BOOST_DE_PRIORITE_D_ATTAQUE:
#                     self.force += 10 #Je sais, ce n'est pas la priorité d'attaque. Mais c'est bien aussi, non ? Je ne suis même pas sûr que la priorité joue un rôle dans les attaques, de toute façon...
#                     self.choix_niveaux[CLASSIQUE][3] = BOOST_DE_PRIORITE_D_ATTAQUE
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == CREATION_FLECHES:
#                     skill = Skill_creation_de_fleches([Cree_fleche_de_base_skill()]) #On crée un skill à donner au joueur
#                     skill.evo() #Au niveau 1, le skill, c'est mieux
#                     self.classe_principale.skills.append(skill) #Ce skill ne peut pas vraiment être utilisé pour l'instant...
#                     self.choix_niveaux[CLASSIQUE][3] = CREATION_FLECHES
#                 elif choix == BOOST_PV:
#                     self.pv_max += 100 #Même questions et remarque que plus haut (plus plus haut que ça)
#                     self.choix_niveaux[CLASSIQUE][3] = BOOST_PV
#                 elif choix == SORT_ACCELERATION:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_acceleration) #Il faudra créer ce sort, sous peine de devoir commenter cette ligne
#                     self.choix_niveaux[CLASSIQUE][3] = SORT_ACCELERATION
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == BOOST_AURA:
#                     skill = Skill_boost_aura() #Je crois que ce skill est encore à inventer
#                     skill.evo() #Au niveau 1, le skill, c'est mieux
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][3] = BOOST_AURA #Fun fact : le joueur qui choisi ce skill ne peut pas avoir d'aura à booster à ce stade. Le skill n'est donc pas utilisé et n'aide pas à monter de niveau, mais c'est un investissement payant si le joueur survit (et s'oriente vers les auras...)
#                 elif choix == BOOST_PM:
#                     self.pm_max += 100 #Même questions et remarque que plus haut (encore plus haut que ça)
#                     self.choix_niveaux[CLASSIQUE][3] = BOOST_PM
#                 elif choix == ONDE_DE_CHOC:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_onde_de_choc) #Il faudra créer ce sort, sous peine de devoir commenter cette ligne
#                     self.choix_niveaux[CLASSIQUE][3] = ONDE_DE_CHOC
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == SORT_DE_SOIN_SUPERIEUR:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_soin_superieur) #Parce que le joueur a déjà un sort de soin ? Dès le début, obtenu en récompense d'un niveau précédent ?
#                     self.choix_niveaux[CLASSIQUE][3] = SORT_DE_SOIN_SUPERIEUR
#                 elif choix == ENCHANTEMENT_FORCE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_force) #Vérifier le nom exact de la magie ("Enchantement_de_force" potentiellement)
#                     self.choix_niveaux[CLASSIQUE][3] = ENCHANTEMENT_FORCE
#                 elif choix == PROJECTION_ENERGIE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_jet_de_mana) #Il me semble que c'est bien la même chose
#                     self.choix_niveaux[CLASSIQUE][3] = PROJECTION_ENERGIE

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 4:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == ECRASEMENT:
#                     skill = Skill_ecrasement() #Un mur ? Où ça ? Un mob ? Où ça ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][4] = ECRASEMENT
#                 elif choix == OBSERVATION:
#                     skill = Skill_observation() # Un prérequis de l'analyse et du vol. Permet de savoir ce qui ne nous regarde pas.
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][4] = OBSERVATION
#                 elif choix == MANIPULATION_EPEE:
#                     skill = Skill_manipulation_epee() # Augmente l'efficacité des attaque à l'épée. Dans un jeu idéal, fournirait aussi de nouveaux mouvements...
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][4] = MANIPULATION_EPEE
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == BOOST_PORTEE:
#                     lancer = trouve_skill(self.classe_principale,Skill_lancer)
#                     lancer.boost_portee()
#                     self.choix_niveaux[CLASSIQUE][4] = BOOST_PORTEE
#                 elif choix == SORT_VISION:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_vision) #Peut-être proposer un autre sort, moins consommateur de PM, qui se place automatiquement sur le lanceur ?
#                     self.choix_niveaux[CLASSIQUE][4] = SORT_VISION #Autre idée : un skill ou un sort qui permet d'afficher la vue de l'esprit, et pas celle du joueur. Pour avoir une meilleure compréhension des champs de bataille.
#                 elif choix == CREATION_EXPLOSIF:
#                     skill = Skill_creation_d_explosifs([Cree_charge_de_base_skill()])
#                     skill.evo() #Au niveau 1, le skill, c'est mieux
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][4] = CREATION_EXPLOSIF
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == ELEMENTALISTE:
#                     classe = Elementaliste() # Où comment rendre l'arbre des éléments cheaté
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][4] = ELEMENTALISTE
#                 elif choix == RAYON_THERMIQUE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_laser)
#                     self.choix_niveaux[CLASSIQUE][4] = RAYON_THERMIQUE
#                 elif choix == REGEN_MP:
#                     self.regen_pm += 1
#                     self.choix_niveaux[CLASSIQUE][4] = REGEN_MP
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == RAYON_THERMIQUE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_laser) #C'est bien les mêmes ?
#                     self.choix_niveaux[CLASSIQUE][4] = RAYON_THERMIQUE
#                 elif choix == ENCHANTEMENT_DEFENSE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_defense) #À créer, je crois...
#                     self.choix_niveaux[CLASSIQUE][4] = ENCHANTEMENT_DEFENSE
#                 elif choix == REGEN_PM:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_regeneration_pm) #Un transfert de pm à quelqu'un d'autre, grosso-modo. À créer, je pense.
#                     self.choix_niveaux[CLASSIQUE][4] = REGEN_PM

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 5:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == BOOST_PRIORITE:
#                     self.priorite += 1 #Hum, est-ce que c'est assez ? Trop ? En faire une constante pour pouvoir la modifier plus facilement
#                     self.choix_niveaux[CLASSIQUE][5] = BOOST_PRIORITE
#                 elif choix == ANALYSE:
#                     skill = Skill_analyse() #Peut analyser les termes du système et révéler la vérité sur le monde. Pas beaucoup d'utilité en pratique, mais un joueur débutant peut l'utiliser pour découvrir le fonctionnement du jeu
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = ANALYSE
#                 elif choix == VOL:
#                     skill = Skill_vol() #Pourquoi tuer le monstre, quand on peut récupérer la clé de la porte directement dans sa poche ? Fonctionne aussi sur les humains, et les alliés de façon plus générale (gniark gniark gniark)
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = VOL
#                 elif choix == BOOST_ATTAQUE_EPEE:
#                     skill = Skill_boost_attaque_epee() #À créer
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = BOOST_ATTAQUE_EPEE
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == FLECHE_PERCANTE:
#                     creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches) 
#                     creation_fleche.ajoute(Cree_fleche_percante_skill()) #Une flèche qui traverse même si elle ne tue pas ?
#                     self.choix_niveaux[CLASSIQUE][5] = FLECHE_PERCANTE
#                 elif choix == OBSERVATION:
#                     skill = Skill_observation()
#                     skill.evo() #Au niveau 1, le skill, c'est mieux
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = OBSERVATION
#                 elif choix == FLECHE_EXPLOSIVE:
#                     creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
#                     if creation_fleche !=  None:
#                         creation_fleche.ajoute(Cree_fleche_explosive_skill())
#                     creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
#                     if creation_explosif != None:
#                         creation_explosif.ajoute(Cree_fleche_explosive_skill())
#                     self.choix_niveaux[CLASSIQUE][5] = FLECHE_EXPLOSIVE
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == IMMORTALITE: #Sérieusement.
#                     skill = Skill_immortel() #Non mais vraiment, ça rend immortel.
#                     skill.evo() #Impossible de mourir, quelle que soient les circonstances !
#                     self.classe_principale.skills.append(skill) #Et ce n'est qu'un début !
#                     self.choix_niveaux[CLASSIQUE][5] = IMMORTALITE #Vous verrez.
#                 elif choix == BOOST_DEGATS_MAGIQUES:
#                     skill = Boost_degats_magiques() #Je vois mal comment ça fonctionnera, honnêtement. Il n'est jamais trop tard pour changer d'avis...
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = BOOST_DEGATS_MAGIQUE
#                 elif choix == BOOST_PRIORITE_MAGIQUE:
#                     skill = Boost_priorite_magique() #Et là, je vois à peine mieux.
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = BOOST_PRIORITE_MAGIQUE
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == ENCHANTEMENT_FAIBLESSE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_faiblesse) #Donner toute la panoplie des déboosts d'un coup ?
#                     self.choix_niveaux[CLASSIQUE][5] = ENCHANTEMENT_FAIBLESSE
#                 elif choix == EPEISTE:
#                     classe = Epeiste() #Oui, épéiste mage, et alors ?
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][5] = EPEISTE
#                 elif choix == BOOST_RESTAURATIONS:
#                     skill = Boost_restaurations() #Un skill qui boost les soins et restaurations de PM
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][5] = BOOST_RESTAURATIONS

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 6:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == MANIPULATION_BOUCLIER:
#                     skill = Skill_manipulation_bouclier() #Ce skill augmente l'efficacité des bouclier et ouvre à de nouveaux mouvements, on peut se servir d'un bouclier sans.
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][6] = MANIPULATION_BOUCLIER
#                 elif choix == BOOST_PRIORITE_OBSERVATION:
#                     skill = Skill_boost_priorite_observation()
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][6] = BOOST_PRIORITE_OBSERVATION
#                 elif choix == SORT_AUTO_SOIN:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_auto_soin)
#                     self.choix_niveaux[CLASSIQUE][6] = SORT_AUTO_SOIN
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == BOOST_DEGATS_FLECHES:
#                     skill = Skill_boost_degats_fleches() #Ce skill n'existe pas encore... Est-ce qu'il fonctionne sur les flèches de glace (magie) ?
#                     skill.evo() #Au niveau 1, le skill, c'est mieux
#                     self.classe_principale.skills.append(skill) #Ce skill ne peut pas vraiment être utilisé pour l'instant...
#                     self.choix_niveaux[CLASSIQUE][6] = BOOST_DEGATS_FLECHES
#                 elif choix == CHARGE_LOURDE:
#                     creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
#                     creation_explosif.ajoute(Cree_charge_lourde_skill()) #Beaucoup de dégats, petite zone
#                     self.choix_niveaux[CLASSIQUE][6] = CHARGE_LOURDE
#                 elif choix == CHARGE_ETENDUE:
#                     creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
#                     creation_explosif.ajoute(Cree_charge_etendue_skill()) #Peu de dégats, grande zone
#                     self.choix_niveaux[CLASSIQUE][6] = CHARGE_ETENDUE
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == INHUMANITE:
#                     self.especes.remove('humain') #Ça évite de se faire agresser par la plupart des monstres. Les amis humains risquent de ne pas apprécier, par contre...
#                     self.choix_niveaux[CLASSIQUE][6] = INHUMANITE
#                 elif choix == MAGICIEN:
#                     classe = Magicien() #Un gros boost à tout ce qui est orienté magie.
#                     classe.evo() #Et la classe Magicien peut récupérer le skill Magie
#                     self.classe_principale.sous_classes.append(classe) #On me souffle à l'oreillette que monter la classe Mage au niveau 10 suffit à obtenir Magicien, par contre... À condition que j'implémente Mage
#                     self.choix_niveaux[CLASSIQUE][6] = MAGICIEN
#                 elif choix == BOOST_DE_PORTEE:
#                     skill = Boost_portee() #Portee des magie, évidemment... je suppose ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][6] = BOOST_DE_PORTEE
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == BOOST_ATTAQUE_EPEE:
#                     skill = Boost_epee() # Il ne boost que l'attaque ? À voir...
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][6] = BOOST_ATTAQUE_EPEE
#                 elif choix == BOOST_SOIN:
#                     skill = Boost_soin() # Un boost spécifique aux sorts de soin
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][6] = BOOST_SOIN
#                 elif choix == ONDE_DE_CHOC:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_onde_de_choc)
#                     self.choix_niveaux[CLASSIQUE][6] = ONDE_DE_CHOC

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 7:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == SORT_DE_VUE: #Oh, un sort, il s'est perdu le pauvre ?
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_de_vision) #Mettre un autre sort moins couteux, on n'a pas tant de mana nous !
#                     self.choix_niveaux[CLASSIQUE][7] = SORT_DE_VUE
#                 elif choix == VOL_PRIORITE:
#                     skill = Skill_vol_priorite() #Je ne suis pas convaincu par le fonctionnement de ces capacités de vol...
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][7] = VOL_PRIORITE
#                 elif choix == BOOST_ATTAQUE_LANCE:
#                     skill = Skill_boost_lance()
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][7] = BOOST_ATTAQUE_LANCE
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == BOOST_PRIORITE_FLECHES:
#                     skill = Skill_boost_priorite_fleches() #Quand est-ce que la priorité des flèches intervient ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][7] = BOOST_PRIORITE_FLECHES
#                 elif choix == FLECHE_EXPLOSIVE:
#                     creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
#                     if creation_fleche !=  None:
#                         creation_fleche.ajoute(Cree_fleche_explosive_skill())
#                     creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
#                     if creation_explosif != None:
#                         creation_explosif.ajoute(Cree_fleche_explosive_skill())
#                     self.choix_niveaux[CLASSIQUE][7] = FLECHE_EXPLOSIVE
#                 elif choix == ARTIFICIER:
#                     classe = Artificier()
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][7] = ARTIFICIER
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == FANTOME:
#                     #On rajoute fantome à notre espèce ? À notre pseudo-classe ? C'est une vraie classe ? À voir... Permet de traverser les murs, en tous cas.
#                     self.choix_niveaux[CLASSIQUE][7] = FANTOME
#                 elif choix == INSTAKILL:
#                     skill = Skill_instakill() #Pour tuer sans se salir les mains (si l'instakill réussit, personne n'est au courant... en général)
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][7] = INSTAKILL
#                 elif choix == JET_DE_MANA:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_jet_de_mana)
#                     self.choix_niveaux[CLASSIQUE][7] = JET_DE_MANA
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == ENCHANTEMENT_RENFORCEMENT:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_renforcement) # Pour renforcer les items ! Les épées, à tout hasard...
#                     self.choix_niveaux[CLASSIQUE][7] = ENCHANTEMENT_RENFORCEMENT
#                 elif choix == SORT_DE_PROTECTION:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_protection) # Protège tous les gens autour (enfin, juste les alliés)
#                     self.choix_niveaux[CLASSIQUE][7] = SORT_DE_PROTECTION
#                 elif choix == BOOST_PM:
#                     self.pm_max += 100
#                     self.choix_niveaux[CLASSIQUE][7] = BOOST_PM

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 8:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == BOOST_ATTAQUE:
#                     self.force += 10
#                     self.choix_niveaux[CLASSIQUE][8] = BOOST_ATTAQUE
#                 elif choix == DEFENSE:
#                     skill = Skill_defense() #Pour ceux qui l'ont raté en utilisant l'arbre des éléments
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][8] = DEFENSE
#                 elif choix == BOOST_PRIORITE:
#                     self.priorite += 1 #Très monotone, cet arbre, vous ne trouvez pas ?
#                     self.choix_niveaux[CLASSIQUE][8] = BOOST_PRIORITE
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == ARCHER:
#                     classe = Archer()
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][8] = ARCHER
#                 elif choix == FLECHE_FANTOME:
#                     creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
#                     creation_fleche.ajoute(Cree_fleche_fantome_skill()) #Une fleche qui ignore les murs
#                     self.choix_niveaux[CLASSIQUE][8] = FLECHE_FANTOME
#                 elif choix == BOOST_DEGAT:
#                     self.force += 10 #Les dégats de projectiles ne sont pas affectés par la force, je crois...
#                     self.choix_niveaux[CLASSIQUE][8] = BOOST_DEGAT
#                 elif choix == CHARGE_ETENDUE:
#                     creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
#                     creation_explosif.ajoute(Cree_charge_etendue_skill()) #La deuxième et dernière chance de l'obtenir
#                     self.choix_niveaux[CLASSIQUE][8] = CHARGE_ETENDUE
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == NECROMANCIEN: #Quand je vous disais que l'immortalité n'était qu'un début...
#                     classe = Necromancien() #Le nécromancien est immortel (c'est une condition pour le devenir) et ranime ses ennemis et ses alliés pour qu'ils le servent.
#                     classe.evo() #En général, ça se passe comme ça : *TOC TOC* - Auriez-vous cinq minutes pour parler de notre seigneur Eskom, prince des ténèbres ?
#                     self.classe_principale.sous_classes.append(classe) # - Bien sûr que vous les avez, vous êtes mort... Mais le seigneur Eskom, prince des ténèbres, peut vous accorder une nouvelle vie... à mon service.
#                     self.choix_niveaux[CLASSIQUE][8] = NECROMANCIEN #Bon, nécromancien est incompatible avec plein de trucs, mais il serait trop puissant sinon (il bloque les montées de niveau de la classe principale ?)
#                 elif choix == BOOST_AURA:
#                     skill = Skill_boost_aura() #Là, ça s'adresse plus aux full-ombre/instakill qu'aux futurs-triple-élémentaux
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][8] = BOOST_AURA
#                 elif choix == BOOST_PRIORITE:
#                     self.priorite += 1
#                     self.choix_niveaux[CLASSIQUE][8] = BOOST_PRIORITE
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == ENCHANTEMENT_DEFENSIF:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_defensif) #Confère à un objet des propriétés défensives
#                     self.choix_niveaux[CLASSIQUE][5] = ENCHANTEMENT_DEFENSIF
#                 elif choix == ENCHANTEUR:
#                     classe = Enchanteur() #Pour enchanter encore plus efficacement
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][8] = ENCHANTEUR
#                 elif choix == SOUTIEN:
#                     classe = Soutien() #Pas très fou honnêtement. Mais entre les dix niveaux de croissance à venir et la possibilité de prendre l'ange au prochain niveau, ça commence à se valoir...
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][8] = SOUTIEN

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 9:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == BOOST_PRIORITE_DEPLACEMENT:
#                     skill = Skill_boost_priorite_deplacement() #Pour rendre l'écrasement plus efficace
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_DEPLACEMENT
#                 elif choix == BOOST_PRIORITE_ANALYSE:
#                     skill = Skill_boost_priorite_analyse() # C'est que certains trucs ne se laisse pas analyser si facilement !
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_ANALYSE
#                 elif choix == BOOST_PV:
#                     self.pv_max += 100
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_PV
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == FLECHE_FANTOME:
#                     creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
#                     creation_fleche.ajoute(Cree_fleche_fantome_skill()) #Une fleche qui ignore les murs
#                     self.choix_niveaux[CLASSIQUE][9] = FLECHE_FANTOME
#                 elif choix == BOOST_PRIORITE_EXPLOSIF:
#                     skill = Skill_boost_priorite_explosifs() #Quand est-ce que la priorité des explosifs intervient ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_EXPLOSIF
#                 elif choix == BOOST_VITESSE_EXPLOSIF:
#                     skill = Skill_boost_vitesse_explosifs() #Voilà qui va me faire beaucoup de skills à créer...
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_VITESSE_EXPLOSIF
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == BOOST_PRIORITE_AURA:
#                     skill = Skill_boost_priorite_aura()
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_AURA
#                 elif choix == AURA_MORTELLE:
#                     skill = Skill_aura_mortelle()
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = AURA_MORTELLE
#                 elif choix == ASSASSIN:
#                     classe = Assassin()
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][9] = ASSASSIN
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == BOOST_DE_ZONE_DE_RESTAURATION:
#                     skill = Skill_boost_zone_restauration() #Je crois que ce skill est encore à inventer. Qu'est-ce qu'il est censé faire déjà ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][9] = BOOST_DE_ZONE_DE_RESTAURATION
#                 elif choix == ANGE:
#                     classe = Ange() # Le soigneur/renforceur ultime. Mais devra s'y reprendre à trois fois pour tuer une mouche.
#                     classe.evo()
#                     self.classe_principale.sous_classes.append(classe)
#                     self.choix_niveaux[CLASSIQUE][9] = ANGE
#                 elif choix == ENCHANTEMENT_ROUILLE:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_enchantement_rouille) #Il me semble que c'est bien la même chose
#                     self.choix_niveaux[CLASSIQUE][9] = ENCHANTEMENT_ROUILLE

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         elif niveau == 10:
#             if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
#                 if choix == MANIPULATION_ARME:
#                     skill = Skill_manipulation_arme() #Une option pour le décaller dans une autre classe, maître d'armes à tout hasard ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][10] = MANIPULATION_ARME
#                 elif choix == BOOST_PV:
#                     self.pv_max += 100
#                     self.choix_niveaux[CLASSIQUE][10] = BOOST_PV
#                 elif choix == DEFENSE:
#                     skill = Skill_defense() # Comment ça, j'essaye "encore" de le recaser ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][10] = DEFENSE
#             elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
#                 if choix == FLECHES_LOURDE_LEGERE:
#                     creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
#                     creation_fleche.ajoute(Cree_fleche_lourde_skill())
#                     creation_fleche.ajoute(Cree_fleche_legere_skill()) #Pour compléter l'éventail de l'archer amateur comme du sniper professionnel, variez les plaisirs et optez pour le duo flèche lourd, flèche légère !
#                     self.choix_niveaux[CLASSIQUE][10] = FLECHES_LOURDE_LEGERE
#                 elif choix == BOOST_PRIORITE:
#                     self.priorite += 1
#                     self.choix_niveaux[CLASSIQUE][10] = BOOST_PRIORITE
#                 elif choix == BOOST_PORTEE_EXPLOSIFS:
#                     creation_explosifs = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
#                     creation_explosifs.boost_portee()
#                     self.choix_niveaux[CLASSIQUE][10] = BOOST_PORTEE_EXPLOSIFS
#             elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
#                 if choix == ECLAIR_NOIR:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_eclair_noir) # À la fois le sort et le projectile le plus puissant du jeu ! Dévastateur dans toutes les situations, peut annihiler une horde et pousser le boss final à la fuite ! Ok, peut-être pas le boss final...
#                     self.choix_niveaux[CLASSIQUE][10] = ECLAIR_NOIR
#                 elif choix == BOOST_DEGATS_PROJECTILES:
#                     skill = Skill_boost_degats_projectiles() # Je ne sais plus à quoi il sert. Pour les sorts de projectiles, peut-être ?
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][10] = BOOST_DEGATS_PROJECTILES
#                 elif choix == BOOST_PM:
#                     self.pm_max += 100
#                     self.choix_niveaux[CLASSIQUE][10] = BOOST_PM
#             elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
#                 if choix == BOOST_ENCHANTEMENT:
#                     skill = Skill_boost_enchantement() # Non, les boosts intrasecs à la classe enchanteur ne sont pas suffisant...
#                     skill.evo()
#                     self.classe_principale.skills.append(skill)
#                     self.choix_niveaux[CLASSIQUE][10] = BOOST_ENCHANTEMENT
#                 elif choix == RESURECTION:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_resurection) # Quand on laisse ses alliés faire tout le sale boulot, ça peut servir...
#                     self.choix_niveaux[CLASSIQUE][10] = RESURECTION
#                 elif choix == ECLAIR_NOIR:
#                     magie = trouve_skill(self.classe_principale,Skill_magie)
#                     magie.ajoute(Magie_eclair_noir) # À la fois le sort et le projectile le plus puissant du jeu ! Dévastateur dans toutes les situations, peut annihiler une horde et pousser le boss final à la fuite ! Ok, peut-être pas le boss final...
#                     self.choix_niveaux[CLASSIQUE][10] = ECLAIR_NOIR

#             self.pv_max += 10
#             self.pm_max += 10
#             self.niveau += 1
#             self.priorite += 1

#         #Pour les affinités, c'est simple (sauf si on veut rescussiter le skill d'augmentation de l'affinité):
#         if choix == affinite_terre :
#             self.aff_t *= 1.5
#             self.aff_o *= 0.9 #L'ombre se mélange vraiment mal avec le reste
#             self.choix_niveaux[ELEMENTAL][TERRE][affinite] = True
#             if self.prem_terre == None:
#                 self.prem_terre = affinite
#         elif choix == affinite_feu :
#             self.aff_f *= 1.5
#             self.aff_o *= 0.9 #L'ombre se mélange vraiment mal avec le reste
#             self.choix_niveaux[ELEMENTAL][FEU][affinite] = True
#             if self.prem_feu == None:
#                 self.prem_feu = affinite
#         elif choix == affinite_glace :
#             self.aff_g *= 1.5
#             self.aff_o *= 0.9 #L'ombre se mélange vraiment mal avec le reste
#             self.choix_niveaux[ELEMENTAL][GLACE][affinite] = True
#             if self.prem_glace == None:
#                 self.prem_glace = affinite
#         elif choix == affinite_ombre :
#             self.aff_o *= 1.5
#             self.aff_t *= 0.9 #L'ombre se mélange vraiment mal avec le reste
#             self.aff_f *= 0.9 #L'ombre se mélange vraiment mal avec le reste
#             self.aff_g *= 0.9 #L'ombre se mélange vraiment mal avec le reste
#             self.choix_niveaux[ELEMENTAL][OMBRE][affinite] = True
#             if self.prem_ombre == None:
#                 self.prem_ombre = affinite

#         #Pour les auras, il faudra rajouter le choix de ratacher le skill à la classe élémentaliste
#         elif choix == aura_terre :
#             skill = Skill_aura_elementale_terre(Aura_terre) #On crée le skill
#             skill.evo() #On le passe au niveau 1
#             self.classe_principale.skills.append(skill)
#             self.choix_niveaux[ELEMENTAL][TERRE][aura] = True
#         elif choix == aura_feu :
#             skill = Skill_aura_elementale_feu(Aura_feu) #On crée le skill
#             skill.evo() #On le passe au niveau 1
#             self.classe_principale.skills.append(skill)
#             self.choix_niveaux[ELEMENTAL][FEU][aura] = True
#         elif choix == aura_glace :
#             skill = Skill_aura_elementale_glace(Aura_glace) #On crée le skill
#             skill.evo() #On le passe au niveau 1
#             self.classe_principale.skills.append(skill)
#             self.choix_niveaux[ELEMENTAL][GLACE][aura] = True
#         elif choix == aura_ombre :
#             skill = Skill_aura_elementale_ombre(Aura_ombre) #On crée le skill
#             skill.evo() #On le passe au niveau 1
#             self.classe_principale.skills.append(skill)
#             self.choix_niveaux[ELEMENTAL][OMBRE][aura] = True

#         # Pour les magies, on se contente de les rajouter aux magies disponibles du skill magie (créer un skill spécifique qui peut rapporter de l'xp pour une autre classe que la principale ? vérifier que les magies n'y sont pas encore ?)
#         elif choix == magie_terre :
#             skill = trouve_skill(self.classe_principale,Skill_magie)
#             skill.ajoute(Magie_rocher)
#             skill.ajoute(Magie_enchantement_sable)
#             skill.ajoute(Magie_avalanche)
#             self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] = True
#             if self.prem_terre == None:
#                 self.prem_terre = MAGIE
#         elif choix == magie_feu :
#             skill = trouve_skill(self.classe_principale,Skill_magie)
#             skill.ajoute(Magie_boule_de_feu)
#             skill.ajoute(Magie_enchantement_flamme)
#             skill.ajoute(Magie_brasier)
#             self.choix_niveaux[ELEMENTAL][FEU][MAGIE] = True
#             if self.prem_feu == None:
#                 self.prem_feu = MAGIE
#         elif choix == magie_glace :
#             skill = trouve_skill(self.classe_principale,Skill_magie)
#             skill.ajoute(Magie_fleche_de_glace)
#             skill.ajoute(Magie_enchantement_neige)
#             skill.ajoute(Magie_blizzard)
#             self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] = True
#             if self.prem_glace == None:
#                 self.prem_glace = MAGIE
#         elif choix == magie_ombre :
#             skill = trouve_skill(self.classe_principale,Skill_magie)
#             skill.ajoute(Magie_ombre_furtive)
#             skill.ajoute(Magie_enchantement_tenebre)
#             skill.ajoute(Magie_obscurite)
#             self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] = True
#             if self.prem_ombre == None:
#                 self.prem_ombre = MAGIE

#         # Pour les élémentaux, il faudra rajouter le choix de ratacher la classe d'élémental à la classe élémentaliste, et de déplacer le skill d'aura vers la nouvelle classe d'élémental (et le skill d'affinité si on le crée)
#         elif choix == elemental_terre :
#             classe = Elemental_de_terre()
#             classe.evo()
#             self.classe_principale.sous_classes.append(classe)
#             self.choix_niveaux[ELEMENTAL][TERRE][elemental] = True
#             self.choix_niveaux[ELEMENTAL][TERRE][affinite] = False
#             self.immunites.append(TERRE)
#         elif choix == elemental_feu :
#             classe = Elemental_de_feu()
#             classe.evo()
#             self.classe_principale.sous_classes.append(classe)
#             self.choix_niveaux[ELEMENTAL][FEU][elemental] = True
#             self.choix_niveaux[ELEMENTAL][FEU][affinite] = False
#             self.immunites.append(FEU)
#         elif choix == elemental_glace :
#             classe = Elemental_de_glace()
#             classe.evo()
#             self.classe_principale.sous_classes.append(classe)
#             self.choix_niveaux[ELEMENTAL][GLACE][elemental] = True
#             self.choix_niveaux[ELEMENTAL][GLACE][affinite] = False
#             self.immunites.append(GLACE)
#         elif choix == elemental_ombre :
#             classe = Elemental_d_ombre()
#             classe.evo()
#             self.classe_principale.sous_classes.append(classe)
#             self.choix_niveaux[ELEMENTAL][OMBRE][elemental] = True
#             self.choix_niveaux[ELEMENTAL][OMBRE][affinite] = False
#             self.immunites.append(OMBRE)

    # def discute(self,touche): #/!\ Est-ce que c'est utilisé quelque part?
    #     self.interlocuteur.parle(touche)