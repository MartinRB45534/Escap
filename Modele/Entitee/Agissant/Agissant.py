from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Type, Dict, Set
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...Systeme.Classe.Classe_principale import Classe_principale
    from .Espece import Espece
    from .Inventaire import Inventaire
    from .Statistiques import Statistiques
    from ...Esprit.Esprit import Esprit
    from ..Item.Item import Item
    from ...Labyrinthe.Labyrinthe import Labyrinthe
    from ...Systeme.Elements import Element
    from .Vue.Vue import Vue

# Imports des classes parentes
from ..Entitee import Non_superposable, Mobile

class Agissant(Non_superposable,Mobile): #Tout agissant est un cadavre, tout cadavre n'agit pas.
    """La classe des entitées animées. Capable de décision, de différentes actions, etc. Les principales caractéristiques sont l'ID, les stats, et la classe principale."""
    def __init__(self,identite:str,labyrinthe:Labyrinthe,cond_evo:List,skills_intrasecs:Set[Skill_intrasec],skills:Set[Skill_extra],niveau:int,pv_max:float,regen_pv_max:float,regen_pv_min:float,restauration_regen_pv:float,pm_max:float,regen_pm:float,force:float,priorite:float,vitesse:float,affinites:Dict[Element,float],immunites:Set[Element],espece:Espece,oubli:float,resolution:int,forme:str,forme_tete:str,nb_doigts:int,magies:List[Type[Magie]],items:List[Type[Item]],position:crt.Position,ID: Optional[int]=None):
        Entitee.__init__(self,position,ID)
        self.identite = identite
        self.labyrinthe = labyrinthe
        self.statistiques = Statistiques(self,priorite,vitesse,force,pv_max,regen_pv_max,regen_pv_min,restauration_regen_pv,pm_max,regen_pm,affinites,immunites)
        self.espece = espece
        self.classe_principale = Classe_principale(cond_evo,skills_intrasecs,skills,niveau)
        self.niveau = self.classe_principale.niveau
        self.oubli = oubli
        self.resolution = resolution
        self.forme = forme
        self.forme_tete = forme_tete
        self.statut = "attente"
        self.etat = Etats_agissants.VIVANT

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
        
        self.cadavre = Cadavre(self)

        if magies:
            skill:Optional[Skills_magiques] = trouve_skill(self.classe_principale,Skills_magiques)
            if skill is None:
                raise ValueError("Pas de skill magique pour l'entitée")
            for magie in magies:
                skill.ajoute(magie)
        if items:
            new_items:Set[Item] = set()
            for item in items:
                new_items.add(item(labyrinthe,crt.POSITION_ABSENTE))
            self.inventaire.equippe(new_items)

    @property
    def equipement(self):
        return self.inventaire.get_equippement()

    def get_impact(self) -> crt.Position:
        return self.position+self.dir_regard

    # Les actions de l'agissant
    def attaque(self,direction:crt.Direction):
        self.regarde(direction)
        skill = trouve_skill(self.classe_principale,Skill_attaque_arme)
        arme = self.arme
        if skill and arme:
            self.fait(skill.fait(self,arme,direction))
        else:
            skill = trouve_skill(self.classe_principale,Skill_attaque)
            assert skill is not None
            self.fait(skill.fait(self,direction))

    def va(self,direction:crt.Direction):
        self.regarde(direction)
        skill = trouve_skill(self.classe_principale,Skill_deplacement)
        assert skill is not None
        self.fait(skill.fait(self,direction))

    def agit_en_vue(self,defaut = ""): #Par défaut, on n'a pas d'action à distance
        return defaut

    def comporte_distance(self,degats:float):
        return 0

    def veut_attaquer(self,degats:float=0):
        pass

    def veut_fuir(self,degats:float=0):
        pass

    def get_direction(self):
        if self.dir_regard is not None:
            return self.dir_regard
        else:
            return crt.Direction.HAUT #Par défaut, on regarde vers le haut

    def fait(self,action:Action,force:bool=False):
        self.action = action

    def regarde(self,direction:crt.Direction,force:bool=False):
        if direction is not None:
            self.dir_regard = direction

    @property
    def arme(self):
        return self.inventaire.get_arme()

    @property
    def bouclier(self):
        return self.inventaire.get_bouclier()

    @property
    def clees(self):
        return self.inventaire.get_clees()

    def peut_voir(self,direction:crt.Direction):
        return self.labyrinthe.get_mur(self.position,direction).ferme # TODO : revoir ça

    def affinite(self,element:Element):
        return self.statistiques.get_affinite(element)

    def peut_payer(self,cout:float):
        skill = trouve_skill(self.classe_principale,Skill_magie_infinie)
        res = True
        if skill is None:
            res = self.get_total_pm() >= cout
        return res

    def paye(self,cout:float):
        #On paye d'abord avec le mana directement accessible
        if self.pm >= cout:
            self.pm -= cout #Si on peut tout payer, tant mieux.
        else :
            cout_restant = cout
            if self.pm > 0:
                self.pm = 0
                cout_restant -= self.pm
            if cout_restant > 0: #Sinon, on fait appel aux éventuelles réserves de mana
                for effet in self.effets:
                    if isinstance(effet,Reserve_mana):
                        if effet.mana >= cout_restant:
                            effet.execute(cout_restant)
                            cout_restant = 0
                            break
                        else :
                            cout_restant -= effet.mana
                            effet.execute(effet.mana)
            if cout_restant > 0: # Si ce n'est toujours pas assez, on utilise la magie infinie (on aurait pas pu se retrouver dans la situation de payer plus sans ça, donc on l'a forcement !)
                self.pm -= cout_restant

    def get_total_pm(self):
        total = self.pm
        for effet in self.effets:
            if isinstance(effet,Reserve_mana):
                total += effet.mana
        return total
    
    @property
    def force(self):
        return self.statistiques.get_force()

    @property
    def vitesse(self):
        return self.statistiques.get_vitesse()

    @property
    def priorite(self):
        return self.statistiques.get_priorite()

    def subit(self,degats:float,element=Element.TERRE):
        if element not in self.statistiques.immunites:
            degats /= self.statistiques.get_affinite(element)
            self.statistiques.blesse(degats)

    def instakill(self,responsable:Agissant):
        immortel = trouve_skill(self.classe_principale,Skill_immortel)
        if immortel is not None:
            if self.pv > 0:
                self.pv = 0 #Et ça s'arrète là
        else:
            self.meurt()

    def soigne(self,soin:float):
        self.statistiques.soigne(soin)

    def rejoint(self,esprit:Esprit):
        self.esprit = esprit

    def meurt(self):
        if self.position is None:
            raise ValueError("Un personnage qui n'a pas de position est en train de mourir !")
        self.pv = self.pm = 0
        self.etat = Etats_agissants.MORT
        self.taux_regen_pv = self.taux_regen_pm = self.taux_force = self.taux_priorite = self.taux_vitesse = self.taux_aff_o = self.taux_aff_f = self.taux_aff_t = self.taux_aff_g = self.taux_stats = {} #/!\ À corriger !
        self.effets = []
        case = self.labyrinthe.get_case(self.position)
        self.inventaire.drop_all(case)
        case.part(self)
        case.items.add(self.cadavre)
        self.cadavre.position = self.position
        self.position = crt.POSITION_ABSENTE

    def get_esprit(self):
        return self.esprit

    def get_description(self,observation=0):
            return ["Un agissant","Qu'est-ce qu'il fait dans un inventaire ?"]

    def get_skill_vision(self) -> Skill_vision:
        skill = trouve_skill(self.classe_principale,Skill_vision)
        if skill is None:
            raise ValueError("Un agissant n'a pas de skill de vision !")
        return skill

    def get_skins_statuts(self):
        if self.statut == "paix":
            return [SKIN_STATUT_PAIX]
        elif self.statut == "exploration":
            return [SKIN_STATUT_EXPLORATION]
        elif self.statut == "fuite":
            return [SKIN_STATUT_FUITE]
        elif self.statut == "soutien":
            return [SKIN_STATUT_SOUTIEN]
        elif self.statut == "soin":
            return [SKIN_STATUT_SOIN]
        elif self.statut == "attaque":
            return [SKIN_STATUT_ATTAQUE]
        elif self.statut == "attaque boostée":
            return [SKIN_STATUT_ATTAQUE_BOOSTEE]
        elif self.statut == "rapproche":
            return [SKIN_STATUT_RAPPROCHE]
        else:
            return [SKIN_VIDE]

    # Découvrons le déroulé d'un tour, avec agissant-san :
    def debut_tour(self):
        if self.etat == Etats_agissants.VIVANT:
            #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
            #La régénération ! Plein de nouveaux pm et pv à gaspiller ! C'est pas beau la vie ?
            self.statistiques.debut_tour()
            self.inventaire.debut_tour()
            # Partie auras à retravailler         /!\ Qu'est-ce que je voulais retravailler là ?
            skills = self.classe_principale.debut_tour()
            for skill in skills :
                if isinstance(skill,Skill_aura):
                    effet = skill.utilise()
                    self.effets.append(effet)
                # Quels autres skills peuvent tomber dans cette catégorie ?
            #Et les effets. Vous les voyez tous les beaux enchantements qui nous renforcent ?
            for i in range(len(self.effets)-1,-1,-1) :
                effet = self.effets[i]
                if isinstance(effet,On_debut_tour):
                    effet.execute(self) #On exécute divers effets (dont les auras qu'on vient de rajouter au dessus)
                if isinstance(effet,Time_limited):
                    effet.wait()
                if effet.phase == "affichage": #L'affichage se fait en fin de tour
                    self.effets.remove(effet)
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas débuter mon tour !")

    def pseudo_debut_tour(self): #Not sure why I wanted that to exist, honestly...
        if self.etat == Etats_agissants.VIVANT:
            self.inventaire.pseudo_debut_tour()
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas débuter mon tour !")

    # Les esprits gambergent, tergiversent et hésitent.

    def post_decision(self):
        #On a pris de bonnes décisions pour ce nouveau tour ! On va bientôt pouvoir agir, mais avant ça, peut-être quelques effets à activer ?
        for effet in self.effets:
            if isinstance(effet,On_post_decision):
                effet.execute(self) #On exécute divers effets

    # Les agissants agissent, les items projetés se déplacent, éventuellement explosent.
    def on_action(self):
        if self.action is not None:
            if self.action.execute():
                self.action = None

    def post_action(self):
        #Le controleur nous a encore forcé à agir ! Quel rabat-joie, avec ses cout de mana, ses latences, ses "Vous ne pouvez pas utiliser un skill que vous n'avez pas." !
        attaques:List[Attaque] = []
        dopages:List[Dopage] = []
        for effet in self.effets:
            if isinstance(effet,On_post_action): #Les protections (générales) par exemple
                effet.execute(self)
            elif isinstance(effet,Dopage):
                dopages.append(effet)
            elif isinstance(effet,Attaque):
                attaques.append(effet)
        for attaque in attaques :
            for dopage in dopages:
                dopage.execute(attaque)
            attaque.execute() #C'est à dire qu'on attaque autour de nous. On n'en est pas encore à subir.

    # Tout le monde s'est préparé, a placé ses attaques sur les autres, etc. Les cases ont protégé leurs occupants.

    def pre_attack(self):
        #On est visé par plein d'attaques ! Espérons qu'on puisse se protéger.
        attaques:List[Attaque_particulier] = []
        on_attaques:List[On_attack] = []
        for effet in self.effets:
            if isinstance(effet,On_attack): #Principalement les effets qui agissent sur les attaques
                on_attaques.append(effet)
            elif isinstance(effet,Attaque_particulier):
                attaques.append(effet)
        skill:Optional[Skill_defense] = trouve_skill(self.classe_principale,Skill_defense)
        taux = 1
        if skill is not None :
            taux *= skill.utilise()
        items:List[Defensif] = []
        for item in self.inventaire.get_equippement():
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
        if self.etat == Etats_agissants.VIVANT:
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
        else:
            raise ValueError("Oups, je ne suis pas vivant, je ne peux pas finir mon tour !")
        if self.etat == Etats_agissants.VIVANT:
            if self.pv <= 0 :
                immortel:Optional[Skill_immortel] = trouve_skill(self.classe_principale,Skill_immortel)
                if immortel is not None :
                    self.taux_stats["immortalité"] = immortel.utilise()
                else :
                    essence:Optional[Skill_essence_magique] = trouve_skill(self.classe_principale,Skill_essence_magique)
                    if essence is not None :
                        cout = essence.utilise(self.pv)
                        if self.peut_payer(cout):
                            self.paye(cout)
                            self.pv = 0
                        else :
                            self.meurt()
                    else :
                        self.meurt()
            else :
                immortel:Optional[Skill_immortel] = trouve_skill(self.classe_principale,Skill_immortel)
                if immortel is not None :
                    if "immortalité" in self.taux_stats:
                        self.taux_stats.pop("immortalité")
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
        pass

