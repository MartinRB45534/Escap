from Jeu.Effet.Effet import *
from Jeu.Constantes import *

class Attaque(One_shot):
    """L'effet d'attaque dans sa version générale. Pour chaque case dans la zone, crée une attaque (version intermèdiaire). Attachée au responsable."""
    def __init__(self,responsable=0,degats=0,element=TERRE,distance="contact",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
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
        self.distance = distance

    def action(self,controleur):
        position = controleur.get_entitee(self.responsable).get_position()
        positions_touches = controleur.get_pos_touches(position,self.portee,self.propagation,self.direction,"alliés",self.responsable)
        for position_touche in positions_touches:
            controleur.labs[position[0]].matrice_cases[position_touche[1]][position_touche[2]].effets.append(Attaque_case(self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_magique(Attaque):
    """Une attaque créée par magie."""
    def __init__(self,responsable=0,degats=0,element=TERRE,distance="proximité",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque.__init__(self,responsable,degats,element,distance,portee,propagation,direction,autre,taux_autre)

    def action(self,controleur):
        position = controleur.get_entitee(self.responsable).get_position()
        positions_touches = controleur.get_pos_touches(position,self.portee,self.propagation,self.direction,"tout",self.responsable)
        for position_touche in positions_touches:
            controleur.labs[position[0]].matrice_cases[position_touche[1]][position_touche[2]].effets.append(Attaque_case(self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_decentree(Attaque_magique):
    """Une attaque magique qui affecte une zone plus ou moins éloignée."""
    def __init__(self,position,responsable=0,degats=0,element=TERRE,distance="distance",portee=1,propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque_magique.__init__(self,responsable,degats,element,distance,portee,propagation,direction,autre,taux_autre)
        self.position = position

    def action(self,controleur):
        positions_touches = controleur.get_pos_touches(self.position,self.portee,self.propagation,self.direction,"tout",self.responsable)
        for position_touche in positions_touches:
            controleur.labs[self.position[0]].matrice_cases[position_touche[1]][position_touche[2]].effets.append(Attaque_case(self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_delayee(Attaque_magique):
    """Une attaque qui se fera plus tard."""
    def __init__(self,delai,responsable=0,degats=0,element=TERRE,portee=1,distance="distance",propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque_magique.__init__(self,responsable,degats,element,portee,distance,propagation,direction,autre,taux_autre)
        self.delai = delai

class Attaque_decentree_delayee(Attaque_decentree,Attaque_delayee):
    """Une attaque magique typique : affecte une zone éloignée après un temps de retard."""
    def __init__(self,position,delai,responsable=0,degats=0,element=TERRE,portee=1,distance="distance",propagation="C__S___",direction=None,autre=None,taux_autre=None):
        Attaque_magique.__init__(self,responsable,degats,element,portee,distance,propagation,direction,autre,taux_autre)
        self.position = position
        self.delai = delai

    def action(self,controleur):
        positions_touches = controleur.get_pos_touches(self.position,self.portee,self.propagation,self.direction,"tout",self.responsable)
        for position_touche in positions_touches:
            controleur.labs[self.position[0]].matrice_cases[position_touche[1]][position_touche[2]].effets.append(Attaque_case_delayee(self.delai,self.responsable,self.degats,self.element,self.distance,self.direction,self.autre,self.taux_autre))

class Attaque_case(One_shot):
    """L'effet d'attaque dans sa version intermédiaire. Créée par une attaque (version générale), chargé d'attacher une attaque particulière aux agissants de la case, en passant d'abord les défenses de la case. Attachée à la case."""
    def __init__(self,responsable,degats,element,distance="contact",direction = None,autre=None,taux_autre=None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.autre = autre
        self.taux_autre = taux_autre
        self.distance = distance

    def action(self,case,position):
        victimes_potentielles = case.controleur.trouve_agissants_courants(position)
        for victime_potentielle in victimes_potentielles:
            if not victime_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_corps():
                if self.autre == None :
                    case.controleur.get_entitee(victime_potentielle).effets.append(Attaque_particulier(self.responsable,self.degats,self.element,self.distance,self.direction))
                elif self.autre == "piercing":
                    case.controleur.get_entitee(victime_potentielle).effets.append(Attaque_percante(self.responsable,self.degats,self.element,self.distance,self.direction,self.taux_autre))

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
        else:
            print("Euh, quel est cet élément ?")
            print(self.element)
            return SKIN_VIDE

class Attaque_case_delayee(Attaque_case,Delaye):
    def __init__(self,delai,responsable,degats,element,distance="distance",direction = None,autre=None,taux_autre=None):
        Attaque_case.__init__(self,responsable,degats,element,distance,direction,autre,taux_autre)
        self.affiche = False
        self.delai=delai

    def execute(self,case,position):
        if self.phase == "démarrage":
            if self.delai > 0:
                self.delai -= 1
            else:
                self.affiche = True
                self.action(case,position)
                self.termine()

class Attaque_particulier(One_shot):
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version intermèdiaire), chargé d'infligé les dégats, en passant d'abord les défenses de l'agissant. Attachée à la victime."""
    def __init__(self,responsable,degats,element,distance="contact",direction = None):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.element = element
        self.direction = direction
        self.distance = distance

    def action(self,victime):
        victime.subit(self.degats,self.distance,self.element,self.responsable)

    def get_skin(self):
        return SKIN_BLESSURE

class Attaque_percante(Attaque_particulier): #Attention ! Perçant pour une attaque signifie qu'elle traverse les defenses. C'est totalement différend pour un item !
    """L'effet d'attaque dans sa version particulière. Créée par une attaque (version générale), chargé d'infligé les dégats, en passant d'abord les défenses de la case puis celles de l'agissant. Attachée à la victime. En prime, une partie de ses dégats ne sont pas bloquables."""
    def __init__(self,responsable,degats,element,distance="contact",direction = None,taux_perce = 0):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats * taux_perce
        self.degats_imbloquables = degats - self.degats #Ces dégats ne seront pas affectés par les bloquages.
        self.element = element
        self.direction = direction
        self.distance = distance

    def action(self,victime):
        self.degats += self.degats_imbloquables
        victime.subit(self.degats,self.distance,self.element,self.responsable)

    def get_skin(self):
        return SKIN_BLESSURE

class Purification_lumineuse(Attaque):
    """L'effet de purification. Une attaque de 'lumière'."""
    def __init__(self,responsable,degats,portee):
        self.affiche = False
        self.phase = "démarrage"
        self.responsable = responsable
        self.degats = degats
        self.portee = portee

    def action(self,controleur):
        position = controleur.get_entitee(self.responsable).get_position()
        positions_touches = controleur.get_pos_touches(position,self.portee,"C__S___",None,"tout")
        for position_touche in positions_touches:
            for victime_potentielle in controleur.trouve_agissants_courants(position_touche):
                if not "humain" in controleur.get_especes(victime_potentielle):
                    victime = controleur.get_entitee(victime_potentielle)
                    victime.pv -= self.degats * victime.get_aff(OMBRE)
  