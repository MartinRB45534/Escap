from __future__ import annotations
from typing import TYPE_CHECKING, Optional,  Any
import random
import carte as crt

# Imports des classes parentes
from ..entitee import NonSuperposable, Mobile

# Imports utilisés dans le code (il y en a beaucoup !!!)
from ...action import Deplace, Attaque, Action, Magie
from ...effet import OnDebutTourAgissant, OnPostDecisionAgissant, OnPostActionAgissant, OnFinTourAgissant, TimeLimited, Protection, AttaqueParticulier, ReserveMana, Dopage
from .vue.vue import voit_vue
from ...commons import EtatsAgissants
from ..item import Cadavre, Defensif
from ...systeme import SkillIntrasec, SkillExtra, SkillAttaqueArme, SkillAttaque, SkillDeplacement, SkillEcrasement, SkillsMagiques, SkillMagieInfinie, SkillDefense, SkillImmortel, SkillEssenceMagique, SkillVision, SkillAura, trouve_skill, ClassePrincipale
from .statistiques import Statistiques
from .inventaire import Inventaire

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .espece import Espece
    from ...esprit.esprit import Esprit
    from ..item.item import Item
    from ..decors.decors import Decors
    from ...labyrinthe.labyrinthe import Labyrinthe
    from ...labyrinthe.mur import Mur
    from ...commons.elements import Element
    from .vue.vue import Vue

