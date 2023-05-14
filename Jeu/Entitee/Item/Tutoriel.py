from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Jeu.Entitee.Item.Equippement.Armure.Armure import Armure
from Jeu.Entitee.Item.Equippement.Degainable.Lance.Lance import Lance
from Jeu.Entitee.Item.Equippement.Degainable.Epee.Epee import Epee
from Jeu.Entitee.Item.Equippement.Haume.Haume import Haume
from Jeu.Entitee.Item.Equippement.Anneau.Anneau import Anneau
from Jeu.Entitee.Item.Equippement.Role.Defensif.Defensifs import Defensif_valeur, Defensif_proportion, Defensif_plafond
from Jeu.Entitee.Item.Equippement.Role.Accelerateur import Accelerateur
from Jeu.Entitee.Item.Equippement.Role.Anoblisseur import Anoblisseur
from Jeu.Entitee.Item.Equippement.Role.Equippement_tribal import Equipement_tribal
from Jeu.Entitee.Item.Equippement.Role.Reparateur.Reparateurs import Pompe_a_pv
from Jeu.Entitee.Item.Equippement.Role.Reparateur_magique.Reparateurs_magiques import Pompe_a_pm
from Jeu.Entitee.Item.Equippement.Role.Elementaires import Rocheux
from Jeu.Entitee.Item.Item import Ingredient

# Valeurs par défaut des paramètres
from Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

#Quelques items pour le tutoriel :

class Armure_dor(Armure,Defensif_valeur):
    """L'armure du joueur, brisée dans la chute.""" #Vérifier si le joueur est chanceux !
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_valeur.__init__(self,1) #Chaque attaque est réduite de 1 dégat ! Est-ce trop pour une armure brisée ?
        self.poids = 10
        self.frottements = 10
        self.niveau = niveau
        self.nom = "armure_dor_cassee"

    def get_description(self,observation=0):
        return ["Une armure","Totalement_brisée"]

    def get_skin(self):
        return SKIN_ARMURE_DOR

class Lance_dor(Lance):
    """La lance du joueur, brisée dans la chute.""" #Vérifier si le joueur est chanceux !
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,TERRE,0.45,2,position) #Juste un peu moins de dégats que le stomp
        self.poids = 3
        self.frottements = 4
        self.niveau = niveau
        self.nom = "lance_dor_cassee"

    def get_description(self,observation=0):
        return ["Une lance","Totalement brisée"]

    def get_skin(self):
        return SKIN_LANCE_DOR

class Epee_epeiste(Epee):
    """Les épées des deux humains épéistes."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,TERRE,tranchant_epee_epeiste[niveau-1],portee_epee_epeiste[niveau-1],position)
        self.poids = poids_epee_epeiste[niveau-1]
        self.frottements = frottements_epee_epeiste[niveau-1]
        self.niveau = niveau
        self.nom = "epee_epeiste"

    def get_description(self,observation=0):
        return ["Une épée","Très bien entretenue"]

    def get_skin(self):
        return SKIN_EPEE

class Armure_epeiste(Armure,Defensif_proportion):
    """Les armures des deux humains épéistes."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats_armure_epeiste[niveau-1])
        self.poids = poids_armure_epeiste[niveau-1]
        self.frottements = frottements_armure_epeiste[niveau-1]
        self.niveau = niveau
        self.nom = "armure_epeiste"

    def get_description(self,observation=0):
        return ["Une armure","Un peu légère"]

    def get_skin(self):
        return SKIN_ARMURE_BASIQUE

class Tunique_enchantee(Armure,Defensif_proportion):
    """La tunique du mec paumé du deuxième étage. Étonnament résistante."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats_tunique_enchantee[niveau-1])
        self.poids = poids_tunique_enchantee[niveau-1]
        self.frottements = frottements_tunique_enchantee[niveau-1]
        self.niveau = niveau
        self.nom = "tunique_enchantee"

    def get_description(self,observation=0):
        return ["Une tunique","Un peu légère"]

    def get_skin(self):
        return SKIN_TUNIQUE_ENCHANTEE

class Robe_magique(Armure,Pompe_a_pm): #Lui donner un item plus utile, plus en lien avec ses capacités ?
    """La robe de la peureuse."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Pompe_a_pm.__init__(self,pm_robe_magique[niveau-1])
        self.poids = poids_robe_magique[niveau-1]
        self.frottements = frottements_robe_magique[niveau-1]
        self.niveau = niveau
        self.nom = "robe_magique"

    def get_description(self,observation=0):
        return ["Une robe","Probablement sans effet ?"]

    def get_skin(self):
        return SKIN_ROBE_MAGIQUE

