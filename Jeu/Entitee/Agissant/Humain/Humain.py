from Jeu.Skins.Skins import *
from Jeu.Entitee.Agissant.Agissant import *
from Jeu.Entitee.Agissant.Role.Roles import *
from Jeu.Dialogues.Dialogues import *

class Humain(Agissant,Interactif,Entitee_superieure):
    """La classe des pnjs et du joueur. A un comportement un peu plus complexe, et une personnalité."""
    def __init__(self,controleur,position,identite,niveau,ID):
        Agissant.__init__(self,controleur,position,identite,niveau,ID)
        self.statut_humain = "attente"
        self.dialogue = -1 #Le dialogue par défaut, celui des ordres
        self.replique = None #La réplique en cours de l'agissant vaut None lorsqu'il n'y a pas de dialogue en cours
        self.repliques = [] #Les réponses possibles de l'interlocuteur
        self.replique_courante = 0 #La réponse sélectionnée

        self.mouvement = 0 #0 pour un déplacement ciblé, 1 pour chercher, 2 pour un déplacement ciblé prioritaire et précis
        self.cible_deplacement = self.ID #Une ID pour suivre quelqu'un, ou une position pour s'y diriger
        self.comportement_corps_a_corps = 0 #0 pour attaquer, 1 pour ignorer, 2 pour fuir
        self.comportement_distance = 0 #0 pour foncer dans le tas, 1 pour tenter une attaque à distance puis se rapprocher, 2 pour tenter une attaque à distance puis fuir, 3 pour fuir puis tenter une attaque à distance
        self.antagonise_neutres = False #Si True, sera offensé par la simple vision d'un neutre (utile pour fuir les ennemis avant qu'ils n'attaquent)
        self.antagonise_offensifs = False #Si True, sera offensé par les neutres qui veulent l'attaquer (utile pour fuir les ennemis avant qu'ils n'attaquent sans déclencher de combats pour rien, mais nécessite une certaine intelligence...)

        self.attente = True #Les humains attendent le joueur au début du jeu

    def comporte_distance(self,degats):
        if self.fuite(degats):
            return 3
        else:
            return self.comportement_corps_a_corps

    def veut_attaquer(self,degats):
        return self.comportement_corps_a_corps == 0 and not self.fuite(degats)

    def veut_fuir(self,degats):
        return self.comportement_corps_a_corps == 2 or self.fuite(degats)

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
        if self.mouvement == 2:
            self.mouvement = 0

    def get_offenses(self):
        for offense in self.offenses:
            if offense[0] == 2:
                self.dialogue = 0
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

    def debut_tour(self):
        Agissant.debut_tour(self)
        if self.antagonise_neutres:
            for case in self.vue:
                for entitee in case[6]:
                    if not self.controleur.est_item(entitee):
                        if not entitee in self.controleur.get_esprit(self.esprit).ennemis.keys():
                            self.insurge(entitee,0.01,0)
        elif self.antagonise_offensifs:
            for case in self.vue:
                for ID_entitee in case[6]:
                    entitee = self.controleur.get_entitee(ID_entitee)
                    if issubclass(entitee.get_classe(),Agissant):
                        if self.ID in self.controleur.get_esprit(entitee.esprit).ennemis.keys():
                            self.insurge(ID_entitee,0.01,0)

    def get_skin(self):
        if self.etat == "vivant":
            return SKIN_CORPS_HUMAIN
        else:
            return SKIN_CADAVRE

    def get_skins_statuts(self):
        skins = Agissant.get_skins_statuts(self)
        if self.statut_humain == "exploration":
            skins.append(SKIN_STATUT_CHERCHE)
        elif self.statut_humain == "proximite":
            skins.append(SKIN_STATUT_PROXIMITE)
        elif self.statut_humain == "en chemin":
            skins.append(SKIN_STATUT_CHEMIN)
        elif self.statut_humain == "perdu":
            skins.append(SKIN_STATUT_PERDU)
        elif self.statut_humain == "paume":
            skins.append(SKIN_STATUT_PAUME)
        return skins

    def subit(self,degats,distance="contact",element=TERRE,ID=0): #L'ID 0 ne correspond à personne
        gravite = degats/self.pv_max
        dangerosite = 0
        if distance == "contact":
            dangerosite = degats*2
        elif distance == "proximité":
            dangerosite = degats
        elif distance == "distance":
            dangerosite = degats*0.2
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
            print(f"{self.identite} a été tué par :")
            print(degats,element)
            print(ID)
            print(self.controleur.get_entitee(ID))
            self.effets_mortuaires = self.effets
            self.effets_mortuaires_tueur = self.controleur.get_entitee(ID).effets
            self.controleur.pause = True
        self.insurge(ID,gravite,dangerosite)
