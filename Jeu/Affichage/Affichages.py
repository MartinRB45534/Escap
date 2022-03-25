from Jeu.Constantes import *
from Jeu.Affichage.Affichage import *
from Jeu.Skins.Skins import *
from math import ceil

class Old_affichage:
    def __init__(self,screen):
        #print("Initialisation de l'affichage")
        self.screen = screen
        self.hauteur_ecran = 0
        self.largeur_ecran = 0
        self.hauteur_exploitable = 0
        self.largeur_exploitable = 0
        self.marge_gauche = 0
        self.marge_haut = 0
        self.largeur_rectangles = 0
        self.position_debut_x_rectangle_1 = 0
        self.position_fin_x_rectangle_1 = 0
        self.position_debut_x_carre = 0
        self.position_fin_x_carre = 0
        self.position_debut_x_rectangle_2 = 0
        self.position_fin_x_rectangle_2 = 0
        self.position_debut_y_titre = 0
        self.position_debut_y_rectangles_et_carre = 0
        self.position_fin_y_rectangles_et_carre = 0
        self.frame = 0
        self.messages = [["Affichage initialisé avec succès",20,0]]
        self.recalcule_zones()
        self.dessine_zones(None)

    def recalcule_zones(self):
        self.hauteur_ecran = self.screen.get_height() #Pour comparaison, l'écran de mon ASUS contient du (1350,690)
        self.largeur_ecran = self.screen.get_width()
        while self.hauteur_ecran < 690 or self.largeur_ecran < 1350:
            print("Ecran trop petit, veuilez redimensionner.")
            res = True
            while res:
                for event in pygame.event.get():
                    if event.type == pygame.VIDEORESIZE:
                        res = False
                        e = event
            self.hauteur_ecran = e.h
            self.largeur_ecran = e.w
        pygame.display.set_mode((self.largeur_ecran,self.hauteur_ecran),pygame.RESIZABLE)
        self.hauteur_exploitable = ((self.hauteur_ecran - 30)//20)*20
        self.largeur_exploitable = ((self.largeur_ecran - 30)//20)*20

        if self.hauteur_exploitable * 2 > self.largeur_exploitable :
            self.hauteur_exploitable = self.largeur_exploitable / 2
        elif self.hauteur_exploitable * 2 < self.largeur_exploitable :
            self.largeur_exploitable = self.hauteur_exploitable * 2
        else :
            print("Dimensions parfaites !")
        self.marge_gauche = ((self.largeur_ecran - self.largeur_exploitable) // 2) - 10
        self.marge_haut = ((self.hauteur_ecran - self.hauteur_exploitable) // 2) + -10
        self.largeur_rectangles = (self.largeur_exploitable) / 4

        self.position_debut_x_rectangle_1 = self.marge_gauche
        self.position_fin_x_rectangle_1 = self.position_debut_x_rectangle_1 + self.largeur_rectangles
        self.position_debut_x_carre = self.position_fin_x_rectangle_1 + 10
        self.position_fin_x_carre = self.position_debut_x_carre + self.hauteur_exploitable
        self.position_debut_x_rectangle_2 = self.position_fin_x_carre + 10
        self.position_fin_x_rectangle_2 = self.position_debut_x_rectangle_2 + self.largeur_rectangles

        self.position_debut_y_titre = self.marge_haut
        self.position_debut_y_rectangles_et_carre = self.marge_haut + 20
        self.position_fin_y_rectangles_et_carre = self.position_debut_y_rectangles_et_carre + self.hauteur_exploitable

    def dessine(self,joueur):
        """phase de jeu normale"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_lab(joueur)
        self.dessine_droite(joueur)
        self.dessine_gauche(joueur)

    def dialogue(self,joueur):
        """phase de dialogue avec un pnj"""
        self.dessine_zones(joueur)

        self.dessine_lab(joueur)
        self.dessine_droite_dialogue(joueur)
        self.dessine_gauche(joueur)

    def draw_magie_cible(self,joueur):
        """phase de choix d'une cible"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_lab(joueur)
        self.dessine_droite_magie_cible(joueur)
        self.dessine_gauche(joueur)

    def redraw_magie_cible(self,joueur,proportion_ecoulee):
        """phase de choix d'une cible"""
        self.frame += 1
        self.redessine_zone_d()
        self.dessine_droite_magie_cible(joueur,proportion_ecoulee)

    def draw_magie_case(self,joueur):
        """phase de choix d'une case"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_lab_magie(joueur)
        self.dessine_droite_magie_case(joueur)
        self.dessine_gauche(joueur)

    def redraw_magie_case(self,joueur,proportion_ecoulee):
        """phase de choix d'une case"""
        self.frame += 1
        self.redessine_zone_c()
        self.dessine_lab_magie(joueur)
        self.dessine_droite_magie_case(joueur,proportion_ecoulee)

    def draw_magie_dir(self,joueur):
        """phase de choix d'une direction"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_lab(joueur)
        self.dessine_droite_magie_dir(joueur)
        self.dessine_gauche(joueur)

    def redraw_magie_dir(self,joueur,proportion_ecoulee):
        """phase de choix d'une direction"""
        self.frame += 1
        self.redessine_zone_d()
        self.dessine_droite_magie_dir(joueur,proportion_ecoulee)

    def draw_magie_cout(self,joueur):
        """phase de choix d'un cout"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_lab(joueur)
        self.dessine_droite_magie_cout(joueur)
        self.dessine_gauche(joueur)

    def redraw_magie_cout(self,joueur,proportion_ecoulee):
        """phase de choix d'un cout"""
        self.frame += 1
        self.redessine_zone_d()
        self.dessine_droite_magie_cout(joueur,proportion_ecoulee)

    def draw_menu(self,joueur):
        """phase de choix d'un element dans une menu"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_menu(joueur)
        self.dessine_droite_menu(joueur)
        self.dessine_gauche(joueur)

    def draw_menu_alchimie(self,joueur):
        """phase de choix d'un element dans une menu"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_menu_alchimie(joueur)
        self.dessine_droite_alchimie(joueur)
        self.dessine_gauche(joueur)

    def draw_menu_cuisine(self,joueur):
        """phase de choix d'un element dans une menu"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_menu_cuisine(joueur)
        self.dessine_droite_cuisine(joueur)
        self.dessine_gauche(joueur)

    def dessine_zones(self,joueur=None):
        self.screen.fill((0,0,0))
        if joueur != None:
            emplacement = joueur.position[0]
            if joueur.controleur.pause:
                emplacement += " (en pause)"
            curseur = joueur.curseur
        else:
            emplacement = "???"
            curseur = "carré"
        titre=POLICE20.render(emplacement,True,(255,255,255))
        self.screen.blit(titre,(self.position_debut_x_rectangle_1,self.position_debut_y_titre))
        if curseur == "rectangle_g":
            pygame.draw.rect(self.screen,(255,64,0),(self.position_debut_x_rectangle_1-2,self.position_debut_y_rectangles_et_carre-2,self.largeur_rectangles+4,self.hauteur_exploitable+4))
        elif curseur == "carré":
            pygame.draw.rect(self.screen,(255,64,0),(self.position_debut_x_carre-2,self.position_debut_y_rectangles_et_carre-2,self.hauteur_exploitable+4,self.hauteur_exploitable+4))
        elif curseur == "rectangle_d":
            pygame.draw.rect(self.screen,(255,64,0),(self.position_debut_x_rectangle_2-2,self.position_debut_y_rectangles_et_carre-2,self.largeur_rectangles+4,self.hauteur_exploitable+4))
        self.redessine_zone_g()
        self.redessine_zone_c()
        self.redessine_zone_d()

    def redessine_zone_d(self):
        #Reset la zone de droite. Pour quand on n'a pas besoin de redessiner les trois zones.
        pygame.draw.rect(self.screen,(255,255,255),(self.position_debut_x_rectangle_2,self.position_debut_y_rectangles_et_carre,self.largeur_rectangles,self.hauteur_exploitable))

    def redessine_zone_g(self):
        #Reset la zone de gauche. Pour quand on n'a pas besoin de redessiner les trois zones.
        pygame.draw.rect(self.screen,(255,255,255),(self.position_debut_x_rectangle_1,self.position_debut_y_rectangles_et_carre,self.largeur_rectangles,self.hauteur_exploitable))

    def redessine_zone_c(self):
        #Reset la zone du centre. Pour quand on n'a pas besoin de redessiner les trois zones.
        pygame.draw.rect(self.screen,(0,0,0),(self.position_debut_x_carre,self.position_debut_y_rectangles_et_carre,self.hauteur_exploitable,self.hauteur_exploitable))

    def dessine_gauche(self,joueur): #La fonction qui dessine le rectangle de gauche. Elle affiche principalement les informations du joueur, comme les pv, les pm, l'inventaire, etc.

        marge_gauche = self.position_debut_x_rectangle_1+5
        marge_haut = self.position_debut_y_rectangles_et_carre+5

        police=pygame.font.SysFont(None, 20)

        skill = trouve_skill(joueur.classe_principale,Skill_observation)

        observation = 0

        curseur = joueur.curseur

        couleur_curseur_actif = (255,64,0)

        if curseur == "stats": #Le curseur est sur les stats. On le dessine autour des stats :

            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-10,40))

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-14,36))

            marge_haut += 5

            pos_PV = marge_gauche + 5

            pos_PM = marge_gauche + self.largeur_rectangles//2

            longueur_barre_totale = self.largeur_rectangles//2 - 15

            PV = POLICE20.render("PV",True,(0,0,0))
            PM = POLICE20.render("PM",True,(0,0,0))
            self.screen.blit(PV,(pos_PV,marge_haut))
            self.screen.blit(PM,(pos_PM,marge_haut))

            marge_haut += 15

            if joueur.pv <= 0: #Le joueur a moins de 0 pv. On a besoin de tracer la barre à gauche du 0
                total_pv = joueur.pv_max - joueur.pv
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(pos_PV,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(96,0,160),(pos_PV,marge_haut,longueur_barre_pv,10))

            else:
                total_pv = joueur.pv_max
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(pos_PV,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(255,0,0),(pos_PV,marge_haut,longueur_barre_pv,10))

            if joueur.pm <= 0: #Le joueur a moins de 0 pv. On a besoin de tracer la barre à gauche du 0
                total_pm = joueur.pm_max - joueur.pm
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(pos_PM,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(160,0,224),(pos_PM,marge_haut,longueur_barre_pm,10))

            else:
                total_pm = joueur.pm_max
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(pos_PM,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(32,255,255),(pos_PM,marge_haut,longueur_barre_pm,10))

            marge_haut += 20

        elif curseur == "in_stats":

            #D'abord, on dessine les deux barres de pv et de pm:

            longueur_barre_totale = self.largeur_rectangles-10

            if skill != None:
                observation = skill.utilise() #On observe la barre de pv

            hauteur_barre_pv = self.position_debut_y_rectangles_et_carre+5

            hauteur_texte_pv = self.position_debut_y_rectangles_et_carre+15

            if joueur.pv <= 0: #Le joueur a moins de 0 pv. On a besoin de tracer la barre à gauche du 0
                total_pv = joueur.pv_max - joueur.pv
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(marge_gauche,hauteur_barre_pv,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(96,0,160),(marge_gauche,hauteur_barre_pv,longueur_barre_pv,10))

                quantite=POLICE20.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche+longueur_barre_pv,hauteur_texte_pv))

            else:
                total_pv = joueur.pv_max
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(marge_gauche,hauteur_barre_pv,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(255,0,0),(marge_gauche,hauteur_barre_pv,longueur_barre_pv,10))

                quantite=POLICE20.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche,hauteur_texte_pv))

            if skill != None:
                observation = skill.utilise() #On observe la barre de pm

            hauteur_barre_pm = self.position_debut_y_rectangles_et_carre+30

            hauteur_texte_pm = self.position_debut_y_rectangles_et_carre+40

            if joueur.pm <= 0: #Le joueur a moins de 0 pv. On a besoin de tracer la barre à gauche du 0
                total_pm = joueur.pm_max - joueur.pm
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(marge_gauche,hauteur_barre_pm,self.largeur_rectangles-10,10))
                pygame.draw.rect(self.screen,(160,0,224),(marge_gauche,hauteur_barre_pm,longueur_barre_pm,10))

                quantite=POLICE20.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche+longueur_barre_pm,hauteur_texte_pm))

            elif joueur.pm != joueur.get_total_pm() and observation >= 5: #Le joueur a des effets de réserve et peut les voir (trouver une valeur du niveau du skill observation un peu moins arbitraire !
                total_pm = joueur.get_total_pm() - joueur.pm + joueur.pm_max
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                longueur_barre_pm_sans_reserve = longueur_barre_totale*(joueur.pm_max/total_pm)
                longueur_barre_reserve = longueur_barre_totale - longueur_barre_pm_sans_reserve
                pygame.draw.rect(self.screen,(160,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(32,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_pm,10))
                pygame.draw.rect(self.screen,(32,255,255),(marge_gauche+longueur_barre_pm_sans_reserve,hauteur_barre_pm,longueur_barre_reserve,10))

                quantite=POLICE20.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche,hauteur_texte_pm))

            else:
                total_pm = joueur.pm_max
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(32,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_pm,10))

                quantite=POLICE20.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche,hauteur_texte_pm))

            marge_haut = self.position_debut_y_rectangles_et_carre+55

        else:

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-10,40))

            marge_haut += 5

            pos_PV = marge_gauche + 5

            pos_PM = marge_gauche + self.largeur_rectangles//2

            longueur_barre_totale = self.largeur_rectangles//2 - 15

            PV = POLICE20.render("PV",True,(0,0,0))
            PM = POLICE20.render("PM",True,(0,0,0))
            self.screen.blit(PV,(pos_PV,marge_haut))
            self.screen.blit(PM,(pos_PM,marge_haut))

            marge_haut += 15

            if joueur.pv <= 0: #Le joueur a moins de 0 pv. On a besoin de tracer la barre à gauche du 0
                total_pv = joueur.pv_max - joueur.pv
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(pos_PV,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(96,0,160),(pos_PV,marge_haut,longueur_barre_pv,10))

            else:
                total_pv = joueur.pv_max
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(pos_PV,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(255,0,0),(pos_PV,marge_haut,longueur_barre_pv,10))

            if joueur.pm <= 0: #Le joueur a moins de 0 pv. On a besoin de tracer la barre à gauche du 0
                total_pm = joueur.pm_max - joueur.pm
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(pos_PM,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(160,0,224),(pos_PM,marge_haut,longueur_barre_pm,10))

            else:
                total_pm = joueur.pm_max
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(pos_PM,marge_haut,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(32,255,255),(pos_PM,marge_haut,longueur_barre_pm,10))

            marge_haut += 20

        #On a fini les stats !

        marge_haut += 5

        if skill != None:
            observation = skill.utilise() #On observe l'inventaire

        if curseur == "inventaire":

            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-10,25))
            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-14,21))

            inventaire = POLICE20.render("Inventaire",True,(0,0,0))
            self.screen.blit(inventaire,(marge_gauche+5,marge_haut+5))

            marge_haut += 25

        elif curseur == "in_inventaire":

            #L'affichage de l'inventaire est composé de trois parties : les icones des catégories, les icones des items, et un aperçu de l'item courant

            inventaire = joueur.inventaire #Applaudissez bien fort le protagoniste du rectangle de gauche !

            limite_haut = marge_haut

            cats = inventaire.get_skin_cats()

            titre = POLICE20.render("Inventaire :",True,(0,0,0))
            self.screen.blit(titre,(marge_gauche,limite_haut))

            limite_haut += 25
            marge_haut = limite_haut

            icat = inventaire.cat_courante

            for i in range(len(cats)):
                if i == icat :
                    if inventaire.profondeur == 0:
                        pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche-1,marge_haut-1,42,42))
                    else:
                        
                        pygame.draw.rect(self.screen,(130,130,130),(marge_gauche-1,marge_haut-1,42,42))
                    pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+1,marge_haut+1,38,38))
                else:
                    pygame.draw.rect(self.screen,(200,200,200),(marge_gauche-1,marge_haut-1,42,42))
                cats[i].dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                marge_haut += 44
                #Centrer (verticalement) les icones à l'occasion

            marge_gauche += 44

            noms = ["Potions :","Parchemins :","Clés :","Armes :","Boucliers :","Armures :","Haumes :","Anneaux :","Projectiles :","Cadavres :","Oeufs :"]

            titre_cat = POLICE20.render(noms[icat],True,(0,0,0))
            self.screen.blit(titre_cat,(marge_gauche,limite_haut))
            

            limite_haut += 25
            marge_bas = marge_haut+44
            marge_haut = limite_haut

            items = inventaire.items[inventaire.kiiz[icat]]

            if icat == 3:
                equippement = [inventaire.get_arme()]
            elif icat == 4:
                equippement = [inventaire.get_bouclier()]
            elif icat == 5:
                equippement = [inventaire.get_armure()]
            elif icat == 6:
                equippement = [inventaire.get_haume()]
            elif icat == 7:
                equippement = inventaire.get_anneau()
            else:
                equippement = []

            if items != []:
                for i in range(len(items)):
                    ID_item = items[i]
                    if i == inventaire.item_courant:
                        if inventaire.profondeur == 1:
                            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche-1,marge_haut-1,42,42))
                        else:
                            pygame.draw.rect(self.screen,(130,130,130),(marge_gauche-1,marge_haut-1,42,42))
                        if ID_item in equippement:
                            pygame.draw.rect(self.screen,(170,170,170),(marge_gauche+1,marge_haut+1,38,38))
                        else:
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+1,marge_haut+1,38,38))
                    else:
                        if ID_item in equippement:
                            pygame.draw.rect(self.screen,(170,170,170),(marge_gauche-1,marge_haut-1,42,42))
                        else:
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche-1,marge_haut-1,42,42))
                    item = joueur.controleur.get_entitee(ID_item)
                    item.get_skin().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                    marge_haut += 44

                marge_bas = max(marge_bas,marge_haut + 44)

                marge_gauche += 44

                titre_description = POLICE20.render("Description :",True,(0,0,0))
                self.screen.blit(titre_description,(marge_gauche,limite_haut))

                limite_haut += 25
                marge_haut = limite_haut

                infos = joueur.controleur.get_entitee(items[inventaire.item_courant]).get_description(observation)
                for info in infos :
                    texte_info = POLICE20.render(info,True,(0,0,0))
                    self.screen.blit(texte_info,(marge_gauche,marge_haut))
                    marge_haut += 25

                marge_bas = max(marge_bas,marge_haut + 25)

            marge_haut = marge_bas

        else:

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-10,25))

            inventaire = POLICE20.render("Inventaire",True,(0,0,0))
            self.screen.blit(inventaire,(marge_gauche+5,marge_haut+5))

            marge_haut += 25

        #On en a fini avec l'inventaire

        marge_haut += 5

        marge_gauche = self.position_debut_x_rectangle_1+5

        if skill != None:
            observation = skill.utilise() #On observe la classe principale

        if curseur == "classe":

            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-10,25))
            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-14,21))

            inventaire = POLICE20.render("Classe principale",True,(0,0,0))
            self.screen.blit(inventaire,(marge_gauche+5,marge_haut+5))

            marge_haut += 25

        elif curseur == "in_classe":

            classe = joueur.classe_principale #Applaudissez bien fort l'antagoniste du rectangle de gauche ! (Personne ne veut d'elle, tout le monde préfère les raccourcis clavier...)

            limite_haut = marge_haut

            cont = True

            compt = 1

            while cont :

                compt += 1

                cont = False

                marge_gauche += 10

                if classe.curseur == "classes":

                    pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-(10*compt)-4,21))

                    skill = POLICE20.render("Sous-classes",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                elif classe.curseur == "in_classes":

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render("Sous-classes :",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25
                    classes = classe.sous_classes
                    i_classe = classe.classe_courante
                    for i in range(len(classes)):
                        if i == i_classe:
                            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche+5,marge_haut,self.largeur_rectangles-(10*compt)-5,25))
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+7,marge_haut+2,self.largeur_rectangles-(10*compt)-9,21))
                        else:
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+5,marge_haut,self.largeur_rectangles-(10*compt)-5,25))
                        nom_classe = POLICE20.render(classes[i].nom,True,(0,0,0))
                        self.screen.blit(nom_classe,(marge_gauche+10,marge_haut+5))
                        marge_haut += 25

                elif classe.curseur == "in_classe":

                    cont = True
                    classe = classe.sous_classes[classe.classe_courante]

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render(classe.nom,True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                else:

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render("Sous-classes",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25


                if classe.curseur == "skills_intrasecs":

                    pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-(10*compt)-4,21))

                    skill = POLICE20.render("Skills intrasecs",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                elif classe.curseur == "in_skills_intrasecs":

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render("Skills intrasecs :",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25
                    skills = classe.skills_intrasecs
                    i_skill = classe.skill_intrasec_courant
                    for i in range(len(skills)):
                        if i == i_skill:
                            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche+5,marge_haut,self.largeur_rectangles-(10*compt)-5,25))
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+7,marge_haut+2,self.largeur_rectangles-(10*compt)-9,21))
                        else:
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+5,marge_haut,self.largeur_rectangles-(10*compt)-5,25))
                        nom_skill = POLICE20.render(skills[i].nom,True,(0,0,0))
                        self.screen.blit(nom_skill,(marge_gauche+10,marge_haut+5))
                        marge_haut += 25

                elif not cont:

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render("Skills intrasecs",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                if classe.curseur == "skills":

                    pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-(10*compt)-4,21))

                    skill = POLICE20.render("Skills",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                elif classe.curseur == "in_skills":

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render("Skills :",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25
                    skills = classe.skills
                    i_skill = classe.skill_courant
                    for i in range(len(skills)):
                        if i == i_skill:
                            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche+5,marge_haut,self.largeur_rectangles-(10*compt)-5,25))
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+7,marge_haut+2,self.largeur_rectangles-(10*compt)-9,21))
                        else:
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+5,marge_haut,self.largeur_rectangles-(10*compt)-5,25))
                        nom_skill = POLICE20.render(skills[i].nom,True,(0,0,0))
                        self.screen.blit(nom_skill,(marge_gauche+10,marge_haut+5))
                        marge_haut += 25

                elif not cont:

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = POLICE20.render("Skills",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25



        else:

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-10,25))

            inventaire = POLICE20.render("Classe principale",True,(0,0,0))
            self.screen.blit(inventaire,(marge_gauche+5,marge_haut+5))

            marge_haut += 25

    def dessine_droite(self,joueur):

        marge_gauche = self.position_debut_x_rectangle_2+9
        marge_haut = self.position_debut_y_rectangles_et_carre+5

        police=pygame.font.SysFont(None, 20)

        skill = trouve_skill(joueur.classe_principale,Skill_observation)

        observation = 0

        curseur = joueur.curseur

        couleur_curseur_actif = (255,64,0)

        esprit = joueur.controleur.get_esprit(joueur.esprit)

        curseur_in = esprit.curseur

        corps = sorted(esprit.get_corps_vus())
        ennemis = esprit.get_ennemis_vus()
        if (curseur_in == "corps" or curseur_in == "in_corps") and corps != []:
            ID_courant = corps[esprit.allie_courant]
        elif (curseur_in == "ennemis" or curseur_in == "in_ennemis") and ennemis != []:
            ID_courant = ennemis[esprit.ennemi_courant]
        else:
            ID_courant = 0

        if curseur == "rectangle_d" or curseur == "in_esprit": #Le curseur est sur le rectangle de droite, on l'a déjà dessiné en dessinant les zones

            #Les copains d'abord :

            if (curseur == "rectangle_d" and curseur_in == "corps") or curseur_in == "in_corps":
                pygame.draw.rect(self.screen,(130,130,130),(marge_gauche-4,marge_haut,48,44*len(corps)+4))
                pygame.draw.rect(self.screen,(2,83,9),(marge_gauche-2,marge_haut+2,44,44*len(corps)))

            elif curseur == "in_esprit" and curseur_in == "corps":
                pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche-4,marge_haut,48,44*len(corps)+4))
                pygame.draw.rect(self.screen,(2,83,9),(marge_gauche-2,marge_haut+2,44,44*len(corps)))

            else:
                pygame.draw.rect(self.screen,(2,83,9),(marge_gauche-4,marge_haut,48,44*len(corps)+4))

            marge_haut += 4

            for i in range(len(corps)):
                if corps[i] == ID_courant :
                    if curseur_in == "in_corps":
                        pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche-1,marge_haut-1,42,42))
                        pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+1,marge_haut+1,38,38))
                    else:
                        pygame.draw.rect(self.screen,(130,130,130),(marge_gauche-1,marge_haut-1,42,42))
                        pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+1,marge_haut+1,38,38))
                else:
                    pygame.draw.rect(self.screen,(200,200,200),(marge_gauche-1,marge_haut-1,42,42))
                agissant = joueur.controleur.get_entitee(corps[i])
                taille = 40
                position = (marge_gauche,marge_haut)
                direction = agissant.get_direction()
                arme = agissant.inventaire.arme
                if arme != None:
                    joueur.controleur.get_entitee(arme).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                agissant.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                armure = agissant.inventaire.armure
                if armure != None:
                    joueur.controleur.get_entitee(armure).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                bouclier = agissant.inventaire.bouclier
                if bouclier != None:
                    joueur.controleur.get_entitee(bouclier).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                haume = agissant.inventaire.haume
                agissant.get_skin_tete().dessine_toi(self.screen,position,taille,1,1,direction) #Avoir éventuellement la tête dans une autre direction ?
                if haume != None:
                    joueur.controleur.get_entitee(haume).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                for statut in agissant.get_skins_statuts():
                    statut.dessine_toi(self.screen,position,taille)
                for effet in agissant.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                self.screen.blit(pygame.transform.scale(pygame.image.load("Jeu/Skins/barre_de_vie.png").convert_alpha(),(int(taille*((15*agissant.pv)/(19*agissant.pv_max))),int(taille*(15/19)))),(position[0]+int(taille*(2/19)),position[1]+int(taille*(15/19))))
                marge_haut += 44

            #Puis les ennemis :
            if ennemis != []:

                marge_haut += 5

                if (curseur == "rectangle_d" and curseur_in == "ennemis") or curseur_in == "in_ennemis":
                    pygame.draw.rect(self.screen,(130,130,130),(marge_gauche-4,marge_haut,48,44*len(ennemis)+4))
                    pygame.draw.rect(self.screen,(61,6,1),(marge_gauche-2,marge_haut+2,44,44*len(ennemis)))

                elif curseur == "in_esprit" and curseur_in == "ennemis":
                    pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche-4,marge_haut,48,44*len(ennemis)+4))
                    pygame.draw.rect(self.screen,(61,6,1),(marge_gauche-2,marge_haut+2,44,44*len(ennemis)))

                else:
                    pygame.draw.rect(self.screen,(2,83,9),(marge_gauche-4,marge_haut,48,44*len(ennemis)+4))

                marge_haut += 4

                for i in range(len(ennemis)):
                    if ennemis[i] == ID_courant :
                        if curseur_in == "in_ennemis":
                            pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche-1,marge_haut-1,42,42))
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+1,marge_haut+1,38,38))
                        else:
                            pygame.draw.rect(self.screen,(130,130,130),(marge_gauche-1,marge_haut-1,42,42))
                            pygame.draw.rect(self.screen,(200,200,200),(marge_gauche+1,marge_haut+1,38,38))
                    else:
                        pygame.draw.rect(self.screen,(200,200,200),(marge_gauche-1,marge_haut-1,42,42))
                    agissant = joueur.controleur.get_entitee(ennemis[i])
                    taille = 40
                    position = (marge_gauche,marge_haut)
                    direction = agissant.get_direction()
                    arme = agissant.inventaire.arme
                    if arme != None:
                        joueur.controleur.get_entitee(arme).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                    agissant.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                    armure = agissant.inventaire.armure
                    if armure != None:
                        joueur.controleur.get_entitee(armure).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                    bouclier = agissant.inventaire.bouclier
                    if bouclier != None:
                        joueur.controleur.get_entitee(bouclier).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                    haume = agissant.inventaire.haume
                    agissant.get_skin_tete().dessine_toi(self.screen,position,taille,1,1,direction) #Avoir éventuellement la tête dans une autre direction ?
                    if haume != None:
                        joueur.controleur.get_entitee(haume).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                    for statut in agissant.get_skins_statuts():
                        statut.dessine_toi(self.screen,position,taille)
                    for effet in agissant.effets:
                        if effet.affiche:
                            effet.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                    self.screen.blit(pygame.transform.scale(pygame.image.load("Jeu/Skins/barre_de_vie.png").convert_alpha(),(int(taille*((15*agissant.pv)/(19*agissant.pv_max))),int(taille*(15/19)))),(position[0]+int(taille*(2/19)),position[1]+int(taille*(15/19))))
                    marge_haut += 44

        if curseur == "in_esprit" and ID_courant != 0:
            marge_gauche += 53
            marge_haut = self.position_debut_y_rectangles_et_carre+10
            for texte in joueur.controleur.get_entitee(ID_courant).get_texte_descriptif():
                for tex in self.scinde_texte(texte,self.largeur_rectangles-58):
                    self.screen.blit(tex,(marge_gauche,marge_haut))
                    marge_haut += 20

        if curseur == "carré":
            self.observe(joueur,joueur.position,range(4)[joueur.dir_regard-2],(self.position_debut_x_rectangle_2+15,self.position_debut_y_rectangles_et_carre+15,300,400))

    def dessine_droite_dialogue(self,joueur): #La fonction qui écrit les dialogues à droite
        #Dans un jeu parfait, on aurait une image de l'interlocuteur au dessus des répliques

        self.observe(joueur,joueur.interlocuteur.position,joueur.dir_regard,(self.position_debut_x_rectangle_2+15,self.position_debut_y_rectangles_et_carre+15,300,400))

        marge_haut = self.position_debut_y_rectangles_et_carre + 435
        marge_gauche = self.position_debut_x_rectangle_2 + 5

        #D'abord, la réplique de l'interlocuteur, si il y en a une
        textes = self.scinde_texte(joueur.interlocuteur.get_replique(joueur.interlocuteur.replique),self.largeur_rectangles-10)
        for texte in textes :
            self.screen.blit(texte,(marge_gauche,marge_haut))
            marge_haut += 20
        marge_haut += 20

        replique_courante = joueur.interlocuteur.replique_courante
        for i in range(len(joueur.interlocuteur.repliques)):
            replique = joueur.interlocuteur.get_replique(joueur.interlocuteur.repliques[i])
            textes = self.scinde_texte(replique,self.largeur_rectangles-25)
            if replique_courante == i:
                self.screen.blit(pygame.font.SysFont(None, 20).render("->",True,(255,125,0)),(marge_gauche,marge_haut))
            for texte in textes :
                self.screen.blit(texte,(marge_gauche+15,marge_haut))
                marge_haut += 20
            marge_haut += 10

    def dessine_droite_magie_cible(self,joueur,proportion_ecoulee = 0): #La fonction qui dessine le rectangle de droite, pendant les choix de cible

        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5

        skill = trouve_skill(joueur.classe_principale,Skill_observation)
        observation = 0
        if skill != None:
            observation = skill.utilise()

        for i in range(len(joueur.cibles)):
            if i == joueur.element_courant:
                pygame.draw.rect(self.screen,(255,64,0),(marge_gauche,marge_haut,44,44))
                if joueur.cibles[i] in joueur.cible:
                    pygame.draw.rect(self.screen,(130,130,130),(marge_gauche+2,marge_haut+2,40,40))
                else:
                    pygame.draw.rect(self.screen,(255,255,255),(marge_gauche+2,marge_haut+2,40,40))
            else:
                if joueur.cibles[i] in joueur.cible:
                    pygame.draw.rect(self.screen,(130,130,130),(marge_gauche,marge_haut,44,44))
                else:
                    pygame.draw.rect(self.screen,(255,255,255),(marge_gauche,marge_haut,44,44))
            agissant = joueur.controleur.get_entitee(joueur.cibles[i])
            position = (marge_gauche+2,marge_haut+2)
            taille = 40
            direction = agissant.get_direction()
            arme = agissant.inventaire.arme
            if arme != None:
                joueur.controleur.get_entitee(arme).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
            agissant.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
            armure = agissant.inventaire.armure
            if armure != None:
                joueur.controleur.get_entitee(armure).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
            bouclier = agissant.inventaire.bouclier
            if bouclier != None:
                joueur.controleur.get_entitee(bouclier).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
            haume = agissant.inventaire.haume
            agissant.get_skin_tete().dessine_toi(self.screen,position,taille,1,1,direction) #Avoir éventuellement la tête dans une autre direction ?
            if haume != None:
                joueur.controleur.get_entitee(haume).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
            if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif en-dessous des effets ?
                SKIN_DIALOGUE.dessine_toi(self.screen,position,taille)
            for effet in agissant.effets:
                if effet.affiche:
                    effet.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
            self.screen.blit(pygame.transform.scale(pygame.image.load("Jeu/Skins/barre_de_vie.png").convert_alpha(),(int(taille*((15*agissant.pv)/(19*agissant.pv_max))),int(taille*(15/19)))),(position[0]+int(taille*(2/19)),position[1]+int(taille*(2/19))))
            marge_haut += 50
        marge_gauche += 50
        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        # Rajouter des informations sur l'entitee sous le curseur

        #On cherche à placer une barre au bas du rectangle de droite
        pos_haut = self.position_debut_y_rectangles_et_carre + self.hauteur_exploitable - 15
        pos_gauche = self.position_debut_x_rectangle_2 + 5

        longueur_barre_totale = self.largeur_rectangles-10
        longueur_barre_temps = longueur_barre_totale*proportion_ecoulee

        pygame.draw.rect(self.screen,(255,255,100),(pos_gauche,pos_haut,longueur_barre_totale,10))
        pygame.draw.rect(self.screen,(255,200,0),(pos_gauche,pos_haut,longueur_barre_temps,10))

    def dessine_droite_magie_dir(self,joueur,proportion_ecoulee = 0):

        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5

        SKIN_DIRECTION.dessine_toi(self.screen,(marge_gauche,marge_haut),40,1,1,joueur.dir_regard)

        #On cherche à placer une barre au bas du rectangle de droite
        pos_haut = self.position_debut_y_rectangles_et_carre + self.hauteur_exploitable - 15
        pos_gauche = self.position_debut_x_rectangle_2 + 5

        longueur_barre_totale = self.largeur_rectangles-10
        longueur_barre_temps = longueur_barre_totale*proportion_ecoulee

        pygame.draw.rect(self.screen,(255,255,100),(pos_gauche,pos_haut,longueur_barre_totale,10))
        pygame.draw.rect(self.screen,(255,200,0),(pos_gauche,pos_haut,longueur_barre_temps,10))

    def dessine_droite_magie_case(self,joueur,proportion_ecoulee = 0):
        #Un jour on mettra plus d'informations /!\

        #On cherche à placer une barre au bas du rectangle de droite
        pos_haut = self.position_debut_y_rectangles_et_carre + self.hauteur_exploitable - 15
        pos_gauche = self.position_debut_x_rectangle_2 + 5

        longueur_barre_totale = self.largeur_rectangles-10
        longueur_barre_temps = longueur_barre_totale*proportion_ecoulee

        pygame.draw.rect(self.screen,(255,255,100),(pos_gauche,pos_haut,longueur_barre_totale,10))
        pygame.draw.rect(self.screen,(255,200,0),(pos_gauche,pos_haut,longueur_barre_temps,10))

    def dessine_droite_magie_cout(self,joueur,proportion_ecoulee = 0):

        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5

        longueur_barre_totale = self.largeur_rectangles-10
        longueur_barre_cout = longueur_barre_totale*(joueur.choix_cout_magie/joueur.get_total_pm())
        pygame.draw.rect(self.screen,(255,160,160),(marge_gauche,marge_haut,longueur_barre_totale,10))
        pygame.draw.rect(self.screen,(255,0,0),(marge_gauche,marge_haut,longueur_barre_cout,10))

        marge_haut += 15

        pygame.font.SysFont(None, 20)

        texte = []

        texte.append(POLICE20.render("Mana à disposition : " + str(joueur.get_total_pm()),True,(0,0,0)))
        texte.append(POLICE20.render("Cout_actuel : " + str(joueur.choix_cout_magie),True,(0,0,0)))
        texte.append(POLICE20.render("(Utilisez les touches haut et bas pour modifier le coût.)",True,(0,0,0)))
        texte.append(POLICE20.render("Précision du coût : " + str(joueur.precision_cout_magie),True,(0,0,0)))
        texte.append(POLICE20.render("(Utilisez les touches gauche et droite pour modifier la précision.)",True,(0,0,0)))

        for tex in texte:
            self.screen.blit(tex,(marge_gauche,marge_haut))
            marge_haut += 25

        #On cherche à placer une barre au bas du rectangle de droite
        pos_haut = self.position_debut_y_rectangles_et_carre + self.hauteur_exploitable - 15
        pos_gauche = self.position_debut_x_rectangle_2 + 5

        longueur_barre_totale = self.largeur_rectangles-10
        longueur_barre_temps = longueur_barre_totale*proportion_ecoulee

        pygame.draw.rect(self.screen,(255,255,100),(pos_gauche,pos_haut,longueur_barre_totale,10))
        pygame.draw.rect(self.screen,(255,200,0),(pos_gauche,pos_haut,longueur_barre_temps,10))

    def dessine_droite_menu(self,joueur):
        skill = trouve_skill(joueur.classe_principale,Skill_observation)
        observation = 0
        if skill != None:
            observation = skill.utilise()
        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5
        option = joueur.options_menu[joueur.element_courant]
        for tex in self.scinde_texte(option.get_titre(observation),self.largeur_rectangles-10,30,(255, 127, 0)): #Le titre
            self.screen.blit(tex,(marge_gauche,marge_haut))
            marge_haut += 30
        
        for texte in option.get_description(observation): #La description détaillée
            for tex in self.scinde_texte(texte,self.largeur_rectangles-10):
                self.screen.blit(tex,(marge_gauche,marge_haut))
                marge_haut += 20

    def dessine_droite_alchimie(self,joueur):
        skill = trouve_skill(joueur.classe_principale,Skill_observation)
        observation = 0
        if skill != None:
            observation = skill.utilise()
        alchimie = trouve_skill(joueur.interlocuteur.classe_principale,Skill_alchimie)
        recette = alchimie.recettes[joueur.element_courant]
        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5
        for tex in self.scinde_texte("Recette :",self.largeur_rectangles-10,30,(255, 127, 0)): #Le titre
            self.screen.blit(tex,(marge_gauche,marge_haut))
            marge_haut += 30

        for texte in eval(recette["produit"]).get_description(None,observation) + ["Ingrédients :"]: #La description détaillée /!\ Revoir le get_description
            for tex in self.scinde_texte(texte,self.largeur_rectangles-10):
                self.screen.blit(tex,(marge_gauche,marge_haut))
                marge_haut += 20

        for ingredient in recette["ingredients"].keys():
            for texte in eval(ingredient).get_description(None,observation)+[f"({joueur.inventaire.quantite(eval(ingredient))}/{recette['ingredients'][ingredient]})"," "]: #La description détaillée
                for tex in self.scinde_texte(texte,self.largeur_rectangles-10):
                    self.screen.blit(tex,(marge_gauche,marge_haut))
                    marge_haut += 20

    def dessine_droite_cuisine(self,joueur):
        skill = trouve_skill(joueur.classe_principale,Skill_observation)
        observation = 0
        if skill != None:
            observation = skill.utilise()
        recette = joueur.objet_interactif.recettes[joueur.element_courant]
        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5
        for tex in self.scinde_texte("Recette :",self.largeur_rectangles-10,30,(255, 127, 0)): #Le titre
            self.screen.blit(tex,(marge_gauche,marge_haut))
            marge_haut += 30

        for texte in eval(recette["produit"]).get_description(None,observation) + ["Ingrédients :"]: #La description détaillée /!\ Revoir le get_description
            for tex in self.scinde_texte(texte,self.largeur_rectangles-10):
                self.screen.blit(tex,(marge_gauche,marge_haut))
                marge_haut += 20

        for ingredient in recette["ingredients"].keys():
            for texte in eval(ingredient).get_description(None,observation)+[f"({joueur.inventaire.quantite(eval(ingredient))}/{recette['ingredients'][ingredient]})"," "]: #La description détaillée
                for tex in self.scinde_texte(texte,self.largeur_rectangles-10):
                    self.screen.blit(tex,(marge_gauche,marge_haut))
                    marge_haut += 20

    def dessine_lab(self,joueur): #La fonction qui dessine le carré au centre. Elle affiche le labyrinthe vu par le joueur, ses occupants, et tout ce que le joueur est capable de percevoir.
        vue = joueur.vue
        position = joueur.get_position()
        visible_x = [len(vue)-1,0]
        visible_y = [len(vue[0])-1,0]
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    if i < visible_x[0]:
                        visible_x[0] = i
                    if i > visible_x[1]:
                        visible_x[1] = i
                    if j < visible_y[0]:
                        visible_y[0] = j
                    if j > visible_y[1]:
                        visible_y[1] = j
        distance = max(position[1]-visible_x[0],visible_x[1]-position[1],position[2]-visible_y[0],visible_y[1]-position[2]) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
        vue_x = position[1] - distance
        vue_y = position[2] - distance
        nb_cases = distance*2 + 1
        taille_case = int(self.hauteur_exploitable // nb_cases)
        hauteur_exploitee = taille_case * nb_cases
        marge = (self.hauteur_exploitable - hauteur_exploitee) // 2
        marge_haut = marge + self.position_debut_y_rectangles_et_carre
        for j in range(nb_cases):
            marge_gauche = marge + self.position_debut_x_carre
            for i in range(nb_cases):
                if 0 <= vue_x + i < len(vue) and 0 <= vue_y + j < len(vue[0]):
                    self.affiche(joueur,vue[vue_x + i][vue_y + j],(marge_gauche,marge_haut),taille_case)
                else:
                    SKIN_BROUILLARD.dessine_toi(self.screen,(marge_gauche,marge_haut),taille_case)
                marge_gauche += taille_case
            marge_haut += taille_case

    def dessine_lab_magie(self,joueur):
        vue = joueur.vue
        position = joueur.get_position()
        visible_x = [len(vue)-1,0]
        visible_y = [len(vue[0])-1,0]
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    if i < visible_x[0]:
                        visible_x[0] = i
                    if i > visible_x[1]:
                        visible_x[1] = i
                    if j < visible_y[0]:
                        visible_y[0] = j
                    if j > visible_y[1]:
                        visible_y[1] = j
        distance = max(position[1]-visible_x[0],visible_x[1]-position[1],position[2]-visible_y[0],visible_y[1]-position[2]) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
        vue_x = position[1] - distance
        vue_y = position[2] - distance
        nb_cases = distance*2 + 1
        taille_case = int(self.hauteur_exploitable // nb_cases)
        hauteur_exploitee = taille_case * nb_cases
        marge = (self.hauteur_exploitable - hauteur_exploitee) // 2
        marge_haut = marge + self.position_debut_y_rectangles_et_carre
        for j in range(nb_cases):
            marge_gauche = marge + self.position_debut_x_carre
            for i in range(nb_cases):
                if (position[0],vue_x+i,vue_y+j) in joueur.cibles:
                    self.affiche(joueur,vue[vue_x + i][vue_y + j],(marge_gauche,marge_haut),taille_case)
                else:
                    SKIN_BROUILLARD.dessine_toi(self.screen,(marge_gauche,marge_haut),taille_case)
                if (position[0],vue_x+i,vue_y+j) == joueur.element_courant:
                    pygame.draw.rect(self.screen,(255,64,0),(marge_gauche,marge_haut,taille_case,taille_case),2)
                elif (position[0],vue_x+i,vue_y+j) in joueur.cible:
                    pygame.draw.rect(self.screen,(170,170,170),(marge_gauche,marge_haut,taille_case,taille_case),2)
                marge_gauche += taille_case
            marge_haut += taille_case

    def dessine_choix_touche(self,joueur,zones,skills,magies,lancer):
        marge_haut = 10 + self.position_debut_y_rectangles_et_carre
        marge_gauche = 10 + self.position_debut_x_carre
        (None, 20)
        etage = joueur.etage
        element_courant = joueur.element_courant
        if etage == -1 :
            if element_courant == 0:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            SKIN_ZONES.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 50
            if element_courant == 1:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            SKIN_SKILL.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 50
            if element_courant == 2:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            if magies != []:
                SKIN_SKILL_MAGIE.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            else:
                SKIN_SKILL_MAGIE_GRIS.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 50
            if element_courant == 3:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            if lancer != []:
                SKIN_SKILL_LANCER.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            else:
                SKIN_SKILL_LANCER_GRIS.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 50
            if element_courant == 4:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            SKIN_QUITTER.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_haut += 50
            marge_gauche = 10 + self.position_debut_x_carre
            descr = ["Touches de déplacement du curseur (zones)","Raccourcis des skills","Raccourcis des magies","Raccourcis des projectiles","Quitter"][element_courant]
            texte = POLICE20.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))
        elif etage == 0 :
            touches = []
            for touche in joueur.cat_touches.keys():
                if joueur.cat_touches[touche] == "zone":
                    touches.append(touche)
            noms_dirs = ["Vers le haut","Vers la droite","Vers le bas","Vers la gauche","Entrer","Sortir","Quitter"]
            skins_dirs = [SKIN_HAUT,SKIN_DROITE,SKIN_BAS,SKIN_GAUCHE,SKIN_IN,SKIN_OUT,SKIN_QUITTER]
            for i in range(7):
                if element_courant == i:
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
                skins_dirs[i].dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                for touche in touches :
                    if joueur.dir_touches[touche] == i:
                        letter = pygame.key.name(touche)
                        lettre = POLICE20.render(letter.upper(),True,(255,255,255))
                        self.screen.blit(lettre,(marge_gauche+28,marge_haut+28))
                marge_gauche += 50
            marge_haut += 50
            marge_gauche = 10 + self.position_debut_x_carre
            descr = noms_dirs[element_courant]
            texte = POLICE20.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))
        elif etage == 1:
            touches = []
            for touche in joueur.cat_touches.keys():
                if joueur.cat_touches[touche] == "skill":
                    touches.append(touche)
            for i in range(len(skills)):
                if element_courant == i:
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
                skills[i].get_skin().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                for touche in touches :
                    if i < len(skills) and joueur.skill_touches[touche] == type(skills[i]) and not isinstance(skills[i],(Skill_magie,Skill_lancer)):
                        letter = pygame.key.name(touche)
                        lettre = POLICE20.render(letter.upper(),True,(255,255,255))
                        self.screen.blit(lettre,(marge_gauche+28,marge_haut+28))
                marge_gauche += 50
                if marge_gauche + 60 > self.position_debut_x_rectangle_2 :
                    marge_haut += 50
                    marge_gauche = 10 + self.position_debut_x_carre
            if element_courant == len(skills) :
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            SKIN_QUITTER.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_haut += 50
            marge_gauche = 10 + self.position_debut_x_carre
            if element_courant == len(skills) :
                descr = "Quitter"
            else :
                descr = skills[element_courant].nom
            texte = POLICE20.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))
        elif etage == 2:
            touches = []
            for touche in joueur.cat_touches.keys():
                if joueur.cat_touches[touche] == "skill" and joueur.skill_touches[touche] == Skill_magie:
                    touches.append(touche)
            for i in range(len(magies)):
                if element_courant == i:
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
                magies[i].get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                for touche in touches :
                    if i < len(magies) and joueur.magies[touche] == magies[i].nom:
                        letter = pygame.key.name(touche)
                        lettre = POLICE20.render(letter.upper(),True,(255,255,255))
                        self.screen.blit(lettre,(marge_gauche+28,marge_haut+28))
                marge_gauche += 50
                if marge_gauche + 60 > self.position_debut_x_rectangle_2 :
                    marge_haut += 50
                    marge_gauche = 10 + self.position_debut_x_carre
            if element_courant == len(magies) :
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            SKIN_QUITTER.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_haut += 50
            marge_gauche = 10 + self.position_debut_x_carre
            if element_courant == len(magies) :
                descr = "Quitter"
            else :
                descr = magies[element_courant].nom
            texte = POLICE20.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))
        elif etage == 3:
            touches = []
            for touche in joueur.cat_touches.keys():
                if joueur.cat_touches[touche] == "skill" and joueur.skill_touches[touche] == Skill_lancer:
                    touches.append(touche)
            for i in range(len(lancer)):
                if element_courant == i:
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
                if lancer[i] == None: #Pour lancer l'item courant
                    SKIN_SKILL_LANCER.dessine_toi(self.screen,(marge_gauche,marge_haut),40) #Mettre un meilleur skin ? Vraiment pas d'idée d'illustration sur ce coup là...
                else:
                    lancer[i].get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                for touche in touches :
                    if i < len(lancer) and joueur.projectiles[touche] == lancer[i]:
                        letter = pygame.key.name(touche)
                        lettre = POLICE20.render(letter.upper(),True,(255,255,255))
                        self.screen.blit(lettre,(marge_gauche+28,marge_haut+28))
                marge_gauche += 50
                if marge_gauche + 60 > self.position_debut_x_rectangle_2 :
                    marge_haut += 50
                    marge_gauche = 10 + self.position_debut_x_carre
            if element_courant == len(lancer) :
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            SKIN_QUITTER.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_haut += 50
            marge_gauche = 10 + self.position_debut_x_carre
            if element_courant == len(lancer) :
                descr = "Quitter"
            elif element_courant == 0:
                descr = "Item courant"
            else :
                descr = lancer[element_courant].nom
            texte = POLICE20.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))

    def dessine_menu(self,joueur):
        options = joueur.options_menu
        courant = joueur.element_courant
        elements_par_ligne = (self.largeur_exploitable-20)//50 #On veut exactement les même calculs ici que chez le joueur, source potentielle d'erreurs /!\
        elements_par_colone = len(options)//elements_par_ligne
        if len(options)%elements_par_ligne != 0:
            elements_par_colone += 1
        debut = 0
        fin = len(options)
        if elements_par_colone > elements_par_ligne: #On n'a pas la place de tout afficher
            ligne = courant//elements_par_ligne
            if ligne < elements_par_ligne//2:
                fin = elements_par_ligne*elements_par_ligne
            elif ligne < elements_par_colone+elements_par_ligne//2-elements_par_ligne:
                debut = elements_par_ligne*(ligne-elements_par_ligne//2)
                fin = debut+elements_par_ligne*elements_par_colone #colone ou ligne ici /!\
            else:
                debut = elements_par_ligne*(elements_par_colone-elements_par_ligne)

        marge_haut = 10 + self.position_debut_y_rectangles_et_carre
        marge_gauche = 10 + self.position_debut_x_carre
        for i in range(debut,fin):
            if i == courant:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
            elif i == joueur.cible:
                pygame.draw.rect(self.screen,(125,125,125),(marge_gauche-2,marge_haut-2,44,44))
            options[i].get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 50
            if marge_gauche >= self.position_debut_x_carre+self.largeur_exploitable-60:
                marge_haut += 50
                marge_gauche = 10 + self.position_debut_x_carre

    def dessine_menu_alchimie(self,joueur):
        recettes = trouve_skill(joueur.interlocuteur.classe_principale,Skill_alchimie).recettes
        courant = joueur.element_courant

        marge_haut = 10 + self.position_debut_y_rectangles_et_carre
        marge_gauche = 10 + self.position_debut_x_carre

        i=0

        for recette in recettes:
            if i == joueur.cible:
                pygame.draw.rect(self.screen,(255,64,0),(marge_gauche-5,marge_haut-5,10+40*(2*len(recette["ingredients"])+1),50))
                pygame.draw.rect(self.screen,(0,0,0),(marge_gauche-2,marge_haut-2,4+40*(2*len(recette["ingredients"])+1),44))
            elif i == joueur.element_courant:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-5,marge_haut-5,10+40*(2*len(recette["ingredients"])+1),50))
                pygame.draw.rect(self.screen,(0,0,0),(marge_gauche-2,marge_haut-2,4+40*(2*len(recette["ingredients"])+1),44))
            first=True
            for ingredient in recette["ingredients"].keys():
                if first:
                    first=False
                else:
                    SKIN_PLUS.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                    marge_gauche += 40
                eval(ingredient).get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40) #/!\ Peut-être afficher la quantité d'ingrédients plutôt ici ?"
                marge_gauche += 40
            SKIN_EGAL.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 40
            eval(recette["produit"]).get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 40
            marge_gauche = 10 + self.position_debut_x_carre
            marge_haut += 60
            i+=1

    def dessine_menu_cuisine(self,joueur):
        recettes = joueur.objet_interactif.recettes
        courant = joueur.element_courant

        marge_haut = 10 + self.position_debut_y_rectangles_et_carre
        marge_gauche = 10 + self.position_debut_x_carre

        i=0

        for recette in recettes:
            if i == joueur.cible:
                pygame.draw.rect(self.screen,(255,64,0),(marge_gauche-5,marge_haut-5,10+40*(2*len(recette["ingredients"])+1),50))
                pygame.draw.rect(self.screen,(0,0,0),(marge_gauche-2,marge_haut-2,4+40*(2*len(recette["ingredients"])+1),44))
            elif i == joueur.element_courant:
                pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-5,marge_haut-5,10+40*(2*len(recette["ingredients"])+1),50))
                pygame.draw.rect(self.screen,(0,0,0),(marge_gauche-2,marge_haut-2,4+40*(2*len(recette["ingredients"])+1),44))
            first=True
            for ingredient in recette["ingredients"].keys():
                if first:
                    first=False
                else:
                    SKIN_PLUS.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                    marge_gauche += 40
                eval(ingredient).get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40) #/!\ Peut-être afficher la quantité d'ingrédients plutôt ici ?"
                marge_gauche += 40
            SKIN_EGAL.dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 40
            eval(recette["produit"]).get_image().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
            marge_gauche += 40
            marge_gauche = 10 + self.position_debut_x_carre
            marge_haut += 60
            i+=1

    def choix_touche(self,joueur,zones,skills,magies,lancer):
        """phase de choix d'une touche"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_choix_touche(joueur,zones,skills,magies,lancer)
        self.dessine_droite(joueur)
        self.dessine_gauche(joueur)

    def choix_niveau(self,joueur):
        """phase de choix d'un niveau"""
        self.frame += 1
        self.dessine_zones(joueur)

        self.dessine_choix_niveau(joueur)
        self.dessine_droite_choix_niveau(joueur)
        self.dessine_gauche(joueur)

    def dessine_choix_niveau(self,joueur):
        pygame.draw.rect(self.screen,(255,255,255),(self.position_debut_x_carre,self.position_debut_y_rectangles_et_carre,self.hauteur_exploitable,self.hauteur_exploitable))
        if joueur.arbre :
            # On doit afficher les différents choix
            # On aura besoin des choix disponibles (joueur.choix_dispos) et de la largeur de l'affichage (self.hauteur_exploitable), ainsi que la limite gauche (self.position_debut_x_carre)
            # Pour rappel, le carré du centre fait au moins 660 par 660
            # On doit répartir en hauteur le titre, plus jusqu'à dix niveaux de choix (passés présents ou futur), plus le symbole des arbres en bas
            # Avec 20 pixels pour le titre et 40 par niveau, il reste 240 pour les interstices et la racine en bas
            # On va essayer avec 20 par interstice et les 60 restants pour les arbres
            choix = joueur.choix_dispos
            nb_choix = len(choix)
            largeur_choi = 40 + 10 #Un peu petit peut-être ?
            largeur_choix = nb_choix * largeur_choi -10 #On n'a pas besoin de compter de marge à l'extérieur
            marge_gauche = (self.hauteur_exploitable - largeur_choix)/2

            pos_gauche = self.position_debut_x_carre + 5
            pos_haut = self.position_debut_y_rectangles_et_carre + 5

            titre = POLICE20.render("Choix du niveau " + str(joueur.classe_principale.niveau),True,(0,0,0))
            self.screen.blit(titre,(pos_gauche,pos_haut))

            pos_gauche += marge_gauche - 5
            pos_haut += 20
            pos_centre = self.position_debut_x_carre + self.hauteur_exploitable/2

            if joueur.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT,ESSENCE_MAGIQUE]: #La feuille du troisième niveau (et toutes les impaires) sera à droite
                if joueur.niveau%2 == 1: #Le niveau du joueur n'a pas encore été incrémenté, i.e. si on choisi la récompense du niveau 3, joueur.niveau vaut 2
                    gauche = True
                else:
                    gauche = False
            else:
                if joueur.niveau%2 == 1:
                    gauche = False
                else:
                    gauche = True

            bourg_gauche = self.position_debut_x_carre + 210

            if joueur.niveau < 2 :
                bourgeons = []
            elif nb_choix == 1:
                if gauche :
                    bourgeons = [SKIN_BOURGEON_GAUCHE_CENTRE]
                else:
                    bourgeons = [SKIN_BOURGEON_DROITE_CENTRE]
            elif nb_choix == 2:
                if gauche :
                    bourgeons = [SKIN_BOURGEON_GAUCHE_CENTRE_GAUCHE,SKIN_BOURGEON_GAUCHE_CENTRE_DROIT]
                else:
                    bourgeons = [SKIN_BOURGEON_DROITE_CENTRE_GAUCHE,SKIN_BOURGEON_DROITE_CENTRE_DROIT]
            elif nb_choix == 3:
                if gauche :
                    bourgeons = [SKIN_BOURGEON_GAUCHE_GAUCHE,SKIN_BOURGEON_GAUCHE_CENTRE,SKIN_BOURGEON_GAUCHE_DROITE]
                else:
                    bourgeons = [SKIN_BOURGEON_DROITE_GAUCHE,SKIN_BOURGEON_DROITE_CENTRE,SKIN_BOURGEON_DROITE_DROITE]
            elif nb_choix == 4:
                if gauche :
                    bourgeons = [SKIN_BOURGEON_GAUCHE_LOIN_GAUCHE,SKIN_BOURGEON_GAUCHE_CENTRE_GAUCHE,SKIN_BOURGEON_GAUCHE_CENTRE_DROIT,SKIN_BOURGEON_GAUCHE_LOIN_DROIT]
                else:
                    bourgeons = [SKIN_BOURGEON_DROITE_LOIN_GAUCHE,SKIN_BOURGEON_DROITE_CENTRE_GAUCHE,SKIN_BOURGEON_DROITE_CENTRE_DROIT,SKIN_BOURGEON_DROITE_LOIN_DROIT]
            elif nb_choix == 5:
                if gauche :
                    bourgeons = [SKIN_BOURGEON_GAUCHE_EXTREME_GAUCHE,SKIN_BOURGEON_GAUCHE_GAUCHE,SKIN_BOURGEON_GAUCHE_CENTRE,SKIN_BOURGEON_GAUCHE_DROITE,SKIN_BOURGEON_GAUCHE_EXTREME_DROITE]
                else:
                    bourgeons = [SKIN_BOURGEON_DROITE_EXTREME_GAUCHE,SKIN_BOURGEON_DROITE_GAUCHE,SKIN_BOURGEON_DROITE_CENTRE,SKIN_BOURGEON_DROITE_DROITE,SKIN_BOURGEON_DROITE_EXTREME_DROITE]
            # On va être optimiste et supposer qu'on n'aura jamais plus de 5 choix (jusqu'à 4 normaux, et encore c'est rare, et un secret, ce qui est encore plus rare).

            for niveau in range(10,0,-1):

                if niveau == joueur.niveau + 1 :
                    #C'est le niveau du choix courant !
                    for i in range(nb_choix):
                        if i == joueur.courant :
                            if joueur.etage == 0:
                                pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                            elif joueur.etage == 1:
                                pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44)) #On essaye de faire un truc un peu rouge
                        if choix[i] == REGEN_HP:
                            skin = SKIN_BOOST_REGEN_HP
                        elif choix[i] == REGEN_MP:
                            skin = SKIN_BOOST_REGEN_MP
                        elif choix[i] == DEFENSE:
                            skin = SKIN_SKILL_DEFENSE
                        elif choix[i] == LANCER:
                            skin = SKIN_SKILL_LANCER
                        elif choix[i] == ESSENCE_MAGIQUE:
                            skin = SKIN_SKILL_ESSENCE_MAGIQUE
                        elif choix[i] == MAGIE_INFINIE:
                            skin = SKIN_SKILL_MAGIE_INFINIE
                        elif choix[i] == BOOST_PRIORITE:
                            skin = SKIN_BOOST_PRIORITE
                        elif choix[i] == BOOST_PV:
                            skin = SKIN_BOOST_PV
                        elif choix[i] == BOOST_DE_PRIORITE_D_ATTAQUE:
                            skin = SKIN_BOOST_DE_PRIORITE_D_ATTAQUE
                        elif choix[i] == CREATION_FLECHES:
                            skin = SKIN_SKILL_CREATION_FLECHES
                        elif choix[i] == SORT_ACCELERATION:
                            skin = SKIN_MAGIE_ACCELERATION
                        elif choix[i] == BOOST_AURA:
                            skin = SKIN_SKILL_BOOST_AURA
                        elif choix[i] == BOOST_PM:
                            skin = SKIN_BOOST_PM
                        elif choix[i] == ONDE_DE_CHOC:
                            skin = SKIN_MAGIE_ONDE_DE_CHOC
                        elif choix[i] == SORT_DE_SOIN_SUPERIEUR:
                            skin = SKIN_MAGIE_SOIN_SUPERIEUR
                        elif choix[i] == ENCHANTEMENT_FORCE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_FORCE
                        elif choix[i] == PROJECTION_ENERGIE:
                            skin = SKIN_MAGIE_JET_DE_MANA
                        elif choix[i] == ECRASEMENT:
                            skin = SKIN_SKILL_ECRASEMENT
                        elif choix[i] == OBSERVATION:
                            skin = SKIN_SKILL_OBSERVATION
                        elif choix[i] == MANIPULATION_EPEE:
                            skin = SKIN_SKILL_MANIPULATION_EPEE
                        elif choix[i] == BOOST_PORTEE:
                            skin = SKIN_BOOST_PORTEE
                        elif choix[i] == SORT_VISION:
                            skin = SKIN_MAGIE_VISION
                        elif choix[i] == CREATION_EXPLOSIF:
                            skin = SKIN_SKILL_CREATION_EXPLOSIF
                        elif choix[i] == ELEMENTALISTE:
                            skin = SKIN_ELEMENTALISTE
                        elif choix[i] == RAYON_THERMIQUE:
                            skin = SKIN_MAGIE_LASER
                        elif choix[i] == ENCHANTEMENT_DEFENSE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_DEFENSE
                        elif choix[i] == REGEN_PM:
                            skin = SKIN_MAGIE_RESTAURATION_PM
                        elif choix[i] == ANALYSE:
                            skin = SKIN_SKILL_ANALYSE
                        elif choix[i] == VOL:
                            skin = SKIN_SKILL_VOL
                        elif choix[i] == BOOST_ATTAQUE_EPEE:
                            skin = SKIN_SKILL_BOOST_EPEE
                        elif choix[i] == FLECHE_PERCANTE:
                            skin = SKIN_AJOUT_FLECHE_PERCANTE
                        elif choix[i] == FLECHE_EXPLOSIVE:
                            skin = SKIN_AJOUT_FLECHE_EXPLOSIVE
                        elif choix[i] == IMMORTALITE:
                            skin = SKIN_SKILL_IMMORTALITE
                        elif choix[i] == BOOST_DEGATS_MAGIQUES:
                            skin = SKIN_BOOST_DEGATS_MAGIQUES
                        elif choix[i] == BOOST_PRIORITE_MAGIQUE:
                            skin = SKIN_SKILL_BOOST_PRIORITE_MAGIQUE
                        elif choix[i] == ENCHANTEMENT_FAIBLESSE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE
                        elif choix[i] == EPEISTE:
                            skin = SKIN_EPEISTE
                        elif choix[i] == BOOST_RESTAURATIONS:
                            skin = SKIN_SKILL_BOOST_RESTAURATIONS
                        elif choix[i] == MANIPULATION_BOUCLIER:
                            skin = SKIN_SKILL_MANIPULATION_BOUCLIER
                        elif choix[i] == BOOST_PRIORITE_OBSERVATION:
                            skin = SKIN_BOOST_PRIORITE_OBSERVATION
                        elif choix[i] == SORT_AUTO_SOIN:
                            skin = SKIN_MAGIE_AUTO_SOIN
                        elif choix[i] == BOOST_DEGATS_FLECHES:
                            skin = SKIN_SKILL_BOOST_DEGATS_FLECHES
                        elif choix[i] == CHARGE_LOURDE:
                            skin = SKIN_AJOUT_CHARGE_LOURDE
                        elif choix[i] == CHARGE_ETENDUE:
                            skin = SKIN_AJOUT_CHARGE_ETENDUE
                        elif choix[i] == INHUMANITE:
                            skin = SKIN_INHUMANITE
                        elif choix[i] == MAGICIEN:
                            skin = SKIN_MAGICIEN
                        elif choix[i] == BOOST_DE_PORTEE:
                            skin = SKIN_BOOST_PORTEE_MAGIE
                        elif choix[i] == BOOST_SOIN:
                            skin = SKIN_SKILL_BOOST_SOIN
                        elif choix[i] == SORT_DE_VUE:
                            skin = SKIN_MAGIE_VISION #Flemme de redessiner, pas d'inspiration
                        elif choix[i] == VOL_PRIORITE:
                            skin = SKIN_SKILL_VOL_PRIORITE
                        elif choix[i] == BOOST_ATTAQUE_LANCE:
                            skin = SKIN_SKILL_BOOST_LANCE
                        elif choix[i] == BOOST_PRIORITE_FLECHES:
                            skin = SKIN_SKILL_BOOST_PRIORITE_FLECHE
                        elif choix[i] == ARTIFICIER:
                            skin = SKIN_ARTIFICIER
                        elif choix[i] == FANTOME:
                            skin = SKIN_FANTOME
                        elif choix[i] == INSTAKILL:
                            skin = SKIN_SKILL_INSTAKILL
                        elif choix[i] == JET_DE_MANA:
                            skin = SKIN_MAGIE_JET_DE_MANA
                        elif choix[i] == ENCHANTEMENT_RENFORCEMENT:
                            skin = SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT
                        elif choix[i] == SORT_DE_PROTECTION:
                            skin = SKIN_MAGIE_PROTECTION
                        elif choix[i] == BOOST_ATTAQUE:
                            skin = SKIN_BOOST_ATTAQUE
                        elif choix[i] == ARCHER:
                            skin = SKIN_ARCHER
                        elif choix[i] == FLECHE_FANTOME:
                            skin = SKIN_AJOUT_FLECHE_FANTOME
                        elif choix[i] == BOOST_DEGAT:
                            skin = SKIN_BOOST_FORCE
                        elif choix[i] == NECROMANCIEN:
                            skin = SKIN_NECROMANCIEN
                        elif choix[i] == ENCHANTEUR:
                            skin = SKIN_ENCHANTEUR
                        elif choix[i] == SOUTIEN:
                            skin = SKIN_SOUTIEN
                        elif choix[i] == BOOST_PRIORITE_DEPLACEMENT:
                            skin = SKIN_BOOST_PRIORITE_DEPLACEMENT
                        elif choix[i] == BOOST_PRIORITE_ANALYSE:
                            skin = SKIN_BOOST_PRIORITE_ANALYSE
                        elif choix[i] == BOOST_PRIORITE_EXPLOSIF:
                            skin = SKIN_BOOST_PRIORITE_EXPLOSIFS
                        elif choix[i] == BOOST_VITESSE_EXPLOSIF:
                            skin = SKIN_BOOST_VITESSE_EXPLOSIFS
                        elif choix[i] == BOOST_PRIORITE_AURA:
                            skin = SKIN_SKILL_BOOST_PRIORITE_AURA
                        elif choix[i] == AURA_MORTELLE:
                            skin = SKIN_SKILL_AURA_MORTELLE
                        elif choix[i] == ASSASSIN:
                            skin = SKIN_ASSASSIN
                        elif choix[i] == BOOST_DE_ZONE_DE_RESTAURATION:
                            skin = SKIN_SKILL_BOOST_ZONE_RESTAURATION
                        elif choix[i] == ANGE:
                            skin = SKIN_ANGE
                        elif choix[i] == ENCHANTEMENT_ROUILLE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_ROUILLE
                        elif choix[i] == MANIPULATION_ARME:
                            skin = SKIN_SKILL_MANIPULATION_ARME
                        elif choix[i] == FLECHES_LOURDE_LEGERE:
                            skin = SKIN_AJOUT_FLECHES_LOURDE_LEGERE
                        elif choix[i] == BOOST_PORTEE_EXPLOSIFS:
                            skin = SKIN_BOOST_PORTEE_EXPLOSIFS
                        elif choix[i] == ECLAIR_NOIR:
                            skin = SKIN_MAGIE_ECLAIR_NOIR
                        elif choix[i] == BOOST_DEGATS_PROJECTILES:
                            skin = SKIN_SKILL_BOOST_DEGATS_PROJECTILES
                        elif choix[i] == BOOST_ENCHANTEMENT:
                            skin = SKIN_SKILL_BOOST_ENCHANTEMENT
                        elif choix[i] == RESURECTION:
                            skin = SKIN_MAGIE_RESURECTION
                        elif choix[i] == ENCHANTEMENT_DEFENSIF:
                            skin = SKIN_MAGIE_ENCHANTEMENT_DEFENSIF
                        else:
                            skin = SKIN_MYSTERE
                        #Je fais l'impasse sur les autres pour l'instant
                        skin.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
                        if joueur.niveau >= 2:
                            bourgeons[i].dessine_toi(self.screen,(bourg_gauche,pos_haut - 10))
                        pos_gauche += largeur_choi
                    if joueur.niveau == 0 :
                        SKIN_BOURGEONS.dessine_toi(self.screen,(pos_centre - 50,pos_haut - 10))
                    elif joueur.niveau == 1 :
                        if joueur.choix_niveaux[CLASSIQUE][1] == MAGIE:
                            SKIN_BOURGEON_MAGIQUE.dessine_toi(self.screen,(pos_centre - 50,pos_haut - 10))
                        else :
                            SKIN_BOURGEON_PHYSIQUE.dessine_toi(self.screen,(pos_centre - 50,pos_haut - 10))


                elif niveau <= joueur.niveau :
                    choi = joueur.choix_niveaux[CLASSIQUE][niveau]
                    if niveau == 1:

                        if choi == PHYSIQUE:
                            skin_feuille = SKIN_FEUILLE_PHYSIQUE
                            skin = SKIN_BOOST_REGEN_HP

                        elif choi == PHYSIQUE_PAR_DEFAUT:
                            skin_feuille = SKIN_FEUILLE_PHYSIQUE_PAR_DEFAUT
                            skin = SKIN_VIDE

                        elif choi == MAGIE:
                            skin_feuille = SKIN_FEUILLE_MAGIE
                            skin = SKIN_BOOST_REGEN_MP

                        else:
                            print("Je ne reconnais pas ce choix du niveau 1 : " + str(choi))

                        skin_feuille.dessine_toi(self.screen,(pos_centre-50,pos_haut-10))

                    elif niveau == 2:

                        if choi == DEFENSE:
                            skin_feuille = SKIN_FEUILLE_DEFENSE
                            skin = SKIN_SKILL_DEFENSE

                        elif choi == DEFENSE_PAR_DEFAUT:
                            skin_feuille = SKIN_FEUILLE_DEFENSE_PAR_DEFAUT
                            skin = SKIN_VIDE

                        elif choi == LANCER:
                            skin_feuille = SKIN_FEUILLE_LANCER
                            skin = SKIN_SKILL_LANCER

                        elif choi == ESSENCE_MAGIQUE:
                            skin_feuille = SKIN_FEUILLE_ESSENCE_MAGIQUE
                            skin = SKIN_SKILL_ESSENCE_MAGIQUE

                        elif choi == MAGIE_INFINIE:
                            skin_feuille = SKIN_FEUILLE_MAGIE_INFINIE
                            skin = SKIN_SKILL_MAGIE_INFINIE

                        elif choi == MAGIE_INFINIE_PAR_DEFAUT:
                            skin_feuille = SKIN_FEUILLE_MAGIE_INFINIE_PAR_DEFAUT
                            skin = SKIN_VIDE

                        else:
                            print("Je ne reconnais pas ce choix du niveau 2 : " + str(choi))

                        skin_feuille.dessine_toi(self.screen,(pos_centre-50,pos_haut-10))

                    else:
                        gauche = not gauche
                        if gauche :
                            if choi == None:
                                skin_feuille = SKIN_FEUILLE_GAUCHE_PAR_DEFAUT
                            else:
                                skin_feuille = SKIN_FEUILLE_GAUCHE
                        else :
                            if choi == None:
                                skin_feuille = SKIN_FEUILLE_DROITE_PAR_DEFAUT
                            else:
                                skin_feuille = SKIN_FEUILLE_DROITE

                        if choi == BOOST_PRIORITE:
                            skin = SKIN_BOOST_PRIORITE
                        elif choi == DEFENSE:
                            skin = SKIN_SKILL_DEFENSE
                        elif choi == BOOST_PV:
                            skin = SKIN_BOOST_PV
                        elif choi == BOOST_DE_PRIORITE_D_ATTAQUE:
                            skin = SKIN_BOOST_DE_PRIORITE_D_ATTAQUE
                        elif choi == CREATION_FLECHES:
                            skin = SKIN_SKILL_CREATION_FLECHES
                        elif choi == SORT_ACCELERATION:
                            skin = SKIN_MAGIE_ACCELERATION
                        elif choi == BOOST_AURA:
                            skin = SKIN_SKILL_BOOST_AURA
                        elif choi == BOOST_PM:
                            skin = SKIN_BOOST_PM
                        elif choi == ONDE_DE_CHOC:
                            skin = SKIN_MAGIE_ONDE_DE_CHOC
                        elif choi == SORT_DE_SOIN_SUPERIEUR:
                            skin = SKIN_MAGIE_SOIN_SUPERIEUR
                        elif choi == ENCHANTEMENT_FORCE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_FORCE
                        elif choi == PROJECTION_ENERGIE:
                            skin = SKIN_MAGIE_JET_DE_MANA
                        elif choi == ECRASEMENT:
                            skin = SKIN_SKILL_ECRASEMENT
                        elif choi == OBSERVATION:
                            skin = SKIN_SKILL_OBSERVATION
                        elif choi == MANIPULATION_EPEE:
                            skin = SKIN_SKILL_MANIPULATION_EPEE
                        elif choi == BOOST_PORTEE:
                            skin = SKIN_BOOST_PORTEE
                        elif choi == SORT_VISION:
                            skin = SKIN_MAGIE_VISION
                        elif choi == CREATION_EXPLOSIF:
                            skin = SKIN_SKILL_CREATION_EXPLOSIF
                        elif choi == ELEMENTALISTE:
                            skin = SKIN_ELEMENTALISTE
                        elif choi == RAYON_THERMIQUE:
                            skin = SKIN_MAGIE_LASER
                        elif choi == ENCHANTEMENT_DEFENSE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_DEFENSE
                        elif choi == REGEN_PM:
                            skin = SKIN_MAGIE_RESTAURATION_PM
                        elif choi == ANALYSE:
                            skin = SKIN_SKILL_ANALYSE
                        elif choi == VOL:
                            skin = SKIN_SKILL_VOL
                        elif choi == BOOST_ATTAQUE_EPEE:
                            skin = SKIN_SKILL_BOOST_EPEE
                        elif choi == FLECHE_PERCANTE:
                            skin = SKIN_AJOUT_FLECHE_PERCANTE
                        elif choi == FLECHE_EXPLOSIVE:
                            skin = SKIN_AJOUT_FLECHE_EXPLOSIVE
                        elif choi == IMMORTALITE:
                            skin = SKIN_SKILL_IMMORTALITE
                        elif choi == BOOST_DEGATS_MAGIQUES:
                            skin = SKIN_SKILL_BOOST_DEGATS_MAGIQUES
                        elif choi == BOOST_PRIORITE_MAGIQUE:
                            skin = SKIN_SKILL_BOOST_PRIORITE_MAGIQUE
                        elif choi == ENCHANTEMENT_FAIBLESSE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE
                        elif choi == EPEISTE:
                            skin = SKIN_EPEISTE
                        elif choi == BOOST_RESTAURATIONS:
                            skin = SKIN_SKILL_BOOST_RESTAURATIONS
                        elif choi == MANIPULATION_BOUCLIER:
                            skin = SKIN_SKILL_MANIPULATION_BOUCLIER
                        elif choi == BOOST_PRIORITE_OBSERVATION:
                            skin = SKIN_BOOST_PRIORITE_OBSERVATION
                        elif choi == SORT_AUTO_SOIN:
                            skin = SKIN_MAGIE_AUTO_SOIN
                        elif choi == BOOST_DEGATS_FLECHES:
                            skin = SKIN_SKILL_BOOST_DEGATS_FLECHES
                        elif choi == CHARGE_LOURDE:
                            skin = SKIN_AJOUT_CHARGE_LOURDE
                        elif choi == CHARGE_ETENDUE:
                            skin = SKIN_AJOUT_CHARGE_ETENDUE
                        elif choi == INHUMANITE:
                            skin = SKIN_INHUMANITE
                        elif choi == MAGICIEN:
                            skin = SKIN_MAGICIEN
                        elif choi == BOOST_DE_PORTEE:
                            skin = SKIN_BOOST_PORTEE_MAGIE
                        elif choi == BOOST_SOIN:
                            skin = SKIN_SKILL_BOOST_SOIN
                        elif choi == SORT_DE_VUE:
                            skin = SKIN_MAGIE_VISION #Flemme de redessiner, pas d'inspiration
                        elif choi == VOL_PRIORITE:
                            skin = SKIN_SKILL_VOL_PRIORITE
                        elif choi == BOOST_ATTAQUE_LANCE:
                            skin = SKIN_SKILL_BOOST_LANCE
                        elif choi == BOOST_PRIORITE_FLECHES:
                            skin = SKIN_SKILL_BOOST_PRIORITE_FLECHE
                        elif choi == ARTIFICIER:
                            skin = SKIN_ARTIFICIER
                        elif choi == FANTOME:
                            skin = SKIN_FANTOME
                        elif choi == INSTAKILL:
                            skin = SKIN_SKILL_INSTAKILL
                        elif choi == JET_DE_MANA:
                            skin = SKIN_MAGIE_JET_DE_MANA
                        elif choi == ENCHANTEMENT_RENFORCEMENT:
                            skin = SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT
                        elif choi == SORT_DE_PROTECTION:
                            skin = SKIN_MAGIE_PROTECTION
                        elif choi == BOOST_ATTAQUE:
                            skin = SKIN_BOOST_ATTAQUE
                        elif choi == ARCHER:
                            skin = SKIN_ARCHER
                        elif choi == FLECHE_FANTOME:
                            skin = SKIN_AJOUT_FLECHE_FANTOME
                        elif choi == BOOST_DEGAT:
                            skin = SKIN_BOOST_FORCE
                        elif choi == NECROMANCIEN:
                            skin = SKIN_NECROMANCIEN
                        elif choi == ENCHANTEUR:
                            skin = SKIN_ENCHANTEUR
                        elif choi == SOUTIEN:
                            skin = SKIN_SOUTIEN
                        elif choi == BOOST_PRIORITE_DEPLACEMENT:
                            skin = SKIN_BOOST_PRIORITE_DEPLACEMENT
                        elif choi == BOOST_PRIORITE_ANALYSE:
                            skin = SKIN_BOOST_PRIORITE_ANALYSE
                        elif choi == BOOST_PRIORITE_EXPLOSIF:
                            skin = SKIN_SKILL_BOOST_PRIORITE_EXPLOSIFS
                        elif choi == BOOST_VITESSE_EXPLOSIF:
                            skin = SKIN_SKILL_BOOST_VITESSE_EXPLOSIFS
                        elif choi == BOOST_PRIORITE_AURA:
                            skin = SKIN_SKILL_BOOST_PRIORITE_AURA
                        elif choi == AURA_MORTELLE:
                            skin = SKIN_SKILL_AURA_MORTELLE
                        elif choi == ASSASSIN:
                            skin = SKIN_ASSASSIN
                        elif choi == BOOST_DE_ZONE_DE_RESTAURATION:
                            skin = SKIN_SKILL_BOOST_ZONE_RESTAURATION
                        elif choi == ANGE:
                            skin = SKIN_ANGE
                        elif choi == ENCHANTEMENT_ROUILLE:
                            skin = SKIN_MAGIE_ENCHANTEMENT_ROUILLE
                        elif choi == MANIPULATION_ARME:
                            skin = SKIN_SKILL_MANIPULATION_ARME
                        elif choi == FLECHES_LOURDE_LEGERE:
                            skin = SKIN_AJOUT_FLECHES_LOURDE_LEGERE
                        elif choi == BOOST_PORTEE_EXPLOSIFS:
                            skin = SKIN_BOOST_PORTEE_EXPLOSIFS
                        elif choi == ECLAIR_NOIR:
                            skin = SKIN_MAGIE_ECLAIR_NOIR
                        elif choi == BOOST_DEGATS_PROJECTILES:
                            skin = SKIN_SKILL_BOOST_DEGATS_PROJECTILES
                        elif choi == BOOST_ENCHANTEMENT:
                            skin = SKIN_SKILL_BOOST_ENCHANTEMENT
                        elif choi == RESURECTION:
                            skin = SKIN_MAGIE_RESURECTION
                        elif choi == ENCHANTEMENT_DEFENSIF:
                            skin = SKIN_MAGIE_ENCHANTEMENT_DEFENSIF
                        else:
                            skin = SKIN_MYSTERE
                        skin_feuille.dessine_toi(self.screen,(pos_centre-30,pos_haut-10))
                    skin.dessine_toi(self.screen,(pos_centre - 10, pos_haut + 10),20)

                pos_haut += 60

            SKIN_RACINE_CLASSIQUE.dessine_toi(self.screen,(pos_centre-50,pos_haut-10))

        else :
            # Pour rappel, le carré du centre fait au moins 660 par 660
            # On doit répartir en hauteur :
            #   - Le titre (20px)
            #   - Le choix élémental (40px)
            #   - Le choix aura (40px)
            #   - Les choix affinité et magie (40px)
            #   - Le symbole de l'arbre élémental (avec indice de l'autre arbre en dessous, beaucoup de px)
            # Soit 140 obligés, il reste 420 pour le reste, même avec 120 pour les arbres il nous reste 100 pour chaque branche !
            # On doit répartir en largeur, sur la ligne la plus chargée, les affinités et magies de tous les éléments, soit 8 choix (40px)
            # Soit 320 obligés, il reste 340 pour les marges, dont 20 entre les éléments et à l'extérieur, et 60 entre l'affinité et la magie d'un même élément
            # On va garder l'arbre à peu près identique quelque soit la taille de l'écran :

            pos_gauche = self.position_debut_x_carre + 5
            pos_haut = self.position_debut_y_rectangles_et_carre + 5
            marge_gauche = self.position_debut_x_carre + (self.hauteur_exploitable - 660)/2
            marge_haut = self.position_debut_y_rectangles_et_carre

            titre = POLICE20.render("Choix élémentaire",True,(0,0,0))
            self.screen.blit(titre,(pos_gauche,pos_haut))

            #Les dessins des arbres :
            #D'abord, la terre

            if affinite_terre in joueur.choix_elems and magie_terre in joueur.choix_elems :
                #On n'a encore rien pris sur l'arbre de terre, et on peut prendre la magie et l'affinité
                skin_terre = SKIN_BOURGEONS_TERRE

            elif aura_terre in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][TERRE][affinite]:
                #On a pris l'affinité, et on peut prendre l'aura :
                skin_terre = SKIN_BOURGEON_TERRE_AFF

            elif aura_terre in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][TERRE][MAGIE]:
                #On a pris la magie, et on peut prendre l'aura :
                skin_terre = SKIN_BOURGEON_TERRE_MAGIE

            elif affinite_terre in joueur.choix_elems :
                #On a pris l'aura et la magie, et on peut prendre l'affinité :
                skin_terre = SKIN_BOURGEON_TERRE_REAFF

            elif magie_terre in joueur.choix_elems :
                #On a pris l'aura et l'affinité, et on peut prendre la magie
                skin_terre = SKIN_BOURGEON_TERRE_REMAGIE

            elif elemental_terre in joueur.choix_elems and joueur.prem_terre == affinite:
                #On a pris l'affinité, puis l'aura et la magie, et on peut prendre l'élémental
                skin_terre = SKIN_BOURGEON_TERRE_ELEM_AFF

            elif elemental_terre in joueur.choix_elems and joueur.prem_terre == MAGIE:
                #On a pris la magie, puis l'aura et l'affinité, et on peut prendre l'élémental
                skin_terre = SKIN_BOURGEON_TERRE_ELEM_MAGIE

            #Si aucun des précédents n'était le bon, on n'a pas de choix disponible dans l'arbre de terre. Ça n'empêche pas d'avoir déjà fait des choix !
            elif joueur.choix_niveaux[ELEMENTAL][TERRE][elemental] and joueur.prem_terre == affinite:
                #On a tout pris, en commençant par l'affinité
                skin_terre = SKIN_TERRE_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][elemental] and joueur.prem_terre == MAGIE:
                #On a tout pris, en commençant par la magie
                skin_terre = SKIN_TERRE_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][MAGIE] and joueur.prem_terre == affinite:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_terre = SKIN_TERRE_QUASI_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][affinite] and joueur.prem_terre == MAGIE:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_terre = SKIN_TERRE_QUASI_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][aura] and joueur.prem_terre == affinite:
                #On est allé jusqu'à l'aura, en commençant par l'affinité
                skin_terre = SKIN_TERRE_AURA_AFF

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][aura] and joueur.prem_terre == MAGIE:
                #On est allé jusqu'à l'aura, en commençant par la magie
                skin_terre = SKIN_TERRE_AURA_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][affinite]:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_terre = SKIN_TERRE_AFF

            elif joueur.choix_niveaux[ELEMENTAL][TERRE][MAGIE]:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_terre = SKIN_TERRE_MAGIE

            else :
                #On n'a rien pris dans l'arbre de la terre, mais on ne peut rien prendre
                skin_terre = SKIN_TERRE_VIDE
                
            skin_terre.dessine_toi(self.screen,(marge_gauche,marge_haut))

            
            #Ensuite, le feu

            if affinite_feu in joueur.choix_elems and magie_feu in joueur.choix_elems :
                #On n'a encore rien pris sur l'arbre de feu, et on peut prendre la magie et l'affinité
                skin_feu = SKIN_BOURGEONS_FEU

            elif aura_feu in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][FEU][affinite]:
                #On a pris l'affinité, et on peut prendre l'aura :
                skin_feu = SKIN_BOURGEON_FEU_AFF

            elif aura_feu in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][FEU][MAGIE]:
                #On a pris la magie, et on peut prendre l'aura :
                skin_feu = SKIN_BOURGEON_FEU_MAGIE

            elif affinite_feu in joueur.choix_elems :
                #On a pris l'aura et la magie, et on peut prendre l'affinité :
                skin_feu = SKIN_BOURGEON_FEU_REAFF

            elif magie_feu in joueur.choix_elems :
                #On a pris l'aura et l'affinité, et on peut prendre la magie
                skin_feu = SKIN_BOURGEON_FEU_REMAGIE

            elif elemental_feu in joueur.choix_elems and joueur.prem_feu == affinite:
                #On a pris l'affinité, puis l'aura et la magie, et on peut prendre l'élémental
                skin_feu = SKIN_BOURGEON_FEU_ELEM_AFF

            elif elemental_feu in joueur.choix_elems and joueur.prem_feu == MAGIE:
                #On a pris la magie, puis l'aura et l'affinité, et on peut prendre l'élémental
                skin_feu = SKIN_BOURGEON_FEU_ELEM_MAGIE

            #Si aucun des précédents n'était le bon, on n'a pas de choix disponible dans l'arbre de feu. Ça n'empêche pas d'avoir déjà fait des choix !
            elif joueur.choix_niveaux[ELEMENTAL][FEU][elemental] and joueur.prem_feu == affinite:
                #On a tout pris, en commençant par l'affinité
                skin_feu = SKIN_FEU_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][FEU][elemental] and joueur.prem_feu == MAGIE:
                #On a tout pris, en commençant par la magie
                skin_feu = SKIN_FEU_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][FEU][MAGIE] and joueur.prem_feu == affinite:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_feu = SKIN_FEU_QUASI_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][FEU][affinite] and joueur.prem_feu == MAGIE:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_feu = SKIN_FEU_QUASI_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][FEU][aura] and joueur.prem_feu == affinite:
                #On est allé jusqu'à l'aura, en commençant par l'affinité
                skin_feu = SKIN_FEU_AURA_AFF

            elif joueur.choix_niveaux[ELEMENTAL][FEU][aura] and joueur.prem_feu == MAGIE:
                #On est allé jusqu'à l'aura, en commençant par la magie
                skin_feu = SKIN_FEU_AURA_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][FEU][affinite]:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_feu = SKIN_FEU_AFF

            elif joueur.choix_niveaux[ELEMENTAL][FEU][MAGIE]:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_feu = SKIN_FEU_MAGIE

            else :
                #On n'a rien pris dans l'arbre du feu, mais on ne peut rien prendre
                skin_feu = SKIN_FEU_VIDE
                
            skin_feu.dessine_toi(self.screen,(marge_gauche,marge_haut))

            
            #Puis la glace

            if affinite_glace in joueur.choix_elems and magie_glace in joueur.choix_elems :
                #On n'a encore rien pris sur l'arbre de glace, et on peut prendre la magie et l'affinité
                skin_glace = SKIN_BOURGEONS_GLACE

            elif aura_glace in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][GLACE][affinite]:
                #On a pris l'affinité, et on peut prendre l'aura :
                skin_glace = SKIN_BOURGEON_GLACE_AFF

            elif aura_glace in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][GLACE][MAGIE]:
                #On a pris la magie, et on peut prendre l'aura :
                skin_glace = SKIN_BOURGEON_GLACE_MAGIE

            elif affinite_glace in joueur.choix_elems :
                #On a pris l'aura et la magie, et on peut prendre l'affinité :
                skin_glace = SKIN_BOURGEON_GLACE_REAFF

            elif magie_glace in joueur.choix_elems :
                #On a pris l'aura et l'affinité, et on peut prendre la magie
                skin_glace = SKIN_BOURGEON_GLACE_REMAGIE

            elif elemental_glace in joueur.choix_elems and joueur.prem_glace == affinite:
                #On a pris l'affinité, puis l'aura et la magie, et on peut prendre l'élémental
                skin_glace = SKIN_BOURGEON_GLACE_ELEM_AFF

            elif elemental_glace in joueur.choix_elems and joueur.prem_glace == MAGIE:
                #On a pris la magie, puis l'aura et l'affinité, et on peut prendre l'élémental
                skin_glace = SKIN_BOURGEON_GLACE_ELEM_MAGIE

            #Si aucun des précédents n'était le bon, on n'a pas de choix disponible dans l'arbre de glace. Ça n'empêche pas d'avoir déjà fait des choix !
            elif joueur.choix_niveaux[ELEMENTAL][GLACE][elemental] and joueur.prem_glace == affinite:
                #On a tout pris, en commençant par l'affinité
                skin_glace = SKIN_GLACE_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][elemental] and joueur.prem_glace == MAGIE:
                #On a tout pris, en commençant par la magie
                skin_glace = SKIN_GLACE_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][MAGIE] and joueur.prem_glace == affinite:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_glace = SKIN_GLACE_QUASI_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][affinite] and joueur.prem_glace == MAGIE:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_glace = SKIN_GLACE_QUASI_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][aura] and joueur.prem_glace == affinite:
                #On est allé jusqu'à l'aura, en commençant par l'affinité
                skin_glace = SKIN_GLACE_AURA_AFF

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][aura] and joueur.prem_glace == MAGIE:
                #On est allé jusqu'à l'aura, en commençant par la magie
                skin_glace = SKIN_GLACE_AURA_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][affinite]:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_glace = SKIN_GLACE_AFF

            elif joueur.choix_niveaux[ELEMENTAL][GLACE][MAGIE]:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_glace = SKIN_GLACE_MAGIE

            else :
                #On n'a rien pris dans l'arbre de la glace, mais on ne peut rien prendre
                skin_glace = SKIN_GLACE_VIDE
                
            skin_glace.dessine_toi(self.screen,(marge_gauche,marge_haut))

            
            #Enfin, l'ombre

            if affinite_ombre in joueur.choix_elems and magie_ombre in joueur.choix_elems :
                #On n'a encore rien pris sur l'arbre d'ombre, et on peut prendre la magie et l'affinité
                skin_ombre = SKIN_BOURGEONS_OMBRE

            elif aura_ombre in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][OMBRE][affinite]:
                #On a pris l'affinité, et on peut prendre l'aura :
                skin_ombre = SKIN_BOURGEON_OMBRE_AFF

            elif aura_ombre in joueur.choix_elems and joueur.choix_niveaux[ELEMENTAL][OMBRE][MAGIE]:
                #On a pris la magie, et on peut prendre l'aura :
                skin_ombre = SKIN_BOURGEON_OMBRE_MAGIE

            elif affinite_ombre in joueur.choix_elems :
                #On a pris l'aura et la magie, et on peut prendre l'affinité :
                skin_ombre = SKIN_BOURGEON_OMBRE_REAFF

            elif magie_ombre in joueur.choix_elems :
                #On a pris l'aura et l'affinité, et on peut prendre la magie
                skin_ombre = SKIN_BOURGEON_OMBRE_REMAGIE

            elif elemental_ombre in joueur.choix_elems and joueur.prem_ombre == affinite:
                #On a pris l'affinité, puis l'aura et la magie, et on peut prendre l'élémental
                skin_ombre = SKIN_BOURGEON_OMBRE_ELEM_AFF

            elif elemental_ombre in joueur.choix_elems and joueur.prem_ombre == MAGIE:
                #On a pris la magie, puis l'aura et l'affinité, et on peut prendre l'élémental
                skin_ombre = SKIN_BOURGEON_OMBRE_ELEM_MAGIE

            #Si aucun des précédents n'était le bon, on n'a pas de choix disponible dans l'arbre d'ombre. Ça n'empêche pas d'avoir déjà fait des choix !
            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][elemental] and joueur.prem_ombre == affinite:
                #On a tout pris, en commençant par l'affinité
                skin_ombre = SKIN_OMBRE_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][elemental] and joueur.prem_ombre == MAGIE:
                #On a tout pris, en commençant par la magie
                skin_ombre = SKIN_OMBRE_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] and joueur.prem_ombre == affinite:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_ombre = SKIN_OMBRE_QUASI_COMPLET_AFF

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][affinite] and joueur.prem_ombre == MAGIE:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_ombre = SKIN_OMBRE_QUASI_COMPLET_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][aura] and joueur.prem_ombre == affinite:
                #On est allé jusqu'à l'aura, en commençant par l'affinité
                skin_ombre = SKIN_OMBRE_AURA_AFF

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][aura] and joueur.prem_ombre == MAGIE:
                #On est allé jusqu'à l'aura, en commençant par la magie
                skin_ombre = SKIN_OMBRE_AURA_MAGIE

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][affinite]:
                #On est allé jusqu'à la magie, en commençant par l'affinité
                skin_ombre = SKIN_OMBRE_AFF

            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][MAGIE]:
                #On est allé jusqu'à l'affinité, en commençant par la magie
                skin_ombre = SKIN_OMBRE_MAGIE

            else :
                #On n'a rien pris dans l'arbre de l'ombre, mais on ne peut rien prendre
                skin_ombre = SKIN_OMBRE_VIDE
                
            skin_ombre.dessine_toi(self.screen,(marge_gauche,marge_haut))

            #La ligne des élémentaux :

            pos_gauche = marge_gauche + 70
            pos_haut += 20

            if elemental_terre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == elemental_terre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_ELEMENTAL_TERRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][TERRE][elemental]:
                SKIN_CHOIX_ELEMENTAL_TERRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 160

            if elemental_feu in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == elemental_feu:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_ELEMENTAL_FEU.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][FEU][elemental]:
                SKIN_CHOIX_ELEMENTAL_FEU.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 160

            if elemental_glace in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == elemental_glace:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_ELEMENTAL_GLACE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][GLACE][elemental]:
                SKIN_CHOIX_ELEMENTAL_GLACE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 160

            if elemental_ombre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == elemental_ombre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_ELEMENTAL_OMBRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][elemental]:
                SKIN_CHOIX_ELEMENTAL_OMBRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche = marge_gauche + 70
            pos_haut += 140

            if aura_terre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == aura_terre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AURA_TERRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][TERRE][aura]:
                SKIN_CHOIX_AURA_TERRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 160

            if aura_feu in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == aura_feu:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AURA_FEU.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][FEU][aura]:
                SKIN_CHOIX_AURA_FEU.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 160

            if aura_glace in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == aura_glace:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AURA_GLACE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][GLACE][aura]:
                SKIN_CHOIX_AURA_GLACE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 160

            if aura_ombre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == aura_ombre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AURA_OMBRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][aura]:
                SKIN_CHOIX_AURA_OMBRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche = marge_gauche + 20
            pos_haut += 140

            if affinite_terre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == affinite_terre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AFFINITE_TERRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][TERRE][affinite] or joueur.choix_niveaux[ELEMENTAL][TERRE][elemental]:
                SKIN_CHOIX_AFFINITE_TERRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 100

            if magie_terre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == magie_terre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_MAGIE_TERRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][TERRE][MAGIE]:
                SKIN_CHOIX_MAGIE_TERRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 60

            if affinite_feu in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == affinite_feu:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AFFINITE_FEU.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][FEU][affinite] or joueur.choix_niveaux[ELEMENTAL][FEU][elemental]:
                SKIN_CHOIX_AFFINITE_FEU.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 100

            if magie_feu in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == magie_feu:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_MAGIE_FEU.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][FEU][MAGIE]:
                SKIN_CHOIX_MAGIE_FEU.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 60

            if affinite_glace in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == affinite_glace:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AFFINITE_GLACE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][GLACE][affinite] or joueur.choix_niveaux[ELEMENTAL][GLACE][elemental]:
                SKIN_CHOIX_AFFINITE_GLACE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 100

            if magie_glace in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == magie_glace:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_MAGIE_GLACE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][GLACE][MAGIE]:
                SKIN_CHOIX_MAGIE_GLACE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 60

            if affinite_ombre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == affinite_ombre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_AFFINITE_OMBRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][affinite] or joueur.choix_niveaux[ELEMENTAL][OMBRE][elemental]:
                SKIN_CHOIX_AFFINITE_OMBRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            pos_gauche += 100

            if magie_ombre in joueur.choix_elems:
                if joueur.choix_elems[joueur.element_courant] == magie_ombre:
                    if joueur.etage == 0:
                        pygame.draw.rect(self.screen,(225,225,225),(pos_gauche-2,pos_haut-2,44,44))
                    else:
                        pygame.draw.rect(self.screen,(255,64,0),(pos_gauche-2,pos_haut-2,44,44))
                SKIN_CHOIX_MAGIE_OMBRE.dessine_toi(self.screen,(pos_gauche,pos_haut),40)
            elif joueur.choix_niveaux[ELEMENTAL][OMBRE][MAGIE]:
                SKIN_CHOIX_MAGIE_OMBRE.dessine_toi(self.screen,(pos_gauche+10,pos_haut+10),20)

            SKIN_RACINE_ELEMENTS.dessine_toi(self.screen,(marge_gauche,pos_haut))


    def dessine_droite_choix_niveau(self,joueur):
        """Dessine le rectangle de droite lors du choix de montée de niveau. Décrit le choix sélectionné."""

        if joueur.arbre:
            choi = joueur.choix_dispos[joueur.courant]
            if joueur.etage == 0:
                descr = ["Arbre d'évolution","Flèche du haut pour naviguer dans cet arbre.","Flèche droite ou gauche pour changer d'arbre."]
            elif choi == REGEN_HP:
                descr = ["Option d'évolution :","Renforcement physique","Augmente la régénération des PVs.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == REGEN_MP:
                descr = ["Option d'évolution :","Renforcement magique","Augmente la régénération des PMs.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == DEFENSE:
                descr = ["Option d'évolution :","Defense","Acquisition du skill de défense.","Diminue les dégats subits lors des attaques","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == LANCER:
                descr = ["Option d'évolution :","Lancer","Acquisition du skill de lancer.","Permet de lancer des projectiles.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ESSENCE_MAGIQUE:
                descr = ["Option d'évolution :","Essence magique","Acquisition du skill d'essence magique.","Modifie l'essence même du joueur pour en faire un être de magie.","Les PMs compensent les PVs lorsque c'est nécessaire.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == MAGIE_INFINIE:
                descr = ["Option d'évolution :","Magie infinie","Acquisition du skill de magie infinie","Permet de puiser du mana là où il n'y en a plus, et de continuer à utiliser de la magie.","Les PMs peuvent devenir négatif. Le corps en subira des effets indésirables.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE:
                descr = ["Option d'évolution :","Augmentation de la priorité","La statistique de priorité est augmentée.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PV:
                descr = ["Option d'évolution :","Renforcement physique","Augmente la quantité maximale de PVs.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DE_PRIORITE_D_ATTAQUE:
                descr = ["Option d'évolution :","Augmentation de la priorité d'attaque","La priorité des attaques augmente.","Etat : inneffectif","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == CREATION_FLECHES:
                descr = ["Option d'évolution :","Création de flèches","Acquisition du skill de création de flèches.","Fournit le joueur en flèches à lancer.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SORT_ACCELERATION:
                descr = ["Option d'évolution :","Sort d'accélération","Acquisition de la magie d'accélération","La magie d'accélération augmente temporairement la vitesse du joueur (d'un agissant au choix ?)","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_AURA:
                descr = ["Option d'évolution :","Amélioration des auras","Améliore tous les types d'auras.","Fonctionne aussi sur les auras acquises plus tard.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PM:
                descr = ["Option d'évolution :","Renforcement magique","Augmente la quantitée maximale de PM.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ONDE_DE_CHOC:
                descr = ["Option d'évolution :","Sort d'onde de choc","Acquisition de la magie d'onde de choc.","Une magie d'attaque","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SORT_DE_SOIN_SUPERIEUR:
                descr = ["Option d'évolution :","Sort de soin supérieur","Acquisition de la magie de soin supérieur.","Un sort de soin plus efficace, mais plus coûteux","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEMENT_FORCE:
                descr = ["Option d'évolution :","Enchantement de force","Acquisition de la magie d'enchantement de force.","Augmente la statistique de force d'un agissant pour une longue période.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == PROJECTION_ENERGIE:
                descr = ["Option d'évolution :","Projection d'energie","Acquisition de la magie de projection d'énergie.","Une magie d'attaque.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ECRASEMENT:
                descr = ["Option d'évolution :","Ecrasement","Acquisition du skill d'ecrasement.","Permet de détruire les murs sur son chemin.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == OBSERVATION:
                descr = ["Option d'évolution :","Observation","Acquisition du skill d'observation.","Permet de percevoir des informations sur différentes choses","Etat : fonctionnel, le skill est sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == MANIPULATION_EPEE:
                descr = ["Option d'évolution :","Manipulation d'épées","Acquisition du skill de manipulation d'épée.","Permet d'utiliser les épées plus efficacement.","Etat : fonctionnel, le skill est probablement sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PORTEE:
                descr = ["Option d'évolution :","Augmentation de la portée","Permet de lancer des items plus loin.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SORT_VISION:
                descr = ["Option d'évolution :","Sort de vision","Acquisition de la magie de vision.","Augmente temporairement la portée de la vue du joueur (d'un agissant au choix ?).","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == CREATION_EXPLOSIF:
                descr = ["Option d'évolution :","Création d'explosifs","Acquisition du skill de création d'explosifs.","Fournit le joueur en explosifs à lancer.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ELEMENTALISTE:
                descr = ["Option d'évolution :","Élémentaliste","Acquisition de la classe d'élémentaliste.","Classe sans effets pour l'instant.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == RAYON_THERMIQUE:
                descr = ["Option d'évolution :","Rayon thermique","Acquisition de la magie de rayon thermique.","Une magie d'attaque.","Peut être appelée rayon laser à d'autres endroits.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEMENT_DEFENSE:
                descr = ["Option d'évolution :","Enchantement de défense","Acquisition de la magie d'enchantement de défense.","Confère une protection à un agissant pour une longue période.","Etat : fait crasher le jeu","À regarder de bien plus près à l'occasion !","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == REGEN_PM:
                descr = ["Option d'évolution :","Magie de transfert de mana","Acquisition de la magie de régénération de mana.","Augmente la régénération des PMs de l'agissant ciblé.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ANALYSE:
                descr = ["Option d'évolution :","Analyse","Acquisition du skill d'analyse.","Fournit des informations sur un mot clé ou un terme du système.","Etat : fonctionnel, skill sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == VOL:
                descr = ["Option d'évolution :","Vol","Acquisition du skill de vol.","Dérobe un item à un agissant","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_ATTAQUE_EPEE:
                descr = ["Option d'évolution :","Amélioration de l'attaque à l'épée","Améliore les attaques à l'épée (mais encore ?).","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == FLECHE_PERCANTE:
                descr = ["Option d'évolution :","Fleche perçante","Ajout du projectile Flèche Perçante au skill de création de flèches.","Pour l'instant, juste une flèche normale.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == FLECHE_EXPLOSIVE:
                descr = ["Option d'évolution :","Fleche explosive","Ajout du projectile Flèche Explosive au skill de création de flèches et/ou au skill de création d'explosif.","Une flèche qui est aussi un explosif.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == IMMORTALITE:
                descr = ["Option d'évolution :","Immortalité","Acquisition du skill d'immortalité.","Permet au joueur d'avoir des PVs négatifs (nullifie l'effet de l'essence magique au passage) mais réduit les statistique lorsque c'est le cas.","Etat : fonctionnel, ne peut pas encore être désactivé en faveur de l'essence magique","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DEGATS_MAGIQUES:
                descr = ["Option d'évolution :","Augmentation des dégats magiques","Les dégats magiques sont augmentés.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_MAGIQUE:
                descr = ["Option d'évolution :","Augmentation de la priorité des magie","La priorité des magie est augmentée.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEMENT_FAIBLESSE:
                descr = ["Option d'évolution :","Enchantement de faiblesse","Acquisition de la magie d'enchantement de faiblesse.","Réduit la statistique de force d'un agissant pour une longue période.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == EPEISTE:
                descr = ["Option d'évolution :","Épéiste","Acquisition de la classe d'épéiste.","Renforce tout un tas de caractéristiques liées aux épées.","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_RESTAURATIONS:
                descr = ["Option d'évolution :","Amélioration des restaurations","Améliore les magies de restauration (restauration de PVs, a.k.a. soin, et restauration de PMs).","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == MANIPULATION_BOUCLIER:
                descr = ["Option d'évolution :","Manipulation de bouclier","Acquisition du skill de manipulation de bouclier.","Effets du skill à implémenter.","Etat : fonctionnel, skill probablement sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_OBSERVATION:
                descr = ["Option d'évolution :","Augmentation de la priorité d'observation","Augmente la priorité de l'action d'observation (permet d'observer plus).","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SORT_AUTO_SOIN:
                descr = ["Option d'évolution :","Sort d'auto-soin","Acquisition de la magie d'auto-soin.","Permet de se soigner soi-même, plus efficace qu'un soin classique.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DEGATS_FLECHES:
                descr = ["Option d'évolution :","Augmentation des dégats des flèches","Acquisition du skill d'amélioration des dégats des flèches.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == CHARGE_LOURDE:
                descr = ["Option d'évolution :","Charge lourde","Ajout du projectile Charge Lourde au skill de création de projectiles.","Un explosif qui fait plus de dégats, mais plus lourd à lancer","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == CHARGE_ETENDUE:
                descr = ["Option d'évolution :","Charge étendue","Ajout du projectile Charge Étendue au skill de création de projectiles.","Un explosif qui explose sur une plus grande zone","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == INHUMANITE:
                descr = ["Option d'évolution :","Inhumanité","Retire l'espèce Humain des informations du joueur.","Permet d'éviter l'aggro d'un certain nombre de monstres, mais provoquera un refus de la part de certains humains.","Etat : inneffectif parce que les espèces n'ont pas encore été implémentées","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == MAGICIEN:
                descr = ["Option d'évolution :","Magicien","Acquisition de la classe Magicien.","Améliore les statistiques liées à la magie, permet d'apprendre de nouvelles magies","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DE_PORTEE:
                descr = ["Option d'évolution :","Augmentation de portée","Augmente la portée (des magies ?).","Détails à déterminer.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_SOIN:
                descr = ["Option d'évolution :","Amélioration des soins","Améliore l'efficacité des divers soins.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SORT_DE_VUE:
                descr = ["Option d'évolution :","Sort de vue","Acquision de la magie de vision.","Augmente temporairement la portée de la vue du joueur (d'un agissant au choix ?).","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == VOL_PRIORITE:
                descr = ["Option d'évolution :","Vol de priorité","Acquisition du skill de vol de priorité.","Réduit la statistique de priorité d'un agissant pour augmenter celle du joueur.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_ATTAQUE_LANCE:
                descr = ["Option d'évolution :","Amélioration des attaques à la lance","Améliore les attaques à la lance (mais encore ?).","Etat : fonctionnel, probablement sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_FLECHES:
                descr = ["Option d'évolution :","Augmentation de la priorité des flèches","Augmente la priorité des flèches, et donc de leurs attaques.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ARTIFICIER:
                descr = ["Option d'évolution :","Artificier","Acquisition de la classe d'Artificier.","Améliore les explosifs et leur utilisation, je suppose.","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == FANTOME:
                descr = ["Option d'évolution :","Fantôme","Transforme le joueur en fantôme.","Permet de traverser les murs.","Etat : fonctionnel ou inneffectif","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == INSTAKILL:
                descr = ["Option d'évolution :","Instakill","Acquisition de la magie d'instakill (ou est-ce un skill ?).","Réduit les PVs d'un agissant à 0 instantannément.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == JET_DE_MANA:
                descr = ["Option d'évolution :","Magie de jet de mana","Acquisition de la magie de jet de mana.","Une attaque magique.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEMENT_RENFORCEMENT:
                descr = ["Option d'évolution :","Enchantement de renforcement","Acquisition de la magie d'enchantement de renforcement.","Renforce les statistiques d'un item pour une longue période.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SORT_DE_PROTECTION:
                descr = ["Option d'évolution :","Sort de protection","Acquisition de la magie de protection.","Protège un agissant (une zone ?) contre les attaques.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_ATTAQUE:
                descr = ["Option d'évolution :","Amélioration d'attaque","Améliore les attaques (mais encore ?).","Etat : fonctionnel, probablement sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ARCHER:
                descr = ["Option d'évolution :","Archer","Acquisition de la classe d'Archer.","Améliore les flèches et leur utilisation, je suppose.","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == FLECHE_FANTOME:
                descr = ["Option d'évolution :","Flèche fantôme","Ajout du projectile Flèche Fantôme au skill de création de flèches.","Une flèche qui traverse les murs.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DEGAT:
                descr = ["Option d'évolution :","Augmentation des dégats","Augmente les dégats infligés.","(Cette description a de fortes chances d'être inexacte.)","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == NECROMANCIEN:
                descr = ["Option d'évolution :","Nécromancien","Acquisition de la classe de Nécromancien.","Peut rescussiter des agissants pour les convertir à sa cause.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEUR:
                descr = ["Option d'évolution :","Enchanteur","Acquisition de la classe d'enchanteur.","Améliore les enchantements, je suppose.","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == SOUTIEN:
                descr = ["Option d'évolution :","Soutien","Acquisition de la classe de Soutien.","Améliore les soins et assimilés, je suppose.","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_DEPLACEMENT:
                descr = ["Option d'évolution :","Augmentation de la priorité de déplacement","Augmente la priorité des actions de déplacement.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_ANALYSE:
                descr = ["Option d'évolution :","Augmentation de la priorité d'analyse","Augmente la priorité des analyses.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_EXPLOSIF:
                descr = ["Option d'évolution :","Augmentation de la priorité des explosifs","Augmente la priorité des explosifs, et donc de leurs attaques.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_VITESSE_EXPLOSIF:
                descr = ["Option d'évolution :","Augmentation de la vitesse des explosifs","Augmente la vitesse des explosifs.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PRIORITE_AURA:
                descr = ["Option d'évolution :","Augmentation de la priorité des auras","Augmente la priorité des auras","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == AURA_MORTELLE:
                descr = ["Option d'évolution :","Aura mortelle","Acquisition du skill d'Aura Mortelle.","Lance des attaques de type Instakill sur tous les agissants non-alliés dans l'aura.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ASSASSIN:
                descr = ["Option d'évolution :","Assassin","Acquisition de la classe d'Assassin.","Effets de la classe à déterminer","Etat : fonctionnel, classe sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DE_ZONE_DE_RESTAURATION:
                descr = ["Option d'évolution :","Augmentation de la portée de restauration","Augmente la portée des restaurations de zone.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ANGE:
                descr = ["Option d'évolution :","Ange","Acquisition de la classe Ange.","Améliore les capacités de soutien.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEMENT_ROUILLE:
                descr = ["Option d'évolution :","Enchantement de rouille","Acquisition de la magie d'enchantement de rouille","Réduit les statistiques d'un item pour une longue période.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == MANIPULATION_ARME:
                descr = ["Option d'évolution :","Manipulation d'arme","Acquisition du skill de manipulation d'armes","Améliore les armes, je suppose.","Etat : fonctionnel, probablement sans effet","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == FLECHES_LOURDE_LEGERE:
                descr = ["Option d'évolution :","Flèche lourde, flèche légère","Ajout du projectile de flèche lourde et du projectile de flèche légère au skill de création de flèches.","Une flèche qui fait plus de dégats, mais plus lourde à lancer, et une flèche plus légère, mais moins dangereuse.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_PORTEE_EXPLOSIFS:
                descr = ["Option d'évolution :","Augmentation de la portée des explosifs","Augmente la portée des explosifs, (ou de leurs explosions ?).","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ECLAIR_NOIR:
                descr = ["Option d'évolution :","Éclair noir","Acquisition de la magie d'Éclair Noir.","À la fois la magie, l'attaque et le projectile les plus puissants du jeu. Effet garanti, coût démeusuré.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_DEGATS_PROJECTILES:
                descr = ["Option d'évolution :","Augmentation des dégats des projectiles","Augmente les dégats des projectiles.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == BOOST_ENCHANTEMENT:
                descr = ["Option d'évolution :","Amélioration d'enchantement","Améliore les enchantements (durée, effet ?).","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == RESURECTION:
                descr = ["Option d'évolution :","Résurection","Acquisition de la magie de résurection.","Permet de rescussiter n'importe quel agissant.","Etat : fonctionnel","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == ENCHANTEMENT_DEFENSIF:
                descr = ["Option d'évolution :","Enchantement défensif","Acquisition de la magie d'enchantement défensif.","Confère des propriétés défensives à un item.","Etat : fait crasher le jeu","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            else:
                descr = ["Je ne sais pas décrire ça !.","Nous sommes dans l'arbre classique, voici le code fautif :",str(choi),"Bonne chance à moi pour corriger ça !","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]

        else:
            choi = joueur.choix_elems[joueur.element_courant]
            if joueur.etage == 0:
                descr = ["Arbre élémental d'évolution","Flèche du haut pour naviguer dans cet arbre.","Flèche droite ou gauche pour changer d'arbre."]
            elif choi == affinite_terre:
                descr = ["Option d'évolution :","Affinité à la terre","Augmente sustanciellement l'affinité à la terre.","Réduit un peu l'affinité à l'ombre.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == affinite_feu:
                descr = ["Option d'évolution :","Affinité au feu","Augmente sustanciellement l'affinité au feu.","Réduit un peu l'affinité à l'ombre.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == affinite_glace:
                descr = ["Option d'évolution :","Affinité à la glace","Augmente sustanciellement l'affinité à la glace.","Réduit un peu l'affinité à l'ombre.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == affinite_ombre:
                descr = ["Option d'évolution :","Affinité à l'ombre","Augmente sustanciellement l'affinité à l'ombre.","Réduit un peu l'affinité à la terre.","Réduit un peu l'affinité au feu.","Réduit un peu l'affinité à la glace.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == aura_terre:
                descr = ["Option d'évolution :","Aura de terre","Acquisition du skill d'aura de terre.","Pas d'effet en soi, peut bloquer d'autres auras.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == aura_feu:
                descr = ["Option d'évolution :","Aura de feu","Acquisition du skill d'aura de feu.","Inflige des dégats aux agissants proches.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == aura_glace:
                descr = ["Option d'évolution :","Aura de glace","Acquisition du skill d'aura de glace.","Ralentit les agissants proches.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == aura_ombre:
                descr = ["Option d'évolution :","Aura d'ombre","Acquisition du skill d'aura d'ombre.","Obscurcit les cases proches.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == magie_terre:
                descr = ["Option d'évolution :","Magie de terre","Acquisition des magies de terre.","Trois magies différentes.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == magie_feu:
                descr = ["Option d'évolution :","Magie de feu","Acquisition des magies de feu.","Trois magies différentes.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == magie_glace:
                descr = ["Option d'évolution :","Magie de glace","Acquisition des magies de glace.","Trois magies différentes.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == magie_ombre:
                descr = ["Option d'évolution :","Magie d'ombre","Acquisition des magies d'ombre.","Trois magies différentes.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == elemental_terre:
                descr = ["Option d'évolution :","Élémental de terre","Acquisition de la classe d'Élémental de terre.","Confère une immunité à la terre.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == elemental_feu:
                descr = ["Option d'évolution :","Élémental de feu","Acquisition de la classe d'Élémental de feu.","Confère une immunité au feu.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == elemental_glace:
                descr = ["Option d'évolution :","Élémental de glace","Acquisition de la classe d'Élémental de glace.","Confère une immunité à la glace.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            elif choi == elemental_ombre:
                descr = ["Option d'évolution :","Élémental d'ombre","Acquisition de la classe d'Élémental d'ombre.","Confère une immunité à l'ombre.","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]
            else:
                descr = ["Je ne sais pas décrire ça !.","Nous sommes dans l'arbre élémental, voici le code fautif :",str(choi),"Bonne chance à moi pour corriger ça !","Touche espace pour valider","Flèche du bas pour retourner au choix de l'arbre.","Flèche droite ou gauche pour naviguer dans l'arbre."]

        pos_gauche = self.position_debut_x_rectangle_2 + 5
        pos_haut = self.position_debut_y_rectangles_et_carre + 5

        for phrase in descr:
            texte = POLICE20.render(phrase,True,(0,0,0))
            self.screen.blit(texte,(pos_gauche,pos_haut))
            pos_haut += 20


    def print_tailles(self):
        print("hauteur ecran : ",self.hauteur_ecran)
        print("largeur ecran : " , self.largeur_ecran)
        print("hauteur exploitable : " , self.hauteur_exploitable)
        print("largeur exploitable : " , self.largeur_exploitable)
        print("marge gauche : " , self.marge_gauche)
        print("marge haut : " , self.marge_haut)
        print("largeur rectangles : " , self.largeur_rectangles)
        print("position debut x rectangle 1 : " , self.position_debut_x_rectangle_1)
        print("position fin x rectangle 1 : " , self.position_fin_x_rectangle_1)
        print("position debut x carre : " , self.position_debut_x_carre)
        print("position fin x carre : " , self.position_fin_x_carre)
        print("position debut x rectangle 2 : " , self.position_debut_x_rectangle_2)
        print("position fin x rectangle 2 : " , self.position_fin_x_rectangle_2)
        print("position debut y titre : " , self.position_debut_y_titre)
        print("position debut y rectangles et carre : " , self.position_debut_y_rectangles_et_carre)
        print("position fin y rectangles et carre : " , self.position_fin_y_rectangles_et_carre)
    
    def message(self,texte="Ceci est le message par défaut. Avez-vous oublié de préciser ce que vous vouliez dire ?",secret=0):
        self.messages.append([texte,secret])

    def scinde_texte(self,texte,largeur,hauteur=20,couleur=(0,0,0),police=None):
        """Fonction qui prend en entrée une chaine de caractère et renvoie les surfaces des lignes successives du texte."""
        police = pygame.font.SysFont(police,hauteur) #/!\ Se souvenir de jouer avec les polices un jour /!\
        mots = texte.split() #On explose sur les espaces
        i = 0
        res = []
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and police.size(ligne+" "+mots[i])[0] <= largeur:
                ligne = ligne + " " + mots[i]
                i+=1
            res.append(police.render(ligne,True,couleur))
        return res

    def observe(self,joueur,position,direction,rect):
        """Fonction qui montre ce que voit le joueur.
           On précise la position (celle du joueur, ou la case en face de lui), la direction, et le rectangle où dessiner le résultat."""
        #/!\ Refaire en plus joli !
        if position[0] != joueur.position[0]:
            print("Euh... On veut voir où la ?")
            return
        else:
            x = rect[0]
            y = rect[1]
            largeur = rect[2]
            hauteur = rect[3]

        # Version plus jolie :
            skins = []
            for distance in range(PROFONDEUR_DE_CHAMP): #On ne va pas plus loin que ça pour l'instant
                case = None
                if direction == HAUT:
                    if position[2]-distance>=0 :
                        case = joueur.vue[position[1]][position[2]-distance]
                elif direction == DROITE:
                    if position[1]+distance<len(joueur.vue):
                        case = joueur.vue[position[1]+distance][position[2]]
                elif direction == BAS:
                    if position[2]+distance<len(joueur.vue[0]):
                        case = joueur.vue[position[1]][position[2]+distance]
                elif direction == GAUCHE:
                    if position[1]-distance>=0 :
                        case = joueur.vue[position[1]-distance][position[2]]
                if case != None:
                    if case[1] == -1:
                        skins.append(SKINS_CASES_NOIRES_VUES[distance][0])
                    elif case[1] > 0:
                        skins.append(SKINS_CASES_VUES[distance][0])
                        if not case[5][direction][4]:
                            skins.append(SKINS_MURS_FACE_VUS[distance][0])
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][0])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][0])
                        if not case[5][direction-1][4]:
                            skins.append(SKINS_MURS_VUS[distance][0][0])
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction-1)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_VUS[distance][0][0])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][0][0])
                        if not case[5][direction-3][4]:
                            skins.append(SKINS_MURS_VUS[distance][0][1])
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction-3)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_VUS[distance][0][1])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][0][1])
                for ecart_ in range(distance//2+1):
                    ecart = ecart_+1
                    case = None
                    if direction == HAUT:
                        if position[2]-distance>=0 and position[1]+ecart in range(len(joueur.vue)):
                            case = joueur.vue[position[1]+ecart][position[2]-distance]
                    elif direction == DROITE:
                        if position[1]+distance<len(joueur.vue) and position[2]+ecart in range(len(joueur.vue[0])):
                            case = joueur.vue[position[1]+distance][position[2]+ecart]
                    elif direction == BAS:
                        if position[2]+distance<len(joueur.vue[0]) and position[1]-ecart in range(len(joueur.vue)):
                            case = joueur.vue[position[1]-ecart][position[2]+distance]
                    elif direction == GAUCHE:
                        if position[1]-distance>=0 and position[2]-ecart in range(len(joueur.vue[0])):
                            case = joueur.vue[position[1]-distance][position[2]-ecart]
                    if case != None:
                        if case[1] == -1:
                            skins.append(SKINS_CASES_NOIRES_VUES[distance][ecart])
                        elif case[1] > 0:
                            skins.append(SKINS_CASES_VUES[distance][ecart])#Rajouter les affinités etc. plus tard
                            if not case[5][direction][4]:
                                skins.append(SKINS_MURS_FACE_VUS[distance][ecart])#Rajouter aussi les distinctions des téléportations
                            else:
                                traj = joueur.controleur.get_trajet(case[0],direction)
                                if traj == "escalier bas":
                                    skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][ecart])
                                elif traj == "escalier haut":
                                    skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][ecart])
                            if not case[5][direction-3][4]:
                                skins.append(SKINS_MURS_VUS[distance][ecart])#Pareil
                            else:
                                traj = joueur.controleur.get_trajet(case[0],direction-3)
                                if traj == "escalier bas":
                                    skins.append(SKINS_ESCALIERS_BAS_VUS[distance][ecart])
                                elif traj == "escalier haut":
                                    skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][ecart])
                    ecart = -ecart
                    case = None
                    if direction == HAUT:
                        if position[2]-distance>=0 and position[1]+ecart in range(len(joueur.vue)):
                            case = joueur.vue[position[1]+ecart][position[2]-distance]
                    elif direction == DROITE:
                        if position[1]+distance<len(joueur.vue) and position[2]+ecart in range(len(joueur.vue[0])):
                            case = joueur.vue[position[1]+distance][position[2]+ecart]
                    elif direction == BAS:
                        if position[2]+distance<len(joueur.vue[0]) and position[1]-ecart in range(len(joueur.vue)):
                            case = joueur.vue[position[1]-ecart][position[2]+distance]
                    elif direction == GAUCHE:
                        if position[1]-distance>=0 and position[2]-ecart in range(len(joueur.vue[0])):
                            case = joueur.vue[position[1]-distance][position[2]-ecart]
                    if case != None:
                        if case[1] == -1:
                            skins.append(SKINS_CASES_NOIRES_VUES[distance][ecart])
                        elif case[1] > 0:
                            skins.append(SKINS_CASES_VUES[distance][ecart])
                            if not case[5][direction][4]:
                                skins.append(SKINS_MURS_FACE_VUS[distance][ecart])
                            else:
                                traj = joueur.controleur.get_trajet(case[0],direction)
                                if traj == "escalier bas":
                                    skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][ecart])
                                elif traj == "escalier haut":
                                    skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][ecart])
                            if not case[5][direction-1][4]:
                                skins.append(SKINS_MURS_VUS[distance][ecart])
                            else:
                                traj = joueur.controleur.get_trajet(case[0],direction-1)
                                if traj == "escalier bas":
                                    skins.append(SKINS_ESCALIERS_BAS_VUS[distance][ecart])
                                elif traj == "escalier haut":
                                    skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][ecart])
            skins.reverse()
            for skin in skins:
                skin.dessine_toi(self.screen,(x,y),(largeur,hauteur))

            for ID in joueur.vue[position[1]][position[2]][6]:
                if ID < 11:
                    entitee = joueur.controleur.get_entitee(ID)
                    if issubclass(entitee.get_classe(),Agissant):
                        for skin in entitee.get_skins_vue():
                            skin.dessine_toi(self.screen,(x,y),(largeur,hauteur))
                        break

    def affiche(self,joueur,vue,position,taille):
        self.affichables=[]
        if vue[1]==0:
            SKIN_BROUILLARD.dessine_toi(self.screen,position,taille)
        elif vue[1]==-1: #On a affaire à un case accessible mais pas vue
            SKIN_BROUILLARD.dessine_toi(self.screen,position,taille)
            if vue[0][2] > 0:
                if vue[5][HAUT][0]:
                    if joueur.vue[vue[0][1]][vue[0][2]-1][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,1,1,HAUT)
            if vue[0][1] < len(joueur.vue) - 1:
                if vue[5][DROITE][0]:
                    if joueur.vue[vue[0][1]+1][vue[0][2]][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,1,1,DROITE)
            if vue[0][2] < len(joueur.vue[0]) -1:
                if vue[5][BAS][0]:
                    if joueur.vue[vue[0][1]][vue[0][2]+1][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,1,1,BAS)
            if vue[0][1] > 0:
                if vue[5][GAUCHE][0]:
                    if joueur.vue[vue[0][1]-1][vue[0][2]][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,1,1,GAUCHE)
        else:
            if vue[4]==0: #On teste le code de la case pour déterminer son image
                SKIN_CASE.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==1: #On teste le code de la case pour déterminer son image
                SKIN_CASE_1.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==2: #On teste le code de la case pour déterminer son image
                SKIN_CASE_2.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==3: #On teste le code de la case pour déterminer son image
                SKIN_CASE_3.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==4: #On teste le code de la case pour déterminer son image
                SKIN_CASE_4.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==5: #On teste le code de la case pour déterminer son image
                SKIN_CASE_5.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==6: #On teste le code de la case pour déterminer son image
                SKIN_CASE_6.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==7: #On teste le code de la case pour déterminer son image
                SKIN_CASE_7.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==8: #On teste le code de la case pour déterminer son image
                SKIN_CASE_8.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            case = joueur.controleur.get_case(vue[0])
            for i in range(4):
                mur = case.get_mur_dir(i)
                for effet in mur.effets:
                    if effet.affiche:
                        if isinstance(effet,Porte) :
                            effet.get_skin(joueur.get_clees()).dessine_toi(self.screen,position,taille,1,1,i)
                        elif isinstance(effet,(Mur_plein,Mur_impassable)) :
                            effet.get_skin(vue[4]).dessine_toi(self.screen,position,taille,1,1,i)
                        else :
                            effet.get_skin().dessine_toi(self.screen,position,taille,1,1,i)
            for effet in case.effets:
                if effet.affiche:
                    effet.get_skin().dessine_toi(self.screen,position,taille)
            entitees = vue[6]
            agissant = None
            for ID_entitee in entitees : #Puis les items au sol
                entitee = joueur.controleur.get_entitee(ID_entitee)
                if issubclass(entitee.get_classe(),Item):
                    entitee.get_skin().dessine_toi(self.screen,position,taille,1,1,entitee.get_direction()) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                elif issubclass(entitee.get_classe(),Decors):
                    entitee.get_skin().dessine_toi(self.screen,position,taille)
                else:
                    agissant = entitee
            if agissant != None: #Enfin l'agissant (s'il y en a un)
                direction = agissant.get_direction()
                arme = agissant.inventaire.arme
                if arme != None:
                    joueur.controleur.get_entitee(arme).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                agissant.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                armure = agissant.inventaire.armure
                if armure != None:
                    joueur.controleur.get_entitee(armure).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                bouclier = agissant.inventaire.bouclier
                if bouclier != None:
                    joueur.controleur.get_entitee(bouclier).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                haume = agissant.inventaire.haume
                agissant.get_skin_tete().dessine_toi(self.screen,position,taille,1,1,direction) #Avoir éventuellement la tête dans une autre direction ?
                if haume != None:
                    joueur.controleur.get_entitee(haume).get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                for effet in agissant.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(self.screen,position,taille,1,1,direction)
                esprit = joueur.controleur.get_esprit(joueur.esprit)
                if agissant.ID in esprit.ennemis.keys():
                    fichier = "Jeu/Skins/barre_de_vie_ennemis.png"
                elif agissant.ID in esprit.corps.keys():
                    fichier = "Jeu/Skins/barre_de_vie_allies.png"
                else:
                    fichier = "Jeu/Skins/barre_de_vie_neutres.png"
                self.screen.blit(pygame.transform.scale(pygame.image.load(fichier).convert_alpha(),(int(taille*((15*agissant.pv)/(19*agissant.pv_max))),int(taille*(15/19)))),(position[0]+int(taille*(2/19)),position[1]+int(taille*(2/19))))
                if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif au-dessus des effets ?
                    SKIN_DIALOGUE.dessine_toi(self.screen,position,taille)
            if vue[7] != []:
                esprit = joueur.controleur.get_esprit(joueur.esprit)
                if any([effet[2] in esprit.corps.keys() for effet in vue[7]]):
                    SKIN_ATTAQUE_DELAYEE_ALLIE.dessine_toi(self.screen,position,taille)
                else:
                    SKIN_ATTAQUE_DELAYEE.dessine_toi(self.screen,position,taille)

            #Rajouter des conditions d'observation

    def clear(self):
        self.screen = None

    def unclear(self,screen):
        self.screen = screen


print("Hey, pense à remplacer le faux affichage !")
class Faux_affichage(Conteneur,Old_affichage):
    """Classe temporaire.
       Affiche l'ancien affichage avec les méthodes du nouveau, presque."""
    def __init__(self,screen):
        Old_affichage.__init__(self,screen)
        Conteneur.__init__(self)
        self.contenu = [Faux_lab()]

    def dessine_lab(self,joueur): #La fonction qui dessine le carré au centre. Elle affiche le labyrinthe vu par le joueur, ses occupants, et tout ce que le joueur est capable de percevoir.
        vue = joueur.vue
        position = joueur.get_position()
        visible_x = [len(vue)-1,0]
        visible_y = [len(vue[0])-1,0]
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    if i < visible_x[0]:
                        visible_x[0] = i
                    if i > visible_x[1]:
                        visible_x[1] = i
                    if j < visible_y[0]:
                        visible_y[0] = j
                    if j > visible_y[1]:
                        visible_y[1] = j
        distance = max(position[1]-visible_x[0],visible_x[1]-position[1],position[2]-visible_y[0],visible_y[1]-position[2]) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
        vue_x = position[1] - distance
        vue_y = position[2] - distance
        nb_cases = distance*2 + 1
        taille_case = int(self.hauteur_exploitable // (nb_cases-1))
        taille_affichee = nb_cases* int(self.hauteur_exploitable // nb_cases)
        self.set_tailles((self.hauteur_exploitable,self.hauteur_exploitable))
        hauteur_exploitee = taille_case * nb_cases
        marge = (self.hauteur_exploitable - hauteur_exploitee) // 2
        self.set_position((self.position_debut_x_carre,self.position_debut_y_rectangles_et_carre))
        self.contenu[0].vue = vue
        self.contenu[0].joueur = joueur
        self.contenu[0].position = [0,0]
        self.contenu[0].tailles = [hauteur_exploitee,hauteur_exploitee]
        self.contenu[0].vues = [vue_x,vue_y]
        self.contenu[0].taille_case = taille_case
        self.contenu[0].nb_cases = nb_cases
        Conteneur.affiche(self,self.screen)

    def dessine_lab_magie(self,joueur):
        vue = joueur.vue
        position = joueur.get_position()
        visible_x = [len(vue)-1,0]
        visible_y = [len(vue[0])-1,0]
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    if i < visible_x[0]:
                        visible_x[0] = i
                    if i > visible_x[1]:
                        visible_x[1] = i
                    if j < visible_y[0]:
                        visible_y[0] = j
                    if j > visible_y[1]:
                        visible_y[1] = j
        distance = max(position[1]-visible_x[0],visible_x[1]-position[1],position[2]-visible_y[0],visible_y[1]-position[2]) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
        vue_x = position[1] - distance
        vue_y = position[2] - distance
        nb_cases = distance*2 + 1
        taille_case = int(self.hauteur_exploitable // nb_cases)
        hauteur_exploitee = taille_case * nb_cases
        marge = (self.hauteur_exploitable - hauteur_exploitee) // 2
        marge_haut = marge + self.position_debut_y_rectangles_et_carre
        for j in range(nb_cases):
            marge_gauche = marge + self.position_debut_x_carre
            for i in range(nb_cases):
                if (position[0],vue_x+i,vue_y+j) in joueur.cibles:
                    Old_affichage.affiche(self,joueur,vue[vue_x + i][vue_y + j],(marge_gauche,marge_haut),taille_case)
                else:
                    SKIN_BROUILLARD.dessine_toi(self.screen,(marge_gauche,marge_haut),taille_case)
                if (position[0],vue_x+i,vue_y+j) == joueur.element_courant:
                    pygame.draw.rect(self.screen,(255,64,0),(marge_gauche,marge_haut,taille_case,taille_case),2)
                elif (position[0],vue_x+i,vue_y+j) in joueur.cible:
                    pygame.draw.rect(self.screen,(170,170,170),(marge_gauche,marge_haut,taille_case,taille_case),2)
                marge_gauche += taille_case
            marge_haut += taille_case

class Faux_lab(Affichable):
    def __init__(self):
        self.position=[0,0]
        self.tailles=[0,0]
        self.objets=[]
        self.vue = None
        self.joueur = None
        self.vues = [0,0]
        self.taille_case = 0
        self.nb_cases = 0

    def affiche(self,screen,frame,frame_par_tour):
        vue_x=self.vues[0]
        vue_y=self.vues[1]
        marge_haut = self.position[1]-self.taille_case//2
        for j in range(self.nb_cases):
            marge_gauche = self.position[0]-self.taille_case//2
            for i in range(self.nb_cases):
                if 0 <= vue_x + i < len(self.vue) and 0 <= vue_y + j < len(self.vue[0]):
                    self.old_affiche(screen,self.joueur,self.vue[vue_x + i][vue_y + j],(marge_gauche,marge_haut),self.taille_case)
                else:
                    SKIN_BROUILLARD.dessine_toi(screen,(marge_gauche,marge_haut),self.taille_case)
                marge_gauche += self.taille_case
            marge_haut += self.taille_case

    def old_affiche(self,screen,joueur,vue,position,taille):
        self.affichables=[]
        if vue[1]==0:
            SKIN_BROUILLARD.dessine_toi(screen,position,taille)
        elif vue[1]==-1: #On a affaire à un case accessible mais pas vue
            SKIN_BROUILLARD.dessine_toi(screen,position,taille)
            if vue[0][2] > 0:
                if vue[5][HAUT][0]:
                    if joueur.vue[vue[0][1]][vue[0][2]-1][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(screen,position,taille,1,1,HAUT)
            if vue[0][1] < len(joueur.vue) - 1:
                if vue[5][DROITE][0]:
                    if joueur.vue[vue[0][1]+1][vue[0][2]][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(screen,position,taille,1,1,DROITE)
            if vue[0][2] < len(joueur.vue[0]) -1:
                if vue[5][BAS][0]:
                    if joueur.vue[vue[0][1]][vue[0][2]+1][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(screen,position,taille,1,1,BAS)
            if vue[0][1] > 0:
                if vue[5][GAUCHE][0]:
                    if joueur.vue[vue[0][1]-1][vue[0][2]][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(screen,position,taille,1,1,GAUCHE)
        else:
            if vue[4]==0: #On teste le code de la case pour déterminer son image
                SKIN_CASE.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==1: #On teste le code de la case pour déterminer son image
                SKIN_CASE_1.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==2: #On teste le code de la case pour déterminer son image
                SKIN_CASE_2.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==3: #On teste le code de la case pour déterminer son image
                SKIN_CASE_3.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==4: #On teste le code de la case pour déterminer son image
                SKIN_CASE_4.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==5: #On teste le code de la case pour déterminer son image
                SKIN_CASE_5.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==6: #On teste le code de la case pour déterminer son image
                SKIN_CASE_6.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==7: #On teste le code de la case pour déterminer son image
                SKIN_CASE_7.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            elif vue[4]==8: #On teste le code de la case pour déterminer son image
                SKIN_CASE_8.dessine_toi(screen,position,taille) #La case en premier, donc en bas
            case = joueur.controleur.get_case(vue[0])
            for i in range(4):
                mur = case.get_mur_dir(i)
                for effet in mur.effets:
                    if effet.affiche:
                        if isinstance(effet,Porte) :
                            effet.get_skin(joueur.get_clees()).dessine_toi(screen,position,taille,1,1,i)
                        elif isinstance(effet,(Mur_plein,Mur_impassable)) :
                            effet.get_skin(vue[4]).dessine_toi(screen,position,taille,1,1,i)
                        else :
                            effet.get_skin().dessine_toi(screen,position,taille,1,1,i)
            for effet in case.effets:
                if effet.affiche:
                    effet.get_skin().dessine_toi(screen,position,taille)
            entitees = vue[6]
            agissant = None
            for ID_entitee in entitees : #Puis les items au sol
                entitee = joueur.controleur.get_entitee(ID_entitee)
                if issubclass(entitee.get_classe(),Item):
                    entitee.get_skin().dessine_toi(screen,position,taille,1,1,entitee.get_direction()) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                elif issubclass(entitee.get_classe(),Decors):
                    entitee.get_skin().dessine_toi(screen,position,taille)
                else:
                    agissant = entitee
            if agissant != None: #Enfin l'agissant (s'il y en a un)
                direction = agissant.get_direction()
                arme = agissant.inventaire.arme
                if arme != None:
                    joueur.controleur.get_entitee(arme).get_skin().dessine_toi(screen,position,taille,1,1,direction)
                agissant.get_skin().dessine_toi(screen,position,taille,1,1,direction)
                armure = agissant.inventaire.armure
                if armure != None:
                    joueur.controleur.get_entitee(armure).get_skin().dessine_toi(screen,position,taille,1,1,direction)
                bouclier = agissant.inventaire.bouclier
                if bouclier != None:
                    joueur.controleur.get_entitee(bouclier).get_skin().dessine_toi(screen,position,taille,1,1,direction)
                haume = agissant.inventaire.haume
                agissant.get_skin_tete().dessine_toi(screen,position,taille,1,1,direction) #Avoir éventuellement la tête dans une autre direction ?
                if haume != None:
                    joueur.controleur.get_entitee(haume).get_skin().dessine_toi(screen,position,taille,1,1,direction)
                for effet in agissant.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(screen,position,taille,1,1,direction)
                esprit = joueur.controleur.get_esprit(joueur.esprit)
                if agissant.ID in esprit.ennemis.keys():
                    fichier = "Jeu/Skins/barre_de_vie_ennemis.png"
                elif agissant.ID in esprit.corps.keys():
                    fichier = "Jeu/Skins/barre_de_vie_allies.png"
                else:
                    fichier = "Jeu/Skins/barre_de_vie_neutres.png"
                screen.blit(pygame.transform.scale(pygame.image.load(fichier).convert_alpha(),(ceil(taille*((15*agissant.pv)/(19*agissant.pv_max))),ceil(taille*(15/19)))),(position[0]+ceil(taille*(2/19)),position[1]+ceil(taille*(2/19))))
                if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif au-dessus des effets ?
                    SKIN_DIALOGUE.dessine_toi(screen,position,taille)
            if vue[7] != []:
                esprit = joueur.controleur.get_esprit(joueur.esprit)
                if any([effet[2] in esprit.corps.keys() for effet in vue[7]]):
                    SKIN_ATTAQUE_DELAYEE_ALLIE.dessine_toi(screen,position,taille)
                else:
                    SKIN_ATTAQUE_DELAYEE.dessine_toi(screen,position,taille)

            #Rajouter des conditions d'observation

from Jeu.Entitee.Decors.Decors import *
from Jeu.Entitee.Item.Item import *
from Jeu.Entitee.Agissant.Humain.Humain import Humain
from Jeu.Effet.Effets_mouvement.Blocages import *
from Jeu.Effet.Effets import *
from Jeu.Systeme.Classe import *