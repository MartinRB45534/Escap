from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Type, List, Tuple, Dict, Set

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Effet.Magie.Magie import Magie
    from Jeu.Systeme.Skill_intrasec import Skill_intrasec
    from Jeu.Systeme.Classe import Classe_principale
    from Jeu.Entitee.Agissant.Inventaire import Inventaire
    from Jeu.Esprit.Esprit import Esprit
    from Jeu.Entitee.Item.Item import Item

# Imports des classes parentes
from Jeu.Entitee.Entitee import Non_superposable, Mobile

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT
from Jeu.Constantes import TERRE

class Agissant(Non_superposable,Mobile): #Tout agissant est un cadavre, tout cadavre n'agit pas.
    """La classe des entitées animées. Capable de décision, de différentes actions, etc. Les principales caractéristiques sont l'ID, les stats, et la classe principale."""
    def __init__(self,controleur:Controleur,identite:str,niveau:int,position:Position=ABSENT,ID: Optional[int]=None):
        Entitee.__init__(self,controleur,position,ID)
        self.identite:str = identite
        stats=CONSTANTES_STATS[identite]
        self.pv_max:float = stats['pv'][niveau]
        self.pv:float = self.pv_max
        self.regen_pv_max:float = stats['regen_pv_max'][niveau]
        self.regen_pv_min:float = stats['regen_pv_min'][niveau]
        self.restauration_regen_pv:float = stats['restauration_regen_pv'][niveau]
        self.regen_pv:float = self.regen_pv_max
        self.taux_regen_pv:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la régénération des pv. Correspond aux effets passager sur la régénération des pv.
        self.pm_max:float = stats['pm'][niveau]
        self.pm:float = self.pm_max
        self.regen_pm:float = stats['regen_pm'][niveau]
        self.taux_regen_pm:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la régénération des pm. Correspond aux effets passager sur la régénération des pm.
        self.force:float = stats['force'][niveau]
        self.taux_force:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la force. Correspond aux effets passager sur la force.
        self.priorite:float = stats['priorite'][niveau]
        self.taux_priorite:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la priorité. Correspond aux effets passager sur la priorité.
        self.vitesse:float = stats['vitesse'][niveau]
        self.taux_vitesse:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à la vitesse. Correspond aux effets passager sur la vitesse.
        self.aff_o:float = stats['aff_o'][niveau]
        self.taux_aff_o:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à l'ombre. Correspond aux effets passager sur l'affinité à l'ombre.
        self.aff_f:float = stats['aff_f'][niveau]
        self.taux_aff_f:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité au feu. Correspond aux effets passager sur l'affinité au feu.
        self.aff_t:float = stats['aff_t'][niveau]
        self.taux_aff_t:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à la terre. Correspond aux effets passager sur l'affinité à la terre.
        self.aff_g:float = stats['aff_g'][niveau]
        self.taux_aff_g:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer à l'affinité à la glace. Correspond aux effets passager sur l'affinité à la glace.
        self.taux_stats:Dict[str,float] = {} #Le dictionnaire qui contient tous les multiplicateurs à appliquer aux statistiques. Correspond aux effets passager sur les statistiques. (Inclure les regen dans les stats ?)
        self.immunites:List[int] = [] #La liste des éléments auxquels l'entitée est immunisé (très rare)
        self.especes:List[str] = stats['especes']
        self.classe_principale = Classe_principale(identite,niveau)
        self.niveau = self.classe_principale.niveau
        self.oubli = stats['oubli'][niveau]
        self.resolution = stats['resolution']
        self.forme:str = stats['forme']
        self.forme_tete:str = stats['forme_tete']
        self.statut = "attente"
        self.etat = "vivant"

        #vue de l'agissant
        self.vue = Representation_vue(self.position.lab, [], Decalage(0,0))

        self.offenses:List[Tuple[Agissant,float,float]]=[]
        self.esprit:Esprit=NOBODY

        #possessions de l'agissant
        self.inventaire = Inventaire(self,stats['doigts'],controleur)

        #la direction du regard
        self.dir_regard = HAUT

        self.skill_courant:Optional[Type[Skill_intrasec]] = None

        #Pour lancer des magies
        self.talent = 1
        self.magie_courante:Optional[Magie] = None
        self.cible_magie:Optional[Position|Agissant|List[Position]|List[Agissant]] = None
        self.dir_magie:Optional[Direction] = None
        self.cout_magie:float = 0
        self.magie_parchemin:Optional[Magie] = None
        self.cible_magie_parchemin:Optional[Position|Agissant|List[Position]|List[Agissant]] = None
        self.dir_magie_parchemin:Optional[Direction] = None
        self.cout_magie_parchemin:float = 0
        self.multi = False

        #Pour lancer des projectiles:
        self.projectile_courant:Optional[Cree_item] = None

        self.cadavre = Cadavre(controleur,self)

        if stats['magies']:
            skill:Optional[Skills_magiques] = trouve_skill(self.classe_principale,Skills_magiques)
            if skill is None:
                print(self)
                print(self.classe_principale)
                for skil in self.classe_principale.skills:
                    print(skil.niveau)
                    print(skil)
                raise ValueError("Pas de skill magique pour l'entitée")
            for magie in stats['magies']:
                skill.ajoute(eval(magie))
        if stats['items']:
            new_items:Set[Item] = set()
            for item in stats['items']:
                new_items.add(eval(item)(None,niveau))
            controleur.ajoute_items(new_items)
            self.inventaire.equippe(new_items)
        if stats['special']:
            pass

        self.controleur = controleur

    def get_etage_courant(self):
        return int(self.position.lab.split()[1])

    def get_stats_attaque(self,element:int):
        force = self.force
        for taux in self.taux_force.values():
            force *= taux
        affinite = self.get_aff(element)
        for taux in self.taux_stats.values():
            force *= taux
            affinite *= taux
        return force,affinite,self.dir_regard,self

    def get_impact(self) -> Position:
        return self.position+self.dir_regard


    # Les actions de l'agissant
    def attaque(self,direction:Direction):
        self.regarde(direction)
        if self.get_arme() is not None:
            self.utilise(Skill_attaque)
        else:
            self.utilise(Skill_stomp)
        self.set_statut("attaque")

    def va(self,direction:Direction):
        self.regarde(direction)
        self.utilise(Skill_deplacement) #La plupart des monstres n'ont pas ce skill !

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
            return DIRECTIONS[0]

    def utilise(self,skill:Optional[Type[Skill_intrasec]],force:bool=False):
        self.skill_courant = skill

    def regarde(self,direction:Direction,force:bool=False):
        if direction is not None:
            self.dir_regard = direction

    def set_statut(self,statut:str,force:bool=False):
        self.statut = statut

    def get_arme(self):
        return self.inventaire.get_arme()

    def get_bouclier(self):
        return self.inventaire.get_bouclier()

    def get_clees(self):
        return self.inventaire.get_clees()

    def get_item_lancer(self):
        if self.projectile_courant is None : #On lance l'item courant
            projectile = self.inventaire.get_item_courant()
        else : #On lance un item qu'on crée
            projectile = self.projectile_courant.cree_item(self) #Le 'self.projectile_courant' est un créateur de projectile
        return projectile

    def insurge(self,offenseur:Agissant,gravite:float,dangerosite:float):
        if offenseur:
            self.offenses.append((offenseur,gravite,dangerosite))

    def get_offenses(self) -> Tuple[List[Tuple[Agissant,float,float]],str]:
        offenses = self.offenses
        self.offenses = []
        etat = "vivant" #Rajouter des précisions
        if self.etat != "vivant" or self.controleur is None:
            etat = "incapacite"
        return offenses, etat

    def peut_voir(self,direction:Direction):
        assert self.controleur is not None
        assert self.position is not None
        return self.controleur.case_from_position(self.position)[direction].peut_voir()

    def get_aff(self,element:int):
        assert self.controleur is not None
        affinite = 1
        if element == OMBRE :
            affinite = self.aff_o
            for taux in self.taux_aff_o.values():
                affinite *= taux
            for item in self.inventaire.get_equippement():
                if isinstance(item,Tenebreux):
                    affinite *= item.taux_aff_ombre
        elif element == FEU :
            affinite = self.aff_f
            for taux in self.taux_aff_f.values():
                affinite *= taux
            for item in self.inventaire.get_equippement():
                if isinstance(item,Incandescant):
                    affinite *= item.taux_aff_feu
        elif element == TERRE :
            affinite = self.aff_t
            for taux in self.taux_aff_t.values():
                affinite *= taux
            for item in self.inventaire.get_equippement():
                if isinstance(item,Rocheux):
                    affinite *= item.taux_aff_terre
        elif element == GLACE :
            affinite = self.aff_g
            for taux in self.taux_aff_g.values():
                affinite *= taux
            for item in self.inventaire.get_equippement():
                if isinstance(item,Neigeux):
                    affinite *= item.taux_aff_glace
        else :
            print(f"{element}... quel est donc cet élément mystérieux ?")
        return affinite

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

    def get_total_regen_pv(self):
        assert self.controleur is not None
        regen_pv = self.regen_pv
        for taux in self.taux_regen_pv.values() :
            regen_pv *= taux
        for taux in self.taux_stats.values() :
            regen_pv *= taux
        # /!\ Rajouter les effets négatifs du skill de magie infinie /!\
        for item in self.inventaire.get_equippement():
            if isinstance(item,Reparateur):
                regen_pv = item.regen_pv(regen_pv)
        return regen_pv

    def get_total_regen_pm(self):
        assert self.controleur is not None
        regen_pm = self.regen_pm
        for taux in self.taux_regen_pm.values() :
            regen_pm *= taux
        for taux in self.taux_stats.values() :
            regen_pm *= taux
        for item in self.inventaire.get_equippement():
            if isinstance(item,Reparateur_magique):
                regen_pm = item.regen_pm(regen_pm)
        return regen_pm

    def get_vitesse(self):
        assert self.controleur is not None
        vitesse = self.vitesse
        for taux in self.taux_vitesse.values() :
            vitesse *= taux
        for taux in self.taux_stats.values() :
            vitesse *= taux
        for item in self.inventaire.get_equippement():
            if isinstance(item,Accelerateur):
                vitesse = item.augmente_vitesse(vitesse)
        return vitesse

    def get_priorite(self):
        assert self.controleur is not None
        priorite = self.priorite
        for taux in self.taux_priorite.values() :
            priorite *= taux
        for taux in self.taux_stats.values() :
            priorite *= taux
        for item in self.inventaire.get_equippement():
            if isinstance(item,Anoblisseur):
                priorite *= item.augmente_priorite(priorite)
        return priorite

    def subit(self,offenseur:Agissant,degats:float,distance="contact",element=TERRE): #L'ID 0 ne correspond à personne
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
            self.regen_pv = self.regen_pv_min
        if self.pv <= 0: #Alors tuer les gens, je ne vous en parle pas !!!
            gravite += 0.5
        self.insurge(offenseur,gravite,dangerosite)

    def instakill(self,responsable:Agissant):
        immortel = trouve_skill(self.classe_principale,Skill_immortel)
        if immortel is not None:
            if self.pv > 0:
                self.pv = 0 #Et ça s'arrète là
        else:
            self.meurt()

    def echape_instakill(self,responsable:Agissant):
        self.insurge(responsable,1,self.pv)

    def soigne(self,soin:float):
        self.pv += soin
        if self.pv >= self.pv_max:
            self.pv = self.pv_max

    def rejoint(self,esprit:Esprit):
        self.esprit = esprit

    def meurt(self):
        assert self.controleur is not None
        if self.position is None:
            raise ValueError("Un personnage qui n'a pas de position est en train de mourir !")
        self.pv = self.pm = 0
        self.etat = "mort"
        self.regarde(DIRECTIONS[0])
        self.taux_regen_pv = self.taux_regen_pm = self.taux_force = self.taux_priorite = self.taux_vitesse = self.taux_aff_o = self.taux_aff_f = self.taux_aff_t = self.taux_aff_g = self.taux_stats = {} #/!\ À corriger !
        self.effets = []
        self.inventaire.drop_all(self.position)
        self.controleur.items_courants.add(self.cadavre)
        self.cadavre.position = self.position
        self.position = ABSENT

    def get_esprit(self):
        return self.esprit

    def get_especes(self):
        return self.especes

    def get_description(self,observation=0):
            return ["Un agissant","Qu'est-ce qu'il fait dans un inventaire ?"]

    def get_portee_vue(self):
        skill = trouve_skill(self.classe_principale,Skill_vision)
        if skill is None:
            print("Oups, je n'ai pas de skill vision ! Pourquoi ?")
            print(self)
            portee = 0
        else :
            portee = skill.utilise()
            portee *= self.get_aff(OMBRE) #Puisque c'est le manque de lumière qui réduit le champ de vision !
        return portee

    def get_skin(self):
        return SKIN_AGISSANT

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

    def get_skin_tete(self):
        return SKIN_VIDE

    def get_skins_vue(self):
        assert self.controleur is not None
        skins:List[Image] = []
        if self.inventaire.arme is not None:
            skins.append(self.inventaire.arme.get_skin_vue(self.forme))
        skins.append(SKINS_CORPS_VUS[self.forme])
        if self.inventaire.armure is not None:
            skins.append(self.inventaire.armure.get_skin_vue(self.forme))
        skins.append(SKINS_TETES_VUES[self.forme_tete])
        if self.inventaire.haume is not None:
            skins.append(self.inventaire.haume.get_skin_vue(self.forme))
        return skins

    def get_texte_descriptif(self):
        return ["Un agissant","Pourquoi n'a-t-il pas de description adaptée ?","Voici quelques informations utiles pour corriger l'erreur :",f"ID : {self.ID}",f"Espèces : {self.especes}",f"Class : {type(self)}",f"self : {self}","En espèrant que ça suffise, et désolé pour le dérangement."]

    # Découvrons le déroulé d'un tour, avec agissant-san :
    def debut_tour(self):
        if self.etat == "vivant":
            #Un nouveau tour commence, qui s'annonce remplit de bonnes surprises et de nouvelles rencontres ! Pour partir du bon pied, on a quelques trucs à faire :
            #La régénération ! Plein de nouveaux pm et pv à gaspiller ! C'est pas beau la vie ?
            self.pv += self.get_total_regen_pv()
            self.regen_pv += self.restauration_regen_pv
            self.pm += self.get_total_regen_pm() #Et oui, les pm après, désolé...
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            if self.regen_pv > self.regen_pv_max:
                self.regen_pv = self.regen_pv_max
            if self.pm > self.pm_max:
                self.pm = self.pm_max
            self.inventaire.debut_tour()
            if self.latence >= 0:
                self.latence -= self.get_vitesse()
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
            print("Oups, je ne suis pas vivant, je ne peux pas débuter mon tour !")

    def pseudo_debut_tour(self): #Not sure why I wanted that to exist, honestly...
        if self.etat == "vivant":
            self.inventaire.pseudo_debut_tour()
        else:
            print("Oups, je ne suis pas vivant, je ne peux pas pseudo_débuter mon tour !")

    # Les esprits gambergent, tergiversent et hésitent.

    def post_decision(self):
        #On a pris de bonnes décisions pour ce nouveau tour ! On va bientôt pouvoir agir, mais avant ça, peut-être quelques effets à activer ?
        for effet in self.effets:
            if isinstance(effet,On_post_decision):
                effet.execute(self) #On exécute divers effets

    # Les agissants agissent, les items projetés se déplacent, éventuellement explosent.
    def on_action(self):
        self.utilise(None, True) #Si on a de la chance, on pourra jouer plusieurs fois dans le tour ! (Bientôt...)
        for effet in self.effets:
            if isinstance(effet,On_action):
                effet.execute(self) #Principalement les lancements de magies

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
            attaque.execute(self.controleur) #C'est à dire qu'on attaque autour de nous. On n'en est pas encore à subir.

    # Tout le monde s'est préparé, a placé ses attaques sur les autres, etc. Les cases ont protégé leurs occupants.

    def pre_attack(self):
        assert self.controleur is not None
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
        if self.etat == "vivant":
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
            print("Oups, je ne suis pas vivant, je ne peux pas finir mon tour !")
        if self.etat == "vivant":
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
                    print("Quelqu'un d'autre que le joueur a une incohérence entre son niveau et le niveau de sa classe principale !")
                    print(self)
                    print(self.niveau)
                    print(self.niveau)
                    print(self.classe_principale.niveau)
        else:
            print("Hum, apparemment ce n'est pas si inutile...")

    def level_up(self):
        niveau = self.classe_principale.niveau
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

