from math import ceil
from typing import Dict, List, Tuple
from Jeu.Constantes import *
from Jeu.Systeme.Classe import *
from Jeu.Systeme.Constantes_decors.Decors import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Systeme.Constantes_projectiles.Projectiles import *
from Jeu.Systeme.Constantes_items.Items import *
from Jeu.Systeme.Constantes_stats import *
from Jeu.Dialogues.Dialogues import *
from Jeu.Skins.Skins import *
from Modifiers import *
import operator
import random
import copy

try:
    from Jeu.Equilibrage import *
    latence_deplacement[0] = LATENCE_DEPLACEMENT
    latence_course[0] = LATENCE_COURSE
    latence_stomp[0] = LATENCE_STOMP
    latence_attaque[0] = LATENCE_ATTAQUE
    taux_utilisation_stomp[0] = TAUX_STOMP
    taux_utilisation_attaque[0] = TAUX_ATTAQUE
    tranchant_lance_gobelin[0] = TAUX_LANCE
    tranchant_epee_gobelin[0] = TAUX_EPEE
    tranchant_cimetere_gobelin[0] = TAUX_CIMETERE
    taux_degats_armure_sentinelle_gobelin[0] = TAUX_ARMURE_SENT
    taux_degats_haume_gobelin[0] = TAUX_HAUME
    taux_degats_armure_guerrier_gobelin[0] = TAUX_ARMURE_GUER
    pm_bandeau_gobelin[0] = PM_BANDEAU
    taux_degats_tunique_enchantee[0] = TAUX_TUNIQUE
    pm_robe_magique[0] = REGEN_PM_ROBE
    tranchant_epee_epeiste[0] = TAUX_EPEE_ENCOMBRANT
    taux_degats_armure_epeiste[0] = TAUX_ARMURE_ENCOMBRANT
    pm_tunique_alchimiste[0] = REGEN_PM_TUNIQUE
    degats_soutane[0] = DEGATS_SOUTANE
    pm_robe_sorciere[0] = REGEN_PM_ROBE_SORCIERE
    pm_chapeau_sorciere[0] = REGEN_PM_CHAPEAU_SORCIERE
    tranchant_epee_marchand[0] = TAUX_EPEE_MARCHAND
    degats_armure_marchand[0] = TAUX_ARMURE_MARCHAND

    cout_pm_boost[0] = PM_BOOST
    taux_boost[0] = TAUX_BOOST
    latence_boost[0] = LATENCE_BOOST
    cout_pm_multi_boost[0] = PM_MULTI_BOOST
    taux_multi_boost[0] = TAUX_MULTI_BOOST
    latence_multi_boost[0] = LATENCE_MULTI_BOOST
    cout_pm_secousse[0] = COUT_SECOUSSE
    degats_secousse[0] = DEGATS_SECOUSSE
    portee_secousse[0] = PORTEE_SECOUSSE
    latence_secousse[0] = LATENCE_SECOUSSE
    cout_pm_soin[0] = PM_SOIN
    gain_pv_soin[0] = PV_SOIN
    latence_soin[0] = LATENCE_SOIN
    cout_pm_multi_soin[0] = PM_MULTI_SOIN
    gain_pv_multi_soin[0] = PV_MULTI_SOIN
    latence_multi_soin[0] = LATENCE_MULTI_SOIN
    cout_pm_volcan[0] = COUT_VOLCAN
    degats_volcan[0] = DEGATS_VOLCAN
    portee_volcan[0] = PORTEE_VOLCAN
    latence_volcan[0] = LATENCE_VOLCAN
    cout_pm_petite_secousse[0] = COUT_MAGE
    degats_petite_secousse[0] = DEGATS_MAGE
    latence_petite_secousse[0] = LATENCE_MAGE

    CONSTANTES_STATS["joueur"]["pv"][1] = PV_JOUEUR
    CONSTANTES_STATS["joueur"]["vitesse"][1] = VITESSE_JOUEUR
    CONSTANTES_STATS["joueur"]["force"][1] = FORCE_JOUEUR
    CONSTANTES_STATS["joueur"]["regen_pv"][1] = REGEN_JOUEUR
    CONSTANTES_STATS["receptionniste"]["pv"][1] = PV_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["vitesse"][1] = VITESSE_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["force"][1] = FORCE_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["regen_pv"][1] = REGEN_RECEPTIONNISTE
    CONSTANTES_STATS["paume"]["pv"][1] = PV_PAUME
    CONSTANTES_STATS["paume"]["vitesse"][1] = VITESSE_PAUME
    CONSTANTES_STATS["paume"]["force"][1] = FORCE_PAUME
    CONSTANTES_STATS["paume"]["regen_pv"][1] = REGEN_PAUME
    CONSTANTES_STATS["peureuse"]["pv"][1] = PV_PEUREUSE
    CONSTANTES_STATS["peureuse"]["vitesse"][1] = VITESSE_PEUREUSE
    CONSTANTES_STATS["peureuse"]["force"][1] = FORCE_PEUREUSE
    CONSTANTES_STATS["peureuse"]["regen_pv"][1] = REGEN_PEUREUSE
    CONSTANTES_STATS["peureuse"]["pm"][1] = PM_PEUREUSE
    CONSTANTES_STATS["peureuse"]["regen_pm"][1] = REGEN_PM_PEUREUSE
    CONSTANTES_STATS["encombrant"]["pv"][1] = PV_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["vitesse"][1] = VITESSE_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["force"][1] = FORCE_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["regen_pv"][1] = REGEN_ENCOMBRANT
    CONSTANTES_STATS["alchimiste"]["pv"][1] = PV_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["vitesse"][1] = VITESSE_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["force"][1] = FORCE_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["regen_pv"][1] = REGEN_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["pm"][1] = PM_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["regen_pm"][1] = REGEN_PM_ALCHIMISTE
    CONSTANTES_STATS["peste"]["pv"][1] = PV_PESTE
    CONSTANTES_STATS["peste"]["vitesse"][1] = VITESSE_PESTE
    CONSTANTES_STATS["peste"]["force"][1] = FORCE_PESTE
    CONSTANTES_STATS["peste"]["regen_pv"][1] = REGEN_PESTE
    CONSTANTES_STATS["peste"]["pm"][1] = PM_PESTE
    CONSTANTES_STATS["peste"]["regen_pm"][1] = REGEN_PM_PESTE
    CONSTANTES_STATS["bombe_atomique"]["pv"][1] = PV_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["vitesse"][1] = VITESSE_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["force"][1] = FORCE_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["regen_pv"][1] = REGEN_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["pm"][1] = PM_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["regen_pm"][1] = REGEN_PM_BOMBE
    CONSTANTES_STATS["marchand"]["pv"][1] = PV_MARCHAND
    CONSTANTES_STATS["marchand"]["vitesse"][1] = VITESSE_MARCHAND
    CONSTANTES_STATS["marchand"]["force"][1] = FORCE_MARCHAND
    CONSTANTES_STATS["marchand"]["regen_pv"][1] = REGEN_MARCHAND
    CONSTANTES_STATS["premier_monstre"]["pv"][1] = PV_PREMIER
    CONSTANTES_STATS["premier_monstre"]["vitesse"][1] = VITESSE_PREMIER
    CONSTANTES_STATS["premier_monstre"]["force"][1] = FORCE_PREMIER
    CONSTANTES_STATS["deuxieme_monstre"]["pv"][1] = PV_DEUXIEME
    CONSTANTES_STATS["deuxieme_monstre"]["vitesse"][1] = VITESSE_DEUXIEME
    CONSTANTES_STATS["deuxieme_monstre"]["pm"][1] = PM_DEUXIEME
    CONSTANTES_STATS["deuxieme_monstre"]["regen_pm"][1] = REGEN_DEUXIEME
    CONSTANTES_STATS["troisieme_monstre"]["pv"][1] = PV_TROISIEME
    CONSTANTES_STATS["troisieme_monstre"]["vitesse"][1] = VITESSE_TROISIEME
    CONSTANTES_STATS["troisieme_monstre"]["force"][1] = FORCE_TROISIEME
    CONSTANTES_STATS["sentinelle_gobelin"]["pv"][1] = PV_SENT
    CONSTANTES_STATS["sentinelle_gobelin"]["vitesse"][1] = VITESSE_SENT
    CONSTANTES_STATS["sentinelle_gobelin"]["force"][1] = FORCE_SENT
    CONSTANTES_STATS["guerrier_gobelin"]["pv"][1] = PV_GUER
    CONSTANTES_STATS["guerrier_gobelin"]["vitesse"][1] = VITESSE_GUER
    CONSTANTES_STATS["guerrier_gobelin"]["force"][1] = FORCE_GUER
    CONSTANTES_STATS["mage_gobelin"]["pv"][1] = PV_MAGE
    CONSTANTES_STATS["mage_gobelin"]["vitesse"][1] = VITESSE_MAGE
    CONSTANTES_STATS["mage_gobelin"]["pm"][1] = PM_MAGE
    CONSTANTES_STATS["mage_gobelin"]["regen_pm"][1] = REGEN_MAGE
    CONSTANTES_STATS["shaman_gobelin"]["pv"][1] = PV_SHAMAN
    CONSTANTES_STATS["shaman_gobelin"]["vitesse"][1] = VITESSE_SHAMAN
    CONSTANTES_STATS["shaman_gobelin"]["pm"][1] = PM_SHAMAN
    CONSTANTES_STATS["shaman_gobelin"]["regen_pm"][1] = REGEN_SHAMAN
    CONSTANTES_STATS["gobelin"]["pv"][1] = PV_GOB
    CONSTANTES_STATS["gobelin"]["vitesse"][1] = VITESSE_GOB
    CONSTANTES_STATS["gobelin"]["force"][1] = FORCE_GOB
    CONSTANTES_STATS["chef_gobelin"]["pv"][1] = PV_CHEF
    CONSTANTES_STATS["chef_gobelin"]["vitesse"][1] = VITESSE_CHEF
    CONSTANTES_STATS["chef_gobelin"]["force"][1] = FORCE_CHEF
    CONSTANTES_STATS["chef_gobelin"]["regen_pv"][1] = REGEN_CHEF

    dpt_joueur = FORCE_JOUEUR*TAUX_STOMP*VITESSE_JOUEUR/LATENCE_STOMP
    dpt_boost_joueur = dpt_joueur * TAUX_BOOST
    dpt_multi_boost_joueur = dpt_joueur * TAUX_MULTI_BOOST
    dpt_receptionniste = FORCE_RECEPTIONNISTE*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT*VITESSE_RECEPTIONNISTE/LATENCE_ATTAQUE
    dpt_boost_receptionniste = dpt_receptionniste * TAUX_BOOST
    dpt_multi_boost_receptionniste = dpt_receptionniste * TAUX_MULTI_BOOST
    dpt_paume = FORCE_PAUME*TAUX_STOMP*VITESSE_PAUME/LATENCE_STOMP
    dpt_boost_paume = dpt_paume * TAUX_BOOST
    dpt_multi_boost_paume = dpt_paume * TAUX_MULTI_BOOST
    dpt_encombrant = FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT*VITESSE_ENCOMBRANT/LATENCE_ATTAQUE
    dpt_boost_encombrant = dpt_encombrant * TAUX_BOOST
    dpt_multi_boost_encombrant = dpt_encombrant * TAUX_MULTI_BOOST
    dpt1_alchimiste = DEGATS_SECOUSSE*VITESSE_ALCHIMISTE/LATENCE_SECOUSSE
    dpt1_boost_alchimiste = dpt1_alchimiste * TAUX_BOOST
    dpt1_multi_boost_alchimiste = dpt1_alchimiste * TAUX_MULTI_BOOST
    dpt2_alchimiste = DEGATS_SECOUSSE*(REGEN_PM_ALCHIMISTE+REGEN_PM_TUNIQUE)/COUT_SECOUSSE
    dpt2_boost_alchimiste = dpt2_alchimiste * TAUX_BOOST
    dpt2_multi_boost_alchimiste = dpt2_alchimiste * TAUX_MULTI_BOOST
    pvt1_peste = PV_SOIN*VITESSE_PESTE/LATENCE_SOIN
    pvt2_peste = PV_SOIN*REGEN_PM_PESTE/PM_SOIN
    pvt1_multi_peste = PV_MULTI_SOIN*VITESSE_PESTE/LATENCE_MULTI_SOIN
    pvt2_multi_peste = PV_MULTI_SOIN*REGEN_PM_PESTE/PM_MULTI_SOIN
    dpt1_bombe = DEGATS_VOLCAN*VITESSE_BOMBE/LATENCE_VOLCAN
    dpt1_boost_bombe = dpt1_bombe * TAUX_BOOST
    dpt1_multi_boost_bombe = dpt1_bombe * TAUX_MULTI_BOOST
    dpt2_bombe = DEGATS_VOLCAN*(REGEN_PM_BOMBE+REGEN_PM_ROBE_SORCIERE+REGEN_PM_CHAPEAU_SORCIERE)/COUT_VOLCAN
    dpt2_boost_bombe = dpt2_bombe * TAUX_BOOST
    dpt2_multi_boost_bombe = dpt2_bombe * TAUX_MULTI_BOOST
    dpt_marchand = FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND*VITESSE_MARCHAND/LATENCE_ATTAQUE
    dpt_boost_marchand = dpt_marchand * TAUX_BOOST
    dpt_multi_boost_marchand = dpt_marchand * TAUX_MULTI_BOOST
    dpt1_min_peureuse = min(FORCE_JOUEUR*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*VITESSE_PEUREUSE/LATENCE_BOOST
    dpt1_max_peureuse = max(FORCE_JOUEUR*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*VITESSE_PEUREUSE/LATENCE_BOOST
    dpt2_min_peureuse = min(FORCE_JOUEUR*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*(REGEN_PM_PEUREUSE+REGEN_PM_ROBE)/PM_BOOST
    dpt2_max_peureuse = max(FORCE_JOUEUR*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*(REGEN_PM_PEUREUSE+REGEN_PM_ROBE)/PM_BOOST
    dpt1_multi_peureuse = (FORCE_JOUEUR*TAUX_STOMP+FORCE_PAUME*TAUX_STOMP+FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT+DEGATS_SECOUSSE+DEGATS_VOLCAN+FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_MULTI_BOOST-1)*VITESSE_PEUREUSE/LATENCE_MULTI_BOOST
    dpt2_multi_peureuse = (FORCE_JOUEUR*TAUX_STOMP+FORCE_PAUME*TAUX_STOMP+FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT+DEGATS_SECOUSSE+DEGATS_VOLCAN+FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_MULTI_BOOST-1)*(REGEN_PM_PEUREUSE+REGEN_PM_ROBE)/PM_MULTI_BOOST
    dpt_gob = FORCE_GOB*TAUX_ATTAQUE*TAUX_EPEE*VITESSE_GOB/LATENCE_ATTAQUE
    dpt_boost_gob = dpt_gob * TAUX_BOOST
    dpt_sent = FORCE_SENT*TAUX_ATTAQUE*TAUX_LANCE*VITESSE_SENT/LATENCE_ATTAQUE
    dpt_boost_sent = dpt_sent * TAUX_BOOST
    dpt_guer = FORCE_GUER*TAUX_ATTAQUE*TAUX_CIMETERE*VITESSE_GUER/LATENCE_ATTAQUE
    dpt_boost_guer = dpt_guer * TAUX_BOOST
    dpt1_mage = DEGATS_MAGE*VITESSE_MAGE/LATENCE_MAGE
    dpt1_boost_mage = dpt1_mage * TAUX_BOOST
    dpt2_mage = DEGATS_MAGE*(REGEN_MAGE+PM_BANDEAU)/COUT_MAGE
    dpt2_boost_mage = dpt2_mage * TAUX_BOOST
    dpt1_min_shaman = min(FORCE_GOB*TAUX_ATTAQUE*TAUX_EPEE,FORCE_SENT*TAUX_ATTAQUE*TAUX_LANCE,FORCE_GUER*TAUX_ATTAQUE*TAUX_CIMETERE,DEGATS_MAGE)*(TAUX_BOOST-1)*VITESSE_SHAMAN/LATENCE_BOOST
    dpt1_max_shaman = max(FORCE_GOB*TAUX_ATTAQUE*TAUX_EPEE,FORCE_SENT*TAUX_ATTAQUE*TAUX_LANCE,FORCE_GUER*TAUX_ATTAQUE*TAUX_CIMETERE,DEGATS_MAGE)*(TAUX_BOOST-1)*VITESSE_SHAMAN/LATENCE_BOOST
    dpt2_min_shaman = min(FORCE_GOB*TAUX_ATTAQUE*TAUX_EPEE,FORCE_SENT*TAUX_ATTAQUE*TAUX_LANCE,FORCE_GUER*TAUX_ATTAQUE*TAUX_CIMETERE,DEGATS_MAGE)*(TAUX_BOOST-1)*(REGEN_SHAMAN)/PM_BOOST
    dpt2_max_shaman = max(FORCE_GOB*TAUX_ATTAQUE*TAUX_EPEE,FORCE_SENT*TAUX_ATTAQUE*TAUX_LANCE,FORCE_GUER*TAUX_ATTAQUE*TAUX_CIMETERE,DEGATS_MAGE)*(TAUX_BOOST-1)*(REGEN_SHAMAN)/PM_BOOST
    dpt_chef = FORCE_CHEF*TAUX_ATTAQUE*TAUX_EPEE*VITESSE_CHEF/LATENCE_ATTAQUE
    dpt_boost_chef = dpt_chef * TAUX_BOOST
    print("Un bref aperçu des stats\n\n")
    print(f"Joueur :         {PV_JOUEUR:>3} PV, {dpt_joueur:.2f} ({dpt_multi_boost_joueur:.2f}, {dpt_boost_joueur:.2f}) dpt, {REGEN_JOUEUR} regen")
    print(f"Receptionniste : {PV_RECEPTIONNISTE:>3} PV, {dpt_receptionniste:.2f} ({dpt_multi_boost_receptionniste:.2f}, {dpt_boost_receptionniste:.2f}) dpt, {REGEN_RECEPTIONNISTE} regen, {TAUX_ARMURE_ENCOMBRANT:.2%} degats bloqués")
    print(f"Paumé :          {PV_PAUME:>3} PV, {dpt_paume:.2f} ({dpt_multi_boost_paume:.2f}, {dpt_boost_paume:.2f}) dpt, {REGEN_PAUME} regen, {TAUX_TUNIQUE:.2%} degats bloqués")
    print(f"Peureuse :       {PV_PEUREUSE:>3} PV, {dpt1_min_peureuse:.2f}~{dpt1_max_peureuse:.2f} dpt1, {dpt2_min_peureuse:.2f}~{dpt2_max_peureuse:.2f} dpt2, {dpt1_multi_peureuse:.2f} multi-dpt1, {dpt2_multi_peureuse:.2f} multi-dpt2, {REGEN_PEUREUSE} regen")
    print(f"Encombrant :     {PV_ENCOMBRANT:>3} PV, {dpt_encombrant:.2f} ({dpt_multi_boost_encombrant:.2f}, {dpt_boost_encombrant:.2f}) dpt, {REGEN_ENCOMBRANT} regen, {TAUX_ARMURE_ENCOMBRANT:.2%} degats bloqués")
    print(f"Alchimiste :     {PV_ALCHIMISTE:>3} PV, {dpt1_alchimiste:.2f} ({dpt1_multi_boost_alchimiste:.2f}, {dpt1_boost_alchimiste:.2f}) dpt1, {dpt2_alchimiste:.2f} ({dpt2_multi_boost_alchimiste:.2f}, {dpt2_boost_alchimiste:.2f}) dpt2, {REGEN_ALCHIMISTE} regen")
    print(f"Peste :          {PV_PESTE:>3} PV, {pvt1_peste:.2f} ({pvt2_peste:.2f}) soin par tour, {pvt1_multi_peste:.2f} ({pvt2_multi_peste:.2f}) multi-soin par tour, {REGEN_PESTE} regen, {DEGATS_SOUTANE} degats max")
    print(f"Bombe atomique : {PV_BOMBE:>3} PV, {dpt1_bombe:.2f} ({dpt1_multi_boost_bombe:.2f}, {dpt1_boost_bombe:.2f}) dpt1, {dpt2_bombe:.2f} ({dpt2_multi_boost_bombe:.2f}, {dpt2_boost_bombe:.2f}) dpt2, {REGEN_BOMBE} regen")
    print(f"Marchand :       {PV_MARCHAND:>3} PV, {dpt_marchand:.2f} ({dpt_multi_boost_marchand:.2f}, {dpt_boost_marchand:.2f}) dpt, {REGEN_MARCHAND} regen, {TAUX_ARMURE_MARCHAND} degats bloqués")
    print(f"Gobelin :    {PV_GOB:>3} PV, {dpt_gob:.2f} ({dpt_boost_gob:.2f}) dpt")
    print(f"Sentinelle : {PV_SENT:>3} PV, {dpt_sent:.2f} ({dpt_boost_sent:.2f}) dpt, {1-(1-TAUX_ARMURE_SENT)*(1-TAUX_HAUME):.2%} degats bloqués")
    print(f"Guerrier :   {PV_GUER:>3} PV, {dpt_guer:.2f} ({dpt_boost_guer:.2f}) dpt, {TAUX_ARMURE_GUER:.2%} degats bloqués")
    print(f"Mage :       {PV_MAGE:>3} PV, {dpt1_mage:.2f} ({dpt1_boost_mage:.2f}) dpt1, {dpt2_mage:.2f} ({dpt2_boost_mage:.2f}) dpt2")
    print(f"Shaman :     {PV_SHAMAN:>3} PV, {dpt1_min_shaman:.2f}~{dpt1_max_shaman:.2f} dpt1, {dpt2_min_shaman:.2f}~{dpt2_max_shaman:.2f} dpt2")
    print(f"Chef :       {PV_CHEF:>3} PV, {dpt_chef:.2f} ({dpt_boost_chef:.2f}) dpt, {REGEN_CHEF} regen, {1-(1-TAUX_ARMURE_SENT)*(1-TAUX_HAUME):.2%} degats bloqués")

except SyntaxError:
    print("La syntaxe du fichier Equilibrage.py est incorrecte.")
except ModuleNotFoundError:
    print("Il n'y a pas de fichier Equilibrage.py, on va garder l'équilibrage par défaut.")


# /!\ Mettre les lignes à jour !
# Contenu du fichier :
# La classe Controleur (lignes 0-500) ;
# La classe Labyrinthe (lignes 500-900), avec :
#    La classe Generateur (lignes 900-1200) ;
#    La classe Case (lignes 1200-1300) ;
#    La classe Murs (lignes 1300-1400) ;
#    La classe Pattern (lignes 1400-1700) ;
# La classe Entitee (lignes 1700), avec ;
#    La classe Entitee_superieure (lignes 1700) ;
#    La classe Fantome (lignes 1700) ;
#    La classe Cadavre (lignes 1700) ;
#    La classe Oeuf (lignes 1700) ;
#    La classe Agissant (lignes 1700-2000) ;
#    La classe Joueur (lignes 2000-2200) ;
#    La classe Item et ses multiples sous-classes (lignes 2200-2500) ;
#    La classe Inventaire (lignes 2500-2700) ;
# La classe Esprit (lignes 2700-2900) ;
# Les mutiples classes de Magie_* (lignes 2900-3900) ;
# La classe Effet et ses multiples sous-classes (lignes 3900-4800) ;
# La classe Sort et ses multiples sous-classes (lignes 4800-5100) ;
# La classe Affichage (lignes 5100-5300).

# Conseil de navigation : Ctrl+f + "Class Bidule" vous enverra au début de la classe Bidule


#    .
#   / \     Je ne respecte absolument pas les régles de base de la programmation objet, puisque je vais donner à tous les objets de mon univers (ou presque) ce controleur qui les contient tous (ou presque).
#  / ! \    S'attendre à de vives ciritques !
# /_____\
