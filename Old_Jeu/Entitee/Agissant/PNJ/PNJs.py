from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Type, List, Tuple, Dict

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Old_Jeu.Action.Action import Action
    from Old_Jeu.Systeme.Skill.Actif import Actif
    from Old_Jeu.Entitee.Item.Projectile.Projectile import Projectile

# Imports des classes parentes
from Old_Jeu.Entitee.Agissant.Agissant import Agissant
from Old_Jeu.Entitee.Entitee import Interactif
from Old_Jeu.Entitee.Agissant.Role.Mage import Mage

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class PNJ(Agissant, Interactif):
    """
    Un personnage non-jouable (en vrai plutôt non-joué ici, il peut être controlable par un joueur).
    Se distingue par sa capacité à parler, obéir et le fait d'attendre le joueur jusqu'à le rencontrer.
    """
    def __init__(self, controleur: Controleur, identite: str, niveau: int, ID: Optional[int] = None, position: Position = ABSENT):
        Agissant.__init__(self, controleur, identite, niveau, position, ID)
        self.dialogue = -1 #Le dialogue par défaut, celui des ordres
        self.replique = None #La réplique en cours de l'agissant vaut None lorsqu'il n'y a pas de dialogue en cours
        self.repliques = [] #Les réponses possibles de l'interlocuteur
        self.replique_courante = 0 #La réponse sélectionnée

        self.mouvement = 3 #0 pour un déplacement vague, 1 pour chercher, 2 pour un déplacement ciblé (prioritaire et précis), 3 pour l'attente, 4 pour l'attaque (déplacement ciblé et attaque dès qu'à portée)
        self.cible_deplacement = self #Une ID pour suivre quelqu'un, ou une position pour s'y diriger
        self.comportement_corps_a_corps = 0 #0 pour attaquer, 1 pour ignorer, 2 pour fuir
        self.comportement_distance = 0 #0 pour foncer dans le tas, 1 pour tenter une attaque à distance puis se rapprocher, 2 pour tenter une attaque à distance puis fuir, 3 pour fuir puis tenter une attaque à distance
        self.antagonise_neutres = False #Si True, sera offensé par la simple vision d'un neutre (utile pour fuir les ennemis avant qu'ils n'attaquent)
        self.antagonise_offensifs = False #Si True, sera offensé par les neutres qui veulent l'attaquer (utile pour fuir les ennemis avant qu'ils n'attaquent sans déclencher de combats pour rien, mais nécessite une certaine intelligence...)

        self.statut_pnj = "attente"

    def get_skins_statuts(self):
        skins = Agissant.get_skins_statuts(self)
        if self.statut_pnj == "exploration":
            skins.append(SKIN_STATUT_CHERCHE)
        elif self.statut_pnj == "proximite":
            skins.append(SKIN_STATUT_PROXIMITE)
        elif self.statut_pnj == "en chemin":
            skins.append(SKIN_STATUT_CHEMIN)
        elif self.statut_pnj == "perdu":
            skins.append(SKIN_STATUT_PERDU)
        elif self.statut_pnj == "paume":
            skins.append(SKIN_STATUT_PAUME)
        return skins

    def fuite(self,degats:float=0):
        return False

    def comporte_distance(self,degats:float):
        if self.fuite(degats):
            return 3
        else:
            return self.comportement_corps_a_corps

    def veut_attaquer(self,degats:float):
        return self.comportement_corps_a_corps == 0 and not self.fuite(degats)

    def veut_fuir(self,degats:float=0):
        return self.comportement_corps_a_corps == 2 or self.fuite(degats)

    def get_offenses(self):
        for offense in self.offenses:
            if offense[0] == 2: #/!\ Comment gérer des dialogues différents avec chaque autre humain ? Pour l'instant, on ne va pas y toucher
                self.dialogue = 0
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        elif self.fuite():
            etat = "fuite"
        else:
            etat = "PNJ" #Les PNJs ont des comportements inutilement alambiqués...
        return offenses, etat

    def set_case_dialogue(self,position):
        self.mouvement = 0
        self.cible_deplacement = position

    def set_agissant_dialogue(self,ID):
        self.mouvement = 0
        self.cible_deplacement = ID

    def set_cible(self,cible:int|Position):
        self.mouvement = 0
        self.cible_deplacement = cible
        self.replique = "dialogue-1phrase1.1.1.2"
        self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3"]

    def end_dialogue(self,dialogue=-1):
        self.controleur.joueur.interlocuteur = None
        self.controleur.unset_phase(DIALOGUE)
        self.dialogue = dialogue
        if self.mouvement == 2:
            self.mouvement = 0

    def debut_tour(self):
        Agissant.debut_tour(self)
        if self.antagonise_neutres:
            for case in self.vue:
                if case.agissant is not None:
                    if not case.agissant in self.esprit.ennemis:
                        self.insurge(case.agissant,0.01,0)
        elif self.antagonise_offensifs:
            for case in self.vue:
                if case.agissant is not None:
                    if self in case.agissant.esprit.ennemis:
                        self.insurge(case.agissant,0.01,0)

    def start_dialogue(self):
        raise NotImplementedError(f"Je ne peux pas commencer un dialogue. Parce que tu n'as pas surdéfini la méthode start_dialogue pour {self}.")

    def interprete(self,replique:str):
        raise NotImplementedError(f"Je ne peux pas interpréter {replique}. Parce que tu n'as pas surdéfini la méthode interprete pour {self}.")

    def get_replique(self,code:str):
        raise NotImplementedError(f"Je ne peux pas trouver la réplique correspondant à {code}. Parce que tu n'as pas surdéfini la méthode get_replique pour {self}.")