class Tunique_alchimiste(Armure,Pompe_a_pm):
    """La tunique de l'alchimiste."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Pompe_a_pm.__init__(self,pm_tunique_alchimiste[niveau-1])
        self.poids = poids_tunique_alchimiste[niveau-1]
        self.frottements = frottements_tunique_alchimiste[niveau-1]
        self.niveau = niveau
        self.nom = "tunique_alchimiste"

    def get_description(self,observation=0):
        return ["Une tunique","A appartenu à un alchimiste"]

    def get_skin(self):
        return SKIN_TUNIQUE_ALCHIMISTE

class Soutane(Armure,Defensif_plafond):
    """La soutane de la sainte."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_plafond.__init__(self,degats_soutane[niveau-1])
        self.poids = poids_soutane[niveau-1]
        self.frottements = frottements_soutane[niveau-1]
        self.niveau = niveau
        self.nom = "soutane"

    def get_description(self,observation=0):
        return ["Une soutane","A appartenu à un pape,","il y a très longtemps."]

    def get_skin(self):
        return SKIN_SOUTANE

class Robe_de_sorciere(Armure,Pompe_a_pm): #Un peu redondant avec le chapeau...
    """La robe de la sorcière."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Pompe_a_pm.__init__(self,pm_robe_sorciere[niveau-1])
        self.poids = poids_robe_sorciere[niveau-1]
        self.frottements = frottements_robe_sorciere[niveau-1]
        self.niveau = niveau
        self.nom = "robe_sorciere"

    def get_description(self,observation=0):
        return ["Une robe","A appartenu à une magicienne"]

    def get_skin(self):
        return SKIN_ROBE_SORCIERE

class Chapeau_de_sorciere(Haume,Pompe_a_pm):
    """Le chapeau de la sorcière."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Haume.__init__(self,controleur,position)
        Pompe_a_pm.__init__(self,pm_chapeau_sorciere[niveau-1])
        self.poids = poids_chapeau_sorciere[niveau-1]
        self.frottements = frottements_chapeau_sorciere[niveau-1]
        self.niveau = niveau
        self.nom = "chapeau_sorciere"

    def get_description(self,observation=0):
        return ["Un chapeau","A appartenu à une magicienne"]

    def get_skin(self):
        return SKIN_CHAPEAU_DE_SORCIERE

class Armure_marchand(Armure,Defensif_valeur):
    """L'armure du marchand.""" #/!\ Faire spawner le marchand avec une armure qu'on retrouve plus tard dans le jeu, pas avec un équippement propre !
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_valeur.__init__(self,degats_armure_marchand[niveau-1])
        self.poids = poids_armure_marchand[niveau-1]
        self.frottements = frottements_armure_marchand[niveau-1]
        self.niveau = niveau
        self.nom = "armure_marchand"

    def get_description(self,observation=0):
        return ["Une armure","Plutôt solide !"]

    def get_skin(self):
        return SKIN_ARMURE_BASIQUE

class Epee_marchand(Epee):
    """L'épée du marchand.""" #/!\ Faire spawner le marchand avec une arme qu'on retrouve plus tard dans le jeu, pas avec un équippement propre ! (Une arme d'un autre élément que la terre par exemple ?)
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,GLACE,tranchant_epee_marchand[niveau-1],portee_epee_marchand[niveau-1],position)
        self.poids = poids_epee_marchand[niveau-1]
        self.frottements = frottements_epee_marchand[niveau-1]
        self.niveau = niveau
        self.nom = "epee_marchand"

    def get_description(self,observation=0):
        return ["Une épée","Avec une jolie teinte bleutée"]

    def get_skin(self):
        return SKIN_EPEE_MARCHAND

class Epee_de_gobelin(Epee,Equipement_tribal):
    """L'épée des gobelins de base. Ils en sont équippés à partir du niveau 5 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,TERRE,tranchant_epee_gobelin[niveau-1],portee_epee_gobelin[niveau-1],position)
        Equipement_tribal.__init__(self,"gobelin",taux_refus_epee_gobelin[niveau-1])
        self.poids = poids_epee_gobelin[niveau-1]
        self.frottements = frottements_epee_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Une épée","Elle est petite et mal entretenue"]

    def get_skin(self):
        return SKIN_EPEE_GOBELIN

class Lance_de_gobelin(Lance,Equipement_tribal):
    """La lance des sentinelles gobelins. Ils en sont équippés à partir du niveau 3 (peut-être moins ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,TERRE,tranchant_lance_gobelin[niveau-1],portee_lance_gobelin[niveau-1],position)
        Equipement_tribal.__init__(self,"gobelin",taux_refus_lance_gobelin[niveau-1])
        self.poids = poids_lance_gobelin[niveau-1]
        self.frottements = frottements_lance_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Une lance","Elle est petite et un peu rouillée"]

    def get_skin(self):
        return SKIN_LANCE_GOBELIN

