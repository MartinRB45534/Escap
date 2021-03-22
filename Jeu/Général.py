from Jeu.Systeme.Classe import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Systeme.Constantes_projectiles.Projectiles import *
from Jeu.Systeme.Constantes_stats import *
from Jeu.Constantes import *
from Jeu.Skins.Skins import *
import random

# /!\ Mettre les lignes à jour !
# Contenu du fichier :
# La classe Controleur (lignes 0-500) ;
# La classe Labyrinthe (lignes 500-900), avec :
#    La classe Generateur (lignes 900-1200) ;
#    La classe Case (lignes 1200-1300) ;
#    La classe Murs (lignes 1300-1400) ;
#    La classe Pattern (lignes 1400-1700) ;
# La classe Entitee (lignes 1700), avec ;
#    La classe Entitee_superieure (lignes 1700) ;
#    La classe Fantome (lignes 1700) ;
#    La classe Cadavre (lignes 1700) ;
#    La classe Oeuf (lignes 1700) ;
#    La classe Agissant (lignes 1700-2000) ;
#    La classe Joueur (lignes 2000-2200) ;
#    La classe Item et ses multiples sous-classes (lignes 2200-2500) ;
#    La classe Inventaire (lignes 2500-2700) ;
# La classe Esprit (lignes 2700-2900) ;
# Les mutiples classes de Magie_* (lignes 2900-3900) ;
# La classe Effet et ses multiples sous-classes (lignes 3900-4800) ;
# La classe Sort et ses multiples sous-classes (lignes 4800-5100) ;
# La classe Affichage (lignes 5100-5300).

# Conseil de navigation : Ctrl+f + "Class Bidule" vous enverra au début de la classe Bidule


#    .
#   / \     Je ne respecte absolument pas les régles de base de la programmation objet, puisque je vais donner à tous les objets de mon univers (ou presque) ce controleur qui les contient tous (ou presque).
#  / ! \    S'attendre à de vives ciritques !
# /_____\

class Controleur():
    def __init__(self):
        #print("Initialisation du controleur")
        self.labs = {} #Un dictionnaire avec tous les labyrinthes, indéxés par leur identifiant dans les positions.
        #print("Labyrinthe : check")
        self.entitees = {}
        #print("Entitées : check")
        self.esprits = {}
        self.labs_courants = []
        self.entitees_courantes = []
        self.esprits_courants = []
        self.nb_tours = 0
        self.phase = TOUR
        self.phases = [TOUR]

    def jeu(self,screen):

        #On crée les labyrinthes. Pour l'instant :
        #Un labyrinthe avec une clé et une porte (et d'autres trucs éventuellements)
        self.labs[0] = Labyrinthe(0,20,20,(0,0,0),[Patern((0,2,3),10,8,[(0,0,1),(0,5,7),(0,5,0)],["test_code"])])
        #Un labyrinthe sans grand-chose de spécial
        self.labs[1] = Labyrinthe(1,20,20,(1,0,0),[Patern((1,5,6),2,12,[(1,1,3),(1,1,6),(1,0,8),(1,0,10)]),Patern((1,2,4),12,2,[(1,3,1),(1,4,1),(1,1,0),(1,10,0)])])
        #Un labyrinthe avec une barrière à items, pour quand je pourrai en lancer
        self.labs["test_barriere"] = Labyrinthe("test_barriere",20,20,("test_barriere",0,0),[Patern(("test_barriere",0,0),10,20,[]),Patern(("test_barriere",10,0),10,20,[("test_barriere",0,6)])])
        #Un labyrinthe avec un labo de magicien (parchemins et potions en tous genres, de quoi tester le fonctionnement des magies
        self.labs["test_magies"] = Labyrinthe("test_magies",5,5,("test_magies",0,0),[Patern(("test_magie",0,0),5,5,[])])
        #Un labyrinthe avec des gens qui se battent
        self.labs["test_esprit"] = Labyrinthe("test_esprit",10,10,("test_esprit",0,0),[Patern(("test_esprit",0,0),10,10,[],[],False)])
        #Un labyrinthe avec des armes à utiliser
        self.labs["armurerie"] = Labyrinthe("armurerie",10,10,("armurerie",0,0),[Patern(("armurerie",0,0),10,10,[])])

        #On rajoute un joueur ;
        self.entitees[2] = Joueur(("test_magies",2,2),screen) #Ne fonctionne que si on vient de faire l'init

        #On place la barrière du labyrinthe "test_barriere"
        self.set_barriere_classe(("test_barriere",9,6),DROITE,Item)

        #On place la clé du labyrinthe 0
        self.ajoute_entitee(Cle((0,0,0),["test_code"]))

        #On prépare quelques passages entre les labyrinthes
        self.set_teleport(("test_magies",0,2),(0,19,2),GAUCHE,DROITE)
        self.set_teleport(("test_magies",2,0),("armurerie",9,9),HAUT,BAS)
        self.set_teleport(("test_magies",4,2),("test_barriere",0,19),DROITE,GAUCHE)
        self.set_teleport(("test_magies",2,4),("test_esprit",1,0),BAS,HAUT)
        self.set_teleport((0,0,4),(1,19,17),GAUCHE,DROITE)
        self.set_teleport((1,0,10),("test_barriere",19,17),GAUCHE,DROITE)

        #On place un poison dans le labyrinthe 0, et son antidote
        self.ajoute_entitee(Potion_empoisonnee((0,2,2)))
        self.ajoute_entitee(Potion_antidote((0,8,9)))
        #On place aussi un parchemin qui peut servir d'antidote dans le labyrinthe 1
        self.ajoute_entitee(Parchemin_purification((1,17,9)))

        #On place des parchemins pour apprendre des sorts dans le labyrinthe "test_magie"
        self.ajoute_entitee(Poly_soin(("test_magies",0,0)))
        self.ajoute_entitee(Poly_auto_soin(("test_magies",0,0)))
        self.ajoute_entitee(Poly_soin_zone(("test_magies",0,0)))
        self.ajoute_entitee(Poly_resurection(("test_magies",0,1)))
        self.ajoute_entitee(Poly_boule_de_feu(("test_magies",4,1)))
        self.ajoute_entitee(Poly_reanimation(("test_magies",4,2)))

        #On place des équippements dans le labyrinthe "armurerie"
        self.ajoute_entitee(Armure_type(("armurerie",5,6),0.5))
        self.ajoute_entitee(Haume_type(("armurerie",6,7),0.75))
        self.ajoute_entitee(Epee(("armurerie",3,7),TERRE,5,2))
        self.ajoute_entitee(Lance(("armurerie",4,7),TERRE,10,3))
        self.ajoute_entitee(Anneau_magique(("armurerie",0,0),1.2))
        self.ajoute_entitee(Anneau_magique(("armurerie",0,1),1.2))
        self.ajoute_entitee(Anneau_magique(("armurerie",0,2),1.2))
        self.ajoute_entitee(Anneau_magique(("armurerie",0,3),1.2))
        self.ajoute_entitee(Anneau_magique(("armurerie",0,4),1.2))
        self.ajoute_entitee(Anneau_de_vitalite(("armurerie",0,5),1.2))
        self.ajoute_entitee(Anneau_de_vitalite(("armurerie",0,6),1.2))
        self.ajoute_entitee(Anneau_de_vitalite(("armurerie",0,7),1.2))
        self.ajoute_entitee(Anneau_de_vitalite(("armurerie",0,8),1.2))
        self.ajoute_entitee(Anneau_de_vitalite(("armurerie",0,9),1.2))

        self.esprits["1"] = Esprit_defensif("1",2,self,("test_esprit",0,0))
        self.esprits["2"] = Esprit_bourrin("2",2,self,("test_esprit",9,4))
        self.esprits["1"].antagonise("2")
        self.esprits["2"].antagonise("1")

        self.esprits["Joueur"] = Esprit_solitaire("Joueur",2,self) #L'esprit du joueur
        self.active_lab(self.entitees[2].position[0])

    def tuto(self,screen):
        #On crée le joueur :
        joueur = Joueur(("Étage 1 : couloir",13,0),screen)
        self.ajoute_entitee(joueur) #Est-ce qu'il est à cet étage dès le début ? Même pendant la cinématique ?
        self.esprits["joueur"] = Esprit_humain(joueur.ID,self)

        #On crée le premier étage et son occupant :
        receptionniste = Receptionniste(("Étage 1 : couloir",14,0))
        self.ajoute_entitee(receptionniste)
        self.esprits["receptionniste"] = Esprit_humain(receptionniste.ID,self)
        paterns1 = [Patern(("Étage 1 : couloir",9,0),10,3,[("Étage 1 : couloir",0,1)],["clé couloir"])]
        self.labs["Étage 1 : couloir"]=Labyrinthe("Étage 1 : couloir",19,3,("Étage 1 : couloir",0,0),paterns1,1,1,TERRE,1)

        #On crée le deuxième étage et son occupant :
        paume = Paume(("Étage 2 : labyrinthe",1,0))
        self.ajoute_entitee(paume)
        self.esprits["paume"] = Esprit_humain(paume.ID,self)
        paterns2 = [Patern(("Étage 2 : labyrinthe",0,0),5,5,[("Étage 2 : labyrinthe",4,1),("Étage 2 : labyrinthe",4,2),("Étage 2 : labyrinthe",4,3)]),
                    Patern(("Étage 2 : labyrinthe",5,5),5,5,[("Étage 2 : labyrinthe",0,1)],["Porte_centre_2"])]
        self.labs["Étage 2 : labyrinthe"]=Labyrinthe("Étage 2 : labyrinthe",15,15,("Étage 2 : labyrinthe",0,0),paterns2,1,1,TERRE,0.5)
        self.construit_escalier(("Étage 1 : couloir",18,1),("Étage 2 : labyrinthe",0,0),DROITE,GAUCHE)

        #On crée le troisième étage et son occupante :
        peureuse = Peureuse(("Étage 3 : combat",12,13))
        self.ajoute_entitee(peureuse)
        self.esprits["peureuse"] = Esprit_humain(peureuse.ID,self)
        cle1 = Cle(("Étage 3 : combat",12,13),"Porte_entree_encombrant_5")
        self.ajoute_entitee(cle1)
        peureuse.inventaire.ajoute(cle1)
        cle2 = Cle(("Étage 3 : combat",12,13),"Porte_contournement_encombrant_5")
        self.ajoute_entitee(cle2)
        peureuse.inventaire.ajoute(cle2)
        gobel1 = Sentinelle_gobelin(("Étage 3 : combat",11,5),1) #Trois sentinelles gardent l'entrée du camp gobelin
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(("Étage 3 : combat",5,11),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Sentinelle_gobelin(("Étage 3 : combat",6,6),1)
        self.ajoute_entitee(gobel3)
        self.esprits["gobelins_combat"]=Esprit_simple("gobelins_combat",[gobel1.ID,gobel2.ID,gobel3.ID],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns3 = [Patern(("Étage 3 : combat",6,6),9,9,[("Étage 3 : combat",0,4),("Étage 3 : combat",4,0),("Étage 3 : combat",0,0)]),
                    Patern(("Étage 3 : combat",5,5),3,3,[("Étage 3 : combat",0,0),("Étage 3 : combat",2,2)]),
                    Patern(("Étage 3 : combat",10,4),3,3,[("Étage 3 : combat",1,0),("Étage 3 : combat",1,2)]),
                    Patern(("Étage 3 : combat",4,10),3,3,[("Étage 3 : combat",2,1),("Étage 3 : combat",0,1)])]
        self.labs["Étage 3 : combat"]=Labyrinthe("Étage 3 : combat",15,15,("Étage 3 : combat",0,0),paterns3,1,1,TERRE,0.4)
        self.construit_escalier(("Étage 2 : labyrinthe",1,5),("Étage 3 : combat",14,14),HAUT,BAS)

        #On crée le quatrième étage et son occupant :
        codeur = Codeur(("Étage 4 : monstres",15,1))
        self.ajoute_entitee(codeur)
        self.esprits["codeur"] = Esprit_humain(codeur.ID,self)
        gobel1 = Sentinelle_gobelin(("Étage 4 : monstres",23,13),1) #Une sentinelle garde les abords
        self.ajoute_entitee(gobel1)
        gobel2 = Gobelin(("Étage 4 : monstres",21,7),1) #Un gobelin standard s'y balade
        self.ajoute_entitee(gobel2)
        gobel3 = Mage_gobelin(("Étage 4 : monstres",15,5),1) #Ainsi qu'un mage,
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(("Étage 4 : monstres",4,5),1) #et deux guerriers
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(("Étage 4 : monstres",5,5),1)
        self.ajoute_entitee(gobel5)
        self.esprits["gobelins_monstres"]=Esprit_simple("gobelins_monstres",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns4 = [Patern(("Étage 4 : monstres",4,0),10,2,[("Étage 4 : monstres",0,1)],[],False),
                    Patern(("Étage 4 : monstres",14,0),3,3,[("Étage 4 : monstres",0,1)]),
                    Patern(("Étage 4 : monstres",0,10),8,5,[("Étage 4 : monstres",7,2)],["Porte_coin_4"]),
                    Patern(("Étage 4 : monstres",20,5),10,4,[("Étage 4 : monstres",2,0),("Étage 4 : monstres",5,0),("Étage 4 : monstres",6,0),("Étage 4 : monstres",8,0)],[],False)]
        self.labs["Étage 4 : monstres"]=Labyrinthe("Étage 4 : monstres",30,15,("Étage 4 : monstres",0,0),paterns4,1,1,TERRE,0.35)
        self.construit_escalier(("Étage 3 : combat",0,3),("Étage 4 : monstres",29,7),GAUCHE,DROITE)

        #On crée le cinquième étage et ses occupant :
        encombrant = Encombrant(("Étage 5 : portes",2,3))
        self.ajoute_entitee(encombrant)
        self.esprits["encombrant"] = Esprit_humain(encombrant.ID,self)
        passepartout1 = Cle(("Étage 5 : portes",8,22),["Porte_cellule_slime_5","Porte_cellule_piège_5","Porte_cellule_pré-piège_5","Porte_petite_cellule_droite_5"])
        self.ajoute_entitee(passepartout1)
        passepartout2 = Cle(("Étage 5 : portes",9,18),["Porte_double_cellule_deuxième_5","Porte_petite_cellule_gauche_5","Porte_grande_cellule_droite_5"])
        self.ajoute_entitee(passepartout2)
        cle1 = Cle(("Étage 5 : portes",4,15),["Porte_grande_cellule_5"])
        self.ajoute_entitee(cle1)
        cle2 = Cle(("Étage 5 : portes",0,9),["Porte_cellule_ombriul_5"])
        self.ajoute_entitee(cle2)
        cle3 = Cle(("Étage 5 : portes",9,10),["Porte_double_cellule_première_5"])
        self.ajoute_entitee(cle3)
        cle4 = Cle(("Étage 5 : portes",1,4),["Porte_sortie_encombrant_5"])
        self.ajoute_entitee(cle4)
        gobel1 = Sentinelle_gobelin(("Étage 5 : portes",23,13),1) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel1)
        gobel2 = Guerrier_gobelin(("Étage 5 : portes",4,5),2) #Un renégat mis à l'isolement pour le mater, ou un piège diabolique dirigé contre le joueur ?
        self.ajoute_entitee(gobel2)
        slime = Slime(("Étage 5 : portes",4,5),1) #Un slime ! Est-ce que les gobelins ont pris soin de l'affaiblir ?
        self.ajoute_entitee(slime)
        ombriul = Ombriul(("Étage 5 : portes",4,5),1) #Un prisonnier de guerre
        self.ajoute_entitee(ombriul)
        self.esprits["gobelins_portes"]=Esprit_simple("gobelins_portes",[gobel1.ID,gobel2.ID],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        self.esprits["ombriul_captif"]=Esprit_simple("ombriul_captif",[ombriul.ID],self)
        esprit_slime = Esprit_slime([slime],self)
        self.esprits[esprit_slime.nom]=esprit_slime #Les esprits des slimes sont presque aussi compliqués que ceux des humains, les ruptures en moins.
        paterns5 = [Patern(("Étage 5 : portes",0,0),10,24,[]),
                    Patern(("Étage 5 : portes",0,1),5,5,[("Étage 5 : portes",1,0),("Étage 5 : portes",4,2)],["Porte_sortie_encombrant_5","Porte_entree_encombrant_5"]),
                    Patern(("Étage 5 : portes",0,6),3,3,[("Étage 5 : portes",2,1)],["Porte_double_cellule_deuxième_5"]),
                    Patern(("Étage 5 : portes",3,6),3,3,[("Étage 5 : portes",2,1)],["Porte_double_cellule_première_5"]),
                    Patern(("Étage 5 : portes",0,9),4,7,[("Étage 5 : portes",3,4)],["Porte_grande_cellule_5"]),
                    Patern(("Étage 5 : portes",0,16),3,3,[("Étage 5 : portes",2,1)],["Porte_petite_cellule_gauche_5"]),
                    Patern(("Étage 5 : portes",0,19),4,4,[("Étage 5 : portes",3,2)],["Porte_cellule_slime_5"]),
                    Patern(("Étage 5 : portes",6,0),4,4,[("Étage 5 : portes",2,3)],["Porte_cellule_piège_5"]),
                    Patern(("Étage 5 : portes",7,4),3,6,[("Étage 5 : portes",0,3)],["Porte_cellule_pré-piège_5"]),
                    Patern(("Étage 5 : portes",5,10),5,3,[("Étage 5 : portes",1,0)],["Porte_cellule_ombriul_5"]),
                    Patern(("Étage 5 : portes",6,13),4,5,[("Étage 5 : portes",0,2)],["Porte_grande_cellule_droite_5"]),
                    Patern(("Étage 5 : portes",7,18),3,3,[("Étage 5 : portes",0,1)],["Porte_petite_cellule_droite_5"])]
        self.labs["Étage 5 : portes"]=Labyrinthe("Étage 5 : portes",10,24,("Étage 5 : portes",0,0),paterns5)
        self.construit_escalier(("Étage 4 : monstres",29,14),("Étage 5 : portes",0,23),DROITE,GAUCHE) #/!\ Modifier le layout de ce niveau !

        #On crée le sixième étage et son occupant :
        alchimiste = Alchimiste(("Étage 6 : potions",2,0))
        self.ajoute_entitee(alchimiste)
        self.esprits["alchimiste"] = Esprit_humain(alchimiste.ID,self)
        self.labs["Étage 6 : potions"]=Labyrinthe("Étage 6 : potions",10,60,("Étage 6 : potions",0,0),[Patern(("Étage 6 : potions",4,0),2,10,[("Étage 6 : potions",0,9),("Étage 6 : potions",1,9)]),Patern(("Étage 6 : potions",1,13),8,8,[("Étage 6 : potions",4,0),("Étage 6 : potions",5,7)]),Patern(("Étage 6 : potions",1,25),6,8,[("Étage 6 : potions",4,0),("Étage 6 : potions",5,7)]),Patern(("Étage 6 : potions",2,40),8,8,[("Étage 6 : potions",4,0),("Étage 6 : potions",5,7)]),Patern(("Étage 6 : potions",4,52),5,8,[("Étage 6 : potions",4,0)])])
        self.construit_escalier(("Étage 5 : portes",4,0),("Étage 6 : potions",5,0),HAUT,HAUT) #/!\ Modifier le layout de ce niveau !

        #On crée le septième étage et son occupante :
        peste = Peste(("Étage 7 : meutes",2,0))
        self.ajoute_entitee(peste)
        self.esprits["peste"] = Esprit_humain(peste.ID,self)
        self.labs["Étage 7 : meutes"]=Labyrinthe("Étage 7 : meutes",10,60,("Étage 7 : meutes",0,0),[Patern(("Étage 7 : meutes",4,0),2,10,[("Étage 7 : meutes",0,9),("Étage 7 : meutes",1,9)]),Patern(("Étage 7 : meutes",1,13),8,8,[("Étage 7 : meutes",4,0),("Étage 7 : meutes",5,7)]),Patern(("Étage 7 : meutes",1,25),6,8,[("Étage 7 : meutes",4,0),("Étage 7 : meutes",5,7)]),Patern(("Étage 7 : meutes",2,40),8,8,[("Étage 7 : meutes",4,0),("Étage 7 : meutes",5,7)]),Patern(("Étage 7 : meutes",4,52),5,8,[("Étage 7 : meutes",4,0)])])
        self.construit_escalier(("Étage 6 : potions",4,0),("Étage 7 : meutes",5,0),HAUT,HAUT) #/!\ Modifier le layout de ce niveau !

        #On crée le huitième étage et son occupante :
        bombe_atomique = Bombe_atomique(("Étage 8 : magie",2,0))
        self.ajoute_entitee(bombe_atomique)
        self.esprits["bombe_atomique"] = Esprit_humain(bombe_atomique.ID,self)
        self.labs["Étage 8 : magie"]=Labyrinthe("Étage 8 : magie",10,60,("Étage 8 : magie",0,0),[Patern(("Étage 8 : magie",4,0),2,10,[("Étage 8 : magie",0,9),("Étage 8 : magie",1,9)]),Patern(("Étage 8 : magie",1,13),8,8,[("Étage 8 : magie",4,0),("Étage 8 : magie",5,7)]),Patern(("Étage 8 : magie",1,25),6,8,[("Étage 8 : magie",4,0),("Étage 8 : magie",5,7)]),Patern(("Étage 8 : magie",2,40),8,8,[("Étage 8 : magie",4,0),("Étage 8 : magie",5,7)]),Patern(("Étage 8 : magie",4,52),5,8,[("Étage 8 : magie",4,0)])])
        self.construit_escalier(("Étage 7 : meutes",4,0),("Étage 8 : magie",5,0),HAUT,HAUT) #/!\ Modifier le layout de ce niveau !

        #On crée le neuvième étage et son occupant :
        marchand = Marchand(("Étage 9 : équippement",2,0))
        self.ajoute_entitee(marchand)
        self.esprits["marchand"] = Esprit_humain(marchand.ID,self)
        self.labs["Étage 9 : équippement"]=Labyrinthe("Étage 9 : équippement",10,60,("Étage 9 : équippement",0,0),[Patern(("Étage 9 : équippement",4,0),2,10,[("Étage 9 : équippement",0,9),("Étage 9 : équippement",1,9)]),Patern(("Étage 9 : équippement",1,13),8,8,[("Étage 9 : équippement",4,0),("Étage 9 : équippement",5,7)]),Patern(("Étage 9 : équippement",1,25),6,8,[("Étage 9 : équippement",4,0),("Étage 9 : équippement",5,7)]),Patern(("Étage 9 : équippement",2,40),8,8,[("Étage 9 : équippement",4,0),("Étage 9 : équippement",5,7)]),Patern(("Étage 9 : équippement",4,52),5,8,[("Étage 9 : équippement",4,0)])])
        self.construit_escalier(("Étage 8 : magie",6,0),("Étage 9 : équippement",5,0),HAUT,HAUT) #/!\ Modifier le layout de ce niveau !

        #On crée le dixième étage
        self.labs["Étage 10 : Boss"]=Labyrinthe("Étage 10 : Boss",10,60,("Étage 10 : Boss",0,0),[Patern(("Étage 10 : Boss",4,0),2,10,[("Étage 10 : Boss",0,9),("Étage 10 : Boss",1,9)]),Patern(("Étage 10 : Boss",1,13),8,8,[("Étage 10 : Boss",4,0),("Étage 10 : Boss",5,7)]),Patern(("Étage 10 : Boss",1,25),6,8,[("Étage 10 : Boss",4,0),("Étage 10 : Boss",5,7)]),Patern(("Étage 10 : Boss",2,40),8,8,[("Étage 10 : Boss",4,0),("Étage 10 : Boss",5,7)]),Patern(("Étage 10 : Boss",4,52),5,8,[("Étage 10 : Boss",4,0)])])
        self.construit_escalier(("Étage 9 : équippement",4,0),("Étage 10 : Boss",5,0),BAS,HAUT) #/!\ Modifier le layout de ce niveau !

        #On lance la cinématique :
        #À rajouter
        #Et on active le lab du joueur
        self.active_lab("Étage 1 : couloir")

    def duel(self,esprit1,esprit2,niveau_1=1,niveau_2=1,tailles_lab=(20,20),vide=True,vue=False,screen=None):
        """Fonction qui crée les conditions d'un duel."""

        if vue : # On peut avoir des spectateurs, mais pas forcément
            self.ajoute_entitee(Joueur(("arène",tailles_lab[0]//2,tailles_lab[1]//2),screen))
        # Première étape : créer l'arène
        self.labs["arène"]=Labyrinthe("arène",tailles_lab[0],tailles_lab[1],("arène",0,0),[Patern(("arène",0,0),tailles_lab[0],tailles_lab[1],[],[],vide)])
        # Deuxième étape : créer les opposants
        self.esprits["1"] = esprit1("1",niveau_1,self,("arène",0,0))
        self.esprits["2"] = esprit2("2",niveau_2,self,("arène",tailles_lab[0]-1,0))
        # Troisième étape : créer un conflit
        self.esprits["1"].antagonise("2")
        self.esprits["2"].antagonise("1")
        # Quatrième étape : admirer
        self.active_lab("arène")

    def set_phase(self,phase):
        if phase not in self.phases : #On ne veut pas avoir deux fois la même phase !
            self.phases.append(phase) #La dernière phase est toujours la phase active !
        self.phase = phase # /!\ Rajouter des conditions ici ! Certaines phases ne peuvent pas être interrompues par d'autres
        if phase == TOUR:
            pygame.key.set_repeat()
        else:
            pygame.key.set_repeat(400,200)

    def unset_phase(self,phase):
        if phase in self.phases :
            self.phases.remove(phase)
        self.phase = self.phases[-1]

    def set_barriere_classe(self,position,direction,classe):
        self.active_lab(position[0])
        mur = self.labs[position[0]].matrice_cases[position[1]][position[2]].murs[direction]
        mur.brise()
        mur.effets.append(Barriere_classe(classe))
        mur_opp = mur.get_mur_oppose()
        if mur_opp != None:
            mur_opp.brise()
            mur_opp.effets.append(Barriere_classe(classe))
        self.desactive_lab(position[0])

    def active_lab(self,key): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour activer un nouveau labyrinthe. En entrée, la clé du labyrinthe à activer.
           Un étage, en règle générale, est "inactif", c'est à dire que ses occupants ne bougent pas. Il devient "actif" quand une entitée y entre, pour 5 tours si c'est une entitée basique, et jusqu'à 5 tours après son départ si c'est une entitée supérieure (joueur, dev, kumoko, etc.).
           Lorsque le labyrinthe est "activé", sa clé (qui l'indexe dans le dictionnaire des labs et se retrouve dans la coordonées de position verticale de ses occupants) est ajoutée aux labs_courants. On cherche parmis les entitées celles qui se trouvent dans ce lab et on rajoute leur identifiant aux entitées courantes.
           Dans la version définitive, cette fonction sera appelée à la fin de la chute pour passer le joueur dans le niveau 1."""
        #On active le lab :
        self.labs[key].active(self) #On lui donne le controleur pour qu'il puisse l'appeler au besoin.
        #On cherche ses occupants :
        for ke in self.entitees.keys() :
            entitee = self.get_entitee(ke)
            position = entitee.get_position()
            if position != None: #Il y a des entitees dans les inventaires
                if position[0] == key : #La position commence par la coordonnée verticale.
                    if not ke in self.entitees_courantes:
                        self.entitees_courantes.append(ke)
                    entitee.active(self)
        if not key in self.labs_courants:
            self.labs_courants.append(key)

    def desactive_lab(self,key): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour désactiver un labyrinthe actif. En entrée, la clé du labyrinthe à désactiver.
           Tout labyrinthe se désactive après 5 tours d'absence d'entitée supérieure (joueur, dev, kumoko, etc.).
           Le lab actif possédant le controleur en attribut, il appelle cette fonction lui-même quand son compteur interne tombe à 0."""
        #On desactive les occupants du lab :
        for ke in self.entitees.keys() : #Normalement on a déjà vérifié qu'il n'y a pas d'entitée supérieure...
            entitee = self.get_entitee(ke)
            position = entitee.get_position()
            if position != None: #Il y a des entitees dans les inventaires
                if position[0] == key : #La position commence par la coordonnée verticale.
                    if ke in self.entitees_courantes:
                        self.entitees_courantes.remove(ke)
                    entitee.desactive()
        if key in self.labs_courants:
            self.labs_courants.remove(key)

    def move(self,position,entitee): #Non utilisé dans la version de mi-juillet
        """Fonction appelée quand une entitée change de labyrinthe. En entrée, la position cible et l'entitée avant son déplacement.
           Si le labyrinthe de départ n'a plus d'entitée supérieure, on va devoir préparer sa désactivation. Si le labyrinthe d'arrivée n'avait pas d'entitée supérieure, il va falloir l'activer."""
        ancien_lab = entitee.get_position()[0]
        nouveau_lab = position[0]
        if isinstance(entitee,Entitee_superieure): #Si on a une entitée supérieure :
            if not(nouveau_lab in self.labs_courants) : #On active si nécessaire
                self.active_lab(nouveau_lab)
            elif self.labs[nouveau_lab].temps_restant != -1: #On maintient activé jusqu'à nouvel ordre si nécessaire (sinon, c'est qu'il y a déjà une entitée supérieure dans le labyrinthe, on a rien à faire)
                self.labs[nouveau_lab].temps_restant = -1
        else : #Si on a une entitée normale :
            if not(nouveau_lab in self.labs_courants) :
                self.active_lab(nouveau_lab) #On active si nécessaire...
                self.labs[nouveau_lab].quitte() #...Mais on quittera bientôt
            elif self.labs[nouveau_lab].temps_restant != -1:
                self.labs[nouveau_lab].quitte() #On quittera un peu plus tard si nécessaire (sinon, c'est qu'il y a une entitée supérieure dans le labyrinthe, on a rien à faire)
            
        entitee.set_position(position) #L'entitée se déplace, elle et toutes ses possessions (notamment l'inventaire !)
        #On cherche une éventuelle entitée supérieure dans l'ancien labyrinthe :
        sup = False
        for key_entitee in self.entitees_courantes :
            position = self.entitees[key_entitee].get_position()
            if position != None:
                if (position[0] == ancien_lab) and isinstance(self.entitees[key_entitee],Entitee_superieure):
                    sup = True
        if not(sup): #On n'a pas d'entitee supérieure dans le labyrinthe
            self.labs[ancien_lab].quitte() #On lance le décompte de 5 tours (faire + de 5 tours ?)

    def get_lab(self,num_lab):
        return self.labs[num_lab]

    def set_teleport(self,pos_dep,pos_arr,dir_dep,dir_arr):
        case_dep = self.get_case(pos_dep)
        case_arr = self.get_case(pos_arr)
        mur_dep = case_dep.get_mur_dir(dir_dep)
        mur_arr = case_arr.get_mur_dir(dir_arr)
        mur_dep.detruit()
        mur_arr.detruit()
        mur_dep.set_cible(pos_arr,True)
        mur_arr.set_cible(pos_dep,True)

    def construit_escalier(self,pos_dep,pos_arr,dir_dep,dir_arr):
        case_dep = self.get_case(pos_dep)
        case_arr = self.get_case(pos_arr)
        mur_dep = case_dep.get_mur_dir(dir_dep)
        mur_arr = case_arr.get_mur_dir(dir_arr)
        mur_dep.detruit()
        mur_arr.detruit()
        mur_dep.set_escalier(pos_arr,HAUT) #Par convention, la première case est en bas
        mur_arr.set_escalier(pos_dep,BAS)

    def get_case(self,position):
        return self.get_lab(position[0]).get_case(position)

    def make_vue(self,agissant):
        position = agissant.get_position()
        num_lab = position[0]
        labyrinthe = self.get_lab(num_lab)
        vue = labyrinthe.get_vue(agissant)
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                if vue[i][j][1] > 0:
                    vue[i][j][8] = self.trouve_occupants((num_lab,i,j)) #À changer quand les positions seront tridimensionnelles !
        agissant.vue = vue

    def voit_occupants(self,position): #Pour l'instant le joueur est le seul agissant.
        occupants = self.trouve_occupants(position)
        images = []
        for occupant in occupants:
            images.append(self.get_entitee(occupant).get_image())
        return images

    def est_item(self,entitee):
        return issubclass(self.get_entitee(entitee).get_classe(),Item)

    def trouve_items(self,position):
        occupants = self.trouve_occupants(position)
        items = []
        for occupant in occupants:
            if self.est_item(occupant):
                items.append(occupant)
        return items

    def trouve_agissants(self,position):
        occupants = self.trouve_occupants(position)
        agissants = []
        for occupant in occupants:
            if not self.est_item(occupant):
                agissants.append(occupant)
        return agissants

    def trouve_occupants(self,position):
        occupants = []
        for entitee in self.entitees.keys():
            if self.get_entitee(entitee).get_position() == position:
                occupants.append(entitee)
        return occupants

    def fait_agir(self,agissant):
        type_skill = agissant.skill_courant
        skill = trouve_skill(agissant.classe_principale,type_skill)
        if skill == None :
            print("On ne peut pas utiliser un skill que l'on n'a pas... et on ne devrait pas pouvoir le choisir d'ailleurs : "+str(type_skill))
        else :



            if type_skill == Skill_analyse: #À améliorer ! /!\
                mallus,niveau,cible = skill.utilise()
                self.lance_analyse(mallus,niveau,cible)



            elif type_skill == Skill_vol:
                possesseur,item = self.selectionne_item_vol()
                latence,reussite = skill.utilise(possesseur.priorite,agissant.priorite)
                agissant.add_latence(latence)
                if reussite :
                    possesseur.inventaire.supprime_item(item)
                    agissant.inventaire.ramasse_item(item)
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("Tu as volé avec succès un "+item+" à "+victime+" !")
                else :
                    possesseur.persecuteurs.append(agissant.ID)
                #refaire les autres vols sur le même modèle /!\



            elif type_skill == Skill_ramasse:
                items = self.trouve_items(agissant.get_position())
                latence = 1
                for ID_item in items:
                    item = self.get_entitee(ID_item)
                    latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
                    latence += latence_item
                    if reussite:
                        agissant.inventaire.ramasse_item(ID_item)
                agissant.add_latence(latence)



            elif type_skill == Skill_stomp:
                #Une attaque qui se fait sans arme.
                force,affinite,direction,ID = agissant.get_stats_attaque(TERRE)
                latence,taux,portee = skill.utilise()

                degats = force*taux*affinite
                attaque = Attaque(ID,degats,TERRE,portee)

                agissant.add_latence(latence)
                agissant.effets.append(attaque)



            elif type_skill == Skill_attaque:
                #Une attaque qui se fait avec une arme.
                arme = agissant.get_arme()
                if arme == None:
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("Tu n'as pas d'arme ?") #Sans arme, on devrait utiliser le stomp.
                        affichage.message("Essaye le stomp !") # !! À modifier pour indiquer la touche courante du stomp, si elle existe !!!
                else:
                    arme = self.get_entitee(arme)
                    element,tranchant,portee = arme.get_stats_attaque()
                    force,affinite,direction,ID = agissant.get_stats_attaque(element)
                    latence,taux = skill.utilise()

                    taux_manipulation = 1
                    manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
                    if manipulation != None :
                        taux_manipulation = manipulation.utilise_attaque()

                    if isinstance(arme,Epee) :
                        if manipulation == None :
                            manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_epee)
                            if manipulation != None :
                                taux_manipulation = manipulation.utilise()

                        forme = "Sd_S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes

                    elif isinstance(arme,Lance) :
                        if manipulation == None :
                            manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_lance)
                            if manipulation != None :
                                taux_manipulation = manipulation.utilise()

                        forme = "R__S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes
                    else :
                        print("Quelle est cette arme ? " + agissant.arme)

                    degats = force*affinite*tranchant*taux*taux_manipulation
                    attaque = Attaque(ID,degats,element,portee,forme,direction)

                    agissant.add_latence(latence)
                    agissant.effets.append(attaque)



            elif type_skill == Skill_blocage :
                #Pour être protégé par le bouclier pendant les tours suivants.
                bouclier = agissant.get_bouclier()
                if bouclier == None:
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("Tu n'as pas de bouclier !") #Sans bouclier, on devrait se mettre à couvert.
                        affichage.message("Tu devrais esquiver, plutôt.")
                else:
                    latence,taux_skill = skill.utilise()

                    taux_manipulation = 1
                    duree = 3
                    manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
                    if manipulation != None :
                        taux_manipulation,duree = manipulation.utilise()
                    else :
                        manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_bouclier)
                        if manipulation != None :
                            taux_manipulation,duree = manipulation.utilise()

                    taux = taux_skill * taux_manipulation

                    effet = Protection(duree,bouclier) #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres effets

                    for effet_prec in agissant.effets :
                        if isinstance(effet_prec,Protection):
                            agissant.effets.remove(effet_prec) #On ne peut pas avoir deux protections à la fois !

                    agissant.add_latence(latence)
                    agissant.effets.append(effet)
                    effet.execute(agissant) #On passe l'effet en phase "en cours"
                    bouclier.taux_defense["protection"] = taux



            elif type_skill == Skill_lancer :
                projectile = agissant.get_item_lancer()

                if projectile != None :
                    if isinstance(projectile,int): #Un agissant bien élevé manipule le moins d'objets possible, et leur préfère leurs ID
                        projectile = self.get_entitee(projectile)
                    latence,hauteur,vitesse = skill.utilise()
                    agissant.add_latence(latence*projectile.poids)
                    projectile.position = agissant.get_position()
                    projectile.hauteur = hauteur*agissant.force/projectile.poids
                    projectile.taux_vitesse["lancementv"]=vitesse
                    projectile.direction = agissant.dir_regard
                    projectile.lanceur = agissant.ID
                    self.entitees_courantes.append(projectile.ID)
                    if projectile.controleur == None:
                        projectile.active(self)
                else :
                    if isinstance(agissant,Joueur):
                        affichage = agissant.affichage
                        affichage.message("J'ai dû mal comprendre...")
                        affichage.message("Tu veux lancer un item que tu n'as pas ?")



            elif type_skill in [Skill_deplacement,Skanda,Lesser_Skanda]:
                latence,niveau = skill.utilise()
                direction = agissant.get_direction()
                position = agissant.get_position()
                agissant.add_latence(latence)

                lab = self.get_lab(position[0])
                lab.veut_passer(agissant,direction)



            elif type_skill == Skill_soin :
                latence,soin,portee = skill.utilise()
                agissant.add_latence(latence)
                self.soigne(agissant,agissant.get_position(),portee,soin)



            elif type_skill == Skill_regeneration_MP :
                latence,regen,portee = skill.utilise()
                agissant.add_latence(latence)
                self.regenere(agissant,agissant.get_position(),portee,regen)



            elif type_skill in [Skill_reanimation,Skill_reanimation_renforcee] :
                cadavre = selectionne_item_cadavre()
                latence,taux,sup = skill.utilise()
                agissant.add_latence(latence)
                if cadavre.priorite + sup < agissant.priorite :
                    esprit = self.get_esprit(agissant)
                    cadavre.effets.append(Reanimation(taux,esprit))
                else:
                    cadavre.effets.append(Reanimation(taux,self.get_esprit(cadavre)))


            elif type_skill in [Skill_magie,Height_of_Occultism,Lesser_Height_of_Occultism] :
                nom_magie = agissant.magie_courante
                latence,magie = skill.utilise(nom_magie)
                cout = magie.cout_pm
                if agissant.peut_payer(cout) :
                    agissant.effets.append(magie)
                    reussite = True
                    #if isinstance(agissant,Joueur):
                    #    malchance = trouve_skill(agissant.classe_principale,Skill_malchanceux)
                    #else:
                    #    malchance = None
                    #if malchance != None:
                    #    reussite = malchance.utilise("cast_magic")
                    if isinstance(magie,Magie_cible) :
                        self.select_cible(magie,agissant)
                    if isinstance(magie,Magie_dirigee) :
                        self.select_direction(magie,agissant)
                    if isinstance(magie,Magie_cout) :
                        self.select_cout(magie,agissant)
                    agissant.paye(magie.cout_pm)
                    agissant.add_latence(latence)
                    if not reussite :
                        magie.miss_fire(agissant)



            elif type_skill in [Divine_Thread_Weaving,Lesser_Divine_Thread_Weaving] :
                action = agissant.action
                latence,item = skill.utilise(action)
                agissant.add_latence(latence)
                self.items.append(item)



            elif type_skill in [Scythe,Lesser_Scythe] :
                perce,element,taux = skill.utilise()
                attaque = Attaque(agissant.ID,agissant.force*taux,element,1,"R__T_Pb",agissant.direction,"piercing",perce)
                self.tentative_attaque(attaque)



            elif type_skill == Egg_Laying:
                latence, oeuf = skill.utilise()
                agissant.add_latence(latence)
                if oeuf != None :
                    self.ajoute_entitee(oeuf)



            elif type_skill == Skill_merge:
                ID_cible = agissant.cible_merge
                latence = skill.utilise()
                if ID_cible != None:
                    esprit = self.get_entitee(ID_cible).esprit
                    self.get_esprit(agissant.esprit).merge(esprit) #/!\ Syntaxe probablement fausse et foireuse, à vérifier
                agissant.add_latence(latence)



            elif type_skill == Skill_absorb:
                items = self.trouve_items(agissant.get_position())
                latence = 1
                for ID_item in items:
                    item = self.get_entitee(ID_item)
                    latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
                    latence += latence_item
                    if reussite:
                        agissant.inventaire.ramasse_item(ID_item)
                        if item.get_classe() == Cadavre:
                            pass #/!\ Comment le skill est choisi ? Au hasard ? Comment différencier le type de slime (copie le skill au niveau 1, copie le skill à son niveau, vole le skill et laisse une copie au niveau 1, prend le skill mais le laisse quand même)
                agissant.add_latence(latence)



            elif type_skill == Skill_divide:
                latence = skill.utilise()
                if agissant.peut_payer(20) #Insérer le cout ici d'une façon ou d'une autre /!\
                    new_slime = type(agissant)(agissant.position,agissant.niveau,True)
                    agissant.paye(20)
                    agissant.subit(20) #Il perd la moitié de ses pv max et de ses pm max
                agissant.add_latence(latence)



    def fait_voler(self,item):
        direction = item.get_direction()
        position = item.get_position()
        lab = self.get_lab(position[0])
        lab.veut_passer(item,direction)

    def select_cible(self,magie,agissant):
        if random.random() < agissant.talent :
            magie.cible = agissant.cible_magie
        
    def select_direction(self,magie,agissant):
        if random.random() < agissant.talent :
            magie.direction = agissant.dir_magie

    def select_cout(self,magie,agissant):
        magie.cout_pm = agissant.cout_magie

    def get_cibles_potentielles_agissants(self,magie,joueur):
        cibles_potentielles = []
        for colonne in joueur.vue:
            for case in colonne:
                for ID_entitee in case[8]:
                    entitee = self.get_entitee(ID_entitee)
                    if not issubclass(entitee.get_classe(),Item):
                        cibles_potentielles.append(entitee)
        if isinstance(magie,Portee_limitee):
            poss = self.get_position_touches(joueur.position,magie.portee_limite)
            cibles = []
            for agissant in cibles_potentielles:
                if agissant.position in poss:
                    cibles.append(agissant.ID)
        else:
            cibles = []
            for agissant in cibles_potentielles:
                cibles.append(agissant.ID)
        return cibles

    def get_cibles_potentielles_items(self,magie,joueur):
        cibles_potentielles = []
        for colonne in joueur.vue:
            for case in colonne:
                for ID_entitee in case[8]:
                    entitee = self.get_entitee(ID_entitee)
                    if issubclass(entitee.get_classe(),Item):
                        cibles_potentielles.append(entitee)
                    else:
                        cibles_potentielles += entitee.inventaire.get_items() #/!\ Rajouter une condition d'observation ! Mais ne pas l'appliquer à soi-même !
        if isinstance(magie,Portee_limitee):
            poss = self.get_position_touches(joueur.position,magie.portee_limite)
            cibles = []
            for item in cibles_potentielles:
                if item.position in poss:
                    cibles.append(item.ID)
        else:
            cibles = []
            for item in cibles_potentielles:
                cibles.append(item.ID)
        return cibles

    def get_cibles_potentielles_cases(self,magie,joueur):
        cibles_potentielles = []
        for colonne in joueur.vue:
            for case in colonne:
                cibles_potentielles.append(case[0])
        if isinstance(magie,Portee_limitee):
            poss = self.get_positions_touches(joueur.position,magie.portee_limite)
            cibles = []
            for pos in cibles_potentielles:
                if pos in poss:
                    cibles.append(pos)
        else:
            cibles = cibles_potentielles
        return cibles

    def get_esprit(self,nom):
        if nom != None:
            return self.esprits[nom]
        else:
            return None

    def get_nom_esprit(self,corp):
        return self.get_entitee(corp).get_esprit()

    def get_entitee(self,ID):
        return self.entitees[ID]

    def ajoute_entitees(self,entitees):
        for entitee in entitees:
            self.ajoute_entitee(entitee)

    def ajoute_entitee(self,entitee):
        self.entitees[entitee.ID]=entitee
        if entitee.position != None:
            if entitee.position[0] in self.labs_courants:
                entitee.active(self)
                self.entitees_courantes.append(entitee.ID)

    def get_entitees_etage(self,num_lab):
        entitees = []
        for ID_entitee in self.entitees_courantes:
            entitee = self.get_entitee(ID_entitee)
            if entitee.position != None:
                if self.get_entitee(ID_entitee).position[0]==num_lab:
                    entitees.append(ID_entitee)
        return entitees

    def get_agissants_items_labs_esprits(self):
        self.nb_tours+=1
        agissants = []
        items = []
        labs = []
        esprits = []
        noms_esprits = []
        for i in range(len(self.entitees_courantes)-1,-1,-1) :
            ID_entitee = self.entitees_courantes[i]
            entitee = self.get_entitee(ID_entitee)
            if isinstance(entitee,Agissant):
                if entitee.etat == "vivant" or isinstance(entitee,Joueur):
                    agissants.append(entitee)
                    esprit = entitee.get_esprit()
                    if esprit != None:
                        if not esprit in noms_esprits:
                            noms_esprits.append(esprit)
                else:
                    items.append(entitee)
            elif isinstance(entitee,Item):
                if entitee.etat == "intact":
                    items.append(entitee)
                else:
                    self.entitees_courantes.remove(ID_entitee)
                    self.entitees.pop(ID_entitee)
                    entitee.desactive()
        for niveau_lab in self.labs_courants:
            labs.append(self.labs[niveau_lab])
        for nom in noms_esprits:
            esprits.append(self.get_esprit(nom))
        return agissants, items, labs, esprits

    def get_touches(self,responsable,position,portee=1,propagation="CD_S___",direction=None,bloquable = True): #Trouve les agissants affectés par une attaque
        attaquant = self.get_entitee(responsable)
        nom_esprit = attaquant.esprit
        intouchables = []
        if nom_esprit != None:
            esprit = self.get_esprit(nom_esprit)
            intouchables = esprit.get_corps()
        else:
            intouchables = [responsable]
        labyrinthe = self.labs[position[0]]
        victimes_possibles = self.get_entitees_etage(position[0])
        obstacles = []
        for i in range(len(victimes_possibles)-1,-1,-1) :
            victime_possible = victimes_possibles[i]
            if victime_possible in intouchables :
                victimes_possibles.remove(victime_possible)
            elif bloquable:
                victime = self.get_entitee(victime_possible)
                if not issubclass(victime.get_classe(),Item):
                    position_v = victime.get_position()
                    obstacles.append(position_v)
        labyrinthe.attaque(position,portee,propagation,direction,obstacles)
        victimes = []
        for victime_possible in victimes_possibles :
            victime = self.get_entitee(victime_possible)
            if not issubclass(victime.get_classe(),Item):
                position_v = victime.get_position()
                if labyrinthe.matrice_cases[position_v[1]][position_v[2]].clarte > 0 :
                    victimes.append(victime)
        return victimes

    def get_touches_pos(self,responsable,position,portee=1,propagation = "C__S___",direction=None): #La même, mais pour les effets positifs comme les soins
        bienfaiteur = self.get_entitee(responsable)
        nom_esprit = bienfaiteur.esprit
        intouchables = []
        if nom_esprit != None:
            esprit = self.get_esprit(nom_esprit)
            intouchables = esprit.get_ennemis()
        else:
            intouchables = []
        labyrinthe = self.labs[position[0]]
        labyrinthe.attaque(position,portee,propagation,direction,[])
        beneficiaires_possibles = self.get_entitees_etage(position[0])
        beneficiaires = []
        for i in range(len(beneficiaires_possibles)-1,-1,-1) :
            beneficiaire_possible = beneficiaires_possibles[i]
            if beneficiaire_possible in intouchables :
                beneficiaires_possibles.remove(beneficiaires_possibles)
            else:
                beneficiaire = self.get_entitee(beneficiaire_possible)
                if not issubclass(beneficiaire.get_classe(),Item):
                    position_b = beneficiaire.get_position()
                    if labyrinthe.matrice_cases[position_b[1]][position_b[2]].clarte > 0 :
                        beneficiaires.append(beneficiaire)
        return beneficiaires

    def get_cadavres_touches(self,position,portee=1,propagation = "C__S___",direction = None): #La même, mais pour les effets sur les cadavres comme la réanimation
        cadavres = []
        labyrinthe = self.labs[position[0]]
        labyrinthe.attaque(position,portee,propagation,direction,[])
        cadavres_possibles = self.get_entitees_etage(position[0])
        for i in range(len(cadavres_possibles)-1,-1,-1) :
            cadavre_possible = self.get_entitee(cadavres_possibles[i])
            if cadavre_possible.get_classe() == Cadavre:
                position_c = cadavre_possible.get_position()
                if labyrinthe.matrice_cases[position_c[1]][position_c[2]].clarte > 0 :
                    cadavres.append(cadavre_possible)
        return cadavres

    def get_cases_touches(self,position,portee=1,propagation = "C__S___",direction = None,traverse="tout",responsable=0): #La même, mais pour les effets sur les cases
        cases = []
        labyrinthe = self.labs[position[0]]
        labyrinthe.attaque(position,portee,propagation,direction,[])
        for colonne in labyrinthe.matrice_cases :
            for case in colonne:
                if case.clarte > 0 :
                    cases.append(case)
        return cases

    def get_pos_touches(self,position,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0): #La même, mais pour les positions
        #On décide des obstacles:
        pos_obstacles = []
        if traverse == "rien":
            obstacles = self.get_entitees_etage(position[0])
            for ID_obstacle in obstacle:
                obstacle = self.get_entitee(ID_obstacle)
                if not issubclass(obstacle.get_classe(),Item):
                    pos_obstacles.append(obstacle.get_position())
        elif traverse == "alliés":
            obstacles_possibles = self.get_entitees_etage(position[0])
            nom_esprit = self.get_entitee(responsable).esprit
            if nom_esprit != None:
                for ID_obstacle in obstacles_possibles:
                    obstacle = self.get_entitee(ID_obstacle)
                    if not issubclass(obstacle.get_classe(),Item):
                        if obstacle.esprit != nom_esprit:
                            pos_obstacles.append(obstacle.get_position())
        elif traverse == "ennemis":
            obstacles_possibles = self.get_entitees_etage(position[0])
            nom_esprit = self.get_entitee(responsable).esprit
            if nom_esprit != None:
                for ID_obstacle in obstacles_possibles:
                    obstacle = self.get_entitee(ID_obstacle)
                    if not issubclass(obstacle.get_classe(),Item):
                        if obstacle.esprit == nom_esprit:
                            pos_obstacles.append(obstacle.get_position())
        elif traverse == "tout":
            pass
        else:
            print("Quelle est cette traversée ?")
        poss = []
        labyrinthe = self.labs[position[0]]
        labyrinthe.attaque(position,portee,propagation,direction,pos_obstacles)
        for i in range(len(labyrinthe.matrice_cases)):
            for j in range(len(labyrinthe.matrice_cases[0])):
                if labyrinthe.matrice_cases[i][j].clarte > 0:
                    poss.append((position[0],i,j))
        return poss

    def clear(self):
        for ID_entitee in self.entitees.keys():
            self.entitees[ID].clear()

class Labyrinthe:
    def __init__(self,ID,largeur,hauteur,depart,patterns=None,durete = 1,niveau = 1,element = TERRE,proba=0.1):
        #print("Initialisation du labyrinthe")
        self.id = ID #Correspond à la clé du labyrinthe. Créer un init différend pour chaque lab ?
        self.largeur = largeur
        self.hauteur = hauteur
        self.durete = durete
        self.niveau = niveau #Est-ce que la dureté des murs et le niveau des cases sont une seule et même chose ?
        self.element = element

        self.depart = depart

        self.matrice_cases = [[Case((self.id,j,i),niveau,element) for i in range(hauteur)]for j in range(largeur)]

        for i in range(self.largeur):
            self.matrice_cases[i][0].murs[HAUT].effets = [Mur_impassable()]
            self.matrice_cases[i][self.hauteur-1].murs[BAS].effets = [Mur_impassable()]

        for j in range(self.hauteur):
            self.matrice_cases[0][j].murs[GAUCHE].effets = [Mur_impassable()]
            self.matrice_cases[self.largeur-1][j].murs[DROITE].effets = [Mur_impassable()]

        self.patterns=patterns
        self.cases_visitees = None

        self.temps_restant = -1 #Devient positif quand le labyrinthe est actif sans entitée supérieure
        self.controleur = None #Tant qu'il n'est pas actif, il n'a pas de controleur à qui se référer

        self.generation(proba,None,None)
        print("Génération : check")

    def generation(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui génère la matrice du labyrinthe
            Entrées:
                -Les cases spéciales sous la forme suivante:[coord_case,objet]
                -L'éventuelle probabilité pour casser des murs
                -L'éventuel nombre de murs casser
                -L'éventuelle pourcentage de murs a casser
            Sorties:
                rien
        """
        #ini du tableau de case (4 murs pleins)
        for colone in self.matrice_cases:
            for case in colone:
                for mur in case.murs:
                    mur.effets.append(Mur_plein(self.durete))
        #génération en profondeur via l'objet generateur
        print("Génération du labyrinthe")
        gene=Generateur(self.matrice_cases,self.depart,self.largeur,self.hauteur,self.patterns)
        print("Générateur : check")
        self.matrice_cases=gene.generation(proba,nbMurs,pourcentage)

    def veut_passer(self,intrus,direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        self.matrice_cases[intrus.get_position()[1]][intrus.get_position()[2]].veut_passer(intrus,direction)

    def step(coord,entitee):
        self.matrice_cases[coord[0]][coord[1]].step(entitee)

    def get_vue(self,agissant):
        return self.resoud(agissant.get_position(),agissant.get_portee_vue())
            
    def getMatrice_cases(self):
        #on obtient une copie indépendante du labyrinthe
        new_mat = [[self.matrice_cases[j][i].get_copie() for i in range(self.hauteur)]for j in range(self.largeur)]
        return new_mat

    def get_case(self,position):
        return self.matrice_cases[position[1]][position[2]]

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].post_action((self.id,i,j))

    def fin_tour(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].fin_tour()
        if self.temps_restant >= 0:
            if self.temps_restant == 0:
                self.controleur.desactive_lab(self.id)
                self.controleur = None
                for i in range(self.largeur):
                    for j in range(self.hauteur):
                        self.matrice_cases[i][j].desactive()
            self.temps_restant -= 1
    #Et c'est la fin du tour !

    def quitte(self):
        self.temps_restant = 5

    def active(self,controleur):
        self.controleur = controleur
        self.temps_restant = -1 #Au cas où
        for i in range(self.largeur):
            for j in range(self.hauteur):
                self.matrice_cases[i][j].active(controleur)

    def attaque(self,position,portee,propagation,direction,obstacles):
        return self.resoud(position,portee,"attaque",propagation,direction,obstacles)

    def resoud(self,position,portee,action="vue",propagation="C__S_Pb",direction=None,dead_ends=[],reset=True):
        #Les possibilités de propagation sont :
        #                           Circulaire, le mode de propagation de la vision
        #                           Rectiligne, dans une unique direction
        #                           Semi-circulaire, dans trois directions fixées
        #                           Quarter-circulaire, dans deux directions fixées
        #                           Circulaire dégénéré, commence dans toutes les directions puis devient Semi-circulaire pour interdire les demi-tours
        #                           Semi-circulaire dégénéré, commence dans trois directions puis devient Quarter-circulaire pour interdire les demi-tours
        #                           Circulaire double dégénéré, devient Semi-circulaire dégénéré
        #                           Spatial, se déplace selon les coordonées comme la vue
        #                           Teleporte, se déplace par les téléporteurs comme les attaques magiques
        #                           Passe-porte, passe au travers des portes
        #                           Passe_barrières, passe au travers de certaines portes
        #                           Passe_mur, ignore les murs
        #Exemple de syntaxe du mode de propagation : "Sd_T_Pp", "CD_S_Pm" ou "R__T___"

        if reset:
            for i in range(len(self.matrice_cases)):
                for j in range(len(self.matrice_cases[0])):
                    self.matrice_cases[i][j].clarte = 0

        dirs = [HAUT,DROITE,BAS,GAUCHE]
        forme = propagation[0]
        if forme == "R":
            dirs = [direction]
        elif forme == "S":
            dirs.remove(dirs[direction-2])
        elif forme == "Q":
            dirs.remove(dirs[direction-2])
            dirs.remove(dirs[direction-3])

        queue=[(position,dirs,propagation)]

        self.matrice_cases[position[1]][position[2]].clarte = portee

        retrait = 1

        while len(queue)!=0 :

            data=queue[0]
            position = data[0]
            if action == "vue":
                retrait = self.matrice_cases[position[1]][position[2]].get_opacite()
            clarte = self.matrice_cases[position[1]][position[2]].clarte - retrait
            #enlever position dans queue
            queue.pop(0)

            if not position in dead_ends:
                #trouver les positions explorables
                positions_voisins=self.voisins_case(data)

                datas_explorables = self.positions_utilisables(positions_voisins,data)

                for data_explorable in datas_explorables:
                    pos = data_explorable[0]
                    clarte_cible = self.matrice_cases[pos[1]][pos[2]].clarte

                    if clarte <= 0 and clarte_cible <= 0:
                        self.matrice_cases[pos[1]][pos[2]].clarte = -1

                    elif clarte > clarte_cible :
                        #on marque la case comme visitée
                        self.matrice_cases[pos[1]][pos[2]].clarte = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(data_explorable)

        if action == "vue":
            matrice_cases = [[self.matrice_cases[i][j].get_infos((self.id,i,j)) for j in range(len(self.matrice_cases[0]))] for i in range(len(self.matrice_cases))]
        else :
            matrice_cases = self.matrice_cases

        return matrice_cases

    def voisins_case(self,data):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        ainsi que leurs coordonnées
        """
        position = data[0]
        propagation = data[2]
        deplacement = propagation[3]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        if deplacement == "S":
            if position[2]-1>=0:
                positions_voisins.append((position[0],position[1],position[2]-1))
            else:
                positions_voisins.append(None)
                
            if position[1]+1<self.largeur:
                positions_voisins.append((position[0],position[1]+1,position[2]))
            else:
                positions_voisins.append(None)
                
            if position[2]+1<self.hauteur:
                positions_voisins.append((position[0],position[1],position[2]+1))
            else:
                positions_voisins.append(None)
                
            if position[1]-1>=0:
                positions_voisins.append((position[0],position[1]-1,position[2]))
            else:
                positions_voisins.append(None)
        elif deplacement == "T":
            for i in range(4):
                cible = self.matrice_cases[position[1]][position[2]].murs[i].get_cible()
                if cible != None:
                    if cible[0] != position[0]:
                        cible = None
                positions_voisins.append(cible)
        else:
            print("Propagation inconnue")

        return positions_voisins

    def positions_utilisables(self,positions_voisins,data):
        """
        Fonction qui prend en entrées:
            les voisins de la case
            les positions des voisins
            la position de la case
            le chemin deja exploré
        et qui renvoie les directions ou l'on peut passer
        """
        position = data[0]
        directions = data[1]
        propagation = data[2]
        forme = propagation[0]
        degenerescence = propagation[1]
        deplacement = propagation[3]
        passage = propagation[6]
        datas_utilisables=[]
        cardinaux = [HAUT,DROITE,BAS,GAUCHE]

        for direction in directions:
            if positions_voisins[direction]!=None:
                voisin = positions_voisins[direction]

                #on vérifie si on peut passer
                blocage = self.matrice_cases[position[1]][position[2]].get_mur_dir(direction).get_blocage()
                if blocage != "Imp" and (passage=="m" or (blocage!="Ple" and ((passage=="p" and (blocage == "Por" or blocage == "P_b")) or (passage=="b" and (blocage == "Bar" or blocage == "P_b")) or (blocage == "Esc" and deplacement == "T") or blocage == None))):
                    #On détermine éventuellement la nouvelle forme de propagation
                    if degenerescence == "d":
                        if forme == "C":
                            nouv_prop = "S_"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Q_"+propagation[2:]
                        elif forme == "Q":
                            nouv_prop = "R_"+propagation[2:]
                    elif degenerescence == "D":
                        if forme == "C":
                            nouv_prop = "Sd"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Qd"+propagation[2:]
                    else:
                        nouv_prop = propagation

                    if forme=="R":
                        nouv_dir=[direction]
                    elif forme!="C":
                        #On détermine la direction d'où l'on vient
                        if deplacement=="S":
                            dir_back = cardinaux[direction-2]
                        elif deplacement=="T":
                            dir_back = 0
                            for i in cardinaux:
                                if self.matrice_cases[voisin[1]][voisin[2]].get_mur_dir(i).get_cible()==position:
                                    dir_back = i
                        #On n'y retournera pas !
                        nouv_dir=[]
                        for i in directions:
                            if i!=dir_back:
                                nouv_dir.append(i)
                    else:
                        nouv_dir=[HAUT,DROITE,BAS,GAUCHE]

                    nouv_data=(voisin,nouv_dir,nouv_prop)

                    datas_utilisables.append(nouv_data)
        return datas_utilisables

class Generateur:
    def __init__(self,matrice_cases,depart,largeur,hauteur,paterns,modeGeneration="Profondeur"):
        #print("Initialisation du générateur")
        self.depart = depart
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrice_cases = matrice_cases
        self.modeGeneration = modeGeneration
        self.paterns = paterns
        self.poids = [1,1,1,1]

    def generation(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui permet de générer une matrice conformément au paramètres
        et au paterns
        Entrées:
            -L'éventuelle probabilité pour casser des murs
            -L'éventuel nombre de murs casser
            -L'éventuelle pourcentage de murs a casser
        Sorties:une matrice de cases générée
        """
        #print("Génération")
        matrice=None
        
        self.pre_gene_paterns()
        if self.modeGeneration=="Profondeur":
            #print("Mode de génération : profondeur")
            matrice= self.generation_en_profondeur()
            #print("Génération en profondeur : check")
            #on casse les murs conformément aux paramètres
            self.casser_X_murs(proba,nbMurs,pourcentage)
        else:
            print("mode de génération choisi incompatible")

        self.post_gene_paterns()
        
        return matrice

    def pre_gene_paterns(self):
        """
        Fonction qui pregenere les paterns
        (on génère le squelette)
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.pre_generation(self.matrice_cases)

    def post_gene_paterns(self):
        """
        Fonction qui postgenere les paterns
        (on remplie les patterns)
        """
        if self.paterns != None:
            for patern in self.paterns :
                patern.post_generation(self.matrice_cases)

    def generation_en_profondeur(self):
        """
        Fonction qui génère la matrice avec la méthode du parcours en profondeur
        Entrées:Rien
        Sorties:une matrice de cases générée avec le parcours en profondeur
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre générateur
        #cela permet d'avoir le meme résultat
        #rdm=851353618387733257
        #print("seed ",rdm)
        random.seed(rdm)

        #print("Début de la génération")
        #position dans la matrice
        position = self.depart
        #le stack est une liste de positions
        stack=[position]
    

        while len(stack)!=0 :
            
            #on récupère les coords de là où l'on est cad la dernière case dans le stack
            position = stack[len(stack)-1]
            
            murs_generables = self.murs_utilisables(position)

            if len(murs_generables) > 0 : 
                
                #randrange est exclusif
                num_mur=self.randomPoids(murs_generables)
                
                #direction du mur à casser
                direction_mur=murs_generables[num_mur]

                mur = self.matrice_cases[position[1]][position[2]].murs[direction_mur]

                self.casser_mur(mur)

                new_pos = mur.get_cible()
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append(new_pos)
            else:
                #on revient encore en arrière
                stack.pop()

        #print("Fini")
        
        return self.matrice_cases

    def murs_utilisables(self,position,murs_requis = 4):
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables=[]

        for i in range(4):
            mur = self.matrice_cases[position[1]][position[2]].murs[i] #mur = self.matrice_cases[position[1][0]][position[1][1]].murs[i]
            cible = mur.get_cible()
            if cible != None and cible[0]==self.depart[0]:
                case_cible = self.matrice_cases[cible[1]][cible[2]]
                mur_oppose = self.get_mur_oppose(mur)
                if mur_oppose != None and case_cible.nb_murs_pleins()>=murs_requis and mur_oppose.is_touchable() and mur.is_touchable():
                    murs_utilisables.append(i)
        return murs_utilisables

    def randomPoids(self,murs_utilisables):
        """
        Fonction qui prend en entrée:
            les murs utilisables par la fonction
        et qui renvoie le numéro d'un mur générée avec un alétoire modifié
        """

        nbrandom=0
        res=-1
        
        poids_selectionnees=[]
        poids_total=0

        for i in range (0,len(murs_utilisables)):
            poids_selectionnees+=[poids_total+self.poids[murs_utilisables[i]]]
            poids_total+=self.poids[murs_utilisables[i]]

        nbrandom=random.randrange(0,poids_total)

        i=0

        while i<len(poids_selectionnees) and res==-1:
            if nbrandom < poids_selectionnees[i]:
                res=i
            i+=1
        return res

    def casser_X_murs(self,proba=None,nbMurs=None,pourcentage=None):
        """
        Fonction qui doit casser des murs sur la matrice
        on peut déterminer le nombre de murs avec un probabilité (proba*nb murs au total)
        ou selon un nombre défini en entrée
        ou un pourcentage
        """
        if proba!=None:
            self.casser_murs_selon_proba(proba)
        elif nbMurs!=None:
            self.casser_murs(nbMurs)
        elif pourcentage!=None:
            self.casser_murs(int(pourcentage/100*self.nb_murs_total()))
        else:
            print("mauvaise utilisation de la fonction, on ne sait que faire")

    def casser_murs(self,nb_murs_a_casser):
        """
        Fonction qui casse un certains nombre de murs aléatoirement
        Entrées:
            -le nombre de murs a casser
        """
        nb_murs_casser=0

        while nb_murs_casser<=nb_murs_a_casser:
            coord_case=[random.randrange(0,len(self.matrice_cases)),random.randrange(0,len(self.matrice_cases[0]))]

            if self.casser_mur_random_case(coord_case):
                nb_murs_casser+=1


    def restrictions_case(self,coord_case):
        """
        Fonction qui renvoie les murs intouchables
        Entrées:
            -les coordonnées de le case
        Sorties:
            -les directions ou les murs ne sont pas touchables
        """
        directions_interdites=[]

        murs=self.matrice_cases[coord_case[0]][coord_case[1]].get_murs()
        for i in range(0,4):
            if not(murs[i].is_touchable):
                directions_interdites.append(i)
            
        return directions_interdites

    def casser_mur_random_case(self,position_case):
        """
        Fonction qui prend en entrée la position de la case dont on veut casser un mur
        et qui renvoie un booléen indiquant si l'on as pu casser un mur
        """
        casser = False

        murs=self.murs_utilisables(self.voisins_case(position_case[0],position_case[1]))
        if len(murs)!=0:
            mur_a_casser=random.randrange(0,len(murs))
            self.casser_mur(self.matrice_cases[position_case[0]][position_case[1]].murs[murs[mur_a_casser]])
            casser = True
        return casser

    def casser_murs_selon_proba(self,proba):
        """
        Fonction qui casse des murs selon une probabilité donnée
        Entrée:
            -la probabilité de casser un mur
        """
        for x in range(1,self.largeur) :
            for y in range(1,self.hauteur) :
                case = self.matrice_cases[x][y]
                murs=self.murs_utilisables((self.depart[0],x,y),0)
                if HAUT in murs and random.random() <= proba :
                    self.casser_mur(case.murs[HAUT])
                if GAUCHE in murs and random.random() <= proba :
                    self.casser_mur(case.murs[GAUCHE])
                    
    def casser_mur(self,mur):
        """
        Fonction qui casse un mur spécifique
        Entrées:
            la direction du mur
            la position de la case
        Sorites:Rien
        """
        #on casse les murs de la case et de la case d'en face
        autre_mur = self.get_mur_oppose(mur)
        if autre_mur ==  None :
            print("On a un mur non réciproque !")
        else :
            mur.brise()
            autre_mur.brise()

    def nb_murs_total(self):
        """
        Fonction qui renvoie le nombres de murs pleins contenus dans le labyrinthe
        """
        murs_pleins=0
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                murs_pleins+=self.matrice_cases[x][y].nb_murs_pleins()
        
        return int((murs_pleins-self.hauteur*2-self.largeur*2)/2)

    def get_mur_oppose(self,mur):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None and cible[0] == self.depart[0]:
            for mur_potentiel in self.matrice_cases[cible[1]][cible[2]].murs :
                cible_potentielle = mur_potentiel.get_cible()
                if cible_potentielle != None and cible_potentielle[0] == self.depart[0]:
                    if mur in self.matrice_cases[cible_potentielle[1]][cible_potentielle[2]].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                        mur_oppose = mur_potentiel
        return mur_oppose

class Case:
    def __init__(self,position,niveau = 1,element = TERRE,effets = [],opacite = 1):
        # Par défaut, pas de murs.
        self.murs = [Mur([Teleport((position[0],position[1],position[2]-1))]),Mur([Teleport((position[0],position[1]+1,position[2]))]),Mur([Teleport((position[0],position[1],position[2]+1))]),Mur([Teleport((position[0],position[1]-1,position[2]))])]
        self.opacite = opacite
        self.opacite_bonus = 0
        self.niveau = niveau
        self.element = element
        self.clarte = 0
        self.code = 0
        self.effets = [] #Les cases ont aussi des effets ! Les auras, par exemple.
        self.effets += effets
        if self.element == TERRE:
            self.effets.append(Terre_permanente(self.niveau*2))
        elif self.element == FEU:
            self.effets.append(Feu_permanent(self.niveau,self.niveau*5))
        elif self.element == GLACE:
            self.effets.append(Glace_permanente(self.niveau,self.niveau/10))
        elif self.element == OMBRE:
            self.effets.append(Ombre_permanente(self.niveau,self.niveau/2))
        self.controleur = None

    #Découvrons le déroulé d'un tour, avec case-chan :

    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! On commence par activer les effets réguliers :
        self.code = 0
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()

    #Certains agissants particulièrement tapageurs font un concours de celui qui aura la plus grosse aura (comment ça, cette phrase particulièrement compliquée aura juste servi à faire un jeu de mot sur aura
    def ajoute_aura(self,aura):
        """Fonction qui ajoute un effet d'aura. On décidera de ceux qui s'exécutent plus tard."""
        self.effets.append(aura)
        if isinstance(aura,Aura_elementale): #On a besoin de savoir quelle aura prévaudra
            aura.priorite += self.clarte/2 #La clarté vient d'être utilisée pour déterminer la portée de l'aura, et n'est normalement pas encore réinitialisée
            if isinstance(aura,Feu):
                resp = aura.responsable
                for aura_bis in self.effets:
                    if isinstance(aura_bis,Feu) and aura_bis.responsable == resp :
                        aura_bis.phase = "terminé"

    #Les agissants prennent des décisions, agissent, se déplacent, les items se déplacent aussi.
    def veut_passer(self,intrus,direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère au mur compétent, qui gère tout."""
        self.murs[direction].veut_passer(intrus)

    def step_out(self,entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_out):
                effet.execute(entitee)

    def step_in(self,entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_in):
                effet.execute(entitee) #On agit sur les agissants qui arrivent (pièges, téléportation, etc.)

    #Tout le monde a fini de se déplacer.
    def post_action(self,position):
        self.opacite_bonus = 0 # On reset ça à chaque tour, sinon ça va devenir tout noir
        if len(self.effets) == 1: #On a un seul effet ! L'effet d'aura.
            if self.element != TERRE: #Les auras de terre sont juste là pour embêter les autres de toute façon
                self.effets[0].execute(self,position)
            else :
                self.code += 1
        else:
            on_attaques = []
            attaques = []
            priorite_max = 0
            IDmax = 0
            auras = {}

            for effet in self.effets:
                if isinstance(effet,Aura_elementale):
                    ID = effet.responsable
                    if ID in auras.keys() : # On a déjà une aura de ce type
                        auras[ID].append(effet)
                    else:
                        auras[ID]=[effet]
                    prio = effet.priorite
                    if prio > priorite_max : # On a un nouveau gagnant !
                        IDmax = ID
                        priorite_max = prio
                elif isinstance(effet,On_attack):
                    on_attaques.append(effet)
                elif isinstance(effet,Attaque_case):
                    attaques.append(effet)
                elif isinstance(effet,On_post_action): #Les auras non-élémentales sont aussi des On_post_action
                    effet.execute(self,position)

            for aura in auras[IDmax]:
                aura.execute(self,position)

            for attaque in attaques:
                for protection in on_attaques:
                    protection.execute(attaque)
                attaque.execute(self,position)

    def fin_tour(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if effet.phase == "terminé":
                self.effets.remove(effet)
                

    #Le tour se termine gentiment, et on recommence !

#Pour la génération, quand on a pas encore les barrières, portes et compagnie.
    def nb_murs_pleins(self):
        """
        Fonction qui renvoie le nombre de murs pleins dans la case
        """
        pleins=0

        for mur in self.murs :
            if mur.is_ferme() :
                pleins+=1
        
        return pleins
                
    def casser_mur(self,direction):
        """
        Fonction qui casse le mur dans la direction indiquée
        """
        self.murs[direction].brise()

    def construire_mur(self,direction,durete):
        """
        Fonction qui construit le mur dans la direction indiquée
        """
        self.murs[direction].construit(durete)

    def interdire_mur(self,direction):
        """
        Fonction qui construit le mur impassable dans la direction indiquée
        """
        self.murs[direction].interdit()

    def mur_plein(self,direction):
        """
        Fonction qui indique si le mur indiquée par la direction est plein ou non
        """
        return self.murs[direction].is_ferme()

    def acces(self,direction):
        return not(self.murs[direction].is_ferme()) and self.murs[direction].get_cible()

    def murs_pleins(self):
        directions = []
        for direction in [HAUT,DROITE,BAS,GAUCHE]:
            if self.mur_plein[direction]:
                directions.append(direction)
        return directions

    def get_mur_dir(self,direction):
        return self.murs[direction]

    def get_murs(self):
        return self.murs

    def get_mur_haut(self):
        return self.murs[0]

    def get_mur_droit(self):
        return self.murs[1]

    def get_mur_bas(self):
        return self.murs[2]

    def get_mur_gauche(self):
        return self.murs[3]

    def toString(self):
        return "haut "+str(self.murs[0].get_etat())+" droite "+str(self.murs[1].get_etat())+" bas "+str(self.murs[2].get_etat())+" gauche "+str(self.murs[3].get_etat())+"  "

    def get_opacite(self):
        return self.opacite + self.opacite_bonus

    def get_infos(self,position):
        return [position,self.clarte,0,0,0,0,self.calcule_code(),[self.acces(i) for i in range(4)],[]]

    def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
        return self.code

    def get_image(self): #À changer plus tard
        images_effets = []
        for effet in self.effets:
            images_effets.append(effet.get_image())
        images_murs = []
        if self.mur_plein(HAUT):
            images_murs.append(Mur_vue_haut())
        if self.mur_plein(BAS):
            images_murs.append(Mur_vue_bas())
        if self.mur_plein(DROITE):
            images_murs.append(Mur_vue_droite())
        if self.mur_plein(GAUCHE):
            images_murs.append(Mur_vue_gauche())
        return Case_vue(images_murs,images_effets,self.clarte)

    def get_copie(self):
        copie = Case((0,0,0),self.niveau,self.element,self.effets,self.opacite)
        copie.murs = self.murs
        return copie

    def active(self,controleur):
        self.controleur = controleur
        for mur in self.murs :
            mur.active(controleur)

    def desactive(self):
        self.controleur = None
        for mur in self.murs :
            mur.desactive()

class Mur:
    def __init__(self,effets):
        self.effets = effets
        self.peut_passer = False
        self.controleur = None

    def is_ferme(self):
        ferme = False
        for effet in self.effets :
            if isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and effet.ferme):
                ferme = True
        return ferme

    def get_blocage(self):
        blocage = None
        for effet in self.effets :
            if isinstance(effet,Mur_impassable):
                blocage = "Imp"
            elif blocage != "Imp" and (isinstance(effet,Mur_plein) and not(effet.casse)):
                blocage = "Ple"
            elif blocage != "Imp" and blocage != "Ple" and (isinstance(effet,Porte_barriere) and effet.ferme):
                blocage = "P_b"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and (isinstance(effet,Porte) and effet.ferme):
                blocage = "Por"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and isinstance(effet,Barriere):
                blocage = "Bar"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and blocage != "Por" and blocage != "Bar" and isinstance(effet,Escalier):
                blocage = "Esc"
        return blocage

    def is_touchable(self):
        touchable = True
        for effet in self.effets :
            if isinstance(effet,(Mur_impassable)):
                touchable = False
        return touchable

    def veut_passer(self,intrus):
        self.peut_passer = True
        for effet in self.effets :
            if isinstance(effet,On_try_through):
                effet.execute(self,intrus) #On vérifie que rien n'empêche le passage de l'intrus
        if self.peut_passer :
            for effet in self.effets :
                if isinstance(effet,On_through):
                    effet.execute(intrus) #Il est conseillé d'avoir un seul effet de déplacement, comme un seul effet d'autorisation de passage...
            if issubclass(intrus.get_classe(),Item):
                intrus.vole()
        elif issubclass(intrus.get_classe(),Item):
            intrus.heurte_mur()

    def interdit(self):
        self.effets.append(Mur_impassable())

    def construit(self,durete):
        self.effets.append(Mur_plein(durete))

    def detruit(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_try_through):
                self.effets.remove(effet)
                del(effet)

    def brise(self):
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_try_through) and not isinstance(effet,Mur_impassable) :
                self.effets.remove(effet)
                del(effet)

    def get_cible(self):
        cible = None
        en_cours = True
        i = 0
        while en_cours and i < len(self.effets) :
            effet = self.effets[i]
            if isinstance(effet,Teleport) :
                en_cours = False
                cible = effet.position
            i += 1
        return cible

    def set_cible(self,position,surnaturel = False):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        self.effets.append(Teleport(position,surnaturel))

    def set_escalier(self,position,sens):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        self.effets.append(Escalier(position,sens))

    def get_mur_oppose(self):
        mur_oppose = None
        cible = self.get_cible()
        if cible != None:
            case_cible = self.controleur.get_case(cible)
            for mur in case_cible.murs :
                cible_potentielle = mur.get_cible()
                if cible_potentielle != None:
                    case_cible_potentielle = self.controleur.get_case(cible_potentielle)
                    if self in case_cible_potentielle.murs:
                        mur_oppose = mur
        return mur_oppose
        

    def active(self,controleur):
        self.controleur = controleur

    def desactive(self):
        self.controleur = None

class Patern:
    def __init__(self,position,largeur,hauteur,entrees=[(0,1,0)],codes=[],vide = True,durete = 1,niveau = 1,element = TERRE):
        self.position = position
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrice_cases = [[Case((self.position[0],j+self.position[1],i+self.position[2]),niveau,element) for i in range(hauteur)]for j in range(largeur)]
        self.entrees = entrees
        self.codes = codes
        self.vide = vide
        self.durete = durete
        self.niveau = niveau
        self.element = element

    def post_gen_entrees(self,matrice_lab):
        """
        Fonction qui transforme les entrées en portes ou en murs vides
        """
        
        for nb in range(len(self.entrees)):
            x = self.entrees[nb][1]+self.position[1]
            y = self.entrees[nb][2]+self.position[2]
            print(x,y)
            case = matrice_lab[x][y]
            for bord in self.contraintes_cases(self.entrees[nb]):
                mur = case.murs[bord]
                if nb < len(self.codes) :
                    mur.brise()
                    mur.effets.append(Porte(self.durete,self.codes[nb]))
                    mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                    if mur_oppose != None :
                        mur_oppose.brise()
                        mur_oppose.effets.append(Porte(self.durete,self.codes[nb]))
                else :
                    mur.brise()
                    mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                    if mur_oppose != None :
                        mur_oppose.brise()

    def pre_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui pre génère les cases du patern
        """
        coordonnee_x = self.position[1]
        coordonnee_y = self.position[2]
        for i in range(coordonnee_x,coordonnee_x+self.largeur):
            for j in range(coordonnee_y,coordonnee_y+self.hauteur):
                x_pat=i-coordonnee_x
                y_pat=j-coordonnee_y
                #on ne doit générer que les cases au bords
                #plus précisement on doit empêcher le générateur d'y toucher
                if not self.case_est_une_entree((self.position[0],x_pat,y_pat)) and self.case_au_bord((self.position[0],x_pat,y_pat)):
                    dirs_intouchables=self.contraintes_cases((self.position[0],x_pat,y_pat))
                    for direction in dirs_intouchables:
                        mur = matrice_lab[i][j].murs[direction]
                        mur.interdit()
                        mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                        if mur_oppose != None :
                            mur_oppose.interdit()

    def post_generation(self,matrice_lab):
        """
        Fonction qui prend en entrée:
            la matrice de cases du labyrinthe
        et qui clear la salle
        """
        for i in range(self.position[1],self.position[1]+self.largeur):
            for j in range(self.position[2],self.position[2]+self.hauteur):
                pos_pat = (self.position[0],i-self.position[1],j-self.position[2])
                #on enlève les murs intouchables
                dirs_intouchables=[]
                if self.case_au_bord(pos_pat):
                    dirs_intouchables=self.contraintes_cases(pos_pat)
                for direction in [HAUT,DROITE,BAS,GAUCHE]:
                    mur = matrice_lab[i][j].murs[direction]
                    if direction in dirs_intouchables:
                        mur.detruit()
                        mur.construit(self.durete)
                        mur_oppose = self.get_mur_oppose(mur,matrice_lab)
                        if mur_oppose != None :
                            mur_oppose.detruit()
                            mur_oppose.construit(self.durete)
                    elif self.vide:
                        mur.detruit()
        self.post_gen_entrees(matrice_lab)
            
    def case_est_une_entree(self,position):
        """
        Fonction qui prend en entrées:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si elle est une entrée ou pas
        """
        est_entree=False
        for entree in self.entrees:
            if entree == position:
                est_entree=True

        return est_entree
    def case_au_bord(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie un booléen indiquant si la case est au bord ou non
        """
        return (position[1] == 0 or position[1] == self.largeur-1)or(position[2] == 0 or position[2] == self.hauteur-1)
        
    def clear_case(self,position):
        """
        Fonction qui clear la case selectionner
        """
        for i in range(0,4):
            self.matrice_cases[position[1]][position[2]].casser_mur(i)
    
    def incorporation_case(self,position):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            et génère les murs en fonction de sa position
        """
        #on casse les murs qui ne sont pas aux extrèmes
        if position[1]!=0:
            self.matrice_cases[position[1]][position[2]].casser_mur(GAUCHE)
            
        if position[1]!=(self.largeur-1):
            self.matrice_cases[position[1]][position[2]].casser_mur(DROITE)

        if position[2]!=0:
            self.matrice_cases[position[1]][position[2]].casser_mur(HAUT)
            
        if position[2]!=(self.hauteur-1):
            self.matrice_cases[position[1]][position[2]].casser_mur(BAS)

    
    
    def integration_case(self,position,matrice_lab):
        """
        Fonction qui prend en enetrées:
            les coordonnées de la case
            la matrice du labyrinthe

        et casse les murs qui empêches la navigation dans le labyrinthe
        """

        bords=self.case_bord(position,len(matrice_lab),len(matrice_lab[0]))

        for bord in bords:
            mur = matrice_lab[position[1]][position[2]].murs[bord]
            mur_oppose=self.get_mur_oppose(mur,matrice_lab)
            if mur_oppose!=None and not(mur.is_ferme()):
                mur.briser()

    def case_bord(self,position,largeur_mat,hauteur_mat):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
            la largeur et la hauteur de la matrice
            et qui renvoie la/les direction/s des bords
        """
        bords=[]
        
        #on ajoute les murs qui ne sont pas aux extrèmes
        if position[1]!=0:
            bords+=[GAUCHE]
            
        if position[1]!=(largeur_mat-1):
            bords+=[DROITE]

        if position[2]!=0:
            bords+=[HAUT]
            
        if position[2]!=(hauteur_mat-1):
            bords+=[BAS]

        return bords

    def contraintes_cases(self,position):
        """
        Fonction qui renvoie les murs qui sont soumis a des contraintes
        venant de la salle
        Entrées:
            -les coordonnées de la case
        Sorties:
            -les directions des murs a ne pas caser
        """
        #pour l'instant les contraintes se limites justes au bords de la matrice
        bords=[]
        
        if position[1]==0:
            bords+=[GAUCHE]
            
        if position[1]==(self.largeur-1):
            bords+=[DROITE]

        if position[2]==0:
            bords+=[HAUT]
            
        if position[2]==(self.hauteur-1):
            bords+=[BAS]

        return bords

    def copie(self,position,matrice_lab):
        """
        Fonction qui prend en entrée:
            les coordonnées de base du patern dans le labyrinthe
            la matrice de cases du labyrinthe
        et qui copie les cases du patern dans le labyrinthe
        """
        for i in range(position[1],position[1]+self.largeur):
            for j in range(position[2],position[2]+self.hauteur):
                matrice_lab[i][j]=self.matrice_cases[i-position[1]][j-position[2]]
                self.integration_case((self.position[0],i,j),matrice_lab)
        return matrice_lab

    def get_pos(self):
        return self.position

    def get_mur_oppose(self,mur,matrice_lab):
        cible = mur.get_cible()
        mur_oppose = None
        if cible != None:
            if cible[0] == self.position[0]:
                for mur_potentiel in matrice_lab[cible[1]][cible[2]].murs :
                    cible_potentielle = mur_potentiel.get_cible()
                    if cible_potentielle != None:
                        if cible_potentielle[0] == self.position[0]:
                            if mur in matrice_lab[cible_potentielle[1]][cible_potentielle[2]].murs : #Les murs sont réciproques (attention deux murs d'une même case ne peuvent pas mener à la même autre case !
                                mur_oppose = mur_potentiel
        return mur_oppose

class Entitee:
    """La classe des entitées physiques."""
    def __init__(self,position,ID=None):
        self.position = position
        self.latence = 0
        self.effets = []
        self.controleur = None
        if ID==None:
            self.ID = ID_MAX.incremente()
        else:
            self.ID = ID

    def set_position(self,position):
        self.position = position

    def ajoute_effet(self,effet):
        self.effets.append(effet)

    def get_position(self):
        return self.position

    def get_direction(self):
        return HAUT

    def get_description(self,observation):
        return ["Une entitee","N'aurait pas dû être instanciée.","Probablement une erreur..."]

    def get_skin(self):
        return SKIN_MYSTERE

    def add_latence(self,latence):
        self.latence += latence

    def set_latence(self,latence):
        self.latence = latence

    def active(self,controleur):
        self.controleur = controleur

    def desactive(self):
        self.controleur = None

class Entitee_superieure(Entitee):
    """La classe des entitées qui font bouger le labyrinthe autour d'eux."""
    pass

class Fantome(Entitee):
    """La classe des entitées qui traversent les murs."""
    pass

class Agissant(Entitee): #Tout agissant est un cadavre, tout cadavre n'agit pas.
    """La classe des entitées animées. Capable de décision, de différentes actions, etc. Les principales caractéristiques sont l'ID, les stats, et la classe principale."""
    def __init__(self,position,identite,niveau,ID=None):
        Entitee.__init__(self,position,ID)
        stats=CONSTANTES_STATS[identite]
        self.pv=stats['pv'][niveau]
        self.pv_max=self.pv
        self.regen_pv=stats['regen_pv'][niveau]
        self.taux_regen_pv = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la régénération des pv. Correspond aux effets passager sur la régénération des pv.
        self.pm=stats['pm'][niveau]
        self.pm_max=self.pm
        self.regen_pm=stats['regen_pm'][niveau]
        self.taux_regen_pm = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la régénération des pm. Correspond aux effets passager sur la régénération des pm.
        self.force=stats['force'][niveau]
        self.taux_force = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la force. Correspond aux effets passager sur la force.
        self.priorite=stats['priorite'][niveau]
        self.taux_priorite = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la priorité. Correspond aux effets passager sur la priorité.
        self.vitesse=stats['vitesse'][niveau]
        self.taux_vitesse = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.aff_o=stats['aff_o'][niveau]
        self.taux_aff_o = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à l'ombre. Correspond aux effets passager sur l'affinité à l'ombre.
        self.aff_f=stats['aff_f'][niveau]
        self.taux_aff_f = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité au feu. Correspond aux effets passager sur l'affinité au feu.
        self.aff_t=stats['aff_t'][niveau]
        self.taux_aff_t = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à la terre. Correspond aux effets passager sur l'affinité à la terre.
        self.aff_g=stats['aff_g'][niveau]
        self.taux_aff_g = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à la glace. Correspond aux effets passager sur l'affinité à la glace.
        self.taux_stats = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer aux statistiques. Correspond aux effets passager sur les statistiques. (Inclure les regen dans les stats ?)
        self.immunites = [] #La liste des éléments auxquels l'entitée est immunisé (très rare)
        self.especes=stats['especes']
        self.classe_principale = Classe_principale(identite,niveau)
        self.niveau = self.classe_principale.niveau
        self.etat = "vivant"

        #vue de l'agissant
        self.vue = None
        self.position_vue = None
        self.vue_nouvelle = False

        self.offenses=[]
        self.esprit=None

        #possessions de l'agissant
        self.inventaire = Inventaire(self.ID,stats['doigts'])

        #la direction du regard
        self.skill_courant = None
        self.dir_regard = 0
        self.talent = 1
        self.magie_courante = None
        self.cible_magie = None
        self.dir_magie = None
        self.cout_magie = 0
        self.multi = False
        self.latence = 0
        self.hauteur = 0 #Des fois qu'on devienne un item

        if stats['magies']:
            skill = trouve_skill(self.classe_principale,Skill_magie)
            if skill == None:
                print(self)
                print(self.classe_principale)
                for skil in self.classe_principale.skills:
                    print(skil.niveau)
                    print(skil)
            for magie in stats['magies']:
                skill.ajoute(eval(magie))
        if stats['special']:
            #Quelques entitées un peu particulières :
            #Comme celles qui commencent avec des magies
            pass

    def active(self,controleur):
        self.controleur = controleur
        self.inventaire.active(controleur)

    def desactive(self):
        self.inventaire.desactive()
        self.controleur = None

    def get_stats_attaque(self,element):
        force = self.force
        for taux in self.taux_force.values():
            force *= taux
        affinite = self.get_aff(element)
        for taux in self.taux_stats.values():
            force *= taux
            affinite *= taux
        return force,affinite,self.dir_regard,self.ID

    def attaque(self,direction):
        self.dir_regard = direction
        if self.get_arme() != None:
            self.skill_courant = Skill_attaque
        else:
            self.skill_courant = Skill_stomp

    def va(self,direction):
        self.dir_regard = direction
        self.skill_courant = Skill_deplacement #La plupart des monstres n'ont pas ce skill !

    def get_direction(self):
        if self.dir_regard != None:
            return self.dir_regard
        else:
            return HAUT

    def get_arme(self):
        return self.inventaire.get_arme()

    def get_bouclier(self):
        return self.inventaire.get_bouclier()

    def get_clees(self):
        return self.inventaire.get_clees()

    def get_item_lancer(self):
        if self.projectile_courant == None : #On lance l'item courant
            projectile = self.inventaire.get_item_courant()
        else : #On lance un item qu'on crée
            projectile = self.projectile_courant.cree_item(self) #Le 'self.projectile_courant' est un créateur de projectile
        return projectile

    def insurge(self,offenseur,gravite):
        if offenseur != 0:
            self.offenses.append([offenseur,gravite])

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        etat = "vivant" #Rajouter des précisions
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        return offenses, etat

    def get_aff(self,element):
        affinite = 1
        if element == OMBRE :
            affinite = self.aff_o
            for taux in self.taux_aff_o.values():
                affinite *= taux
        elif element == FEU :
            affinite = self.aff_f
            for taux in self.taux_aff_f.values():
                affinite *= taux
        elif element == TERRE :
            affinite = self.aff_t
            for taux in self.taux_aff_t.values():
                affinite *= taux
        elif element == GLACE :
            affinite = self.aff_g
            for taux in self.taux_aff_g.values():
                affinite *= taux
        else :
            print(element + "... quel est donc cet élément mystérieux ?")
        return affinite

    def peut_payer(self,cout):
        skill = trouve_skill(self.classe_principale,Skill_magie_infinie)
        res = True
        if skill == None:
            res = self.get_total_pm() >= cout
        return res

    def paye(self,cout):
        #On paye d'abord avec le mana directement accessible
        if self.pm >= cout:
            self.pm -= cout #Si on peut tout payer, tant mieux.
        else :
            cout_restant = cout
            if self.pm > 0:
                self.pm = 0
                cout_restant -= self.pm
            if cout_restant > 0: #Sinon, on fait appel aux éventuelles réserves de mana
                i = 0
                while cout_restant > 0 and i < len(self.effets):
                    if isinstance(self.effets[i],Reserve_mana):
                        reserve = self.effets[i]
                        if reserve.mana >= cout_restant:
                            reserve.execute(cout_restant)
                            cout_restant = 0
                        else :
                            cout_restant -= reserve.mana
                            reserve.execute(reserve.mana)
                    i += 1
            if cout_restant > 0: # Si ce n'est toujours pas assez, on utilise la magie infinie (on aurait pas pu payer plus sans ça, donc on l'a forcement !)
                self.pm -= cout_restant

    def get_total_pm(self):
        total = self.pm
        for effet in self.effets:
            if isinstance(effet,Reserve_mana):
                total += effet.mana
        return total

    def get_total_regen_pv(self):
        regen_pv = self.regen_pv
        for taux in self.taux_regen_pv.values() :
            regen_pv *= taux
        for taux in self.taux_stats.values() :
            regen_pv *= taux
        # /!\ Rajouter les effets négatifs du skill de magie infinie /!\
        items = []
        for equippement in self.inventaire.get_equippement():
            item = self.controleur.get_entitee(equippement)
            if isinstance(item,Regeneration_pv):
                regen_pv *= item.get_taux()
        return regen_pv

    def get_total_regen_pm(self):
        regen_pm = self.regen_pm
        for taux in self.taux_regen_pm.values() :
            regen_pm *= taux
        for taux in self.taux_stats.values() :
            regen_pm *= taux
        items = []
        for equippement in self.inventaire.get_equippement():
            item = self.controleur.get_entitee(equippement)
            if isinstance(item,Regeneration_pm):
                regen_pm *= item.get_taux()
        return regen_pm

    def get_vitesse(self):
        vitesse = self.vitesse
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        for taux in self.taux_stats.values() :
            vitesse *= taux
        return vitesse

    def get_priorite(self):
        priorite = self.priorite
        for taux in self.taux_priorite.values() :
            priorite *= taux
        for taux in self.taux_stats.values() :
            priorite *= taux
        return priorite

    def subit(self,degats,element=TERRE,ID=0): #L'ID 0 ne correspond à personne
        gravite = degats/self.pv_max
        if gravite > 1: #Si c'est de l'overkill, ce n'est pas la faute de l'attaquant non plus !
            gravite = 1
        if self.pv <= self.pv_max//3: #Frapper un blessé, ça ne se fait pas !
            gravite += 0.2
        if self.pv <= self.pv_max//9: #Et un mourrant, encore moins !!
            gravite += 0.3
        if element not in self.immunites :
            self.pv -= degats/self.get_aff(element)
        if self.pv <= 0: #Alors tuer les gens, je ne vous en parle pas !!!
            gravite += 0.5
        self.insurge(ID,gravite)

    def instakill(self,ID=0):
        immortel = self.controleur.trouve_skill(self.classe_principale,Skill_immortel)
        if immortel != None:
            if self.pv > 0:
                self.pv = 0 #Et ça s'arrète là
        else:
            self.meurt()

    def echape_instakill(self,ID):
        self.insurge(ID,1)

    def soigne(self,soin):
        self.pv += soin

    def rejoint(self,nom_esprit):
        self.esprit = nom_esprit

    def meurt(self):
        self.pv = self.pm = 0
        self.etat = "mort"
        self.dir_regard = HAUT
        self.taux_regen_pv = self.taux_regen_pm = self.taux_force = self.taux_priorite = self.taux_vitesse = self.taux_aff_o = self.taux_aff_f = self.taux_aff_t = self.taux_aff_g = self.taux_stats = {}
        self.effets = []
        self.inventaire.drop_all(self.position)

    def get_esprit(self):
        return self.esprit

    def get_classe(self):
        if self.etat == "vivant":
            return Agissant
        if self.etat == "mort":
            return Cadavre
        if self.etat == "oeuf":
            return Oeuf

    def get_especes(self):
        return self.especes

    def get_description(self,observation):
        if self.etat == "vivant":
            return ["Un agissant","Qu'est-ce qu'il fait dans mon inventaire ?"]
        if self.etat == "mort":
            return ["Un cadavre","Où as-tu trouvé ça ?"]
        if self.etat == "oeuf":
            return ["Un oeuf","Je n'ai rien pour le cuire..."]

    def get_portee_vue(self):
        skill = trouve_skill(self.classe_principale,Skill_vision)
        if skill == None:
            print("Oups, je n'ai pas de skill vision ! Pourquoi ?")
            print(self.ID)
            portee = 0
        else :
            portee = skill.utilise()
            portee *= self.get_aff(OMBRE) #Puisque c'est le manque de lumière qui réduit le champ de vision !
        return portee

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

    # Découvrons le déroulé d'un tour, avec agissant-san :
    def debut_tour(self):
        if self.etat == "vivant":
            #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
            #La régénération ! Plein de nouveaux pm et pv à gaspiller ! C'est pas beau la vie ?
            self.pv += self.get_total_regen_pv()
            self.pm += self.get_total_regen_pm() #Et oui, les pm après, désolé...
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            if self.pm > self.pm_max:
                self.pm = self.pm_max
            self.inventaire.debut_tour()
            if self.latence >= 0:
                self.latence -= self.get_vitesse()
            # Partie auras à retravailler
            skills = self.classe_principale.debut_tour()
            for skill in skills :
                if isinstance(skill,Skill_aura):
                    effet = skill.utilise()
                    self.effets.append(effet)
                # Quels autres skills peuvent tomber dans cette catégorie ?
            #Et les effets. Vous les voyez tous les beaux enchantements qui nous renforcent ?
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets (dont les auras qu'on vient de rajouter au dessus)
            if isinstance(effet,Time_limited):
                effet.wait()

    # Les esprits gambergent, tergiversent et hésitent.

    def post_decision(self):
        #On a pris de bonnes décisions pour ce nouveau tour ! On va bientôt pouvoir agir, mais avant ça, peut-être quelques effets à activer ?
        for effet in self.effets:
            if isinstance(effet,On_post_decision):
                effet.execute(self) #On exécute divers effets

    # Les agissants agissent, les items projetés se déplacent, éventuellement explosent.
    def on_action(self):
        self.skill_courant = None #Si on a de la chance, on pourra jouer plusieurs fois dans le tour ! (Bientôt...)
        for effet in self.effets:
            if isinstance(effet,On_action):
                effet.execute(self) #Principalement les lancements de magies

    def post_action(self):
        #Le controleur nous a encore forcé à agir ! Quel rabat-joie, avec ses cout de mana, ses latences, ses "Vous ne pouvez pas utiliser un skill que vous n'avez pas." !
        attaques = []
        dopages = []
        for effet in self.effets:
            if isinstance(effet,On_post_action): #Les protections (générales) par exemple
                effet.execute(self)
            elif isinstance(effet,On_attack):
                dopages.append(effet)
            elif isinstance(effet,Attaque):
                attaques.append(effet)
        for attaque in attaques :
            for dopage in dopages:
                dopage.execute(attaque)
            attaque.execute(self.controleur) #C'est à dire qu'on attaque autour de nous. On n'en est pas encore à subir.

    # Tout le monde s'est préparé, a placé ses attaques sur les autres, etc. Les cases ont protégé leurs occupants.

    def pre_attack(self):
        #On est visé par plein d'attaques ! Espérons qu'on puisse se protéger.
        attaques = []
        on_attaques = []
        for effet in self.effets:
            if isinstance(effet,On_attack): #Principalement les effets qui agissent sur les attaques
                on_attaques.append(effet)
            elif isinstance(effet,Attaque_particulier):
                attaques.append(effet)
        skill = trouve_skill(self.classe_principale,Skill_defense)
        taux = 1
        if skill != None :
            taux *= skill.utilise()
        items = []
        for equippement in self.inventaire.get_equippement():
            item = self.controleur.get_entitee(equippement)
            if isinstance(item,Defensif):
                items.append(item)
        for attaque in attaques :
            attaque.degats *= taux
            for on_attaque in on_attaques:
                on_attaque.execute(attaque)
            for item in items:
                item.intercepte(attaque)
            attaque.execute(self)

    # Les autres subissent aussi des attaques.

    def fin_tour(self):
        #Quelques effets avant la fin du tour (maladie, soin, tout ça tout ça...)
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_fin_tour):
                effet.execute(self)
            elif isinstance(effet,Maladie):
                effet.contagion(self)
            if effet.phase == "terminé":
                self.effets.remove(effet)
        #Il est temps de voir si on peut encore recoller les morceaux.
        if self.pv <= 0:
            immortel = trouve_skill(self.classe_principale,Skill_immortel)
            if immortel != None :
                self.taux_stats["immortalité"] = immortel.utilise()
            else :
                essence = trouve_skill(self.classe_principale,Skill_essence_magique)
                if essence != None :
                    cout = essence.utilise(self.pv)
                    if peut_payer(cout):
                        paye(cout)
                        self.pv = 0
                    else :
                        self.meurt()
                else :
                    self.meurt()
        else :
            immortel = trouve_skill(self.classe_principale,Skill_immortel)
            if immortel != None :
                if "immortalité" in self.taux_stats.keys():
                    self.taux_stats.pop("immortalité")
        self.inventaire.fin_tour()
        self.classe_principale.gagne_xp()
        if self.niveau != self.classe_principale.niveau : #On a gagné un niveau
            if isinstance(self,Humain):
                self.level_up()
            else:
                print("Quelqu'un d'autre que le joueur a une incohérence entre son niveau et le niveau de sa classe principale !")
                print(self)
                print(self.niveau)
                print(self.classe_principale.niveau)

class Tank(Agissant):
    """La classe des agissants forts en défense."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"tank",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//9:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Dps(Agissant):
    """La classe des agissants forts en attaque."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"dps",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Soigneur(Agissant):
    """La classe des agissants qui soignent les autres."""
    def __init__(self,position,niveau):
        Agissant.__nit__(self,position,'soigneur',niveau)
        magie = trouve_skill(self.classe_principale,Skill_magie)
        magie.ajoute(Magie_soin)
        magie.ajoute(Magie_auto_soin)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= 3*self.pv_max//4 or self.pm < 50:
            etat = "fuite"
        else:
            etat = "soin"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Renforceur(Agissant):
    """La classe des agissants qui renforcent les autres."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"soutien",niveau)
        magie = trouve_skill(self.classe_principale,Skill_magie)
        magie.ajoute(Magie_enchantement_force())


    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= 3*self.pv_max//4 or self.pm < 50:
            etat = "fuite"
        else:
            etat = "soutien"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            if self.esprit == "1":
                return SKIN_VERT
            elif self.esprit == "2":
                return SKIN_ROUGE
            else:
                return SKIN_AGISSANT
        else:
            return SKIN_CADAVRE

class Sentinelle(Agissant):
    """Une classe factice. Pour les agissants qui ne se déplace qu'en présence d'ennemis. Ne fonctionne pas lorsqu'un humain est aux commandes."""
    pass

class Gobelin(Agissant):
    """Le monstre de base. Faible, souvent en groupe."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_GOBELIN
        else:
            return SKIN_CADAVRE

    #Est-ce qu'il a besoin d'une méthode spécifique ? Pour les offenses peut-être ?

class Sentinelle_gobelin(Gobelin,Sentinelle):
    """Un gobelin qui reste sur place tant qu'il ne voit pas d'ennemi. Créé spécifiquement pour les premiers étages et le tutoriel.
       Il a une meilleure défense que les gobelins de base."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"sentinelle_gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//9:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

class Guerrier_gobelin(Gobelin):
    """Un gobelin agressif est avide de sang.
       Il a une meilleure attaque que les gobelins de base."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"guerrier_gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

class Explorateur_gobelin(Gobelin):
    """Un gobelin rapide et trop curieux.
       Il a une bonne vitesse que les gobelins de base, qui l'avantage aussi en combat."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"explorateur_gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

class Mage_gobelin(Gobelin):
    """Un gobelin avec un potentiel magique.
       Il peut utiliser une attaque magique."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"mage_gobelin",niveau)

    def attaque(self,direction):
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        if self.peut_payer(cout_pm_poing_magique[skill.niveau-1]): #Quelle est l'attaque magique des gobelins ?
            self.skill_courant = Skill_magie
            self.magie_courante = "magie poing magique"
        else:
            self.skill_courant = Skill_stomp

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

class Shaman_gobelin(Gobelin):
    """Un gobelin avec un potentiel magique.
       Il peut utiliser un sort de boost."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"shaman_gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= 3*self.pv_max//4 or self.pm < 50:
            etat = "fuite"
        else:
            etat = "soutien"
        return offenses, etat

class Chef_gobelin(Gobelin):
    """Un gobelin qui dirige un groupe.
       Bonnes stats, augmente l'efficacité de l'esprit."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"chef_gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

class Slime(Agissant):
    """Un tas de gelée. Faible, tant qu'il est tout seul et de bas niveau..."""
    def __init__(self,position,niveau):
        Agissant.__init__(self,position,"slime",niveau)

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_SLIME
        else:
            return SKIN_CADAVRE

class Humain(Agissant,Entitee_superieure):
    """La classe des pnjs et du joueur. A un comportement un peu plus complexe, et une personnalité."""
    def __init__(self,position,identite,niveau,ID):
        Agissant.__init__(self,position,identite,niveau,ID)
        self.dialogue = -1 #Le dialogue par défaut, celui des ordres
        self.replique = None #La réplique en cours de l'agissant vaut None lorsqu'il n'y a pas de dialogue en cours
        self.repliques = [] #Les réponses possibles de l'interlocuteur
        self.replique_courante = 0 #La réponse sélectionnée

        self.mouvement = 0 #0 pour un déplacement ciblé, 1 pour chercher
        self.cible_deplacement = self.ID #Une ID pour suivre quelqu'un, ou une position pour s'y diriger
        self.comportement_ennemis = 0 #0 pour combattre, 1 pour ignorer, 2 pour fuir, 3 pour tuer une cible
        self.comportement_neutres = 1 #0 pour combattre, 1 pour ignorer, 2 pour fuir
        self.cible_attaque = None #La cible à tuer

        self.attente = True #Les humains attendent le joueur au début du jeu

    def parle(self,touche):
        if touche == pygame.K_UP:
            if self.replique_courante == 0:
                self.replique_courante = len(self.repliques)
            self.replique_courante -= 1
        elif touche == pygame.K_DOWN:
            self.replique_courante += 1
            if self.replique_courante == len(self.repliques):
                self.replique_courante = 0
        elif touche == pygame.K_SPACE:
            self.interprete(self.replique_courante)

    def end_dialogue(self,dialogue=-1):
        self.controleur.get_entitee(2).interlocuteur = None
        self.controleur.get_entitee(2).event = None
        self.controleur.unset_phase(EVENEMENT)
        self.dialogue = dialogue

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.attente:
            etat = "attente"
        elif self.fuite():
            etat = "fuite"
        else:
            etat = "humain" #Les humains ont des comportements inutilement alambiqués...
        return offenses, etat

    def level_up(self):
        niveau = self.classe_principale.niveau # /!\ Peut donner des résultats non-voulus si la montée de niveau a lieu pendant qu'on est sous le coup d'un enchantement
        stats=CONSTANTES_STATS[self.identite]
        self.pv_max=stats['pv'][niveau]
        self.regen_pv=stats['regen_pv'][niveau]
        self.pm_max=stats['pm'][niveau]
        self.regen_pm=stats['regen_pm'][niveau]
        self.force=stats['force'][niveau]
        self.priorite=stats['priorite'][niveau]
        self.vitesse=stats['vitesse'][niveau]
        self.aff_o=stats['aff_o'][niveau]
        self.aff_f=stats['aff_f'][niveau]
        self.aff_t=stats['aff_t'][niveau]
        self.aff_g=stats['aff_g'][niveau]
        self.niveau = self.classe_principale.niveau

class Joueur(Humain): #Le premier humain du jeu, avant l'étage 1 (évidemment, c'est le personnage principal !)
    """La classe du joueur."""
    def __init__(self,position,screen):

        self.identite = 'joueur'
        self.place = 0

        Humain.__init__(self,position,self.identite,1,2)

        self.apreciations = [0,0,0,0,0,0,0,0,0,0]
        self.role = "independant"

        #Il doit afficher tout ce qu'il voit...
        print("Initialisation du joueur")
        self.affichage = Affichage(screen)
        self.event = None
        self.etage = 0
        self.arbre = True
        self.courant = 0
        self.choix_elems = []
        print("Affichage : check")
        self.curseur = "carré" #... et sélectionner un certain nombre de trucs
        self.highest = 0 #Le plus haut où l'on soit allé.

        #Il peut aussi monter de niveau, et a plusieurs choix lorsqu'il le fait :
        self.choix_niveaux = {CLASSIQUE:{1:None, #Le niveau 1 prendra la valeur physique ou magique
                                         2:None, #Le niveau 2 prendra la valeur corps à corps, distance, magie_infinie ou essence magique
                                         3:None, #Les propositions pour les niveaux suivants dépendent grandement du choix aus niveaux 1 et 2
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

        #Il utilise le clavier pour tout controler. Les touches sont liées à des actions, on peut aussi modifier les touches.
        self.cat_touches = {pygame.K_UP:"directionelle", #Les touches directionnelles tournent le joueur
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
                            pygame.K_SPACE:"courant", #La barre espace sélectionne, valide, etc. l'objet courant. Elle ne peut pas être modifiée
                            pygame.K_RETURN:"touches"} #La touche Entrée confirme certains choix, ou peut modifier les touches. Elle ne peut pas être modifiée

        self.dir_touches = {pygame.K_UP:HAUT, #Les touches associées à une direction
                            pygame.K_DOWN:BAS,
                            pygame.K_LEFT:GAUCHE,
                            pygame.K_RIGHT:DROITE,
                            pygame.K_q:GAUCHE,
                            pygame.K_z:HAUT,
                            pygame.K_d:DROITE,
                            pygame.K_s:BAS,
                            pygame.K_a:IN,
                            pygame.K_e:OUT}

        self.skill_touches = {pygame.K_p:Skill_stomp, #Les touches associées à un skill.
                              pygame.K_m:Skill_ramasse,
                              pygame.K_w:Skill_deplacement,
                              pygame.K_x:Skill_attaque}

        self.magies = {} #Le skill magie contient beaucoup de magie. La touche est associée à la fois au skill magie et à la magie correspondante.
        self.methode_courante = None
        magie = Magie_explosion_de_mana
        skill = trouve_skill(self.classe_principale,Skill_magie)
        skill.ajoute(magie)

        self.projectiles = {} #Le skill lancer peut s'utiliser de plusieurs façon : en le combinant à un skill de création de projectile, les touches sont associées comme pour les magies# sur l'item courant de l'inventaire, par le biais d'une touche du skill lancer ou, si l'item est un projectile, directement depuis l'inventaire

    def get_skin(self):
        return SKIN_JOUEUR

    def fuite(self):
        return False #À modifier pour quand on prend le controle de Dev

    def debut_tour(self):
        self.affichage.dessine(self)
        Agissant.debut_tour(self)
        if self.get_etage_courant() > self.highest:
            self.highest = self.get_etage_courant()
            if self.highest == 1:
                self.interpele()
            elif self.highest == 2:
                self.interpele()
            elif self.highest == 4:
                #La peureuse passe à l'explication des différents monstres
                pass
            elif self.highest == 5:
                peureuse = self.controleur.entitess[5]
                if peureuse.dialogue == -1:
                    peureuse.dialogue = 3

    def get_etage_courant(self):
        return int(self.position[0].split()[1])

    def recontrole(self):
        """La fonction qui réagit aux touches du clavier."""
        # On commence par trouver à quelle catégorie appartient la touche :
        touches = pygame.key.get_pressed()
        for touche in self.skill_touches.keys():
            if touches[touche]:
                self.skill_courant = self.skill_touches[touche]
                if self.skill_courant == Skill_magie : # Le skill magie contient beaucoup de magies différentes !
                    self.magie_courante = self.magies[touche]
                if self.skill_courant == Skill_lancer : # Le skill lancer contient beaucoup d'objets différends
                    self.projectile_courant = self.projectiles[touche]

    def utilise_courant(self):
        if self.curseur == "in_inventaire":
            self.inventaire.utilise_courant(self)
        elif self.curseur == "in_classe":
            self.skill_courant = self.classe_principale.utilise_courant()
        else: #On vaut parler à quelqu'un
            self.interpele() #On interpele les agissants à proximité

    def interpele(self):
        #On cherche la personne :
        if self.dir_regard == HAUT:
            positions = [(self.position[0],self.position[1]-1,self.position[2]),(self.position[0],self.position[1],self.position[2]-1),(self.position[0],self.position[1],self.position[2]+1),(self.position[0],self.position[1]+1,self.position[2])]
            directions = [GAUCHE,HAUT,BAS,DROITE]
        elif self.dir_regard == BAS:
            positions = [(self.position[0],self.position[1]+1,self.position[2]),(self.position[0],self.position[1],self.position[2]-1),(self.position[0],self.position[1],self.position[2]+1),(self.position[0],self.position[1]-1,self.position[2])]
            directions = [DROITE,HAUT,BAS,GAUCHE]
        elif self.dir_regard == GAUCHE:
            positions = [(self.position[0],self.position[1],self.position[2]-1),(self.position[0],self.position[1]-1,self.position[2]),(self.position[0],self.position[1]+1,self.position[2]),(self.position[0],self.position[1],self.position[2]+1)]
            directions = [HAUT,GAUCHE,DROITE,BAS]
        elif self.dir_regard == DROITE:
            positions = [(self.position[0],self.position[1],self.position[2]+1),(self.position[0],self.position[1]-1,self.position[2]),(self.position[0],self.position[1]+1,self.position[2]),(self.position[0],self.position[1],self.position[2]-1)]
            directions = [BAS,GAUCHE,DROITE,HAUT]
        self.interlocuteur = None #Normalement c'est déjà le cas
        for i in range(4):
            pos = positions[i]
            agissants = self.controleur.trouve_agissants(pos)
            for ID in agissants:
                agissant = self.controleur.get_entitee(ID)
                if isinstance(agissant,Humain) and self.interlocuteur == None and not self.controleur.est_item(ID):
                    self.interlocuteur = agissant
                    self.controleur.set_phase(EVENEMENT)
                    self.event = DIALOGUE
                    self.interlocuteur.start_dialogue()
                    self.interlocuteur.dialogue = -1
                    self.dir_regard = directions[i]
                    self.interlocuteur.dir_regard = range(4)[directions[i]-2]

    def controle(self,touche):
        if self.controleur.phase == TOUR:
            if touche in self.cat_touches.keys():
                if self.cat_touches[touche] == "zone":
                    direction = self.dir_touches[touche]
                    self.change_zone(direction)
                elif self.cat_touches[touche] == "courant" : # On a affaire à la touche qui utilise le skill ou l'objet courant
                    self.utilise_courant()
                elif self.cat_touches[touche] == "touches" : # On veut changer les touches
                    self.start_change_touches()
                elif self.cat_touches[touche] == "directionelle" : # On a affaire à une touche directionnelle
                    self.dir_regard = self.dir_touches[touche]
                elif self.cat_touches[touche] == "skill" : # On a affaire à l'une des touches qui ont été choisies comme raccourci d'un skill
                    self.skill_courant = self.skill_touches[touche]
                    if self.skill_courant == Skill_lancer : # Le skill lancer contient beaucoup d'objets différends
                        self.projectile_courant = self.projectiles[touche]
                    elif self.skill_courant == Skill_magie : # Le skill magie contient beaucoup de magies différentes !
                        self.magie_courante = self.magies[touche] #self.magie_courante n'est que le nom de la magie
                        skill = trouve_skill(self.classe_principale,Skill_magie)
                        self.magie = skill.magies[self.magie_courante](skill.niveau) #Ici on a une magie similaire (juste pour l'initialisation du choix, oubliée après parce que le skill fournira la vrai magie avec utilise())
                        if isinstance(self.magie,Magie_cible):
                            self.controleur.set_phase(COMPLEMENT_CIBLE)
                        if isinstance(self.magie,Magie_cout):
                            self.controleur.set_phase(COMPLEMENT_COUT)
                        if isinstance(self.magie,Magie_dirigee):
                            self.controleur.set_phase(COMPLEMENT_DIR)
                        #Vérifier si on a besoin de complémenter la magie
        elif self.controleur.phase in [COMPLEMENT_CIBLE,COMPLEMENT_COUT,COMPLEMENT_DIR]:
            #Les touches servent alors à choisir le complément
            self.methode_courante(touche)
        elif self.controleur.phase == TOUCHE:
            #On veut modifier les touches
            self.continue_change_touche(touche)
        elif self.controleur.phase == EVENEMENT:
            #Il se passe quelque chose !
            #Option 1 : une cinématique. On ignore tous les inputs SAUF celui pour passer la cinématique
            #Option 2 : un dialogue. Les inputs servent à choisir les réponses et déclenche la réplique suivante/la fin du dialogue
            #Option 3 : un choix d'évolution (montée de niveau de la classe principale ou autre avec cadeaux à la clé)
            #Option 4 : un choix d'évolution (possibilité de réorganisation des skills/classes)
            #Option 5 : une information d'évolution/accomplissement/etc. (est-ce vraiment un évènement ? est-ce une cinématique ?)
            #Pour l'instant, on se contente d'implémenter le choix d'évolution :
            if self.event == LEVELUP:
                self.choisi_cadeau(touche)
            elif self.event == DIALOGUE:
                self.discute(touche)

    def complement(self):
        """Appelée une fois par tour pendant le choix des complements
           Gère le temps et l'affichage"""
        if self.methode_courante == None :
            if self.controleur.phase == COMPLEMENT_DIR:
                self.start_select_direction(self.magie)
            elif self.controleur.phase == COMPLEMENT_COUT:
                self.start_select_cout(self.magie)
            elif self.controleur.phase == COMPLEMENT_CIBLE:
                self.start_select_cible(self.magie)
        current_time = pygame.time.get_ticks()
        if current_time > self.too_late :
            #Le temps est écoulé !
            self.methode_courante = None
            self.start_time = 0
            self.too_late = 0
            self.precision_cout_magie = 0
            self.choix_cout_magie = 0
            self.element_courant = 0
            #Etc.
            self.controleur.unset_phase(self.controleur.phase)
        else :
            proportion_ecoulee = (current_time - self.start_time)/self.temps
            if self.methode_courante == self.continue_select_direction:
                self.affichage.redraw_magie_dir(self,proportion_ecoulee)
            elif self.methode_courante == self.continue_select_cout:
                self.affichage.redraw_magie_cout(self,proportion_ecoulee)
            elif self.methode_courante == self.continue_select_cible:
                self.affichage.redraw_magie_cible(self,proportion_ecoulee)
            elif self.methode_courante == self.continue_select_case:
                self.affichage.redraw_magie_case(self,proportion_ecoulee)

    def start_select_direction(self,magie):
        self.methode_courante = self.continue_select_direction #Est-ce que ça fonctionnera avec le self comme ça ? Hum...
        self.affichage.draw_magie_dir(self)
        self.temps = magie.temps
        self.start_time = pygame.time.get_ticks()
        self.too_late = self.start_time + self.temps

    def continue_select_direction(self,touche):
        if touche == pygame.K_UP :
            self.dir_regard = HAUT
        elif touche == pygame.K_DOWN :
            self.dir_regard = BAS
        elif touche == pygame.K_LEFT :
            self.dir_regard = GAUCHE
        elif touche == pygame.K_RIGHT :
            self.dir_regard = DROITE
        elif touche == pygame.K_RETURN :
            self.dir_magie = self.dir_regard
            self.controleur.unset_phase(COMPLEMENT_DIR)
            self.methode_courante = None

    def start_select_cout(self,magie):
        self.methode_courante = self.continue_select_cout #Est-ce que ça fonctionnera avec le self comme ça ? Hum...
        self.precision_cout_magie = 10
        self.choix_cout_magie = 0
        self.affichage.draw_magie_cout(self)
        self.temps = magie.temps
        self.start_time = pygame.time.get_ticks()
        self.too_late = self.start_time + self.temps

    def continue_select_cout(self,touche):
        if touche == pygame.K_UP and self.choix_cout_magie + self.precision_cout_magie <= self.get_total_pm() :
            self.choix_cout_magie += self.precision_cout_magie
        elif touche == pygame.K_DOWN and self.choix_cout_magie - self.precision_cout_magie >= 0:
            self.choix_cout_magie -= self.precision_cout_magie
        elif touche == pygame.K_LEFT and precision_cout_magie > 0:
            self.precision_cout_magie -= 1
        elif touche == pygame.K_RIGHT :
            self.precision_cout_magie += 1
        elif touche == pygame.K_RETURN :
            self.cout_magie = self.choix_cout_magie
            self.controleur.unset_phase(COMPLEMENT_COUT)
            self.methode_courante = None

    def start_select_cible(self,magie):
        if isinstance(magie,Multi_cible):
            self.multi = True
        else:
            self.multi = False
        if isinstance(magie,Cible_agissant):
            self.methode_courante = self.continue_select_cible
            self.cibles = self.controleur.get_cibles_potentielles_agissants(magie,self)
            self.element_courant = 0 #Je recycle
            self.cible = []
            self.affichage.draw_magie_cible(self)
            self.temps = magie.temps
            self.start_time = pygame.time.get_ticks()
            self.too_late = self.start_time + self.temps
        elif isinstance(magie,Cible_item):
            self.methode_courante = self.continue_select_cible
            self.cibles = self.controleur.get_cibles_potentielles_items(magie,self)
            self.element_courant = 0 #Je recycle
            self.cible = []
            self.affichage.draw_magie_cible(self)
            self.temps = magie.temps
            self.start_time = pygame.time.get_ticks()
            self.too_late = self.start_time + self.temps
        elif isinstance(magie,Cible_case):
            self.start_select_cible_case(magie)

    def continue_select_cible(self,touche):
        if touche == pygame.K_UP :
            if self.element_courant == 0:
                self.element_courant = len(self.cibles)
            self.element_courant -= 1
        elif touche == pygame.K_DOWN :
            self.element_courant += 1
            if self.element_courant == len(self.cibles):
                self.element_courant = 0
        elif touche == pygame.K_SPACE :
            new_cible = self.cibles[self.element_courant]
            if self.multi : #Si jamais une magie peut cibler plusieurs cibles.
                if new_cible in self.cible :
                    self.cible.remove(new_cible)
                else :
                    self.cible.append(new_cible)
            else:
                self.cible = [new_cible]
        elif touche == pygame.K_RETURN and self.cible != [] :
            if self.multi :
                self.cible_magie = self.cible
            elif self.cible != []:
                self.cible_magie = self.cible[0]
            self.controleur.unset_phase(COMPLEMENT_CIBLE)
            self.methode_courante = None

    def start_select_cible_case(self,magie):
        self.methode_courante = self.continue_select_case
        self.cibles = self.controleur.get_cibles_potentielles_cases(magie,self)
        self.element_courant = (self.position[0],self.position[1],self.position[2]) #Je recycle
        self.cible = []
        self.affichage.draw_magie_case(self)
        self.temps = magie.temps
        self.start_time = pygame.time.get_ticks()
        self.too_late = self.start_time + self.temps

    def continue_select_case(self,touche):
        if touche == pygame.K_UP :
            self.element_courant = (self.element_courant[0],self.element_courant[1],self.element_courant[2]-1)
        elif touche == pygame.K_DOWN :
            self.element_courant = (self.element_courant[0],self.element_courant[1],self.element_courant[2]+1)
        elif touche == pygame.K_LEFT :
            self.element_courant = (self.element_courant[0],self.element_courant[1]-1,self.element_courant[2])
        elif touche == pygame.K_RIGHT :
            self.element_courant = (self.element_courant[0],self.element_courant[1]+1,self.element_courant[2])
        elif touche == pygame.K_SPACE and self.element_courant in self.cibles:
            if self.multi : #Si jamais une magie peut cibler plusieurs cibles.
                if self.element_courant in self.cible :
                    self.cible.remove(self.element_courant)
                else :
                    self.cible.append(self.element_courant)
            else:
                self.cible = [self.element_courant]
        elif touche == pygame.K_RETURN and self.cible != [] :
            if self.multi :
                self.cible_magie = self.cible
            else:
                self.cible_magie = self.cible[0]
            self.controleur.unset_phase(COMPLEMENT_CIBLE)
            self.methode_courante = None

    def start_change_touches(self,etage = -1,element_courant = 0): #On commence le changement de touches
        self.controleur.set_phase(TOUCHE)
        self.etage = etage #Pour pouvoir commencer directement sur le skill ou la magie qu'on vient d'acquérir
        self.element_courant = element_courant
        self.suspens = False
        zones,skills,magies,lancer = self.get_touches_courantes()
        self.affichage.choix_touche(self,zones,skills,magies,lancer)

    def continue_change_touche(self,touche):
        zones,skills,magies,lancer = self.get_touches_courantes()
        if self.suspens:
            if touche == pygame.K_RETURN : # On ne souhaite pas attribuer de nouvelle touche
                self.suspens = False
            elif touche in self.cat_touches.keys() : # La touche est déjà attribuée !
                self.affichage.message("Cette touche est déjà utilisée !")
            else :
                if self.etage == 0 :
                    self.cat_touches[touche] = "zone"
                    self.dir_touches[touche] = zones[self.element_courant]
                elif self.etage == 1 :
                    self.cat_touches[touche] = "skill"
                    self.skill_touches[touche] = type(skills[self.element_courant])
                elif self.etage == 2 :
                    self.cat_touches[touche] = "skill"
                    self.skill_touches[touche] = Skill_magie
                    self.magies[touche] = magies[self.element_courant].nom
                elif self.etage == 3 :
                    self.cat_touches[touche] = "skill"
                    self.skill_touches[touche] = Skill_lancer
                    self.projectiles[touche] = lancer[self.element_courant]
                self.affichage.message("La nouvelle touche a bien été définie.")
                self.suspens = False
        elif touche == pygame.K_UP and self.etage != -1 :
            self.element_courant = self.etage
            self.etage = -1
        elif touche == pygame.K_DOWN and self.etage == -1 :
            if self.element_courant != 4:
                self.etage = self.element_courant
                self.element_courant = 0
        elif touche == pygame.K_RIGHT :
            self.element_courant += 1
            if self.etage == -1 and self.element_courant > 4 :
                self.element_courant = 0
            elif self.etage == 0 and self.element_courant > len(zones) :
                self.element_courant = 0
            elif self.etage == 1 and self.element_courant > len(skills) :
                self.element_courant = 0
            elif self.etage == 2 and self.element_courant > len(magies) :
                self.element_courant = 0
            elif self.etage == 3 and self.element_courant > len(lancer) :
                self.element_courant = 0
        elif touche == pygame.K_LEFT :
            self.element_courant -= 1
            if self.etage == -1 and self.element_courant < 0 :
                self.element_courant = 4
            elif self.etage == 0 and self.element_courant < 0 :
                self.element_courant = len(zones)
            elif self.etage == 1 and self.element_courant < 0 :
                self.element_courant = len(skills)
            elif self.etage == 2 and self.element_courant < 0 :
                self.element_courant = len(magies)
            elif self.etage == 3 and self.element_courant < 0 :
                self.element_courant = len(lancer)
        elif touche == pygame.K_RETURN :
            if (self.etage == -1 and self.element_courant == 4) or (self.etage == 0 and self.element_courant == len(zones)) or (self.etage == 1 and self.element_courant == len(skills)) or (self.etage == 2 and self.element_courant == len(magies)) or (self.etage == 3 and self.element_courant == len(lancer)):
                if self.check_touches():
                    self.controleur.unset_phase(TOUCHE)
            else :
                if self.etage != -1 and (self.etage != 1 or not isinstance(skills[self.element_courant],(Skill_magie,Skill_lancer))):
                    self.suspens = True
                if self.etage == 0 :
                    touche = None
                    for key in self.dir_touches.keys():
                        if self.dir_touches[key] == zones[self.element_courant] and self.cat_touches[key] == "zone":
                            touche = key
                    if touche !=  None:
                        self.cat_touches.pop(touche)
                        self.dir_touches.pop(touche)
                elif self.etage == 1 :
                    touche = None
                    for key in self.skill_touches.keys():
                        if self.skill_touches[key] == type(skills[self.element_courant]):
                            touche = key
                    if touche !=  None:
                        self.cat_touches.pop(touche)
                        self.skill_touches.pop(touche)
                elif self.etage == 2 :
                    touche = None
                    for key in self.magies.keys():
                        if self.magies[key] == magies[self.element_courant].nom:
                            touche = key
                    if touche !=  None:
                        self.cat_touches.pop(touche)
                        self.skill_touches.pop(touche)
                        self.magies.pop(touche)
                elif self.etage == 3 :
                    touche = None
                    for key in self.projectiles.keys():
                        if self.projectiles[key] == lancer[self.element_courant]:
                            touche = key
                    if touche !=  None:
                        self.cat_touches.pop(touche)
                        self.skill_touches.pop(touche)
                        self.projectiles.pop(touche)
        self.affichage.choix_touche(self,zones,skills,magies,lancer)

    def check_touches(self):
        # On vérifie que les touches indispensables sont bien pourvues
        ok = True
        if len(self.dir_touches) != 10 : #Il faut impérativement pourvoir les 6 touches de zones et les touches directionnelles
            ok = False
            self.affichage.message("Les touches directionnelles et les touches de zones sont indispensables !")
        if not Skill_deplacement in self.skill_touches.values():
            self.affichage.message("Vous n'avez pas de touche pour le déplacement...")
        if not Skill_ramasse in self.skill_touches.values():
            self.affichage.message("Vous n'avez pas de touche pour ramasser les items...")
        return ok

    def get_touches_courantes(self):
        #Renvoie les éléments susceptibles d'avoir une touche attitrée
        zones = [0,1,2,3,4,5]
        skills = self.classe_principale.get_skills_actifs()
        magies = []
        lancer = [] #Pour lancer l'item courant, plutôt qu'un item créé
        magie = trouve_skill(self.classe_principale,Skill_magie)
        if magie != None:
            for mag in magie.magies.values():
                magies.append(mag)
        Lancer = trouve_skill(self.classe_principale,Skill_lancer)
        if Lancer != None:
            lancer = [None]
            fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
            if fleche != None:
                for fle in fleche.fleches:
                    lancer.append(fle)
            explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
            if explosif != None:
                for expl in explosif.explosifs:
                    lancer.append(expl)
        return zones,skills,magies,lancer

    def change_zone(self,direction):
        # On change de zone : HAUT pour remonter à la zone supérieure, BAS pour descendre dans les détails de la zone courante, GAUCHE et DROITE pour passer aux zones voisines
        if self.curseur == "carré" :
            if direction == DROITE:
                self.curseur = "rectangle_d"
            elif direction == GAUCHE:
                self.curseur = "rectangle_g"
            elif direction == IN:
                self.curseur = "liste_d"
        elif self.curseur == "rectangle_d":
            if direction == DROITE:
                self.curseur = "rectangle_g"
            elif direction == GAUCHE:
                self.curseur = "carré"
            elif direction == IN:
                self.curseur = "messages"
        elif self.curseur == "rectangle_g":
            if direction == DROITE:
                self.curseur = "carré"
            elif direction == GAUCHE:
                self.curseur = "rectangle_d"
            elif direction == IN:
                self.curseur = "inventaire"
        elif self.curseur == "stats":
            if direction == BAS:
                self.curseur = "inventaire"
            elif direction == HAUT:
                self.curseur = "classe"
            elif direction == IN:
                self.curseur = "in_stats"
            elif direction == OUT:
                self.curseur = "rectangle_g"
        elif self.curseur == "inventaire":
            if direction == BAS:
                self.curseur = "classe"
            elif direction == HAUT:
                self.curseur = "stats"
            elif direction == IN:
                self.curseur = "in_inventaire"
            elif direction == OUT:
                self.curseur = "rectangle_g"
        elif self.curseur == "classe":
            if direction == BAS:
                self.curseur = "stats"
            elif direction == HAUT:
                self.curseur = "inventaire"
            elif direction == IN:
                self.curseur = "in_classe"
            elif direction == OUT:
                self.curseur = "rectangle_g"
        elif self.curseur == "liste_d":
            if direction == DROITE:
                self.curseur = "cases"
            elif direction == GAUCHE:
                self.curseur = "cases"
            elif direction == IN:
                self.curseur = "in_liste"
            elif direction == OUT:
                self.curseur = "carré"
        elif self.curseur == "cases":
            if direction == DROITE:
                self.curseur = "liste_d"
            elif direction == GAUCHE:
                self.curseur = "liste_d"
            elif direction == IN:
                self.curseur = "in_cases"
            elif direction == OUT:
                self.curseur = "carré"
        elif self.curseur == "messages":
            if direction == IN:
                self.curseur = "in_messages"
            elif direction == OUT:
                self.curseur = "rectangle_d"
        elif self.curseur == "in_stats":
            if self.affichage.deplace_stats(direction):
                self.curseur = "stats"
        elif self.curseur == "in_inventaire":
            if self.inventaire.deplace(direction):
                self.curseur = "inventaire"
        elif self.curseur == "in_classe":
            if self.classe_principale.deplace(direction):
                self.curseur = "classe"
        elif self.curseur == "in_liste":
            if self.affichage.deplace_liste(direction):
                self.curseur = "liste_d"
        elif self.curseur == "in_cases":
            if self.affichage.deplace_cases(direction):
                self.curseur = "cases"
        elif self.curseur == "in_messages":
            if self.affichage.deplace_messages(direction):
                self.curseur = "messages"

    def level_up(self):
        """La fonction qui augmente le niveau du joueur. Augmente les stats, et offre un cadeau d'évolution au choix."""
        #Insérer toute l'augmentation des stats ici
        self.trouve_choix_possibles() #On actualise les choix possibles de l'arbre classique
        self.trouve_choix_elems() #On actualise les choix possibles de l'arbre élémentaire
        self.arbre = CLASSIQUE
        self.element_courant = 0
        self.courant = 0
        self.etage = 0
        self.event = LEVELUP
        self.controleur.set_phase(EVENEMENT)

    def evenement(self):
        """La fonction qui est appelée à chaque tour au cours d'un événement"""
        if self.event == LEVELUP:
            self.affichage.choix_niveau(self)
        elif self.event == DIALOGUE:
            self.affichage.dialogue(self)

    def trouve_choix_possibles(self):
        """La fonction qui détermine les options disponibles au choix."""
        niveau = self.niveau+1
        if niveau == 1:
            self.choix_dispos = [REGEN_HP,REGEN_MP]

        elif niveau == 2:
            if self.choix_niveaux[CLASSIQUE][1] == MAGIE:
                self.choix_dispos = [ESSENCE_MAGIQUE,MAGIE_INFINIE]
            else:
                self.choix_dispos = [DEFENSE,LANCER]

        elif niveau == 3:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_PRIORITE,BOOST_PV,BOOST_DE_PRIORITE_D_ATTAQUE]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [CREATION_FLECHES,BOOST_PV,SORT_ACCELERATION]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [BOOST_AURA,BOOST_PM,ONDE_DE_CHOC]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [SORT_DE_SOIN_SUPERIEUR,ENCHANTEMENT_FORCE,PROJECTION_ENERGIE]

        elif niveau == 4:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [ECRASEMENT,OBSERVATION,MANIPULATION_EPEE]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [BOOST_PORTEE,SORT_VISION,CREATION_EXPLOSIF]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [ELEMENTALISTE,RAYON_THERMIQUE,REGEN_MP]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [RAYON_THERMIQUE,ENCHANTEMENT_DEFENSE,REGEN_PM]

        elif niveau == 5:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_PRIORITE,ANALYSE,VOL,BOOST_ATTAQUE_EPEE]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [FLECHE_PERCANTE,OBSERVATION,FLECHE_EXPLOSIVE]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [IMMORTALITE,BOOST_DEGATS_MAGIQUES,BOOST_PRIORITE_MAGIQUE]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [ENCHANTEMENT_FAIBLESSE,EPEISTE,BOOST_RESTAURATIONS]

        elif niveau == 6:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [MANIPULATION_BOUCLIER,BOOST_PRIORITE_OBSERVATION,SORT_AUTO_SOIN]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [BOOST_DEGATS_FLECHES,CHARGE_LOURDE,CHARGE_ETENDUE]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [INHUMANITE,MAGICIEN,BOOST_DE_PORTEE]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_ATTAQUE_EPEE,BOOST_SOIN,ONDE_DE_CHOC]

        elif niveau == 7:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [SORT_DE_VUE,VOL_PRIORITE,BOOST_ATTAQUE_LANCE]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [BOOST_PRIORITE_FLECHES,FLECHE_EXPLOSIVE,ARTIFICIER]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [FANTOME,INSTAKILL,JET_DE_MANA]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [ENCHANTEMENT_RENFORCEMENT,SORT_DE_PROTECTION,BOOST_PM]

        elif niveau == 8:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_ATTAQUE,DEFENSE,BOOST_PRIORITE]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [ARCHER,FLECHE_FANTOME,BOOST_DEGAT,CHARGE_ETENDUE]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [NECROMANCIEN,BOOST_AURA,BOOST_PRIORITE]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [ENCHANTEMENT_DEFENSIF,ENCHANTEUR,SOUTIEN]

        elif niveau == 9:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_PRIORITE_DEPLACEMENT,BOOST_PRIORITE_ANALYSE,BOOST_PV]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [FLECHE_FANTOME,BOOST_PRIORITE_EXPLOSIF,BOOST_VITESSE_EXPLOSIF]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [BOOST_PRIORITE_AURA,AURA_MORTELLE,ASSASSIN]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_DE_ZONE_DE_RESTAURATION,ANGE,ENCHANTEMENT_ROUILLE]

        elif niveau == 10:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                self.choix_dispos = [MANIPULATION_ARME,BOOST_PV,DEFENSE]
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                self.choix_dispos = [FLECHES_LOURDE_LEGERE,BOOST_PRIORITE,BOOST_PORTEE_EXPLOSIFS]
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                self.choix_dispos = [ECLAIR_NOIR,BOOST_DEGATS_PROJECTILES,BOOST_PM]
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                self.choix_dispos = [BOOST_ENCHANTEMENT,RESURECTION,ECLAIR_NOIR]

    def trouve_choix_elems(self):
        """La fonction qui détermine les options disponibles au choix."""
        #On vérifie si on a une contrainte élémentaire (incompatibilité entre l'ombre et les autres éléments) :
        if self.choix_niveaux[ELEMENTAL][OMBRE][elemental] :
            self.choix_elems = []
            #On bloque tout (les autres éléments sont incompatibles, et on a atteint le summum de l'ombre)
        elif self.choix_niveaux[ELEMENTAL][OMBRE][affinite] and self.choix_niveaux[ELEMENTAL][OMBRE][aura] and self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] :
            self.choix_elems = [elemental_ombre]
        elif self.choix_niveaux[ELEMENTAL][OMBRE][affinite] and self.choix_niveaux[ELEMENTAL][OMBRE][aura] :
            #On n'a donc pas la magie d'ombre
            self.choix_elems = [magie_ombre]
        elif self.choix_niveaux[ELEMENTAL][OMBRE][aura] and self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] :
            #On n'a donc pas l'affinité
            self.choix_elems = [affinite_ombre]
        elif self.choix_niveaux[ELEMENTAL][OMBRE][affinite] or self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] :
            #On n'a donc pas l'aura
            self.choix_elems = [aura_ombre]
        #Si aucun des choix précédents n'est le bon, on n'a pas d'ombre
        elif self.choix_niveaux[ELEMENTAL][TERRE][elemental] and self.choix_niveaux[ELEMENTAL][FEU][elemental] and self.choix_niveaux[ELEMENTAL][GLACE][elemental]:
            self.choix_elems = []
            #On bloque tout (l'ombre est incompatible, et on a atteint le summum de la terre, du feu et de la glace)
        elif self.choix_niveaux[ELEMENTAL][TERRE][affinite] and self.choix_niveaux[ELEMENTAL][TERRE][aura] and self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] :
            self.choix_elems = [elemental_terre]
            #L'affinité à la terre bloque les autres éléments
        elif self.choix_niveaux[ELEMENTAL][FEU][affinite] and self.choix_niveaux[ELEMENTAL][FEU][aura] and self.choix_niveaux[ELEMENTAL][FEU][MAGIE] :
            self.choix_elems = [elemental_feu]
            #L'affinité à la feu bloque les autres éléments
        elif self.choix_niveaux[ELEMENTAL][GLACE][affinite] and self.choix_niveaux[ELEMENTAL][GLACE][aura] and self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] :
            self.choix_elems = [elemental_glace]
            #L'affinité à la glace bloque les autres éléments
        elif self.choix_niveaux[ELEMENTAL][TERRE][affinite] and self.choix_niveaux[ELEMENTAL][TERRE][aura] :
            self.choix_elems = [magie_terre]
            #L'affinité à la terre bloque les autres éléments et il manque la magie
        elif self.choix_niveaux[ELEMENTAL][FEU][affinite] and self.choix_niveaux[ELEMENTAL][FEU][aura] :
            self.choix_elems = [magie_feu]
            #L'affinité à la feu bloque les autres éléments et il manque la magie
        elif self.choix_niveaux[ELEMENTAL][GLACE][affinite] and self.choix_niveaux[ELEMENTAL][GLACE][aura] :
            self.choix_elems = [magie_glace]
            #L'affinité à la glace bloque les autres éléments et il manque la magie
        elif self.choix_niveaux[ELEMENTAL][TERRE][affinite] :
            self.choix_elems = [aura_terre]
            #L'affinité à la terre bloque les autres éléments et il manque l'aura
        elif self.choix_niveaux[ELEMENTAL][FEU][affinite] :
            self.choix_elems = [aura_feu]
            #L'affinité à la feu bloque les autres éléments et il manque l'aura
        elif self.choix_niveaux[ELEMENTAL][GLACE][affinite] :
            self.choix_elems = [aura_glace]
            #L'affinité à la glace bloque les autres éléments et il manque l'aura
        #Si aucun des choix précédents, on n'a pas d'affinité, donc pas d'incompatibilité (à part avec l'ombre éventuellement)
        elif self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] or self.choix_niveaux[ELEMENTAL][FEU][MAGIE] or self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] or self.choix_niveaux[ELEMENTAL][TERRE][elemental] or self.choix_niveaux[ELEMENTAL][FEU][elemental] or self.choix_niveaux[ELEMENTAL][GLACE][elemental]:
            #L'ombre est indisponible
            self.choix_elems = []
            #On parcours les éléments un par un
            if self.choix_niveaux[ELEMENTAL][TERRE][elemental] :
                pass
                #On a atteint le summum de la terre, pas d'autre choix ici
            elif self.choix_niveaux[ELEMENTAL][TERRE][aura] :
                #On n'a pas l'affinité (évidemment)
                self.choix_elems.append(affinite_terre)
            elif self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] :
                #On n'a pas l'aura non plus
                self.choix_elems.append(aura_terre)
            else :
                #On n'a ni l'affinité, ni la magie
                self.choix_elems.append(affinite_terre)
                self.choix_elems.append(magie_terre)
            if self.choix_niveaux[ELEMENTAL][FEU][elemental] :
                pass
                #On a atteint le summum du feu, pas d'autre choix ici
            elif self.choix_niveaux[ELEMENTAL][FEU][aura] :
                #On n'a pas l'affinité (évidemment)
                self.choix_elems.append(affinite_feu)
            elif self.choix_niveaux[ELEMENTAL][FEU][MAGIE] :
                #On n'a pas l'aura non plus
                self.choix_elems.append(aura_feu)
            else :
                #On n'a ni l'affinité, ni la magie
                self.choix_elems.append(affinite_feu)
                self.choix_elems.append(magie_feu)
            if self.choix_niveaux[ELEMENTAL][GLACE][elemental] :
                pass
                #On a atteint le summum de la glace, pas d'autre choix ici
            elif self.choix_niveaux[ELEMENTAL][GLACE][aura] :
                #On n'a pas l'affinité (évidemment)
                self.choix_elems.append(affinite_glace)
            elif self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] :
                #On n'a pas l'aura non plus
                self.choix_elems.append(aura_glace)
            else :
                #On n'a ni l'affinité, ni la magie
                self.choix_elems.append(affinite_glace)
                self.choix_elems.append(magie_glace)
        else :
            #On n'a encore fait aucun choix, donc tous les éléments sont ouverts
            self.choix_elems = [affinite_terre,magie_terre,affinite_feu,magie_feu,affinite_glace,magie_glace,affinite_ombre,magie_ombre]
        #On cherchera à raccourcir tout ça une autre fois (si si, j'y penserai !)

    def choisi_cadeau(self,touche):
        if touche == pygame.K_UP :
            if self.arbre and self.etage == 0:
                self.etage = 1
            elif not(self.arbre) and self.etage == 0:
                if len(self.choix_elems) != 0: #Attention au cas où on n'a plus de choix élémentaux valides
                    self.etage = 1
        elif touche == pygame.K_DOWN :
            if self.etage == 1:
                self.etage = 0
        elif touche == pygame.K_RIGHT :
            if self.etage == 0:
                self.arbre = not(self.arbre)
            elif self.etage == 1:
                if self.arbre :
                    self.courant += 1
                    if self.courant == len(self.choix_dispos):
                        self.courant = 0
                else :
                    self.element_courant += 1
                    if self.element_courant == len(self.choix_elems):
                        self.element_courant = 0
        elif touche == pygame.K_LEFT :
            if self.etage == 0:
                self.arbre = not(self.arbre)
            elif self.etage == 1:
                if self.arbre :
                    if self.courant == 0:
                        self.courant = len(self.choix_dispos)
                    self.courant -= 1
                else :
                    if self.element_courant == 0:
                        self.element_courant = len(self.choix_elems)
                    self.element_courant -= 1
        elif touche == pygame.K_SPACE :
            if self.etage == 1:
                if self.arbre :
                    choix = self.choix_dispos[self.courant]
                else :
                    choix = self.choix_elems[self.element_courant]
                self.controleur.unset_phase(EVENEMENT)
                self.prend_cadeau(choix)

    def prend_cadeau(self,choix):
        """Fonction qui prend le cadeau choisi"""
        niveau = self.niveau + 1
        if niveau == 1:
            if choix == REGEN_HP:
                self.regen_pv += 1 #La quantité ajouté devrait être une constante, du fichier du même nom
                self.choix_niveaux[CLASSIQUE][1] = PHYSIQUE
            elif choix == REGEN_MP:
                self.regen_pm += 1 #Même remarque ici
                self.choix_niveaux[CLASSIQUE][1] = MAGIE
            else:
                self.choix_niveaux[CLASSIQUE][1] = PHYSIQUE_PAR_DEFAUT

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 2:
            if choix == DEFENSE:
                skill = Skill_defense() #On crée un skill à donner au joueur
                skill.evo() #Au niveau 1, le skill, c'est mieux
                self.classe_principale.skills.append(skill)
                self.choix_niveaux[CLASSIQUE][2] = DEFENSE
            elif choix == LANCER:
                skill = Skill_lancer() #On crée un skill à donner au joueur
                skill.evo() #Au niveau 1, le skill, c'est mieux
                self.classe_principale.skills.append(skill)
                self.choix_niveaux[CLASSIQUE][2] = LANCER
            elif choix == ESSENCE_MAGIQUE:
                skill = Skill_essence_magique() #On crée un skill à donner au joueur
                skill.evo() #Au niveau 1, le skill, c'est mieux
                self.classe_principale.skills.append(skill)
                self.choix_niveaux[CLASSIQUE][2] = ESSENCE_MAGIQUE
            elif choix == MAGIE_INFINIE:
                skill = Skill_magie_infinie() #On crée un skill à donner au joueur
                skill.evo() #Au niveau 1, le skill, c'est mieux
                self.classe_principale.skills.append(skill)
                self.choix_niveaux[CLASSIQUE][2] = MAGIE_INFINIE
            elif self.choix_niveaux[CLASSIQUE][1] == MAGIE:
                self.choix_niveaux[CLASSIQUE][2] = MAGIE_INFINIE_PAR_DEFAUT
            else:
                self.choix_niveaux[CLASSIQUE][2] = DEFENSE_PAR_DEFAUT

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 3:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == BOOST_PRIORITE:
                    self.priorite += 1 #Hum, est-ce que c'est assez ? Trop ? En faire une constante pour pouvoir la modifier plus facilement
                    self.choix_niveaux[CLASSIQUE][3] = BOOST_PRIORITE
                elif choix == BOOST_PV:
                    self.pv_max += 100 #Même questions et remarque que plus haut
                    self.choix_niveaux[CLASSIQUE][3] = BOOST_PV
                elif choix == BOOST_DE_PRIORITE_D_ATTAQUE:
                    self.force += 10 #Je sais, ce n'est pas la priorité d'attaque. Mais c'est bien aussi, non ? Je ne suis même pas sûr que la priorité joue un rôle dans les attaques, de toute façon...
                    self.choix_niveaux[CLASSIQUE][3] = BOOST_DE_PRIORITE_D_ATTAQUE
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == CREATION_FLECHES:
                    skill = Skill_creation_de_fleches([Cree_fleche_de_base_skill()]) #On crée un skill à donner au joueur
                    skill.evo() #Au niveau 1, le skill, c'est mieux
                    self.classe_principale.skills.append(skill) #Ce skill ne peut pas vraiment être utilisé pour l'instant...
                    self.choix_niveaux[CLASSIQUE][3] = CREATION_FLECHES
                elif choix == BOOST_PV:
                    self.pv_max += 100 #Même questions et remarque que plus haut (plus plus haut que ça)
                    self.choix_niveaux[CLASSIQUE][3] = BOOST_PV
                elif choix == SORT_ACCELERATION:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_acceleration) #Il faudra créer ce sort, sous peine de devoir commenter cette ligne
                    self.choix_niveaux[CLASSIQUE][3] = SORT_ACCELERATION
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == BOOST_AURA:
                    skill = Skill_boost_aura() #Je crois que ce skill est encore à inventer
                    skill.evo() #Au niveau 1, le skill, c'est mieux
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][3] = BOOST_AURA #Fun fact : le joueur qui choisi ce skill ne peut pas avoir d'aura à booster à ce stade. Le skill n'est donc pas utilisé et n'aide pas à monter de niveau, mais c'est un investissement payant si le joueur survit (et s'oriente vers les auras...)
                elif choix == BOOST_PM:
                    self.pm_max += 100 #Même questions et remarque que plus haut (encore plus haut que ça)
                    self.choix_niveaux[CLASSIQUE][3] = BOOST_PM
                elif choix == ONDE_DE_CHOC:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_onde_de_choc) #Il faudra créer ce sort, sous peine de devoir commenter cette ligne
                    self.choix_niveaux[CLASSIQUE][3] = ONDE_DE_CHOC
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == SORT_DE_SOIN_SUPERIEUR:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_soin_superieur) #Parce que le joueur a déjà un sort de soin ? Dès le début, obtenu en récompense d'un niveau précédent ?
                    self.choix_niveaux[CLASSIQUE][3] = SORT_DE_SOIN_SUPERIEUR
                elif choix == ENCHANTEMENT_FORCE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_force) #Vérifier le nom exact de la magie ("Enchantement_de_force" potentiellement)
                    self.choix_niveaux[CLASSIQUE][3] = ENCHANTEMENT_FORCE
                elif choix == PROJECTION_ENERGIE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_jet_de_mana) #Il me semble que c'est bien la même chose
                    self.choix_niveaux[CLASSIQUE][3] = PROJECTION_ENERGIE

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 4:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == ECRASEMENT:
                    skill = Skill_ecrasement() #Un mur ? Où ça ? Un mob ? Où ça ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][4] = ECRASEMENT
                elif choix == OBSERVATION:
                    skill = Skill_observation() # Un prérequis de l'analyse et du vol. Permet de savoir ce qui ne nous regarde pas.
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][4] = OBSERVATION
                elif choix == MANIPULATION_EPEE:
                    skill = Skill_manipulation_epee() # Augmente l'efficacité des attaque à l'épée. Dans un jeu idéal, fournirait aussi de nouveaux mouvements...
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][4] = MANIPULATION_EPEE
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == BOOST_PORTEE:
                    lancer = trouve_skill(self.classe_principale,Skill_lancer)
                    lancer.boost_portee()
                    self.choix_niveaux[CLASSIQUE][4] = BOOST_PORTEE
                elif choix == SORT_VISION:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_vision) #Peut-être proposer un autre sort, moins consommateur de PM, qui se place automatiquement sur le lanceur ?
                    self.choix_niveaux[CLASSIQUE][4] = SORT_VISION #Autre idée : un skill ou un sort qui permet d'afficher la vue de l'esprit, et pas celle du joueur. Pour avoir une meilleure compréhension des champs de bataille.
                elif choix == CREATION_EXPLOSIF:
                    skill = Skill_creation_d_explosifs([Cree_charge_de_base_skill()])
                    skill.evo() #Au niveau 1, le skill, c'est mieux
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][4] = CREATION_EXPLOSIF
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == ELEMENTALISTE:
                    classe = Elementaliste() # Où comment rendre l'arbre des éléments cheaté
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][4] = ELEMENTALISTE
                elif choix == RAYON_THERMIQUE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_laser)
                    self.choix_niveaux[CLASSIQUE][4] = RAYON_THERMIQUE
                elif choix == REGEN_MP:
                    self.regen_pm += 1
                    self.choix_niveaux[CLASSIQUE][4] = REGEN_MP
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == RAYON_THERMIQUE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_laser) #C'est bien les mêmes ?
                    self.choix_niveaux[CLASSIQUE][4] = RAYON_THERMIQUE
                elif choix == ENCHANTEMENT_DEFENSE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_defense) #À créer, je crois...
                    self.choix_niveaux[CLASSIQUE][4] = ENCHANTEMENT_DEFENSE
                elif choix == REGEN_PM:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_regeneration_pm) #Un transfert de pm à quelqu'un d'autre, grosso-modo. À créer, je pense.
                    self.choix_niveaux[CLASSIQUE][4] = REGEN_PM

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 5:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == BOOST_PRIORITE:
                    self.priorite += 1 #Hum, est-ce que c'est assez ? Trop ? En faire une constante pour pouvoir la modifier plus facilement
                    self.choix_niveaux[CLASSIQUE][5] = BOOST_PRIORITE
                elif choix == ANALYSE:
                    skill = Skill_analyse() #Peut analyser les termes du système et révéler la vérité sur le monde. Pas beaucoup d'utilité en pratique, mais un joueur débutant peut l'utiliser pour découvrir le fonctionnement du jeu
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = ANALYSE
                elif choix == VOL:
                    skill = Skill_vol() #Pourquoi tuer le monstre, quand on peut récupérer la clé de la porte directement dans sa poche ? Fonctionne aussi sur les humains, et les alliés de façon plus générale (gniark gniark gniark)
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = VOL
                elif choix == BOOST_ATTAQUE_EPEE:
                    skill = Skill_boost_attaque_epee()
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = BOOST_ATTAQUE_EPEE
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == FLECHE_PERCANTE:
                    creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches) 
                    creation_fleche.ajoute(Cree_fleche_percante_skill()) #Une flèche qui traverse même si elle ne tue pas ?
                    self.choix_niveaux[CLASSIQUE][5] = FLECHE_PERCANTE
                elif choix == OBSERVATION:
                    skill = Skill_observation()
                    skill.evo() #Au niveau 1, le skill, c'est mieux
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = OBSERVATION
                elif choix == FLECHE_EXPLOSIVE:
                    creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
                    if creation_fleche !=  None:
                        creation_fleche.ajoute(Cree_fleche_explosive_skill())
                    creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
                    if creation_explosif != None:
                        creation_explosif.ajoute(Cree_fleche_explosive_skill())
                    self.choix_niveaux[CLASSIQUE][5] = FLECHE_EXPLOSIVE
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == IMMORTALITE: #Sérieusement.
                    skill = Skill_immortel() #Non mais vraiment, ça rend immortel.
                    skill.evo() #Impossible de mourir, quelle que soient les circonstances !
                    self.classe_principale.skills.append(skill) #Et ce n'est qu'un début !
                    self.choix_niveaux[CLASSIQUE][5] = IMMORTALITE #Vous verrez.
                elif choix == BOOST_DEGATS_MAGIQUES:
                    skill = Boost_degats_magiques() #Je vois mal comment ça fonctionnera, honnêtement. Il n'est jamais trop tard pour changer d'avis...
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = BOOST_DEGATS_MAGIQUE
                elif choix == BOOST_PRIORITE_MAGIQUE:
                    skill = Boost_priorite_magique() #Et là, je vois à peine mieux.
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = BOOST_PRIORITE_MAGIQUE
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == ENCHANTEMENT_FAIBLESSE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_faiblesse) #Donner toute la panoplie des déboosts d'un coup ?
                    self.choix_niveaux[CLASSIQUE][5] = ENCHANTEMENT_FAIBLESSE
                elif choix == EPEISTE:
                    classe = Epeiste() #Oui, épéiste mage, et alors ?
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][5] = EPEISTE
                elif choix == BOOST_RESTAURATIONS:
                    skill = Boost_restaurations() #Un skill qui boost les soins et restaurations de PM
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][5] = BOOST_RESTAURATIONS

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 6:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == MANIPULATION_BOUCLIER:
                    skill = Skill_manipulation_bouclier() #Ce skill augmente l'efficacité des bouclier et ouvre à de nouveaux mouvements, on peut se servir d'un bouclier sans.
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][6] = MANIPULATION_BOUCLIER
                elif choix == BOOST_PRIORITE_OBSERVATION:
                    skill = Skill_boost_priorite_observation()
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][6] = BOOST_PRIORITE_OBSERVATION
                elif choix == SORT_AUTO_SOIN:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_auto_soin)
                    self.choix_niveaux[CLASSIQUE][6] = SORT_AUTO_SOIN
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == BOOST_DEGATS_FLECHES:
                    skill = Skill_boost_degats_fleches() #Ce skill n'existe pas encore... Est-ce qu'il fonctionne sur les flèches de glace (magie) ?
                    skill.evo() #Au niveau 1, le skill, c'est mieux
                    self.classe_principale.skills.append(skill) #Ce skill ne peut pas vraiment être utilisé pour l'instant...
                    self.choix_niveaux[CLASSIQUE][6] = BOOST_DEGATS_FLECHES
                elif choix == CHARGE_LOURDE:
                    creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
                    creation_explosif.ajoute(Cree_charge_lourde_skill()) #Beaucoup de dégats, petite zone
                    self.choix_niveaux[CLASSIQUE][6] = CHARGE_LOURDE
                elif choix == CHARGE_ETENDUE:
                    creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
                    creation_explosif.ajoute(Cree_charge_etendue_skill()) #Peu de dégats, grande zone
                    self.choix_niveaux[CLASSIQUE][6] = CHARGE_ETENDUE
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == INHUMANITE:
                    self.especes.remove('humain') #Ça évite de se faire agresser par la plupart des monstres. Les amis humains risquent de ne pas apprécier, par contre...
                    self.choix_niveaux[CLASSIQUE][6] = INHUMANITE
                elif choix == MAGICIEN:
                    classe = Magicien() #Un gros boost à tout ce qui est orienté magie.
                    classe.evo() #Et la classe Magicien peut récupérer le skill Magie
                    self.classe_principale.sous_classes.append(classe) #On me souffle à l'oreillette que monter la classe Mage au niveau 10 suffit à obtenir Magicien, par contre... À condition que j'implémente Mage
                    self.choix_niveaux[CLASSIQUE][6] = MAGICIEN
                elif choix == BOOST_DE_PORTEE:
                    skill = Boost_portee() #Portee des magie, évidemment... je suppose ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][6] = BOOST_DE_PORTEE
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == BOOST_ATTAQUE_EPEE:
                    skill = Boost_epee() # Il ne boost que l'attaque ? À voir...
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][6] = BOOST_ATTAQUE_EPEE
                elif choix == BOOST_SOIN:
                    skill = Boost_soin() # Un boost spécifique aux sorts de soin
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][6] = BOOST_SOIN
                elif choix == ONDE_DE_CHOC:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_onde_de_choc)
                    self.choix_niveaux[CLASSIQUE][6] = ONDE_DE_CHOC

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 7:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == SORT_DE_VUE: #Oh, un sort, il s'est perdu le pauvre ?
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_de_vision) #Mettre un autre sort moins couteux, on n'a pas tant de mana nous !
                    self.choix_niveaux[CLASSIQUE][7] = SORT_DE_VUE
                elif choix == VOL_PRIORITE:
                    skill = Skill_vol_priorite() #Je ne suis pas convaincu par le fonctionnement de ces capacités de vol...
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][7] = VOL_PRIORITE
                elif choix == BOOST_ATTAQUE_LANCE:
                    skill = Skill_boost_lance()
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][7] = BOOST_ATTAQUE_LANCE
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == BOOST_PRIORITE_FLECHES:
                    skill = Skill_boost_priorite_fleches() #Quand est-ce que la priorité des flèches intervient ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][7] = BOOST_PRIORITE_FLECHES
                elif choix == FLECHE_EXPLOSIVE:
                    creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
                    if creation_fleche !=  None:
                        creation_fleche.ajoute(Cree_fleche_explosive_skill())
                    creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
                    if creation_explosif != None:
                        creation_explosif.ajoute(Cree_fleche_explosive_skill())
                    self.choix_niveaux[CLASSIQUE][7] = FLECHE_EXPLOSIVE
                elif choix == ARTIFICIER:
                    classe = Artificier()
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][7] = ARTIFICIER
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == FANTOME:
                    #On rajoute fantome à notre espèce ? À notre pseudo-classe ? C'est une vraie classe ? À voir... Permet de traverser les murs, en tous cas.
                    self.choix_niveaux[CLASSIQUE][7] = FANTOME #Fun fact : le joueur qui choisi ce skill ne peut pas avoir d'aura à booster à ce stade. Le skill n'est donc pas utilisé et n'aide pas à monter de niveau, mais c'est un investissement payant si le joueur survit (et s'oriente vers les auras...)
                elif choix == INSTAKILL:
                    skill = Skill_instakill() #Pour tuer sans se salir les mains (si l'instakill réussit, personne n'est au courant... en général)
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][7] = INSTAKILL
                elif choix == JET_DE_MANA:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_jet_de_mana)
                    self.choix_niveaux[CLASSIQUE][7] = JET_DE_MANA
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == ENCHANTEMENT_RENFORCEMENT:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_renforcement) # Pour renforcer les items ! Les épées, à tout hasard...
                    self.choix_niveaux[CLASSIQUE][7] = ENCHANTEMENT_RENFORCEMENT
                elif choix == SORT_DE_PROTECTION:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_protection) # Protège tous les gens autour (enfin, juste les alliés)
                    self.choix_niveaux[CLASSIQUE][7] = SORT_DE_PROTECTION
                elif choix == BOOST_PM:
                    self.pm_max += 100
                    self.choix_niveaux[CLASSIQUE][7] = BOOST_PM

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 8:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == BOOST_ATTAQUE:
                    self.force += 10
                    self.choix_niveaux[CLASSIQUE][8] = BOOST_ATTAQUE
                elif choix == DEFENSE:
                    skill = Skill_defense() #Pour ceux qui l'ont raté en utilisant l'arbre des éléments
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][8] = DEFENSE
                elif choix == BOOST_PRIORITE:
                    self.priorite += 1 #Très monotone, cet arbre, vous ne trouvez pas ?
                    self.choix_niveaux[CLASSIQUE][8] = BOOST_PRIORITE
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == ARCHER:
                    classe = Archer()
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][8] = ARCHER
                elif choix == FLECHE_FANTOME:
                    creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
                    creation_fleche.ajoute(Cree_fleche_fantome_skill()) #Une fleche qui ignore les murs
                    self.choix_niveaux[CLASSIQUE][8] = FLECHE_FANTOME
                elif choix == BOOST_DEGAT:
                    self.force += 10 #Les dégats de projectiles ne sont pas affectés par la force, je crois...
                    self.choix_niveaux[CLASSIQUE][8] = BOOST_DEGAT
                elif choix == CHARGE_ETENDUE:
                    creation_explosif = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
                    creation_explosif.ajoute(Cree_charge_etendue_skill()) #La deuxième et dernière chance de l'obtenir
                    self.choix_niveaux[CLASSIQUE][8] = CHARGE_ETENDUE
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == NECROMANCIEN: #Quand je vous disais que l'immortalité n'était qu'un début...
                    classe = Necromancien() #Le nécromancien est immortel (c'est une condition pour le devenir) et ranime ses ennemis et ses alliés pour qu'ils le servent.
                    classe.evo() #En général, ça se passe comme ça : *TOC TOC* - Auriez-vous cinq minutes pour parler de notre seigneur Eskom, prince des ténèbres ?
                    self.classe_principale.sous_classes.append(classe) # - Bien sûr que vous les avez, vous êtes mort... Mais le seigneur Eskom, prince des ténèbres, peut vous accorder une nouvelle vie... à mon service.
                    self.choix_niveaux[CLASSIQUE][8] = NECROMANCIEN #Bon, nécromancien est incompatible avec plein de trucs, mais il serait trop puissant sinon (il bloque les montées de niveau de la classe principale ?)
                elif choix == BOOST_AURA:
                    skill = Skill_boost_aura() #Là, ça s'adresse plus aux full-ombre/instakill qu'aux futurs-triple-élémentaux
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][8] = BOOST_AURA
                elif choix == BOOST_PRIORITE:
                    self.priorite += 1
                    self.choix_niveaux[CLASSIQUE][8] = BOOST_PRIORITE
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == ENCHANTEMENT_DEFENSIF:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_defensif) #Confère à un objet des propriétés défensives
                    self.choix_niveaux[CLASSIQUE][5] = ENCHANTEMENT_DEFENSIF
                elif choix == ENCHANTEUR:
                    classe = Enchanteur() #Pour enchanter encore plus efficacement
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][8] = ENCHANTEUR
                elif choix == SOUTIEN:
                    classe = Soutien() #Pas très fou honnêtement. Mais entre les dix niveaux de croissance à venir et la possibilité de prendre l'ange au prochain niveau, ça commence à se valoir...
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][8] = SOUTIEN

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 9:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == BOOST_PRIORITE_DEPLACEMENT:
                    skill = Skill_boost_priorite_deplacement() #Pour rendre l'écrasement plus efficace
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_DEPLACEMENT
                elif choix == BOOST_PRIORITE_ANALYSE:
                    skill = Skill_boost_priorite_analyse() # C'est que certains trucs ne se laisse pas analyser si facilement !
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_ANALYSE
                elif choix == BOOST_PV:
                    self.pv_max += 100
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_PV
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == FLECHE_FANTOME:
                    creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
                    creation_fleche.ajoute(Cree_fleche_fantome_skill()) #Une fleche qui ignore les murs
                    self.choix_niveaux[CLASSIQUE][9] = FLECHE_FANTOME
                elif choix == BOOST_PRIORITE_EXPLOSIF:
                    skill = Skill_boost_priorite_explosifs() #Quand est-ce que la priorité des explosifs intervient ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_EXPLOSIF
                elif choix == BOOST_VITESSE_EXPLOSIF:
                    skill = Skill_boost_vitesse_explosifs() #Voilà qui va me faire beaucoup de skills à créer...
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_VITESSE_EXPLOSIF
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == BOOST_PRIORITE_AURA:
                    skill = Skill_boost_priorite_aura()
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_PRIORITE_AURA
                elif choix == AURA_MORTELLE:
                    skill = Skill_aura_mortelle()
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = AURA_MORTELLE
                elif choix == ASSASSIN:
                    classe = Assassin()
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][9] = ASSASSIN
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == BOOST_DE_ZONE_DE_RESTAURATION:
                    skill = Skill_boost_zone_restauration() #Je crois que ce skill est encore à inventer. Qu'est-ce qu'il est censé faire déjà ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][9] = BOOST_DE_ZONE_DE_RESTAURATION
                elif choix == ANGE:
                    classe = Ange() # Le soigneur/renforceur ultime. Mais devra s'y reprendre à trois fois pour tuer une mouche.
                    classe.evo()
                    self.classe_principale.sous_classes.append(classe)
                    self.choix_niveaux[CLASSIQUE][9] = ANGE
                elif choix == ENCHANTEMENT_ROUILLE:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_enchantement_rouille) #Il me semble que c'est bien la même chose
                    self.choix_niveaux[CLASSIQUE][9] = ENCHANTEMENT_ROUILLE

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        elif niveau == 10:
            if self.choix_niveaux[CLASSIQUE][2] in [DEFENSE,DEFENSE_PAR_DEFAUT]:
                if choix == MANIPULATION_ARME:
                    skill = Skill_manipulation_arme() #Une option pour le décaller dans une autre classe, maître d'armes à tout hasard ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][10] = MANIPULATION_ARME
                elif choix == BOOST_PV:
                    self.pv_max += 100
                    self.choix_niveaux[CLASSIQUE][10] = BOOST_PV
                elif choix == DEFENSE:
                    skill = Skill_defense() # Comment ça, j'essaye "encore" de le recaser ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][10] = DEFENSE
            elif self.choix_niveaux[CLASSIQUE][2] == LANCER:
                if choix == FLECHES_LOURDE_LEGERE:
                    creation_fleche = trouve_skill(self.classe_principale,Skill_creation_de_fleches)
                    creation_fleche.ajoute(Cree_fleche_lourde_skill())
                    creation_fleche.ajoute(Cree_fleche_legere_skill()) #Pour compléter l'éventail de l'archer amateur comme du sniper professionnel, variez les plaisirs et optez pour le duo flèche lourd, flèche légère !
                    self.choix_niveaux[CLASSIQUE][10] = FLECHES_LOURDE_LEGERE
                elif choix == BOOST_PRIORITE:
                    self.priorite += 1
                    self.choix_niveaux[CLASSIQUE][10] = BOOST_PRIORITE
                elif choix == BOOST_PORTEE_EXPLOSIFS:
                    creation_explosifs = trouve_skill(self.classe_principale,Skill_creation_d_explosifs)
                    creation_explosifs.boost_portee()
                    self.choix_niveaux[CLASSIQUE][10] = BOOST_PORTEE_EXPLOSIFS
            elif self.choix_niveaux[CLASSIQUE][2] == ESSENCE_MAGIQUE:
                if choix == ECLAIR_NOIR:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_eclair_noir) # À la fois le sort et le projectile le plus puissant du jeu ! Dévastateur dans toutes les situations, peut annihiler une horde et pousser le boss final à la fuite ! Ok, peut-être pas le boss final...
                    self.choix_niveaux[CLASSIQUE][10] = ECLAIR_NOIR
                elif choix == BOOST_DEGATS_PROJECTILES:
                    skill = Skill_boost_degats_projectiles() # Je ne sais plus à quoi il sert. Pour les sorts de projectiles, peut-être ?
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][10] = BOOST_DEGATS_PROJECTILES
                elif choix == BOOST_PM:
                    self.pm_max += 100
                    self.choix_niveaux[CLASSIQUE][10] = BOOST_PM
            elif self.choix_niveaux[CLASSIQUE][2] in [MAGIE_INFINIE,MAGIE_INFINIE_PAR_DEFAUT]:
                if choix == BOOST_ENCHANTEMENT:
                    skill = Skill_boost_enchantement() # Non, les boosts intrasecs à la classe enchanteur ne sont pas suffisant...
                    skill.evo()
                    self.classe_principale.skills.append(skill)
                    self.choix_niveaux[CLASSIQUE][10] = BOOST_ENCHANTEMENT
                elif choix == RESURECTION:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_resurection) # Quand on laisse ses alliés faire tout le sale boulot, ça peut servir...
                    self.choix_niveaux[CLASSIQUE][10] = RESURECTION
                elif choix == ECLAIR_NOIR:
                    magie = trouve_skill(self.classe_principale,Skill_magie)
                    magie.ajoute(Magie_eclair_noir) # À la fois le sort et le projectile le plus puissant du jeu ! Dévastateur dans toutes les situations, peut annihiler une horde et pousser le boss final à la fuite ! Ok, peut-être pas le boss final...
                    self.choix_niveaux[CLASSIQUE][10] = ECLAIR_NOIR

            self.pv_max += 10
            self.pm_max += 10
            self.niveau += 1
            self.priorite += 1

        #Pour les affinités, c'est simple (sauf si on veut rescussiter le skill d'augmentation de l'affinité):
        if choix == affinite_terre :
            self.aff_t *= 1.5
            self.aff_o *= 0.9 #L'ombre se mélange vraiment mal avec le reste
            self.choix_niveaux[ELEMENTAL][TERRE][affinite] = True
            if self.prem_terre == None:
                self.prem_terre = affinite
        elif choix == affinite_feu :
            self.aff_f *= 1.5
            self.aff_o *= 0.9 #L'ombre se mélange vraiment mal avec le reste
            self.choix_niveaux[ELEMENTAL][FEU][affinite] = True
            if self.prem_feu == None:
                self.prem_feu = affinite
        elif choix == affinite_glace :
            self.aff_g *= 1.5
            self.aff_o *= 0.9 #L'ombre se mélange vraiment mal avec le reste
            self.choix_niveaux[ELEMENTAL][GLACE][affinite] = True
            if self.prem_glace == None:
                self.prem_glace = affinite
        elif choix == affinite_ombre :
            self.aff_o *= 1.5
            self.aff_t *= 0.9 #L'ombre se mélange vraiment mal avec le reste
            self.aff_f *= 0.9 #L'ombre se mélange vraiment mal avec le reste
            self.aff_g *= 0.9 #L'ombre se mélange vraiment mal avec le reste
            self.choix_niveaux[ELEMENTAL][OMBRE][affinite] = True
            if self.prem_ombre == None:
                self.prem_ombre = affinite

        #Pour les auras, il faudra rajouter le choix de ratacher le skill à la classe élémentaliste
        elif choix == aura_terre :
            skill = Skill_aura_elementale_terre(Aura_terre) #On crée le skill
            skill.evo() #On le passe au niveau 1
            self.classe_principale.skills.append(skill)
            self.choix_niveaux[ELEMENTAL][TERRE][aura] = True
        elif choix == aura_feu :
            skill = Skill_aura_elementale_feu(Aura_feu) #On crée le skill
            skill.evo() #On le passe au niveau 1
            self.classe_principale.skills.append(skill)
            self.choix_niveaux[ELEMENTAL][FEU][aura] = True
        elif choix == aura_glace :
            skill = Skill_aura_elementale_glace(Aura_glace) #On crée le skill
            skill.evo() #On le passe au niveau 1
            self.classe_principale.skills.append(skill)
            self.choix_niveaux[ELEMENTAL][GLACE][aura] = True
        elif choix == aura_ombre :
            skill = Skill_aura_elementale_ombre(Aura_ombre) #On crée le skill
            skill.evo() #On le passe au niveau 1
            self.classe_principale.skills.append(skill)
            self.choix_niveaux[ELEMENTAL][OMBRE][aura] = True

        # Pour les magies, on se contente de les rajouter aux magies disponibles du skill magie (créer un skill spécifique qui peut rapporter de l'xp pour une autre classe que la principale ? vérifier que les magies n'y sont pas encore ?)
        elif choix == magie_terre :
            skill = trouve_skill(self.classe_principale,Skill_magie)
            skill.ajoute(Magie_rocher)
            skill.ajoute(Magie_enchantement_sable)
            skill.ajoute(Magie_avalanche)
            self.choix_niveaux[ELEMENTAL][TERRE][MAGIE] = True
            if self.prem_terre == None:
                self.prem_terre = MAGIE
        elif choix == magie_feu :
            skill = trouve_skill(self.classe_principale,Skill_magie)
            skill.ajoute(Magie_boule_de_feu)
            skill.ajoute(Magie_enchantement_flamme)
            skill.ajoute(Magie_brasier)
            self.choix_niveaux[ELEMENTAL][FEU][MAGIE] = True
            if self.prem_feu == None:
                self.prem_feu = MAGIE
        elif choix == magie_glace :
            skill = trouve_skill(self.classe_principale,Skill_magie)
            skill.ajoute(Magie_fleche_de_glace)
            skill.ajoute(Magie_enchantement_neige)
            skill.ajoute(Magie_blizzard)
            self.choix_niveaux[ELEMENTAL][GLACE][MAGIE] = True
            if self.prem_glace == None:
                self.prem_glace = MAGIE
        elif choix == magie_ombre :
            skill = trouve_skill(self.classe_principale,Skill_magie)
            skill.ajoute(Magie_ombre_furtive)
            skill.ajoute(Magie_enchantement_tenebre)
            skill.ajoute(Magie_obscurite)
            self.choix_niveaux[ELEMENTAL][OMBRE][MAGIE] = True
            if self.prem_ombre == None:
                self.prem_ombre = MAGIE

        # Pour les élémentaux, il faudra rajouter le choix de ratacher la classe d'élémental à la classe élémentaliste, et de déplacer le skill d'aura vers la nouvelle classe d'élémental (et le skill d'affinité si on le crée)
        elif choix == elemental_terre :
            classe = Elemental_de_terre()
            classe.evo()
            self.classe_principale.sous_classes.append(classe)
            self.choix_niveaux[ELEMENTAL][TERRE][elemental] = True
            self.choix_niveaux[ELEMENTAL][TERRE][affinite] = False
            self.immunites.append(TERRE)
        elif choix == elemental_feu :
            classe = Elemental_de_feu()
            classe.evo()
            self.classe_principale.sous_classes.append(classe)
            self.choix_niveaux[ELEMENTAL][FEU][elemental] = True
            self.choix_niveaux[ELEMENTAL][FEU][affinite] = False
            self.immunites.append(FEU)
        elif choix == elemental_glace :
            classe = Elemental_de_glace()
            classe.evo()
            self.classe_principale.sous_classes.append(classe)
            self.choix_niveaux[ELEMENTAL][GLACE][elemental] = True
            self.choix_niveaux[ELEMENTAL][GLACE][affinite] = False
            self.immunites.append(GLACE)
        elif choix == elemental_ombre :
            classe = Elemental_d_ombre()
            classe.evo()
            self.classe_principale.sous_classes.append(classe)
            self.choix_niveaux[ELEMENTAL][OMBRE][elemental] = True
            self.choix_niveaux[ELEMENTAL][OMBRE][affinite] = False
            self.immunites.append(OMBRE)

    def discute(self,touche):
        self.interlocuteur.parle(touche)

class Receptionniste(Humain): #Le deuxième humain du jeu, à l'étage 1 (engage la conversation après la chute, indique les commandes de base)
    """La classe du récéptionniste."""
    def __init__(self,position):

        self.identite = 'receptionniste'
        self.place = 1

        Humain.__init__(self,position,self.identite,5,3) #À un haut niveau dès le départ

        self.appreciations = [0,3,0,0,0,0,1,3,6,0]
        self.dialogue = 1

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite, et qu'il n'y ait aucun allié en danger au front
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.2 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : modifier le taux limite en fonction des autres humains en danger au front et de l'appréciation qu'on a pour eux
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Qu'est-ce que je peux faire pour toi ?"
            self.repliques = ["Va quelque part.","Change ta méthode de combat.","C'est une question personnelle."] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
        elif self.dialogue == -2: #Le joueur est venu nous voir avant d'être sorti du premier couloir
            self.replique = "Qu'est-ce qu'il y a ?"
            self.repliques = ["Je ne trouve pas l'escalier.","Il n'y a pas d'autre chemin ?","Merci encore pour ton aide."]
        elif self.dialogue == 1: #Le joueur vient de tomber
            self.replique = "Quelle chute ! Tu vas bien ? Appuie sur Espace si tu peux m'entendre."
            self.repliques = [""]
        elif self.dialogue == 2: #Le joueur vient de se dégourdir les jambes
            self.replique = "Alors, ça va mieux ?"
            self.repliques = ["Oui, un peu. Où est-on ?","Je suis en pleine forme maintenant ! Où est-ce que je devrais aller ?"]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        if nb_replique in range(len(self.repliques)): #Une vérification stupide, au cas où
            replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        else:
            print("Mais quel est l'idiot qui m'a codé ça comme un pied ?")
            print(self.repliques)
            print(nb_replique)
            return
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le receptionniste accueil le joueur
        if replique == "":
            self.replique="Tu peux te lever ? Utilise les flèches directionnelles pour te diriger, et W pour marcher. Appuie sur Espace à côté de moi pour revenir me parler."
            self.repliques = ["Merci pour ton aide."]
        elif replique == "Merci pour ton aide.":
            self.appreciations[0]+= 0.5
            self.end_dialogue(2)

        #Deuxième dialogue
        #Le receptionniste guide le joueur vers l'escalier
        elif replique == "Oui, un peu. Où est-on ?":
            self.replique = "Dans le labyrinthe de [insérer le nom de la montagne/mine/caverne ici]. La sortie est gardée par un [insérer le nom du boss ici] que je n'ai pas réussi à vaincre."
            self.repliques = ["Un [insérer le nom du boss ici] ? J'en ai croisé un là-haut, il m'a fait tomber ici.","La sortie ? Où ça ?"]
        elif replique == "Un [insérer le nom du boss ici] ? J'en ai croisé un là-haut, il m'a fait tomber ici.":
            self.replique = "Heureusement que ton armure t'a protégé de la chute..."
            self.repliques = ["Et du coup, où est la sortie ?"]
        elif replique == "Et du coup, où est la sortie ?":
            self.replique = "Il y a un escalier au bout du couloir, à droite."
            self.repliques = [" "]
        elif replique == "La sortie ? Où ça ?":
            self.replique = "Il y a un escalier au bout du couloir, à droite."
            self.repliques = [" "]
        elif replique == "Je suis en pleine forme maintenant ! Où est-ce que je devrais aller ?":
            self.replique = "Il y a un escalier au bout du couloir, à droite."
            self.repliques = [" "]
        elif replique == " ":
            self.end_dialogue(-2)

        elif replique == "Je ne trouve pas l'escalier.":
            self.replique = "Au bout du couloir, à droite."
            self.repliques = [" "]
        elif replique == "Il n'y a pas d'autre chemin ?":
            self.replique = "Il y a bien une porte tout à gauche, mais elle est fermée à clée."
            self.repliques = ["Tant pis. Je vais essayer l'escalier alors."]
        elif replique == "Tant pis. Je vais essayer l'escalier alors.":
            self.replique = "Bon courage !"
            self.repliques = [" "]
        elif replique == "Merci encore pour ton aide.":
            self.replique = "De rien."
            self.repliques = [" "]

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_RECEPTIONNISTE

class Paume(Humain): #Le troisième humain du jeu, à l'étage 2 (complêtement paumé, rejoint le joueur sauf rares exceptions)
    """La classe du mec paumé."""
    def __init__(self,position):

        self.identite = 'paume'
        self.place = 2

        Humain.__init__(self,position,self.identite,1,4) #Plutôt faible, de base

        self.appreciations = [1,1,3,2,0,0,0,7,4,-1]
        self.dialogue = 1

        #Est-ce qu'il a un minimum d'équippement ?

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.1 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : modifier le taux limite en fonction des autres humains en danger au front et de l'appréciation qu'on a pour eux (exceptionnel, pour le cas où le paumé serait amoureux, sinon il obéit et fuit normalement)
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Je peux me rendre utile ?"
            self.repliques = ["Va quelque part.","Change ta méthode de combat.","J'aimerais parler avec toi."] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
        elif self.dialogue == -2: #Le joueur nous a très mal traité
            self.replique = "Quoi ?"
            self.repliques = ["Rien !","Tu veux que je t'aide à sortir d'ici ?","Je voudrais m'excuser pour ce que j'ai dit."]
        elif self.dialogue == 1: #Le joueur vient d'arriver depuis le premier étage
            self.replique = "Quelle chance, il y a quelqu'un ici !"
            self.repliques = ["Bonjour...","Je ne fais que passer, au-revoir."]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par l'escalier
        if replique == "Bonjour...":
            self.replique="Où est-ce que tu vas comme ça ?"
            self.repliques = ["Je cherche la sortie."]
        elif replique == "Je cherche la sortie.":
            self.replique="Ces grottes sont un vrai labyrinthe, tu risquerais de te perdre !"
            self.repliques = ["Je vais y aller quand même.","Il y a un autre chemin ?"]
        elif replique == "Il y a un autre chemin ?":
            self.replique="Non..."
            self.repliques = ["Alors je n'ai pas d'autre choix que d'y aller"]
        elif replique in ["Je vais y aller quand même.","Alors je n'ai pas d'autre choix que d'y aller"]:
            self.replique="Ton courage est impressionnant ! Moi, je suis ici depuis plusieurs jours."
            self.repliques = ["Tu peux venir avec moi, si ça te rassure.","Tu es vraiment pathétique."]
        elif replique == "Tu peux venir avec moi, si ça te rassure.":
            self.replique="Merci beaucoup ! N'hésite pas à me demander si tu as besoin de quelque-chose"
            self.repliques = ["Je ferai appel à toi."]
            self.appreciations[0]+= 0.5
        elif replique == "Je ferai appel à toi.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Tu es vraiment pathétique.":
            self.appreciations[0]-= 0.5
            self.end_dialogue(-2)
        elif replique == "Je ne fais que passer, au-revoir.":
            self.appreciations[0]-= 0.5
            self.end_dialogue(-2)

        #Dialogue par défaut -2
        elif replique == "Rien !":
            self.end_dialogue(-2)
        elif replique == "Tu veux que je t'aide à sortir d'ici ?":
            self.replique="Non merci, je préfère rester bloquer que demander ton aide !"
            self.repliques = ["Eh bien reste-ici !"]
        elif replique == "Eh bien reste-ici !":
            self.end_dialogue(-2)
        elif replique == "Je voudrais m'excuser pour ce que j'ai dit.":
            self.replique="... Bon, je te pardonne."
            self.repliques = ["Du coup, on va à la sortie ?"]
            self.appreciations[0]+= 0.5
        elif replique == "Du coup, on va à la sortie ?":
            self.replique="Ok, montre-moi le chemin."
            self.repliques = ["Tache de ne pas te perdre.","Fais-moi confiance !"]
        elif replique == "Tache de ne pas te perdre.":
            self.appreciations[0]-= 0.5
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Fais-moi confiance !":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_PAUME

class Peureuse(Humain): #La quatrième humaine du jeu, à l'étage 3 (terrorisée par les monstres)
    """La classe de la peureuse."""
    def __init__(self,position):

        self.identite = 'peureuse'
        self.place = 3

        Humain.__init__(self,position,self.identite,1,5) #Plutôt faible, de base

        self.appreciations = [1,1,0,-1,0,9,1,6,-1,-1]
        self.dialogue = 1

        #Est-ce qu'elle a un minimum d'équippement ?

        #Peut recevoir l'ordre : d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas) ou en présence d'un monstre à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.7 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : fuire dès qu'il y a un monstre en vue et accessible
    # et ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def boost(self):
        #On cherche un allié à booster
        #À compléter quand on aura des magies de boost à utiliser
        return False

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Tu as besoin de quelque chose ?"
            self.repliques = ["Tu pourrais aller quelque part ?","Discutons un peu."] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
        elif self.dialogue == -2: #Le joueur nous a mal traîté
            self.replique = "Tu as du culot de revenir me parler après ce que tu m'as dit !"
            self.repliques = [""]
        elif self.dialogue == 1: #Le joueur vient d'arriver depuis le deuxième étage
            self.replique = "Bonjour !"
            self.repliques = ["Salut...","Bonjour ma jolie."]
        elif self.dialogue == 2: #On a atteint les premiers monstres
            self.replique = "Nous nous rapprochons du camp gobelin, il serait bien que je t'explique quelques trucs sur les monstres."
            self.repliques = ["Oui, volontiers.","C'est gentil de proposer, mais je n'ai pas besoin d'aide.","Tu me prends pour un débutant ? Tu crois que je ne connais pas les monstres ?"]
        elif self.dialogue == 3: #On a atteint la prison
            self.replique = "Est-ce que tu vois ces portes dans les murs autour de toi ?"
            self.repliques = ["Oui.","Ces [insérer une description ici] ?","Évidemment, je ne suis pas aveugle !"]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par l'escalier
        if replique in ["Salut...","Désolé..."]:
            self.replique=""
            self.repliques = ["...qu'est-ce que tu fais ici ?","...où est la sortie ?"]
        elif replique == "...qu'est-ce que tu fais ici ?":
            self.replique="Je voudrais continuer, mais il y a des monstres sur le chemin."
            self.repliques = ["Tu veux que je les tue pour toi ?","Des monstres ? Ils sont dangereux ?"]
        elif replique == "...où est la sortie ?":
            self.replique="Tout en bas."
            self.repliques = ["Pourquoi tu n'y vas pas ?"]
        elif replique == "Pourquoi tu n'y vas pas ?":
            self.replique="Il y a des monstres sur le chemin."
            self.repliques = ["Tu veux que je les tue pour toi ?","Des monstres ? Ils sont dangereux ?"]
        elif replique == "Tu veux que je les tue pour toi ?":
            self.replique="S'il te plaît !"
            self.repliques = ["Laisse-moi faire."]
        elif replique == "Laisse-moi faire.":
            self.appreciations[0] += 0.5
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Des monstres ? Ils sont dangereux ?":
            self.replique="Un peu. C'est surtout que je suis fragile..."
            self.repliques = ["Je vais essayer de les combattre.","Pff... les faibles n'ont qu'à mourir."]
        elif replique == "Je vais essayer de les combattre.":
            self.replique="Je peux te suivre ?"
            self.repliques = ["Oui, viens.","Non, tu ne ferais que me gêner."]
        elif replique == "Oui viens.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Non, tu ne ferais que me gêner.":
            self.appreciations[0]-= 0.5
            self.end_dialogue(-2)
        elif replique == "Pff... les faibles n'ont qu'à mourir.":
            self.appreciations[0]-= 0.5
            self.end_dialogue(-2)
        elif replique == "Bonjour ma jolie.":
            self.replique="Ne me parle pas si familièrement."
            self.repliques = ["Désolé...","Allez, fais pas ta timide..."]
        elif replique == "Allez, fais pas ta timide...":
            self.replique="Sérieusement, t'es lourd ! J'ai déjà un copain, [insérer le nom du copain ici], alors arrête !"
            self.repliques = ["Désolé..."]

        #Dialogue par défaut -2
        elif replique == "":
            self.end_dialogue(-2)

        #Dialogue de description des monstres
        elif replique == "Oui, volontiers.":
            self.replique="Les monstres sont très différents les uns des autres, aussi bien par leurs comportements que par leurs capacitées."
            self.repliques = ["Donc, ils ne vont pas tous attendre sans bouger comme ceux de l'étage précédent ?","Leurs capacitées ? Tu veux dire leur puissance de combat ?"]
        elif replique == "Donc, ils ne vont pas tous attendre sans bouger comme ceux de l'étage précédent ?":
            self.replique="Exactement. Ceux-là sont des sentinnelles, ils ne bougent que quand ils aperçoivent un ennemi."
            self.repliques = ["Attendre qu'on vienne à eux est donc plutôt une exception ?","Est-ce qu'il y a d'autres monstres que des gobelins ici ?"]
        elif replique == "Attendre qu'on vienne à eux est donc plutôt une exception ?":
            self.replique="Oui. C'est encore plus rare chez les monstres non-humanoïdes comme les slimes."
            self.repliques = ["Il existe différentes espèces de monstres ?","Et qu'est-ce que tu disais sur leurs capacitées ?"]
        elif replique in ["Il existe différentes espèces de monstres ?","Est-ce qu'il y a d'autres monstres que des gobelins ici ?"]:
            self.replique="IL y a les gobelins, les orcs, les slimes, les ombriuls... certains ne sont pas hostiles aux humains, et ne combattront que si on les provoque."
            self.repliques = ["Et qu'est-ce que tu disais sur leurs capacitées ?"]
        elif replique == "Et qu'est-ce que tu disais sur leurs capacitées ?":
            self.replique="Certains ont une meilleure défense, ou une bonne vitesse, d'autres peuvent même utiliser de la magie pour attaquer ou soigner."
            self.repliques = ["Et il faut qu'on combatte tout ça ? Ah, la galère...","Et bien, nous aussi, donc on s'en sortira !"]
        elif replique == "Et il faut qu'on combatte tout ça ? Ah, la galère...":
            self.replique="Hélas..."
            self.repliques = ["Bon, allons-y."]
        elif replique == "Et bien, nous aussi, donc on s'en sortira !":
            self.appreciations[0]+= 0.5
            self.replique="Oui ! Je te fais confiance !"
            self.repliques = ["Bon, allons-y."]
        elif replique == "Leurs capacitées ? Tu veux dire leur puissance de combat ?":
            self.replique="Entre autre, mais je pensais plutôt aux capacités comme le soin, ou les attaques magiques."
            self.repliques = ["Ces créatures peuvent utiliser de la magie ?"]
        elif replique == "Ces crétures peuvent utiliser de la magie ?":
            self.replique="Les humanoïdes comme les gobelins comptent parfois des mages dans leurs rangs."
            self.repliques = ["Donc ils ont des rôles spécifiques...","Et les monstres non-humanoïdes ?"]
        elif replique == "Donc ils ont des rôles spécifiques...":
            self.replique="Exactement. Les sentinelles qu'on a croisés à l'étage précédent sont spécialisés en défense et ne se déplacent que quand ils aperçoivent un ennemi, alors que d'autres nous cherchent activement."
            self.repliques = ["Pourquoi faut-il qu'ils veuillent tous notre peau...","Ces gobelins sont bien organisés."]
        elif replique == "Pourquoi faut-il qu'ils veuillent tous notre peau...":
            self.replique="La plupart des monstres ont une dent contre les humains, mais pas tous. Il arrive même qu'ils se battent entre espèces."
            self.repliques = ["Il y a beaucoup d'espèces de monstres ici ?"]
        elif replique == "Il y a beaucoup d'espèces de monstres ici ?":
            self.replique="Je ne sais pas, et j'espère en croiser le moins possible..."
            self.repliques = ["Ne t'inquiète pas, je te protégerai.","On verra bien. Allons-y."]
        elif replique == "Ne t'inquiète pas, je te protégerai.":
            self.replique="Merci !"
            self.appreciations[0]+=0.5
            self.repliques = ["Bon, allons-y."]
        elif replique == "Ces gobelins sont bien organisés.":
            self.replique="C'est peut-être parce qu'ils ont un chef ? Les orcs sont un peu pareil."
            self.repliques = ["Je vois... Bon, on y va ?"]
        elif replique == "Je vois... Bon, on y va ?":
            self.replique="Oui, allons-y."
            self.repliques = ["  "]
        elif replique == "C'est gentil de proposer, mais je n'ai pas besoin d'aide.":
            self.replique="D'accord, bonne chance."
            self.repliques = ["  "]
        elif replique in ["  ","On verra bien. Allons-y.","Bon, allons-y."]:
            self.end_dialogue()
        elif replique == "Tu me prends pour un débutant ? Tu crois que je ne connais pas les monstres ?":
            self.replique="Ne viens pas te plaindre si tu meurs !"
            self.repliques = [" "]

        #Dialogue de la prison
        elif replique == "Oui.":
            self.replique="Il te faut des clés pour les ouvrir."
            self.repliques = ["Des clés ? Où est-ce que je peux les trouver ?"]
        elif replique == "Des clés ? Où est-ce que je peux les trouver ?":
            self.replique="Par terre, après avoir tué un monstre par exemple. Ramasse-les avec la touche m."
            self.repliques = ["Ok, je regarderai autour de moi."]
        elif replique == "Ok, je regarderai autour de moi.":
            self.controleur.entitees[0].inventaire.ramasse(self.inventaire.get_clee("Porte_entree_encombrant_5")) #On refile au joueur la clé dont il a besoin
            self.replique="Attends ! J'en ai une, elle te sera peut-être utile."
            self.repliques = ["Merci. J'y vais alors.","Comment tu l'as trouvée ?"]
        elif replique == "Merci. J'y vais alors.":
            self.end_dialogue()
        elif replique == "Comment tu l'as trouvée ?":
            self.replique="Un des gobelins l'a laissée tomber quand ils ont capturés mon petit-ami."
            self.repliques = ["Tu crois qu'il est enfermé ici ? Je vais le libérer."]
        elif replique == "Tu crois qu'il est enfermé ici ? Je vais le libérer.":
            self.appreciations[0]+= 0.5
            self.end_dialogue()
        elif replique == "Ces [insérer une description ici] ?":
            self.replique="C'est ça. Il te faut des clés pour les ouvrir."
            self.repliques = ["Des clés ? Où est-ce que je peux les trouver ?"]
        elif replique == "Évidemment, je ne suis pas aveugle !":
            self.replique="Alors je suppose que tu sauras trouver les clés tout seul !"
            self.controleur.entitees[0].inventaire.ramasse(self.inventaire.get_clee("Porte_entree_encombrant_5")) #On refile quand même au joueur la clé dont il a besoin
            self.repliques = [" "]
        elif replique == " ":
            self.appreciations[0]-= 0.5
            self.end_dialogue()

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_PEUREUSE

class Codeur(Humain): #Le cinquième humain du jeu, à l'étage 4 (répond au nom de Dev, quand Il n'est pas occupé à programmer un autre jeu)
    """Ma classe."""
    def __init__(self,position):

        self.identite = 'codeur'
        self.place = 4

        Humain.__init__(self,position,self.identite,1,1) #La notion de niveau n'a pas d'emprise sur Dev... Il peut modifier son niveau simple 'self.niveau = '

        self.appreciations = [5,0,0,0,0,0,0,0,0,0]

    def fuite(self):
        return False

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef (c'est la seule option pour parler à Dev dans le tuto)
            self.replique = "Salut, qu'est-ce que tu viens faire ici ?"
            self.repliques = ["Je me suis perdu !","Je voulais explorer tous les recoins."]
        elif self.dialogue == -2: #Le joueur nous a dit qu'il s'était perdu
            self.replique = "Salut, qu'est-ce que tu viens faire ici ?"
            self.repliques = ["Je me suis perdu !","Je voulais explorer tous les recoins. "]
        elif self.dialogue == -3: #Le joueur ne s'intéresse qu'aux combats
            self.replique = "Alors, comment vont tes combats ?"
            self.repliques = ["Bien, merci."]
        elif self.dialogue == -4: #Le joueur est revenu mentir
            self.replique = "Tu n'obtiendras rien de plus de moi."
            self.repliques = ["  "]
        elif self.dialogue == -5: #Le joueur a écouté nos conseils
            self.replique = "Salut, quoi de neuf ?"
            self.repliques = ["Je passais juste dire bonjour.","Est-ce que je peux entendre tes conseils à nouveaux ?"]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive vers Dev
        if replique == "Je me suis perdu !":
            self.replique="Ahah, c'est fait pour. Bonne chance pour la suite."
            self.repliques = [""]
        elif replique == "":
            self.end_dialogue(-2)
        elif replique == "Je voulais explorer tous les recoins.":
            self.replique="Tu as bien raison. Observe, examine, scrute les moindres détails, cherche la vérité, et tu seras victorieux !"
            self.repliques = ["Ça va vraiment m'aider à combattre les monstres ?","Quels genre de détails dois-je chercher ?"]
        elif replique == "Ça va vraiment m'aider à combattre les monstres ?":
            self.replique="Pas vraiment."
            self.repliques = ["Je vais y aller alors."]
        elif replique == "Je vais y aller alors.":
            self.end_dialogue(-3)
        elif replique == "Quels genre de détails dois-je chercher ?":
            self.replique="Tu peux observer les inscriptions sur les murs, écouter ce que les PNJs ont à te dire... la suite viendra plus tard."
            self.repliques = ["Merci pour ces conseils."]
        elif replique == "Merci pour ces conseils.":
            self.appreciations[0] += 0.5
            self.end_dialogue(-5)

        #Dialogue par défaut -2
        elif replique == "Je voulais explorer tous les recoins. ":
            self.replique="Vraiment ? Tu viens de me dire que tu t'étais perdu pourtant..."
            self.repliques = [" "]
        elif replique == " ":
            self.replique="Tu pensais vraiment que je ne m'en souviendrais pas ?"
            self.repliques = ["Désolé, je ne voulais pas te mentir..."]
        elif replique == "Désolé, je ne voulais pas te mentir...":
            self.replique="Allez, vas-y."
            self.repliques = ["  "]
        elif replique == "  ":
            self.end_dialogue(-4)

        #Dialogue par défaut -3
        elif replique == "Bien, merci.":
            self.end_dialogue(-3)

        #Dialogue par défaut -5
        elif replique == "Je passais juste dire bonjour.":
            self.replique="Tu as des choses plus importantes à faire..."
            self.repliques = ["Oui, j'y vais."]
        elif replique == "Oui, j'y vais":
            self.end_dialogue(-5)
        elif replique == "Est-ce que je peux entendre tes conseils à nouveaux ?":
            self.replique="Quelle partie ? 'Observe, examine, scrute les moindres détails, cherche la vérité, et tu seras victorieux !' ou 'Tu peux observer les inscriptions sur les murs, écouter ce que les PNJs ont à te dire... la suite viendra plus tard.' ?"
            self.repliques = ["Les deux, merci !"]
        elif replique == "Les deux, merci !":
            self.end_dialogue(-5)

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_CODEUR

class Encombrant(Humain): #Le sixième humain du jeu, à l'étage 5 (moyennement apprèciable, surtout si on essaye de draguer sa copine)
    """La classe de l'encombrant."""
    def __init__(self,position):

        self.identite = 'encombrant'
        self.place = 5

        Humain.__init__(self,position,self.identite,2,6) #En plus il a fallu que ce soit un combattant relativement aguerri...

        self.appreciations = [0,1,-1,6,0,5,0,3,3,0]
        self.dialogue = 1

        #Penser à l'équipper

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.4 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Tu as besoin de quelque chose ?"
            self.repliques = ["J'ai besoin que tu ailles quelque part.","Change de stratégie au combat.","On peut discuter ?"]
        elif self.dialogue == -2: #Le joueur nous a offensé !
            self.replique = "Meurs !"
            self.repliques = [""]
        elif self.dialogue == 1: #Le vient de passer la porte
            self.replique = "Hey, salut ! Moi c'est [insérer le nom du copain ici]."
            self.repliques = ["Moi c'est Arvel.","Alors c'est toi, son copain !"] #/!\ N'afficher la réplique du copain que si on a discuté de son copain avec la peureuse

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "Moi c'est Arvel.":
            self.replique="Content de te voir !"
            self.repliques = ["Moi aussi, mais comment je te fais sortir d'ici ? La porte se referme après mon passage."]
        elif replique == "Moi aussi, mais comment je te fais sortir d'ici ? La porte se referme après mon passage.":
            self.replique="Il y a une autre clé ici. Tu peux la ramasser avec la touche M. Elle ouvre la porte là-bas, qui ne se referme pas." #/!\ Faire dépendre de la touche effectivement utilisée par le joueur !
            self.repliques = ["Cool ! On y va alors !","Je vais ressortir par l'autre porte en fait, au-revoir."]
        elif replique == "Cool ! On y va alors !":
            self.replique="Merci pour ça. Je te le revaudrai."
            self.repliques = ["Alors je te demanderai si j'ai besoin d'aide."]
        elif replique == "Alors je te demanderai si j'ai besoin d'aide.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Je vais ressortir par l'autre porte en fait, au-revoir.":
            self.end_dialogue(-2)
            #self.controleur.get_esprit(self.esprit).antagonise(truc comme ça ou une offense ?
            #+ modifier le role, ou quelque chose, pour qu'il combatte
            self.attente = False
        elif replique == "Alors c'est toi, son copain !":
            self.replique="Quoi ?"
            self.repliques = ["Je vais te tuer, mais ce n'est rien de personnel."]
        elif replique == "Je vais te tuer, mais ce n'est rien de personnel.":
            #self.controleur.get_esprit(self.esprit).antagonise(truc comme ça ou une offense ?
            #+ modifier le role, ou quelque chose, pour qu'il combatte
            self.attente = False
            self.end_dialogue(-2)

        #Dialogue par défaut -2
        elif replique == "":
            self.end_dialogue(-2)

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_ENCOMBRANT

class Alchimiste(Humain): #Le septième humain du jeu, à l'étage 6 (un faiseur de potions aux magies diverses)
    """La classe de l'alchimiste."""
    def __init__(self,position):

        self.identite = 'alchimiste'
        self.place = 6

        Humain.__init__(self,position,self.identite,5,7) #Puissant, mais pas le plus utile en combat...

        self.appreciations = [0,1,0,0,0,0,2,-2,2,-3]
        self.dialogue = 1

        #Penser à l'équipper, et à remplir son inventaire de potions

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas) à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.3 + 0.01*self.appreciations[1] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir et ne pas fuir si on n'est pas à portée de monstres

    def attaque_en_vue(self):
        #On cherche le meilleur endroit pour placer une attaque de zone
        #À compléter quand on aura des magies d'attaque à utiliser
        return False

    def attaque(self,direction):
        #Quelle est sa magie de prédilection ? Pour l'instant on va prendre l'avalanche
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        if self.peut_payer(cout_pm_avalanche[skill.niveau-1]):
            self.skill_courant = Skill_magie
            self.magie_courante = "avalanche" #/!\
            self.dir_magie = direction
        else:
            self.skill_courant = Skill_stomp

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Mes talents sont-ils requis ?"
            self.repliques = ["J'ai besoin que tu ailles quelque part.","Change de stratégie au combat.","Fais-moi une potion.","Examine une potion.","Lance un sort.","On peut discuter ?"]
        elif self.dialogue == -2: #Le joueur nous a traité de vieillard
            self.replique = "Qu'est-ce qu'il y a, gamin ?"
            self.repliques = ["Tu ne voudrais pas rejoindre notre groupe ? Pour ta propre sécurité.","Désolé pour mon comportement."]
        elif self.dialogue == 1:
            self.replique = "Ho ho ho ! Y aurait-il d'autres humains coincés ici ?"
            self.repliques = ["Oui, tu veux nous rejoindre ?","Ne fais pas attention, vieillard, on ne faisait que passer."]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "Oui, tu veux nous rejoindre ?":
            self.replique="Avec grand plaisir ! Mes talents d'alchimiste vous serons d'une grande aide."
            self.repliques = ["Un alchimiste ! Qu'est-ce que tu peux faire ?","Je ferais appel à toi."]
        elif replique == "Un alchimiste ! Qu'est-ce que tu peux faire ?":
            self.replique="Créer des potions, examiner des potions... Je sais aussi utiliser plein de magies."
            self.repliques = ["Je ferais appel à toi."]
        elif replique == "Je ferais appel à toi.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Ne fais pas attention, vieillard, on ne faisait que passer.":
            self.appreciations[0] -= 0.5
            self.end_dialogue(-2)

        #Dialogue par défaut -2
        elif replique == "Tu ne voudrais pas rejoindre notre groupe ? Pour ta propre sécurité.":
            self.replique="Non merci, je me débrouille très bien tout seul."
            self.repliques = ["Comme tu voudras.","Ne t'étonne pas de mourir !"]
        elif replique == "Comme tu voudras.":
            self.end_dialogue(-2)
        elif replique == "Ne t'étonne pas de mourir !":
            self.end_dialogue(-2)
            #self.controleur.get_esprit(self.esprit).antagonise(truc comme ça ou une offense ?
            #+ modifier le role, ou quelque chose, pour qu'il combatte
            self.attente = False
        elif replique == "Désolé pour mon comportement.":
            self.replique="Disons que ça passe pour cette fois."
            self.repliques = ["Du coup, est-ce que tu voudrais rejoindre notre groupe ?"]
        elif replique == "Du coup, est-ce que tu voudrais rejoindre notre groupe ?":
            self.replique="Pourquoi pas. On n'est plus forts à plusieurs."
            self.repliques = ["Bienvenu. Et désolé encore."]
        elif replique == "Bienvenu. Et désolé encore.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_ALCHIMISTE

class Peste(Humain): #La huitième humaine du jeu, à l'étage 7 (une sainte très à cheval sur beaucoup trop de trucs)
    """La classe de la peste."""
    def __init__(self,position):

        self.identite = 'peste'
        self.place = 7

        Humain.__init__(self,position,self.identite,3,8) #Très bonne soigneuse, accessoirement

        self.appreciations = [1,-1,-2,-2,0,-3,-1,9,-4,-1]
        self.dialogue = 1

        #Penser à l'équipper

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas)
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.1 + 0.01*self.appreciations[7] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir et ne pas fuir si on n'est pas à portée de monstre

    def heal(self):
        #On cherche Un allié à soigner
        #À compléter quand on aura une magie de soin à utiliser
        return False

    def attaque(self,direction):
        #Quelle est sa magie de prédilection ? Pour l'instant on va prendre l'avalanche
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        if self.peut_payer(cout_pm_avalanche[skill.niveau-1]):
            self.skill_courant = Skill_magie
            self.magie_courante = "purification" #/!\
            self.dir_magie = direction
        else:
            self.skill_courant = Skill_stomp

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Qu'est-ce que je dois faire pour tuer plus de monstres ?"
            self.repliques = ["Si tu vas à un certain, endroit, on pourrait tuer plus de monstres.","Je voulais te parler d'un truc."]
        elif self.dialogue == -2: #Le joueur veut se débrouiller seul
            self.replique = "(Je n'arriverai jamais à tuer tous les monstres...)"
            self.repliques = ["Tu parles toute seule ? Tu ne serais pas un peu folle ?","On peut s'entraider pour tuer les monstres ?"]
        elif self.dialogue == -3: #Le joueur ne veut pas tuer tous les monstres
            self.replique = "Tu peux me laisser ? J'ai des monstres à tuer."
            self.repliques = [" "]
        elif self.dialogue == -4:
            self.replique = "Meurs !"
            self.repliques = ["  "]
        elif self.dialogue == 1:
            self.replique = "Hey, toi !"
            self.repliques = ["Qu'est-ce qu'il y a ?","Ne me parle pas comme ça !"]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "Qu'est-ce qu'il y a ?":
            self.replique="J'ai besoin d'aide pour tuer tous ces immondes monstres."
            self.repliques = ["Tu pourrais rejoindre notre groupe.","Est-on obligé de tous les tuer ?"]
        elif replique == "Tu pourrais rejoindre notre groupe.":
            self.replique="Ok. Je peux vous soigner si ces sales monstres vous blessent."
            self.repliques = ["Tu as des capacité de guérison ?","D'accord."]
        elif replique == "Tu as des capacité de guérison ?":
            self.replique="Je suis la Sainte choisie par le grand Dieu [insérer le nom d'un Dieu ici] ! Tu ne trouveras pas de meilleure guérisseuse dans tout [insérer le nom d'une capitale ici]."
            self.repliques = ["Waoh ! Je compterais sur toi alors."]
        elif replique in ["Waoh ! Je compterais sur toi alors.","D'accord.","Je veux bien"]:
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Est-on obligé de tous les tuer ?":
            self.appreciations[0] -= 0.5
            self.replique="Tu voudrais laisser ces vermines en vie !?"
            self.repliques = ["Non, non, bien sûr que non...","Si ça peut nous permettre de rester en vie..."]
        elif replique == "Non, non, bien sûr que non...":
            self.replique="Alors, tu m'aides ?"
            self.repliques = ["Non, je me débrouillerai tout seul.","Je veux bien."]
        elif replique == "Non, je me débrouillerai tout seul.":
            self.end_dialogue(-2)
        elif replique == "Si ça peut nous permettre de rester en vie...":
            self.end_dialogue(-3)

        #Dialogue par défaut -2
        elif replique == "Tu parles toute seule ? Tu ne serais pas un peu folle ?":
            self.replique="De quel droit m'insulte-tu ? Meurs !"
            self.repliques = [""]
        elif replique == "":
            self.end_dialogue(-4)
            #self.controleur.get_esprit(self.esprit).antagonise(truc comme ça ou une offense ?
            #+ modifier le role, ou quelque chose, pour qu'elle combatte
            self.attente = False
        elif replique == "On peut s'entraider pour tuer les monstres ?":
            self.replique="Humph. D'accord."
            self.repliques = ["Merci."]
        elif replique == "Merci":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False

        #Dialogue par défaut -3
        elif replique == " ":
            self.end_dialogue(-3)

        #Dialogue par défaut -4
        elif replique == "  ":
            self.end_dialogue(-4)

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_PESTE

class Bombe_atomique(Humain): #La neuvième humaine du jeu, à l'étage 8 (une magicienne légèrement aguicheuse)
    """La classe de la bombe atomique."""
    def __init__(self,position):

        self.identite = 'bombe_atomique'
        self.place = 8

        Humain.__init__(self,position,self.identite,4,9) #Ses magies sont littéralement explosives !

        self.appreciations = [3,-1,1,-1,0,2,1,-1,3,0]
        self.dialogue = 1

        #Penser à l'équipper

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas) ou en présence d'un monstre à condition d'avoir un chemin de fuite
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.3 + 0.01*self.appreciations[8] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir

    def attaque(self,direction):
        #Quelle est sa magie de prédilection ? Pour l'instant on va prendre l'avalanche
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        if self.peut_payer(cout_pm_poing_ardent[skill.niveau-1]):
            self.skill_courant = Skill_magie
            self.magie_courante = "magie poing ardent"
        else:
            self.skill_courant = Skill_stomp

    def attaque_en_vue(self):
        #On cherche le meilleur endroit pour placer une attaque de zone
        #À compléter quand on aura des magies d'attaque à utiliser
        return False

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Tu as besoin d'aide, mon chou ?"
            self.repliques = ["Est-ce que tu pourrais aller quelque-part ?","C'est à propos des combats.","On peut parler en privé ?"]
        elif self.dialogue == -2:
            self.replique = "Ah, c'est encore toi ?"
            self.repliques = ["Tu ne voudrais pas m'accompagner ?","Désolé, je me suis trompé de personne."]
        elif self.dialogue == -3:
            self.replique = "Meurs !"
            self.repliques = ["   "]
        elif self.dialogue == 1:
            self.replique = "Bonjour mon chou..."
            self.repliques = ["Bonjour ma belle.","Bonjour..."]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "Bonjour ma belle.":
            self.appreciations[0] += 0.5
            self.replique="Qu'est-ce qui t'amène ici ?"
            self.repliques = ["Je cherche la sortie.","Je t'ai aperçue de loin, et j'ai voulu faire ta connaissance."]
        elif replique == "Je cherche la sortie.":
            self.replique="Moi aussi. On peut faire un bout de chemin ensemble ?"
            self.repliques = ["Avec plaisir.","Non merci."]
        elif replique in ["Avec plaisir.","Comment refuser une compagnie si agréable ?"]:
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Non merci.":
            self.end_dialogue(-2)
        elif replique == "Je t'ai aperçue de loin, et j'ai voulu faire ta connaissance.":
            self.appreciations[0] += 0.5
            self.replique="Ahah... Tu veux que je tienne un peu compagnie ?"
            self.repliques = ["Comment refuser une compagnie si agréable ?","Non merci."]
        elif replique == "Bonjour...":
            self.replique=""
            self.repliques = ["...tu sais où est la sortie ?","...tu sais te battre ?"]
        elif replique == "...tu sais où est la sortie ?":
            self.replique="Au centième étage. Tu as encore du chemin à faire..."
            self.repliques = ["Tu pourrais m'aider ?","Je n'ai pas de temps à perdre alors. À plus."]
        elif replique == "Tu pourrais m'aider ?":
            self.replique="Je suppose que je peux t'accompagner pour un bout du chemin."
            self.repliques = ["Merci"]
        elif replique == "Je n'ai pas de temps à perdre alors. À plus.":
            self.end_dialogue(-2)
        elif replique == "...tu sais te battre ?":
            self.replique="Tu veux que je te montre ?"
            self.repliques = ["Non, je te crois. Ça t'intéresserait de venir avec moi ?","Ouais, amène-toi."]
        elif replique == "Non, je te crois. Ça t'intéresserait de venir avec moi ?":
            self.replique="Oui. Demande-moi si tu as un monstre à carboniser."
            self.repliques = ["J'y penserai."]
        elif replique == "J'y penserai.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Ouais, amène-toi.":
            self.replique="Non, je voulais dire, te montrer sur les monstres."
            self.repliques = ["Je te fais peur ?","Ok. Accompagne-moi alors."]
        elif replique == "Je te fais peur ?":
            self.replique="Tu l'auras voulu..."
            self.repliques = [" "]
        elif replique == " ":
            self.end_dialogue(-3)
            #self.controleur.get_esprit(self.esprit).antagonise(truc comme ça ou une offense ?
            #+ modifier le role, ou quelque chose, pour qu'elle combatte
            self.attente = False
        elif replique == "Ok. Accompagne-moi alors.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False

        #Dialogue par défaut -2
        elif replique == "Tu ne voudrais pas m'accompagner ?":
            self.replique="Ok."
            self.repliques = ["  "]
        elif replique == "  ":
            self.appreciations[0] -= 0.5
            self.end_dialogue()
        elif replique == "Désolé, je me suis trompé de personne.":
            self.end_dialogue(-2)

        #Dialogue par défaut -3
        elif replique == "   ":
            self.end_dialogue(-3)

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_BOMBE_ATOMIQUE

class Marchand(Humain): #Le dixième humain du jeu, à l'étage 9 (le seul lien avec l'extérieur)
    """La classe du marchand."""
    def __init__(self,position):

        self.identite = 'marchand'
        self.place = 9

        Humain.__init__(self,position,self.identite,1,10) #Il a un skill d'échange d'objet avec son patron à l'extérieur

        self.appreciations = [0,0,-1,0,0,-1,0,3,0,2]
        self.dialogue = 1

        #Est-ce qu'il a un minimum d'équippement ? Ou est-ce qu'il achète son équippement de base après avoir rencontré le joueur ?

        #Peut recevoir l'ordre : d'attaquer (chercher et combattre les ennemis),
        #                        de tuer (éliminer un ennemi ciblé),
        #                        d'attendre (rester sur place jusqu'à l'arrivée d'ennemis ou un nouvel ordre),
        #                        de tenir une position (rester sur place à tout prix),
        #                        d'aller (se diriger vers l'endroit ciblé, en éliminant les ennemis en cours de route, puis y attendre),
        #                        de fuir (se mettre à l'abri en évitant les combats),
        #                        d'explorer (chercher la sortie),
        #                        de suivre (se déplacer avec le joueur, combattre les monstres en chemin, aller vers la sortie lorsque quelqu'un l'a trouvée)

    def fuite(self):
        #On fuit si on est en danger (pv trop bas)
        #Pour l'instant on va juste vérifier les pv :
        taux_limite = 0.4 + 0.01*self.appreciations[9] #Quand on se hait, on devient plus suicidaire
        return self.pv // self.pv_max <= taux_limite

    # /!\ Pour améliorer ça : ne pas fuir s'il n'y a nulle part où fuir ou si le joueur a donné ordre de ne pas fuir et qu'on a suffisamment d'appréciation pour lui (rajouter un modificateur au taux_limite ?)

    def start_dialogue(self): #On commence un nouveau dialogue !
        #On initialise nos attributs
        self.replique_courante = 0
        #La plupart dépendent du dialogue
        if self.dialogue == -1: #Le joueur est venu nous voir de son propre chef
            self.replique = "Un client !"
            self.repliques = ["Non, je voulais te donner une consigne.","Je voudrais vendre.","Je voudrais acheter"]
        elif self.dialogue == -2:
            self.replique = "Un client !"
            self.repliques = ["Je voudrais vendre.","Je voudrais acheter"]
        elif self.dialogue == 1:
            self.replique = "Vous avez besoin de quelque chose ?"
            self.repliques = ["Vous pouvez faire quelque chose pour moi ?"]

    def interprete(self,nb_replique):
        #Dans une première version simple, je suppose qu'une même réplique n'apparaît pas deux fois dans tout le jeu
        replique = self.repliques[nb_replique] #Donc la réplique est la phrase que le joueur à choisi
        #Il suffit de savoir quelle phrase le joueur a choisi pour réagir en conséquence

        #Premier dialogue
        #Le joueur arrive par la porte
        if replique == "Vous pouvez faire quelque chose pour moi ?":
            self.replique="Bien sûr ! Je suis marchand, et je peux vous proposer toutes sortes d'objets. Certains articles coûtent un peu cher, mais vu les circonstances, vous ne trouverez pas mieux"
            self.repliques = ["Je n'ai pas d'argent...","Intéressant... tu veux venir avec moi ?"]
        elif replique == "Je n'ai d'argent...":
            self.replique="Tu n'as qu'à me vendre ce dont tu ne te sers pas. Même les cadavres de monstre ont de la valeur." #/!\ Donner un peu de sous ?
            self.repliques = ["Ce serait embêtant de revenir ici à chaque fois que j'ai tué un monstre..."]
        elif replique == "Ce serait embêtant de revenir ici à chaque fois que j'ai tué un monstre...":
            self.replique="Je peux t'accompagner."
            self.repliques = ["Je veux bien.","Non merci."]
        elif replique == "Je veux bien.":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False
        elif replique == "Non merci.":
            self.end_dialogue(-2)
        elif replique == "Intéressant... tu veux venir avec moi ?":
            self.replique="Volontiers. Il n'y a pas beaucoup d'autres clients ici."
            self.repliques = [""]
        elif replique == "":
            self.end_dialogue()
            self.controleur.get_esprit(self.controleur.get_entitee(2).esprit).merge(self.esprit)
            self.mouvement = 0 #Légèrement redondant ici
            self.cible_deplacement = 2 #Le joueur a toujours l'ID 2 /!\
            self.attente = False

        self.replique_courante = 0

    def get_skin(self):
        return SKIN_MARCHAND

class Item(Entitee):
    """La classe des entitées inanimées. Peuvent se situer dans un inventaire. Peuvent être lancés (déconseillé pour les non-projectiles)."""
    def __init__(self,position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Pour avoir le droit de la ramasser.
        self.porteur = None
        self.lanceur = None
        self.direction = None #Utile uniquement quand l'item se déplace.
        self.latence = 0 #Utile uniquement quand l'item se déplace.
        self.vitesse = 1 #La quantitée soustraite à la latence chaque tour.
        self.taux_vitesse = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.poids = 10 #Utile uniquement quand l'item est lancé. Détermine le temps qu'il faut à l'agissant pour le lancer et le temps que l'item se déplacera.
        self.frottements = 10 #Utile uniquement quand l'item se déplace. Détermine la latence à chaque déplacement.
        self.hauteur = 0 #Utile uniquement quand l'item se déplace. Diminue à chaque tour. L'item s'immobilise à 0 (éventuellement déclenche des effets).
        self.nom = "item"

    def get_direction(self):
        if self.direction != None:
            return self.direction
        else:
            return HAUT

    def get_vitesse(self):
        vitesse = self.vitesse
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        return vitesse

    def heurte_agissant(self,agissant):
        for effet in self.effets :
            if isinstance(effet,On_hit) :
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,Percant) :
            self.ajoute_effet(En_sursis())
        elif isinstance(self,(Fragile,Evanescent)):
            self.etat = "brisé"
            self.arret()
        else :
            self.arret()

    def heurte_mur(self):
        for effet in self.effets :
            if isinstance(effet,On_hit):
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,(Fragile,Evanescent)):
            self.etat = "brisé"
            self.arret()
        else :
            self.arret()

    def atterit(self):
        for effet in self.effets :
            if isinstance(effet,On_hit) :
                effet.execute(self.lanceur,self.position,self.controleur)
        if isinstance(self,Evanescent):
            self.etat = "brisé"
            self.arret()
        else :
            self.arret()

    def arret(self):
        self.latence = 0
        if "lancementv" in self.taux_vitesse.keys():
            self.taux_vitesse.pop("lancementv")
        self.hauteur = 0

    #Découvrons le déroulé d'un tour, avec item-kun :
    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonne surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
        for effet in self.effets:
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()

    #Les agissants font leurs trucs, le controleur nous déplace, nous heurte (aïe !), tout le monde s'étripe...
    def vole(self):
        #On voooole (si on a été lancé)
        self.hauteur -= self.poids
        self.add_latence(self.frottements)
        if self.hauteur <= 0:
            self.atterit()

    def fin_tour(self):
        #C'est déjà fini ? Vivement le prochain !
        if self.hauteur > 0:
            self.latence -= self.get_vitesse()
        for effet in self.effets:
            if isinstance(effet,On_fin_tour):
                effet.execute(self) #À condition qu'il y ait un prochain...

class Cadavre(Item):

    def get_description(self,observation):
        return ["Un cadavre","Où as-tu trouvé ça ?"]

class Oeuf(Item):

    def get_description(self,observation):
        return ["Un oeuf","Je n'ai rien pour le cuire..."]

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,position,codes):
        Item.__init__(self,position)
        self.codes = codes

    def get_codes(self):
        return self.codes

    def get_classe(self):
        return Cle

    def get_description(self,observation):
        return ["Une clé","Je suppose qu'elle ouvre une porte."]

    def get_skin(self):
        return SKIN_CLE

class Consommable(Item):
    """La classe des items qui peuvent être consommés. Ajoute à l'agissant un effet. Disparait après usage."""
    def __init__(self,position,effet):
        Item.__init__(self,position)
        self.effet = effet

class Potion(Consommable):
    """La classe des consommables qui peuvent se boire."""
    def utilise(self,agissant):
        agissant.ajoute_effet(self.effet)
        self.etat = "brisé"

    def get_description(self,observation):
        return ["Une potion","Tu veux la boire ?"]

    def get_classe(self):
        return Potion

    def get_skin(self):
        return SKIN_POTION

class Potion_empoisonnee(Potion):
    """Une potion pas très bonne pour la santé."""
    def __init__(self,position):
        Potion.__init__(self,position,Poison(1,1,0.0101))

    def get_description(self,observation):
        return ["Une potion","Elle n'a pas l'air très apétissante..."]

    def get_skin(self):
        return SKIN_POTION_POISON

class Potion_antidote(Potion):
    """Une potion qui élimine les poisons."""
    def __init__(self,position):
        Potion.__init__(self,position,Antidote())

    def get_description(self,observation):
        return ["Une potion","Elle a probablement un effet bénéfique."]

class Potion_medicament(Potion):
    """Une potion qui élimine les maladies."""
    def __init__(self,position):
        Potion.__init__(self,position,Medicament())

    def get_description(self,observation):
        return ["Une potion","Elle a probablement un effet bénéfique."]

class Parchemin(Consommable):
    """La classe des consommables qui s'activent avec du mana."""
    def __init__(self,position,effet,cout):
        Item.__init__(self,position)
        self.effet = effet
        self.cout = cout

    def get_description(self,observation):
        return ["Un parchemin","C'est quoi ces gribouillis ?"]

    def utilise(self,agissant):
        if agissant.peut_payer(self.cout) :
            agissant.paye(self.cout)
            agissant.ajoute_effet(self.effet)
            self.etat = "brisé"
        elif isinstance(agissant,Joueur):
            agissant.affichage.message(Message(["Tu n'as pas assez de mana pour utiliser ce parchemin"]))

    def get_classe(self):
        return Parchemin

    def get_skin(self):
        return SKIN_PARCHEMIN

class Parchemin_purification(Parchemin):
    """Un parchemin qui soigne poisons et maladies."""
    def __init__(self,position):
        Parchemin.__init__(self,position,Purification(),50)

    def get_description(self,observation):
        return ["Un parchemin","Soignera poisons et maladies."]

class Poly_de_cours(Parchemin):
    """Un parchemin qui enseigne une magie."""
    def __init__(self,position,magie,cout):
        Parchemin.__init__(self,position,Enseignement(magie),cout)

    def get_description(self,observation):
        return["Un parchemin de cours","Probablement perdu par un élève.","D'après les tâches de sang, il fuyait un monstre."]

class Poly_soin(Poly_de_cours):
    """Un parchemin qui enseigne la magie de soin."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_soin,50)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI407 Soin'","Qu'est-ce que c'est ?"]

class Poly_auto_soin(Poly_de_cours):
    """Un parchemin qui enseigne la magie de soin."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_auto_soin,30)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI304 Soin'","Qu'est-ce que c'est ?"]

class Poly_soin_zone(Poly_de_cours):
    """Un parchemin qui enseigne la magie de soin."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_soin_de_zone,75)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI507 Soin'","Qu'est-ce que c'est ?"]

class Poly_resurection(Poly_de_cours):
    """Un parchemin qui enseigne la magie de résurection."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_resurection,200)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI928 Résurection'","Qu'est-ce que c'est ?"]

class Poly_reanimation(Poly_de_cours):
    """Un parchemin qui enseigne la magie de réanimation de masse."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_reanimation_de_zone,199)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'BANI666 Réanimation'","Qu'est-ce que c'est ?"]

class Poly_boule_de_feu(Poly_de_cours):
    """Un parchemin qui enseigne la magie de boule de feu."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_boule_de_feu,80)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'FEU201 Boule de feu'","Qu'est-ce que c'est ?"]

class Poly_fleche_de_glace(Poly_de_cours):
    """Un parchemin qui enseigne la magie de flèche de glace."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_fleche_de_glace,85)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'GLAC201 Flèche de glace'","Qu'est-ce que c'est ?"]

class Poly_rocher(Poly_de_cours):
    """Un parchemin qui enseigne la magie de rocher."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_rocher,75)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'TERR201 Rocher'","Qu'est-ce que c'est ?"]

class Poly_ombre_furtive(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'ombre furtive."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_ombre_furtive,70)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'OMBR201 Ombre furtive'","Qu'est-ce que c'est ?"]

class Poly_jet_de_mana(Poly_de_cours):
    """Un parchemin qui enseigne la magie de jet de mana."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_jet_de_mana,100)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI303 Jet de mana'","Qu'est-ce que c'est ?"]

class Poly_eclair_noir(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'éclair noir."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_eclair_noir,300)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI902 Eclair noir'","Qu'est-ce que c'est ?"]

class Poly_faiblesse(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de faiblesse."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_faiblesse,20)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH101 Faiblesse'","Qu'est-ce que c'est ?"]

class Poly_cecite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de cécité."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_cecite,30)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH201 Cécité'","Qu'est-ce que c'est ?"]

class Poly_perte_de_pv(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de perte de pv."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_perte_de_pv,40)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH301 Perte de pv'","Qu'est-ce que c'est ?"]

class Poly_perte_de_pm(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de perte de pm."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_perte_de_pm,50)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH401 Perte de pm'","Qu'est-ce que c'est ?"]

class Poly_poches_trouees(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de poches trouées."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_poches_trouees,60)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH501 Poches trouées'","Qu'est-ce que c'est ?"]

class Poly_confusion(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de confusion."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_confusion,70)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH601 Confusion'","Qu'est-ce que c'est ?"]

class Poly_force(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de force."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_force,20)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH102 Force'","Qu'est-ce que c'est ?"]

class Poly_vision(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de vision."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_vision,30)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH202 Vision'","Qu'est-ce que c'est ?"]

class Poly_absorption(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement d'absorption."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_absorption,40)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH302 Absorption'","Qu'est-ce que c'est ?"]

class Poly_vitalite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de vitalité."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_vitalite,50)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH402 Vitalité'","Qu'est-ce que c'est ?"]

class Poly_celerite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de célérité."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_celerite,60)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH502 Célérité'","Qu'est-ce que c'est ?"]

class Poly_immunite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement d'immunite."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_immunite,70)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH602 Immunité'","Qu'est-ce que c'est ?"]

class Poly_flamme(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de flamme."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_flamme,40)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'FEU301 Flamme'","Qu'est-ce que c'est ?"]

class Poly_neige(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de neige."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_neige,40)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'GLAC301 Neige'","Qu'est-ce que c'est ?"]

class Poly_sable(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de sable."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_sable,40)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'TERR301 Sable'","Qu'est-ce que c'est ?"]

class Poly_tenebre(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de ténèbre."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_tenebre,40)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'OMBR301 Ténèbres'","Qu'est-ce que c'est ?"]

class Poly_rouille(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de rouille."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_rouille,70)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH203 Rouille'","Qu'est-ce que c'est ?"]

class Poly_renforcement(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de renforcement."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_renforcement,90)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH303 Renforcement'","Qu'est-ce que c'est ?"]

class Poly_bombe(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de  bombe."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_enchantement_bombe,60)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ENCH103 Bombe'","Qu'est-ce que c'est ?"]

class Poly_reserve(Poly_de_cours):
    """Un parchemin qui enseigne la magie de reserve."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_reserve,100)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ECON501 Reserve'","Qu'est-ce que c'est ?"]

class Poly_investissement(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'investissement."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_investissement,95)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'ECON502 Investissement'","Qu'est-ce que c'est ?"]

class Poly_explosion_de_mana(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'explosion de mana."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_explosion_de_mana,100)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI512 Explosion de mana'","Qu'est-ce que c'est ?"]

class Poly_laser(Poly_de_cours):
    """Un parchemin qui enseigne la magie de laser."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_laser,50)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI407 Laser'","Qu'est-ce que c'est ?"]

class Poly_brasier(Poly_de_cours):
    """Un parchemin qui enseigne la magie de brasier."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_brasier,60)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'FEU401 Brasier'","Qu'est-ce que c'est ?"]

class Poly_avalanche(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'avalanche."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_avalanche,60)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'TERR401 Avalanche'","Qu'est-ce que c'est ?"]

class Poly_blizzard(Poly_de_cours):
    """Un parchemin qui enseigne la magie de blizzard."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_blizzard,65)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'GLAC501 Blizzard'","Qu'est-ce que c'est ?"]

class Poly_obscurite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'obscurité."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_obscurite,65)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'OMBR501 Obscurité'","Qu'est-ce que c'est ?"]

class Poly_dopage(Poly_de_cours):
    """Un parchemin qui enseigne la magie de dopage."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_dopage,30)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'MAGI201 Dopage'","Qu'est-ce que c'est ?"]

class Poly_instakill(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'instakill."""
    def __init__(self,position):
        Poly_de_cours.__init__(self,position,Magie_instakill,120)

    def get_description(self,observation):
        return["Un parchemin de cours","Intitulé : 'BANI807 Instakill'","Qu'est-ce que c'est ?"]

class Equipement(Item):
    """La classe des items qui peuvent être portés. Sont toujours actifs tant qu'ils sont portés."""
    pass

class Defensif(Equipement):
    """La classe des équipements défensifs. Réduit les dégats."""
    def __init__(self,position,taux_degats):
        Item.__init__(self,position)
        self.taux_degats = taux_degats
        self.taux_stats = {}

    def intercepte(self,attaque):
        for taux in self.taux_stats.values():
            attaque.degats *= taux
        attaque.degats *= self.taux_degats

class Regeneration_pm(Equipement):
    """La classe des équipements régénérateurs de mana. Augmentent les pm récupérés à chaque tour."""
    def __init__(self,position,taux_regen_pm):
        Item.__init__(self,position)
        self.taux_regen_pm = taux_regen_pm

    def get_taux(self):
        return self.taux_regen_pm

class Regeneration_pv(Equipement):
    """La classe des équipements régénérateurs de vie. Augmentent les pv récupérés à chaque tour."""
    def __init__(self,position,taux_regen_pv):
        Item.__init__(self,position)
        self.taux_regen_pv = taux_regen_pv

    def get_taux(self):
        return self.taux_regen_pv

class Armure(Equipement):
    """La classe des équipements défensifs de type armure. On ne peut en porter qu'une à la fois. Réduit les dégats."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.poids = 10 #C'est lourd !
        self.frottements = 8 #Il y a pire.

    def get_classe(self):
        return Armure

    def get_description(self,observation):
        return ["Une armure","Essaye de l'enfiler !"]

    def get_skin(self):
        return SKIN_ARMURE

class Armure_type(Armure,Defensif):
    """Une armure type : défend contre les attaques."""
    def __init__(self,position,taux_degats):
        Armure.__init__(self,position)
        Defensif.__init__(self,position,taux_degats)

class Haume(Equipement):
    """La classe des équipements défensifs de type haume. On ne peut en porter qu'un à la fois. Réduit les dégats."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.poids = 3 #C'est plutôt léger.
        self.frottements = 6

    def get_classe(self):
        return Haume

    def get_description(self,observation):
        return ["Un haume","..."]

    def get_skin(self):
        return SKIN_CASQUE

class Haume_type(Haume,Defensif):
    """Un haume type : défend contre les attaques."""
    def __init__(self,position,taux_degats):
        Haume.__init__(self,position)
        Defensif.__init__(self,position,taux_degats)

class Anneau(Equipement):
    """La classe des équipements de type anneau. Le nombre d'anneaux qu'on peut porter dépend de l'espèce. Les anneaux peuvent avoir des effets très différends (magiques pour la plupart)."""
    def __init__(self,position):
        Item.__init__(self,position)
        self.poids = 1 #C'est très léger !
        self.frottement = 2 #Il y a mieux.

    def get_description(self,observation):
        return ["Un anneau","Tu peux en porter plusieurs."]

    def get_classe(self):
        return Anneau

    def get_skin(self):
        return SKIN_ANNEAU

class Anneau_magique(Anneau,Regeneration_pm):
    """Un anneau magique : augmente la régénération des pm."""
    def __init__(self,position,taux_regen):
        Anneau.__init__(self,position)
        Regeneration_pm.__init__(self,position,taux_regen)

class Anneau_de_vitalite(Anneau,Regeneration_pv):
    """Un anneau un peu moins magique : augmente la régénération des pv."""
    def __init__(self,position,taux_regen):
        Anneau.__init__(self,position)
        Regeneration_pv.__init__(self,position,taux_regen)

class Degainable(Item):
    """La classe des items qui doivent être dégainés. Sont utilisés en complément d'un skill, n'ont pas d'effet le reste du temps."""
    pass

class Arme(Degainable):
    """La classe des équipements qui augmentent la force d'attaque."""
    def __init__(self,position,element,tranchant,portee):
        Item.__init__(self,position)
        self.element = element
        self.tranchant = tranchant
        self.taux_tranchant = {}
        self.portee = portee
        self.taux_portee = {}
        self.taux_stats = {}

    def get_stats_attaque(self):
        tranchant = self.tranchant
        for taux in self.taux_tranchant.values():
            tranchant *= taux
        portee = self.portee
        for taux in self.taux_portee.values():
            portee *= taux
        for taux in self.taux_stats.values():
            tranchant *= taux
            portee *= taux
        return self.element,tranchant,portee

    def get_classe(self):
        return Arme

class Epee(Arme):
    """La classe des armes de type épée. Permettent de porter des coups semi-circulaires devant l'agissant."""
    def __init__(self,position,element,tranchant,portee):
        Arme.__init__(self,position,element,tranchant,portee)
        self.poids = 5
        self.frottements = 4

    def get_description(self,observation):
        return ["Une épée","Pour couper le saucisson."]

    def get_skin(self):
        return SKIN_EPEE

class Lance(Arme):
    """La classe des armes de type lance. Permettent de porter des coups rectilignes devant l'agissant."""
    def __init__(self,position,element,tranchant,portee):
        Arme.__init__(self,position,element,tranchant,portee)
        self.poids = 3
        self.frottements = 3

    def get_description(self,observation):
        return ["Une lance","Pour faire des trous dans les gens."]

    def get_skin(self):
        return SKIN_LANCE

class Bouclier(Degainable):
    """La classe des boucliers. Permettent de se protéger des attaques lorsqu'ils sont utilisés."""
    def __init__(self,position,degats_bloques,taux_degats):
        Item.__init__(self,position)
        self.degats_bloques = degats_bloques
        self.taux_degats = taux_degats
        self.taux_stats = {}
        self.poids = 5
        self.frottements = 1 #En mode frisbee ça volle très bien !

    def intercepte(self,attaque):
        attaque.degats -= self.degats_bloques
        if attaque.degats < 0:
            attaque.degats = 0
        else :
            for taux in taux_stats.values():
                attaque.degats *=  taux
            attaque.degats *= self.taux_degats

    def get_classe(self):
        return Bouclier

    def get_description(self,observation):
        return ["Un frisbee","Ah non, c'est un bouclier !"]

    def get_skin(self):
        return SKIN_BOUCLIER

class Projectile(Item):
    """La classe des items destinés à être lancés. Possèdent naturellement une vitesse non nulle."""
    def __init__(self,position,vitesse,effets):
        Item.__init__(self,position)
        self.vitesse = vitesse
        self.effets = effets #Les effets déclenché lors du choc avec un agissant.

    def get_classe(self):
        return Projectile

class Explosif(Projectile):
    """La classe des projectiles qui explosent. Affectés différemment par certains skills."""
    def get_skin(self):
        if self.hauteur > 0:
            return SKIN_EXPLOSIF
        else:
            return SKIN_EXPLOSE

class Charge_de_base(Explosif):
    """L'explosif le plus basique qui soit. Plutôt commun, accessible dès le niveau 1 du skill de création d'explosifs. À manipuler avec précaution, risque d'antagonisation involontaire."""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_charge_de_base[niveau-1]
        self.taux_vitesse = {}
        self.poids = 4
        self.frottements = 3
        self.hauteur = 0
        self.effets = [On_hit(portee_charge_de_base[niveau-1],degats_charge_de_base[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Charge_lourde(Explosif):
    """Un explosif puissant, mais de portée réduite."""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_charge_lourde[niveau-1]
        self.taux_vitesse = {}
        self.poids = 7
        self.frottements = 4
        self.hauteur = 0
        self.effets = [On_hit(portee_charge_lourde[niveau-1],degats_charge_lourde[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Charge_etendue(Explosif):
    """Un explosif faible, mais de portée importante."""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_charge_etendue[niveau-1]
        self.taux_vitesse = {}
        self.poids = 3
        self.frottements = 2
        self.hauteur = 0
        self.effets = [On_hit(portee_charge_etendue[niveau-1],degats_charge_etendue[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Percant(Projectile):
    """La classe des projectiles qui peuvent transpercer un ennemi."""
    pass

class Fleche(Percant):
    """La classe des projectiles de type flèche. Affectés différemment par certains skills."""
    def get_skin(self):
        return SKIN_FLECHE

class Fleche_de_base(Fleche):
    """La flèche la plus basique qui soit. La plus commune dans le labyrinthe, accessible dès le niveau 1 du skill de création de flèches."""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_de_base[niveau-1]
        self.taux_vitesse = {}
        self.poids = 1
        self.frottements = 2 #C'est plutôt rapide.
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_de_base[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_fantome(Fleche,Fantome):
    """Une flèche qui peut traverser les murs. Est-ce l'âme d'une flèche décédée ?"""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_fantome[niveau-1]
        self.taux_vitesse = {}
        self.poids = 1
        self.frottements = 2
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_fantome[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_lourde(Fleche):
    """Une flèche lourde. Elle va moins loin et un peu moins vite, mais rien que de bonnes stats ne puissent compenser. Et elle est dévastatrice !"""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_lourde[niveau-1]
        self.taux_vitesse = {}
        self.poids = 5 #C'est déjà mieux que certains... non-projectiles, je suppose ?
        self.frottements = 1
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_lourde[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_legere(Fleche):
    """Une flèche légère. Rapidité inégalée, portée incomparable... mais pas beaucoup de dégats, évidemment."""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_legere[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0.5
        self.frottements = 0.5 #Faire de toutes ces stats des constantes dépendant du niveau, aussi ?
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_legere[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_explosive(Fleche,Explosif):
    """Une flèche explosive. C'est une flèche ou un explosif ? Mieux vaut rester loin en tous cas..."""
    def __init__(self,niveau,position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_explosive[niveau-1]
        self.taux_vitesse = {}
        self.poids = 3
        self.frottements = 2 
        self.hauteur = 0
        self.effets = [On_hit(portee_fleche_explosive[niveau-1],degats_fleche_explosive[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Perce_armure(Item):
    """La classe des items qui peuvent infliger des dégats sans être affectés par les défenses comme l'armure ou le bouclier."""

class Fragile(Item):
    """La classe des items qui se brisent lors d'un choc."""
    pass

class Evanescent(Item):
    """La classe des items qui disparaissent s'ils ne sont pas en mouvement (les sorts de projectiles, par exemple, qui sont des items...)."""
    pass

class Projectile_magique(Projectile,Evanescent):
    """La classe des projectiles créés par magie."""
    pass

class Magie_explosive(Explosif,Projectile_magique):
    """La classe des projectiles explosifs créés par magie."""
    pass

class Fleche_magique(Fleche,Projectile_magique):
    """La classe des flèches créées par magie."""
    pass

class Perce_armure_magique(Perce_armure,Projectile_magique):
    """La classe des projectiles perce_armures créés par magie."""
    pass

class Magie_explosive_percante(Magie_explosive,Percant):
    """La classe des projectiles explosifs perçant créés par magie."""
    pass

class Boule_de_feu(Magie_explosive):
    """Les projectiles crées par le sort de boule de feu."""
    def __init__(self,niveau,position,direction,lanceur):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #On s'en fout, on ne peut pas ramasser une boule de feu...
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_boule_de_feu[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1 #Une boule de feu ne peut pas être au sol...
        self.effets = [On_hit(portee_boule_de_feu[niveau-1],degats_boule_de_feu[niveau-1],FEU)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_BOULE_DE_FEU

### Créer un parchemin d'invocation de boule de feu !

class Fleche_de_glace(Fleche_magique):
    """Les projectiles crées par le sort de fleche de glace."""
    def __init__(self,niveau,position,direction,lanceur):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Est-ce qu'on peut ramasser les fleches de glace ?
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_fleche_de_glace[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_fleche_de_glace[niveau-1],GLACE)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_FLECHE_DE_GLACE

### Créer un parchemin d'invocation de fleche de glace !

class Rocher(Projectile_magique):
    """Les projectiles crées par le sort de rocher."""
    def __init__(self,niveau,position,direction,lanceur):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_rocher[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_rocher[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_ROCHER

### Créer un parchemin d'invocation de rocher !

class Ombre_furtive(Perce_armure_magique):
    """Les projectiles crées par le sort d'ombre_furtive."""
    def __init__(self,niveau,position,direction,lanceur):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #On s'en fout, on ne peut pas ramasser une ombre...
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_ombre_furtive[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1 #Une ombre ne peut pas être au sol... si ?
        self.effets = [On_hit(1,degats_ombre_furtive[niveau-1],OMBRE)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_OMBRE_FURTIVE

### Pas de parchemins pour les magies noires (enfin pour les apprendre, si (et encore), mais pour les lancer, non)...

class Jet_de_mana(Projectile_magique):
    """Les projectiles crées par le sort de jet de mana."""
    def __init__(self,niveau,position,direction,lanceur):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_jet_de_mana[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_jet_de_mana[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    ### Lui créer un get_skin !

class Eclair_noir(Magie_explosive_percante):
    """Les projectiles crées par le sort d'éclair noir."""
    def __init__(self,niveau,position,direction,lanceur):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_eclair_noir[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_choc_eclair_noir[niveau-1]),On_hit(portee_eclair_noir[niveau-1],degats_explosifs_eclair_noir[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    ### Lui créer un get_skin !

class Cree_item:
    """La classe des créateurs d'item."""
    def __init__(self,classe_item = Item):
        self.item = classe_item

class Cree_fleche_de_base_skill(Cree_item):
    """La classe des créateurs de fleche de base, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_de_base
        self.nom = "Flèche de base"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_FLECHE_DE_BASE

class Cree_fleche_percante_skill(Cree_item):
    """La classe des créateurs de fleche percante, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_de_base #Pour l'instant les flèches perçantes n'existent pas
        self.nom = "Flèche percante"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_FLECHE_DE_BASE

class Cree_fleche_fantome_skill(Cree_item):
    """La classe des créateurs de fleche fantome, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_fantome
        self.nom = "Flèche fantome"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_FLECHE_FANTOME

class Cree_fleche_lourde_skill(Cree_item):
    """La classe des créateurs de fleche lourde, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_lourde
        self.nom = "Flèche lourde"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_FLECHE_LOURDE

class Cree_fleche_legere_skill(Cree_item):
    """La classe des créateurs de fleche legere, associé au skill de création de fleche."""
    def __init__(self):
        self.item = Fleche_legere
        self.nom = "Flèche legere"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_FLECHE_LEGERE

class Cree_fleche_explosive_skill(Cree_item):
    """La classe des créateurs de fleche lourde, associé au skill de création de fleche ou d'explosif."""
    def __init__(self):
        self.item = Fleche_explosive
        self.nom = "Flèche explosive"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill_fleche = trouve_skill(agissant.classe_principale,Skill_creation_de_fleches)
        skill_explosif = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill_fleche == skill_explosif == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        elif skill_fleche != None:
            if skill_explosif != None:
                if skill_fleche.niveau > skill_explosif.niveau :
                    niveau = skill_fleche.utilise(0.01) #L'xp gagné. En faire un variable /!\
                    item = self.item(niveau,None)
                    agissant.controleur.ajoute_entitee(item)
                else:
                    niveau = skill_explosif.utilise(0.01) #L'xp gagné. En faire un variable /!\
                    item = self.item(niveau,None)
                    agissant.controleur.ajoute_entitee(item)
            else:
                niveau = skill_fleche.utilise(0.01) #L'xp gagné. En faire un variable /!\
                item = self.item(niveau,None)
                agissant.controleur.ajoute_entitee(item)
        else:
            niveau = skill_explosif.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_FLECHE_EXPLOSIVE

class Cree_charge_de_base_skill(Cree_item):
    """La classe des créateurs de charge lourde, associé au skill de création d'explosif."""
    def __init__(self):
        self.item = Charge_de_base
        self.nom = "Charge de base"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_CHARGE_DE_BASE

class Cree_charge_lourde_skill(Cree_item):
    """La classe des créateurs de charge lourde, associé au skill de création d'explosif."""
    def __init__(self):
        self.item = Charge_lourde
        self.nom = "Charge lourde"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_CHARGE_LOURDE

class Cree_charge_etendue_skill(Cree_item):
    """La classe des créateurs de charge étendue, associé au skill de création d'explosif."""
    def __init__(self):
        self.item = Charge_etendue
        self.nom = "Charge etendue"

    def cree_item(self,agissant): #On ne lui donne que la classe principale, et il se débrouille pour trouver le skill
        skill = trouve_skill(agissant.classe_principale,Skill_creation_d_explosifs)
        if skill == None:
            print("Euh... Quoi ? Qu'est-ce qui m'est arrivé ?")
            item = None
        else:
            niveau = skill.utilise(0.01) #L'xp gagné. En faire un variable /!\
            item = self.item(niveau,None)
            agissant.controleur.ajoute_entitee(item)
        return item

    def get_skin(self):
        return SKIN_CREE_CHARGE_ETENDUE

class Inventaire:

    def __init__(self,ID_possesseur,nb_doigts):
        self.possesseur = ID_possesseur #On classe les possessions d'un agissant selon les usages qu'il peut en faire :
        self.items = {Potion:[], #Une potion peut se boire
                      Parchemin:[], #Un parchemin peut s'activer avec du mana
                      Cle:[], #Les clés ouvrent les portes
                      Arme:[], #Les armes s'équippent et sont utilisées pour attaquer
                      Bouclier:[], #Les boucliers s'équippent et sont utilisés pour se défendre
                      Armure:[], #Les armures s'équippent et ont des effets passifs
                      Haume:[], #Les haumes s'équippent et ont des effets passifs
                      Anneau:[], #Les anneaux s'équippent et ont des effets passifs
                      Projectile:[], #Les projectiles se lancent (on peut lancer n'importe quoi, techniquement...)
                      Cadavre:[], #Oui, on peut récupérer des cadavres, et alors, circluez, ya rien à voir...
                      Oeuf:[] #Vous allez quand même pas me dire que c'est l'oeuf qui vous choque ! Il y a marqué cadavre juste au dessus !
                      }
        self.kiiz = [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile,Cadavre,Oeuf]
        self.arme = None #L'arme équipée
        self.bouclier = None #Le bouclier équipé
        self.armure = None #L'armure équipée
        self.haume = None #Le haume équipé
        self.anneau = [None]*nb_doigts #Les anneaux équipés
        self.cat_courante = 0
        self.item_courant = 0
        self.profondeur = 0
        self.controleur = None

    def active(self,controleur):
        self.controleur = controleur
        for key in self.items.keys():
            for item in self.items[key]:
                controleur.get_entitee(item).active(controleur)

    def desactive(self):
        for key in self.items.keys():
            for item in self.items[key]:
                self.controleur.get_entitee(item).desactive()
        self.controleur = None
        
    def ramasse_item(self,ID_item):
        """
        Fonction qui gère le ramassage d'un item
        Entrée:
            -l'ID de l'item à ramasser
        """
        item = self.controleur.get_entitee(ID_item)
        item.position = None
        self.items[item.get_classe()].append(ID_item)

    def ajoute(self,item):
        #Comme la précédente, mais c'est l'item et non son ID qui est passé en paramètre
        item.position = None
        self.items[item.get_classe()].append(item.ID)

    def utilise_item(self,agissant):
        """
        Fonction qui utilise l'item actuellement sélectionné dans l'inventaire
        En sortie : Rien
        """
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,consommable):
            item.utilise(agissant)

    def utilise_courant(self,proprietaire):
        """Appelé en appuyant sur la touche espace, utilise l'item actuellement sélectionné."""
        ###L'utilisation varie beaucoup selon le type d'item :
        
        ID_item = self.get_item_courant()
        if ID_item != None:
            item = self.controleur.get_entitee(ID_item)
            if isinstance(item,Consommable): #Un consommable se consomme (si c'est un parchemin, l'activation peut échouer)
                item.utilise(proprietaire)
            elif isinstance(item,Arme): #Un équipable s'équipe. Il y a certaines conditions.
                self.set_arme()
            elif isinstance(item,Bouclier):
                self.set_bouclier()
            elif isinstance(item,Armure):
                self.set_armure()
            elif isinstance(item,Haume):
                self.set_haume()
            elif isinstance(item,Anneau):
                self.set_anneau()

    def get_items_visibles(self):
        items_visibles = []
        if self.arme != None:
            items_visibles.append(self.arme)
        if self.bouclier != None:
            items_visibles.append(self.bouclier)
        if self.armure != None:
            items_visibles.append(self.armure)
        if self.haume != None:
            items_visibles.append(self.haume)
        return items_visibles

    def get_arme(self):
        return self.arme

    def set_arme(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Arme):
            self.arme = ID_item

    def get_bouclier(self):
        return self.bouclier

    def set_bouclier(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Bouclier):
            self.bouclier = ID_item

    def get_armure(self):
        return self.armure

    def set_armure(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Armure):
            self.armure = ID_item

    def get_haume(self):
        return self.haume

    def set_haume(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Haume):
            self.haume = ID_item

    def get_anneau(self):
        return self.anneau

    def set_anneau(self):
        ID_item = self.get_item_courant()
        item = self.controleur.get_entitee(ID_item)
        if isinstance(item,Anneau):
            if ID_item in self.anneau:
                self.anneau.remove(ID_item)
                self.anneau.append(None)
            else :
                for i in range(len(self.anneau)-1,0,-1):
                    self.anneau[i]=self.anneau[i-1]
                self.anneau[0]=ID_item

    def get_equippement(self):
        equippement = []
        if self.arme != None:
            equippement.append(self.arme)
        if self.bouclier != None:
            equippement.append(self.bouclier)
        if self.armure != None:
            equippement.append(self.armure)
        if self.haume != None:
            equippement.append(self.haume)
        for anneau in self.anneau:
            if anneau != None:
                equippement.append(anneau)
        return equippement

    def equippe(self,equippement):
        for item in equippement:
            ID = item.ID
            if isinstance(item,Arme):
                if not ID in self.items[Arme]:
                    self.items[Arme].append(ID)
                self.arme = ID
            elif isinstance(item,Bouclier):
                if not ID in self.items[Bouclier]:
                    self.items[Bouclier].append(ID)
                self.arme = ID
            elif isinstance(item,Armure):
                if not ID in self.items[Armure]:
                    self.items[Armure].append(ID)
                self.arme = ID
            elif isinstance(item,Anneau):
                if not ID in self.items[Anneau]:
                    self.items[Anneau].append(ID)
                if not ID in self.anneau:
                    for i in range(len(self.anneau)-1,0,-1):
                        self.anneau[i]=self.anneau[i-1]
                    self.anneau[0]=ID

    def get_clees(self):
        clees = []
        for ID_cle in self.items[Cle]:
            cle = self.controleur.get_entitee(ID_cle)
            for code in cle.codes:
                clees.append(code)
        return clees

    def get_clee(self,code):
        cle = None
        for ID_cle in self.items[Cle]:
            if code in self.controleur.get_entitee(ID_cle).codes:
                clee = ID_cle
        return cle

    def get_items(self):
        items = []
        for kii in self.kiiz:
            for ID in self.items[kii]:
                items.append(self.controleur.get_entitee(ID))
        return items

    def get_item_courant(self):
        cat = self.items[self.kiiz[self.cat_courante]]
        if self.item_courant < len(cat):
            item_courant = cat[self.item_courant]
        else:
            item_courant = None
        return item_courant

    def nettoie_item(self): #Méthode appelée à chaque fin de tour pour supprimer les items retirés ou utilisés.
        for cat in range(10): #On parcourt les catégories
            items = self.items[self.kiiz[cat]]
            for nb_item in range(len(items)-1,-1,-1): #On parcourt les items
                ID_item = items[nb_item]
                item = self.controleur.get_entitee(ID_item)
                if item.position != None or item.etat == "brisé": #S'il a été lancé ou n'est plus en état
                    items.remove(ID_item)

                    if cat == self.cat_courante :
                        if nb_item < self.item_courant or nb_item == len(items) == self.item_courant :
                            self.item_courant -= 1 #On gère d'éventuels problèmes de selection

                    if self.arme == ID_item :
                        self.arme = None
                    elif self.bouclier == ID_item :
                        self.bouclier = None
                    elif self.armure == ID_item :
                        self.armure = None
                    elif self.haume == ID_item :
                        self.haume = None
                    else :
                        for doigt in range(len(self.anneau)):
                            if self.anneau[doigt] == ID_item :
                                self.anneau[doigt] = None #Quel genre d'imbécile briserait ou lancerait son équippement ? Enfin...

        if 0 == len(self.items[Potion]) == len(self.items[Parchemin]) == len(self.items[Cle]) == len(self.items[Arme]) == len(self.items[Bouclier]) == len(self.items[Armure]) == len(self.items[Haume]) == len(self.items[Anneau]) == len(self.items[Projectile]) == len(self.items[Cadavre]) == len(self.items[Oeuf]) : #Sérieusement, l'inventaire est vide ?!
            self.cat_courante = 0
            self.item_courant = 0
        else :
            while len(self.items[self.kiiz[self.cat_courante]]) == 0: #On a au moins une catégorie non vide.
                self.cat_courante = (self.cat_courante + 1) % 10
            if self.item_courant == -1 : #Ce devrait être le cas si on est passé dans la boucle précédente, et ce n'est pas très souhaitable...
                self.item_courant = 0
                self.profondeur = 0

    def deplace(self,direction):
        res = False
        if direction == IN and self.profondeur <= 1:
            self.profondeur += 1
        elif direction == OUT:
            if self.profondeur == 0:
                res = True
            else:
                self.profondeur -=1
        elif direction == BAS:
            if self.profondeur == 0:
                self.cat_courante += 1
                if self.cat_courante >= 10:
                    self.cat_courante = 0
                self.item_courant = 0
            elif self.profondeur == 1:
                self.item_courant += 1
                if self.item_courant >= len(self.items[self.kiiz[self.cat_courante]]):
                    self.item_courant = 0
        elif direction == HAUT:
            if self.profondeur == 0:
                self.cat_courante -= 1
                if self.cat_courante < 0:
                    self.cat_courante = 9
                self.item_courant = 0
            elif self.profondeur == 1:
                self.item_courant -= 1
                if self.item_courant < 0:
                    self.item_courant = len(self.items[self.kiiz[self.cat_courante]])-1
        return res

    def drop_all(self,position):
        items = []
        for cat_item in self.kiiz : #On drop aussi les cadavres et les oeufs
            items += self.items[cat_item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.position = position

    def drop(self,position):
        cat = self.items[self.kiiz[self.cat_courante]]
        if cat != []:
            ID_item = cat[self.item_courant]
            item = self.controleur.get_entitee(ID_item)
            item.position = position

    def debut_tour(self):
        items = []
        for cat_item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile] : #On sépare les 'vrais' items des faux.
            items += self.items[cat_item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.debut_tour()
        #On ne manipule pas les cadavres
        for ID_oeuf in self.items[Oeuf]: #Mais les oeufs incubent !
            oeuf = self.controleur.get_entitee(ID_oeuf)
            hatch = trouve_skill(oeuf.classe_principale,Hatching)
            if hatch != None:
                if hatch.utilise(): #Et peuvent même éclore !
                    self.controleur.fait_eclore(oeuf,self.possesseur)

    def fin_tour(self):
        items = []
        for item in [Potion,Parchemin,Cle,Arme,Bouclier,Armure,Haume,Anneau,Projectile] : #On sépare les 'vrais' items des faux.
            items += self.items[item]
        for ID_item in items :
            item = self.controleur.get_entitee(ID_item)
            item.fin_tour() #Moins de choses à faire à la fin du tour.
        self.nettoie_item()

class Esprit :
    """La classe des esprits, qui manipulent les agisants."""
    def __init__(self,nom): #On identifie les esprits par des noms (en fait on s'en fout, vu qu'on ne fait pas d'opérations dessus on pourrait avoir des labs, des entitees et des esprits nommés avec des str, des int, des float, des bool, etc.)
        self.corps = {}
        self.vue = {}
        self.ennemis = {}
        self.oubli = 1
        self.nom = nom
        self.controleur = None

    def ajoute_corp(self,corp):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            self.controleur.get_entitee(corp).rejoint(self.nom)

    def ajoute_corps(self,corps):
        for corp in corps:
            self.ajoute_corp(corp)

    def retire_corp(self,corp):
        if corp in self.corps:
            self.corps.pop(corp)

    def retire_corps(self,corps):
        for corp in corps:
            self.retire_corp(corp)

    def get_corps(self):
        corps = []
        for corp in self.corps.keys():
            corps.append(corp)
        return corps

    def ajoute_vue(self,vue,niveau):
        self.vue[niveau] = vue

    def maj_vue(self,vue,niveau):
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                case = vue[i][j]
                if case[1] > 0: #Si la clarté est positive
                    self.vue[niveau][i][j] = case #On remplace par la dernière version de la vision

    def trouve_agissants(self,vue):
        agissants = []
        for i in range(len(vue)):
            for j in range(len(vue[0])):
                case = vue[i][j]
                agissants += case[8]
        return agissants

    def oublie_agissants(self,agissants):
        for vue in self.vue.values():
            for i in range(len(vue)):
                for j in range(len(vue[0])):
                    case = vue[i][j]
                    for ID in agissants:
                        if ID in case[8]:
                            case[8].remove(ID)

    def ordonne_bourrin(self,agissant):
        #Il faudra identifier les comportements possibles des agissants : attaque bourrine, attaque à distance, support (renforcement), soin, fuite, recherche et autres (réanimation pour les nécromantiens par exemple)
        #Pour l'instant juste des bourrins.
        position = agissant.get_position()
        case = self.vue[position[0]][position[1]][position[2]] #On récupère le labyrinthe
        cases = []
        dirs = []
        importance = 0
        for i in range(4):
            if case[7][i]:
                if case[7][i][0] in self.vue.keys():
                    case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                    entitees = case_pot[8]
                    libre = True
                    for ID_entitee in entitees:
                        entitee = agissant.controleur.get_entitee(ID_entitee)
                        if not issubclass(entitee.get_classe(),Item): #Un agissant !
                            if case[7][i][0] == position[0] and ID_entitee in self.ennemis.keys(): #Un ennemi ! Et au bon étage
                                if self.ennemis[ID_entitee] > importance:
                                    importance = self.ennemis[ID_entitee]
                                    agissant.attaque(i)
                            else: #Probablement un allié, ou un neutre, ou à un autre étage (cette configuration autorise les tentatives d'attaques au travers des portails de même niveau)
                                libre = False
                    if libre:
                        cases.append(case_pot)
                        dirs.append(i)

        if importance == 0: #On n'a pas d'ennemi à portée

            if len(cases) == 0: #Pas de cases libres à proximité
                agissant.skill_courant = None

            else :
            
                dir_choix = 2
                num_choix = 0
                distance = case[3]

                for i in range(len(cases)):
                    if cases[i][3] > distance or (cases[i][3] == distance and cases[i][4] >= cases[num_choix][4]):
                        distance = cases[i][3]
                        dir_choix = dirs[i]
                        num_choix = i

                if distance == 0 : #Pas d'accès direct à une cible

                    distance = case[4]
                    meilleur_choix = False
                    agissant.skill_courant = None #Dans l'éventualité où on est déjà sur la meilleure case

                    for i in range(len(cases)):
                        if cases[i][4] > distance:
                            meilleur_choix = True
                            distance = cases[i][4] #On prend le chemin avec des obstacles
                            dir_choix = dirs[i]

                    if meilleur_choix:
                        agissant.va(dir_choix)

                    if distance == 0: #Pas d'accès du tout !
                        if not isinstance(agissant,Sentinelle): #Les sentinelles ne cherchent pas
                            if len(dirs)>1: #On peut se permettre de choisir
                                if agissant.dir_regard != None: #L'agissant regarde quelque part
                                    dir_back = [HAUT,DROITE,BAS,GAUCHE][agissant.dir_regard-2]
                                    if dir_back in dirs: #On ne veut pas y retourner
                                        dirs.remove(dir_back)
                            agissant.va(dirs[random.randint(0,len(dirs)-1)]) #On prend une direction random
                            # ! Modifier pour avoir différents comportements !

                else : #Accès direct à une cible !
                    agissant.va(dir_choix)

    def ordonne_fuite(self,agissant):
        #Il faudra identifier les comportements possibles des agissants : attaque bourrine, attaque à distance, support (renforcement), soin, fuite, recherche et autres (réanimation pour les nécromantiens par exemple)
        position = agissant.get_position()
        case = self.vue[position[0]][position[1]][position[2]] #On récupère le labyrinthe
        cases = []
        dirs = []
        for i in range(4):
            if case[7][i]:
                if case[7][i][0] in self.vue.keys():
                    case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                    entitees = case_pot[8]
                    libre = True
                    for ID_entitee in entitees:
                        if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item): #On veut s'enfuir, pas foncer dans quelqu'un !
                            libre = False
                    if libre:
                        cases.append(case_pot)
                        dirs.append(i)

        if len(cases) == 0: #On n'a nulle part où aller ! Aaaaaaaaaaaaaaaaaaaaaaaaaaaaah !
            agissant.skill_courant = None

        else:

            dir_choix = 2
            num_choix = 0
            distance = case[3]

            if distance == 0 : #On n'est pas accessible directement, ouf !

                distance = case[4]

                if distance == 0: #On n'est pas accessible du tout ! On va pouvoir souffler un peu.
                    if isinstance(agissant,Soigneur): #On peut se soigner soi-même !
                        agissant.soigne(agissant.ID)
                    elif not isinstance(agissant,Sentinelle): #Les sentinelles ne cherchent pas
                        if len(directions)>1: #On peut se permettre de choisir
                            if agissant.dir_regard != None: #L'agissant regarde quelque part
                                dir_back = [HAUT,DROITE,BAS,GAUCHE][agissant.dir_regard-2]
                                if dir_back in directions: #On ne veut pas y retourner
                                    directions.remove(dir_back)
                        agissant.va(directions[random.randint(0,len(directions)-1)]) #On prend une direction random
                    # ! Modifier pour avoir différents comportements !

                else : #On est accessible indirectement ! Aaah !
                    meilleur_choix = False
                    agissant.skill_courant = None #Dans l'éventualité où on est déjà sur la meilleure case

                    for i in range(len(cases)):
                        if cases[i][4] < distance:
                            meilleur_choix = True
                            distance = cases[i][4] #On s'éloigne quand même
                            dir_choix = directions[i]

                    if meilleur_choix:
                        agissant.va(dir_choix)

            else : #On est accessible directement ! Aaaaaaaah !
                for i in range(len(cases)):
                    if cases[i][3] < distance or (cases[i][3] == distance and cases[i][4] < cases[num_choix][4]): #On cherche à s'éloigner
                        distance = cases[i][3]
                        dir_choix = directions[i]
                        num_choix = i
                    
                agissant.va(dir_choix)

    def ordonne_soin(self,agissant,fuyards,bourrins):
        #On va considérer qu'on peut soigner à n'importe quelle distance pour l'instant
        #Mais pas d'un étage à l'autre quand même !
        PV_mins = 0
        cible = None
        for ID_fuyard in fuyards :
            fuyard = self.controleur.get_entitee(ID_fuyard)
            if fuyard.get_position()[0] == agissant.get_position()[0] and (cible == None or fuyard.pv <= PV_mins) :
                cible = ID_fuyard
                PV_mins = fuyard.pv
        if cible == None : #On soigne les bourrins alors
            for ID_bourrin in bourrins :
                bourrin = self.controleur.get_entitee(ID_bourrin)
                if bourrin.get_position()[0] == agissant.get_position()[0] and (cible == None or bourrin.pv <= PV_mins) and bourrin.pv < bourrin.pv_max :
                    cible = ID_bourrin
                    PV_mins = bourrin.pv
        if cible != None:
            agissant.soigne(cible)
        elif not isinstance(agissant,Sentinelle): #Les sentinelles ne cherchent pas
            self.ordonne_cherche(agissant)

    def ordonne_soutien(self,agissant,bourrins):
        #On va considérer qu'on peut soutenir à n'importe quelle distance pour l'instant
        #Mais pas d'un étage à l'autre quand même !
        importance = 0
        cible = None
        for ID_bourrin in bourrins :
            bourrin = self.controleur.get_entitee(ID_bourrin)
            pos = bourrin.get_position()
            distance = self.vue[pos[0]][pos[1]][pos[2]][3]
            if bourrin.get_position()[0] == agissant.get_position()[0] and distance > importance :
                cible = ID_bourrin
                importance = distance
        if cible != None:
            agissant.boost(cible)
        elif not isinstance(agissant,Sentinelle): #Les sentinelles ne cherchent pas
            self.ordonne_cherche(agissant)

    def ordonne_cherche(self,agissant):
        position = agissant.get_position()
        case = self.vue[position[0]][position[1]][position[2]] #On récupère le labyrinthe
        cases = []
        dirs = []
        for i in range(4):
            if case[7][i]:
                if case[7][i][0] in self.vue.keys():
                    case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                    entitees = case_pot[8]
                    libre = True
                    for ID_entitee in entitees:
                        if not issubclass(agissant.controleur.get_entitee(ID_entitee).get_classe(),Item):
                            libre = False
                    if libre:
                        cases.append(case_pot)
                        dirs.append(i)

        if len(cases) == 0: #On n'a nulle part où aller
            agissant.skill_courant = None

        else:

            if len(directions)>1: #On peut se permettre de choisir
                if agissant.dir_regard != None: #L'agissant regarde quelque part
                    dir_back = [HAUT,DROITE,BAS,GAUCHE][agissant.dir_regard-2]
                    if dir_back in directions: #On ne veut pas y retourner
                        directions.remove(dir_back)
            agissant.va(directions[random.randint(0,len(directions)-1)])
            # ! Modifier pour avoir différents comportements !

    def refait_vue(self):
        vues = []
        for corp in self.corps.keys(): #On récupère les vues
            if self.corps[corp] != "incapacite":
                agissant = self.controleur.get_entitee(corp)
                vues.append(agissant.vue)
        agissants_vus = []
        for vue in vues: #On identifie les agissants perçus
            agissants_vus += self.trouve_agissants(vue)
        self.oublie_agissants(agissants_vus) #Puisqu'on les a vus, on n'a plus besoin de garder en mémoire leur position précédente
        for vue in vues :
            niveau = vue[0][0][0][0] #La première coordonée de la position (première information) de la première case de la première colonne
            if niveau in self.vue.keys(): 
                self.maj_vue(vue,niveau)
            else:
                self.ajoute_vue(vue,niveau)

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant = self.controleur.get_entitee(corp)
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                ID_offenseur = offense[0]
                gravite = offense[1]
                if ID_offenseur in self.ennemis:
                    self.ennemis[ID_offenseur] += gravite
                else:
                    self.ennemis[ID_offenseur] = gravite

    def calcule_trajets(self):
        for ID_ennemi in self.ennemis.keys():
            ennemi = self.controleur.get_entitee(ID_ennemi)
            if ennemi.etat == "vivant":
                position = ennemi.get_position()
                if position[0] in self.vue.keys():
                    self.resoud(position,self.ennemis[ID_ennemi])
                    self.resoud(position,self.ennemis[ID_ennemi],3,True)

    def resoud(self,position,portee,indice=4,dead_ends=False):

        if indice == 5:
            for vue in self.vue.values():
                for colonne in vue:
                    for case in colonne:
                        case[5] = 0

        #la queue est une liste de positions
        queue=[position]

        if position[0] in self.vue.keys():

            self.vue[position[0]][position[1]][position[2]][indice] = portee

            arret_obstacle = False

            while len(queue)!=0 :

                position = queue[0]

                clarte = self.vue[position[0]][position[1]][position[2]][indice]/2
                #enlever position dans queue
                queue.pop(0)

                #trouver les positions explorables

                pos_explorables = self.positions_utilisables(position,arret_obstacle)

                arret_obstacle = dead_ends

                for pos in pos_explorables:
                    if clarte > self.vue[pos[0]][pos[1]][pos[2]][indice]:
                        #on marque la case comme visitée
                        self.vue[pos[0]][pos[1]][pos[2]][indice] = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(pos)

    def print_vue(self):
        for etage in self.vue.keys():
            matrice = self.vue[etage]
            print("Vue de l'esprit :")
            print(self.nom)
            for j in range(len(matrice)):
                haut = ""
                centre = ""
                bas = ""
                for i in range(len(matrice[0])):
                    case = matrice[i][j]
                    if case[6] == 0:
                        haut += " ~~~ "
                        centre += ": ? :"
                        bas += " ~~~ "
                    else:
                        haut+= " "
                        if case[7][0]:
                            haut += "   "
                        else:
                            haut += "---"
                        haut += " "
                        if case[7][3]:
                            centre += " "
                        else:
                            centre += "|"
                        if case[3] > 0:
                            centre += "x"
                        else:
                            centre += " "
                        if case[8] != []:
                            occ = " "
                            for occupant in case[8]:
                                if occupant in self.corps.keys():
                                    occ = "O"
                                elif occupant in self.ennemis.keys():
                                    occ = "X"
                            centre += occ
                        else:
                            centre += " "
                        if case[4] > 0:
                            centre += "x"
                        else:
                            centre += " "
                        if case[7][1]:
                            centre += " "
                        else:
                            centre += "|"
                        bas += " "
                        if case[7][2]:
                            bas += "   "
                        else:
                            bas += "---"
                        bas += " "
                print(haut)
                print(centre)
                print(bas)

    def positions_utilisables(self,position,dead_ends):
        pos_utilisables=[]
        cardinaux = [HAUT,DROITE,BAS,GAUCHE]

        case = self.vue[position[0]][position[1]][position[2]]

        for direction in cardinaux:
            if case[7][direction] and not(dead_ends and case[8]!=[]) and case[7][direction][0] in self.vue.keys():
                pos_utilisables.append(case[7][direction])

        return pos_utilisables

    def antagonise(self,nom_esprit):
        for corp in self.controleur.get_esprit(nom_esprit).get_corps():
            if not corp in self.ennemis.keys():
                self.ennemis[corp] = 0.1

    def decide(self):
        bourrins = []
        fuyards = []
        soigneurs = []
        soutiens = []
        autres = []
        for corp in self.corps.keys():
            if self.corps[corp] == "attaque":
                bourrins.append(corp)
            elif self.corps[corp] == "fuite": 
                fuyards.append(corp)
            elif self.corps[corp] == "soin":
                soigneurs.append(corp)
            elif self.corps[corp] == "soutien":
                soutiens.append(corp)
            else:
                autres.append(corp)
        if bourrins == fuyards == soigneurs == [] and soutiens != []:
            bourrins.append(soutiens[0])
            soutiens.pop(0)
        elif bourrins == fuyards == []:
            bourrins = soigneurs
            soigneurs = []
        elif soigneurs == []:
            bourrins += fuyards
            fuyards = []
        for corp in bourrins:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur): #Comment faire pour que le joueur puisse être en autopilote ?
                    agissant.recontrole()
                else:
                    self.ordonne_bourrin(agissant)
        for corp in fuyards:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()
                else:
                    self.ordonne_fuite(agissant)
        for corp in soigneurs:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()
                else:
                    self.ordonne_soin(agissant,fuyards,bourrins)
        for corp in soutiens:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()
                else:
                    self.ordonne_soutien(agissant,bourrins)
        for corp in autres:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()

    def oublie(self):
        for lab in self.vue.values():
            for i in range(len(lab)):
                for j in range(len(lab[0])):
                    case = lab[i][j]
                    if case[2] > 0:
                        case[2] -= 1
                    if case[2] <= 0:
                        case[1] = 0
                        case[6] = 0
                        case[7] = [False,False,False,False]
                        case[8] = []
                    case[3] = 0
                    case[4] = 0
                    case[5] = 0

    #Découvront le déroulé d'un tour avec esprit-sensei :
    def debut_tour(self):
        #On va faire plein de choses pendant ce tour (est-ce vraiment nécessaire de prendre des décisions si aucun des corps ne va jouer à ce tour ?
        self.get_offenses() #On s'insurge à grands cris (s'il y a lieu)
        self.refait_vue() #On prend connaissance de son environnement
        #Il faudra éventuellement définir une stratégie
        self.calcule_trajets() #On dresse les plans de bataille (s'il y a lieu)
        self.decide() #On donne les ordres

    #Tout le monde agit, nos bon-à-rien d'agissants se font massacrer à cause de leurs capacités médiocres ou remportent la victoire grâce à nos ordres brillants

    def fin_tour(self):
        #Le tour est fini, on réfléchira pendant le prochain. Comment ça, c'est mauvais pour la mémoire ?
        self.oublie()

class Esprit_type(Esprit):
    """Un esprit caricatural, pour les besoins de mes expériences."""
    def __init__(self,nom,niveau,controleur,position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        if niveau == 1:
            corps = [Tank(position,1),Dps(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Tank(position,2),Tank(position,1),Dps(position,2),Dps(position,2),Soigneur(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = (position[0],position[1],position[2]+i)
            i+=1

class Esprit_sans_scrupule(Esprit_type):
    """Un esprit qui s'en prend principalement aux soigneurs et aux soutiens."""

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant = self.controleur.get_entitee(corp)
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                ID_offenseur = offense[0]
                gravite = offense[1]
                if ID_offenseur in self.ennemis:
                    self.ennemis[ID_offenseur] += gravite
                else:
                    self.ennemis[ID_offenseur] = gravite
                offenseur = self.controleur.get_entitee(ID_offenseur)
                esprit_offenseur = self.controleur.get_esprit(offenseur.esprit)
                corps_ennemis = esprit_offenseur.corps
                for ID in corps_ennemis.keys():
                    if corps_ennemis[ID] == "soin":
                        if ID in self.ennemis:
                            self.ennemis[ID] += gravite
                        else:
                            self.ennemis[ID] = gravite
                    elif corps_ennemis[ID] == "soutien":
                        if ID in self.ennemis:
                            self.ennemis[ID] += gravite/2
                        else:
                            self.ennemis[ID] = gravite/2

class Esprit_bourrin(Esprit_type):
    """Un esprit sans soigneurs ni soutiens."""
    def __init__(self,nom,niveau,controleur,position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        if niveau == 1:
            corps = [Dps(position,1),Dps(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Dps(position,2),Dps(position,2),Dps(position,2),Dps(position,1),Dps(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = (position[0],position[1],position[2]+i)
            i+=1

class Esprit_defensif(Esprit_type):
    """Un esprit sans soigneurs ni soutiens."""
    def __init__(self,nom,niveau,controleur,position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        if niveau == 1:
            corps = [Tank(position,1),Tank(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Tank(position,2),Tank(position,2),Dps(position,2),Tank(position,1),Dps(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = (position[0],position[1],position[2]+i)
            i+=1

class Esprit_solitaire(Esprit_type):
    """Un esprit avec un unique corp."""
    def __init__(self,corp,controleur):
        self.nom = nom
        self.controleur = controleur
        self.oubli = 5
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        self.ajoute_corp(corp)

class Esprit_simple(Esprit_type):
    """Un esprit avec les corps qu'on lui donne."""
    def __init__(self,nom,corps,controleur):
        self.nom = nom
        self.controleur = controleur
        self.oubli = 5
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        self.ajoute_corps(corps)

class Esprit_humain(Esprit_type):
    """Un esprit qui dirige un ou plusieurs humains. Peut interragir avec d'autres esprits humains."""
    def __init__(self,corp,controleur): #Les humains commencent tous séparément, donc ils ont leur propre esprit au début
        self.nom = controleur.get_entitee(corp).identite
        self.controleur = controleur
        self.oubli = 5 #Faire dépendre de l'humain
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        self.ajoute_corp(corp)
        self.chef = corp #Les humains ne peuvent pas s'empêcher d'avoir des chefs

    def merge(self,nom): #Regroupe deux esprits, lorsque des humains forment un groupe
        esprit = self.controleur.get_esprit(nom)
        for corp in esprit.corps.keys():
            self.ajoute_corp(corp)
        for ennemi in esprit.ennemis.keys():
            if ennemi in self.ennemis.keys():
                self.ennemis[ennemi] = max(self.ennemis[ennemi],esprit.ennemis[ennemi])
            else:
                self.ennemis[ennemi] = esprit.ennemis[ennemi]
        for vue in esprit.vue.values():
            niveau = vue[0][0][0][0] #La première coordonée de la position (première information) de la première case de la première colonne
            if niveau in self.vue.keys(): 
                self.maj_vue(vue,niveau)
            else:
                self.ajoute_vue(vue,niveau)
        self.controleur.esprits.pop(nom)
        self.chef = self.elit()

    def elit(self):
        if 2 in self.corps.keys():
            self.chef = 2 #Le joueur est le chef par défaut ! Ah mais non mais !
        else:
            self.chef = None
            candidats = []
            for corp in self.corps.keys():
                if "humain" in self.controleur.get_entitee(corp).get_especes():
                    candidats.append(self.controleur.get_entitee(corp)) #Les humains sont les seuls à pouvoir diriger un esprit d'humain. Et les seuls à voter, aussi.
            votes_max = 0
            for candidat in candidats:
                votes = 0
                place = candidat.get_place()
                for votant in candidats:
                    votes += votant.appreciation(place)
                if votes > votes_max:
                    self.chef = candidat.ID #/!\ Éviter les chefs morts, à l'occasion /!\
                    votes_max = votes

    def exclus(self,corp): #C'est super sympa, les relations humaines !
        #Il va falloir créer un nouvel esprit pour l'humain exclus
        #Et il va falloir donner un nom à ce nouvel esprit
        #Les esprits humains sont nommés d'après leur porteur originel
        if self.controleur.get_entitee(corp).identite != self.nom: #Tout va bien
            self.controleur.esprits[self.controleur.get_entitee(corp).identite]=Esprit_humain(corp,self.controleur)
        else:
            self.controleur.esprits[self.controleur.get_entitee(corp).identite]=Esprit_humain(corp,self.controleur)
            self.elit() #Autant changer tous les rapports de force d'un coup
            self.nom = self.controleur.get_entitee(self.chef).identite

    def decide(self):
        bourrins = []
        fuyards = []
        soigneurs = []
        soutiens = []
        humains = []
        autres = []
        for corp in self.corps.keys():
            if self.corps[corp] == "attaque":
                bourrins.append(corp)
            elif self.corps[corp] == "fuite": 
                fuyards.append(corp)
            elif self.corps[corp] == "soin":
                soigneurs.append(corp)
            elif self.corps[corp] == "soutien":
                soutiens.append(corp)
            elif self.corps[corp] == "humain":
                humains.append(corp)
            else:
                autres.append(corp)
        bourrins_sups = []
        #On va traiter les humains en premier (on note que les humains fuyards ne se compliquent pas tant la vie) :
        for humain in humains :
            res = self.deplace_humain(humain)
            if res == "attaque": #L'humain est en position d'attaquer bientôt ou a attaqué, conformément aux ordres
                bourrins_sups.append(humain)
            #Sinon, c'est que l'humain s'est déjà déplacé
        if bourrins == fuyards == soigneurs == [] and soutiens != []:
            bourrins.append(soutiens[0])
            soutiens.pop(0)
        elif bourrins == fuyards == []:
            bourrins = soigneurs
            soigneurs = []
        elif soigneurs == []:
            bourrins += fuyards
            fuyards = []
        for corp in bourrins:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur): #Comment faire pour que le joueur puisse être en autopilote ?
                    agissant.recontrole()
                else:
                    self.ordonne_bourrin(agissant)
        for corp in fuyards:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()
                else:
                    self.ordonne_fuite(agissant)
        bourrins += bourrins_sups
        for corp in soigneurs:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()
                else:
                    self.ordonne_soin(agissant,fuyards,bourrins)
        for corp in soutiens:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()
                else:
                    self.ordonne_soutien(agissant,bourrins)
        for corp in autres:
            agissant = self.controleur.get_entitee(corp)
            if agissant.latence <= 0 :
                if isinstance(agissant,Joueur):
                    agissant.recontrole()

    def deplace_humain(self,ID_humain):
        res = None
        #Les mouvements des humains sont très alambiqués...
        #D'abord, les consignes positionnelles :
        humain = self.controleur.get_entitee(ID_humain)
        if humain.identite == "joueur":
            humain.recontrole()
            if humain.skill_courant in [Skill_stomp,Skill_attaque]:
                res = "attaque"
            else:
                res = "deplacement"
        else:
            if humain.mouvement == 0: #0 pour aller vers, et 1 pour chercher
                if isinstance(humain.cible_deplacement,int):
                    cible = self.controleur.get_entitee(humain.cible_deplacement).get_position()
                    portee = 5
                else:
                    cible = humain.cible_deplacement
                    portee = 3
            else:
                cible = humain.get_position()
                portee = 10 #C'est juste pour qu'il puisse aller où il veut
            pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
            if humain.position in pos_cibles: #Tout va bien, on y est ! On peut combattre, par exemple.
                #Tout le monde attaque au corps à corps quand ils en ont l'occasion (sauf la peureuse, qui fuit)
                position = humain.get_position()
                case = self.vue[position[0]][position[1]][position[2]] #On récupère le labyrinthe
                cases = []
                dirs = []
                importance = 0
                for i in range(4):
                    if case[7][i]:
                        if case[7][i][0] in self.vue.keys():
                            case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                            entitees = case_pot[8]
                            libre = True
                            for ID_entitee in entitees:
                                entitee = humain.controleur.get_entitee(ID_entitee)
                                if not issubclass(entitee.get_classe(),Item): #Un agissant !
                                    if case[7][i][0] == position[0] and ID_entitee in self.ennemis.keys() and humain.comportement_ennemis == 0: #Un ennemi ! Et le feu vert pour l'attaquer
                                        if self.ennemis[ID_entitee] > importance:
                                            importance = self.ennemis[ID_entitee]
                                            humain.attaque(i)
                                            res = "attaque"
                                    elif case[7][i][0] == position[0] and not ID_entitee in self.corps.keys() and humain.comportement_neutres == 0: #Un neutre ! Et le feu vert pour l'attaquer
                                        if importance == 0:
                                            humain.attaque(i)
                                            res = "attaque"
                                    else: #Probablement un allié, ou un neutre
                                        libre = False
                            if libre:
                                cases.append(case_pot)
                                dirs.append(i)
                if importance == 0: #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer)
                    if humain.comportement_ennemis == 2:
                        res = "fuite"
                    elif humain.identite in ["alchimiste","bombe_atomique"]: #Les deux capables d'attaquer à distance (attaques de zone)
                        if humain.attaque_en_vue(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "attaque"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peste": #La soigneuse
                        if humain.heal(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soin"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peureuse": #La spécialiste du soutien
                        if humain.boost(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soutien"
                        else:
                            res = "deplacement"
                    else: #Il ne reste plus que les bourrins
                        res = "deplacement"
                    if res in ["deplacement","fuite"] and humain.latence <= 0:
                        if len(cases) == 0: #Pas de cases libres à proximité
                            humain.skill_courant = None
                        else :
                            dir_choix = 2
                            num_choix = 0
                            distance = case[3]
                            for i in range(len(cases)):
                                if ((cases[i][3] > distance or (cases[i][3] == distance and cases[i][4] >= cases[num_choix][4])) and humain.comportement_ennemis == 0) or ((cases[i][3] < distance or (cases[i][3] == distance and cases[i][4] <= cases[num_choix][4])) and humain.comportement_ennemis == 2):
                                    distance = cases[i][3]
                                    dir_choix = dirs[i]
                                    num_choix = i
                            if distance == 0 : #Pas d'accès direct à une cible
                                distance = case[4]
                                meilleur_choix = False
                                humain.skill_courant = None #Dans l'éventualité où on est déjà sur la meilleure case
                                for i in range(len(cases)):
                                    if (cases[i][4] > distance and humain.comportement_ennemis == 0) or (cases[i][4] > distance and humain.comportement_ennemis == 2):
                                        meilleur_choix = True
                                        distance = cases[i][4] #On prend le chemin avec des obstacles
                                        dir_choix = dirs[i]
                                if meilleur_choix:
                                    humain.va(dir_choix)
                                if distance == 0: #Pas d'accès du tout !
                                    if len(dirs)>1: #On peut se permettre de choisir
                                        if humain.dir_regard != None: #L'agissant regarde quelque part
                                            dir_back = [HAUT,DROITE,BAS,GAUCHE][humain.dir_regard-2]
                                            if dir_back in dirs: #On ne veut pas y retourner
                                                dirs.remove(dir_back)
                                    humain.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                                    # ! Modifier pour avoir différents comportements !
                            else : #Accès direct à une cible !
                                humain.va(dir_choix)
            else:
                self.resoud(cible,10,5)
                position = humain.get_position()
                case = self.vue[position[0]][position[1]][position[2]]
                cases = []
                dirs = []
                importance = 0
                for i in range(4):
                    if case[7][i]:
                        if case[7][i][0] in self.vue.keys():
                            case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                            entitees = case_pot[8]
                            libre = True
                            for ID_entitee in entitees:
                                entitee = humain.controleur.get_entitee(ID_entitee)
                                if not issubclass(entitee.get_classe(),Item): #Un agissant !
                                    if case[7][i][0] == position[0] and ID_entitee in self.ennemis.keys() and humain.comportement_ennemis == 0: #Un ennemi ! Et le feu vert pour l'attaquer
                                        if self.ennemis[ID_entitee] > importance:
                                            importance = self.ennemis[ID_entitee]
                                            humain.attaque(i)
                                            res = "attaque"
                                    elif case[7][i][0] == position[0] and not ID_entitee in self.corps.keys() and humain.comportement_neutres == 0: #Un neutre ! Et le feu vert pour l'attaquer
                                        if importance == 0:
                                            humain.attaque(i)
                                            res = "attaque"
                                    else: #Probablement un allié, ou un neutre
                                        libre = False
                            if libre:
                                cases.append(case_pot)
                                dirs.append(i)
                if importance == 0: #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer)
                    if humain.comportement_ennemis == 2:
                        res = "fuite"
                    elif humain.identite in ["alchimiste","bombe_atomique"]: #Les deux capables d'attaquer à distance (attaques de zone)
                        if humain.attaque_en_vue(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "attaque"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peste": #La soigneuse
                        if humain.heal(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soin"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peureuse": #La spécialiste du soutien
                        if humain.boost(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soutien"
                        else:
                            res = "deplacement"
                    else: #Il ne reste plus que les bourrins
                        res = "deplacement"
                    if res in ["deplacement","fuite"] and humain.latence <= 0:
                        if len(cases) == 0: #Pas de cases libres à proximité
                            humain.skill_courant = None
                        else :
                            dir_choix = 2
                            num_choix = 0
                            distance = case[5]
                            for i in range(len(cases)):
                                if cases[i][5] > distance:
                                    distance = cases[i][5]
                                    dir_choix = dirs[i]
                                    num_choix = i
                            if distance > 0 : #On connait le chemin pour aller à la cible
                                humain.va(dir_choix)
                            else:
                                if len(dirs)>1: #On cherche la cible
                                    if humain.dir_regard != None: #L'agissant regarde quelque part
                                        dir_back = [HAUT,DROITE,BAS,GAUCHE][humain.dir_regard-2]
                                        if dir_back in dirs: #On ne veut pas y retourner
                                            dirs.remove(dir_back)
                                humain.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\

        return res

class Esprit_slime(Esprit_type):
    """Un esprit qui dirige un ou plusieurs slimes. Peut interragir avec d'autres esprits slimes."""
    def __init__(self,corp,controleur): #Les slimes commencent tous séparément, donc ils ont leur propre esprit au début
        self.nom = "esprit_slime"+str(controleur.get_entitee(corp).ID)
        self.controleur = controleur
        self.oubli = 5 #Faire dépendre des skills
        self.ennemis = {}
        self.vue = {}
        self.corps = {}
        self.ajoute_corp(corp)
        self.classe = controleur.get_entitee(corp).classe_principale

    def merge(self,nom): #Regroupe deux esprits, lorsque des slimes se regroupent
        esprit = self.controleur.get_esprit(nom)
        for corp in esprit.corps.keys():
            self.ajoute_corp(corp)
        for ennemi in esprit.ennemis.keys():
            if ennemi in self.ennemis.keys():
                self.ennemis[ennemi] = max(self.ennemis[ennemi],esprit.ennemis[ennemi])
            else:
                self.ennemis[ennemi] = esprit.ennemis[ennemi]
        for vue in esprit.vue.values():
            niveau = vue[0][0][0][0] #La première coordonée de la position (première information) de la première case de la première colonne
            if niveau in self.vue.keys(): 
                self.maj_vue(vue,niveau)
            else:
                self.ajoute_vue(vue,niveau)
        self.controleur.esprits.pop(nom)
        self.merge_classe(esprit.classe)

    def merge_classe(classe):
        #On va comparer tous les skills de chaque classe
        #Les slimes ont trois skills intrasecs : la fusion, pour unir deux groupes de slimes en un seul, la division, pour créer un nouveau slime, et l'absorption, pour ramasser un cadavre et voler ses skills
        #Ils peuvent avoir beaucoup de skills non-intrasecs, et n'utilisent souvent que les passifs
        #Ils ne peuvent pas avoir de sous-classes

        for skill_intrasec in classe.skills_intrasecs:
            autre_skill_intrasec = trouve_skill(self.classe_principale,type(skill_intrasec))
            if autre_skill_intrasec != None:
                if skill_intrasec.niveau > autre_skill_intrasec.niveau:
                    self.classe_principale.skill_intrasecs.remove(autre_skill_intrasec)
                    self.classe_principale.skill_intrasecs.append(skill_intrasec)
                elif skill_intrasec.xp > autre_skill_intrasec.xp:
                    self.classe_principale.skill_intrasecs.remove(autre_skill_intrasec)
                    self.classe_principale.skill_intrasecs.append(skill_intrasec)
            else: #Ça ne devrait pas arriver dans les intrasecs, mais sait-on jamais...
                print("Le slime receveur n'avait de skill intrasec correspondant à celui-ci :")
                print(skill_intrasec)
                self.classe_principale.skill_intrasecs.append(skill_intrasec)

        for skill in classe.skills:
            autre_skill = trouve_skill(self.classe_principale,type(skill))
            if autre_skill != None:
                if skill.niveau > autre_skill.niveau:
                    self.classe_principale.skill_intrasecs.remove(autre_skill)
                    self.classe_principale.skill_intrasecs.append(skill)
                elif skill.xp > autre_skill.xp:
                    self.classe_principale.skill_intrasecs.remove(autre_skill)
                    self.classe_principale.skill_intrasecs.append(skill)
            else:
                self.classe_principale.skill_intrasecs.append(skill)

    def ajoute_corp(self,corp):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            self.controleur.get_entitee(corp).rejoint(self.nom)
            self.controleur.get_entitee(corp).classe_principale = self.classe #C'est la plus grande force des slimes : progresser ensemble !

    #/!\ Faire un processus de décision propre aux slimes, qui prend en compte les capacités (communes heureusement) et la situation de chacun

    def deplace_humain(self,ID_humain):
        res = None
        #Les mouvements des humains sont très alambiqués...
        #D'abord, les consignes positionnelles :
        humain = self.controleur.get_entitee(ID_humain)
        if humain.identite == "joueur":
            humain.recontrole()
            if humain.skill_courant in [Skill_stomp,Skill_attaque]:
                res = "attaque"
            else:
                res = "deplacement"
        else:
            if humain.mouvement == 0: #0 pour aller vers, et 1 pour chercher
                if isinstance(humain.cible_deplacement,int):
                    cible = self.controleur.get_entitee(humain.cible_deplacement).get_position()
                    portee = 5
                else:
                    cible = humain.cible_deplacement
                    portee = 3
            else:
                cible = humain.get_position()
                portee = 10 #C'est juste pour qu'il puisse aller où il veut
            pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
            if humain.position in pos_cibles: #Tout va bien, on y est ! On peut combattre, par exemple.
                #Tout le monde attaque au corps à corps quand ils en ont l'occasion (sauf la peureuse, qui fuit)
                position = humain.get_position()
                case = self.vue[position[0]][position[1]][position[2]] #On récupère le labyrinthe
                cases = []
                dirs = []
                importance = 0
                for i in range(4):
                    if case[7][i]:
                        if case[7][i][0] in self.vue.keys():
                            case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                            entitees = case_pot[8]
                            libre = True
                            for ID_entitee in entitees:
                                entitee = humain.controleur.get_entitee(ID_entitee)
                                if not issubclass(entitee.get_classe(),Item): #Un agissant !
                                    if case[7][i][0] == position[0] and ID_entitee in self.ennemis.keys() and humain.comportement_ennemis == 0: #Un ennemi ! Et le feu vert pour l'attaquer
                                        if self.ennemis[ID_entitee] > importance:
                                            importance = self.ennemis[ID_entitee]
                                            humain.attaque(i)
                                            res = "attaque"
                                    elif case[7][i][0] == position[0] and not ID_entitee in self.corps.keys() and humain.comportement_neutres == 0: #Un neutre ! Et le feu vert pour l'attaquer
                                        if importance == 0:
                                            humain.attaque(i)
                                            res = "attaque"
                                    else: #Probablement un allié, ou un neutre
                                        libre = False
                            if libre:
                                cases.append(case_pot)
                                dirs.append(i)
                if importance == 0: #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer)
                    if humain.comportement_ennemis == 2:
                        res = "fuite"
                    elif humain.identite in ["alchimiste","bombe_atomique"]: #Les deux capables d'attaquer à distance (attaques de zone)
                        if humain.attaque_en_vue(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "attaque"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peste": #La soigneuse
                        if humain.heal(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soin"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peureuse": #La spécialiste du soutien
                        if humain.boost(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soutien"
                        else:
                            res = "deplacement"
                    else: #Il ne reste plus que les bourrins
                        res = "deplacement"
                    if res in ["deplacement","fuite"] and humain.latence <= 0:
                        if len(cases) == 0: #Pas de cases libres à proximité
                            humain.skill_courant = None
                        else :
                            dir_choix = 2
                            num_choix = 0
                            distance = case[3]
                            for i in range(len(cases)):
                                if ((cases[i][3] > distance or (cases[i][3] == distance and cases[i][4] >= cases[num_choix][4])) and humain.comportement_ennemis == 0) or ((cases[i][3] < distance or (cases[i][3] == distance and cases[i][4] <= cases[num_choix][4])) and humain.comportement_ennemis == 2):
                                    distance = cases[i][3]
                                    dir_choix = dirs[i]
                                    num_choix = i
                            if distance == 0 : #Pas d'accès direct à une cible
                                distance = case[4]
                                meilleur_choix = False
                                humain.skill_courant = None #Dans l'éventualité où on est déjà sur la meilleure case
                                for i in range(len(cases)):
                                    if (cases[i][4] > distance and humain.comportement_ennemis == 0) or (cases[i][4] > distance and humain.comportement_ennemis == 2):
                                        meilleur_choix = True
                                        distance = cases[i][4] #On prend le chemin avec des obstacles
                                        dir_choix = dirs[i]
                                if meilleur_choix:
                                    humain.va(dir_choix)
                                if distance == 0: #Pas d'accès du tout !
                                    if len(dirs)>1: #On peut se permettre de choisir
                                        if humain.dir_regard != None: #L'agissant regarde quelque part
                                            dir_back = [HAUT,DROITE,BAS,GAUCHE][humain.dir_regard-2]
                                            if dir_back in dirs: #On ne veut pas y retourner
                                                dirs.remove(dir_back)
                                    humain.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                                    # ! Modifier pour avoir différents comportements !
                            else : #Accès direct à une cible !
                                humain.va(dir_choix)
            else:
                self.resoud(cible,10,5)
                position = humain.get_position()
                case = self.vue[position[0]][position[1]][position[2]]
                cases = []
                dirs = []
                importance = 0
                for i in range(4):
                    if case[7][i]:
                        if case[7][i][0] in self.vue.keys():
                            case_pot = self.vue[case[7][i][0]][case[7][i][1]][case[7][i][2]]
                            entitees = case_pot[8]
                            libre = True
                            for ID_entitee in entitees:
                                entitee = humain.controleur.get_entitee(ID_entitee)
                                if not issubclass(entitee.get_classe(),Item): #Un agissant !
                                    if case[7][i][0] == position[0] and ID_entitee in self.ennemis.keys() and humain.comportement_ennemis == 0: #Un ennemi ! Et le feu vert pour l'attaquer
                                        if self.ennemis[ID_entitee] > importance:
                                            importance = self.ennemis[ID_entitee]
                                            humain.attaque(i)
                                            res = "attaque"
                                    elif case[7][i][0] == position[0] and not ID_entitee in self.corps.keys() and humain.comportement_neutres == 0: #Un neutre ! Et le feu vert pour l'attaquer
                                        if importance == 0:
                                            humain.attaque(i)
                                            res = "attaque"
                                    else: #Probablement un allié, ou un neutre
                                        libre = False
                            if libre:
                                cases.append(case_pot)
                                dirs.append(i)
                if importance == 0: #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer)
                    if humain.comportement_ennemis == 2:
                        res = "fuite"
                    elif humain.identite in ["alchimiste","bombe_atomique"]: #Les deux capables d'attaquer à distance (attaques de zone)
                        if humain.attaque_en_vue(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "attaque"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peste": #La soigneuse
                        if humain.heal(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soin"
                        else:
                            res = "deplacement"
                    elif humain.identite == "peureuse": #La spécialiste du soutien
                        if humain.boost(): #Renvoie True et choisi la cible, la magie, et le skill s'il y a une cible en vue
                            res = "soutien"
                        else:
                            res = "deplacement"
                    else: #Il ne reste plus que les bourrins
                        res = "deplacement"
                    if res in ["deplacement","fuite"] and humain.latence <= 0:
                        if len(cases) == 0: #Pas de cases libres à proximité
                            humain.skill_courant = None
                        else :
                            dir_choix = 2
                            num_choix = 0
                            distance = case[5]
                            for i in range(len(cases)):
                                if cases[i][5] > distance:
                                    distance = cases[i][5]
                                    dir_choix = dirs[i]
                                    num_choix = i
                            if distance > 0 : #On connait le chemin pour aller à la cible
                                humain.va(dir_choix)
                            else:
                                if len(dirs)>1: #On cherche la cible
                                    if humain.dir_regard != None: #L'agissant regarde quelque part
                                        dir_back = [HAUT,DROITE,BAS,GAUCHE][humain.dir_regard-2]
                                        if dir_back in dirs: #On ne veut pas y retourner
                                            dirs.remove(dir_back)
                                humain.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\

        return res



class Effet :
    """Les effets regroupent des choses qui arrivent à des éléments du système. Ils peuvent cibler une case, un mur, un agissant, un étage, etc. et sont souvent limités dans le temps ou par d'autres conditions. Ils sont évalués par le controleur dans différentes circonstances."""
    def __init__(self):
        print("a surdéfinir")

    def action(self):
        """La fonction qui exécute l'action de l'effet. En général, renvoie des valeurs que le controleur traitera."""
        print("a surdéfinir")

    def execute(self):
        """La fonction qui est appelée par le controleur. Détermine, d'après les informations transmises par le controleur, si l'action doit être effectuée ou pas. Vérifie si l'effet doit encore exister ou non."""
        print("a surdéfinir")

    def get_image(self):
        return Effet_vue()

    def termine(self):
        """La fonction qui termine l'effet."""
        if self.affiche:
            self.phase = "affichage"
        else:
            self.phase = "terminé"

    def get_skin(self):
        return SKIN_EFFET

#On distingue les effets par circonstances d'appel.
class On_tick(Effet) :
    """La classe des effets appelés à chaque tour."""
    def execute(self,porteur): #En général, prend en paramètre le porteur de l'effet. Pas toujours.
        self.action(porteur)

class On_debut_tour(On_tick):
    """La classe des effets appelés au début du tour."""
    pass

class On_post_decision(On_tick):
    """La classe des effets appelés après la phase de décision."""
    pass

class On_action(On_tick):
    """La classe des effets appelés après un action."""
    pass

class On_post_action(On_tick):
    """La classe des effets appelés après la phase d'action."""
    pass

class On_pre_attack(On_tick):
    """La classe des effets appelés avant les attaques."""
    pass

class On_fin_tour(On_tick):
    """La classe des effets appelés à la fin du tour."""
    pass

class Evenement(On_tick) :
    """La classe des effets limités par le temps, appelés une seule fois par tour."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant=temps_restant
        self.phase = "démarrage"

    def action(self):
        """La fonction qui exécute l'action de l'évènement. En général, renvoie des valeurs que le controleur traitera ?"""
        print("a surdéfinir")

class Protection_general(Evenement,On_post_action):
    """Le joueur qui a utilisé un bouclier 'protège' une zone autour de lui. C'est à dire qu'à chaque tour, d'après sa position, sa direction et les murs, certaines cases reçoivent une protection jusqu'à la fin du tour."""
    def __init__(self,temps_restant,bouclier):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.

    def action(self,agissant):
        cases = get_cases_voisines(agissant.get_position(),0) #Seule la case de l'agissant est protégée par cette version de la protection.
        for case in cases :
            case.effets.append(Protection_particulier(1,bouclier,[agissant.dir_regard]))

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class Investissement_mana(Evenement,On_debut_tour):
    """Le joueur met du mana de côté, et en a plus après !"""
    def __init__(self,temps_restant,mana):
        self.phase = "démarrage"
        self.affiche = False
        self.temps_restant = temps_restant
        self.mana = mana
        self.phase = "en cours"

    def action(self,agissant):
        if self.phase == "terminé":
            agissant.pm += self.mana

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.temps_restant <= 0 :
            self.termine()
            self.action(agissant)

class Obscurite(Evenement,On_debut_tour):
    """Evenement d'obscurité."""
    def __init__(self,niveau):
        self.affiche = False
        self.temps_restant = duree_obscurite[niveau-1]
        self.phase = "démarrage"
        self.gain_opacite = gain_obscurite[niveau-1]

    def action(self,case): #La case affectée devient plus impénétrable à la lumière
        if self.phase == "démarrage" :
            case.opacite += self.gain_opacite
        elif self.phase == "terminé":
            case.opacite -= self.gain_opacite

    def execute(self,case):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.action(case)
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
            self.action(case)

class On_attack(Effet):
    """Classe des effets appelés lors d'une attaque."""
    pass

class Protection_particulier(Evenement,On_attack):
    """La case protégée par le bouclier est 'entourée' par ce dernier, c'est à dire que pour y rentrer par certains côtés, une attaque doit d'abord être affectée par le bouclier."""
    def __init__(self,temps_restant,bouclier,directions):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.bouclier = bouclier #Techniquement c'est le bouclier qui intercepte.
        self.directions = directions

    def action(self,attaque):
        if get_dir_opposee(attaque.direction) in self.directions:
            self.bouclier.intercepte(attaque)

    def execute(self,attaque):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(attaque)

class Blizzard(Evenement,On_post_action):
    """Evenement de blizzard."""
    def __init__(self,niveau):
        self.affiche = False
        self.temps_restant = duree_blizzard[niveau]
        self.phase = "démarrage"
        self.gain_latence = gain_latence_blizzard[niveau]

    def action(self,case,position):
        if self.phase == "en cours":
            occupants = case.controleur.trouve_agissants(position)
            for occupant in occupants :
                case.controleur.get_entitee(occupant).latence.add_latence(self.gain_latence)

    def execute(self,case,position):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case,position)

class Enchantement(Evenement) :
    """Des effets avec un temps très long ! Leur classe à part permet de les affecter différement."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.temps_restant=temps_restant
        self.phase = "démarrage"

    def action(self):
        """La fonction qui exécute l'action de l'enchantement. En général, renvoie des valeurs que le controleur traitera ?"""
        print("a surdéfinir")

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.action(agissant)
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
            self.action(agissant)

class Enchantement_force(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la force (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_force):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_force = gain_force

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_force :
            agissant.taux_force["enchantf"] = gain_force
        elif self.phase == "terminé":
            agissant.taux_force.pop("enchantf")


class Enchantement_vision(Enchantement,On_debut_tour):
    """Les enchantements qui affectent le champ de vision (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_vision):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vision = gain_vision

    def action(self,agissant):
        skill = trouve_skill(agissant.classe_principale,Skill_vision)
        if self.phase == "démarrage" :
            skill.portee += gain_vision
        elif self.phase == "terminé":
            skill.portee -= gain_vision

class Enchantement_pv(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la régénération des PV (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_pv):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pv = gain_pv

    def action(self,agissant):
        if self.phase == "démarrage" :
            agissant.regen_pv += gain_pv
        elif self.phase == "terminé":
            agissant.regen_pv -= gain_pv

class Enchantement_pm(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la régénération des PM (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_pm):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pm = gain_pm

    def action(self,agissant):
        if self.phase == "démarrage" :
            agissant.regen_pm += gain_pm
        elif self.phase == "terminé":
            agissant.regen_pm -= gain_pm

class Enchantement_confusion(Enchantement,On_post_decision):
    """Les enchantements qui provoque des erreurs de direction."""
    def __init__(self,temps_restant,taux_erreur):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_erreur = taux_erreur

    def action(self,agissant):
        if self.phase == "en cours":
            if random.random() < self.taux_erreur and dir_voulue != None and agissant.latence <= 0 :
                dir_voulue = agissant.dir_regard
                dir_possibles = [HAUT,BAS,GAUCHE,DROITE].remove(dir_voulue)
                agissant.dir_regard = dir_possible[random.randint(0,2)]

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class Enchantement_poches_trouees(Enchantement,On_debut_tour):
    """Les enchantements qui fait droper des items involontairement."""
    def __init__(self,temps_restant,taux_drop):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_drop = taux_drop

    def action(self,agissant):
        if self.phase == "en cours":
            if random.random() < self.taux_drop :
                agissant.drop_random()

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class Enchantement_vitesse(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la vitesse (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_vitesse):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vitesse = gain_vitesse

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantv" not in agissant.taux_vitesse :
            agissant.taux_vitesse["enchantv"] = gain_vitesse
        elif self.phase == "terminé":
            agissant.taux_vitesse.pop("enchantv")

class Enchantement_immunite(Enchantement,On_debut_tour):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""
    def __init__(self,temps_restant,superiorite):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.superiorite = superiorite

    def action(self,agissant):
        if self.phase == "en cours":
            for effet in agissant.effets :
                if issubclass(type(effet),Maladie):
                    if maladie.priorite + self.superiorite < agissant.superiorite :
                        effet.phase = "terminé"
                        effet.action(agissant)
                        agissant.effets.remove(effet)

    def execute(self,agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class Enchantement_flamme(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément feu."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_aff_f :
            agissant.taux_aff_f["enchantf"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_f.pop("enchantf")

class Enchantement_neige(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément glace."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_aff_g :
            agissant.taux_aff_g["enchantn"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_g.pop("enchantn")

class Enchantement_sable(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément terre."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchants" not in agissant.taux_aff_t :
            agissant.taux_aff_t["enchants"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_t.pop("enchants")

class Enchantement_tenebre(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément ombre."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant):
        if self.phase == "démarrage" and "enchantt" not in agissant.taux_aff_o :
            agissant.taux_aff_o["enchantt"] = gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_o.pop("enchantt")

class Enchantement_arme(Enchantement,On_debut_tour):
    """Enchantement qui modifie les statistiques d'une arme (en positif ou négatif)."""
    def __init__(self,temps_restant,gain_force,gain_portee):
        self.temps_restant = temps_restant
        self.affiche = False
        self.phase = "démarrage"
        self.gain_force = gain_force
        self.gain_portee = gain_portee

    def action(self,arme):
        if self.phase == "démarrage" and "enchantf" not in arme.taux_force :
            arme.taux_force["enchantf"] = gain_force
        elif self.phase == "terminé":
            arme.taux_force.pop("enchantf")
        if self.phase == "démarrage" and "enchantp" not in arme.taux_portee :
            arme.taux_portee["enchantp"] = gain_portee
        elif self.phase == "terminé":
            arme.taux_portee.pop("enchantp")

class Enchantement_bombe(Enchantement,On_debut_tour):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,temps_restant,effet):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.charge = effet

    def action(self,item):
        if self.phase == "démarrage" :
            item.effets.append(self.effet)
        elif self.phase == "terminé":
            item.effets.remove(self.effet)

class Maladie(On_post_decision,On_tick):
    """L'effet de maladie. Applique un déboost à l'agissant. Peut se transmettre aux voisins. Il existe différentes maladies."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0

    def action(self,malade):
        print("À surdéfinir !")

    def contagion(self,malade): #Méthode propre aux maladies
        voisins = get_voisins(malade,distance)
        for voisin in voisins :
            if random.random() < contagiosite and (type(self) != type(effet) for effet in voisin.effets): #On ne tombe pas deux fois malade de la même maladie
                voisin.effets.append(type(self)(self.contagiosite,self.distance,self.persistence,self.virulence)) #Nid à problèmes très potentiel !

    def execute(self,malade):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.immunite <= self.persistence :
            self.termine()
        else :
            self.action(malade)

class Tirnogose(Maladie):
    """Maladie qui cause une perte progressive de PV. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "en cours" :
            malade.pv -= self.virulence
            self.immunite += 1

class Fibaluse(Maladie):
    """Maladie qui réduit les statistiques. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "démarrage" and "maladf" not in malade.taux_stats :
            malade.taux_stats["maladf"] = virulence
        elif self.phase == "en cours" :
            self.immunite += 1
        elif self.phase == "terminé" :
            malade.taux_stats.pop("maladf")

    def execute(self,malade):
        if self.phase == "démarrage" :
            self.action(malade)
            self.phase = "en cours"
        elif self.persistence <= self.immunite :
            self.termine()
            self.action(malade)
        else :
            self.action(malade)

class Ibsutiomialgie(Maladie):
    """Maladie qui peut causer une mort subite. Peut se transmettre aux voisins."""
    def __init__(self,contagiosite,distance,persistence,virulence):
        self.affiche = False
        self.phase = "démarrage"
        self.contagiosite = contagiosite
        self.distance = distance
        self.persistence = persistence
        self.immunite = 0
        self.virulence = virulence

    def action(self,malade):
        if self.phase == "démarrage" and random.random() < virulence :
            malade.meurt()
        elif self.phase == "en cours" :
            self.immunite += 1

class Poison(On_debut_tour,On_tick):
    """La classe des effets d'empoisonnement."""
    def __init__(self,responsable,degats_max,progression):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = 0
        self.progression = progression
        self.degats_max = degats_max

    def action(self,victime):
        if self.phase == "en cours" :
            victime.pv -= self.degats
            if self.degats < self.degats_max:
                self.degats += self.progression

    def execute(self,victime):
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif victime.etat == "mort" :
            self.termine()
        else :
            self.action(victime)

class Time_limited(Effet):
    """Classe des effets limités par le temps, qu'on ne peut pas considérer comme des événements car leur appel est irrégulier."""
    def __init__(self,temps_restant):
        self.affiche = False
        self.phase = "démarrage"
        self.temps_restant = temps_restant

    def wait(self):
        self.temps_resant -= 1
        if self.temps_restant <= 0:
            self.termine()

class On_need(Effet) :
    """Classe des effets appelés lors de circonstances particulières. Ils n'ont pas besoin d'être mis à jour, pris en compte ou quoique ce soit le reste du temps."""
    pass

class Reserve_mana(On_need):
    """Effet qui correspond à une réserve de mana pour le joueur qui peut piocher dedans lorsqu'il en a besoin, mais ce mana n'est pas compté dans le calcul de son mana max."""
    def __init__(self,mana):
        self.phase = "démarrage"
        self.affiche = False
        self.mana = mana
        self.phase = "en cours"

    def action(self,mana):
        if self.phase == "en cours":
            self.mana -= mana

    def execute(self,mana):
        if self.phase == "en cours" :
            self.action(mana)
        if self.mana <= 0 :
            self.termine()

class One_shot(Effet):
    """Classe des effets qui n'ont à être appelés qu'une seule fois."""

    def execute(self,parametre): # La plupart des one_shot sont de cette forme...
        if self.phase == "démarrage" :
            self.action(parametre)
            self.termine()

class Antidote(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,Poison):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Medicament(One_shot,On_fin_tour):
    """Effet qui supprime les effets de maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,Maladie): # Créer des médicaments différents selon les maladies ?
                effet.phase = "terminé" # Rajouter une condition de priorite

class Purification(One_shot,On_fin_tour):
    """Effet qui supprime les effets de poison ou maladie du joueur."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        for effet in porteur.effets:
            if isinstance(effet,(Maladie,Poison)):
                effet.phase = "terminé" # Rajouter une condition de priorite

class Enseignement(One_shot,On_fin_tour):
    """Effet qui enseigne une magie au joueur."""
    def __init__(self,magie):
        self.affiche = False
        self.magie = magie
        self.phase = "démarrage"

    def action(self,porteur):
        skill = trouve_skill(porteur.classe_principale,Skill_magie)
        if skill != None:
            skill.ajoute(self.magie)

class Dopage(One_shot,On_attack):
    """Effet qui "dope" la prochaine attaque du joueur."""
    def __init__(self,taux_degats):
        self.affiche = False
        self.phase = "démarrage"
        self.taux_degats = taux_degats

    def action(self,attaque):
        if self.phase == "démarrage" :
            attaque.degats *= self.taux_degats

class Instakill(One_shot,On_post_action):
    """L'effet d'instakill. S'il réussit, la victime voit ses PV descendre à 0. Sinon, rien.""" #Comment retirer aussi les PM, si la victime a la persévérance (essence magique) ?
    def __init__(self,responsable,priorite):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite

    def action(self,porteur):
        if porteur.priorite < self.priorite :
            porteur.instakill(self.responsable)
        else :
            porteur.echape_instakill(self.responsable)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

class En_sursis(One_shot,On_fin_tour):
    """L'effet de sursis d'un projectile perçant qui a jusqu'à la fin du tour pour tuer l'agissant sur sa case."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,item):
        if item.controleur.trouve_agissants(item.get_position()) != []:
            if isinstance(item,(Fragile,Evanescent)):
                item.etat = "brisé"
            else :
                item.arret()
        
class Attaque(One_shot):
    """L'effet d'attaque dans sa version générale. Pour chaque case dans la zone, crée une attaque (version intermèdiaire). Attachée au responsable."""
    def __init__(self,responsable=0,degats=0,element=TERRE,portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.portee = portee
        self.propagation = propagation
        self.direction = direction
        self.autre = autre
        self.taux_autre = taux_autre

    def action(self,controleur):
        position = controleur.get_entitee(self.responsable).get_position()
        positions_touches = controleur.get_pos_touches(position,self.portee,self.propagation,self.direction,"alliés",self.responsable)
        for position_touche in positions_touches:
            controleur.labs[position[0]].matrice_cases[position_touche[1]][position_touche[2]].effets.append(Attaque_case(self.responsable,self.degats,self.element,self.direction,self.autre,self.taux_autre))

class Attaque_case(One_shot):
    """L'effet d'attaque dans sa version intermédiaire. Créée par une attaque (version générale), chargé d'attacher une attaque particulière aux agissants de la case, en passant d'abord les défenses de la case. Attachée à la case."""
    def __init__(self,responsable,degats,element,direction = None,autre=None,taux_autre=None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.autre = autre
        self.taux_autre = taux_autre

    def action(self,case,position):
        victimes_potentielles = case.controleur.trouve_agissants(position)
        for victime_potentielle in victimes_potentielles:
            if not victime_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_corps():
                if self.autre == None :
                    case.controleur.get_entitee(victime_potentielle).effets.append(Attaque_particulier(self.responsable,self.degats,self.element,self.direction))
                elif self.autre == "piercing":
                    case.controleur.get_entitee(victime_potentielle).effets.append(Attaque_percante(self.responsable,self.degats,self.element,self.direction,taux_perce))

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.action(case,position)
            self.termine()

    def get_skin(self):
        if self.element == TERRE:
            return SKIN_ATTAQUE_TERRE
        elif self.element == FEU:
            return SKIN_ATTAQUE_FEU
        elif self.element == GLACE:
            return SKIN_ATTAQUE_GLACE
        elif self.element == OMBRE:
            return SKIN_ATTAQUE_OMBRE

class Attaque_particulier(One_shot):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable,degats,element,direction = None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction

    def action(self,victime):
        victime.subit(self.degats,self.element,self.responsable)

    def get_skin(self):
        return SKIN_BLESSURE

class Attaque_percante(Attaque_particulier): #Attention ! Perçant pour une attaque signifie qu'elle traverse les defenses. C'est totalement différend pour un item !
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version générale), chargé d'infligé les dégats, en passant d'abord les défenses de la case puis celles de l'agissant. Attachée à la victime. En prime, une partie de ses dégats ne sont pas bloquables."""
    def __init__(self,responsable,degats,element,direction = None,taux_perce = 0):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats * taux_perce
        self.degats_imbloquables = degats - self.degats #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction

    def action(self,victime):
        self.degats += self.degats_imbloquables
        victime.subit(self.degats,self.element,self.responsable)

    def get_skin(self):
        return SKIN_BLESSURE
    
class On_hit(Effet):
    """La classe des effets qui se déclenchent quand un projectile heurte un agissant ou un mur."""
    def __init__(self,portee,degats,element = TERRE):
        self.affiche = False
        self.portee = portee
        self.degats = degats
        self.element = element

    def action(self,lanceur,position,controleur):
        positions_touches = controleur.get_pos_touches(position,self.portee)
        for position_touche in positions_touches:
            controleur.labs[position[0]].matrice_cases[position_touche[1]][position_touche[2]].effets.append(Attaque_case(lanceur,self.degats,self.element))

    def execute(self,lanceur,position,controleur):
        self.action(lanceur,position,controleur)

class On_step_in(Effet):
    """La classe des effets déclenchés lorsqu'on marche sur une case."""
    pass

class On_step_out(Effet):
    """La classe des effets déclenchés quand on quitte une case."""
    pass

class On_through(Effet):
    """La classe des effets déclenchés quand on traverse un mur."""
    pass

class Teleport(On_through):
    """L'effet de téléportation, qui modifie la position de l'agissant (il peut aussi s'agir d'un déplacement normal)."""
    def __init__(self,position,surnaturel = False):
        self.affiche = surnaturel
        self.position = position

    def action(self,entitee):
        # On va chercher un éventuel occupant de la case cible
        occupants = entitee.controleur.trouve_agissants(self.position)
        if issubclass(entitee.get_classe(),Item):
            if entitee.get_position()[0]!=self.position[0]: #Un item passe quoi qu'il arrive
                entitee.controleur.move(self.position,entitee)
            else:
                entitee.set_position(self.position)
            for occupant in occupants:
                entitee.heurte_agissant(occupant) #Mais il heurte les agissants
        else:
            passe = True
            if occupants != []:
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement) #On peut peut-être écraser l'occupant de l'autre case
                if ecrasement != None:
                    for occupant in occupants:
                        agissant = entitee.controleur.get_entitee(occupant)
                        if not ecrasement.utilise(agissant.get_priorite(),entitee.get_priorite()):
                            passe = False
                else:
                    passe = False
            if passe:
                if entitee.get_position()[0]!=self.position[0]: #Un item passe quoi qu'il arrive
                    entitee.controleur.move(self.position,entitee)
                else:
                    entitee.set_position(self.position)

    def execute(self,entitee):
        self.action(entitee)

    def get_skin(self):
        return SKIN_PORTAIL

class Escalier(Teleport):

    def __init__(self,position,sens):
        self.affiche = True
        self.sens = sens
        self.position = position

    def get_skin(self):
        if self.sens == HAUT:
            return SKIN_ESCALIER_HAUT
        elif self.sens == BAS:
            return SKIN_ESCALIER_BAS #/!\ Modifier pour avoir deux images différentes

class On_try_through(Effet):
    """La classe des effets déclenchés quand on essaye de traverser un mur."""
    
class Mur_plein(On_try_through):
    """L'effet qui correspond à la présence d'un mur plein sur le passage de l'entitee."""
    def __init__(self,durete):
        self.affiche = True
        self.durete = durete #La priorite qu'il faut avoir pour briser ce mur.
        self.casse = False

    def action(self,mur,entitee):
        if not(isinstance(entitee,Fantome)): #Deux moyens de traverser un mur plein : être un fantome ;
            ecrasement = None
            if not(issubclass(entitee.get_classe(),Item)):
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)   # ou l'écraser.
            if ecrasement != None :
                passage = ecrasement.utilise(self.durete,entitee.get_priorite())
                if passage :
                    self.casse = True
                    mur_oppose = mur.get_mur_oppose()
                    if mur_oppose != None:
                        for effet in mur_oppose.effets :
                            if isinstance(effet,Mur_plein):
                                effet.casse = True
                else :
                    mur.peut_passer = False
            else :
                mur.peut_passer = False

    def execute(self,mur,entitee):
        if not(self.casse) :
            self.action(mur,entitee)

    def get_skin(self):
        if not(self.casse) :
            return SKIN_MUR
        else:
            return SKIN_MUR_CASSE

class Mur_impassable(On_try_through):
    """L'effet qui correspond à un mur absolument infranchissable."""
    def __init__(self):
        self.affiche = True

    def action(self,mur,entitee):
        mur.peut_passer = False

    def execute(self,mur,entitee):
        self.action(mur,entitee)

    def get_skin(self):
        return SKIN_MUR

class Porte(On_try_through):
    """L'effet qui correspond à la présence d'une porte sur le passage de l'entitée (une porte et un mur plein peuvent se cumuler, mais ce n'est pas conseillé)."""
    def __init__(self,durete,code,automatique = False):
        self.affiche = True
        self.durete = durete #La priorite qu'il faut avoir pour briser ce mur.
        self.code = code #Le code qui permet d'ouvrir la porte
        self.casse = False
        self.ferme = True
        self.auto = automatique

    def action(self,mur,entitee):
        if not(isinstance(entitee,Fantome)):          #Trois moyens de traverser une porte : être un fantome ;
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()): # avoir la clée ;
                ecrasement = None
                if not(issubclass(entitee.get_classe(),Item)):
                    ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)  # ou tout détruire !
                if ecrasement != None :
                    passage = ecrasement.utilise(self.durete,entitee.get_priorite())
                    if passage :
                        self.casse = True
                        self.affiche = False
                        self.ferme = False #Si on détruit la porte, elle n'est plus fermée...
                        mur_oppose = mur.get_mur_oppose()
                        if mur_oppose != None:
                            for effet in mur_oppose.effets :
                                if isinstance(effet,Porte):
                                    effet.casse = True
                                    effet.affiche = False
                                    effet.ferme = False #On voudrait aussi ouvrir l'autre côté de la porte.
                    else :
                        mur.peut_passer = False
                else :
                    mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False
                mur_oppose = mur.get_mur_oppose()
                if mur_oppose != None:
                    for effet in mur_oppose.effets :
                        if isinstance(effet,Porte):
                            effet.ferme = False #On voudrait aussi ouvrir l'autre côté de la porte.

    def execute(self,mur,entitee):
        if not(self.casse) and self.ferme :
            self.action(mur,entitee)

    def get_skin(self):
        if self.ferme:
            return SKIN_PORTE
        else:
            return SKIN_PORTE_OUVERTE

class Barriere(On_try_through):
    """L'effet qui correspond à la présence d'une barrière magique, qui bloque certaines entitées selon certains critères."""

    def execute(self,mur,entitee):
        self.action(mur,entitee)

    def get_skin(self):
        return SKIN_BARRIERE

class Barriere_classe(Barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions de classe."""
    def __init__(self,classe):
        self.affiche = True
        self.classe = classe

    def action(self,mur,entitee): #Pour interdire certains coins aux fantômes
        if isinstance(entitee,self.classe):
            mur.peut_passer = False

class Barriere_espece(Barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions d'espèce."""
    def __init__(self,espece):
        self.affiche = True
        self.espece = espece

    def action(self,mur,entitee):
        if isinstance(entitee,Agissant) and self.espece in entitee.get_especes():
            mur.peut_passer = False

class Barriere_tribale(Barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'appartenance à un esprit."""
    def __init__(self,esprit):
        self.affiche = True
        self.esprit = esprit

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if isinstance(entitee,Agissant) and entitee.get_esprit() != self.esprit:
            mur.peut_passer = False

class Barriere_altitude(Barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'altitude de l'item."""
    def __init__(self,altitude):
        self.affiche = True
        self.altitude = altitude

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if not(isinstance(entitee,Item)) or not(entitee.hauteur >= self.altitude):
            mur.peut_passer = False

class Porte_barriere(Barriere,Porte):
    """Lorsqu'une barrière peut être franchie avec une clée."""
    pass

class Porte_classe(Porte_barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions de classe, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,classe,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.classe = classe

    def action(self,mur,entitee): #Pour interdire certains coins aux fantômes
        if isinstance(entitee,self.classe):
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_espece(Porte_barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions d'espèce, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,espece,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.espece = espece

    def action(self,mur,entitee):
        if isinstance(entitee,Agissant) and self.espece in entitee.get_especes():
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_tribale(Porte_barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'appartenance à un esprit, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,esprit,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.esprit = esprit

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if isinstance(entitee,Agissant) and entitee.get_esprit() != self.esprit:
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_altitude(Porte_barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'altitude de l'item."""
    def __init__(self,durete,code,altitude,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.altitude = altitude

    def action(self,mur,entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if not(isinstance(entitee,Item)) or not(entitee.hauteur >= self.altitude):
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

# On va distinguer 3 types d'aura :
#   - Les auras naturellement attachées à une case. Ce sont des auras élémentaires. Elles peuvent être temporairement réprimée par une autre aura élémentale.
#   - Les auras non-élémentaires. Comme l'aura d'instakill ou l'aura divine, elles sont superposables autant qu'on veut, et attachées à un agissant.
#   - Les auras élémentaires attachées à un agissant. Celles qui nous embêtent le plus. La plus forte étouffe les autres, mais laisse les autres auras du même agissant s'exprimer.
# Peut-être considérer l'utilisation d'auras autour d'items comme la boule de feu ?
class Aura(On_tick):
    """La classe des auras (attachées à la case)."""
    pass #Ne doit pas être instanciée

class Aura_elementale(Aura):
    """La classe des effets d'auras élémentales. Attaché à la case."""

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(self.niveau,porteur.ID,priorite))

class Aura_permanente(Aura_elementale):
    """La classe des effets d'aura élémentales permanentes, celles qui représentent l'élément par défaut de la case."""

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.phase = "en cours"

class Terre(One_shot,Aura_elementale):
    """L'effet qui applique l'aura de terre à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.distance = 0
        self.affiche = False

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.termine() #Pour l'instant elle ne fait rien. Rien qu'empêcher les autres auras de s'exprimer. Je suppose que ça peut servir quand on visite des étages non-terrestres.
        case.code += 1 #0 ou 1, selon que la case a une aura de Terre ou non

class Terre_permanente(Aura_permanente):
    """L'effet qui applique l'aura de terre à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.affiche = False

    def execute(self,case,position):
        case.code += 1 #0 ou 1, selon que la case a une aura de Terre ou non

class Feu(Evenement,Aura_elementale):
    """L'effet qui applique l'aura de feu à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite,duree):
        self.phase = "démarrage"
        self.temps_restant = duree
        self.responsable = responsable
        self.priorite = priorite
        self.distance = 0
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_agissants(position)
        lanceur = contr.get_entitee(self.responsable)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            if agissant.esprit != lanceur.esprit :
                agissant.subit(self.temps_restant,FEU,self.responsable)
        case.code += 2 #0 ou 2, selon que la case a une aura de Feu ou non

    def execute(self,case,position):
        self.temps_restant -= 1
        self.priorite -= 0.3 #La priorite diminue progressivement, donc une aura de feu descend rarement jusqu'à 0 dégats.
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case,position)

class Feu_permanent(Aura_permanente):
    """L'effet qui applique l'aura de feu à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite,degats):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.degats = degats
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_agissants(position)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            agissant.subit(self.degats,FEU)
        case.code += 2 #0 ou 2, selon que la case a une aura de Feu ou non

class Glace(One_shot,Aura_elementale):
    """L'effet qui applique l'aura de glace à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite,gain_latence):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.gain_latence= gain_latence
        self.distance = 0
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_agissants(position)
        lanceur = contr.get_entitee(self.responsable)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            if agissant.esprit != lanceur.esprit and GLACE not in agissant.immunites :
                agissant.latence += self.gain_latence
        case.code += 4 #0 ou 4, selon que la case a une aura de Glace ou non

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.action(case,position)
            self.termine()

class Glace_permanente(Aura_permanente):
    """L'effet qui applique l'aura de glace à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite,gain_latence):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.gain_latence = gain_latence
        self.affiche = False

    def action(self,case,position):
        contr = case.controleur
        occupants = contr.trouve_agissants(position)
        for occupant in occupants :
            agissant = contr.get_entitee(occupant)
            if GLACE not in agissant.immunites :
                agissant.latence += self.gain_latence
        case.code += 4 #0 ou 4, selon que la case a une aura de Glace ou non

class Ombre(One_shot,Aura_elementale):
    """L'effet qui applique l'aura d'ombre à une case. Laissé ici par un agissant."""

    def __init__(self,responsable,priorite,gain_opacite):
        self.phase = "démarrage"
        self.responsable = responsable
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.distance = 0
        self.affiche = False

    def action(self,case,position):
        case.opacite_bonus = self.gain_opacite
        case.code += 8 #0 ou 8, selon que la case a une aura d'Ombre ou non. Comme l'ombre et le reste sont incompatibles, les codes 9 à 15 sont libres. Le code maximum pour la partie élémentaire est 8

    def execute(self,case,position):
        if self.phase == "démarrage":
            self.action(case,position)
            self.termine()

class Ombre_permanente(Aura_permanente):
    """L'effet qui applique l'aura d'ombre à une case. Il a toujours été là, et il n'en bougera pas."""

    def __init__(self,priorite,gain_opacite):
        self.phase = "démarrage"
        self.responsable = 0
        self.priorite = priorite
        self.gain_opacite = gain_opacite
        self.affiche = False

    def action(self,case,position):
        case.opacite_bonus = self.gain_opacite
        case.code += 8 #0 ou 8, selon que la case a une aura d'Ombre ou non. Comme l'ombre et le reste sont incompatibles, les codes 9 à 15 sont libres. Le code maximum pour la partie élémentaire est 8

# Voilà maintenant les auras au niveau de l'agissant :

class Aura_terre(One_shot,On_debut_tour):
    """Le centre de l'aura de terre d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_terre[self.niveau-1]
        self.priorite = priorite_aura_terre[self.niveau-1]
        self.effet = Terre
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite))

class Aura_feu(One_shot,On_debut_tour):
    """Le centre de l'aura de feu d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_feu[self.niveau-1]
        self.priorite = priorite_aura_feu[self.niveau-1]
        self.duree = duree_aura_feu[self.niveau-1]
        self.effet = Feu
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite,self.duree))

class Aura_glace(One_shot,On_debut_tour):
    """Le centre de l'aura de glace d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_glace[self.niveau-1]
        self.priorite = priorite_aura_glace[self.niveau-1]
        self.gain_latence = gain_latence_aura_glace[self.niveau-1]
        self.effet = Glace
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite,self.gain_latence))

class Aura_ombre(One_shot,On_debut_tour):
    """Le centre de l'aura d'ombre d'un agissant. Attaché à l'agissant, placera les effets voulus sur les cases voisines."""

    def __init__(self,niveau):
        self.phase = "démarrage"
        self.niveau = niveau
        self.portee = portee_aura_ombre[self.niveau-1]
        self.priorite = priorite_aura_ombre[self.niveau-1]
        self.gain_opacite = gain_opacite_aura_ombre[self.niveau-1]
        self.effet = Ombre
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,self.portee)
        priorite = porteur.priorite + self.priorite
        for case in cases:
            case.ajoute_aura(self.effet(porteur.ID,priorite,self.gain_opacite))

class Magie(On_action):
    """La classe des magies. Un effet qui s'attache au lanceur le temps de remplir les paramètres, puis se lance avant la phase d'attaque."""
    def __init__(self,gain_xp,cout_pm,latence): #Toutes ces caractéristiques sont déterminées par la sous-classe au moment de l'instanciation, en fonction de la magie utilisée et du niveau.
        self.gain_xp = gain_xp
        self.cout_mp = cout_mp
        self.latence = latence
        self.phase = "démarrage"

    def execute(self,lanceur):
        if self.phase == "démarrage":
            self.action(lanceur)
            self.termine()

    def miss_fire(self,lanceur):
        lanceur.subit(20)

class Magie_dirigee(Magie) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,temps):
        self.temps_dir = temps
        self.direction = None

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.direction != None:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Magie_cout(Magie):
    """La classe des magies dont le coût peut varier."""
    def __init__(self,temps):
        self.temps_cout = temps

class Magie_cible(Magie) :
    """La classe des magies qui nécessitent une (ou plusieurs) cible(s)."""
    def __init__(self,temps):
        self.temps = temps
        self.cible = None

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.cible != None:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Multi_cible(Magie_cible) :
    """La classe des magies qui nécessitent plusieurs cibles."""
    def __init__(self,temps):
        self.temps = temps
        self.cible = []

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.cible != []:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Magie_cible_dirigee(Magie_cible,Magie_dirigee):
    def __init__(self,temps_dir,temps):
        self.temps_dir = temps_dir
        self.temps = temps
        self.cible = None
        self.direction = None

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.direction != None and self.cible != None:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Sort :
    """La classe des sorts. Lancer un sort de magie coûte du mana. Les agissants capable d'utiliser de la magie disposent d'un skill qui regroupe toutes les magies.
       !!! Ne pas confondre Sort et Magie ! Le premier est le produit de la deuxième ! Une magie regroupe 10 sorts, soit les dix formes de la magie, du niveau 1 au niveau 10."""
    def __init__(self,gain_xp,cout_mp,latence): #Les caractéristiques partagées par tous les sorts
        self.gain_xp = gain_xp
        self.cout_mp = cout_mp
        self.latence = latence

    #Il n'y a pas de méthode commune à tous les sorts

class Portee_limitee(Magie_cible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,portee):
        self.portee = portee

class Cible_agissant(Magie_cible):
    """La classe des magies qui ciblent d'autres agissants."""
    def __init__(self):
        print("Cible_agissant ne doit pas être instanciée.")

class Cible_item(Magie_cible):
    """La classe des magies qui ciblent des items."""
    def __init__(self):
        print("Cible_item ne doit pas être instanciée.")

class Cible_item_inventaire(Magie_cible):
    """La classe des magies qui ciblent des items dans l'inventaire d'un agissant."""
    def __init__(self):
        print("Cible_item_inventaire ne doit pas être instanciée.")

class Cible_case(Magie_cible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    def __init__(self):
        print("Cible_case ne doit pas être instanciée.")

# Normalement on en a fini avec les magies ciblées

class Invocation(Magie):
    """La classe des magies qui créent une entitée (un agissant pour se battre à vos côtés, un projectile magique pour attaquer les ennemis, un item à utiliser plus tard..."""
    def __init__(self,gain_xp,cout_mp,latence,entitee):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Invocation_projectile(Invocation,Magie_dirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,gain_xp,cout_mp,latence,temps,entitee):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        Magie_dirigee.__init__(self,temps)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Creation_effet(Magie):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,gain_xp,cout_mp,latence,effet):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.effet = effet

    def get_effet(self):
        return self.effet

class Enchante(Creation_effet):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,gain_xp,cout_mp,latence,enchantement):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.enchantement = enchantement

    def get_enchantement(self):
        return self.enchantement

class Enchante_item(Enchante,Cible_item):
    """La classe des magies qui enchantent un item."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_cases(Enchante,Cible_case,Multi_cible):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_agissant(Enchante,Cible_agissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Attaque_magique(Magie):
    """La classe des magies d'attaque (pas les projectiles, ni les effets qui infligent des dégats, ni les instakills, juste les dégats directs, représentés par un objet Attaque)."""
    def __init__(self,gain_xp,cout_mp,latence,attaque):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.attaque = attaque

    def get_attaque(self):
        return self.attaque

class Attaque_magique_dirigee(Magie_dirigee):
    def __init__(self,gain_xp,cout_mp,latence,temps,attaque):
        Attaque_magique.__init__(self,gain_xp,cout_mp,latence,attaque)
        Magie_dirigee.__init__(self,temps)

# Maintenant on va créer les véritables sorts. On commence par les soins :
class Magie_soin(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin[niveau-1]
        self.cout_pm = cout_pm_soin[niveau-1]
        self.latence = latence_soin[niveau-1]
        self.gain_pv = gain_pv_soin[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = False

    def action(self,lanceur):
        agissant_cible = lanceur.controleur.get_entitee(self.cible)
        agissant_cible.effets.append(Soin(self.gain_pv))

    def get_skin():
        return SKIN_MAGIE_SOIN

class Magie_soin_superieur(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie_soin_superieur"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_superieur[niveau-1]
        self.cout_pm = cout_pm_soin_superieur[niveau-1]
        self.latence = latence_soin_superieur[niveau-1]
        self.gain_pv = gain_pv_soin_superieur[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = False

    def action(self,lanceur):
        agissant_cible = lanceur.controleur.get_entitee(self.cible)
        agissant_cible.effets.append(Soin(self.gain_pv))

    def get_skin():
        return SKIN_MAGIE_SOIN_SUPERIEUR

class Magie_soin_de_zone(Cible_case):
    """La magie qui invoque un effet de soin sur une zone."""
    nom = "magie zone de soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_zone[niveau-1]
        self.cout_pm = cout_pm_soin_zone[niveau-1]
        self.latence = latence_soin_zone[niveau-1]
        self.gain_pv = gain_pv_soin_zone[niveau-1]
        self.portee = portee_soin_zone[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = False

    def action(self,lanceur):
        poss = lanceur.controleur.get_pos_touches(self.cible,self.portee)
        for pos in poss:
            lanceur.controleur.labs[pos[0]].matrice_cases[pos[1]][pos[2]].effets.append(Soin_case(self.gain_pv),lanceur.ID)

    def get_skin():
        return SKIN_MAGIE_SOIN_ZONE

class Magie_auto_soin(Magie):
    """La magie qui invoque un effet de soin sur son lanceur."""
    nom = "magie auto soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_auto[niveau-1]
        self.cout_pm = cout_pm_soin_auto[niveau-1]
        self.latence = latence_soin_auto[niveau-1]
        self.gain_pv = gain_pv_soin_auto[niveau-1]
        self.affiche = False

    def action(self,lanceur):
        lanceur.effets.append(Soin(self.gain_pv))

    def get_skin():
        return SKIN_MAGIE_AUTO_SOIN

class Soin_case(On_post_action):
    """Un effet de soin. À répercuter sur les occupants éventuels de la case."""
    def __init__(self,gain_pv,responsable=0,cible="alliés"):
        self.phase = "démarrage"
        self.gain_pv = gain_pv
        self.responsable = responsable
        self.cible = cible
        self.affiche = True

    def action(self,case,position):
        cibles_potentielles = case.controleur.trouve_agissants(position)
        for cible_potentielle in cibles_potentielles:
            if self.responsable == 0: #Pas de responsable. Sérieusement ?
                case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.gain_pv))
            else:
                esprit = case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit)
                if esprit == None: #Pas d'esprit ? Sérieusement ?
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.gain_pv))
                elif self.cible == "alliés" and cible_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_corps():
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.gain_pv))
                elif self.cible == "neutres" and not cible_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_ennemis():
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.gain_pv))

    def execute(self,case,position):
        if self.phase == "démarrage" :
            self.action(case,position)
            self.termine()

class Soin(On_fin_tour):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    def __init__(self,gain_pv):
        self.phase = "démarrage"
        self.gain_pv = gain_pv
        self.affiche = False

    def action(self,porteur):
        porteur.soigne(self.gain_pv)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

class Magie_resurection(Magie):
    """La magie qui invoque un effet de resurection."""
    nom = "magie resurection"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_resurection[niveau-1]
        self.cout_pm = cout_pm_resurection[niveau-1]
        self.latence = latence_resurection[niveau-1]
        self.affiche = False

    def action(self,lanceur):
        ID_cadavre = lanceur.inventaire.get_item_courant()
        cadavre = lanceur.controleur.get_entitee(ID_cadavre)
        if cadavre.get_classe() == Cadavre:
            lanceur.inventaire.drop(lanceur.position)
            cadavre.effets.append(Resurection())

    def get_skin():
        return SKIN_MAGIE_RESURECTION

class Resurection(On_fin_tour):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,porteur):
        porteur.pv = porteur.pv_max
        porteur.etat = "vivant"

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

class Magie_reanimation_de_zone(Cible_case,Portee_limitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    nom = "magie reanimation"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_reanimation[niveau-1]
        self.cout_pm = cout_pm_reanimation[niveau-1]
        self.latence = latence_reanimation[niveau-1]
        self.taux_pv = taux_pv_reanimation[niveau-1]
        self.portee = portee_reanimation[niveau-1]
        self.portee_limite = portee_limite_reanimation[niveau-1]
        self.superiorite = superiorite_reanimation[niveau-1]
        self.temps = 10000
        self.cible = None
        self.affiche = False

    def action(self,porteur):
        cadavres = porteur.controleur.get_cadavres_touches(self.cible,self.portee)
        esprit = porteur.controleur.get_esprit(porteur.get_esprit())
        for cadavre in cadavres:
            if cadavre.get_priorite()+self.superiorite < porteur.get_priorite():
                cadavre.effets.append(Reanimation(self.taux_pv,esprit))

    def get_skin():
        return SKIN_MAGIE_REANIMATION_ZONE

class Reanimation(On_fin_tour):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,taux,esprit):
        self.phase = "démarrage"
        self.taux = taux
        self.esprit = esprit
        self.affiche = False

    def action(self,porteur):
        porteur.pv = porteur.pv_max*self.taux
        porteur.etat = "vivant"
        if self.esprit != None:
            esprit_porteur = porteur.controleur.get_esprit(porteur)
            if esprit_porteur != None:
                esprit_porteur.retire_corp(porteur)
            self.esprit.ajoute_corp(porteur)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

# C'est tout pour les soins et assimilés.
# On passe aux projectiles :

class Magie_boule_de_feu(Magie_dirigee):
    """La magie qui invoque une boule de feu."""
    nom = "magie boule de feu"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_boule_de_feu[niveau-1]
        self.cout_pm = cout_pm_boule_de_feu[niveau-1]
        self.latence = latence_boule_de_feu[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Boule_de_feu(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_skin():
        return SKIN_MAGIE_BOULE_DE_FEU

class Magie_fleche_de_glace(Magie_dirigee):
    """La magie qui invoque une flèche de glace."""
    nom = "magie fleche de glace"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_fleche_de_glace[niveau-1]
        self.cout_pm = cout_pm_fleche_de_glace[niveau-1]
        self.latence = latence_fleche_de_glace[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Fleche_de_glace(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_skin():
        return SKIN_MAGIE_FLECHE_DE_GLACE

class Magie_rocher(Magie_dirigee):
    """La magie qui invoque un rocher."""
    nom = "magie rocher"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_rocher[niveau-1]
        self.cout_pm = cout_pm_rocher[niveau-1]
        self.latence = latence_rocher[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Rocher(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_skin():
        return SKIN_MAGIE_ROCHER

class Magie_ombre_furtive(Magie_cible_dirigee,Cible_case,Portee_limitee):
    """La magie qui invoque une ombre futive."""
    nom = "magie ombre furtive"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_ombre_furtive[niveau-1]
        self.cout_pm = cout_pm_ombre_furtive[niveau-1]
        self.latence = latence_ombre_furtive[niveau-1]
        self.portee_limite = portee_ombre_furtive[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.direction = None
        self.temps = 10000
        self.temps_dir = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Ombre_furtive(self.niveau,self.cible,self.direction,porteur.ID))

    def get_skin():
        return SKIN_MAGIE_OMBRE_FURTIVE

class Magie_jet_de_mana(Magie_dirigee):
    """La magie qui invoque un jet de mana."""
    nom = "magie jet de mana"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_jet_de_mana[niveau-1]
        self.cout_pm = cout_pm_jet_de_mana[niveau-1]
        self.latence = latence_jet_de_mana[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Jet_de_mana(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_skin():
        return SKIN_MAGIE_JET_DE_MANA

class Magie_eclair_noir(Magie_dirigee):
    """La magie qui invoque un éclair noir."""
    nom = "magie eclair noir"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_eclair_noir[niveau-1]
        self.cout_pm = cout_pm_eclair_noir[niveau-1]
        self.latence = latence_eclair_noir[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Eclair_noir(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_skin():
        return SKIN_MAGIE_ECLAIR_NOIR

class Magie_enchantement_faiblesse(Enchante_agissant):
    """La magie qui place un enchantement de faiblesse sur un agissant."""
    nom = "magie faiblesse"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_faiblesse[niveau-1]
        self.cout_pm = cout_pm_faiblesse[niveau-1]
        self.latence = latence_faiblesse[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_force(duree_faiblesse[self.niveau-1],gain_force_faiblesse[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE

class Magie_enchantement_cecite(Enchante_agissant):
    """La magie qui place un enchantement de cécité sur un agissant."""
    nom = "magie cecite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_cecite[niveau-1]
        self.cout_pm = cout_pm_cecite[niveau-1]
        self.latence = latence_cecite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_vision(duree_cecite[self.niveau-1],gain_vision_cecite[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_CECITE

class Magie_enchantement_perte_de_pv(Enchante_agissant):
    """La magie qui place un enchantement de perte de pv sur un agissant."""
    nom = "magie perte de pv"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_perte_de_pv[niveau-1]
        self.cout_pm = cout_pm_perte_de_pv[niveau-1]
        self.latence = latence_perte_de_pv[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pv(duree_perte_de_pv[self.niveau-1],gain_pv_perte_de_pv[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PV

class Magie_enchantement_perte_de_pm(Enchante_agissant):
    """La magie qui place un enchantement de perte de pm sur un agissant."""
    nom = "magie perte de pm"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_perte_de_pm[niveau-1]
        self.cout_pm = cout_pm_perte_de_pm[niveau-1]
        self.latence = latence_perte_de_pm[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pm(duree_perte_de_pm[self.niveau-1],gain_pm_perte_de_pm[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PM

class Magie_enchantement_confusion(Enchante_agissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    nom = "magie confusion"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_confusion[niveau-1]
        self.cout_pm = cout_pm_confusion[niveau-1]
        self.latence = latence_confusion[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_confusion(duree_confusion[self.niveau-1],taux_erreur_confusion[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_CONFUSION

class Magie_enchantement_poches_trouees(Enchante_agissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    nom = "magie poches trouees"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poches_trouees[niveau-1]
        self.cout_pm = cout_pm_poches_trouees[niveau-1]
        self.latence = latence_poches_trouees[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_poches_trouees(duree_poches_trouees[self.niveau-1],taux_drop_poches_trouees[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_POCHES_TROUEES

class Magie_enchantement_force(Enchante_agissant):
    """La magie qui place un enchantement de force sur un agissant."""
    nom = "magie force"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_force[niveau-1]
        self.cout_pm = cout_pm_force[niveau-1]
        self.latence = latence_force[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_force(duree_force[self.niveau-1],gain_force[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_FORCE

class Magie_enchantement_vision(Enchante_agissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    nom = "magie vision"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_vision[niveau-1]
        self.cout_pm = cout_pm_vision[niveau-1]
        self.latence = latence_vision[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_vision(duree_vision[self.niveau-1],gain_vision[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_VISION

class Magie_enchantement_vitalite(Enchante_agissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    nom = "magie vitalite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_vitalite[niveau-1]
        self.cout_pm = cout_pm_vitalite[niveau-1]
        self.latence = latence_vitalite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pv(duree_vitalite[self.niveau-1],gain_pv_vitalite[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_VITALITE

class Magie_enchantement_absorption(Enchante_agissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    nom = "magie absorption"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_absorption[niveau-1]
        self.cout_pm = cout_pm_absorption[niveau-1]
        self.latence = latence_absorption[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pm(duree_absorption[self.niveau-1],gain_pm_absorption[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_ABSORPTION

class Magie_enchantement_celerite(Enchante_agissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    nom = "magie celerite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_celerite[niveau-1]
        self.cout_pm = cout_pm_celerite[niveau-1]
        self.latence = latence_celerite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_vitesse(duree_celerite[self.niveau-1],gain_vitesse_celerite[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_CELERITE

class Magie_enchantement_immunite(Enchante_agissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    nom = "magie immunite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_immunite[niveau-1]
        self.cout_pm = cout_pm_immunite[niveau-1]
        self.latence = latence_immunite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_immunite(duree_immunite[self.niveau-1],superiorite_immunite[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_IMMUNITE

class Magie_enchantement_flamme(Enchante_agissant):
    """La magie qui place un enchantement de flamme sur un agissant."""
    nom = "magie flamme"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_flamme[niveau-1]
        self.cout_pm = cout_pm_flamme[niveau-1]
        self.latence = latence_flamme[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_flamme(duree_flamme[self.niveau-1],gain_affinite_flamme[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_FLAMME

class Magie_enchantement_neige(Enchante_agissant):
    """La magie qui place un enchantement de neige sur un agissant."""
    nom = "magie neige"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_neige[niveau-1]
        self.cout_pm = cout_pm_neige[niveau-1]
        self.latence = latence_neige[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_neige(duree_neige[self.niveau-1],gain_affinite_neige[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_NEIGE

class Magie_enchantement_sable(Enchante_agissant):
    """La magie qui place un enchantement de sable sur un agissant."""
    nom = "magie sable"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_sable[niveau-1]
        self.cout_pm = cout_pm_sable[niveau-1]
        self.latence = latence_sable[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_sable(duree_sable[self.niveau-1],gain_affinite_sable[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_SABLE

class Magie_enchantement_tenebre(Enchante_agissant):
    """La magie qui place un enchantement de ténèbre sur un agissant."""
    nom = "magie tenebre"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_tenebre[niveau-1]
        self.cout_pm = cout_pm_tenebre[niveau-1]
        self.latence = latence_tenebre[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_tenebre(duree_tenebre[self.niveau-1],gain_affinite_tenebre[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_TENEBRE

class Magie_enchantement_rouille(Enchante_item):
    """La magie qui place un enchantement de rouille sur un item."""
    nom = "magie rouille"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_rouille[niveau-1]
        self.cout_pm = cout_pm_rouille[niveau-1]
        self.latence = latence_rouille[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_arme(duree_rouille[self.niveau-1],gain_force_rouille[self.niveau-1],gain_portee_rouille[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_ROUILLE

class Magie_enchantement_renforcement(Enchante_item):
    """La magie qui place un enchantement de renforcement sur un item."""
    nom = "magie renforcement"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_renforcement[niveau-1]
        self.cout_pm = cout_pm_renforcement[niveau-1]
        self.latence = latence_renforcement[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_arme(duree_renforcement[self.niveau-1],gain_force_renforcement[self.niveau-1],gain_portee_renforcement[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT

class Magie_enchantement_bombe(Enchante_item):
    """La magie qui place un enchantement de bombe sur un item."""
    nom = "magie bombe"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_bombe[niveau-1]
        self.cout_pm = cout_pm_bombe[niveau-1]
        self.latence = latence_bombe[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_bombe(duree_bombe[self.niveau-1],On_hit(portee_bombe[self.niveau-1],degats_bombe[self.niveau-1])))

    def get_skin():
        return SKIN_MAGIE_ENCHANTEMENT_BOMBE

class Magie_reserve(Magie_cout):
    """La magie qui fait une réserve de mana."""
    nom = "magie reserve"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_reserve[niveau-1]
        self.cout_pm = 0
        self.latence = latence_reserve[niveau-1]
        self.niveau = niveau
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Reserve_mana(self.cout_pm*taux_reserve[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_RESERVE

class Magie_investissement(Magie_cout):
    """La magie qui crée un investissement."""
    nom = "magie investissement"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_investissement[niveau-1]
        self.cout_pm = 0
        self.latence = latence_investissement[niveau-1]
        self.niveau = niveau
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Investissement_mana(duree_investissement[self.niveau-1],self.cout_pm*taux_investissement[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_INVESTISSEMENT

class Magie_explosion_de_mana(Magie_cout):
    """La magie qui crée une explosion de mana."""
    nom = "magie explosion de mana"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_explosion_de_mana[niveau-1]
        self.cout_pm = 0
        self.latence = latence_explosion_de_mana[niveau-1]
        self.niveau = niveau
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Attaque(porteur.ID,self.cout_pm*taux_degats_explosion_de_mana[self.niveau-1],TERRE,portee_explosion_de_mana[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_EXPLOSION_DE_MANA

class Magie_laser(Attaque_magique_dirigee):
    """La magie qui crée une attaque de laser."""
    nom = "magie laser"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_laser[niveau-1]
        self.cout_pm = cout_pm_laser[niveau-1]
        self.latence = latence_laser[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Attaque(porteur.ID,degats_laser[self.niveau-1],TERRE,portee_laser[self.niveau-1],"R__T___",self.direction))

    def get_skin():
        return SKIN_MAGIE_LASER

class Magie_poing_magique(Attaque_magique_dirigee): #À modifier selon l'espèce qui l'utilise
    """La magie qui crée une attaque de poing magique."""
    nom = "magie poing magique"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_magique[niveau-1]
        self.cout_pm = cout_pm_poing_magique[niveau-1]
        self.latence = latence_poing_magique[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Attaque(porteur.ID,degats_poing_magique[self.niveau-1],TERRE,portee_poing_magique[self.niveau-1],"Sd_T___",self.direction))

    def get_skin():
        return SKIN_MAGIE_POING_MAGIQUE

class Magie_poing_ardent(Attaque_magique_dirigee): #L'attaque de mélée de la bombe atomique
    """La magie qui crée une attaque de poing ardent."""
    nom = "magie poing ardent"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_ardent[niveau-1]
        self.cout_pm = cout_pm_poing_ardent[niveau-1]
        self.latence = latence_poing_ardent[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Attaque(porteur.ID,degats_poing_ardent[self.niveau-1],TERRE,portee_poing_ardent[self.niveau-1],"Sd_T___",self.direction))

    def get_skin():
        return SKIN_MAGIE_POING_MAGIQUE

class Magie_brasier(Attaque_magique):
    """La magie qui crée une attaque de brasier."""
    nom = "magie brasier"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_brasier[niveau-1]
        self.cout_pm = cout_pm_brasier[niveau-1]
        self.latence = latence_brasier[niveau-1]
        self.niveau = niveau
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Attaque(porteur.ID,degats_brasier[self.niveau-1],FEU,portee_brasier[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_BRASIER

class Magie_avalanche(Attaque_magique_dirigee):
    """La magie qui crée une attaque d'avalanche."""
    nom = "magie avalanche"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_avalanche[niveau-1]
        self.cout_pm = cout_pm_avalanche[niveau-1]
        self.latence = latence_avalanche[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Attaque(porteur.ID,degats_avalanche[self.niveau-1],TERRE,portee_avalanche[self.niveau-1],"S__S_Pb",self.direction))

    def get_skin():
        return SKIN_MAGIE_AVALANCHE

class Magie_blizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_blizzard[niveau-1]
        self.cout_pm = cout_pm_blizzard[niveau-1]
        self.latence = latence_blizzard[niveau-1]
        self.niveau = niveau
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,portee_blizzard[self.niveau-1])
        for case in cases:
            case.effets.append(Blizzard(self.niveau))

    def get_skin():
        return SKIN_MAGIE_BLIZZARD

class Magie_obscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_obscurite[niveau-1]
        self.cout_pm = cout_pm_obscurite[niveau-1]
        self.latence = latence_obscurite[niveau-1]
        self.niveau = niveau
        self.affiche = False

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,portee_obscurite[self.niveau-1])
        for case in cases:
            case.effets.append(Obscurite(self.niveau))

    def get_skin():
        return SKIN_MAGIE_OBSCURITE

class Magie_dopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_dopage[niveau-1]
        self.cout_pm = cout_pm_dopage[niveau-1]
        self.latence = latence_dopage[niveau-1]
        self.niveau = niveau
        self.affiche = False

    def action(self,porteur):
        porteur.effets.append(Dopage(taux_dopage[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_DOPAGE

class Magie_instakill(Magie_cible):
    """La magie qui crée un effet d'instakill sur un agissant."""
    nom = "magie instakill"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_instakill[niveau-1]
        self.cout_pm = cout_pm_instakill[niveau-1]
        self.latence = latence_instakill[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = False

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Instakill(porteur.ID,porteur.priorite - superiorite_instakill[self.niveau-1]))

    def get_skin():
        return SKIN_MAGIE_INSTAKILL

# Les sorts de projectiles qui sont lancés depuis l'emplacement de l'agissant n'ont pas besoin de classe propre (la classe Invocation suffit).
# On les liste quand même pour rappel :
#    - La boule de feu (c'est un projectile explosif (crée une zone de dégats quand il touche un ennemi ou un mur), parmi les magies de feu, quand il cause des dégats, inflige un effet de feu (la cible perd de la vie lentement))
#    - La flèche de glace (c'est un projectile percant (poursuit son trajet si l'agissant meurt), parmi les magies de glace, quand il cause des dégats, inflige un effet de glace (la cible est ralentie))
#    - Le rocher (c'est un projectile simple (tout dans les dégats !), parmi les magies de terre)
# (La magie de projectile d'ombre n'est pas lancée depuis l'emplacement de l'agissant, d'où son absence dans la liste.)
#    - Le projectile magique (c'est un projectile simple)
#    - L'éclair noir (c'est un projectile perçant explosif (quand il touche un agissant ou un mur, il provoque une grande zone de dégats autour de lui, et si l'obstacle était un agissant et est mort suite aux dégats directs ou à l'explosion, l'éclair noir poursuit sa course)
#    - D'autres ?

# Les enchantements qui affectent le joueur n'ont pas besoin de classe propre (la classe Enchantement suffit). De même pour les autres enchantements.
# On les liste quand même pour rappel :
#    - Faiblesse (réduit la force d'un agissant)
#    - Cécité (réduit la portée de la vision d'un agissant) (particulièrement utile contre les éclaireurs d'une meute)
#    - Perte de pv (réduit progressivement les pv d'un agissant)
#    - Perte de pm (réduit progressivement les pm d'un agissant)
#    - Confusion (l'agissant a une certaine chance de ne pas regarder dans la bonne direction lors de ses actions (attaque ou déplacement par exemple)
#    - Poches trouées (l'agissant a une certaine chance de perdre l'un de ses items à chaque tour)
#    - Force (augmente la force d'un agissant)
#    - Vision (augmente la portée de la vision d'un agissant) (particulièrement utile pour un sniper, un observateur, ou un enchanteur)
#    - Célérité (augmente la vitesse d'un agissant)
#    - Vitalité (augmente la régénération des pv d'un agissant)
#    - Absorption (augmente la régénération des pm d'un agissant)
#    - Immunité (protège l'agissant contre les maladies et poisons)
#    - Flamme (augmente l'affinité au feu, parmi les magies de feu)
#    - Neige (augmente l'affinité à la glace, parmi les magies de glace)
#    - Sable (augmente l'affinité à la terre, parmi les magies de terre)
#    - Ténèbre (augmente l'affinité à l'ombre, parmi les magies d'ombre)
#    - Rouille (réduit les statistiques d'une arme)
#    - Renforcement (augmente les statistiques d'une arme)
#    - Bombe (confère des propriétés d'explosif à un item)
#    - D'autres ?

# Les attaques magiques lancées depuis la position du joueur n'ont pas besoin de classe propre (la classe Attaque_magique suffit).
# On les liste quand même pour rappel :
#    - Laser (attaque rectiligne de très grande portée)
#    - Brasier (attaque de zone centrée sur l'agissant, parmi les magies de feu, inflige un effet de feu (la cible perd de la vie lentement))
#    - Avalanche (attaque semi-circulaire de grande portee, parmi les magies de terre)
#    - D'autres ?

# Les effets qui ciblent le joueur ou sont lancés à l'emplacement du joueur n'ont pas besoin de classe propre (la classe Effet suffit).
# On les liste quand même pour rappel :
#    - Dopage (augmente la force du joueur lors de la prochaine attaque)
#    - Réserve (crée une réserve de pm (indépendante des pm de l'agissant, donc potentiellement au delà des pm max) (contenant moins de pm que le sort n'en a coûté, mais permettant de dépenser plus de pm d'un coup par la suite))
#    - Investissement (donne des pm longtemps après le lancement du sort (plus de pm que le coût, si les pm dépassent les pm max l'agissant arrêtera de régénérer ses pm))
#    - Blizzard (crée une zone de ralentissement centrée sur l'agissant, parmi les magies de glace, inflige un effet de glace (la cible est ralentie))
#    - Obscurité (crée une zone où le champ de vision est réduit)
#    - D'autres ?

class Affichage:
    def __init__(self,screen):
        print("Initialisation de l'affichage")
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
        self.dessine_zones("carré")

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
        self.dessine_zones(joueur.curseur)

        self.dessine_lab(joueur)
        self.dessine_droite(joueur)
        self.dessine_gauche(joueur)

    def dialogue(self,joueur):
        """phase de dialogue avec un pnj"""
        self.dessine_zones(joueur.curseur)

        self.dessine_lab(joueur)
        self.dessine_droite_dialogue(joueur)
        self.dessine_gauche(joueur)

    def draw_magie_cible(self,joueur):
        """phase de choix d'une cible"""
        self.frame += 1
        self.dessine_zones(joueur.curseur)

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
        self.dessine_zones(joueur.curseur)

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
        self.dessine_zones(joueur.curseur)

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
        self.dessine_zones(joueur.curseur)

        self.dessine_lab(joueur)
        self.dessine_droite_magie_cout(joueur)
        self.dessine_gauche(joueur)

    def redraw_magie_cout(self,joueur,proportion_ecoulee):
        """phase de choix d'un cout"""
        self.frame += 1
        self.redessine_zone_d()
        self.dessine_droite_magie_cout(joueur,proportion_ecoulee)

    def dessine_zones(self,curseur):
        self.screen.fill((0,0,0))
        police=pygame.font.SysFont(None, 20)
        titre=police.render("Ceci est un test !",True,(255,255,255))
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

            PV = police.render("PV",True,(0,0,0))
            PM = police.render("PM",True,(0,0,0))
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

                quantite=police.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche+longueur_barre_pv,hauteur_texte_pv))

            else:
                total_pv = joueur.pv_max
                longueur_barre_pv = longueur_barre_totale*(joueur.pv/total_pv)
                pygame.draw.rect(self.screen,(255,160,160),(marge_gauche,hauteur_barre_pv,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(255,0,0),(marge_gauche,hauteur_barre_pv,longueur_barre_pv,10))

                quantite=police.render("0",True,(0,0,0))
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

                quantite=police.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche+longueur_barre_pm,hauteur_texte_pm))

            elif joueur.pm != joueur.get_total_pm() and observation >= 5: #Le joueur a des effets de réserve et peut les voir (trouver une valeur du niveau du skill observation un peu moins arbitraire !
                total_pm = joueur.get_total_pm() - joueur.pm + joueur.pm_max
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                longueur_barre_pm_sans_reserve = longueur_barre_totale*(joueur.pm_max/total_pm)
                longueur_barre_reserve = longueur_barre_totale - longueur_barre_pm_sans_reserve
                pygame.draw.rect(self.screen,(160,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(32,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_pm,10))
                pygame.draw.rect(self.screen,(32,255,255),(marge_gauche+longueur_barre_pm_sans_reserve,hauteur_barre_pm,longueur_barre_reserve,10))

                quantite=police.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche,hauteur_texte_pm))

            else:
                total_pm = joueur.pm_max
                longueur_barre_pm = longueur_barre_totale*(joueur.pm/total_pm)
                pygame.draw.rect(self.screen,(160,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_totale,10))
                pygame.draw.rect(self.screen,(32,255,255),(marge_gauche,hauteur_barre_pm,longueur_barre_pm,10))

                quantite=police.render("0",True,(0,0,0))
                self.screen.blit(quantite,(marge_gauche,hauteur_texte_pm))

            marge_haut = self.position_debut_y_rectangles_et_carre+55

        else:

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-10,40))

            marge_haut += 5

            pos_PV = marge_gauche + 5

            pos_PM = marge_gauche + self.largeur_rectangles//2

            longueur_barre_totale = self.largeur_rectangles//2 - 15

            PV = police.render("PV",True,(0,0,0))
            PM = police.render("PM",True,(0,0,0))
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

            inventaire = police.render("Inventaire",True,(0,0,0))
            self.screen.blit(inventaire,(marge_gauche+5,marge_haut+5))

            marge_haut += 25

        elif curseur == "in_inventaire":

            #L'affichage de l'inventaire est composé de trois parties : les icones des catégories, les icones des items, et un aperçu de l'item courant

            inventaire = joueur.inventaire #Applaudissez bien fort le protagoniste du rectangle de gauche !

            limite_haut = marge_haut

            cats = [SKIN_POTION,SKIN_PARCHEMIN,SKIN_CLE,SKIN_ARME,SKIN_BOUCLIER_BIS,SKIN_ARMURE_BIS,SKIN_CASQUE,SKIN_ANNEAU,SKIN_PROJECTILE,SKIN_CRANE,SKIN_OEUF]
            cat_courante = inventaire.cat_courante

            titre = police.render("Inventaire :",True,(0,0,0))
            self.screen.blit(titre,(marge_gauche,limite_haut))

            limite_haut += 25
            marge_haut = limite_haut

            icat = inventaire.cat_courante

            for i in range(11):
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

            noms = ["Potions :","Parchemins :","Clés :","Armes :","Boucliers :","Armures :","Haumes :","Anneaux :","Cadavres :","Oeufs :"]

            titre_cat = police.render(noms[icat],True,(0,0,0))
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

                titre_description = police.render("Description :",True,(0,0,0))
                self.screen.blit(titre_description,(marge_gauche,limite_haut))

                limite_haut += 25
                marge_haut = limite_haut

                infos = joueur.controleur.get_entitee(items[inventaire.item_courant]).get_description(observation)
                for info in infos :
                    texte_info = police.render(info,True,(0,0,0))
                    self.screen.blit(texte_info,(marge_gauche,marge_haut))
                    marge_haut += 25

                marge_bas = max(marge_bas,marge_haut + 25)

            marge_haut = marge_bas

        else:

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-10,25))

            inventaire = police.render("Inventaire",True,(0,0,0))
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

            inventaire = police.render("Classe principale",True,(0,0,0))
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

                    skill = police.render("Sous-classes",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                elif classe.curseur == "in_classes":

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render("Sous-classes :",True,(0,0,0))
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
                        nom_classe = police.render(classes[i].nom,True,(0,0,0))
                        self.screen.blit(nom_classe,(marge_gauche+10,marge_haut+5))
                        marge_haut += 25

                elif classe.curseur == "in_classe":

                    cont = True
                    classe = classe.sous_classes[classe.classe_courante]

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render(classe.nom,True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                else:

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render("Sous-classes",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25


                if classe.curseur == "skills_intrasecs":

                    pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-(10*compt)-4,21))

                    skill = police.render("Skills intrasecs",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                elif classe.curseur == "in_skills_intrasecs":

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render("Skills intrasecs :",True,(0,0,0))
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
                        nom_skill = police.render(skills[i].nom,True,(0,0,0))
                        self.screen.blit(nom_skill,(marge_gauche+10,marge_haut+5))
                        marge_haut += 25

                elif not cont:

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render("Skills intrasecs",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                if classe.curseur == "skills":

                    pygame.draw.rect(self.screen,couleur_curseur_actif,(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche+2,marge_haut+2,self.largeur_rectangles-(10*compt)-4,21))

                    skill = police.render("Skills",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25

                elif classe.curseur == "in_skills":

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render("Skills :",True,(0,0,0))
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
                        nom_skill = police.render(skills[i].nom,True,(0,0,0))
                        self.screen.blit(nom_skill,(marge_gauche+10,marge_haut+5))
                        marge_haut += 25

                elif not cont:

                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-(10*compt),25))

                    skill = police.render("Skills",True,(0,0,0))
                    self.screen.blit(skill,(marge_gauche+5,marge_haut+5))

                    marge_haut += 25



        else:

            pygame.draw.rect(self.screen,(225,225,225),(marge_gauche,marge_haut,self.largeur_rectangles-10,25))

            inventaire = police.render("Classe principale",True,(0,0,0))
            self.screen.blit(inventaire,(marge_gauche+5,marge_haut+5))

            marge_haut += 25

    def dessine_droite(self,joueur): #La fonction qui dessine le rectangle de droite. Elle affiche le joueur, son interlocuteur ou son ennemi, sur fond de labyrinthe. Elle fait appel a des graphiques presque déjà complets (une couche pour le labyrinthe, une autre pour l'agissant, une troisième pour les équippements de l'agissant, une quatrième pour une expression du visage.

        marge_haut = self.position_debut_y_rectangles_et_carre + 2

        skill = trouve_skill(joueur.classe_principale,Skill_observation)

        observation = 0

        for i in range(len(self.messages)-1,-1,-1):
            message = self.messages[i]
            if skill != None:
                observation = skill.utilise() #On le réactive à chaque fois qu'on observe quelque chose !
            message[1]-=1
            if message[2]<=observation:
                police=pygame.font.SysFont(None, 20)
                texte = police.render(message[0],True,(0,0,0))
                self.screen.blit(texte,(self.position_debut_x_rectangle_2+2,marge_haut))
                marge_haut += 20
            if message[1] == 0:
                self.messages.remove(message)

    def dessine_droite_dialogue(self,joueur): #La fonction qui écrit les dialogues à droite
        #Dans un jeu parfait, on aurait une image de l'interlocuteur au dessus des répliques

        marge_haut = self.position_debut_y_rectangles_et_carre + 5
        marge_gauche = self.position_debut_x_rectangle_2 + 5

        #D'abord, la réplique de l'interlocuteur, si il y en a une
        textes = self.scinde_texte(joueur.interlocuteur.replique,self.largeur_rectangles-10)
        for texte in textes :
            self.screen.blit(texte,(marge_gauche,marge_haut))
            marge_haut += 20

        replique_courante = joueur.interlocuteur.replique_courante
        for i in range(len(joueur.interlocuteur.repliques)):
            replique = joueur.interlocuteur.repliques[i]
            textes = self.scinde_texte(replique,self.largeur_rectangles-25)
            if replique_courante == i:
                self.screen.blit(pygame.font.SysFont(None, 20).render("->",True,(255,125,0)),(marge_gauche,marge_haut))
            for texte in textes :
                self.screen.blit(texte,(marge_gauche+15,marge_haut))
                marge_haut += 20

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
            joueur.controleur.get_entitee(joueur.cibles[i]).get_skin().dessine_toi(self.screen,(marge_gauche+2,marge_haut+2),40)
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

        SKIN_DIRECTION.dessine_toi(self.screen,(marge_gauche,marge_haut),40,joueur.dir_regard)

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

        police = pygame.font.SysFont(None, 20)

        texte = []

        texte.append(police.render("Mana à disposition : " + str(joueur.get_total_pm()),True,(0,0,0)))
        texte.append(police.render("Cout_actuel : " + str(joueur.choix_cout_magie),True,(0,0,0)))
        texte.append(police.render("(Utilisez les touches haut et bas pour modifier le coût.)",True,(0,0,0)))
        texte.append(police.render("Précision du coût : " + str(joueur.precision_cout_magie),True,(0,0,0)))
        texte.append(police.render("(Utilisez les touches gauche et droite pour modifier la précision.)",True,(0,0,0)))

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
        taille_case = self.hauteur_exploitable // nb_cases
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
        taille_case = self.hauteur_exploitable // nb_cases
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
        police = pygame.font.SysFont(None, 20)
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
            texte = police.render(descr,True,(255,255,255))
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
                        lettre = police.render(letter.upper(),True,(255,255,255))
                        self.screen.blit(lettre,(marge_gauche+28,marge_haut+28))
                marge_gauche += 50
            marge_haut += 50
            marge_gauche = 10 + self.position_debut_x_carre
            descr = noms_dirs[element_courant]
            texte = police.render(descr,True,(255,255,255))
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
                        lettre = police.render(letter.upper(),True,(255,255,255))
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
            texte = police.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))
        elif etage == 2:
            touches = []
            for touche in joueur.cat_touches.keys():
                if joueur.cat_touches[touche] == "skill" and joueur.skill_touches[touche] == Skill_magie:
                    touches.append(touche)
            for i in range(len(magies)):
                if element_courant == i:
                    pygame.draw.rect(self.screen,(225,225,225),(marge_gauche-2,marge_haut-2,44,44))
                magies[i].get_skin().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                for touche in touches :
                    if i < len(magies) and joueur.magies[touche] == magies[i].nom:
                        letter = pygame.key.name(touche)
                        lettre = police.render(letter.upper(),True,(255,255,255))
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
            texte = police.render(descr,True,(255,255,255))
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
                    lancer[i].get_skin().dessine_toi(self.screen,(marge_gauche,marge_haut),40)
                for touche in touches :
                    if i < len(lancer) and joueur.projectiles[touche] == lancer[i]:
                        letter = pygame.key.name(touche)
                        lettre = police.render(letter.upper(),True,(255,255,255))
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
            texte = police.render(descr,True,(255,255,255))
            self.screen.blit(texte,(marge_gauche,marge_haut))

    def choix_touche(self,joueur,zones,skills,magies,lancer):
        """phase de choix d'une touche"""
        self.frame += 1
        self.dessine_zones(joueur.curseur)

        self.dessine_choix_touche(joueur,zones,skills,magies,lancer)
        self.dessine_droite(joueur)
        self.dessine_gauche(joueur)

    def choix_niveau(self,joueur):
        """phase de choix d'un niveau"""
        self.frame += 1
        self.dessine_zones(joueur.curseur)

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

            police = pygame.font.SysFont(None, 20)

            titre = police.render("Choix du niveau " + str(joueur.classe_principale.niveau),True,(0,0,0))
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

            police = pygame.font.SysFont(None, 20)

            titre = police.render("Choix élémentaire",True,(0,0,0))
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

        police = pygame.font.SysFont(None, 20)

        for phrase in descr:
            texte = police.render(phrase,True,(0,0,0))
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
    
    def message(self,texte="Ceci est le message par défaut. Avez-vous oublié de préciser ce que vous vouliez dire ?",temps = 20,secret=0):
        self.messages.append([texte,temps,secret])

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

    def affiche(self,joueur,vue,position,taille):
        self.affichables=[]
        if vue[1]==0:
            SKIN_BROUILLARD.dessine_toi(self.screen,position,taille)
        elif vue[1]==-1: #On a affaire à un case accessible mais pas vue
            SKIN_BROUILLARD.dessine_toi(self.screen,position,taille)
            if vue[0][2] > 0:
                if vue[7][HAUT]:
                    if joueur.vue[vue[0][1]][vue[0][2]-1][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,HAUT)
            if vue[0][1] < len(joueur.vue) - 1:
                if vue[7][DROITE]:
                    if joueur.vue[vue[0][1]+1][vue[0][2]][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,DROITE)
            if vue[0][2] < len(joueur.vue[0]) -1:
                if vue[7][BAS]:
                    if joueur.vue[vue[0][1]][vue[0][2]+1][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,BAS)
            if vue[0][1] > 0:
                if vue[7][GAUCHE]:
                    if joueur.vue[vue[0][1]-1][vue[0][2]][1]>0:
                        SKIN_MUR_BROUILLARD.dessine_toi(self.screen,position,taille,GAUCHE)
        else:
            if vue[6]==0: #On teste le code de la case pour déterminer son image
                SKIN_CASE.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==1: #On teste le code de la case pour déterminer son image
                SKIN_CASE_1.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==2: #On teste le code de la case pour déterminer son image
                SKIN_CASE_2.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==3: #On teste le code de la case pour déterminer son image
                SKIN_CASE_3.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==4: #On teste le code de la case pour déterminer son image
                SKIN_CASE_4.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==5: #On teste le code de la case pour déterminer son image
                SKIN_CASE_5.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==6: #On teste le code de la case pour déterminer son image
                SKIN_CASE_6.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==7: #On teste le code de la case pour déterminer son image
                SKIN_CASE_7.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            elif vue[6]==8: #On teste le code de la case pour déterminer son image
                SKIN_CASE_8.dessine_toi(self.screen,position,taille) #La case en premier, donc en bas
            case = joueur.controleur.get_case(vue[0])
            for i in range(4):
                mur = case.get_mur_dir(i)
                for effet in mur.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(self.screen,position,taille,i)
            for effet in case.effets:
                if effet.affiche:
                    effet.get_skin().dessine_toi(self.screen,position,taille)
                    if effet.phase == "affichage":
                        effet.phase = "terminé"
            entitees = vue[8]
            agissant = None
            for ID_entitee in entitees : #Puis les items au sol
                entitee = joueur.controleur.get_entitee(ID_entitee)
                if issubclass(entitee.get_classe(),Item):
                    entitee.get_skin().dessine_toi(self.screen,position,taille,entitee.get_direction()) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                else:
                    agissant = entitee
            if agissant != None: #Enfin l'agissant (s'il y en a un)
                direction = agissant.get_direction()
                arme = agissant.inventaire.arme
                if arme != None:
                    joueur.controleur.get_entitee(arme).get_skin().dessine_toi(self.screen,position,taille,direction)
                agissant.get_skin().dessine_toi(self.screen,position,taille,direction)
                armure = agissant.inventaire.armure
                if armure != None:
                    joueur.controleur.get_entitee(armure).get_skin().dessine_toi(self.screen,position,taille,direction)
                bouclier = agissant.inventaire.bouclier
                if bouclier != None:
                    joueur.controleur.get_entitee(bouclier).get_skin().dessine_toi(self.screen,position,taille,direction)
                haume = agissant.inventaire.haume
                if haume != None:
                    joueur.controleur.get_entitee(haume).get_skin().dessine_toi(self.screen,position,taille,direction)
                if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif en-dessous des effets ?
                    SKIN_DIALOGUE.dessine_toi(self.screen,position,taille)
                for effet in agissant.effets:
                    if effet.affiche:
                        effet.get_skin().dessine_toi(self.screen,position,taille,direction)
                        if effet.phase == "affichage":
                            effet.phase = "terminé"
            #Rajouter des conditions d'observation

    def clear(self):
        self.screen = None

    def unclear(self,screen):
        self.screen = screen
