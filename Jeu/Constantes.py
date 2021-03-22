import pygame

def trouve_skill(classe,type_skill): #Vraiment une méthode propre au controleur ?
    trouve = None
    for skill in classe.skills:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill à 0 mais on ne sait jamais.
            trouve = skill
    for skill in classe.skills_intrasecs:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill à 0 mais on ne sait jamais.
            trouve = skill
    if trouve == None:
        for sous_classe in classe.sous_classes: #On récurse la recherche dans les sous-classes.
            trouve_bis = trouve_skill(sous_classe,type_skill)
            if trouve_bis != None:
                trouve = trouve_bis
    return trouve

class Id_max:
    def __init__(self):
        self.valeur = 0

    def incremente(self):
        self.valeur+=1
        return self.valeur

    def set_id_max(self,n):
        self.valeur = n

global ID_MAX
ID_MAX = Id_max()

#Constantes d'équilibrage :
global constantes_lab
constantes_lab = {0:0.1}

#constantes
global HAUT
HAUT=0
global DROITE
DROITE=1
global BAS
BAS=2
global GAUCHE
GAUCHE=3
global IN
IN=4
global OUT
OUT=5


global MUR_VIDE
MUR_VIDE=0
global MUR_PLEIN
MUR_PLEIN=1
global INTOUCHABLE
INTOUCHABLE=2

global PORTE_FERMEE
PORTE_FERMEE=0
global PORTE_OUVERTE
PORTE_OUVERTE=1

#global Potion

global FENETRE_X
FENETRE_X = 600
global FENETRE_Y
FENETRE_Y = 600

global malchance_forcee
malchance_forcee = False

global voir_tout
voir_tout = 0
global parcours_en_profondeur
parcours_en_profondeur = 1
global aveugle
aveugle = 2
global distance_max
distance_max = 3

global passage
passage = 1


global BEGINNER
BEGINNER = 0
global EASY
EASY = 1
global AVERAGE
AVERAGE = 2
global HARD
HARD = 3
global INSANE
INSANE = 4
global IMPOSSIBLE
IMPOSSIBLE = 5


global BOUGER
BOUGER = 0
global ATTAQUER
ATTAQUER = 1
global PARLER
PARLER = 2
global INTERAGIR
INTERAGIR = 3
global CONSULTER_MINIMAP
CONSULTER_MINIMAP = 4
global CONSULTER_INVENTAIRE
CONSULTER_INVENTAIRE = 5
global PRECISION
PRECISION = 6
global POSTCISION
POSTCISION = 7
global RETOUR
RETOUR = 8
global BOUGER_MINIMAP
BOUGER_MINIMAP = 9
global BOUGER_INVENTAIRE
BOUGER_INVENTAIRE = 10
global UTILISER
UTILISER = 11
global AIDER
AIDER = 12


global ARRIVEE
ARRIVEE=(30, 144, 255)

global LABYRINTHE
LABYRINTHE=0
global MINIMAP
MINIMAP=1
global INVENTAIRE_
INVENTAIRE_=2
global DIALOGUE
DIALOGUE=3
global ITEM
ITEM=4

global LIGHT
LIGHT = 0
global HEAVY
HEAVY = 1


global sauvegarde
sauvegarde = "save.p"

global TAILLE_FIXE
TAILLE_FIXE = False
global taille_fixe
taille_fixe = 10

global SCREEN

#À supprimer ?
global LAB
global JOUEUR
global AGISSANTS
global ITEMS

global BIENFAIT
BIENFAIT = 0
global DELIT
DELIT = 1
global CRIME
CRIME = 2

global MORT
MORT = 0
global VIVANT
VIVANT = 1

global TERRE
TERRE = 0
global FEU
FEU = 1
global GLACE
GLACE = 2
global OMBRE
OMBRE = 3

#Les positions possibles du curseur :
global RECTANGLE_G #Le rectangle gauche de l'affichage
RECTANGLE_G = 0
global CARRE #Le carré au centre de l'affichage, correspond à la vue du joueur, elle a son propre sous-curseur
CARRE = 1
global RECTANGLE_D #Le rectangle droit de l'affichage
RECTANGLE_D = 2

#Dans le rectangle gauche :
global STATS #Les stats du joueur
STATS = 0
global INVENTAIRE #L'inventaire contient la liste des possessions du joueur, il a son propre sous-curseur
INVENTAIRE = 1
global SKILLS #Les skills tels que décrits par la classe principale du joueur, ils ont leur propre sous-curseur
SKILLS = 2

#Dans les stats du joueur :
global VIE #Les informations sur la vie du joueur
VIE = 0
global MANA #Les informations sur le mana du joueur
MANA = 1
global PRIORITE #Les informations sur la priorite du joueur (visible à partir d'un certain niveau d'observation)
PRIORITE = 2

#Dans les informations sur la vie du joueur :
global TITRE #Le titre devant la barre de vie
TITRE = 0
global BARRE #La barre de vie
BARRE = 1
global MIN #Le 0 de la barre de vie (visible à partir d'un certain niveau d'observation)
MIN = 2
global VAL #La valeur de la partie pleine de la barre de vie (visible à partir d'un certain niveau d'observation)
VAL = 3
global MAX #La valeur maximal que peut atteindre naturellement la barre de vie (visible à partir d'un certain niveau d'observation)
MAX = 4

