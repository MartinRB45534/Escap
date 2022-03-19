from Jeu.Constantes import *
from Jeu.Entitee.Item.Item import *
from Jeu.Effet.Effets import *

class Mur:
    def __init__(self,effets):
        self.effets = effets
        self.peut_passer = False
        self.controleur = None

    def is_ferme(self,clees=[]):
        ferme = False
        for effet in self.effets :
            if isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                ferme = True
        return ferme

    def get_blocage(self,clees):
        blocage = None
        for effet in self.effets :
            if isinstance(effet,Mur_impassable):
                blocage = "Imp"
            elif blocage != "Imp" and isinstance(effet,Mur_plein) and not(effet.casse):
                blocage = "Ple"
            elif blocage != "Imp" and blocage != "Ple" and isinstance(effet,Porte_barriere) and effet.ferme and not(effet.code in clees):
                blocage = "P_b"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and isinstance(effet,Porte) and effet.ferme and not(effet.code in clees):
                blocage = "Por"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and isinstance(effet,Barriere):
                blocage = "Bar"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and blocage != "Por" and blocage != "Bar" and isinstance(effet,Escalier):
                blocage = "Esc"
            elif blocage != "Imp" and blocage != "Ple" and blocage != "P_b" and blocage != "Por" and blocage != "Bar" and blocage != "Esc" and isinstance(effet,Teleport) and effet.affiche:
                blocage = "Tel"
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

    def peut_voir(self):
        visible = True
        for effet in self.effets :
            if (isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not(effet.casse)) or (isinstance(effet,Porte) and effet.ferme)) or (isinstance(effet,Teleport) and effet.affiche):
                visible = False
        return visible

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

    def cree_porte(self,durete,code,porte=None):
        self.brise()
        if porte == None:
            self.effets.append(Porte(durete,code))
        else:
            self.effets.append(porte(durete,code))

    def get_trajet(self):
        trajet = None
        for effet in self.effets :
            if trajet != "teleport" and (isinstance(effet,Escalier) and effet.sens == HAUT):
                trajet = "escalier haut"
            elif trajet != "teleport" and (isinstance(effet,Escalier) and effet.sens == BAS):
                trajet = "escalier bas"
            elif isinstance(effet,Teleport) and effet.affiche == True:
                trajet = "teleport"
        return trajet

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

    def get_cible_ferme(self,clees):
        return [self.get_cible_ferme_simple(),self.get_cible_ferme_portes(clees),self.get_cible_ferme_portails(),self.get_cible_ferme_portes_portails(clees),self.get_cible_ferme_escaliers(clees)]

    def get_cible_ferme_simple(self):
        """Renvoie la position de la case d'arrivée si on est un mur ouvert sans téléporteur, False sinon"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not effet.affiche :
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and effet.ferme):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portes(self,clees):
        """Renvoie aussi la position si le mur est une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not effet.affiche :
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portails(self):
        """Renvoie aussi la position si le mur est un téléporteur (mais pas s'il est une porte)"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not isinstance(effet,Escalier):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and effet.ferme):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_portes_portails(self,clees):
        """Renvoie aussi la position si le mur est un téléporteur ou une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport) and not isinstance(effet,Escalier):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def get_cible_ferme_escaliers(self,clees):
        """Renvoie aussi la position si le mur est un téléporteur ou une porte dont l'agissant a la clé"""
        cible = True
        for effet in self.effets :
            if isinstance(effet,Teleport):
                cible = effet.position
            elif isinstance(effet,Mur_impassable) or (isinstance(effet,Mur_plein) and not effet.casse) or (isinstance(effet,Porte) and (effet.ferme and not(effet.code in clees))):
                return False
        if cible is True:
            return False
        return cible

    def set_cible(self,position,surnaturel=False,portail=None):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        if portail == None:
            portail = Teleport
        self.effets.append(portail(position,surnaturel))

    def set_escalier(self,position,sens,escalier=None):
        for effet in self.effets:
            if isinstance(effet,Teleport):
                self.effets.remove(effet)
        if escalier == None:
            escalier = Escalier
        self.effets.append(escalier(position,sens))

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