class NoOne(Agissant):
    def __init__(self):
        pass

    def __equal__(self, other):
        if isinstance(other,NoOne):
            return True
        else:
            return False

# Imports utilisés dans le code (il y en a beaucoup !!!)
from ...Action.Attaque import Attaque
from ..Entitee import Entitee
from .Vue.Vue import voit_vue
from .Etats import Etats_agissants
from ...Action.Action import Action
from ...Esprit.Esprit import NOBODY
from ..Item.Cadavre import Cadavre
from ..Item.Equippement.Role.Defensif.Defensif import Defensif
from .Inventaire import Inventaire
from ...Systeme.Skill.Skills import Skill_intrasec, Skill_extra, Skill_attaque_arme, Skill_attaque, Skill_deplacement, Skill_magie_infinie, Skill_defense, Skill_immortel, Skill_essence_magique, Skill_vision, Skill_aura, Skills_magiques
from ...Systeme.Classe.Classes import trouve_skill
from ...Effet.Effets import On_attack, On_fin_tour, Maladie, Dopage, Attaque_particulier, Magie, Reserve_mana, On_debut_tour, On_post_decision, On_post_action, Time_limited
from Old_Affichage.Skins.Skins import SKIN_STATUT_ATTAQUE, SKIN_STATUT_ATTAQUE_BOOSTEE, SKIN_STATUT_PAIX, SKIN_STATUT_FUITE, SKIN_STATUT_EXPLORATION, SKIN_STATUT_RAPPROCHE, SKIN_STATUT_SOIN, SKIN_STATUT_SOUTIEN, SKIN_VIDE