class NoOne(Agissant):
    def __init__(self):
        pass

    def __equal__(self, other):
        if isinstance(other,NoOne):
            return True
        else:
            return False

# Imports utilisés dans le code (il y en a beaucoup !!!)
from Jeu.Entitee.Entitee import Entitee
from Jeu.Systeme.Constantes_stats import CONSTANTES_STATS
from Jeu.Labyrinthe.Structure_spatiale.Direction import HAUT, DIRECTIONS
from Jeu.Labyrinthe.Structure_spatiale.Decalage import Decalage
from Jeu.Labyrinthe.Vue import Representation_vue
from Jeu.Esprit.Esprit import NOBODY
from Jeu.Entitee.Item.Cree_item import Cree_item
from Jeu.Entitee.Item.Cadavre import Cadavre
from Jeu.Entitee.Item.Equippement.Role.Elementaires import Tenebreux, Rocheux, Neigeux, Incandescant
from Jeu.Entitee.Item.Equippement.Role.Defensif.Defensif import Defensif
from Jeu.Entitee.Item.Equippement.Role.Accelerateur import Accelerateur
from Jeu.Entitee.Item.Equippement.Role.Anoblisseur import Anoblisseur
from Jeu.Entitee.Item.Equippement.Role.Reparateur.Reparateur import Reparateur
from Jeu.Entitee.Item.Equippement.Role.Reparateur_magique.Reparateur_magique import Reparateur_magique
from Jeu.Entitee.Item.Items import *
from Jeu.Entitee.Agissant.Inventaire import Inventaire
from Jeu.Entitee.Agissant.Agissants import *
from Jeu.Systeme.Classe import trouve_skill, Classe_principale, Skills_magiques, Skill_defense, Skill_immortel, Skill_essence_magique, Skill_attaque, Skill_stomp, Skill_deplacement, Skill_magie_infinie, Skill_vision, Skill_aura
from Jeu.Effet.Effets import *
from Jeu.Constantes import OMBRE, TERRE, GLACE, FEU
from Affichage.Skins.Skins import SKIN_AGISSANT, SKIN_STATUT_ATTAQUE, SKIN_STATUT_ATTAQUE_BOOSTEE, SKIN_STATUT_PAIX, SKIN_STATUT_FUITE, SKIN_STATUT_EXPLORATION, SKIN_STATUT_RAPPROCHE, SKIN_STATUT_SOIN, SKIN_STATUT_SOUTIEN, SKINS_CORPS_VUS, SKINS_TETES_VUES, SKIN_VIDE