class Cimetere_de_gobelin(Epee,Equipement_tribal):
    """L'épée des guerriers gobelins. Ils en sont équippés à partir du niveau 3 (peut-être moins ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Arme.__init__(self,controleur,TERRE,tranchant_cimetere_gobelin[niveau-1],portee_cimetere_gobelin[niveau-1],position)
        Equipement_tribal.__init__(self,"gobelin",taux_refus_cimetere_gobelin[niveau-1])
        self.poids = poids_cimetere_gobelin[niveau-1]
        self.frottements = frottements_cimetere_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Une épée","Il y a du sang sur la lame"]

    def get_skin(self):
        return SKIN_CIMETERE_GOBELIN

class Armure_sentinelle_gobelin(Armure,Defensif_proportion,Equipement_tribal):
    """L'armure des sentinelles gobelins. Ils en sont équippés à partir du niveau 3 (peut-être moins ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats_armure_sentinelle_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_armure_sentinelle_gobelin[niveau-1])
        self.poids = poids_armure_sentinelle_gobelin[niveau-1]
        self.frottements = frottements_armure_sentinelle_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Une armure","Elle a rétréci au lavage ?"]

    def get_skin(self):
        return SKIN_ARMURE_GOBELIN

class Armure_guerrier_gobelin(Armure,Defensif_proportion,Equipement_tribal):
    """L'armure des sentinelles gobelins. Ils en sont équippés à partir du niveau 3 (peut-être moins ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Armure.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats_armure_guerrier_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_armure_guerrier_gobelin[niveau-1])
        self.poids = poids_armure_guerrier_gobelin[niveau-1]
        self.frottements = frottements_armure_guerrier_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Une cote de maille","Avec plein de trous..."]

    def get_skin(self):
        return SKIN_ARMURE_GOBELIN

class Haume_de_gobelin(Haume,Defensif_proportion,Equipement_tribal):
    """Le casque des sentinelles gobelins. Ils en sont équippés à partir du niveau 5 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Haume.__init__(self,controleur,position)
        Defensif_proportion.__init__(self,taux_degats_haume_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_haume_gobelin[niveau-1])
        self.poids = poids_haume_gobelin[niveau-1]
        self.frottements = frottements_haume_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un casque","Un peu cabossé"]

    def get_skin(self):
        return SKIN_CASQUE_GOBELIN

class Bandeau_de_gobelin(Haume,Pompe_a_pm,Equipement_tribal):
    """Le bandeau des mages gobelins. Ils en sont équippés à partir du niveau 5 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Haume.__init__(self,controleur,position)
        Pompe_a_pm.__init__(self,pm_bandeau_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_bandeau_gobelin[niveau-1])
        self.poids = poids_bandeau_gobelin[niveau-1]
        self.frottements = frottements_bandeau_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un bout de tissu","Peut-être un peu magique ?"]

    def get_skin(self):
        return SKIN_BANDEAU_GOBELIN

class Anneau_terrestre_gobelin(Anneau,Rocheux,Equipement_tribal):
    """L'anneau d'affinité à la terre des chefs gobelins. Ils en sont équippés à partir du niveau 1 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Anneau.__init__(self,controleur,position)
        Rocheux.__init__(self,aff_anneau_terrestre_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_anneau_terrestre_gobelin[niveau-1])
        self.poids = poids_anneau_terrestre_gobelin[niveau-1]
        self.frottements = frottements_anneau_terrestre_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un anneau","Il a l'air taillé dans la pierre"]

    def get_skin(self):
        return SKIN_ANNEAU

class Anneau_magique_gobelin(Anneau,Pompe_a_pm,Equipement_tribal):
    """L'anneau de régénération de mana des chefs gobelins. Ils en sont équippés à partir du niveau 1 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Anneau.__init__(self,controleur,position)
        Pompe_a_pm.__init__(self,pm_anneau_magique_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_anneau_magique_gobelin[niveau-1])
        self.poids = poids_anneau_magique_gobelin[niveau-1]
        self.frottements = frottements_anneau_magique_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un anneau","Il y a d'étranges inscriptions autour"]

    def get_skin(self):
        return SKIN_ANNEAU

class Anneau_soin_gobelin(Anneau,Pompe_a_pv,Equipement_tribal):
    """L'anneau de soin des chefs gobelins. Ils en sont équippés à partir du niveau 1 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Anneau.__init__(self,controleur,position)
        Pompe_a_pv.__init__(self,pv_anneau_soin_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_anneau_soin_gobelin[niveau-1])
        self.poids = poids_anneau_soin_gobelin[niveau-1]
        self.frottements = frottements_anneau_soin_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un anneau","Enfile-le"]

    def get_skin(self):
        return SKIN_ANNEAU

