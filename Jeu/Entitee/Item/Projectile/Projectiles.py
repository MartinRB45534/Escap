from Jeu.Entitee.Item.Projectile.Projectile import *
from Jeu.Systeme.Constantes_projectiles.Projectiles import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Labyrinthe.Structure_spatiale.Direction import *

class Explosif(Projectile):
    """La classe des projectiles qui explosent. Affectés différemment par certains skills."""
    def get_skin(self):
        if self.hauteur > 0:
            return SKIN_EXPLOSIF
        else:
            return SKIN_EXPLOSE

class Charge_de_base(Explosif):
    """L'explosif le plus basique qui soit. Plutôt commun, accessible dès le niveau 1 du skill de création d'explosifs. À manipuler avec précaution, risque d'antagonisation involontaire."""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_charge_de_base[niveau-1]
        self.taux_vitesse = {}
        self.poids = 4
        self.frottements = 3
        self.hauteur = 0
        self.effets = [On_hit(portee_charge_de_base[niveau-1],degats_charge_de_base[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Charge_lourde(Explosif):
    """Un explosif puissant, mais de portée réduite."""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_charge_lourde[niveau-1]
        self.taux_vitesse = {}
        self.poids = 7
        self.frottements = 4
        self.hauteur = 0
        self.effets = [On_hit(portee_charge_lourde[niveau-1],degats_charge_lourde[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Charge_etendue(Explosif):
    """Un explosif faible, mais de portée importante."""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_charge_etendue[niveau-1]
        self.taux_vitesse = {}
        self.poids = 3
        self.frottements = 2
        self.hauteur = 0
        self.effets = [On_hit(portee_charge_etendue[niveau-1],degats_charge_etendue[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Percant(Projectile):
    """La classe des projectiles qui peuvent transpercer un ennemi."""
    pass

class Fleche(Percant):
    """La classe des projectiles de type flèche. Affectés différemment par certains skills."""
    def get_skin(self):
        return SKIN_FLECHE

class Fleche_de_base(Fleche):
    """La flèche la plus basique qui soit. La plus commune dans le labyrinthe, accessible dès le niveau 1 du skill de création de flèches."""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_de_base[niveau-1]
        self.taux_vitesse = {}
        self.poids = 1
        self.frottements = 2 #C'est plutôt rapide.
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_de_base[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_fantome(Fleche,Fantome):
    """Une flèche qui peut traverser les murs. Est-ce l'âme d'une flèche décédée ?"""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_fantome[niveau-1]
        self.taux_vitesse = {}
        self.poids = 1
        self.frottements = 2
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_fantome[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_lourde(Fleche):
    """Une flèche lourde. Elle va moins loin et un peu moins vite, mais rien que de bonnes stats ne puissent compenser. Et elle est dévastatrice !"""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_lourde[niveau-1]
        self.taux_vitesse = {}
        self.poids = 5 #C'est déjà mieux que certains... non-projectiles, je suppose ?
        self.frottements = 1
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_lourde[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_legere(Fleche):
    """Une flèche légère. Rapidité inégalée, portée incomparable... mais pas beaucoup de dégats, évidemment."""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_legere[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0.5
        self.frottements = 0.5 #Faire de toutes ces stats des constantes dépendant du niveau, aussi ?
        self.hauteur = 0
        self.effets = [On_hit(1,degats_fleche_legere[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Fleche_explosive(Fleche,Explosif):
    """Une flèche explosive. C'est une flèche ou un explosif ? Mieux vaut rester loin en tous cas..."""
    def __init__(self,niveau:int,position:Position):
        Entitee.__init__(self,position)
        self.etat = "intact"
        self.priorite = 0 #Faire dépendre du niveau ?
        self.porteur = None
        self.lanceur = None
        self.direction = None
        self.latence = 0
        self.vitesse = vitesse_fleche_explosive[niveau-1]
        self.taux_vitesse = {}
        self.poids = 3
        self.frottements = 2 
        self.hauteur = 0
        self.effets = [On_hit(portee_fleche_explosive[niveau-1],degats_fleche_explosive[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

class Perce_armure(Item):
    """La classe des items qui peuvent infliger des dégats sans être affectés par les défenses comme l'armure ou le bouclier."""

class Fragile(Item):
    """La classe des items qui se brisent lors d'un choc."""
    pass

class Evanescent(Item):
    """La classe des items qui disparaissent s'ils ne sont pas en mouvement (les sorts de projectiles, par exemple, qui sont des items...)."""
    pass

class Projectile_magique(Projectile,Evanescent):
    """La classe des projectiles créés par magie."""
    pass

class Magie_explosive(Explosif,Projectile_magique):
    """La classe des projectiles explosifs créés par magie."""
    pass

class Fleche_magique(Fleche,Projectile_magique):
    """La classe des flèches créées par magie."""
    pass

class Perce_armure_magique(Perce_armure,Projectile_magique):
    """La classe des projectiles perce_armures créés par magie."""
    pass

class Magie_explosive_percante(Magie_explosive,Percant):
    """La classe des projectiles explosifs perçant créés par magie."""
    pass

class Boule_de_feu(Magie_explosive):
    """Les projectiles crées par le sort de boule de feu."""
    def __init__(self,niveau:int,position:Position,direction:Direction,lanceur:int):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #On s'en fout, on ne peut pas ramasser une boule de feu...
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_boule_de_feu[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1 #Une boule de feu ne peut pas être au sol...
        self.effets = [On_hit(portee_boule_de_feu[niveau-1],degats_boule_de_feu[niveau-1],FEU)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_BOULE_DE_FEU

### Créer un parchemin d'invocation de boule de feu !

class Fleche_de_glace(Fleche_magique):
    """Les projectiles crées par le sort de fleche de glace."""
    def __init__(self,niveau:int,position:Position,direction:Direction,lanceur:int):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #Est-ce qu'on peut ramasser les fleches de glace ?
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_fleche_de_glace[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_fleche_de_glace[niveau-1],GLACE)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_FLECHE_DE_GLACE

### Créer un parchemin d'invocation de fleche de glace !

class Rocher(Projectile_magique):
    """Les projectiles crées par le sort de rocher."""
    def __init__(self,niveau:int,position:Position,direction:Direction,lanceur:int):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_rocher[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_rocher[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_ROCHER

### Créer un parchemin d'invocation de rocher !

class Ombre_furtive(Perce_armure_magique):
    """Les projectiles crées par le sort d'ombre_furtive."""
    def __init__(self,niveau:int,position:Position,direction:Direction,lanceur:int):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0 #On s'en fout, on ne peut pas ramasser une ombre...
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_ombre_furtive[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1 #Une ombre ne peut pas être au sol... si ?
        self.effets = [On_hit(1,degats_ombre_furtive[niveau-1],OMBRE)]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    def get_skin(self):
        return SKIN_OMBRE_FURTIVE

### Pas de parchemins pour les magies noires (enfin pour les apprendre, si (et encore), mais pour les lancer, non)...

class Jet_de_mana(Projectile_magique):
    """Les projectiles crées par le sort de jet de mana."""
    def __init__(self,niveau:int,position:Position,direction:Direction,lanceur:int):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_jet_de_mana[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_jet_de_mana[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    ### Lui créer un get_skin !

class Eclair_noir(Magie_explosive_percante):
    """Les projectiles crées par le sort d'éclair noir."""
    def __init__(self,niveau:int,position:Position,direction:Direction,lanceur:int):
        Entitee.__init__(self,position)
        self.etat = "intact" #Le niveau l'évacuera s'il n'est plus intact.
        self.priorite = 0
        self.porteur = None
        self.lanceur = lanceur
        self.direction = direction
        self.latence = 0
        self.vitesse = vitesse_eclair_noir[niveau-1]
        self.taux_vitesse = {}
        self.poids = 0 #C'est de la magie...
        self.frottements = 1 #C'est plutôt rapide.
        self.hauteur = 1
        self.effets = [On_hit(1,degats_choc_eclair_noir[niveau-1]),On_hit(portee_eclair_noir[niveau-1],degats_explosifs_eclair_noir[niveau-1])]
        self.niveau = niveau #On garde l'info pour un éventuel observateur

    ### Lui créer un get_skin !
