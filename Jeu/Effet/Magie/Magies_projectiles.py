from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Jeu.Effet.Magie.Magie import Magie_dirigee,Magie_cible_dirigee,Cible_case,Portee_limitee

class Magie_boule_de_feu(Magie_dirigee):
    """La magie qui invoque une boule de feu."""
    nom = "magie boule de feu"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_boule_de_feu[niveau-1]
        self.cout_pm = cout_pm_boule_de_feu[niveau-1]
        self.latence = latence_boule_de_feu[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.direction is not None
        porteur.controleur.ajoute_entitee(Boule_de_feu(porteur.controleur,self.niveau,self.direction,porteur,porteur.position))

    def get_image(self):
        return SKIN_MAGIE_BOULE_DE_FEU

    def get_titre(self,observation=0):
        return f"Magie de boule de feu (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de projectile","Invoque une boule de feu de niveau {self.niveau} à l'emplacement du lanceur.","La boule de feu explose au contact d'un agissant ou d'un mur et inflige des dégats de feu aux cases voisines.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_boule_de_feu[self.niveau-1]}",f"Portée de l'explosion : {portee_boule_de_feu[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_fleche_de_glace(Magie_dirigee):
    """La magie qui invoque une flèche de glace."""
    nom = "magie fleche de glace"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_fleche_de_glace[niveau-1]
        self.cout_pm = cout_pm_fleche_de_glace[niveau-1]
        self.latence = latence_fleche_de_glace[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.direction is not None
        porteur.controleur.ajoute_entitee(Fleche_de_glace(porteur.controleur,self.niveau,self.direction,porteur,porteur.position))

    def get_image(self):
        return SKIN_MAGIE_FLECHE_DE_GLACE

    def get_titre(self,observation=0):
        return f"Magie de flèche de glace (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de projectile","Invoque une flèche de glace de niveau {self.niveau} à l'emplacement du lanceur.","La flèche de glace inflige des dégats de glace au contact d'un agissant et poursuit sa course si l'agissant meurt.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_fleche_de_glace[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_rocher(Magie_dirigee):
    """La magie qui invoque un rocher."""
    nom = "magie rocher"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_rocher[niveau-1]
        self.cout_pm = cout_pm_rocher[niveau-1]
        self.latence = latence_rocher[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.direction is not None
        porteur.controleur.ajoute_entitee(Rocher(porteur.controleur,self.niveau,self.direction,porteur,porteur.position))

    def get_image(self):
        return SKIN_MAGIE_ROCHER

    def get_titre(self,observation=0):
        return f"Magie de rocher (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de projectile","Invoque un rocher de niveau {self.niveau} à l'emplacement du lanceur.","Le rocher inflige des dégats de terre au contact d'un agissant.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_rocher[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_ombre_furtive(Magie_cible_dirigee,Cible_case,Portee_limitee):
    """La magie qui invoque une ombre futive."""
    nom = "magie ombre furtive"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_ombre_furtive[niveau-1]
        self.cout_pm = cout_pm_ombre_furtive[niveau-1]
        self.latence = latence_ombre_furtive[niveau-1]
        self.portee_limite = portee_ombre_furtive[niveau-1]
        self.niveau = niveau
        self.cible:Position = ABSENT
        self.direction = None
        self.temps = 10000
        self.temps_dir = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.direction is not None
        porteur.controleur.ajoute_entitee(Ombre_furtive(porteur.controleur,self.niveau,self.direction,porteur,self.cible))

    def get_image(self):
        return SKIN_MAGIE_OMBRE_FURTIVE

    def get_titre(self,observation=0):
        return f"Magie d'ombre furtive (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de projectile","Invoque une ombre furtive de niveau {self.niveau} à proximité du lanceur.","L'ombre furtive inflige des dégats d'ombre au contact d'un agissant.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_ombre_furtive[self.niveau-1]}",f"Portée (du point de lancement de l'ombre furtive par rapport au lanceur) : {portee_ombre_furtive[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_jet_de_mana(Magie_dirigee):
    """La magie qui invoque un jet de mana."""
    nom = "magie jet de mana"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_jet_de_mana[niveau-1]
        self.cout_pm = cout_pm_jet_de_mana[niveau-1]
        self.latence = latence_jet_de_mana[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.direction is not None
        porteur.controleur.ajoute_entitee(Jet_de_mana(porteur.controleur,self.niveau,self.direction,porteur,porteur.position))

    def get_image(self):
        return SKIN_MAGIE_JET_DE_MANA

    def get_titre(self,observation=0):
        return f"Magie de jet de mana (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de projectile","Invoque un jet de mana de niveau {self.niveau} à l'emplacement du lanceur.","Le jet de mana inflige des dégats de terre au contact d'un agissant.",f"Coût : {self.cout_pm} PMs",f"Dégats : {degats_jet_de_mana[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_eclair_noir(Magie_dirigee):
    """La magie qui invoque un éclair noir."""
    nom = "magie eclair noir"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_eclair_noir[niveau-1]
        self.cout_pm = cout_pm_eclair_noir[niveau-1]
        self.latence = latence_eclair_noir[niveau-1]
        self.niveau = niveau
        self.direction = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.direction is not None
        porteur.controleur.ajoute_entitee(Eclair_noir(porteur.controleur,self.niveau,self.direction,porteur,porteur.position))

    def get_image(self):
        return SKIN_MAGIE_ECLAIR_NOIR

    def get_titre(self,observation=0):
        return f"Magie d'éclair noir (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Une magie de projectile","Invoque un éclair noir {self.niveau} à l'emplacement du lanceur.","L'éclair noir inflige des dégats de terre au contact d'un agissant, explose au contact d'un mur ou d'un agissant et inflige des dégats de terre à proximité, et poursuit sa course si l'agissant meurt.",f"Coût : {self.cout_pm} PMs",f"Dégats de contact : {degats_choc_eclair_noir[self.niveau-1]}",f"Dégats d'explosion : {degats_explosifs_eclair_noir[self.niveau-1]}",f"Portée de l'explosion : {portee_eclair_noir[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Entitee.Item.Projectile.Projectiles import Eclair_noir, Jet_de_mana, Ombre_furtive, Boule_de_feu, Rocher, Fleche_de_glace
from Affichage.Skins.Skins import SKIN_MAGIE_ECLAIR_NOIR, SKIN_MAGIE_BOULE_DE_FEU, SKIN_MAGIE_JET_DE_MANA, SKIN_MAGIE_OMBRE_FURTIVE, SKIN_MAGIE_ROCHER, SKIN_MAGIE_FLECHE_DE_GLACE
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT