from Jeu.Effet.Magie import *
from Jeu.Effet.Enchantements import *
from Jeu.Effet.Effets_divers import *
from Jeu.Effet.Effets_protection import *

# Maintenant on va créer les véritables sorts. On commence par les soins :
class Magie_soin(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin[niveau-1]
        self.cout_pm = cout_pm_soin[niveau-1]
        self.latence = latence_soin[niveau-1]
        self.gain_pv = gain_pv_soin[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        agissant_cible = lanceur.controleur.get_entitee(self.cible)
        agissant_cible.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_SOIN

    def get_titre(self,observation):
        return f"Magie de soin (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de soin","Elle affecte un agissant à portée de vue du lanceur.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_multi_soin(Cible_agissant,Multi_cible):
    """La magie qui invoque un effet de soin sur des agissants ciblés."""
    nom = "magie multi soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_multi_soin[niveau-1]
        self.cout_pm = cout_pm_multi_soin[niveau-1]
        self.latence = latence_multi_soin[niveau-1]
        self.gain_pv = gain_pv_multi_soin[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        for cible in self.cible:
            agissant_cible = lanceur.controleur.get_entitee(cible)
            agissant_cible.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_SOIN

    def get_titre(self,observation):
        return f"Magie de multi-soin (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de soin","Elle affecte un ou plusieurs agissants à portée de vue du lanceur.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_soin_superieur(Cible_agissant):
    """La magie qui invoque un effet de soin sur un agissant ciblé."""
    nom = "magie_soin_superieur"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_superieur[niveau-1]
        self.cout_pm = cout_pm_soin_superieur[niveau-1]
        self.latence = latence_soin_superieur[niveau-1]
        self.gain_pv = gain_pv_soin_superieur[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        agissant_cible = lanceur.controleur.get_entitee(self.cible)
        agissant_cible.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_SOIN_SUPERIEUR

    def get_titre(self,observation):
        return f"Magie de soin avancée (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de soin","Elle affecte un agissant à portée de vue du lanceur.","Plus efficace et moins couteuse que la version classique.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_soin_de_zone(Cible_case):
    """La magie qui invoque un effet de soin sur une zone."""
    nom = "magie zone de soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_zone[niveau-1]
        self.cout_pm = cout_pm_soin_zone[niveau-1]
        self.latence = latence_soin_zone[niveau-1]
        self.gain_pv = gain_pv_soin_zone[niveau-1]
        self.portee = portee_soin_zone[niveau-1]
        self.temps = 10000
        self.cible = None #Fixée par le controleur
        self.affiche = True

    def action(self,lanceur):
        poss = lanceur.controleur.get_pos_touches(self.cible,self.portee)
        for pos in poss:
            lanceur.controleur.labs[pos[0]].matrice_cases[pos[1]][pos[2]].effets.append(Soin_case(self.gain_pv,lanceur.ID))

    def get_image(self):
        return SKIN_MAGIE_SOIN_ZONE

    def get_titre(self,observation):
        return f"Magie de soin de zone (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de soin","Elle affecte une zone à proximité du lanceur.","La zone de soin peut s'étendre au-delà de la vue du lanceur.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Magie_auto_soin(Magie):
    """La magie qui invoque un effet de soin sur son lanceur."""
    nom = "magie auto soin"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_soin_auto[niveau-1]
        self.cout_pm = cout_pm_soin_auto[niveau-1]
        self.latence = latence_soin_auto[niveau-1]
        self.gain_pv = gain_pv_soin_auto[niveau-1]
        self.affiche = True

    def action(self,lanceur):
        lanceur.effets.append(Soin(lanceur.ID,self.gain_pv))

    def get_image(self):
        return SKIN_MAGIE_AUTO_SOIN

    def get_titre(self,observation):
        return f"Magie d'auto-soin (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de soin","Elle affecte uniquement le lanceur.","Plus efficace et moins couteuse que la version classique.",f"Coût : {self.cout_pm} PMs",f"Soin : {self.gain_pv} PVs",f"Latence : {self.latence}"]

class Soin_case(On_post_action):
    """Un effet de soin. À répercuter sur les occupants éventuels de la case."""
    def __init__(self,gain_pv,responsable=0,cible="alliés"):
        self.phase = "démarrage"
        self.gain_pv = gain_pv
        self.responsable = responsable
        self.cible = cible
        self.affiche = True

    def action(self,case,position):
        cibles_potentielles = case.controleur.trouve_agissants_courants(position)
        for cible_potentielle in cibles_potentielles:
            if self.responsable == 0: #Pas de responsable. Sérieusement ?
                case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))
            else:
                esprit = case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit)
                if esprit == None: #Pas d'esprit ? Sérieusement ?
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))
                elif self.cible == "alliés" and cible_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_corps():
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))
                elif self.cible == "neutres" and not cible_potentielle in case.controleur.get_esprit(case.controleur.get_entitee(self.responsable).esprit).get_ennemis():
                    case.controleur.get_entitee(cible_potentielle).effets.append(Soin(self.responsable,self.gain_pv))

    def execute(self,case,position):
        if self.phase == "démarrage" :
            self.action(case,position)
            self.termine()

class Soin(On_fin_tour):
    """Un effet de soin. Généralement placé sur l'agissant par une magie de soin, de soin de zone, ou d'auto-soin."""
    def __init__(self,responsable,gain_pv):
        self.phase = "démarrage"
        self.responsable = responsable
        self.gain_pv = gain_pv
        self.affiche = True

    def action(self,porteur):
        porteur.soigne(self.gain_pv)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

    def get_skin(self):
        return SKIN_SOIN

class Magie_resurection(Magie):
    """La magie qui invoque un effet de resurection."""
    nom = "magie resurection"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_resurection[niveau-1]
        self.cout_pm = cout_pm_resurection[niveau-1]
        self.latence = latence_resurection[niveau-1]
        self.affiche = True

    def action(self,lanceur):
        ID_cadavre = lanceur.inventaire.get_item_courant()
        cadavre = lanceur.controleur.get_entitee(ID_cadavre)
        if cadavre.get_classe() == Cadavre:
            lanceur.inventaire.drop(lanceur.position)
            cadavre.effets.append(Resurection())

    def get_image(self):
        return SKIN_MAGIE_RESURECTION

    def get_titre(self,observation):
        return f"Magie de résurection (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de résurection","Elle ramène un cadavre à la vie.","Le cadavre doit être dans l'inventaire du lanceur.","L'agissant rescussité récupère l'intégralité de ses PVs, mais pas ses PMs. Il ne récupère pas son équippement, son argent ou ses effets, même permanents. Il ne rejoint pas le responsable de la resurection.",f"Coût : {self.cout_pm} PMs",f"Latence : {self.latence}"]

class Resurection(On_fin_tour):
    """Un effet de résurection. Généralement placé sur le cadavre par une magie de résurection. Rend tous les pv et ne change pas l'appartenance à un groupe."""
    def __init__(self):
        self.phase = "démarrage"
        self.affiche = False

    def action(self,porteur):
        porteur.pv = porteur.pv_max
        porteur.etat = "vivant"

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

class Magie_reanimation_de_zone(Cible_case,Portee_limitee):
    """La magie qui invoque un effet de reanimation sur tous les cadavres d'une zone."""
    nom = "magie reanimation"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_reanimation[niveau-1]
        self.cout_pm = cout_pm_reanimation[niveau-1]
        self.latence = latence_reanimation[niveau-1]
        self.taux_pv = taux_pv_reanimation[niveau-1]
        self.portee = portee_reanimation[niveau-1]
        self.portee_limite = portee_limite_reanimation[niveau-1]
        self.superiorite = superiorite_reanimation[niveau-1]
        self.temps = 10000
        self.cible = None
        self.affiche = True

    def action(self,porteur):
        cadavres = porteur.controleur.get_cadavres_touches(self.cible,self.portee)
        esprit = porteur.controleur.get_esprit(porteur.get_esprit())
        for cadavre in cadavres:
            if cadavre.get_priorite()+self.superiorite < porteur.get_priorite():
                cadavre.effets.append(Reanimation(self.taux_pv,esprit))

    def get_image(self):
        return SKIN_MAGIE_REANIMATION_ZONE

    def get_titre(self,observation):
        return f"Magie de réanimation (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de réanimation","Elle affecte tous les cadavres dans une zone à proximité du lanceur.","L'agissant rescussité récupère une partie de ses PVs, mais pas ses PMs. Il ne récupère pas son équippement, son argent ou ses effets, même permanents. Il rejoint le responsable de la réanimation. La réanimation échoue si la priorité de l'agissant est trop haut par rapport au responsable.",f"Coût : {self.cout_pm} PMs",f"PVs rendus : {self.taux_pv} des PVs max",f"Différence de priorité : {self.superiorite}",f"Portée de la zone de réanimation : {self.portee}",f"Portée du centre de la zone (par rapport au joueur) : {self.portee_limite}",f"Latence : {self.latence}"]

class Reanimation(On_fin_tour):
    """Un effet de réanimation. Généralement placé sur le cadavre par une magie de réanimation de zone ou un skill de réanimation."""
    def __init__(self,taux,esprit):
        self.phase = "démarrage"
        self.taux = taux
        self.esprit = esprit
        self.affiche = False

    def action(self,porteur):
        porteur.pv = porteur.pv_max*self.taux
        porteur.etat = "vivant"
        if self.esprit != None:
            esprit_porteur = porteur.controleur.get_esprit(porteur)
            if esprit_porteur != None:
                esprit_porteur.retire_corp(porteur)
            self.esprit.ajoute_corp(porteur)

    def execute(self,porteur):
        if self.phase == "démarrage" :
            self.action(porteur)
            self.termine()

# C'est tout pour les soins et assimilés.
# On passe aux projectiles :

