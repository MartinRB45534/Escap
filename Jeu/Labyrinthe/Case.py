from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Entitee.Entitees import *

# from Jeu.Constantes import *
from Jeu.Labyrinthe.Mur import *
from Jeu.Effet.Auras import *
from Jeu.Labyrinthe.Structure_spatiale.Direction import *
from Jeu.Labyrinthe.Vue import Representation_case

class Case:
    def __init__(self,position:Position,niveau = 1,element = TERRE,effets:List[Effet] = [],opacite = 1):
        # Par défaut, pas de murs.
        self.position = position
        self.murs = [Mur(position+direction,niveau) for direction in DIRECTIONS]
        self.opacite = opacite
        self.opacite_bonus = 0
        self.niveau = niveau
        self.element = element
        self.clarte = 0
        self.code = 0
        self.repoussante = False
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

    def __getitem__(self,key:Direction) -> Mur:
        return self.murs[key]

    def __setitem__(self,key:Direction,value:Mur):
        self.murs[key] = value

    #Découvrons le déroulé d'un tour, avec case-chan :

    def debut_tour(self):
        #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! On commence par activer les effets réguliers :
        for i in range(len(self.effets)-1,-1,-1) :
            effet = self.effets[i]
            if isinstance(effet,On_debut_tour):
                effet.execute(self) #On exécute divers effets
            if isinstance(effet,Time_limited):
                effet.wait()
            if effet.phase == "affichage":
                self.effets.remove(effet)
                

    def pseudo_debut_tour(self):
        self.code = 0
        priorite_max = 0
        IDmax = 0
        auras = {}

        for effet in self.effets:
            if isinstance(effet,Aura_elementale):
                ID = effet.responsable
                if ID in auras : # On a déjà une aura de ce type
                    auras[ID].append(effet)
                else:
                    auras[ID]=[effet]
                prio = effet.priorite
                if prio > priorite_max : # On a un nouveau gagnant !
                    IDmax = ID
                    priorite_max = prio

        for aura in auras[IDmax]:
            if isinstance(aura,(Terre,Terre_permanente)):
                self.code += 1
            elif isinstance(aura,(Feu,Feu_permanent)):
                self.code += 2
            elif isinstance(aura,(Glace,Glace_permanente)):
                self.code += 4
            elif isinstance(aura,(Ombre,Ombre_permanente)):
                self.code += 8

    #Certains agissants particulièrement tapageurs font un concours de celui qui aura la plus grosse aura (comment ça, cette phrase particulièrement compliquée aura juste servi à faire un jeu de mot sur aura ?)
    def ajoute_aura(self,aura:Aura):
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
    def veut_passer(self,intrus:Mobile,direction:Direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère au mur compétent, qui gère tout."""
        self[direction].veut_passer(intrus)

    def step_out(self,entitee:Entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_out):
                effet.execute(entitee)

    def step_in(self,entitee:Entitee):
        for effet in self.effets:
            if isinstance(effet,On_step_in):
                effet.execute(entitee) #On agit sur les agissants qui arrivent (pièges, téléportation, etc.)

    #Tout le monde a fini de se déplacer.
    def post_action(self):
        self.opacite_bonus = 0 # On reset ça à chaque tour, sinon ça va devenir tout noir
        self.code = 0
        if len(self.effets) == 1: #On a un seul effet ! L'effet d'aura.
            if self.element != TERRE: #Les auras de terre sont juste là pour embêter les autres de toute façon
                self.effets[0].execute(self)
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
                    if ID in auras : # On a déjà une aura de ce type
                        auras[ID].append(effet)
                    else:
                        auras[ID]=[effet]
                    prio = effet.priorite
                    if prio > priorite_max : # On a un nouveau gagnant !
                        IDmax = ID
                        priorite_max = prio
                elif isinstance(effet,On_attack):
                    on_attaques.append(effet)
                elif (isinstance(effet,Attaque_case_delayee) and effet.delai > 0):
                    effet.execute(self) #On diminue le délai
                elif isinstance(effet,Attaque_case):
                    attaques.append(effet)
                elif isinstance(effet,On_post_action): #Les auras non-élémentales sont aussi des On_post_action
                    effet.execute(self)

            for aura in auras[IDmax]:
                aura.execute(self)

            for attaque in attaques:
                for protection in on_attaques:
                    protection.execute(attaque)
                attaque.execute(self)

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
                
    def casser_mur(self,direction:Direction):
        """
        Fonction qui casse le mur dans la direction indiquée
        """
        self[direction].brise()

    def construire_mur(self,direction:Direction):
        """
        Fonction qui construit le mur dans la direction indiquée
        """
        self[direction].construit()

    def interdire_mur(self,direction:Direction):
        """
        Fonction qui construit le mur impassable dans la direction indiquée
        """
        self[direction].interdit()

    def mur_plein(self,direction:Direction):
        """
        Fonction qui indique si le mur indiquée par la direction est plein ou non
        """
        return self[direction].is_ferme()

    def acces(self,direction:Direction,clees:List[str]=[]):
        return not(self[direction].is_ferme(clees)) and self[direction].get_cible()

    def murs_pleins(self):
        directions = []
        for direction in DIRECTIONS:
            if self.mur_plein[direction]:
                directions.append(direction)
        return directions

    def get_mur_dir(self,direction:Direction):
        return self[direction]

    def get_murs(self):
        return self.murs

    # def get_mur_haut(self):
    #     return self[0]

    # def get_mur_droit(self):
    #     return self[1]

    # def get_mur_bas(self):
    #     return self[2]

    # def get_mur_gauche(self):
    #     return self[3]

    # def toString(self):
    #     return "haut "+str(self[0].get_etat())+" droite "+str(self[1].get_etat())+" bas "+str(self[2].get_etat())+" gauche "+str(self[3].get_etat())+"  "

    def get_opacite(self):
        return self.opacite + self.opacite_bonus

    def get_infos(self,clees:List[str]): #Est-ce que ce serait plus clair sous forme de dictionnaire ? Ou d'objet ?
        return Representation_case(self.position, self.clarte, self.calcule_code(), self.get_cibles_fermes(clees), self.get_codes_effets(), self.repoussante)

    def calcule_code(self):#La fonction qui calcule le code correpondant à l'état de la case. De base, 0. Modifié d'après les effets subits par la case.
        return self.code

    def get_cibles_fermes(self,clees:List[str]):
        return [self[i].get_cible_ferme(clees) for i in DIRECTIONS]

    def get_codes_effets(self) -> List[List[int]]:
        effets=[]
        for effet in self.effets:
            if isinstance(effet,Attaque_case_delayee):
                effets.append([effet.responsable,effet.delai,effet.degats])
        return effets

    def get_copie(self):
        copie = Case(self.position,self.niveau,self.element,self.effets,self.opacite)
        copie.murs = self.murs
        return copie

    def active(self,controleur:Controleur):
        self.controleur = controleur
        for mur in self.murs :
            mur.active(controleur)

    def desactive(self):
        self.controleur = None
        for mur in self.murs :
            mur.desactive()