class Agissant(NonSuperposable,Mobile):
    """La classe des entitées animées. Capable de décision, de différentes actions, etc. Les principales caractéristiques sont l'ID, les stats, et la classe principale."""
    def __init__(self,identite:str,labyrinthe:Labyrinthe,cond_evo:list[float],skills_intrasecs:set[SkillIntrasec],skills:set[SkillExtra],niveau:int,pv_max:float,regen_pv_max:float,regen_pv_min:float,restauration_regen_pv:float,pm_max:float,regen_pm:float,force:float,priorite:float,vitesse:float,affinites:dict[Element,float],immunites:set[Element],espece:Espece,oubli:float,resolution:int,forme:str,forme_tete:str,nb_doigts:int,magies:list[type[Magie]],items:list[type[Item]],position:crt.Position,ID: Optional[int]=None):
        Mobile.__init__(self,position,ID)
        NonSuperposable.__init__(self,position,ID)
        self.identite = identite
        self.labyrinthe = labyrinthe
        self.statistiques = Statistiques(self,priorite,vitesse,force,pv_max,regen_pv_max,regen_pv_min,restauration_regen_pv,pm_max,regen_pm,affinites,immunites)
        self.espece = espece
        self.classe_principale = ClassePrincipale(cond_evo,skills_intrasecs,skills,niveau)
        self.niveau = self.classe_principale.niveau
        self.oubli = oubli
        self.resolution = resolution
        self.forme = forme
        self.forme_tete = forme_tete
        self.statut = "attente"
        self.etat = EtatsAgissants.VIVANT

        #vue de l'agissant
        self.vue:Vue = voit_vue(labyrinthe.extrait({self.position}))

        self.esprit:Esprit=NOBODY

        #possessions de l'agissant
        self.inventaire = Inventaire(self,nb_doigts)

        #la direction du regard
        self.dir_regard = crt.Direction.HAUT
        self.action:Optional[Action] = None

        #Pour lancer des magies
        self.talent = 1

        self.magie = Cadavre(self)

        if magies:
            skill:Optional[SkillsMagiques] = trouve_skill(self.classe_principale,SkillsMagiques)
            if skill is None:
                raise ValueError("Pas de skill magique pour l'entitée")
            for magie in magies:
                skill.ajoute(magie)
        if items:
            new_items:set[Item] = set()
            for item in items:
                new_items.add(item(labyrinthe,crt.POSITION_ABSENTE))
            self.inventaire.equippe(new_items)

    @property
    def equipement(self):
        """Retourne l'équipement de l'agissant."""
        return self.inventaire.get_equippement()

    def add_latence(self,latence: float):
        """Ajoute de la latence à l'action de l'entitée."""
        if self.action is not None:
            self.action.latence += latence

    def set_latence(self,latence: float):
        """Modifie la latence de l'action de l'entitée."""
        if self.action is not None:
            self.action.latence = latence

    def get_impact(self) -> crt.Position:
        """Retourne la position de l'impact de l'attaque de l'agissant."""
        return self.position+self.dir_regard

    # Les actions de l'agissant
    def attaque(self,direction:crt.Direction):
        """Fait attaquer l'agissant dans une direction."""
        self.regarde(direction)
        skill = trouve_skill(self.classe_principale,SkillAttaqueArme)
        arme = self.arme
        if skill and arme:
            self.fait(skill.fait(self,arme,direction))
        else:
            skill = trouve_skill(self.classe_principale,SkillAttaque)
            assert skill is not None
            self.fait(skill.fait(self,direction))

    def va(self,direction:crt.Direction):
        """Fait se déplacer l'agissant dans une direction."""
        self.regarde(direction)
        skill = trouve_skill(self.classe_principale,SkillDeplacement)
        assert skill is not None
        self.fait(skill.fait(self,direction))

    def passe(self,mur:Mur):
        """Renvoie True si l'agissant peut passer le mur (fermé)."""
        if self.fantome:
            return True
        ecrasement = trouve_skill(self.classe_principale,SkillEcrasement)
        if ecrasement is not None:
            passage = ecrasement.utilise(mur.niveau,self.priorite)
            if passage:
                mur.casser()
            return passage
        return False
    
    def arrive_agissant(self,agissant:Agissant):
        """Renvoie True si l'agissant peut arriver sur la case (occupée par un agissant)."""
        ecrasement = trouve_skill(self.classe_principale,SkillEcrasement)
        if ecrasement is not None:
            passage = ecrasement.utilise(agissant.priorite,self.priorite)
            if passage:
                agissant.ecrase(self)
            return passage
        return False
    
    def arrive_decors(self,decors:Decors):
        """Renvoie True si l'agissant peut arriver sur la case (occupée par un décors)."""
        ecrasement = trouve_skill(self.classe_principale,SkillEcrasement)
        if ecrasement is not None:
            passage = ecrasement.utilise(decors.priorite,self.priorite)
            if passage:
                decors.ecrase()
            return passage
        return False

    def agit_en_vue(self,defaut:str = ""): #Par défaut, on n'a pas d'action à distance
        """Fait agir l'agissant en vue."""
        return defaut

    def comporte_distance(self,_degats:float) -> int:
        """Retourne le comportement à distance de l'agissant."""
        return 0

    def veut_attaquer(self,_degats:float=0) -> bool:
        """Retourne si l'agissant veut attaquer."""
        return False

    def veut_fuir(self,_degats:float=0) -> bool:
        """Retourne si l'agissant veut fuir."""
        return False

    def get_direction(self):
        return self.dir_regard

    def fait(self,action:Action,_force:bool=False):
        """Fait faire une action à l'agissant."""
        self.action = action

    def regarde(self,direction:crt.Direction,_force:bool=False):
        """Fait regarder l'agissant dans une direction."""
        self.dir_regard = direction

    @property
    def arme(self):
        """Retourne l'arme de l'agissant."""
        return self.inventaire.get_arme()

    @property
    def bouclier(self):
        """Retourne le bouclier de l'agissant."""
        return self.inventaire.get_bouclier()

    @property
    def clees(self):
        """Retourne les clees de l'agissant."""
        return self.inventaire.get_clees()

    # def peut_voir(self,direction:crt.Direction):
    #     return self.vue.get_mur(self.position,direction).ferme

    def affinite(self,element:Element):
        """Retourne l'affinité de l'agissant avec un élément."""
        return self.statistiques.get_affinite(element)

    def peut_payer(self,cout:float):
        """Retourne si l'agissant peut payer un certain cout."""
        skill = trouve_skill(self.classe_principale,SkillMagieInfinie)
        res = True
        if skill is None:
            res = self.get_total_pm() >= cout
        return res

    def paye(self,cout:float):
        """L'agissant paye un certain cout."""
        #On paye d'abord avec le mana directement accessible
        if self.statistiques.pm >= cout:
            self.statistiques.pm -= cout #Si on peut tout payer, tant mieux.
        else :
            cout_restant = cout
            if self.statistiques.pm > 0:
                self.statistiques.pm = 0
                cout_restant -= self.statistiques.pm
            if cout_restant > 0: #Sinon, on fait appel aux éventuelles réserves de mana
                for effet in self.effets:
                    if isinstance(effet,ReserveMana):
                        if effet.mana >= cout_restant:
                            effet.paye(cout_restant)
                            cout_restant = 0
                            break
                        else :
                            cout_restant -= effet.mana
                            effet.paye(effet.mana)
            if cout_restant > 0: # Si ce n'est toujours pas assez, on utilise la magie infinie (on aurait pas pu se retrouver dans la situation de payer plus sans ça, donc on l'a forcement !)
                self.statistiques.pm -= cout_restant

    def get_total_pm(self):
        """Retourne le nombre de points de magie total de l'agissant (incluant les réserves)."""
        total = self.statistiques.pm
        for effet in self.effets:
            if isinstance(effet,ReserveMana):
                total += effet.mana
        return total

    @property
    def force(self):
        """Retourne la force de l'agissant."""
        return self.statistiques.get_force()

    @property
    def vitesse(self):
        """Retourne la vitesse de l'agissant."""
        return self.statistiques.get_vitesse()

    @property
    def priorite(self):
        """Retourne la priorité de l'agissant."""
        return self.statistiques.get_priorite()

    def subit(self,degats:float,element:Element,inverse:bool=False):
        """L'agissant subit des dégats d'un certain élément."""
        if inverse:
            degats *= self.statistiques.get_affinite(element)
            self.statistiques.blesse(degats)
        elif element not in self.statistiques.immunites:
            degats /= self.statistiques.get_affinite(element)
            self.statistiques.blesse(degats)

    def ecrase(self,_responsable:Agissant):
        """L'agissant est écrasé."""
        self.meurt()

    def instakill(self,_responsable:Agissant):
        """L'agissant meurt instantanément."""
        immortel = trouve_skill(self.classe_principale,SkillImmortel)
        if immortel is not None:
            if self.statistiques.pv > 0:
                self.statistiques.pv = 0 #Et ça s'arrète là
        else:
            self.meurt()

    def soigne(self,soin:float):
        """L'agissant est soigné de soin points de vie."""
        self.statistiques.soigne(soin)

    def rejoint(self,esprit:Esprit):
        """L'agissant rejoint un esprit."""
        self.esprit = esprit

    def meurt(self):
        """L'agissant meurt."""
        self.etat = EtatsAgissants.MORT
        self.effets = []
        case = self.labyrinthe.get_case(self.position)
        self.inventaire.drop_all(case)
        case.agissant = None
        case.items.add(self.magie)
        self.magie.position = self.position
        self.position = crt.POSITION_ABSENTE

    def get_esprit(self):
        """Retourne l'esprit de l'agissant."""
        return self.esprit

    def get_skill_vision(self) -> SkillVision:
        """Retourne le skill de vision de l'agissant."""
        skill = trouve_skill(self.classe_principale,SkillVision)
        if skill is None:
            raise ValueError("Un agissant n'a pas de skill de vision !")
        return skill

    # Découvrons le déroulé d'un tour, avec agissant-san :
    def debut_tour(self):
        """L'agissant commence son tour."""
        if self.etat == EtatsAgissants.VIVANT:
            #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
            #La régénération ! Plein de nouveaux pm et pv à gaspiller ! C'est pas beau la vie ?
            self.statistiques.debut_tour()
            self.inventaire.debut_tour()
            # Partie auras à retravailler         /!\ Qu'est-ce que je voulais retravailler là ?
            skills = self.classe_principale.debut_tour()
            for skill in skills :
                if isinstance(skill,SkillAura):
                    effet = skill.utilise()
                    self.effets.append(effet)
                # Quels autres skills peuvent tomber dans cette catégorie ?
            #Et les effets. Vous les voyez tous les beaux enchantements qui nous renforcent ?
            for i in range(len(self.effets)-1,-1,-1) :
                effet = self.effets[i]
                if isinstance(effet,TimeLimited):
                    effet.wait()
                if isinstance(effet,OnDebutTourAgissant):
                    effet.debut_tour(self) #On exécute divers effets (dont les auras qu'on vient de rajouter au dessus)
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas débuter mon tour !")

    def pseudo_debut_tour(self): #Not sure why I wanted that to exist, honestly...
        """L'agissant fait semblant de commencer son tour."""
        if self.etat == EtatsAgissants.VIVANT:
            self.inventaire.pseudo_debut_tour()
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas débuter mon tour !")

    # Les esprits gambergent, tergiversent et hésitent.

    def post_decision(self):
        """L'agissant a pris une décision."""
        #On a pris de bonnes décisions pour ce nouveau tour ! On va bientôt pouvoir agir, mais avant ça, peut-être quelques effets à activer ?
        for effet in self.effets:
            if isinstance(effet,OnPostDecisionAgissant):
                effet.post_decision(self) #On exécute divers effets

    def confus(self, taux_erreur:float):
        """L'agissant est confus."""
        if isinstance(self.action,Deplace):
            if random.random() < taux_erreur:
                self.action.direction = random.choice([dir for dir in crt.Direction if dir is not self.action.direction])

    # Les agissants agissent, les items projetés se déplacent, éventuellement explosent.
    def on_action(self):
        """L'agissant agit."""
        if self.action is not None:
            if self.action.execute():
                self.action = None

    def post_action(self):
        """L'agissant a agit."""
        #Le controleur nous a encore forcé à agir ! Quel rabat-joie, avec ses cout de mana, ses latences, ses "Vous ne pouvez pas utiliser un skill que vous n'avez pas." !
        attaques:list[Attaque] = []
        dopages:list[Dopage] = []
        for effet in self.effets:
            if isinstance(effet,OnPostActionAgissant): #Les protections (générales) par exemple
                effet.post_action(self)
            elif isinstance(effet,Dopage):
                dopages.append(effet)
            elif isinstance(effet,Attaque):
                attaques.append(effet)
        for attaque in attaques :
            for dopage in dopages:
                attaque.dope(dopage) #C'est dans ce sens là pour deux raisons : 1) pouvoir doper proprement les attaques multiples 2) pouvoir ajouter d'autres sortes de dopages (non multiplicatifs)
            attaque.execute() #C'est à dire qu'on attaque autour de nous. On n'en est pas encore à subir.

    # Tout le monde s'est préparé, a placé ses attaques sur les autres, etc. Les cases ont protégé leurs occupants.

    def pre_attack(self):
        """L'agissant est sur le point d'être attaqué (peut-être)."""
        #On est visé par plein d'attaques ! Espérons qu'on puisse se protéger.
        attaques:list[AttaqueParticulier] = []
        on_attaques:list[Protection] = []
        for effet in self.effets:
            if isinstance(effet,Protection): #Principalement les effets qui agissent sur les attaques
                on_attaques.append(effet)
            elif isinstance(effet,AttaqueParticulier):
                attaques.append(effet)
        skill:Optional[SkillDefense] = trouve_skill(self.classe_principale,SkillDefense)
        taux = 1
        if skill is not None :
            taux *= skill.utilise()
        items:list[Defensif] = []
        for item in self.inventaire.get_equippement():
            if isinstance(item,Defensif):
                items.append(item)
        for attaque in attaques :
            attaque.degats *= taux
            for on_attaque in on_attaques:
                on_attaque.protege(attaque)
            for item in items:
                item.intercepte(attaque)
            attaque.attaque(self)

    # Les autres subissent aussi des attaques.

    def fin_tour(self):
        """L'agissant finit son tour."""
        if self.etat == EtatsAgissants.VIVANT:
            #Quelques effets avant la fin du tour (maladie, soin, tout ça tout ça...)
            for i in range(len(self.effets)-1,-1,-1) :
                effet = self.effets[i]
                if isinstance(effet,OnFinTourAgissant):
                    effet.fin_tour(self)
            #Il est temps de voir si on peut encore recoller les morceaux.
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas finir mon tour !")
        if self.etat == EtatsAgissants.VIVANT:
            if self.statistiques.pv <= 0 :
                immortel:Optional[SkillImmortel] = trouve_skill(self.classe_principale,SkillImmortel)
                if immortel is not None :
                    immortel.utilise()
                else :
                    essence:Optional[SkillEssenceMagique] = trouve_skill(self.classe_principale,SkillEssenceMagique)
                    if essence is not None :
                        cout = essence.utilise(self.statistiques.pv)
                        if self.peut_payer(cout):
                            self.paye(cout)
                            self.statistiques.pv = 0
                        else :
                            self.meurt()
                    else :
                        self.meurt()
            self.inventaire.fin_tour()
            self.classe_principale.gagne_xp()
            if self.niveau != self.classe_principale.niveau : #On a gagné un niveau
                if self.classe_principale.evolutif:
                    self.level_up()
                else:
                    raise ValueError(f"Le niveau de {self} est {self.niveau} alors que celui de sa classe est {self.classe_principale.niveau} !")
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas finir mon tour !")

    def level_up(self):
        """L'agissant gagne un niveau."""

class NoOne(Agissant):
    def __init__(self):
        self.esprit = NOBODY

    def __equal__(self, other:Any):
        return isinstance(other,NoOne)

from ...esprit.esprit import NOBODY

NOONE = NoOne()
