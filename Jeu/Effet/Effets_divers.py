from Jeu.Effet.Effet import *
from Jeu.Systeme.Classe import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Constantes import *

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

class Obscurite(Evenement,On_debut_tour):
    """Evenement d'obscurité."""
    def __init__(self,niveau:int):
        self.affiche = False
        self.temps_restant = duree_obscurite[niveau-1]
        self.phase = "démarrage"
        self.gain_opacite = gain_opacite_obscurite[niveau-1]

    def action(self,case): #La case affectée devient plus impénétrable à la lumière
        if self.phase == "démarrage" :
            case.opacite += self.gain_opacite
        elif self.phase == "terminé":
            case.opacite -= self.gain_opacite

class Blizzard(Evenement,On_post_action):
    """Evenement de blizzard."""
    def __init__(self,niveau:int):
        self.affiche = False
        self.temps_restant = duree_blizzard[niveau]
        self.phase = "démarrage"
        self.gain_latence = gain_latence_blizzard[niveau]

    def action(self,case):
        if self.phase == "en cours":
            occupants = case.controleur.trouve_mobiles_courants(case.position)
            for occupant in occupants :
                case.controleur[occupant].latence.add_latence(self.gain_latence)

    def execute(self,case):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(case)

class Teleportation(One_shot,On_post_action):
    """Effet qui déplace une entitée."""
    def __init__(self,position:Position):
        self.affiche = True
        self.phase = "démarrage"
        self.position = position

    def action(self,porteur):
        porteur.position = self.position

    def get_skin(self):
        return SKIN_TELEPORTATION

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

class Impregnation(One_shot,On_fin_tour):
    """Effet qui impregne le parchemin d'une magie."""
    def __init__(self):
        self.affiche = False
        self.phase = "démarrage"

    def action(self,porteur):
        if porteur.ID == 2: #Le joueur veut impregner une de ses magies sur le parchemin
            porteur.methode_fin = porteur.fin_menu_auto_impregnation
            skill = trouve_skill(porteur.classe_principale,Skill_magie)
            porteur.options_menu = skill.menu_magie()
            porteur.start_menu()
        else:
            skill = trouve_skill(porteur.classe_principale,Skill_magie)
            latence,magie = skill.utilise(porteur.magie_courante)
            porteur.latence += latence
            cout = magie.cout_pm
            if porteur.peut_payer(cout):
                porteur.paye(cout)
                parch = Parchemin_impregne(None,magie,cout//2)
                porteur.controleur.ajoute_entitee(parch)
                porteur.inventaire.ajoute(parch)

class Dopage(One_shot,Time_limited):
    """Effet qui "dope" la prochaine attaque du joueur."""
    def __init__(self,responsable,taux_degats,duree):
        self.affiche = True
        self.phase = "démarrage"
        self.responsable = responsable
        self.taux_degats = taux_degats
        self.temps_restant = duree

    def action(self,attaque):
        if self.phase == "démarrage" :
            attaque.degats *= self.taux_degats

    def get_skin(self):
        return SKIN_DOPAGE

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

from Jeu.Entitee.Item.Parchemin.Parchemins import Parchemin_impregne