class Anneau_vitesse_gobelin(Anneau,Accelerateur,Equipement_tribal):
    """L'anneau de vitesse des chefs gobelins. Ils en sont équippés à partir du niveau 1 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Anneau.__init__(self,controleur,position)
        Accelerateur.__init__(self,vitesse_anneau_vitesse_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_anneau_vitesse_gobelin[niveau-1])
        self.poids = poids_anneau_vitesse_gobelin[niveau-1]
        self.frottements = frottements_anneau_vitesse_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un anneau","Vite, enfile-le !"]

    def get_skin(self):
        return SKIN_ANNEAU

class Sceau_roi_gobelin(Anneau,Anoblisseur,Equipement_tribal):
    """L'anneau donné par le roi aux chefs gobelins. Ils en sont équippés à partir du niveau 1 (peut-être plus ?) mais on peut en trouver à l'abandon dans le labyrinthe."""
    def __init__(self,controleur:Controleur,niveau:int,position:Position=ABSENT):
        Anneau.__init__(self,controleur,position)
        Anoblisseur.__init__(self,priorite_sceau_roi_gobelin[niveau-1])
        Equipement_tribal.__init__(self,"gobelin",taux_refus_sceau_roi_gobelin[niveau-1])
        self.poids = poids_sceau_roi_gobelin[niveau-1]
        self.frottements = frottements_sceau_roi_gobelin[niveau-1]
        self.niveau = niveau

    def get_description(self,observation=0):
        return ["Un anneau","Vite, enfile-le !"]

    def get_skin(self):
        return SKIN_ANNEAU

#Quelques ingrédients pour l'alchimie :
class Hypokute(Ingredient):
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.poids = 1
        self.frottements = 5
        self.nom = "hypokute"

    def get_description(self,observation=0):
        return ["Une herbe","Il n'y a pourtant pas de soleil ici..."]

    def get_skin(self):
        return SKIN_HYPOKUTE
    
class Pierre_solide(Ingredient):
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.poids = 5
        self.frottements = 5
        self.nom = "pierre solide"

    def get_description(self,observation=0):
        return ["Une pierre","Particulièrement solide"]

    def get_skin(self):
        return SKIN_PIERRE_SOLIDE
    
class Dent_gobelin(Ingredient):
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.poids = 5
        self.frottements = 5
        self.nom = "dent de gobelin"

    def get_description(self,observation=0):
        return ["Une dent","En mauvais état"]

    def get_skin(self):
        return SKIN_DENT
    
class Peau_gobelin(Ingredient):
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Item.__init__(self,controleur,position)
        self.poids = 5
        self.frottements = 5
        self.nom = "peau de gobelin"

    def get_description(self,observation=0):
        return ["Un morceau de peau","Tout vert"]

    def get_skin(self):
        return SKIN_PEAU_GOBELIN

# Imports utilisés dans le code
from Jeu.Entitee.Item.Item import Item
from Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme
from Jeu.Systeme.Constantes_items.Items import *
from Jeu.Constantes import TERRE, GLACE
from Affichage.Skins.Skins import SKIN_ANNEAU, SKIN_HYPOKUTE, SKIN_PIERRE_SOLIDE, SKIN_DENT, SKIN_PEAU_GOBELIN, SKIN_EPEE_GOBELIN, SKIN_LANCE_GOBELIN, SKIN_ARMURE_GOBELIN, SKIN_CASQUE_GOBELIN, SKIN_BANDEAU_GOBELIN, SKIN_CIMETERE_GOBELIN, SKIN_LANCE_DOR, SKIN_ARMURE_DOR, SKIN_EPEE, SKIN_ARMURE_BASIQUE, SKIN_TUNIQUE_ALCHIMISTE, SKIN_TUNIQUE_ENCHANTEE, SKIN_SOUTANE, SKIN_ROBE_MAGIQUE, SKIN_ROBE_SORCIERE, SKIN_CHAPEAU_DE_SORCIERE, SKIN_EPEE_MARCHAND