class Magie_boule_de_feu(Magie_dirigee):
    """La magie qui invoque une boule de feu."""
    nom = "magie boule de feu"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_boule_de_feu[niveau-1]
        self.cout_pm = cout_pm_boule_de_feu[niveau-1]
        self.latence = latence_boule_de_feu[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Boule_de_feu(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_image(self):
        return SKIN_MAGIE_BOULE_DE_FEU

    def get_titre(self,observation):
        return f"Magie de boule de feu (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de projectile","Invoque une boule de feu de niveau {self.niveau} à l'emplacement du lanceur.","La boule de feu explose au contact d'un agissant ou d'un mur et inflige des dégats de feu aux cases voisines.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_boule_de_feu[self.niveau-1]}",f"Portée de l'explosion : {portee_boule_de_feu[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_fleche_de_glace(Magie_dirigee):
    """La magie qui invoque une flèche de glace."""
    nom = "magie fleche de glace"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_fleche_de_glace[niveau-1]
        self.cout_pm = cout_pm_fleche_de_glace[niveau-1]
        self.latence = latence_fleche_de_glace[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Fleche_de_glace(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_image(self):
        return SKIN_MAGIE_FLECHE_DE_GLACE

    def get_titre(self,observation):
        return f"Magie de flèche de glace (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de projectile","Invoque une flèche de glace de niveau {self.niveau} à l'emplacement du lanceur.","La flèche de glace inflige des dégats de glace au contact d'un agissant et poursuit sa course si l'agissant meurt.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_fleche_de_glace[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_rocher(Magie_dirigee):
    """La magie qui invoque un rocher."""
    nom = "magie rocher"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_rocher[niveau-1]
        self.cout_pm = cout_pm_rocher[niveau-1]
        self.latence = latence_rocher[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Rocher(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_image(self):
        return SKIN_MAGIE_ROCHER

    def get_titre(self,observation):
        return f"Magie de rocher (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de projectile","Invoque un rocher de niveau {self.niveau} à l'emplacement du lanceur.","Le rocher inflige des dégats de terre au contact d'un agissant.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_rocher[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_ombre_furtive(Magie_cible_dirigee,Cible_case,Portee_limitee):
    """La magie qui invoque une ombre futive."""
    nom = "magie ombre furtive"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_ombre_furtive[niveau-1]
        self.cout_pm = cout_pm_ombre_furtive[niveau-1]
        self.latence = latence_ombre_furtive[niveau-1]
        self.portee_limite = portee_ombre_furtive[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.direction = None
        self.temps = 10000
        self.temps_dir = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Ombre_furtive(self.niveau,self.cible,self.direction,porteur.ID))

    def get_image(self):
        return SKIN_MAGIE_OMBRE_FURTIVE

    def get_titre(self,observation):
        return f"Magie d'ombre furtive (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de projectile","Invoque une ombre furtive de niveau {self.niveau} à proximité du lanceur.","L'ombre furtive inflige des dégats d'ombre au contact d'un agissant.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_ombre_furtive[self.niveau-1]}",f"Portée (du point de lancement de l'ombre furtive par rapport au lanceur) : {portee_ombre_furtive[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_jet_de_mana(Magie_dirigee):
    """La magie qui invoque un jet de mana."""
    nom = "magie jet de mana"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_jet_de_mana[niveau-1]
        self.cout_pm = cout_pm_jet_de_mana[niveau-1]
        self.latence = latence_jet_de_mana[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Jet_de_mana(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_image(self):
        return SKIN_MAGIE_JET_DE_MANA

    def get_titre(self,observation):
        return f"Magie de jet de mana (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de projectile","Invoque un jet de mana de niveau {self.niveau} à l'emplacement du lanceur.","Le jet de mana inflige des dégats de terre au contact d'un agissant.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_jet_de_mana[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_eclair_noir(Magie_dirigee):
    """La magie qui invoque un éclair noir."""
    nom = "magie eclair noir"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_eclair_noir[niveau-1]
        self.cout_pm = cout_pm_eclair_noir[niveau-1]
        self.latence = latence_eclair_noir[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.ajoute_entitee(Eclair_noir(self.niveau,porteur.position,self.direction,porteur.ID))

    def get_image(self):
        return SKIN_MAGIE_ECLAIR_NOIR

    def get_titre(self,observation):
        return f"Magie d'éclair noir (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de projectile","Invoque un éclair noir {self.niveau} à l'emplacement du lanceur.","L'éclair noir inflige des dégats de terre au contact d'un agissant, explose au contact d'un mur ou d'un agissant et inflige des dégats de terre à proximité, et poursuit sa course si l'agissant meurt.",f"Coût : {self.cout_pm} PMs",f"Dégats de contact : {degats_choc_eclair_noir[self.niveau-1]}",f"Dégats d'explosion : {degats_explosifs_eclair_noir[self.niveau-1]}",f"Portée de l'explosion : {portee_eclair_noir[self.niveau-1]}",f"Latence : {self.latence}"]

# C'est tout pour les projectiles.
# On passe aux enchantements :

class Magie_enchantement_faiblesse(Enchante_agissant):
    """La magie qui place un enchantement de faiblesse sur un agissant."""
    nom = "magie faiblesse"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_faiblesse[niveau-1]
        self.cout_pm = cout_pm_faiblesse[niveau-1]
        self.latence = latence_faiblesse[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_force(duree_faiblesse[self.niveau-1],gain_force_faiblesse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE

    def get_titre(self,observation):
        return f"Enchantement de faiblesse (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de faiblesse réduit la force de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Réduction de la force : {gain_force_faiblesse[self.niveau-1]}",f"Durée de l'enchantement : {duree_faiblesse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_cecite(Enchante_agissant):
    """La magie qui place un enchantement de cécité sur un agissant."""
    nom = "magie cecite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_cecite[niveau-1]
        self.cout_pm = cout_pm_cecite[niveau-1]
        self.latence = latence_cecite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_vision(duree_cecite[self.niveau-1],gain_vision_cecite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_CECITE

    def get_titre(self,observation):
        return f"Enchantement de cécité (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de cécité réduit la portée de la vision de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Réduction de la vision : {gain_vision_cecite[self.niveau-1]}",f"Durée de l'enchantement : {duree_cecite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_perte_de_pv(Enchante_agissant):
    """La magie qui place un enchantement de perte de pv sur un agissant."""
    nom = "magie perte de pv"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_perte_de_pv[niveau-1]
        self.cout_pm = cout_pm_perte_de_pv[niveau-1]
        self.latence = latence_perte_de_pv[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pv(duree_perte_de_pv[self.niveau-1],gain_pv_perte_de_pv[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PV

    def get_titre(self,observation):
        return f"Enchantement de perte de PVs (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de perte de PVs retire des PVs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PVs perdus par tour : {gain_pv_perte_de_pv[self.niveau-1]}",f"Durée de l'enchantement : {duree_perte_de_pv[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_perte_de_pm(Enchante_agissant):
    """La magie qui place un enchantement de perte de pm sur un agissant."""
    nom = "magie perte de pm"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_perte_de_pm[niveau-1]
        self.cout_pm = cout_pm_perte_de_pm[niveau-1]
        self.latence = latence_perte_de_pm[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pm(duree_perte_de_pm[self.niveau-1],gain_pm_perte_de_pm[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PM

    def get_titre(self,observation):
        return f"Enchantement de perte de PMs (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de perte de PMs retire des PMs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PMs perdus par tour : {gain_pm_perte_de_pm[self.niveau-1]}",f"Durée de l'enchantement : {duree_perte_de_pm[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_confusion(Enchante_agissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    nom = "magie confusion"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_confusion[niveau-1]
        self.cout_pm = cout_pm_confusion[niveau-1]
        self.latence = latence_confusion[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_confusion(duree_confusion[self.niveau-1],taux_erreur_confusion[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_CONFUSION

    def get_titre(self,observation):
        return f"Enchantement de confusion (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de confusion pousse l'agissant à se tromper parfois de direction pour une certaine durée.","L'enchantement ne choisi pas la plus mauvaise direction, mais se contente de modifier la direction de l'agissant, l'agissant peut être quand-même efficace.",f"Coût : {self.cout_pm} PMs",f"Probabilité de se tromper de direction : {taux_erreur_confusion[self.niveau-1]}",f"Durée de l'enchantement : {duree_confusion[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_poches_trouees(Enchante_agissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    nom = "magie poches trouees"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poches_trouees[niveau-1]
        self.cout_pm = cout_pm_poches_trouees[niveau-1]
        self.latence = latence_poches_trouees[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_poches_trouees(duree_poches_trouees[self.niveau-1],taux_drop_poches_trouees[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_POCHES_TROUEES

    def get_titre(self,observation):
        return f"Enchantement de poches trouées (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de poches trouées pousse l'agissant à laisser parfois tomber des items de son inventaire pour une certaine durée.","L'item laché est choisi aléatoirement, et peut faire partie de l'équippement de l'agissant.",f"Coût : {self.cout_pm} PMs",f"Probabilité de laisser tomber un item : {taux_drop_poches_trouees[self.niveau-1]}",f"Durée de l'enchantement : {duree_poches_trouees[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_force(Enchante_agissant):
    """La magie qui place un enchantement de force sur un agissant."""
    nom = "magie force"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_force[niveau-1]
        self.cout_pm = cout_pm_force[niveau-1]
        self.latence = latence_force[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_force(duree_force[self.niveau-1],gain_force[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_FORCE

    def get_titre(self,observation):
        return f"Enchantement de force (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de force augmente la force de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la force : {gain_force[self.niveau-1]}",f"Durée de l'enchantement : {duree_force[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_vision(Enchante_agissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    nom = "magie vision"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_vision[niveau-1]
        self.cout_pm = cout_pm_vision[niveau-1]
        self.latence = latence_vision[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_vision(duree_vision[self.niveau-1],gain_vision[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_VISION

    def get_titre(self,observation):
        return f"Enchantement de vision (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de vision augmente la portée de la vision de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la vision : {gain_vision[self.niveau-1]}",f"Durée de l'enchantement : {duree_vision[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_vitalite(Enchante_agissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    nom = "magie vitalite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_vitalite[niveau-1]
        self.cout_pm = cout_pm_vitalite[niveau-1]
        self.latence = latence_vitalite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pv(duree_vitalite[self.niveau-1],gain_pv_vitalite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_VITALITE

    def get_titre(self,observation):
        return f"Enchantement de vitalité (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de vitalité donne des PVs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PVs gagnés par tour : {gain_pv_vitalite[self.niveau-1]}",f"Durée de l'enchantement : {duree_vitalite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_absorption(Enchante_agissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    nom = "magie absorption"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_absorption[niveau-1]
        self.cout_pm = cout_pm_absorption[niveau-1]
        self.latence = latence_absorption[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_pm(duree_absorption[self.niveau-1],gain_pm_absorption[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_ABSORPTION

    def get_titre(self,observation):
        return f"Enchantement d'absorption (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement d'absorption donne des PMs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PMs gagnés par tour : {gain_pm_absorption[self.niveau-1]}",f"Durée de l'enchantement : {duree_absorption[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_celerite(Enchante_agissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    nom = "magie celerite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_celerite[niveau-1]
        self.cout_pm = cout_pm_celerite[niveau-1]
        self.latence = latence_celerite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_vitesse(duree_celerite[self.niveau-1],gain_vitesse_celerite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_CELERITE

    def get_titre(self,observation):
        return f"Enchantement de célérité (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de célérité augmente la vitesse (le taux de diminution de la latence) de l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la vitesse : {gain_vitesse_celerite[self.niveau-1]}",f"Durée de l'enchantement : {duree_celerite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_immunite(Enchante_agissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    nom = "magie immunite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_immunite[niveau-1]
        self.cout_pm = cout_pm_immunite[niveau-1]
        self.latence = latence_immunite[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_immunite(duree_immunite[self.niveau-1],superiorite_immunite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_IMMUNITE

    def get_titre(self,observation):
        return f"Enchantement d'immunité (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement d'immunité retire les maladies de l'agissant à chaque tour pour une certaine durée.","Le retrait peut échouer si la priorité de la maladie est trop grande par rapport à celle de l'agissant.",f"Coût : {self.cout_pm} PMs",f"Différence de priorité : {superiorite_immunite[self.niveau-1]}",f"Durée de l'enchantement : {duree_immunite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_flamme(Enchante_agissant):
    """La magie qui place un enchantement de flamme sur un agissant."""
    nom = "magie flamme"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_flamme[niveau-1]
        self.cout_pm = cout_pm_flamme[niveau-1]
        self.latence = latence_flamme[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_flamme(duree_flamme[self.niveau-1],gain_affinite_flamme[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_FLAMME

    def get_titre(self,observation):
        return f"Enchantement de flamme (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de flamme augmente l'affinité au feu de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_flamme[self.niveau-1]}",f"Durée de l'enchantement : {duree_flamme[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_neige(Enchante_agissant):
    """La magie qui place un enchantement de neige sur un agissant."""
    nom = "magie neige"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_neige[niveau-1]
        self.cout_pm = cout_pm_neige[niveau-1]
        self.latence = latence_neige[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_neige(duree_neige[self.niveau-1],gain_affinite_neige[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_NEIGE

    def get_titre(self,observation):
        return f"Enchantement de neige (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de neige augmente l'affinité à la glace de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_neige[self.niveau-1]}",f"Durée de l'enchantement : {duree_neige[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_sable(Enchante_agissant):
    """La magie qui place un enchantement de sable sur un agissant."""
    nom = "magie sable"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_sable[niveau-1]
        self.cout_pm = cout_pm_sable[niveau-1]
        self.latence = latence_sable[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_sable(duree_sable[self.niveau-1],gain_affinite_sable[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_SABLE

    def get_titre(self,observation):
        return f"Enchantement de sable (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de sable augmente l'affinité à la terre de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_sable[self.niveau-1]}",f"Durée de l'enchantement : {duree_sable[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_tenebre(Enchante_agissant):
    """La magie qui place un enchantement de ténèbre sur un agissant."""
    nom = "magie tenebre"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_tenebre[niveau-1]
        self.cout_pm = cout_pm_tenebre[niveau-1]
        self.latence = latence_tenebre[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_tenebre(duree_tenebre[self.niveau-1],gain_affinite_tenebre[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_TENEBRE

    def get_titre(self,observation):
        return f"Enchantement de ténèbre (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de ténèbre augmente l'affinité à l'ombre de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_tenebre[self.niveau-1]}",f"Durée de l'enchantement : {duree_tenebre[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_rouille(Enchante_item): #Il faudrait cibler un item visible, équippé par un agissant proche
    """La magie qui place un enchantement de rouille sur un item."""
    nom = "magie rouille"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_rouille[niveau-1]
        self.cout_pm = cout_pm_rouille[niveau-1]
        self.latence = latence_rouille[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_arme(duree_rouille[self.niveau-1],gain_force_rouille[self.niveau-1],gain_portee_rouille[self.niveau-1])) #Comment affecter aussi les autres types d'équippement ?

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_ROUILLE

    def get_titre(self,observation):
        return f"Enchantement de rouille (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un item à proximité du lanceur.","L'enchantement de rouille diminue l'efficacité de l'item pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Réduction de la force (pour une arme) : {gain_force_rouille[self.niveau-1]}",f"Réduction de la portee (pour une arme) : {gain_portee_rouille[self.niveau-1]}",f"Durée de l'enchantement : {duree_rouille[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_renforcement(Enchante_item):
    """La magie qui place un enchantement de renforcement sur un item."""
    nom = "magie renforcement"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_renforcement[niveau-1]
        self.cout_pm = cout_pm_renforcement[niveau-1]
        self.latence = latence_renforcement[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_arme(duree_renforcement[self.niveau-1],gain_force_renforcement[self.niveau-1],gain_portee_renforcement[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT

    def get_titre(self,observation):
        return f"Enchantement de renforcement (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un item à proximité du lanceur.","L'enchantement de renforcement augmente l'efficacité de l'item pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la force (pour une arme) : {gain_force_renforcement[self.niveau-1]}",f"Augmentation de la portee (pour une arme) : {gain_portee_renforcement[self.niveau-1]}",f"Durée de l'enchantement : {duree_renforcement[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_bombe(Enchante_item):
    """La magie qui place un enchantement de bombe sur un item."""
    nom = "magie bombe"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_bombe[niveau-1]
        self.cout_pm = cout_pm_bombe[niveau-1]
        self.latence = latence_bombe[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Enchantement_bombe(duree_bombe[self.niveau-1],On_hit(portee_bombe[self.niveau-1],degats_bombe[self.niveau-1])))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_BOMBE

    def get_titre(self,observation):
        return f"Enchantement de bombe (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Un enchantement","Affecte un item à proximité du lanceur.","L'enchantement de bombe confère un effet explosif à l'item pour une certaine durée (s'il est lancé, il explose au contact d'un agissant ou d'un mur et inflige des dégats de terre aux agissants à proximité).",f"Coût : {self.cout_pm} PMs",f"Dégats de l'explosion : {degats_bombe[self.niveau-1]}",f"Portee de l'explosion : {portee_bombe[self.niveau-1]}",f"Durée de l'enchantement : {duree_bombe[self.niveau-1]}",f"Latence : {self.latence}"]

# C'est tout pour les enchantements.
# On passe aux magies diverses :

class Magie_reserve(Magie_cout):
    """La magie qui fait une réserve de mana."""
    nom = "magie reserve"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_reserve[niveau-1]
        self.cout_pm = 0
        self.latence = latence_reserve[niveau-1]
        self.niveau = niveau
        self.temps = 100000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Reserve_mana(self.cout_pm*taux_reserve[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_RESERVE

    def get_titre(self,observation):
        return f"Magie de réserve (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de réserve","Stocke des PMs, en surplus de la limite de PMs.","Les PMs stocké sont utilisés lorsque les PMs standard sont épuisés. La quantité de PMs dans la réserve dépend de la quantité dépensée lors du lancement du sort.",f"Taux de stockage : {taux_reserve[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_investissement(Magie_cout):
    """La magie qui crée un investissement."""
    nom = "magie investissement"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_investissement[niveau-1]
        self.cout_pm = 0
        self.latence = latence_investissement[niveau-1]
        self.niveau = niveau
        self.temps = 100000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Investissement_mana(duree_investissement[self.niveau-1],self.cout_pm*taux_investissement[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_INVESTISSEMENT

    def get_titre(self,observation):
        return f"Magie d'investissement (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'investissement","Rend après un certain temps plus de PMs qu'il n'en a été dépensés pour lancer le sort.",f"Taux de rendement : {taux_investissement[self.niveau-1]}",f"Temps d'attente : {duree_investissement[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_explosion_de_mana(Magie_cout):
    """La magie qui crée une explosion de mana."""
    nom = "magie explosion de mana"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_explosion_de_mana[niveau-1]
        self.cout_pm = 0
        self.latence = latence_explosion_de_mana[niveau-1]
        self.niveau = niveau
        self.temps = 100000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,self.cout_pm*taux_degats_explosion_de_mana[self.niveau-1],TERRE,"contact",portee_explosion_de_mana[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_EXPLOSION_DE_MANA

    def get_titre(self,observation):
        return f"Magie d'explosion de mana (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés à proximité.","Les dégats dépendent des PMs dépensés pour lancer le sort",f"Taux de dégats : {taux_degats_explosion_de_mana[self.niveau-1]}",f"Portee de l'attaque : {portee_explosion_de_mana[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_laser(Magie_dirigee):
    """La magie qui crée une attaque de laser."""
    nom = "magie laser"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_laser[niveau-1]
        self.cout_pm = cout_pm_laser[niveau-1]
        self.latence = latence_laser[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_laser[self.niveau-1],TERRE,'proximité',portee_laser[self.niveau-1],"R__T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_LASER

    def get_titre(self,observation):
        return f"Magie de laser (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés en ligne droite et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_laser[self.niveau-1]}",f"Portee de l'attaque : {portee_laser[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_magique(Magie_dirigee): #À modifier selon l'espèce qui l'utilise
    """La magie qui crée une attaque de poing magique."""
    nom = "magie poing magique"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_magique[niveau-1]
        self.cout_pm = cout_pm_poing_magique[niveau-1]
        self.latence = latence_poing_magique[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_poing_magique[self.niveau-1],TERRE,"contact",portee_poing_magique[self.niveau-1],"Sd_T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation):
        return f"Magie de poing magique (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_poing_magique[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_magique[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_ardent(Magie_dirigee): #L'attaque de mélée de la bombe atomique
    """La magie qui crée une attaque de poing ardent."""
    nom = "magie poing ardent"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_ardent[niveau-1]
        self.cout_pm = cout_pm_poing_ardent[niveau-1]
        self.latence = latence_poing_ardent[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_poing_ardent[self.niveau-1],FEU,"contact",portee_poing_ardent[self.niveau-1],"Sd_T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation):
        return f"Magie de poing ardent (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_poing_ardent[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_ardent[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_poing_sombre(Magie_dirigee):
    """La magie qui crée une attaque de poing sombre."""
    nom = "magie poing sombre"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poing_sombre[niveau-1]
        self.cout_pm = cout_pm_poing_sombre[niveau-1]
        self.latence = latence_poing_sombre[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_poing_sombre[self.niveau-1],OMBRE,"contact",portee_poing_sombre[self.niveau-1],"Sd_T___",self.direction))

    def get_image(self):
        return SKIN_MAGIE_POING_MAGIQUE

    def get_titre(self,observation):
        return f"Magie de poing sombre (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants non-alliés devant le lanceur et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_poing_sombre[self.niveau-1]}",f"Portee de l'attaque : {portee_poing_sombre[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_brasier(Magie):
    """La magie qui crée une attaque de brasier."""
    nom = "magie brasier"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_brasier[niveau-1]
        self.cout_pm = cout_pm_brasier[niveau-1]
        self.latence = latence_brasier[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_brasier[self.niveau-1],FEU,"proximité",portee_brasier[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation):
        return f"Magie de brasier (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_brasier[self.niveau-1]}",f"Portee de l'attaque : {portee_brasier[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_avalanche(Magie_dirigee):
    """La magie qui crée une attaque d'avalanche."""
    nom = "magie avalanche"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_avalanche[niveau-1]
        self.cout_pm = cout_pm_avalanche[niveau-1]
        self.latence = latence_avalanche[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_magique(porteur.ID,degats_avalanche[self.niveau-1],TERRE,"proximité",portee_avalanche[self.niveau-1],"S__S_Pb",self.direction))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation):
        return f"Magie d'avalanche (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants devant et à proximité.",f"Coût : {self.cout_pm}",f"Degats : {degats_avalanche[self.niveau-1]}",f"Portee de l'attaque : {portee_avalanche[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_blizzard(Magie):
    """La magie qui crée un effet de blizzard autour de l'agissant."""
    nom = "magie blizzard"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_blizzard[niveau-1]
        self.cout_pm = cout_pm_blizzard[niveau-1]
        self.latence = latence_blizzard[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,portee_blizzard[self.niveau-1])
        for case in cases:
            case.effets.append(Blizzard(self.niveau))

    def get_image(self):
        return SKIN_MAGIE_BLIZZARD

    def get_titre(self,observation):
        return f"Magie de blizzard (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de blizzard","Affecte les cases à proximité du lanceur.","Le blizzard augmente à chaque tour le latence de l'agissant sur la case. Si la vitesse de l'agissant n'est pas suffisante pour compenser la latence supplémentaire, l'agissant sur la case est immobilisé. Le lanceur est affecté par le blizzard.",f"Coût : {self.cout_pm}",f"Portee de la magie : {portee_blizzard[self.niveau-1]}",f"Latence supplémentaire : {gain_latence_blizzard[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_obscurite(Magie):
    """La magie qui crée un effet d'obscurite autour de l'agissant."""
    nom = "magie obscurite"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_obscurite[niveau-1]
        self.cout_pm = cout_pm_obscurite[niveau-1]
        self.latence = latence_obscurite[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        cases = porteur.controleur.get_cases_touches(porteur.position,portee_obscurite[self.niveau-1])
        for case in cases:
            case.effets.append(Obscurite(self.niveau))

    def get_image(self):
        return SKIN_MAGIE_OBSCURITE

    def get_titre(self,observation):
        return f"Magie d'obscurité (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'obscurité","Affecte les cases à proximité du lanceur.","L'obscurité augmente l'opacité des cases, rendant plus difficile de voir au travers.",f"Coût : {self.cout_pm}",f"Portee de la magie : {portee_obscurite[self.niveau-1]}",f"Opacité supplémentaire : {gain_opacite_obscurite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_dopage(Magie):
    """La magie qui crée un effet de dopage sur l'agissant."""
    nom = "magie dopage"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_dopage[niveau-1]
        self.cout_pm = cout_pm_dopage[niveau-1]
        self.latence = latence_dopage[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Dopage(porteur.ID,taux_dopage[self.niveau-1],duree_dopage[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation):
        return f"Magie de dopage (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de boost","Affecte le lanceur.","Les dégats de la prochaine attaque du lanceur sont augentés.",f"Coût : {self.cout_pm}",f"Taux de dégats : {taux_dopage[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_boost(Cible_agissant):
    """La magie qui crée un effet de dopage sur un autre agissant."""
    nom = "magie boost"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_boost[niveau-1]
        self.cout_pm = cout_pm_boost[niveau-1]
        self.latence = latence_boost[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Dopage(porteur.ID,taux_boost[self.niveau-1],duree_boost[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation):
        return f"Magie de boost (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de boost","Affecte un agissant en vue du lanceur.","Les dégats de la prochaine attaque de l'agissant sont augentés.",f"Coût : {self.cout_pm}",f"Taux de dégats : {taux_boost[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_multi_boost(Cible_agissant,Multi_cible):
    """La magie qui crée un effet de dopage sur plusieurs autres agissants."""
    nom = "magie multi boost"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_multi_boost[niveau-1]
        self.cout_pm = cout_pm_multi_boost[niveau-1]
        self.latence = latence_multi_boost[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        for cible in self.cible:
            porteur.controleur.get_entitee(cible).effets.append(Dopage(porteur.ID,taux_multi_boost[self.niveau-1],duree_multi_boost[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_DOPAGE

    def get_titre(self,observation):
        return f"Magie de multi-boost (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de boost","Affecte un ou plusieurs agissants en vue du lanceur.","Les dégats de la prochaine attaque des agissants sont augentés.",f"Coût : {self.cout_pm}",f"Taux de dégats : {taux_multi_boost[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_instakill(Magie_cible):
    """La magie qui crée un effet d'instakill sur un agissant."""
    nom = "magie instakill"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_instakill[niveau-1]
        self.cout_pm = cout_pm_instakill[niveau-1]
        self.latence = latence_instakill[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.controleur.get_entitee(self.cible).effets.append(Instakill(porteur.ID,porteur.priorite - superiorite_instakill[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_INSTAKILL

    def get_titre(self,observation):
        return f"Magie de mort instantannée (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de mort instantannée","Affecte un agissant en vue du lanceur.","L'agissant meurt instantannément. S'il est immortel, ses PVs et ses PMs sont réduits à 0.","Le sort peut échouer si la priorité de l'agissant est trop élevée comparée à celle du lanceur.",f"Coût : {self.cout_pm}",f"Différence de priorité : {superiorite_instakill[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_purification(Magie):
    """La magie qui crée un effet de purification sur un agissant."""
    nom = "magie purification"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_purification[niveau-1]
        self.cout_pm = cout_pm_purification[niveau-1]
        self.latence = latence_purification[niveau-1]
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Purification_lumineuse(porteur.ID,degats_purification[self.niveau-1],portee_purification[self.niveau-1])) #Ajouter une direction ?

    def get_image(self):
        return SKIN_MAGIE_PURIFICATION

    def get_titre(self,observation):
        return f"Magie de purification (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de purification","Inflige des dégats aux agissants à proximité du lanceur.","Les dégats sont inversement proportionnels à l'affinité à l'ombre.","La purification n'est pas une attaque, mais se comporte comme telle.",f"Coût : {self.cout_pm}",f"Dégats : {degats_purification[self.niveau-1]}",f"Portée : {portee_purification[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_protection_sacree(Multi_cible,Cible_agissant):
    """La magie qui crée un effet de protection sacrée sur des agissants."""
    nom = "magie protection sacrée"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_protection_sacree[niveau-1]
        self.cout_pm = cout_pm_protection_sacree[niveau-1]
        self.latence = latence_protection_sacree[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        for ID in self.cible:
            porteur.controleur.get_entitee(ID).effets.append(Protection_sacree(duree_protection_sacree[self.niveau-1],pv_protection_sacree[self.niveau-1])) #Ajouter une direction ?

    def get_image(self):
        return SKIN_MAGIE_PROTECTION_SACREE

    def get_titre(self,observation):
        return f"Magie de protection sacrée (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de protection","Bloque les dégats des attaques entrantes jusqu'à une certaine somme.","Les dégats d'ombre sont plus affectés.",f"Coût : {self.cout_pm}",f"Dégats absorbables : {pv_protection_sacree[self.niveau-1]}",f"Durée : {duree_protection_sacree[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_volcan(Cible_case):
    """La magie qui crée une attaque de feu à un autre endroit."""
    nom = "magie volcan"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_volcan[niveau-1]
        self.cout_pm = cout_pm_volcan[niveau-1]
        self.latence = latence_volcan[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_decentree_delayee(self.cible,delai_volcan[self.niveau-1],porteur.ID,degats_volcan[self.niveau-1],FEU,"distance",portee_volcan[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_BRASIER

    def get_titre(self,observation):
        return f"Magie de volcan (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de feu aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout_pm}",f"Dégats : {degats_volcan[self.niveau-1]}",f"Portée : {portee_volcan[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_secousse(Cible_case):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie secousse"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_secousse[niveau-1]
        self.cout_pm = cout_pm_secousse[niveau-1]
        self.latence = latence_secousse[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_decentree_delayee(self.cible,delai_secousse[self.niveau-1],porteur.ID,degats_secousse[self.niveau-1],TERRE,"distance",portee_secousse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation):
        return f"Magie de secousse (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout_pm}",f"Dégats : {degats_secousse[self.niveau-1]}",f"Portée : {portee_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_petite_secousse(Cible_case):
    """La magie qui crée une attaque de terre à un autre endroit. Pas très puissant."""
    nom = "magie petite secousse"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_petite_secousse[niveau-1]
        self.cout_pm = cout_pm_petite_secousse[niveau-1]
        self.latence = latence_petite_secousse[niveau-1]
        self.niveau = niveau
        self.cible = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur):
        porteur.effets.append(Attaque_decentree_delayee(self.cible,delai_petite_secousse[self.niveau-1],porteur.ID,degats_petite_secousse[self.niveau-1],TERRE,"distance",portee_petite_secousse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_AVALANCHE

    def get_titre(self,observation):
        return f"Magie de petite secousse (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie d'attaque","Inflige des dégats de terre aux agissants à proximité d'une case en vue de lanceur.",f"Coût : {self.cout_pm}",f"Dégats : {degats_petite_secousse[self.niveau-1]}",f"Portée : {portee_petite_secousse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_teleportation(Multi_cible,Cible_case):
    """La magie qui téléporte des entitées."""
    nom = "magie téléportation"
    def __init__(self,niveau):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_teleportation[niveau-1]
        self.cout_pm = cout_pm_teleportation[niveau-1]
        self.latence = latence_teleportation[niveau-1]
        self.cible = None
        self.temps = 100000
        self.niveau = niveau
        self.affiche = True

    def action(self,porteur):
        for i in range(len(self.cible)):
            for ID in porteur.controleur.trouve_occupants(self.cible[i]):
                porteur.controleur.get_entitee(ID).effets.append(Teleportation(self.cible[i-1]))

    def get_image(self):
        return SKIN_MAGIE_TELEPORTATION

    def get_titre(self,observation):
        return f"Magie de téléportation (niveau {self.niveau})"

    def get_description(self,observation):
        return ["Une magie de téléportation","Affecte les entitées sur les cases sélectionnées.","Les entitées de chaque case sont déplacées sur la case précédente. Les entitées de la première case sont envoyées sur la dernière case.",f"Coût : {self.cout_pm}",f"Latence : {self.latence}"]

from Jeu.Entitees.Item.Items import *
from Jeu.Entitees.Agissant.Agissant import *