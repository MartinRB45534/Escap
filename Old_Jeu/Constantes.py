import pygame

VERSION = "0.0.-1"

# T = TypeVar("T", bound=Type)

# def trouve_skill(classe,type_skill:T) -> Optional[T]:
#     trouve = None
#     for skill in classe.skills:
#         if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill à 0 mais on ne sait jamais.
#             trouve = skill
#     for skill in classe.skills_intrasecs:
#         if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill à 0 mais on ne sait jamais.
#             trouve = skill
#     if trouve is None:
#         for sous_classe in classe.sous_classes: #On récurse la recherche dans les sous-classes.
#             trouve_bis = trouve_skill(sous_classe,type_skill)
#             if trouve_bis is not None:
#                 trouve = trouve_bis
#     return trouve

class Id_max:
    def __init__(self):
        self.valeur = 0

    def incremente(self):
        self.valeur+=1
        return self.valeur

    def set_id_max(self,n: int):
        self.valeur = n

POLICE20 = pygame.font.SysFont("Default", 20)

POLICE40 = pygame.font.SysFont("Default", 40)

ID_MAX = Id_max()

#Directions
NB_DIRECTIONS = 4

IN=NB_DIRECTIONS
OUT=NB_DIRECTIONS+1
NEXT=NB_DIRECTIONS+2
PREVIOUS=NB_DIRECTIONS+3

#Éléments
TERRE = 0
FEU = 1
GLACE = 2
OMBRE = 3

#Résolutions
BASIQUE = 0
PASSE_PORTE = 1
PASSE_PORTAIL = 2
PASSE_PORTE_ET_PORTAIL = 3
PASSE_ESCALIER = 4

CLASSIQUE = True
ELEMENTAL = False

physique = 0
magique = 1

affinite = 0
aura = 1
MAGIE = 2
elemental = 3

affinite_terre = 0
aura_terre = 1
magie_terre = 2
elemental_terre = 3

affinite_feu = 10
aura_feu = 11
magie_feu = 12
elemental_feu = 13

affinite_glace = 20
aura_glace = 21
magie_glace = 22
elemental_glace = 23

affinite_ombre = 30
aura_ombre = 31
magie_ombre = 32
elemental_ombre = 33

# 0,1,2 et 3 sont déjà pris
REGEN_HP = 4
REGEN_MP = 5
DEFENSE = 6
LANCER = 7
ESSENCE_MAGIQUE = 8
MAGIE_INFINIE = 9
#10,11,12 et 13 sont déjà pris
BOOST_PRIORITE = 14
BOOST_PV = 15
BOOST_DE_PRIORITE_D_ATTAQUE = 16
CREATION_FLECHES = 17
SORT_ACCELERATION = 18
BOOST_AURA = 19
#20,21,22 et 23 sont déjà pris
BOOST_PM = 24
ONDE_DE_CHOC = 25
SORT_DE_SOIN_SUPERIEUR = 26
ENCHANTEMENT_FORCE = 27
PROJECTION_ENERGIE = 28
ECRASEMENT = 29
#30,31,32 et 33 sont déjà pris
OBSERVATION = 34
MANIPULATION_EPEE = 35
BOOST_PORTEE = 36
SORT_VISION = 37
CREATION_EXPLOSIF = 38
ELEMENTALISTE = 39
RAYON_THERMIQUE = 40
ENCHANTEMENT_DEFENSE = 41
REGEN_PM = 42 #À ne surtout pas confondre avec REGEN_MP !
ANALYSE = 44
VOL = 45
BOOST_ATTAQUE_EPEE = 46
FLECHE_PERCANTE = 47
FLECHE_EXPLOSIVE = 48
IMMORTALITE = 49
BOOST_DEGATS_MAGIQUES = 50
BOOST_PRIORITE_MAGIQUE = 51
ENCHANTEMENT_FAIBLESSE = 52
EPEISTE = 53
BOOST_RESTAURATIONS = 54
MANIPULATION_BOUCLIER = 55
BOOST_PRIORITE_OBSERVATION = 56
SORT_AUTO_SOIN = 57
BOOST_DEGATS_FLECHES = 58
CHARGE_LOURDE = 59
CHARGE_ETENDUE = 60
INHUMANITE = 61
MAGICIEN = 62
BOOST_DE_PORTEE = 63
BOOST_SOIN = 65
SORT_DE_VUE = 66
VOL_PRIORITE = 67
BOOST_ATTAQUE_LANCE = 68
BOOST_PRIORITE_FLECHES = 69
ARTIFICIER = 70
FANTOME = 71
INSTAKILL = 72
JET_DE_MANA = 73
ENCHANTEMENT_RENFORCEMENT = 74
SORT_DE_PROTECTION = 75
BOOST_ATTAQUE = 76
ARCHER = 77
FLECHE_FANTOME = 78
BOOST_DEGAT = 79
NECROMANCIEN = 80
ENCHANTEUR = 81
SOUTIEN  = 82
BOOST_PRIORITE_DEPLACEMENT = 83
BOOST_PRIORITE_ANALYSE = 84
BOOST_PRIORITE_EXPLOSIF = 85
BOOST_VITESSE_EXPLOSIF = 86
BOOST_PRIORITE_AURA = 87
AURA_MORTELLE = 88
ASSASSIN = 89
BOOST_DE_ZONE_DE_RESTAURATION = 90
ANGE = 91
ENCHANTEMENT_ROUILLE = 92
MANIPULATION_ARME = 93
FLECHES_LOURDE_LEGERE = 94
BOOST_PORTEE_EXPLOSIFS = 95
ECLAIR_NOIR = 96
BOOST_DEGATS_PROJECTILES = 97
BOOST_ENCHANTEMENT = 98
RESURECTION = 99

PHYSIQUE = 100
PHYSIQUE_PAR_DEFAUT = 43
DEFENSE_PAR_DEFAUT = 64
MAGIE_INFINIE_PAR_DEFAUT = 101
ENCHANTEMENT_DEFENSIF = 102
# Il n'y a pas de numéro 43 et 64


# Phases de jeu
TOUR = 1
DIALOGUE = 2
TOUCHE = 3
LEVEL_UP = 4
RECETTE = 5
MARCHAND = 6
IMPREGNATION = 7
AUTO_IMPREGNATION = 8
AGISSANT_DIALOGUE = 9
CASE_DIALOGUE = 10
AGISSANT_MAGIE = 11
CASE_MAGIE = 12
DIRECTION_MAGIE = 13
COUT_MAGIE = 14
AGISSANT_PARCHEMIN = 15
CASE_PARCHEMIN = 16
DIRECTION_PARCHEMIN = 17
COUT_PARCHEMIN = 18
CINEMATIQUE = 19

LISTE_EXHAUSTIVE_DES_MAGIES_OFFENSIVES = ["magie poing magique","magie poing ardent","magie secousse","magie petite secousse","magie volcan","magie explosion de mana","magie laser","magie brasier","magie avalanche"] #Je suis sur qu'il y en a d'autres