#Les informations sur le mana du joueur sont indentiques aux informations sur la vie du joueur, mais si le joueur a des réserves de magies, un curseur indique la limite haute de quelle réserve est observée (0 pour la réserve naturelle) et quelle barre est observée (0 pour la réserve naturelle)
#Les informations sur la priorité et l'identifiant du joueur sont de la forme titre et val, uniquement.



#Dans le rectangle droit :
#Le rectangle droit peut contenir les informations d'un agissant séléctionné dans la vue (visible à partir d'un certain niveau d'observation, auquel cas le curseur est comme précédemment
#Le rectangle droit peut contenir les informations d'un item séléctionné dans un inventaire (celui du joueur ou d'un agissant observé dans la vue) :
global NOM #Les informations sur le nom de l'item
NOM = 0
#Dans le cas d'une potion, on observera aussi l'effet :
global EFFET #Les informations sur l'effet de la potion
EFFET = 1
#Dans le cas d'un parchemin, il y aura aussi une information sur le cout d'utilisation :
global COUT #Les informations sur le cout du parchemin
COUT = 2
#Dans le cas d'un 

global ARBORESCENCE
ARBORESCENCE = [[RECTANGLE_G,CARRE,RECTANGLE_D],
                [[STATS,INVENTAIRE,SKILLS],[],[]],
                [[[VIE,MANA,PRIORITE],[],[]],[],[]],
                [[[[TITRE,BARRE,MIN,VAL,MAX],[TITRE,BARRE,MIN,VAL,MAX],[TITRE,VAL]],[],[]],[],[]]]

global CLASSIQUE
CLASSIQUE = True
global ELEMENTAL
ELEMENTAL = False

global physique
physique = 0
global magique
magique = 1

global affinite
affinite = 0
global aura
aura = 1
global MAGIE
MAGIE = 2
global elemental
elemental = 3

global affinite_terre
affinite_terre = 0
global aura_terre
aura_terre = 1
global magie_terre
magie_terre = 2
global elemental_terre
elemental_terre = 3

global affinite_feu
affinite_feu = 10
global aura_feu
aura_feu = 11
global magie_feu
magie_feu = 12
global elemental_feu
elemental_feu = 13

global affinite_glace
affinite_glace = 20
global aura_glace
aura_glace = 21
global magie_glace
magie_glace = 22
global elemental_glace
elemental_glace = 23

global affinite_ombre
affinite_ombre = 30
global aura_ombre
aura_ombre = 31
global magie_ombre
magie_ombre = 32
global elemental_ombre
elemental_ombre = 33