class PNJ_mage(PNJ,Mage):
    """
    Un PNJ qui pratique la magie.
    """


    def impregne(self,nom:str,parch:Parchemin_vierge):
        if self.controleur.joueur.interlocuteur is self: #Si l'imprégnation est demandée par le joueur
            if super().impregne(nom,parch):
                self.replique = "dialogue-1phrase1.3.1"
                self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
                if self.controleur.joueur.inventaire.a_parchemin_vierge():
                    self.repliques.append("dialogue-1reponse1.3")
                self.repliques.append("dialogue-1reponse1.4")
                return True
            else:
                self.replique = "dialogue-1phrase1.3.1echec"
                self.repliques = ["dialogue-1reponse1.1","dialogue-1reponse1.2","dialogue-1reponse1.3","dialogue-1reponse1.4"] #La question personnelle est pour quand le joueur veut faire avancer les interractions.
                return False
        else:
            return super().impregne(nom,parch)

class PJ(PNJ): #Les PJs sont des PNJs, parce que le mot PNJ est trompeur
    """
    Un personnage jouable. Se distingue par :
    - des touches de contrôle
    - un interlocuteur
    """
    def __init__(self, controleur: Controleur, position: Position, identite: str, niveau: int, ID: Optional[int] = None):
        PNJ.__init__(self,controleur, identite, niveau, ID, position)
        self.statut_simule:str = "attente"
        self.action_simule:Optional[Action] = None
        self.dir_regard_simule:Optional[Direction] = None
        self.attente:int = -1
        self.interlocuteur:Optional[Interactif] = None
        self.touches:Dict[str,Dict[Tuple|Tuple[int],Dict[int,List[str]|Type[Actif]|Direction|Type[Projectile]|str]|Dict[int,Dict]]] = {
            "effets":{
            },
            "skills":{
            },
            "directions":{
            },
            "kwargs":{
            },
            "projectiles":{},
            "magies":{},
        }

    def fait(self, action:Action, force: bool = False):
        if self is self.controleur.joueur and self.attente and not force:
            self.action_simule = action
        else:
            self.action = action

    def regarde(self, direction: Direction, force: bool = False):
        if self is self.controleur.joueur and self.attente and not force:
            self.dir_regard_simule = direction
        elif direction is not None:
            self.dir_regard = direction

    def set_statut(self, statut: str, force: bool = False):
        if self is self.controleur.joueur and self.attente and not force:
            self.statut_simule = statut
        else:
            self.statut = statut

    def interagit(self):
        #On cherche la personne :
        self.interlocuteur = None #Normalement c'est déjà le cas
        for i in [0,-1,1,2]:
            direction = self.dir_regard+i
            if self.peut_voir(direction):
                pos = self.position+direction
                interactifs = self.controleur.trouve_interactifs_courants(pos)
                if interactifs != set():
                    interactif = interactifs.pop() # Est-ce que je continue à appeler ça un interlocuteur ?
                    if isinstance(interactif,PNJ):
                        self.interlocuteur = interactif
                        self.controleur.set_phase(DIALOGUE)
                        interactif.start_dialogue()
                        self.regarde(direction,True)
                        interactif.regarde(self.dir_regard.oppose())
                    elif isinstance(interactif,Decors_interactif):
                        self.interlocuteur = interactif
                        self.regarde(direction,True)
                        if isinstance(interactif,Ustensile):
                            self.controleur.set_phase(RECETTE)
                    break

class PJ_mage(PJ, PNJ_mage):
    pass

# Imports utilisés dans le code
from Old_Affichage.Skins.Skins import SKIN_STATUT_PAUME, SKIN_STATUT_PERDU, SKIN_STATUT_CHERCHE, SKIN_STATUT_CHEMIN, SKIN_STATUT_PROXIMITE
from Old_Jeu.Action.Non_skill import Impregne
from Old_Jeu.Constantes import DIALOGUE, RECETTE
from Old_Jeu.Entitee.Item.Parchemin.Parchemins import Parchemin_vierge
from Old_Jeu.Entitee.Decors.Decors import Ustensile
from Old_Jeu.Entitee.Decors.Decor import Decors_interactif