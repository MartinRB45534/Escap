from typing import Dict, List
from Jeu.Constantes import *
from Jeu.Entitees.Entitees import *
from Jeu.Labyrinthe import *
from Jeu.Effet.Magies import *
from Jeu.Esprit.Esprits import *
from Modifiers import *
import random


class Controleur():
    def __init__(self,parametres=None,screen=None):
        #print("Initialisation du controleur")
        self.labs:Dict[str,Labyrinthe] = {} #Un dictionnaire avec tous les labyrinthes, indéxés par leur identifiant dans les positions.
        #print("Labyrinthe : check")
        self.entitees:Dict[int,Entitee] = {}
        #print("Entitées : check")
        self.esprits:Dict[str,Esprit] = {}
        self.labs_courants:List[Labyrinthe] = []
        self.entitees_courantes:List[Entitee] = []
        self.esprits_courants:List[Esprit] = []
        self.pause = False
        self.nb_tours = 0
        self.phase = TOUR
        self.phases = [TOUR]
        if parametres == None:
            self.tour_par_seconde = 0
        else:
            self.tour_par_seconde = parametres["tours_par_seconde"]
            self.ajoute_entitee(Joueur(self,None,parametres,screen))

    def jeu(self,screen):

        self.esprits["joueur"] = Esprit_humain(2,self)

        autre = Alchimiste(self,("Étage 1 : test",1,0))
        self.ajoute_entitee(autre)
        self.esprits["alchimiste"] = Esprit_humain(autre.ID,self)

        chaudron = Chaudron_gobelin(("Étage 1 : test",1,3))
        self.ajoute_entitee(chaudron)

        peaux = [Peau_gobelin(("Étage 1 : test",1,2)),Peau_gobelin(("Étage 1 : test",1,4))]
        self.ajoute_entitees(peaux)

        gobel1 = Chef_gobelin(self,("Étage 1 : test",11,15),1)
        self.ajoute_entitee(gobel1)
        #self.esprits["gobel1"]=Esprit_simple("gobel1",[gobel1.ID],["humain"],self)

        gobel2 = Sentinelle_gobelin(self,("Étage 1 : test",2,6),1)
        self.ajoute_entitee(gobel2)
        self.esprits["gobel2"]=Esprit_simple("gobel2",[gobel1.ID,gobel2.ID],[],self)

        self.ajoute_entitee(Parchemin_vierge(("Étage 1 : test",1,5)))

        paterns1 = [Patern(("Étage 1 : test",0,0),20,20,[])]
        self.labs["Étage 1 : test"]=Labyrinthe("Étage 1 : test",20,20,("Étage 1 : test",0,0),paterns1,1,1,TERRE,1)

        self.entitees[2].position = ("Étage 1 : test",0,0)
        self.active_lab("Étage 1 : test")

    def experience5(self):
        #Une expérience sur les paramètres optimaux des esprits



        #L'équipe 1 est très mal disposée, avec les DPS/Tank à l'arrière et les shamans à l'avant
        gobel1 = Sentinelle_gobelin(self,("Labo",1,2),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Labo",3,0),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,("Labo",4,4),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,("Labo",2,1),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Labo",0,1),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Labo",3,6),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Labo",8,2),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,("Labo",9,7),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Labo",9,8),1)
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,("Labo",0,0),1)
        self.ajoute_entitee(boss)
        self.esprits["Equipe 1"]=Esprit_simple("Equipe 1",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,boss.ID],["gobelin"],self)


        #L'équipe 2 est disposée de façon optimale, avec les DPS/Tank à l'avant et les shamans à l'arrière
        gobel1 = Sentinelle_gobelin(self,("Labo",10,10),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Labo",10,11),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,("Labo",12,12),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,("Labo",11,10),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Labo",11,11),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Labo",13,13),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Labo",14,14),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,("Labo",19,19),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Labo",19,18),1)
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,("Labo",12,11),1)
        self.ajoute_entitee(boss)
        self.esprits["Equipe 2"]=Esprit_simple("Equipe 2",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,boss.ID],["gobelin"],self)



        #Le labyrinthe est partiellement fermé
        self.labs["Labo"]=Labyrinthe("Labo",20,20,("Labo",0,0),[],1,1,TERRE,0.5)
        self.active_lab("Labo")

    def check_exp5(self):
        mort1 = 0
        for ID in self.esprits["Equipe 1"].corps.keys():
            if self.get_entitee(ID).etat == "mort":
                mort1 += 1

        mort2 = 0
        for ID in self.esprits["Equipe 2"].corps.keys():
            if self.get_entitee(ID).etat == "mort":
                mort2 += 1

        if (mort1 == 10 and mort2 == 10) or self.nb_tours >= 200:
            return [mort1,mort2,self.nb_tours]
        if mort1 == 10:
            return [mort1,mort2,self.nb_tours]
        if mort2 == 10:
            return [mort1,mort2,self.nb_tours]
        return False

    def tuto(self,screen):

        self.esprits["joueur"] = Esprit_humain(2,self)

        #On crée le premier étage et son occupant :
        receptionniste = Receptionniste(self,("Étage 1 : couloir",14,0))
        self.ajoute_entitee(receptionniste)
        self.esprits["receptionniste"] = Esprit_humain(receptionniste.ID,self)
        paterns1 = [Patern(("Étage 1 : couloir",9,0),10,3,[("Étage 1 : couloir",0,1)],["clé_couloir"])]
        self.labs["Étage 1 : couloir"]=Labyrinthe("Étage 1 : couloir",19,3,("Étage 1 : couloir",0,0),paterns1,1,1,TERRE,1)

        #On crée le deuxième étage et son occupant :
        paume = Paume(self,("Étage 2 : labyrinthe",1,0))
        self.ajoute_entitee(paume)
        self.esprits["paume"] = Esprit_humain(paume.ID,self)
        paterns2 = [Patern(("Étage 2 : labyrinthe",0,0),5,5,[("Étage 2 : labyrinthe",4,1),("Étage 2 : labyrinthe",4,2),("Étage 2 : labyrinthe",4,3)]),
                    Patern(("Étage 2 : labyrinthe",5,5),5,5,[("Étage 2 : labyrinthe",0,1)],["Porte_centre_2"])]
        self.labs["Étage 2 : labyrinthe"]=Labyrinthe("Étage 2 : labyrinthe",15,15,("Étage 2 : labyrinthe",0,0),paterns2,1,1,TERRE,0.5)
        self.construit_escalier(("Étage 1 : couloir",18,1),("Étage 2 : labyrinthe",0,0),DROITE,GAUCHE)

        #On crée le troisième étage et son occupante :
        peureuse = Peureuse(self,("Étage 3 : combat",8,8))
        self.ajoute_entitee(peureuse)
        self.esprits["peureuse"] = Esprit_humain(peureuse.ID,self)
        cle1 = Cle(("Étage 3 : combat",12,13),["Porte_avant_prison_5"])
        self.ajoute_entitee(cle1)
        peureuse.inventaire.ajoute(cle1)
        gobel1 = Premier_monstre(self,("Étage 3 : combat",3,8),1)
        self.ajoute_entitee(gobel1)
        self.esprits["gobelins_combat"]=Esprit_simple("gobelins_combat",[gobel1.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns3 = [Patern(("Étage 3 : combat",4,4),7,7,[("Étage 3 : combat",0,4),("Étage 3 : combat",4,0),("Étage 3 : combat",0,0)]),
                    Patern(("Étage 3 : combat",3,3),3,3,[("Étage 3 : combat",0,0),("Étage 3 : combat",2,2)]),
                    Patern(("Étage 3 : combat",7,2),3,3,[("Étage 3 : combat",1,0),("Étage 3 : combat",1,2)]),
                    Patern(("Étage 3 : combat",8,8),3,3,[("Étage 3 : combat",0,0)]),
                    Patern(("Étage 3 : combat",0,3),1,8,[]),
                    Patern(("Étage 3 : combat",1,6),2,5,[("Étage 3 : combat",0,1),("Étage 3 : combat",0,2),("Étage 3 : combat",0,3),("Étage 3 : combat",1,1),("Étage 3 : combat",1,2),("Étage 3 : combat",1,3)],[],False),
                    Patern(("Étage 3 : combat",2,7),3,3,[("Étage 3 : combat",2,1),("Étage 3 : combat",0,1)])]
        self.labs["Étage 3 : combat"]=Labyrinthe("Étage 3 : combat",11,11,("Étage 3 : combat",0,0),paterns3,1,1,TERRE,0.4)
        self.construit_escalier(("Étage 2 : labyrinthe",1,5),("Étage 3 : combat",10,10),HAUT,BAS)

        #On crée le quatrième étage et ses occupants :
        codeur = Codeur(self,("Étage 4 : monstres",15,1))
        self.ajoute_entitee(codeur)
        self.esprits["codeur"] = Esprit_humain(codeur.ID,self)
        gobel1 = Troisieme_monstre(self,("Étage 4 : monstres",15,8),1) #Une sentinelle garde les abords
        self.ajoute_entitee(gobel1)
        gobel2 = Deuxieme_monstre(self,("Étage 4 : monstres",10,4),1) #Ainsi qu'un mage,
        self.ajoute_entitee(gobel2)
        self.esprits["gobelins_monstres"]=Esprit_simple("gobelins_monstres",[gobel1.ID,gobel2.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns4 = [Patern(("Étage 4 : monstres",4,0),10,2,[("Étage 4 : monstres",0,1)],[],False),
                    Patern(("Étage 4 : monstres",7,2),10,4,[("Étage 4 : monstres",0,2)],[],False),
                    Patern(("Étage 4 : monstres",14,0),3,3,[("Étage 4 : monstres",0,1)]),
                    Patern(("Étage 4 : monstres",0,7),4,3,[("Étage 4 : monstres",3,1)],["Porte_coin_4"])]
        self.labs["Étage 4 : monstres"]=Labyrinthe("Étage 4 : monstres",17,10,("Étage 4 : monstres",0,0),paterns4,1,1,TERRE,0.35)
        self.construit_escalier(("Étage 3 : combat",0,3),("Étage 4 : monstres",16,5),GAUCHE,DROITE)

        #On crée le cinquième étage et ses occupants :
        encombrant = Encombrant(self,("Étage 5 : portes",2,3))
        self.ajoute_entitee(encombrant)
        self.esprits["encombrant"] = Esprit_humain(encombrant.ID,self)
        cle1 = Cle(("Étage 5 : portes",2,3),["Porte_sortie_encombrant_5"])
        self.ajoute_entitee(cle1)
        encombrant.inventaire.ajoute(cle1)
        passepartout1 = Cle(("Étage 5 : portes",5,5),["Porte_première_cellule_5","Porte_double_cellule_première_5","Porte_grande_cellule_5","Porte_cellule_biscornue_5","Porte_entree_encombrant_5"])
        self.ajoute_entitee(passepartout1)
        cle2 = Cle(("Étage 5 : portes",1,9),["Porte_couloir_5"])
        self.ajoute_entitee(cle2)
        cle3 = Cle(("Étage 5 : portes",1,2),["Porte_fin_couloir_5"])
        self.ajoute_entitee(cle3)
        cle5 = Cle(("Étage 5 : portes",3,6),["Porte_armurerie_6"])
        self.ajoute_entitee(cle5)
        cle6 = Cle(("Étage 5 : portes",0,6),["Porte_quatrième_armurerie_9"])
        self.ajoute_entitee(cle6)
        cle7 = Cle(("Étage 5 : portes",0,12),["Porte_annexe_droite_7"])
        self.ajoute_entitee(cle7)
        cle8 = Cle(("Étage 5 : portes",0,6),["Porte_troisième_armurerie_9"])
        self.ajoute_entitee(cle8)
        cle9 = Cle(("Étage 5 : portes",9,13),["Porte_anti_anti_chambre_8"])
        self.ajoute_entitee(cle9)
        gobel1 = Sentinelle_gobelin(self,("Étage 5 : portes",6,10),1) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Étage 5 : portes",5,5),1) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel2)
        gobel2.inventaire.ajoute(passepartout1)
        gobel3 = Guerrier_gobelin(self,("Étage 5 : portes",8,1),1) #Un renégat mis à l'isolement pour le mater, ou un piège diabolique dirigé contre le joueur ?
        self.ajoute_entitee(gobel3)
        slime = Slime(self,("Étage 5 : portes",8,7),1) #Un slime ! Est-ce que les gobelins ont pris soin de l'affaiblir ?
        self.ajoute_entitee(slime)
        ombriul = Ombriul(self,("Étage 5 : portes",5,7),1) #Un prisonnier de guerre
        self.ajoute_entitee(ombriul)
        #Rajouter quelques cadavres pour le nécromancien
        self.esprits["gobelins_portes"]=Esprit_simple("gobelins_portes",[gobel1.ID,gobel2.ID,gobel3.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        self.esprits["ombriul_captif"]=Esprit_simple("ombriul_captif",[ombriul.ID],["humain"],self)
        esprit_slime = Esprit_slime(slime.ID,self)
        self.esprits[esprit_slime.nom]=esprit_slime #Les esprits des slimes sont presque aussi compliqués que ceux des humains, les ruptures en moins.
        paterns5 = [Patern(("Étage 5 : portes",0,0),10,14,[]),
                    Patern(("Étage 5 : portes",7,11),3,3,[]),
                    Patern(("Étage 5 : portes",0,5),5,3,[]),
                    Patern(("Étage 5 : portes",0,1),5,4,[("Étage 5 : portes",1,0),("Étage 5 : portes",4,2)],["Porte_sortie_encombrant_5","Porte_entree_encombrant_5"]),
                    Patern(("Étage 5 : portes",0,8),3,3,[("Étage 5 : portes",1,0),("Étage 5 : portes",2,1)],["Porte_première_cellule_5","Porte_couloir_5"]),
                    Patern(("Étage 5 : portes",0,11),4,3,[("Étage 5 : portes",2,0)],["Porte_avant_prison_5"]),
                    Patern(("Étage 5 : portes",4,11),3,3,[("Étage 5 : portes",1,0),("Étage 5 : portes",2,1)],["Porte_double_cellule_première_5","Porte_double_cellule_deuxième_5"]),
                    Patern(("Étage 5 : portes",6,0),4,5,[("Étage 5 : portes",2,4)],["Porte_grande_cellule_5"]),
                    Patern(("Étage 5 : portes",5,6),4,4,[("Étage 5 : portes",3,2)],["Porte_cellule_biscornue_5"]),
                    Patern(("Étage 5 : portes",3,7),2,2,[]),
                    Patern(("Étage 5 : portes",4,8),2,2,[("Étage 5 : portes",0,0)]),
                    Patern(("Étage 5 : portes",5,6),2,2,[("Étage 5 : portes",0,1)])]
        self.labs["Étage 5 : portes"]=Labyrinthe("Étage 5 : portes",10,14,("Étage 5 : portes",0,0),paterns5)
        self.labs["Étage 5 : portes"].matrice_cases[6][5].murs[BAS].cree_porte(1,"Porte_cellule_plus_biscornue_5")
        self.labs["Étage 5 : portes"].matrice_cases[6][6].murs[HAUT].cree_porte(1,"Porte_cellule_plus_biscornue_5")
        self.labs["Étage 5 : portes"].matrice_cases[4][0].murs[DROITE].cree_porte(1,"Porte_fin_couloir_5")
        self.labs["Étage 5 : portes"].matrice_cases[5][0].murs[GAUCHE].cree_porte(1,"Porte_fin_couloir_5")
        self.labs["Étage 5 : portes"].matrice_cases[2][11].murs[HAUT].cree_porte(1,"Porte_avant_prison_5",Premiere_porte)
        self.labs["Étage 5 : portes"].matrice_cases[4][3].murs[DROITE].effets[1].auto = True
        self.labs["Étage 5 : portes"].matrice_cases[5][3].murs[GAUCHE].effets[1].auto = True
        self.construit_escalier(("Étage 4 : monstres",16,7),("Étage 5 : portes",0,13),DROITE,GAUCHE,Premiere_marche)

        #On crée le sixième étage et son occupant :
        #Nouvelle version :
        alchimiste = Alchimiste(self,("Étage 6 : potions",13,1))
        self.ajoute_entitee(alchimiste)
        self.esprits["alchimiste"] = Esprit_humain(alchimiste.ID,self)

        chaudrons_6 = [Chaudron_gobelin(("Étage 6 : potions",12,4)),
                       Chaudron_gobelin(("Étage 6 : potions",14,8))]
        self.ajoute_entitees(chaudrons_6)

        cles_6 = [Cle(("Étage 6 : potions",4,1),["Porte_cuisine"]), #(0)
                  Cle(("Étage 6 : potions",11,6),["Première_porte_potions"]), #(1)
                  Cle(("Étage 6 : potions",13,10),["Porte_inutile_potion"]), #(2)
                  Cle(("Étage 6 : potions",4,4),["Deuxième_porte_potions"]), #(3)
                  Cle(("Étage 6 : potions",3,9),["Troisième_porte_potions"]), #(4)
                  Cle(("Étage 6 : potions",0,11),["Porte_double_cellule_deuxième_5"]),
                  Cle(("Étage 6 : potions",11,10),["Porte_salle_commune_7"])]
        self.ajoute_entitees(cles_6)

        consomables_6 = [Parchemin_protection(("Étage 6 : potions",2,13)),
                         Potion_force(("Étage 6 : potions",1,13))]
        self.ajoute_entitees(consomables_6)

        ingredients_6 = [Peau_gobelin(("Étage 6 : potions",12,6)),
                         Dent_gobelin(("Étage 6 : potions",14,8)),
                         Pierre_solide(("Étage 6 : potions",9,1)),
                         Hypokute(("Étage 6 : potions",6,7))]
        self.ajoute_entitees(ingredients_6)

        gobel1 = Gobelin(self,("Étage 6 : potions",11,6),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Mage_gobelin(self,("Étage 6 : potions",13,10),1)
        self.ajoute_entitee(gobel2)
        gobel2.inventaire.ajoute(cles_6[2])
        gobel3 = Sentinelle_gobelin(self,("Étage 6 : potions",4,4),1)
        self.ajoute_entitee(gobel3)
        gobel3.inventaire.ajoute(cles_6[3])
        gobel4 = Mage_gobelin(self,("Étage 6 : potions",6,6),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Étage 6 : potions",4,10),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Guerrier_gobelin(self,("Étage 6 : potions",12,4),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Guerrier_gobelin(self,("Étage 6 : potions",14,4),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,("Étage 6 : potions",13,7),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Étage 6 : potions",10,9),1)
        self.ajoute_entitee(gobel9)
        self.esprits["gobelins_potions"]=Esprit_simple("gobelins_potions",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)

        paterns6 = [Patern(("Étage 6 : potions",9,3),6,8,[("Étage 6 : potions",0,7)]), #La cuisine, avec le shaman et les derniers gobelins (0)
                    Patern(("Étage 6 : potions",6,0),3,2,[]), #(5)
                    Patern(("Étage 6 : potions",3,0),3,2,[]), #(12)
                    Patern(("Étage 6 : potions",0,3),2,3,[]), #(10)
                    Patern(("Étage 6 : potions",0,0),3,3,[("Étage 6 : potions",1,2),("Étage 6 : potions",2,1)],["Deuxième_porte_potions","Troisième_porte_potions"]), #(11)
                    Patern(("Étage 6 : potions",3,7),3,2,[]), #(4)
                    Patern(("Étage 6 : potions",0,6),3,3,[("Étage 6 : potions",2,1)],["Première_porte_potions"]), #(3)
                    Patern(("Étage 6 : potions",0,9),3,3,[]), #(8)
                    Patern(("Étage 6 : potions",3,9),3,3,[("Étage 6 : potions",0,1)],["Porte_inutile_potion"]), #(9)
                    Patern(("Étage 6 : potions",2,2),5,5,[]), #(7)
                    Patern(("Étage 6 : potions",12,9),3,3,[]), #(6)
                    Patern(("Étage 6 : potions",11,0),4,4,[("Étage 6 : potions",2,3)],["Porte_cuisine"]), #(1)
                    Patern(("Étage 6 : potions",8,3),4,4,[]), #(2)
                    Patern(("Étage 6 : potions",0,12),5,3,[("Étage 6 : potions",4,1)],["Porte_armurerie_6"])]
        self.labs["Étage 6 : potions"]=Labyrinthe("Étage 6 : potions",15,15,("Étage 6 : potions",14,14),paterns6,1,1,TERRE,0.2)

        self.set_teleport(("Étage 6 : potions",11,2),("Étage 6 : potions",8,3),GAUCHE,HAUT,Premier_portail) # 1,2
        self.set_teleport(("Étage 6 : potions",13,0),("Étage 6 : potions",1,6),HAUT,DROITE,Premier_portail) # 1,3
        self.set_teleport(("Étage 6 : potions",3,8),("Étage 6 : potions",6,0),BAS,GAUCHE) # 4,5
        self.set_teleport(("Étage 6 : potions",4,8),("Étage 6 : potions",13,9),BAS,HAUT) # 4,6
        self.set_teleport(("Étage 6 : potions",5,8),("Étage 6 : potions",4,11),BAS,BAS) # 4,9
        self.set_teleport(("Étage 6 : potions",12,10),("Étage 6 : potions",7,0),GAUCHE,HAUT) # 6,5
        self.set_teleport(("Étage 6 : potions",13,11),("Étage 6 : potions",4,2),BAS,HAUT) # 6,7
        self.set_teleport(("Étage 6 : potions",2,2),("Étage 6 : potions",6,1),GAUCHE,BAS) # 7,5
        self.set_teleport(("Étage 6 : potions",6,5),("Étage 6 : potions",0,11),DROITE,BAS) # 7,8
        self.set_teleport(("Étage 6 : potions",2,9),("Étage 6 : potions",8,1),DROITE,BAS) # 8,5
        self.set_teleport(("Étage 6 : potions",5,11),("Étage 6 : potions",8,0),BAS,DROITE) # 9,5
        self.set_teleport(("Étage 6 : potions",5,10),("Étage 6 : potions",0,4),DROITE,GAUCHE) # 9,10

        self.construit_escalier(("Étage 5 : portes",0,0),("Étage 6 : potions",14,0),GAUCHE,DROITE)

        #On crée le septième étage et son occupante :
        peste = Peste(self,("Étage 7 : meutes",2,0))
        self.ajoute_entitee(peste)
        self.esprits["peste"] = Esprit_humain(peste.ID,self)
        cle1 = Cle(("Étage 7 : meutes",14,6),["Porte_sixième_armurerie_9"])
        self.ajoute_entitee(cle1)
        gobel1 = Guerrier_gobelin(self,("Étage 7 : meutes",4,3),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Guerrier_gobelin(self,("Étage 7 : meutes",10,3),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,("Étage 7 : meutes",6,4),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Gobelin(self,("Étage 7 : meutes",4,4),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Gobelin(self,("Étage 7 : meutes",10,4),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Gobelin(self,("Étage 7 : meutes",9,4),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Étage 7 : meutes",5,5),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,("Étage 7 : meutes",7,5),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Étage 7 : meutes",4,5),1)
        self.ajoute_entitee(gobel9)
        gobel10 = Shaman_gobelin(self,("Étage 7 : meutes",10,5),1)
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_meutes"]=Esprit_simple("gobelins_meutes",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,gobel10.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns7 = [Patern(("Étage 7 : meutes",0,0),15,2,[]),
                    Patern(("Étage 7 : meutes",0,2),4,3,[("Étage 7 : meutes",1,0),("Étage 7 : meutes",2,2)],["Porte_annexe_gauche_7"]),
                    Patern(("Étage 7 : meutes",4,2),7,4,[("Étage 7 : meutes",3,0)],["Porte_salle_commune_7"]),
                    Patern(("Étage 7 : meutes",11,2),4,3,[("Étage 7 : meutes",2,0),("Étage 7 : meutes",1,2)],["Porte_annexe_droite_7"])]
        self.labs["Étage 7 : meutes"]=Labyrinthe("Étage 7 : meutes",15,10,("Étage 7 : meutes",0,9),paterns7,1,1,TERRE,0.3)
        self.construit_escalier(("Étage 6 : potions",12,14),("Étage 7 : meutes",7,0),BAS,HAUT)

        #On crée le huitième étage et son occupante :
        bombe_atomique = Bombe_atomique(self,("Étage 8 : magie",8,7))
        self.ajoute_entitee(bombe_atomique)
        self.esprits["bombe_atomique"] = Esprit_humain(bombe_atomique.ID,self)
        cle1 = Cle(("Étage 8 : magie",0,7),["Porte_deuxième_armurerie_9"])
        self.ajoute_entitee(cle1)
        cle2 = Cle(("Étage 8 : magie",12,8),["Porte_anti_chambre_8"])
        self.ajoute_entitee(cle3)
        cle3 = Cle(("Étage 8 : magie",3,2),["Porte_annexe_gauche_7"])
        self.ajoute_entitee(cle2)
        gobel1 = Mage_gobelin(self,("Étage 8 : magie",1,1),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Mage_gobelin(self,("Étage 8 : magie",1,3),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Mage_gobelin(self,("Étage 8 : magie",2,0),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Mage_gobelin(self,("Étage 8 : magie",4,3),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Mage_gobelin(self,("Étage 8 : magie",5,7),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Étage 8 : magie",6,2),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Étage 8 : magie",8,0),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,("Étage 8 : magie",9,2),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Mage_gobelin(self,("Étage 8 : magie",5,5),1)
        self.ajoute_entitee(gobel9)
        gobel10 = Mage_gobelin(self,("Étage 8 : magie",10,9),1)
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_magie"]=Esprit_simple("gobelins_magie",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,gobel10.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns8 = [Patern(("Étage 8 : magie",10,0),5,4,[("Étage 8 : magie",0,1)]),
                    Patern(("Étage 8 : magie",7,6),4,3,[("Étage 8 : magie",0,1)],["Porte_anti_chambre_8"]),
                    Patern(("Étage 8 : magie",11,4),4,6,[("Étage 8 : magie",2,0),("Étage 8 : magie",0,4)],["Porte_sas_8","Porte_anti_anti_chambre_8"])]
        self.labs["Étage 8 : magie"]=Labyrinthe("Étage 8 : magie",15,10,("Étage 8 : magie",0,0),paterns8,1,1,TERRE,0.4)
        self.construit_escalier(("Étage 7 : meutes",0,9),("Étage 8 : magie",14,7),GAUCHE,DROITE) #/!\ Rajouter un parchemin

        #On crée le neuvième étage et son occupant :
        marchand = Marchand(self,("Étage 9 : équippement",6,2))
        self.ajoute_entitee(marchand)
        cle1 = Cle(("Étage 9 : équippement",2,0),["Porte_première_armurerie_9"])
        self.ajoute_entitee(cle1)
        marchand.inventaire.ajoute(cle1)
        self.esprits["marchand"] = Esprit_humain(marchand.ID,self)
        cle2 = Cle(("Étage 9 : équippement",38,8),["Porte_cinquième_armurerie_9"])
        self.ajoute_entitee(cle2)
        cle1 = Cle(("Étage 9 : équippement",0,1),["Porte_sas_8"])
        self.ajoute_entitee(cle1)
        #On crée aussi quelques items :
        #Pas d'item dans l'armurerie où est le marchand, il l'a déjà dévalisée !
        #Dans la deuxième armurerie, une armure :
        armure = Armure_sentinelle_gobelin(("Étage 9 : équippement",5,9),1)
        self.ajoute_entitee(armure)
        #Dans la troisième, une lance :
        lance = Lance_de_gobelin(("Étage 9 : équippement",16,3),1)
        self.ajoute_entitee(lance)
        #Dans la quatrième, huit anneaux :
        anneau_1 = Anneau_magique_gobelin(("Étage 9 : équippement",22,7),1)
        self.ajoute_entitee(anneau_1)
        anneau_2 = Anneau_magique_gobelin(("Étage 9 : équippement",22,9),1)
        self.ajoute_entitee(anneau_2)
        anneau_3 = Anneau_soin_gobelin(("Étage 9 : équippement",20,7),1)
        self.ajoute_entitee(anneau_3)
        anneau_4 = Anneau_soin_gobelin(("Étage 9 : équippement",20,9),1)
        self.ajoute_entitee(anneau_4)
        anneau_5 = Anneau_vitesse_gobelin(("Étage 9 : équippement",18,7),1)
        self.ajoute_entitee(anneau_5)
        anneau_6 = Anneau_vitesse_gobelin(("Étage 9 : équippement",18,9),1)
        self.ajoute_entitee(anneau_6)
        anneau_7 = Anneau_terrestre_gobelin(("Étage 9 : équippement",16,7),1)
        self.ajoute_entitee(anneau_7)
        anneau_8 = Sceau_roi_gobelin(("Étage 9 : équippement",15,9),1)
        self.ajoute_entitee(anneau_8)
        #/!\ Rajouter un cadavre de roi gobelin et une couronne
        #Dans la cinquième, un haume :
        haume = Haume_de_gobelin(("Étage 9 : équippement",25,1),1)
        self.ajoute_entitee(haume)
        #Dans la sixième, une épée :
        epee = Epee_de_gobelin(("Étage 9 : équippement",39,0),1)
        self.ajoute_entitee(epee)
        gobel1 = Sentinelle_gobelin(self,("Étage 9 : équippement",15,0),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Étage 9 : équippement",15,6),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Guerrier_gobelin(self,("Étage 9 : équippement",17,2),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,("Étage 9 : équippement",17,6),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Étage 9 : équippement",19,4),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Étage 9 : équippement",20,1),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Étage 9 : équippement",17,3),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,("Étage 9 : équippement",18,6),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Étage 9 : équippement",21,3),1)
        self.ajoute_entitee(gobel9)
        gobel10 = Shaman_gobelin(self,("Étage 9 : équippement",26,9),1)
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_equippement"]=Esprit_simple("gobelins_equippement",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,gobel10.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns9 = [Patern(("Étage 9 : équippement",0,0),7,4,[("Étage 9 : équippement",5,3)],["Porte_première_armurerie_9"]),
                    Patern(("Étage 9 : équippement",3,5),4,5,[("Étage 9 : équippement",2,0)],["Porte_deuxième_armurerie_9"]),
                    Patern(("Étage 9 : équippement",11,2),6,4,[("Étage 9 : équippement",0,2)],["Porte_troisième_armurerie_9"]),
                    Patern(("Étage 9 : équippement",15,7),10,3,[("Étage 9 : équippement",8,0)],["Porte_quatrième_armurerie_9"]),
                    Patern(("Étage 9 : équippement",28,0),12,10,[("Étage 9 : équippement",0,0)],[],False),
                    Patern(("Étage 9 : équippement",23,1),8,4,[("Étage 9 : équippement",3,0)],["Porte_cinquième_armurerie_9"]),
                    Patern(("Étage 9 : équippement",36,0),4,4,[("Étage 9 : équippement",1,3)],["Porte_sixième_armurerie_9"]),
                    ]
        self.labs["Étage 9 : équippement"]=Labyrinthe("Étage 9 : équippement",40,10,("Étage 9 : équippement",0,0),paterns9,1,1,TERRE,0.3)
        self.labs["Étage 9 : équippement"].matrice_cases[5][3].murs[BAS].effets[1].ferme = False
        self.labs["Étage 9 : équippement"].matrice_cases[5][4].murs[HAUT].effets[1].ferme = False
        self.construit_escalier(("Étage 8 : magie",13,0),("Étage 9 : équippement",1,9),HAUT,BAS) #/!\ Rajouter les ennemis !

        #On crée le dixième étage
        gobel1 = Sentinelle_gobelin(self,("Étage 10 : Boss",5,5),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Étage 10 : Boss",5,13),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,("Étage 10 : Boss",7,9),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,("Étage 10 : Boss",5,0),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Étage 10 : Boss",5,18),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Étage 10 : Boss",8,6),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Étage 10 : Boss",8,12),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,("Étage 10 : Boss",9,0),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Étage 10 : Boss",9,18),1)
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,("Étage 10 : Boss",9,9),1)
        self.ajoute_entitee(boss)
        self.esprits["gobelins_boss"]=Esprit_simple("gobelins_boss",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,boss.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns10 = [Patern(("Étage 10 : Boss",0,0),25,19,[],[]),
                     Patern(("Étage 10 : Boss",10,0),10,19,[("Étage 10 : Boss",0,9)],["Porte_boss_10"],1,1,FEU),
                     Patern(("Étage 10 : Boss",20,7),3,5,[("Étage 10 : Boss",0,2)],["Porte_dérobée_10"])]
        self.labs["Étage 10 : Boss"]=Labyrinthe("Étage 10 : Boss",25,19,("Étage 10 : Boss",0,0),paterns10,1,1,TERRE,0.1)
        self.construit_escalier(("Étage 9 : équippement",39,4),("Étage 10 : Boss",0,9),DROITE,GAUCHE) #/!\ Rajouter les ennemis !

        #On lance la cinématique :
        #À rajouter
        #Et on active le lab du joueur
        self.entitees[2].position = ("Étage 1 : couloir",13,0)
        self.active_lab(self.entitees[2].position[0])

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

    def cree_agissants(self,classe,niveau,position,largeur,hauteur,nombre):
        poss = [(position[0],position[1]+i,position[2]+j) for i in range(largeur) for j in range(hauteur)] #Les positions possibles
        #Rajouter une  vérification pour ne prendre que les cases vides ?
        agissants = []
        for i in range(nombre):
            if poss != []:
                j = random.randrange(len(poss))
                pos = poss.pop(j) #On choisit aléatoirement la position de l'agissant et on ne veut pas la réutiliser
                agissant = classe(self,pos,niveau)
                self.ajoute_entitee(agissant)
                agissants.append(agissant.ID)
        return agissants

    def toogle_pause(self):
        self.pause = not(self.pause)

    def set_phase(self,phase):
        if phase not in self.phases : #On ne veut pas avoir deux fois la même phase !
            self.phases.append(phase) #La dernière phase est toujours la phase active !
        self.phase = phase # /!\ Rajouter des conditions ici ! Certaines phases ne peuvent pas être interrompues par d'autres
        if self.phase == TOUR:
            pygame.key.set_repeat()
        else:
            pygame.key.set_repeat(400,200)

    def unset_phase(self,phase):
        if phase in self.phases :
            self.phases.remove(phase)
        self.phase = self.phases[-1]
        if self.phase == TOUR:
            pygame.key.set_repeat()
        else:
            pygame.key.set_repeat(400,200)

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

    def set_teleport(self,pos_dep,pos_arr,dir_dep,dir_arr,portail=None):
        case_dep = self.get_case(pos_dep)
        case_arr = self.get_case(pos_arr)
        case_dep.repoussante = True
        case_arr.repoussante = True
        mur_dep = case_dep.get_mur_dir(dir_dep)
        mur_arr = case_arr.get_mur_dir(dir_arr)
        mur_dep.detruit()
        mur_arr.detruit()
        mur_dep.set_cible(pos_arr,True,portail)
        mur_arr.set_cible(pos_dep,True,portail)

    def construit_escalier(self,pos_dep,pos_arr,dir_dep,dir_arr,escalier=None):
        case_dep = self.get_case(pos_dep)
        case_arr = self.get_case(pos_arr)
        case_dep.repoussante = True
        case_arr.repoussante = True
        mur_dep = case_dep.get_mur_dir(dir_dep)
        mur_arr = case_arr.get_mur_dir(dir_arr)
        mur_dep.detruit()
        mur_arr.detruit()
        mur_dep.set_escalier(pos_arr,HAUT,escalier) #Par convention, la première case est en bas
        mur_arr.set_escalier(pos_dep,BAS,escalier)

    def get_case(self,position):
        return self.get_lab(position[0]).get_case(position)

    def get_trajet(self,pos,direction):
        return self.labs[pos[0]].matrice_cases[pos[1]][pos[2]].murs[direction].get_trajet()

    def make_vue(self,agissant):
        position = agissant.get_position()
        num_lab = position[0]
        labyrinthe = self.get_lab(num_lab)
        vue = labyrinthe.get_vue(agissant)
        for occupant in self.entitees_courantes:
            pos = self.get_entitee(occupant).position
            if pos != None and pos[0] == num_lab:
                if vue[pos[1]][pos[2]][1] > 0:
                    vue[pos[1]][pos[2]][6].append(occupant)
        agissant.vue = vue

    # Les fonctions qui suivent sont utilisées dans diverses situations pour trouver les entitées situées sur une case
    # On distingue plusieurs cas :
    # Déplacement (on cherche les entitées qui occupent l'espace, auxquelles on ne peut pas superposer d'autres entitées semblables)
    # Combat (on cherche les entitées qui peuvent subir des dégats, qui ont des PVs)
    # Ramassage (on cherche les entitées qui peuvent être stockées dans un inventaire)
    # Effets divers (auras, soins, etc. (comme pour le combat))
    # Interactions (dialogues, éléments de décors)
    # Pour les déplacements, on veut donc les Non_superposable
    # Pour les combats, les agissants
    # Pour les ramassages, les items (y compris les agissants morts (les cadavres))
    # Pour les interactions, les interactifs (à créer)
    # Pour les effets divers, le plus souvent les agissants, parfois les movibles (à créer)

    def est_item(self,entitee):
        return issubclass(self.get_entitee(entitee).get_classe(),Item)

    def trouve_classe(self,position,classe):
        entitees = []
        for ID_entitee in self.entitees.keys():
            entitee = self.get_entitee(ID_entitee)
            if entitee.get_position() == position and issubclass(entitee.get_classe(),classe):
                entitees.append(ID_entitee)
        return entitees

    def trouve_items(self,position):
        return self.trouve_classe(position,Item)

    def trouve_non_superposables(self,position):
        return self.trouve_classe(position,Non_superposable)

    def trouve_interactifs(self,position):
        return self.trouve_classe(position,Interactif)

    def trouve_mobiles(self,position):
        return self.trouve_classe(position,Mobile)

    def trouve_agissants(self,position):
        return self.trouve_classe(position,Agissant)

    def trouve_occupants(self,position):
        occupants = []
        for entitee in self.entitees.keys():
            if self.get_entitee(entitee).get_position() == position:
                occupants.append(entitee)
        return occupants

    def trouve_classe_courants(self,position,classe):
        entitees = []
        for ID_entitee in self.entitees_courantes:
            entitee = self.get_entitee(ID_entitee)
            if entitee.get_position() == position and issubclass(entitee.get_classe(),classe):
                entitees.append(ID_entitee)
        return entitees

    def trouve_items_courants(self,position):
        return self.trouve_classe_courants(position,Item)

    def trouve_non_superposables_courants(self,position):
        return self.trouve_classe_courants(position,Non_superposable)

    def trouve_interactifs_courants(self,position):
        return self.trouve_classe_courants(position,Interactif)

    def trouve_mobiles_courants(self,position):
        return self.trouve_classe_courants(position,Mobile)

    def trouve_agissants_courants(self,position):
        return self.trouve_classe_courants(position,Agissant)

    def trouve_occupants_courants(self,position):
        occupants = []
        for entitee in self.entitees_courantes:
            if self.get_entitee(entitee).get_position() == position:
                occupants.append(entitee)
        return occupants

    def fait_agir(self,agissant):
        agissant.statut = ""
        if agissant.ID == 2:
            agissant.nouvel_ordre = False
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
                        affichage.message(f"Tu as volé avec succès un {item} à {possesseur} !")
                else :
                    possesseur.persecuteurs.append(agissant.ID)
                #refaire les autres vols sur le même modèle /!\



            elif type_skill == Skill_ramasse:
                items = self.trouve_items_courants(agissant.get_position())
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
                attaque = Attaque(ID,degats,TERRE,"contact",portee)

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
                    attaque = Attaque(ID,degats,element,"contact",portee,forme,direction)

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

                    effet = Protection_general(duree,bouclier) #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres effets

                    for effet_prec in agissant.effets :
                        if isinstance(effet_prec,Protection_general):
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



            elif type_skill in [Skill_deplacement,Skill_course,Skanda,Lesser_Skanda]:
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
                cadavre = self.get_entitee(agissant.cible)
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
                if magie != None:
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
                else:
                    print("On ne peut pas utiliser une magie que l'on a pas !")
                    print(nom_magie,agissant)



            elif type_skill in [Divine_Thread_Weaving,Lesser_Divine_Thread_Weaving] :
                action = agissant.action
                latence,item = skill.utilise(action)
                agissant.add_latence(latence)
                self.items.append(item)



            elif type_skill in [Scythe,Lesser_Scythe] :
                perce,element,taux = skill.utilise()
                attaque = Attaque(agissant.ID,agissant.force*taux,element,"contact",1,"R__T_Pb",agissant.direction,"piercing",perce)
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
                items = self.trouve_items_courants(agissant.get_position())
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
                if agissant.peut_payer(20): #Insérer le cout ici d'une façon ou d'une autre /!\
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

    def select_cible_parchemin(self,magie,agissant):
        if random.random() < agissant.talent :
            magie.cible = agissant.cible_magie_parchemin
        
    def select_direction_parchemin(self,magie,agissant):
        if random.random() < agissant.talent :
            magie.direction = agissant.dir_magie_parchemin

    def select_cout_parchemin(self,magie,agissant):
        magie.cout_pm = agissant.cout_magie_parchemin

    def get_cibles_potentielles_agissants(self,magie,joueur):
        cibles_potentielles = []
        for etage in self.esprits["joueur"].vue.values():
            for colonne in etage:
                for case in colonne:
                    for ID_entitee in case[5]:
                        entitee = self.get_entitee(ID_entitee)
                        if issubclass(entitee.get_classe(),Agissant):
                            cibles_potentielles.append(entitee)
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
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
        for etage in self.esprits["joueur"].vue.values():
            for colonne in etage:
                for case in colonne:
                    for ID_entitee in case[5]:
                        entitee = self.get_entitee(ID_entitee)
                        if issubclass(entitee.get_classe(),Item):
                            cibles_potentielles.append(entitee)
                        else:
                            cibles_potentielles += entitee.inventaire.get_items() #/!\ Rajouter une condition d'observation ! Mais ne pas l'appliquer à soi-même !
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
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
        for etage in self.esprits["joueur"].vue.values():
            for colonne in etage:
                for case in colonne:
                    cibles_potentielles.append(case[0])
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
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

    def get_especes(self,ID):
        entitee = self.get_entitee(ID)
        if issubclass(entitee.get_classe(),Agissant):
            return entitee.especes
        else:
            return []

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
                if isinstance(entitee,Joueur):
                    agissants.insert(0,entitee)
                    esprit = entitee.get_esprit()
                    if esprit != None:
                        if not esprit in noms_esprits:
                            noms_esprits.append(esprit)
                elif entitee.etat == "vivant":
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
                elif entitee.etat == "suspens":
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
                if issubclass(victime.get_classe(),Agissant):
                    position_v = victime.get_position()
                    obstacles.append(position_v)
        labyrinthe.attaque(position,portee,propagation,direction,obstacles)
        victimes = []
        for victime_possible in victimes_possibles :
            victime = self.get_entitee(victime_possible)
            if issubclass(victime.get_classe(),Agissant):
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
            for ID_obstacle in obstacles:
                obstacle = self.get_entitee(ID_obstacle)
                if issubclass(obstacle.get_classe(),Non_superposable):
                    pos_obstacles.append(obstacle.get_position())
        elif traverse == "alliés":
            obstacles_possibles = self.get_entitees_etage(position[0])
            nom_esprit = self.get_entitee(responsable).esprit
            if nom_esprit != None:
                for ID_obstacle in obstacles_possibles:
                    obstacle = self.get_entitee(ID_obstacle)
                    if issubclass(obstacle.get_classe(),Non_superposable):
                        if issubclass(obstacle.get_classe(),Agissant):
                            if obstacle.esprit != nom_esprit:
                                pos_obstacles.append(obstacle.get_position())
                        else:
                            pos_obstacles.append(obstacle.get_position())
        elif traverse == "ennemis":
            obstacles_possibles = self.get_entitees_etage(position[0])
            nom_esprit = self.get_entitee(responsable).esprit
            if nom_esprit != None:
                for ID_obstacle in obstacles_possibles:
                    obstacle = self.get_entitee(ID_obstacle)
                    if issubclass(obstacle.get_classe(),Non_superposable):
                        if issubclass(obstacle.get_classe(),Agissant):
                            if obstacle.esprit == nom_esprit:
                                pos_obstacles.append(obstacle.get_position())
                        else:
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
            self.entitees[ID_entitee].clear()