# 0,1,2 et 3 sont déjà pris
global REGEN_HP
REGEN_HP = 4
global REGEN_MP
REGEN_MP = 5
global DEFENSE
DEFENSE = 6
global LANCER
LANCER = 7
global ESSENCE_MAGIQUE
ESSENCE_MAGIQUE = 8
global MAGIE_INFINIE
MAGIE_INFINIE = 9
#10,11,12 et 13 sont déjà pris
global BOOST_PRIORITE
BOOST_PRIORITE = 14
global BOOST_PV
BOOST_PV = 15
global BOOST_DE_PRIORITE_D_ATTAQUE
BOOST_DE_PRIORITE_D_ATTAQUE = 16
global CREATION_FLECHES
CREATION_FLECHES = 17
global SORT_ACCELERATION
SORT_ACCELERATION = 18
global BOOST_AURA
BOOST_AURA = 19
#20,21,22 et 23 sont déjà pris
global BOOST_PM
BOOST_PM = 24
global ONDE_DE_CHOC
ONDE_DE_CHOC = 25
global SORT_DE_SOIN_SUPERIEUR
SORT_DE_SOIN_SUPERIEUR = 26
global ENCHANTEMENT_FORCE
ENCHANTEMENT_FORCE = 27
global PROJECTION_ENERGIE
PROJECTION_ENERGIE = 28
global ECRASEMENT
ECRASEMENT = 29
#30,31,32 et 33 sont déjà pris
global OBSERVATION
OBSERVATION = 34
global MANIPULATION_EPEE
MANIPULATION_EPEE = 35
global BOOST_PORTEE
BOOST_PORTEE = 36
global SORT_VISION
SORT_VISION = 37
global CREATION_EXPLOSIF
CREATION_EXPLOSIF = 38
global ELEMENTALISTE
ELEMENTALISTE = 39
global RAYON_THERMIQUE
RAYON_THERMIQUE = 40
global ENCHANTEMENT_DEFENSE
ENCHANTEMENT_DEFENSE = 41
global REGEN_PM
REGEN_PM = 42 #À ne surtout pas confondre avec REGEN_MP !
global ANALYSE
ANALYSE = 44
global VOL
VOL = 45
global BOOST_ATTAQUE_EPEE
BOOST_ATTAQUE_EPEE = 46
global FLECHE_PERCANTE
FLECHE_PERCANTE = 47
global FLECHE_EXPLOSIVE
FLECHE_EXPLOSIVE = 48
global IMMORTALITE
IMMORTALITE = 49
global BOOST_DEGATS_MAGIQUES
BOOST_DEGATS_MAGIQUES = 50
global BOOST_PRIORITE_MAGIQUE
BOOST_PRIORITE_MAGIQUE = 51
global ENCHANTEMENT_FAIBLESSE
ENCHANTEMENT_FAIBLESSE = 52
global EPEISTE
EPEISTE = 53
global BOOST_RESTAURATIONS
BOOST_RESTAURATIONS = 54
global MANIPULATION_BOUCLIER
MANIPULATION_BOUCLIER = 55
global BOOST_PRIORITE_OBSERVATION
BOOST_PRIORITE_OBSERVATION = 56
global SORT_AUTO_SOIN
SORT_AUTO_SOIN = 57
global BOOST_DEGATS_FLECHES
BOOST_DEGATS_FLECHES = 58
global CHARGE_LOURDE
CHARGE_LOURDE = 59
global CHARGE_ETENDUE
CHARGE_ETENDUE = 60
global INHUMANITE
INHUMANITE = 61
global MAGICIEN
MAGICIEN = 62
global BOOST_DE_PORTEE
BOOST_DE_PORTEE = 63
global BOOST_SOIN
BOOST_SOIN = 65
global SORT_DE_VUE
SORT_DE_VUE = 66
global VOL_PRIORITE
VOL_PRIORITE = 67
global BOOST_ATTAQUE_LANCE
BOOST_ATTAQUE_LANCE = 68
global BOOST_PRIORITE_FLECHES
BOOST_PRIORITE_FLECHES = 69
global ARTIFICIER
ARTIFICIER = 70
global FANTOME
FANTOME = 71
global INSTAKILL
INSTAKILL = 72
global JET_DE_MANA
JET_DE_MANA = 73
global ENCHANTEMENT_RENFORCEMENT
ENCHANTEMENT_RENFORCEMENT = 74
global SORT_DE_PROTECTION
SORT_DE_PROTECTION = 75
global BOOST_ATTAQUE
BOOST_ATTAQUE = 76
global ARCHER
ARCHER = 77
global FLECHE_FANTOME
FLECHE_FANTOME = 78
global BOOST_DEGAT
BOOST_DEGAT = 79
global NECROMANCIEN
NECROMANCIEN = 80
global ENCHANTEUR
ENCHANTEUR = 81
global SOUTIEN
SOUTIEN  = 82
global BOOST_PRIORITE_DEPLACMEENT
BOOST_PRIORITE_DEPLACEMENT = 83
global BOOST_PRIORITE_ANALYSE
BOOST_PRIORITE_ANALYSE = 84
global BOOST_PRIORITE_EXPLOSIF
BOOST_PRIORITE_EXPLOSIF = 85
global BOOST_VITESSE_EXPLOSIF
BOOST_VITESSE_EXPLOSIF = 86
global BOOST_PRIORITE_AURA
BOOST_PRIORITE_AURA = 87
global AURA_MORTELLE
AURA_MORTELLE = 88
global ASSASSIN
ASSASSIN = 89
global BOOST_DE_ZONE_DE_RESTAURATION
BOOST_DE_ZONE_DE_RESTAURATION = 90
global ANGE
ANGE = 91
global ENCHANTEMENT_ROUILLE
ENCHANTEMENT_ROUILLE = 92
global MANIPULATION_ARME
MANIPULATION_ARME = 93
global FLECHES_LOURDE_LEGERE
FLECHES_LOURDE_LEGERE = 94
global BOOST_PORTEE_EXPLOSIFS
BOOST_PORTEE_EXPLOSIFS = 95
global ECLAIR_NOIR
ECLAIR_NOIR = 96
global BOOST_DEGATS_PROJECTILES
BOOST_DEGATS_PROJECTILES = 97
global BOOST_ENCHANTEMENT
BOOST_ENCHANTEMENT = 98
global RESURECTION
RESURECTION = 99

global PHYSIQUE
PHYSIQUE = 100
global PHYSIQUE_PAR_DEFAUT
PHYSIQUE_PAR_DEFAUT = 43
global DEFENSE_PAR_DEFAUT
DEFENSE_PAR_DEFAUT = 64
global MAGIE_INFINIE_PAR_DEFAUT
MAGIE_INFINIE_PAR_DEFAUT = 101
global ENCHANTEMENT_DEFENSIF
ENCHANTEMENT_DEFENSIF = 102
# Il n'y a pas de numéro 43 et 64

global TOUR
TOUR = 0
global TOUCHE
TOUCHE = 1
global COMPLEMENT_DIR
COMPLEMENT_DIR = 2
global COMPLEMENT_CIBLE
COMPLEMENT_CIBLE = 3
global COMPLEMENT_COUT
COMPLEMENT_COUT = 4
global EVENEMENT
EVENEMENT = 5

global LEVELUP
LEVELUP = 0
