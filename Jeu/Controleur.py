from Jeu.Constantes import *
from Jeu.Entitee.Entitees import *
from Jeu.Labyrinthe.Labyrinthe import *
from Jeu.Effet.Effets import *
from Jeu.Esprit.Esprits import *
from Modifiers import *

from typing import Dict, List, Any, Set
import random

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

    CONSTANTES_STATS["heros"]["pv"][1] = PV_HEROS
    CONSTANTES_STATS["heros"]["vitesse"][1] = VITESSE_HEROS
    CONSTANTES_STATS["heros"]["force"][1] = FORCE_HEROS
    CONSTANTES_STATS["heros"]["regen_pv_max"][1] = REGEN_MAX_HEROS
    CONSTANTES_STATS["heros"]["regen_pv_min"][1] = REGEN_MIN_HEROS
    CONSTANTES_STATS["heros"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_HEROS
    CONSTANTES_STATS["receptionniste"]["pv"][1] = PV_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["vitesse"][1] = VITESSE_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["force"][1] = FORCE_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["regen_pv_max"][1] = REGEN_MAX_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["regen_pv_min"][1] = REGEN_MIN_RECEPTIONNISTE
    CONSTANTES_STATS["receptionniste"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_RECEPTIONNISTE
    CONSTANTES_STATS["paume"]["pv"][1] = PV_PAUME
    CONSTANTES_STATS["paume"]["vitesse"][1] = VITESSE_PAUME
    CONSTANTES_STATS["paume"]["force"][1] = FORCE_PAUME
    CONSTANTES_STATS["paume"]["regen_pv_max"][1] = REGEN_MAX_PAUME
    CONSTANTES_STATS["paume"]["regen_pv_min"][1] = REGEN_MIN_PAUME
    CONSTANTES_STATS["paume"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_PAUME
    CONSTANTES_STATS["peureuse"]["pv"][1] = PV_PEUREUSE
    CONSTANTES_STATS["peureuse"]["vitesse"][1] = VITESSE_PEUREUSE
    CONSTANTES_STATS["peureuse"]["force"][1] = FORCE_PEUREUSE
    CONSTANTES_STATS["peureuse"]["regen_pv_max"][1] = REGEN_MAX_PEUREUSE
    CONSTANTES_STATS["peureuse"]["regen_pv_min"][1] = REGEN_MIN_PEUREUSE
    CONSTANTES_STATS["peureuse"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_PEUREUSE
    CONSTANTES_STATS["peureuse"]["pm"][1] = PM_PEUREUSE
    CONSTANTES_STATS["peureuse"]["regen_pm"][1] = REGEN_PM_PEUREUSE
    CONSTANTES_STATS["encombrant"]["pv"][1] = PV_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["vitesse"][1] = VITESSE_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["force"][1] = FORCE_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["regen_pv_max"][1] = REGEN_MAX_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["regen_pv_min"][1] = REGEN_MIN_ENCOMBRANT
    CONSTANTES_STATS["encombrant"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_ENCOMBRANT
    CONSTANTES_STATS["alchimiste"]["pv"][1] = PV_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["vitesse"][1] = VITESSE_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["force"][1] = FORCE_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["regen_pv_max"][1] = REGEN_MAX_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["regen_pv_min"][1] = REGEN_MIN_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["pm"][1] = PM_ALCHIMISTE
    CONSTANTES_STATS["alchimiste"]["regen_pm"][1] = REGEN_PM_ALCHIMISTE
    CONSTANTES_STATS["peste"]["pv"][1] = PV_PESTE
    CONSTANTES_STATS["peste"]["vitesse"][1] = VITESSE_PESTE
    CONSTANTES_STATS["peste"]["force"][1] = FORCE_PESTE
    CONSTANTES_STATS["peste"]["regen_pv_max"][1] = REGEN_MAX_PESTE
    CONSTANTES_STATS["peste"]["regen_pv_min"][1] = REGEN_MIN_PESTE
    CONSTANTES_STATS["peste"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_PESTE
    CONSTANTES_STATS["peste"]["pm"][1] = PM_PESTE
    CONSTANTES_STATS["peste"]["regen_pm"][1] = REGEN_PM_PESTE
    CONSTANTES_STATS["bombe_atomique"]["pv"][1] = PV_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["vitesse"][1] = VITESSE_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["force"][1] = FORCE_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["regen_pv_max"][1] = REGEN_MAX_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["regen_pv_min"][1] = REGEN_MIN_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["pm"][1] = PM_BOMBE
    CONSTANTES_STATS["bombe_atomique"]["regen_pm"][1] = REGEN_PM_BOMBE
    CONSTANTES_STATS["marchand"]["pv"][1] = PV_MARCHAND
    CONSTANTES_STATS["marchand"]["vitesse"][1] = VITESSE_MARCHAND
    CONSTANTES_STATS["marchand"]["force"][1] = FORCE_MARCHAND
    CONSTANTES_STATS["marchand"]["regen_pv_max"][1] = REGEN_MAX_MARCHAND
    CONSTANTES_STATS["marchand"]["regen_pv_min"][1] = REGEN_MIN_MARCHAND
    CONSTANTES_STATS["marchand"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_MARCHAND
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
    CONSTANTES_STATS["chef_gobelin"]["regen_pv_max"][1] = REGEN_MAX_CHEF
    CONSTANTES_STATS["chef_gobelin"]["regen_pv_min"][1] = REGEN_MIN_CHEF
    CONSTANTES_STATS["chef_gobelin"]["restauration_regen_pv"][1] = RESTAURATION_REGEN_CHEF

    dpt_heros = FORCE_HEROS*TAUX_STOMP*VITESSE_HEROS/LATENCE_STOMP
    dpt_boost_heros = dpt_heros * TAUX_BOOST
    dpt_multi_boost_heros = dpt_heros * TAUX_MULTI_BOOST
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
    dpt1_min_peureuse = min(FORCE_HEROS*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*VITESSE_PEUREUSE/LATENCE_BOOST
    dpt1_max_peureuse = max(FORCE_HEROS*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*VITESSE_PEUREUSE/LATENCE_BOOST
    dpt2_min_peureuse = min(FORCE_HEROS*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*(REGEN_PM_PEUREUSE+REGEN_PM_ROBE)/PM_BOOST
    dpt2_max_peureuse = max(FORCE_HEROS*TAUX_STOMP,FORCE_PAUME*TAUX_STOMP,FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT,DEGATS_SECOUSSE,DEGATS_VOLCAN,FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_BOOST-1)*(REGEN_PM_PEUREUSE+REGEN_PM_ROBE)/PM_BOOST
    dpt1_multi_peureuse = (FORCE_HEROS*TAUX_STOMP+FORCE_PAUME*TAUX_STOMP+FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT+DEGATS_SECOUSSE+DEGATS_VOLCAN+FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_MULTI_BOOST-1)*VITESSE_PEUREUSE/LATENCE_MULTI_BOOST
    dpt2_multi_peureuse = (FORCE_HEROS*TAUX_STOMP+FORCE_PAUME*TAUX_STOMP+FORCE_ENCOMBRANT*TAUX_ATTAQUE*TAUX_EPEE_ENCOMBRANT+DEGATS_SECOUSSE+DEGATS_VOLCAN+FORCE_MARCHAND*TAUX_ATTAQUE*TAUX_EPEE_MARCHAND)*(TAUX_MULTI_BOOST-1)*(REGEN_PM_PEUREUSE+REGEN_PM_ROBE)/PM_MULTI_BOOST
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
    print(f"Joueur :         {PV_HEROS:>3} PV, {dpt_heros:.2f} ({dpt_multi_boost_heros:.2f}, {dpt_boost_heros:.2f}) dpt, {REGEN_HEROS} regen")
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

class Controleur():
    def __init__(self,parametres:Dict,screen:pygame.Surface):
        #print("Initialisation du controleur")
        self.labs:Dict[str,Labyrinthe] = {} #Un dictionnaire avec tous les labyrinthes, indéxés par leur identifiant dans les positions.
        #print("Labyrinthe : check")
        self.entitees:Dict[int,Entitee] = {}
        #print("Entitées : check")
        self.esprits:Dict[str,Esprit] = {}
        self.labs_courants:List[Labyrinthe] = []
        self.entitees_courantes:Set[int] = set()
        self.esprits_courants:List[str] = []
        self.joueur:PJ|PJ_mage|None = None
        self.pause = False
        self.nb_tours = 0
        self.phase = TOUR
        self.phases = [TOUR]
        if parametres == None:
            self.tour_par_seconde = 0
        else:
            self.tour_par_seconde = parametres["tours_par_seconde"]

    def __getitem__(self,key) -> Union[Labyrinthe,Case,Mur,Entitee,Item,Agissant,Any]:
        if isinstance(key,tuple):
            if len(key)==2: #Position et direction
                return self.labs[key[0].lab][key[0]][key[1]]
            elif len(key)==4:
                return self.labs[key[0]][Position(key[0],key[1],key[2])][key[3]]
            elif len(key)==3:
                return self.labs[key[0]][Position(key[0],key[1],key[2])]
        elif isinstance(key,Cote):
            return self.labs[key.emplacement.lab][key.emplacement][key.direction]
        elif isinstance(key,Position):
            return self.labs[key.lab][key]
        elif isinstance(key,int):
            return self.entitees[key]
        elif isinstance(key,str):
            return self.labs[key]
        print(f"n'a pas pu trouver {key}")
        return NotImplemented

    def __setitem__(self,key,value):
        if isinstance(key,tuple):
            if len(key)==2: #Position et direction
                self.labs[key[0].lab][key[0]][key[1]] = value
            elif len(key)==4:
                self.labs[key[0]][Position(key[0],key[1],key[2])][key[3]] = value
            elif len(key)==3:
                self.labs[key[0]][Position(key[0],key[1],key[2])] = value
        elif isinstance(key,Cote):
            self.labs[key.emplacement.lab][key.emplacement][key.direction] = value
        elif isinstance(key,Position):
            self.labs[key.lab][key] = value
        elif isinstance(key,int):
            self.entitees[key] = value

    def jeu(self):

        self.esprits["heros"] = Esprit_humain(2,self)

        autre = Alchimiste(self,Position("Étage 1 : test",1,0))
        self.ajoute_entitee(autre)
        self.esprits["alchimiste"] = Esprit_humain(autre.ID,self)

        chaudron = Chaudron_gobelin(Position("Étage 1 : test",1,3))
        self.ajoute_entitee(chaudron)

        peaux = [Peau_gobelin(Position("Étage 1 : test",1,2)),Peau_gobelin(Position("Étage 1 : test",1,4))]
        self.ajoute_entitees(peaux)

        gobel1 = Chef_gobelin(self,Position("Étage 1 : test",11,15),1)
        self.ajoute_entitee(gobel1)
        #self.esprits["gobel1"]=Esprit_simple("gobel1",[gobel1.ID],["humain"],self)

        gobel2 = Sentinelle_gobelin(self,Position("Étage 1 : test",2,6),1)
        self.ajoute_entitee(gobel2)
        self.esprits["gobel2"]=Esprit_simple("gobel2",[gobel1.ID,gobel2.ID],[],self)

        self.ajoute_entitee(Parchemin_vierge(Position("Étage 1 : test",1,5)))

        paterns1 = [Pattern(Position("Étage 1 : test",0,0),Decalage(20,20),[])]
        self.labs["Étage 1 : test"]=Labyrinthe("Étage 1 : test",Decalage(20,20),Position("Étage 1 : test",0,0),paterns1,1,1,TERRE,1)

        self.joueur.position = Position("Étage 1 : test",0,0)
        self.active_lab("Étage 1 : test")

    def experience5(self):
        #Une expérience sur les paramètres optimaux des esprits



        #L'équipe 1 est très mal disposée, avec les DPS/Tank à l'arrière et les shamans à l'avant
        gobel1 = Sentinelle_gobelin(self,("Labo",1,2),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Labo",3,0),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,("Labo",4,4),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,("Labo",2,1),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Labo",0,1),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Labo",3,6),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Labo",8,2),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,("Labo",9,7),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Labo",9,8),1)
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,("Labo",0,0),1)
        self.ajoute_entitee(boss)
        self.esprits["Equipe 1"]=Esprit_simple("Equipe 1",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,boss.ID],["gobelin"],self)


        #L'équipe 2 est disposée de façon optimale, avec les DPS/Tank à l'avant et les shamans à l'arrière
        gobel1 = Sentinelle_gobelin(self,("Labo",10,10),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,("Labo",10,11),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,("Labo",12,12),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,("Labo",11,10),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,("Labo",11,11),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,("Labo",13,13),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,("Labo",14,14),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,("Labo",19,19),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,("Labo",19,18),1)
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,("Labo",12,11),1)
        self.ajoute_entitee(boss)
        self.esprits["Equipe 2"]=Esprit_simple("Equipe 2",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,boss.ID],["gobelin"],self)



        #Le labyrinthe est partiellement fermé
        self.labs["Labo"]=Labyrinthe("Labo",Decalage(20,20),Position("Labo",0,0),[],1,1,TERRE,0.5)
        self.active_lab("Labo")

    def check_exp5(self):
        mort1 = 0
        for ID in self.esprits["Equipe 1"].corps:
            if self[ID].etat == "mort":
                mort1 += 1

        mort2 = 0
        for ID in self.esprits["Equipe 2"].corps:
            if self[ID].etat == "mort":
                mort2 += 1

        if (mort1 == 10 and mort2 == 10) or self.nb_tours >= 200:
            return [mort1,mort2,self.nb_tours]
        if mort1 == 10:
            return [mort1,mort2,self.nb_tours]
        if mort2 == 10:
            return [mort1,mort2,self.nb_tours]
        return False

    def tuto(self):

        #On crée le premier étage et son occupant :
        receptionniste = Receptionniste(self,Position("Étage 1 : couloir",14,0))
        self.ajoute_entitee(receptionniste)
        self.esprits["receptionniste"] = Esprit_humain(receptionniste.ID,self)
        paterns1 = [Pattern(Position("Étage 1 : couloir",9,0),Decalage(0,3),[Cote(Decalage(0,1),GAUCHE)],["clé_couloir"])]
        self.labs["Étage 1 : couloir"]=Labyrinthe("Étage 1 : couloir",Decalage(19,3),Position("Étage 1 : couloir",0,0),paterns1,1,1,TERRE,1)

        #On crée le deuxième étage et son occupant :
        paume = Paume(self,Position("Étage 2 : labyrinthe",1,0))
        self.ajoute_entitee(paume)
        self.esprits["paume"] = Esprit_humain(paume.ID,self)
        paterns2 = [Pattern(Position("Étage 2 : labyrinthe",0,0),Decalage(5,5),[Cote(Decalage(4,0),DROITE),Cote(Decalage(4,1),DROITE),Cote(Decalage(4,2),DROITE),Cote(Decalage(4,3),DROITE),Cote(Decalage(4,4),DROITE)]),
                    Pattern(Position("Étage 2 : labyrinthe",5,5),Decalage(5,5),[Cote(Decalage(0,0),GAUCHE)],["Porte_centre_2"])]
        self.labs["Étage 2 : labyrinthe"]=Labyrinthe("Étage 2 : labyrinthe",Decalage(15,15),Position("Étage 2 : labyrinthe",0,0),paterns2,1,1,TERRE,0.2)
        self.construit_escalier(Cote(Position("Étage 1 : couloir",18,1),DROITE),Cote(Position("Étage 2 : labyrinthe",0,0),GAUCHE))

        #On crée le troisième étage et son occupante :
        peureuse = Peureuse(self,Position("Étage 3 : combat",8,8))
        self.ajoute_entitee(peureuse)
        self.esprits["peureuse"] = Esprit_humain(peureuse.ID,self)
        cle1 = Cle(Position("Étage 3 : combat",12,13),["Porte_avant_prison_5"])
        self.ajoute_entitee(cle1)
        peureuse.inventaire.ajoute(cle1)
        gobel1 = Premier_monstre(self,Position("Étage 3 : combat",3,8),1)
        self.ajoute_entitee(gobel1)
        self.esprits["gobelins_combat"]=Esprit_simple("gobelins_combat",[gobel1.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns3 = [Pattern(Position("Étage 3 : combat",4,4),Decalage(7,7),[Cote(Decalage(0,3),GAUCHE),Cote(Decalage(0,4),GAUCHE),Cote(Decalage(0,5),GAUCHE),Cote(Decalage(3,0),HAUT),Cote(Decalage(4,0),HAUT),Cote(Decalage(5,0),HAUT),Cote(Decalage(0,0),HAUT),Cote(Decalage(1,0),HAUT),Cote(Decalage(0,0),GAUCHE),Cote(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 3 : combat",3,3),Decalage(3,3),[Cote(Decalage(0,0),HAUT),Cote(Decalage(2,2),BAS),Cote(Decalage(0,0),GAUCHE),Cote(Decalage(2,2),DROITE)]),
                    Pattern(Position("Étage 3 : combat",7,2),Decalage(3,3),[Cote(Decalage(1,0),HAUT),Cote(Decalage(1,2),BAS)]),
                    Pattern(Position("Étage 3 : combat",8,8),Decalage(3,3),[Cote(Decalage(0,0),HAUT),Cote(Decalage(0,0),GAUCHE)]),
                    Pattern(Position("Étage 3 : combat",0,3),Decalage(1,0)),
                    Pattern(Position("Étage 3 : combat",1,3),Decalage(0,3)),
                    Pattern(Position("Étage 3 : combat",1,6),Decalage(2,0)),
                    Pattern(Position("Étage 3 : combat",2,7),Decalage(3,3),[Cote(Decalage(0,1),GAUCHE),Cote(Decalage(2,1),DROITE)])]
        self.labs["Étage 3 : combat"]=Labyrinthe("Étage 3 : combat",Decalage(11,11),Position("Étage 3 : combat",0,0),paterns3,1,1,TERRE,0.2)
        self.construit_escalier(Cote(Position("Étage 2 : labyrinthe",1,5),HAUT),Cote(Position("Étage 3 : combat",10,10),BAS))

        #On crée le quatrième étage et ses occupants :
        codeur = Codeur(self,Position("Étage 4 : monstres",15,1))
        self.ajoute_entitee(codeur)
        self.esprits["codeur"] = Esprit_humain(codeur.ID,self)
        gobel1 = Troisieme_monstre(self,Position("Étage 4 : monstres",15,8),1) #Une sentinelle garde les abords
        self.ajoute_entitee(gobel1)
        gobel2 = Deuxieme_monstre(self,Position("Étage 4 : monstres",10,4),1) #Ainsi qu'un mage,
        self.ajoute_entitee(gobel2)
        self.esprits["gobelins_monstres"]=Esprit_simple("gobelins_monstres",[gobel1.ID,gobel2.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns4 = [Pattern(Position("Étage 4 : monstres",4,0),Decalage(10,2),[Cote(Decalage(0,1),GAUCHE),Cote(Decalage(9,1),DROITE)],[],False),
                    Pattern(Position("Étage 4 : monstres",7,6),Decalage(10,0),[Cote(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 4 : monstres",14,0),Decalage(3,3),[Cote(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 4 : monstres",0,7),Decalage(4,3),[Cote(Decalage(3,1),DROITE)],["Porte_coin_4"])]
        self.labs["Étage 4 : monstres"]=Labyrinthe("Étage 4 : monstres",Decalage(17,10),Position("Étage 4 : monstres",0,0),paterns4,1,1,TERRE,0.1,[1,5,1,5])
        self.construit_escalier(Cote(Position("Étage 3 : combat",0,3),GAUCHE),Cote(Position("Étage 4 : monstres",16,5),DROITE))

        #On crée le cinquième étage et ses occupants :
        encombrant = Encombrant(self,Position("Étage 5 : portes",2,3))
        self.ajoute_entitee(encombrant)
        self.esprits["encombrant"] = Esprit_humain(encombrant.ID,self)
        cle1 = Cle(Position("Étage 5 : portes",2,3),["Porte_sortie_encombrant_5"])
        self.ajoute_entitee(cle1)
        encombrant.inventaire.ajoute(cle1)
        passepartout1 = Cle(Position("Étage 5 : portes",5,5),["Porte_première_cellule_5","Porte_double_cellule_première_5","Porte_grande_cellule_5","Porte_cellule_biscornue_5","Porte_entree_encombrant_5"])
        self.ajoute_entitee(passepartout1)
        cle2 = Cle(Position("Étage 5 : portes",1,9),["Porte_couloir_5"])
        self.ajoute_entitee(cle2)
        cle3 = Cle(Position("Étage 5 : portes",1,2),["Porte_fin_couloir_5"])
        self.ajoute_entitee(cle3)
        cle5 = Cle(Position("Étage 5 : portes",3,6),["Porte_armurerie_6"])
        self.ajoute_entitee(cle5)
        cle6 = Cle(Position("Étage 5 : portes",0,6),["Porte_quatrième_armurerie_9"])
        self.ajoute_entitee(cle6)
        cle7 = Cle(Position("Étage 5 : portes",0,12),["Porte_annexe_droite_7"])
        self.ajoute_entitee(cle7)
        cle8 = Cle(Position("Étage 5 : portes",0,6),["Porte_troisième_armurerie_9"])
        self.ajoute_entitee(cle8)
        cle9 = Cle(Position("Étage 5 : portes",9,13),["Porte_anti_anti_chambre_8"])
        self.ajoute_entitee(cle9)
        gobel1 = Sentinelle_gobelin(self,Position("Étage 5 : portes",6,10),1) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,Position("Étage 5 : portes",5,5),1) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel2)
        gobel2.inventaire.ajoute(passepartout1)
        gobel3 = Guerrier_gobelin(self,Position("Étage 5 : portes",8,1),1) #Un renégat mis à l'isolement pour le mater, ou un piège diabolique dirigé contre le joueur ?
        self.ajoute_entitee(gobel3)
        slime = Slime(self,Position("Étage 5 : portes",8,7),1) #Un slime ! Est-ce que les gobelins ont pris soin de l'affaiblir ?
        self.ajoute_entitee(slime)
        ombriul = Ombriul(self,Position("Étage 5 : portes",5,7),1) #Un prisonnier de guerre
        self.ajoute_entitee(ombriul)
        #Rajouter quelques cadavres pour le nécromancien
        self.esprits["gobelins_portes"]=Esprit_simple("gobelins_portes",[gobel1.ID,gobel2.ID,gobel3.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        self.esprits["ombriul_captif"]=Esprit_simple("ombriul_captif",[ombriul.ID],["humain"],self)
        esprit_slime = Esprit_slime(slime.ID,self)
        self.esprits[esprit_slime.nom]=esprit_slime #Les esprits des slimes sont presque aussi compliqués que ceux des humains, les ruptures en moins.
        paterns5 = [Pattern(Position("Étage 5 : portes",7,11),Decalage(3,3),[Cote(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 5 : portes",0,5),Decalage(5,3),[Cote(Decalage(1,2),BAS)]),
                    Pattern(Position("Étage 5 : portes",0,1),Decalage(5,4),[Cote(Decalage(0,0),HAUT),Cote(Decalage(4,2),DROITE)],["Porte_sortie_encombrant_5","Porte_entree_encombrant_5"]),
                    Pattern(Position("Étage 5 : portes",0,8),Decalage(3,3),[Cote(Decalage(1,0),HAUT),Cote(Decalage(2,1),DROITE),Cote(Decalage(2,2),BAS)],["Porte_première_cellule_5","Porte_couloir_5"]),
                    Pattern(Position("Étage 5 : portes",0,11),Decalage(4,3),[Cote(Decalage(2,0),HAUT)],["Porte_avant_prison_5"]),
                    Pattern(Position("Étage 5 : portes",4,11),Decalage(3,3),[Cote(Decalage(1,0),HAUT),Cote(Decalage(2,1),DROITE)],["Porte_double_cellule_première_5","Porte_double_cellule_deuxième_5"]),
                    Pattern(Position("Étage 5 : portes",6,0),Decalage(4,5),[Cote(Decalage(2,4),BAS)],["Porte_grande_cellule_5"]),
                    Pattern(Position("Étage 5 : portes",5,6),Decalage(4,4),[Cote(Decalage(3,2),DROITE)],["Porte_cellule_biscornue_5"]), #/!\ À corriger /!\
                    Pattern(Position("Étage 5 : portes",3,7),Decalage(2,2),[Cote(Decalage(1,1),BAS),Cote(Decalage(1,1),DROITE)]),
                    Pattern(Position("Étage 5 : portes",4,8),Decalage(2,2),[Cote(Decalage(0,0),HAUT),Cote(Decalage(0,0),GAUCHE)]),
                    Pattern(Position("Étage 5 : portes",5,6),Decalage(2,2),[Cote(Decalage(0,1),GAUCHE)])]
        self.labs["Étage 5 : portes"]=Labyrinthe("Étage 5 : portes",Decalage(10,14),Position("Étage 5 : portes",0,0),paterns5,1,1,TERRE,1)
        self[Cote(Position("Étage 5 : portes",6,5),BAS)].cree_porte("Porte_cellule_plus_biscornue_5")
        self[Cote(Position("Étage 5 : portes",6,6),HAUT)].cree_porte("Porte_cellule_plus_biscornue_5")
        self[Cote(Position("Étage 5 : portes",4,0),DROITE)].cree_porte("Porte_fin_couloir_5")
        self[Cote(Position("Étage 5 : portes",5,0),GAUCHE)].cree_porte("Porte_fin_couloir_5")
        self[Cote(Position("Étage 5 : portes",2,11),HAUT)].cree_porte("Porte_avant_prison_5",Premiere_porte)
        self[Cote(Position("Étage 5 : portes",4,3),DROITE)].effets[1].auto = True
        self[Cote(Position("Étage 5 : portes",5,3),GAUCHE)].effets[1].auto = True
        self.construit_escalier(Cote(Position("Étage 4 : monstres",16,7),DROITE),Cote(Position("Étage 5 : portes",0,13),GAUCHE),Premiere_marche)

        #On crée le sixième étage et son occupant :
        #Nouvelle version :
        alchimiste = Alchimiste(self,Position("Étage 6 : potions",13,1))
        self.ajoute_entitee(alchimiste)
        self.esprits["alchimiste"] = Esprit_humain(alchimiste.ID,self)

        chaudrons_6 = [Chaudron_gobelin(Position("Étage 6 : potions",12,4)),
                       Chaudron_gobelin(Position("Étage 6 : potions",14,8))]
        self.ajoute_entitees(chaudrons_6)

        cles_6 = [Cle(Position("Étage 6 : potions",4,1),["Porte_cuisine"]), #(0)
                  Cle(Position("Étage 6 : potions",11,6),["Première_porte_potions"]), #(1)
                  Cle(Position("Étage 6 : potions",13,10),["Porte_inutile_potion"]), #(2)
                  Cle(Position("Étage 6 : potions",4,4),["Deuxième_porte_potions"]), #(3)
                  Cle(Position("Étage 6 : potions",3,9),["Troisième_porte_potions"]), #(4)
                  Cle(Position("Étage 6 : potions",0,11),["Porte_double_cellule_deuxième_5"]),
                  Cle(Position("Étage 6 : potions",11,10),["Porte_salle_commune_7"])]
        self.ajoute_entitees(cles_6)

        consomables_6 = [Parchemin_protection(Position("Étage 6 : potions",2,13)),
                         Potion_force(Position("Étage 6 : potions",1,13))]
        self.ajoute_entitees(consomables_6)

        ingredients_6 = [Peau_gobelin(Position("Étage 6 : potions",12,6)),
                         Dent_gobelin(Position("Étage 6 : potions",14,8)),
                         Pierre_solide(Position("Étage 6 : potions",9,1)),
                         Hypokute(Position("Étage 6 : potions",6,7))]
        self.ajoute_entitees(ingredients_6)

        gobel1 = Gobelin(self,Position("Étage 6 : potions",11,6),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Mage_gobelin(self,Position("Étage 6 : potions",13,10),1)
        self.ajoute_entitee(gobel2)
        gobel2.inventaire.ajoute(cles_6[2])
        gobel3 = Sentinelle_gobelin(self,Position("Étage 6 : potions",4,4),1)
        self.ajoute_entitee(gobel3)
        gobel3.inventaire.ajoute(cles_6[3])
        gobel4 = Mage_gobelin(self,Position("Étage 6 : potions",6,6),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,Position("Étage 6 : potions",4,10),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Guerrier_gobelin(self,Position("Étage 6 : potions",12,4),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Guerrier_gobelin(self,Position("Étage 6 : potions",14,4),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,Position("Étage 6 : potions",13,7),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,Position("Étage 6 : potions",10,9),1)
        self.ajoute_entitee(gobel9)
        self.esprits["gobelins_potions"]=Esprit_simple("gobelins_potions",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)

        paterns6 = [Pattern(Position("Étage 6 : potions",9,3),Decalage(6,8),[Cote(Decalage(0,0),GAUCHE),Cote(Decalage(0,1),GAUCHE),Cote(Decalage(0,2),GAUCHE),Cote(Decalage(0,3),GAUCHE),Cote(Decalage(3,0),HAUT),Cote(Decalage(4,0),HAUT),Cote(Decalage(5,0),HAUT),Cote(Decalage(0,7),GAUCHE),Cote(Decalage(0,7),BAS),Cote(Decalage(3,7),BAS),Cote(Decalage(4,7),BAS),Cote(Decalage(5,7),BAS)]), #La cuisine, avec le shaman et les derniers gobelins (0)
                    Pattern(Position("Étage 6 : potions",6,0),Decalage(3,2),[]), #(5)
                    Pattern(Position("Étage 6 : potions",3,0),Decalage(3,2),[Cote(Decalage(0,1),GAUCHE)]), #(12) /!\ Il y a un problème ici ?
                    Pattern(Position("Étage 6 : potions",0,3),Decalage(2,3),[Cote(Decalage(1,0),HAUT)]), #(10)
                    Pattern(Position("Étage 6 : potions",0,0),Decalage(3,3),[Cote(Decalage(1,2),BAS),Cote(Decalage(2,1),DROITE),Cote(Decalage(2,2),DROITE),Cote(Decalage(2,2),BAS)],["Deuxième_porte_potions","Troisième_porte_potions"]), #(11)
                    Pattern(Position("Étage 6 : potions",3,7),Decalage(3,2),[Cote(Decalage(0,1),GAUCHE)]), #(4) /!\ QUOI ?!?
                    Pattern(Position("Étage 6 : potions",0,6),Decalage(3,3),[Cote(Decalage(2,1),DROITE),Cote(Decalage(2,0),DROITE),Cote(Decalage(2,0),HAUT)],["Première_porte_potions"]), #(3)
                    Pattern(Position("Étage 6 : potions",0,9),Decalage(3,3),[Cote(Decalage(2,1),DROITE)]), #(8)
                    Pattern(Position("Étage 6 : potions",3,9),Decalage(3,3),[Cote(Decalage(0,1),GAUCHE)],["Porte_inutile_potion"]), #(9)
                    Pattern(Position("Étage 6 : potions",2,2),Decalage(5,5),[]), #(7)
                    Pattern(Position("Étage 6 : potions",12,9),Decalage(3,3),[]), #(6)
                    Pattern(Position("Étage 6 : potions",11,0),Decalage(4,4),[Cote(Decalage(2,3),BAS),Cote(Decalage(0,3),GAUCHE),Cote(Decalage(0,3),BAS)],["Porte_cuisine"]), #(1)
                    Pattern(Position("Étage 6 : potions",8,3),Decalage(4,4),[]), #(2)
                    Pattern(Position("Étage 6 : potions",0,12),Decalage(5,3),[Cote(Decalage(4,1),DROITE)],["Porte_armurerie_6"])]
        self.labs["Étage 6 : potions"]=Labyrinthe("Étage 6 : potions",Decalage(15,15),Position("Étage 6 : potions",14,14),paterns6,1,1,TERRE,0.2)

        self.set_teleport(Cote(Position("Étage 6 : potions",11,2),GAUCHE),Cote(Position("Étage 6 : potions",8,3),HAUT),Premier_portail) # 1,2
        self.set_teleport(Cote(Position("Étage 6 : potions",13,0),HAUT),Cote(Position("Étage 6 : potions",1,6),DROITE),Premier_portail) # 1,3
        self.set_teleport(Cote(Position("Étage 6 : potions",3,8),BAS),Cote(Position("Étage 6 : potions",6,0),GAUCHE)) # 4,5
        self.set_teleport(Cote(Position("Étage 6 : potions",4,8),BAS),Cote(Position("Étage 6 : potions",13,9),HAUT)) # 4,6
        self.set_teleport(Cote(Position("Étage 6 : potions",5,8),BAS),Cote(Position("Étage 6 : potions",4,11),BAS)) # 4,9
        self.set_teleport(Cote(Position("Étage 6 : potions",12,10),GAUCHE),Cote(Position("Étage 6 : potions",7,0),HAUT)) # 6,5
        self.set_teleport(Cote(Position("Étage 6 : potions",13,11),BAS),Cote(Position("Étage 6 : potions",4,2),HAUT)) # 6,7
        self.set_teleport(Cote(Position("Étage 6 : potions",2,2),GAUCHE),Cote(Position("Étage 6 : potions",6,1),BAS)) # 7,5
        self.set_teleport(Cote(Position("Étage 6 : potions",6,5),DROITE),Cote(Position("Étage 6 : potions",0,11),BAS)) # 7,8
        self.set_teleport(Cote(Position("Étage 6 : potions",2,9),DROITE),Cote(Position("Étage 6 : potions",8,1),BAS)) # 8,5
        self.set_teleport(Cote(Position("Étage 6 : potions",5,11),BAS),Cote(Position("Étage 6 : potions",8,0),DROITE)) # 9,5
        self.set_teleport(Cote(Position("Étage 6 : potions",5,10),DROITE),Cote(Position("Étage 6 : potions",0,4),GAUCHE)) # 9,10

        self.construit_escalier(Cote(Position("Étage 5 : portes",0,0),GAUCHE),Cote(Position("Étage 6 : potions",14,0),DROITE))

        #On crée le septième étage et son occupante :
        peste = Peste(self,Position("Étage 7 : meutes",2,0))
        self.ajoute_entitee(peste)
        self.esprits["peste"] = Esprit_humain(peste.ID,self)
        cle1 = Cle(Position("Étage 7 : meutes",14,6),["Porte_sixième_armurerie_9"])
        self.ajoute_entitee(cle1)
        gobel1 = Guerrier_gobelin(self,Position("Étage 7 : meutes",4,3),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Guerrier_gobelin(self,Position("Étage 7 : meutes",10,3),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,Position("Étage 7 : meutes",6,4),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Gobelin(self,Position("Étage 7 : meutes",4,4),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Gobelin(self,Position("Étage 7 : meutes",10,4),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Gobelin(self,Position("Étage 7 : meutes",9,4),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,Position("Étage 7 : meutes",5,5),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,Position("Étage 7 : meutes",7,5),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,Position("Étage 7 : meutes",4,5),1)
        self.ajoute_entitee(gobel9)
        gobel10 = Shaman_gobelin(self,Position("Étage 7 : meutes",10,5),1)
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_meutes"]=Esprit_simple("gobelins_meutes",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,gobel10.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns7 = [Pattern(Position("Étage 7 : meutes",0,0),Decalage(15,2),[Cote(Decalage(1,1),BAS),Cote(Decalage(13,1),BAS)]),
                    Pattern(Position("Étage 7 : meutes",0,2),Decalage(4,3),[Cote(Decalage(1,0),HAUT),Cote(Decalage(2,2),BAS)],["Porte_annexe_gauche_7"]),
                    Pattern(Position("Étage 7 : meutes",4,2),Decalage(7,4),[Cote(Decalage(3,0),HAUT)],["Porte_salle_commune_7"]),
                    Pattern(Position("Étage 7 : meutes",11,2),Decalage(4,3),[Cote(Decalage(2,0),HAUT),Cote(Decalage(1,2),BAS)],["Porte_annexe_droite_7"])]
        self.labs["Étage 7 : meutes"]=Labyrinthe("Étage 7 : meutes",Decalage(15,10),Position("Étage 7 : meutes",0,9),paterns7,1,1,TERRE,0.3,[1,3,1,3])
        self.construit_escalier(Cote(Position("Étage 6 : potions",12,14),BAS),Cote(Position("Étage 7 : meutes",7,0),HAUT))

        #On crée le huitième étage et son occupante :
        bombe_atomique = Bombe_atomique(self,Position("Étage 8 : magie",8,7))
        self.ajoute_entitee(bombe_atomique)
        self.esprits["bombe_atomique"] = Esprit_humain(bombe_atomique.ID,self)
        cle1 = Cle(Position("Étage 8 : magie",0,7),["Porte_deuxième_armurerie_9"])
        self.ajoute_entitee(cle1)
        cle2 = Cle(Position("Étage 8 : magie",12,8),["Porte_anti_chambre_8"])
        self.ajoute_entitee(cle3)
        cle3 = Cle(Position("Étage 8 : magie",3,2),["Porte_annexe_gauche_7"])
        self.ajoute_entitee(cle2)
        gobel1 = Mage_gobelin(self,Position("Étage 8 : magie",1,1),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Mage_gobelin(self,Position("Étage 8 : magie",1,3),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Mage_gobelin(self,Position("Étage 8 : magie",2,0),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Mage_gobelin(self,Position("Étage 8 : magie",4,3),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Mage_gobelin(self,Position("Étage 8 : magie",5,7),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,Position("Étage 8 : magie",6,2),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,Position("Étage 8 : magie",8,0),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,Position("Étage 8 : magie",9,2),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Mage_gobelin(self,Position("Étage 8 : magie",5,5),1)
        self.ajoute_entitee(gobel9)
        gobel10 = Mage_gobelin(self,Position("Étage 8 : magie",10,9),1)
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_magie"]=Esprit_simple("gobelins_magie",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,gobel10.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns8 = [Pattern(Position("Étage 8 : magie",10,0),Decalage(5,4),[Cote(Decalage(0,1),GAUCHE),Cote(Decalage(3,3),BAS)]),
                    Pattern(Position("Étage 8 : magie",7,6),Decalage(4,3),[Cote(Decalage(0,1),GAUCHE),Cote(Decalage(3,1),DROITE)],["Porte_anti_chambre_8"]),
                    Pattern(Position("Étage 8 : magie",11,4),Decalage(4,6),[Cote(Decalage(2,0),HAUT),Cote(Decalage(0,4),GAUCHE)],["Porte_sas_8","Porte_anti_anti_chambre_8"])]
        self.labs["Étage 8 : magie"]=Labyrinthe("Étage 8 : magie",Decalage(15,10),Position("Étage 8 : magie",0,0),paterns8,1,1,TERRE,0.4)
        self.construit_escalier(Cote(Position("Étage 7 : meutes",0,9),GAUCHE),Cote(Position("Étage 8 : magie",14,7),DROITE)) #/!\ Rajouter un parchemin

        #On crée le neuvième étage et son occupant :
        marchand = Marchand(self,Position("Étage 9 : équippement",6,2))
        self.ajoute_entitee(marchand)
        cle1 = Cle(Position("Étage 9 : équippement",2,0),["Porte_première_armurerie_9"])
        self.ajoute_entitee(cle1)
        marchand.inventaire.ajoute(cle1)
        self.esprits["marchand"] = Esprit_humain(marchand.ID,self)
        cle2 = Cle(Position("Étage 9 : équippement",38,8),["Porte_cinquième_armurerie_9"])
        self.ajoute_entitee(cle2)
        cle1 = Cle(Position("Étage 9 : équippement",0,1),["Porte_sas_8"])
        self.ajoute_entitee(cle1)
        #On crée aussi quelques items :
        #Pas d'item dans l'armurerie où est le marchand, il l'a déjà dévalisée !
        #Dans la deuxième armurerie, une armure :
        armure = Armure_sentinelle_gobelin(Position("Étage 9 : équippement",5,9),1)
        self.ajoute_entitee(armure)
        #Dans la troisième, une lance :
        lance = Lance_de_gobelin(Position("Étage 9 : équippement",16,3),1)
        self.ajoute_entitee(lance)
        #Dans la quatrième, huit anneaux :
        anneau_1 = Anneau_magique_gobelin(Position("Étage 9 : équippement",22,7),1)
        self.ajoute_entitee(anneau_1)
        anneau_2 = Anneau_magique_gobelin(Position("Étage 9 : équippement",22,9),1)
        self.ajoute_entitee(anneau_2)
        anneau_3 = Anneau_soin_gobelin(Position("Étage 9 : équippement",20,7),1)
        self.ajoute_entitee(anneau_3)
        anneau_4 = Anneau_soin_gobelin(Position("Étage 9 : équippement",20,9),1)
        self.ajoute_entitee(anneau_4)
        anneau_5 = Anneau_vitesse_gobelin(Position("Étage 9 : équippement",18,7),1)
        self.ajoute_entitee(anneau_5)
        anneau_6 = Anneau_vitesse_gobelin(Position("Étage 9 : équippement",18,9),1)
        self.ajoute_entitee(anneau_6)
        anneau_7 = Anneau_terrestre_gobelin(Position("Étage 9 : équippement",16,7),1)
        self.ajoute_entitee(anneau_7)
        anneau_8 = Sceau_roi_gobelin(Position("Étage 9 : équippement",15,9),1)
        self.ajoute_entitee(anneau_8)
        #/!\ Rajouter un cadavre de roi gobelin et une couronne
        #Dans la cinquième, un haume :
        haume = Haume_de_gobelin(Position("Étage 9 : équippement",25,1),1)
        self.ajoute_entitee(haume)
        #Dans la sixième, une épée :
        epee = Epee_de_gobelin(Position("Étage 9 : équippement",39,0),1)
        self.ajoute_entitee(epee)
        gobel1 = Sentinelle_gobelin(self,Position("Étage 9 : équippement",15,0),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,Position("Étage 9 : équippement",15,6),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Guerrier_gobelin(self,Position("Étage 9 : équippement",17,2),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,Position("Étage 9 : équippement",17,6),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,Position("Étage 9 : équippement",19,4),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,Position("Étage 9 : équippement",20,1),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,Position("Étage 9 : équippement",17,3),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,Position("Étage 9 : équippement",18,6),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,Position("Étage 9 : équippement",21,3),1)
        self.ajoute_entitee(gobel9)
        gobel10 = Shaman_gobelin(self,Position("Étage 9 : équippement",26,9),1)
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_equippement"]=Esprit_simple("gobelins_equippement",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,gobel10.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns9 = [Pattern(Position("Étage 9 : équippement",0,0),Decalage(7,4),[Cote(Decalage(5,3),BAS)],["Porte_première_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",3,5),Decalage(4,5),[Cote(Decalage(2,0),HAUT)],["Porte_deuxième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",11,2),Decalage(6,4),[Cote(Decalage(0,2),GAUCHE)],["Porte_troisième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",15,7),Decalage(10,3),[Cote(Decalage(8,0),HAUT)],["Porte_quatrième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",28,0),Decalage(0,10),[Cote(Decalage(0,0),GAUCHE),Cote(Decalage(0,1),GAUCHE),Cote(Decalage(0,2),GAUCHE),Cote(Decalage(0,3),GAUCHE),Cote(Decalage(0,4),GAUCHE)],[],False),
                    Pattern(Position("Étage 9 : équippement",23,1),Decalage(8,4),[Cote(Decalage(3,0),HAUT)],["Porte_cinquième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",36,0),Decalage(4,4),[Cote(Decalage(1,3),BAS)],["Porte_sixième_armurerie_9"]),
                    ]
        self.labs["Étage 9 : équippement"]=Labyrinthe("Étage 9 : équippement",Decalage(40,10),Position("Étage 9 : équippement",0,0),paterns9,1,1,TERRE,0.1)
        self[Position("Étage 9 : équippement",5,4),HAUT].effets[1].ferme = False
        self[Position("Étage 9 : équippement",5,3),BAS].effets[1].ferme = False
        self.construit_escalier(Cote(Position("Étage 8 : magie",13,0),HAUT),Cote(Position("Étage 9 : équippement",1,9),BAS)) #/!\ Rajouter les ennemis !

        #On crée le dixième étage
        gobel1 = Sentinelle_gobelin(self,Position("Étage 10 : Boss",5,5),1)
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,Position("Étage 10 : Boss",5,13),1)
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,Position("Étage 10 : Boss",7,9),1)
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,Position("Étage 10 : Boss",5,0),1)
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,Position("Étage 10 : Boss",5,18),1)
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,Position("Étage 10 : Boss",8,6),1)
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,Position("Étage 10 : Boss",8,12),1)
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,Position("Étage 10 : Boss",9,0),1)
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,Position("Étage 10 : Boss",9,18),1)
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,Position("Étage 10 : Boss",9,9),1)
        self.ajoute_entitee(boss)
        self.esprits["gobelins_boss"]=Esprit_simple("gobelins_boss",[gobel1.ID,gobel2.ID,gobel3.ID,gobel4.ID,gobel5.ID,gobel6.ID,gobel7.ID,gobel8.ID,gobel9.ID,boss.ID],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns10 = [Pattern(Position("Étage 10 : Boss",10,0),Decalage(0,19),[Cote(Decalage(0,9),GAUCHE)],["Porte_boss_10"]),
                     Pattern(Position("Étage 10 : Boss",20,0),Decalage(3,19),[Cote(Decalage(0,9),GAUCHE)],["Porte_dérobée_10"])]
        self.labs["Étage 10 : Boss"]=Labyrinthe("Étage 10 : Boss",Decalage(23,19),Position("Étage 10 : Boss",0,0),paterns10,1,1,TERRE,1)
        self.construit_escalier(Cote(Position("Étage 9 : équippement",39,4),DROITE),Cote(Position("Étage 10 : Boss",0,9),GAUCHE)) #/!\ Rajouter les ennemis !

        #On lance la cinématique :
        #TODO: À rajouter
        #Et on active le lab du joueur
        self.joueur = Heros(self,Position("Étage 1 : couloir",13,0))
        self.ajoute_entitee(self.joueur)
        self.esprits["heros"] = Esprit_humain(2,self)
        self.active_lab(self.joueur.position.lab)

    def duel(self,esprit1: Esprit,esprit2: Esprit,niveau_1=1,niveau_2=1,tailles_lab=(20,20),vide=True,vue=False,screen=None):
        """Fonction qui crée les conditions d'un duel."""

        if vue : # On peut avoir des spectateurs, mais pas forcément
            self.ajoute_entitee(Heros(("arène",tailles_lab[0]//2,tailles_lab[1]//2),screen))
        # Première étape : créer l'arène
        self.labs["arène"]=Labyrinthe("arène",Decalage(tailles_lab[0],tailles_lab[1]),("arène",0,0),[Pattern(("arène",0,0),tailles_lab[0],tailles_lab[1],[],[],vide)])
        # Deuxième étape : créer les opposants
        self.esprits["1"] = esprit1("1",niveau_1,self,("arène",0,0))
        self.esprits["2"] = esprit2("2",niveau_2,self,("arène",tailles_lab[0]-1,0))
        # Troisième étape : créer un conflit
        self.esprits["1"].antagonise("2")
        self.esprits["2"].antagonise("1")
        # Quatrième étape : admirer
        self.active_lab("arène")

    def cree_agissants(self,classe,niveau: int,position: Position,largeur: int,hauteur: int,nombre: int):
        poss = [position+i*DROITE+j*BAS for i in range(largeur) for j in range(hauteur)] #Les positions possibles
        #Rajouter une  vérification pour ne prendre que les cases vides ?
        agissants = []
        for i in range(nombre):
            if poss != []:
                j = random.randrange(len(poss))
                pos = poss.pop(j) #On choisit aléatoirement la position de l'agissant et on ne veut pas la réutiliser
                agissant = classe(self,pos,niveau)
                self.ajoute_entitee(agissant)
                agissants.append(agissant.ID)
        return agissants

    def toogle_pause(self):
        self.pause = not(self.pause)

    def set_phase(self,phase: int):
        if phase not in self.phases : #On ne veut pas avoir deux fois la même phase !
            self.phases.append(phase) #La dernière phase est toujours la phase active !
        self.phase = phase # /!\ Rajouter des conditions ici ! Certaines phases ne peuvent pas être interrompues par d'autres
        if self.phase == TOUR:
            pygame.key.set_repeat()
        else:
            pygame.key.set_repeat(400,200)

    def unset_phase(self,phase: int):
        if phase in self.phases :
            self.phases.remove(phase)
        self.phase = self.phases[-1]
        if self.phase == TOUR:
            pygame.key.set_repeat()
        else:
            pygame.key.set_repeat(400,200)

    def set_barriere_classe(self,position: Position,direction: Direction,classe):
        self.active_lab(position.lab) #Pourquoi est-ce qu'on a besoin de ça déjà ? (Je ne discute pas le fait que ça soit nécessaire, j'aimerais juste avoir commenté la raison à l'époque.)
        mur = [position,direction]
        mur.brise()
        mur.effets.append(Barriere_classe(classe))
        mur_opp = mur.get_mur_oppose()
        if mur_opp != None:
            mur_opp.brise()
            mur_opp.effets.append(Barriere_classe(classe))
        self.desactive_lab(position.lab)

    def active_lab(self,key: str): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour activer un nouveau labyrinthe. En entrée, la clé du labyrinthe à activer.
           Un étage, en règle générale, est "inactif", c'est à dire que ses occupants ne bougent pas. Il devient "actif" quand une entitée y entre, pour 5 tours si c'est une entitée basique, et jusqu'à 5 tours après son départ si c'est une entitée supérieure (joueur, dev, kumoko, etc.).
           Lorsque le labyrinthe est "activé", sa clé (qui l'indexe dans le dictionnaire des labs et se retrouve dans la coordonées de position verticale de ses occupants) est ajoutée aux labs_courants. On cherche parmis les entitées celles qui se trouvent dans ce lab et on rajoute leur identifiant aux entitées courantes.
           Dans la version définitive, cette fonction sera appelée à la fin de la chute pour passer le joueur dans le niveau 1."""
        #On active le lab :
        self.labs[key].active(self) #On lui donne le controleur pour qu'il puisse l'appeler au besoin.
        #On cherche ses occupants :
        for ke in self.entitees :
            entitee = self[ke]
            position = entitee.get_position()
            if position != None: #Il y a des entitees dans les inventaires
                if position.lab == key : #La position commence par la coordonnée verticale.
                    self.entitees_courantes.add(ke)
                    entitee.active(self)
        if not key in self.labs_courants:
            self.labs_courants.append(key)

    def desactive_lab(self,key: str): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour désactiver un labyrinthe actif. En entrée, la clé du labyrinthe à désactiver.
           Tout labyrinthe se désactive après 5 tours d'absence d'entitée supérieure (joueur, dev, kumoko, etc.).
           Le lab actif possédant le controleur en attribut, il appelle cette fonction lui-même quand son compteur interne tombe à 0."""
        #On desactive les occupants du lab :
        for ke in self.entitees : #Normalement on a déjà vérifié qu'il n'y a pas d'entitée supérieure...
            entitee = self[ke]
            position = entitee.get_position()
            if position != None: #Il y a des entitees dans les inventaires
                if position.lab == key : #La position commence par la coordonnée verticale.
                    self.entitees_courantes.discard(ke)
                    entitee.desactive()
        if key in self.labs_courants:
            self.labs_courants.remove(key)

    def move(self,position: Position,entitee: Entitee): #Non utilisé dans la version de mi-juillet
        """Fonction appelée quand une entitée change de labyrinthe. En entrée, la position cible et l'entitée avant son déplacement.
           Si le labyrinthe de départ n'a plus d'entitée supérieure, on va devoir préparer sa désactivation. Si le labyrinthe d'arrivée n'avait pas d'entitée supérieure, il va falloir l'activer."""
        ancien_lab = entitee.position.lab
        nouveau_lab = position.lab
        if isinstance(entitee,Entitee_superieure): #Si on a une entitée supérieure :
            if not(nouveau_lab in self.labs_courants) : #On active si nécessaire
                self.active_lab(nouveau_lab)
            elif self.labs[nouveau_lab].temps_restant != -1: #On maintient activé jusqu'à nouvel ordre si nécessaire (sinon, c'est qu'il y a déjà une entitée supérieure dans le labyrinthe, on a rien à faire)
                self.labs[nouveau_lab].temps_restant = -1
        else : #Si on a une entitée normale :
            if not(nouveau_lab in self.labs_courants) :
                self.active_lab(nouveau_lab) #On active si nécessaire...
                self.labs[nouveau_lab].quitte() #...Mais on quittera bientôt
            elif self.labs[nouveau_lab].temps_restant != -1:
                self.labs[nouveau_lab].quitte() #On quittera un peu plus tard si nécessaire (sinon, c'est qu'il y a une entitée supérieure dans le labyrinthe, on a rien à faire)
            
        entitee.set_position(position) #L'entitée se déplace, elle et toutes ses possessions (notamment l'inventaire !)
        #On cherche une éventuelle entitée supérieure dans l'ancien labyrinthe :
        sup = False
        for key_entitee in self.entitees_courantes :
            position = self[key_entitee].get_position()
            if position != None:
                if (position.lab == ancien_lab) and isinstance(self[key_entitee],Entitee_superieure):
                    sup = True
        if not(sup): #On n'a pas d'entitee supérieure dans le labyrinthe
            self.labs[ancien_lab].quitte() #On lance le décompte de 5 tours (faire + de 5 tours ?)

    def set_teleport(self,cote_dep: Cote,cote_arr: Cote,portail: Teleport=None):
        self[cote_dep.emplacement].repoussante = True
        self[cote_arr.emplacement].repoussante = True
        self[cote_dep].detruit()
        self[cote_arr].detruit()
        self[cote_dep].set_cible(cote_arr.emplacement,True,portail)
        self[cote_arr].set_cible(cote_dep.emplacement,True,portail)

    def construit_escalier(self,cote_dep: Cote,cote_arr: Cote,escalier: Escalier=None):
        self[cote_dep.emplacement].repoussante = True
        self[cote_arr.emplacement].repoussante = True
        self[cote_dep].detruit()
        self[cote_arr].detruit()
        self[cote_dep].set_escalier(cote_arr.emplacement,HAUT,escalier) #Par convention, la première case est en bas
        self[cote_arr].set_escalier(cote_dep.emplacement,BAS,escalier)

    def get_trajet(self,pos:Position,direction:Direction):
        return self[pos,direction].get_trajet()

    def make_vue(self,agissant: Agissant):
        labyrinthe = self[agissant.position.lab]
        vue = labyrinthe.get_vue(agissant)
        for occupant in self.entitees_courantes:
            pos = self[occupant].position
            try:
                if pos in vue:
                    if vue[pos].clarte > 0:
                        vue[pos].entitees.append(occupant)
            except:
                print(pos)
                print(vue)
                print(occupant)
                print(agissant)
        agissant.vue = vue

    # Les fonctions qui suivent sont utilisées dans diverses situations pour trouver les entitées situées sur une case
    # On distingue plusieurs cas :
    # Déplacement (on cherche les entitées qui occupent l'espace, auxquelles on ne peut pas superposer d'autres entitées semblables)
    # Combat (on cherche les entitées qui peuvent subir des dégats, qui ont des PVs)
    # Ramassage (on cherche les entitées qui peuvent être stockées dans un inventaire)
    # Effets divers (auras, soins, etc. (comme pour le combat))
    # Interactions (dialogues, éléments de décors)
    # Pour les déplacements, on veut donc les Non_superposable
    # Pour les combats, les agissants
    # Pour les ramassages, les items (y compris les agissants morts (les cadavres))
    # Pour les interactions, les interactifs (à créer)
    # Pour les effets divers, le plus souvent les agissants, parfois les movibles (à créer)

    def est_item(self,ID_entitee:int):
        return issubclass(self[ID_entitee].get_classe(),Item)

    def est_agissant(self,ID_entitee:int):
        return issubclass(self[ID_entitee].get_classe(),Agissant)

    def trouve_classe(self,position:Position,classe:Type):
        entitees:List[int] = []
        for entitee in self.entitees.values():
            if entitee.position == position and issubclass(entitee.get_classe(),classe):
                entitees.append(entitee.ID)
        return entitees

    def trouve_items(self,position:Position):
        return self.trouve_classe(position,Item)

    def trouve_non_superposables(self,position:Position):
        return self.trouve_classe(position,Non_superposable)

    def trouve_interactifs(self,position:Position):
        return self.trouve_classe(position,Interactif)

    def trouve_mobiles(self,position:Position):
        return self.trouve_classe(position,Mobile)

    def trouve_agissants(self,position:Position):
        return self.trouve_classe(position,Agissant)

    def trouve_occupants(self,position:Position):
        occupants = []
        for ID_entitee in self.entitees:
            if self[ID_entitee].position == position:
                occupants.append(ID_entitee)
        return occupants

    def trouve_classe_courants(self,position:Position,classe):
        entitees:List[int] = []
        for ID_entitee in self.entitees_courantes:
            entitee = self[ID_entitee]
            if entitee.position == position and issubclass(entitee.get_classe(),classe):
                entitees.append(ID_entitee)
        return entitees

    def trouve_items_courants(self,position:Position):
        return self.trouve_classe_courants(position,Item)

    def trouve_non_superposables_courants(self,position:Position):
        return self.trouve_classe_courants(position,Non_superposable)

    def trouve_interactifs_courants(self,position:Position):
        return self.trouve_classe_courants(position,Interactif)

    def trouve_mobiles_courants(self,position:Position):
        return self.trouve_classe_courants(position,Mobile)

    def trouve_agissants_courants(self,position:Position):
        return self.trouve_classe_courants(position,Agissant)

    def trouve_occupants_courants(self,position:Position):
        occupants:List[int] = []
        for entitee in self.entitees_courantes:
            if self[entitee].position == position:
                occupants.append(entitee)
        return occupants

    def fait_agir(self,agissant:Agissant):
        agissant.set_statut("passif")
        if isinstance(agissant, PJ) and agissant is self.joueur:
            agissant.nouvel_ordre = False
        type_skill = agissant.skill_courant
        skill:Skill_intrasec|None = trouve_skill(agissant.classe_principale,type_skill)
        if skill is None :
            print("On ne peut pas utiliser un skill que l'on n'a pas... et on ne devrait pas pouvoir le choisir d'ailleurs : "+str(type_skill))
        else :



            if isinstance(skill, Skill_analyse): #À améliorer ! /!\
                mallus,niveau,cible = skill.utilise()
                self.lance_analyse(mallus,niveau,cible)



            elif isinstance(skill, Skill_vol):
                possesseur,item = self.selectionne_item_vol()
                latence,reussite = skill.utilise(possesseur.priorite,agissant.priorite)
                agissant.add_latence(latence)
                if reussite :
                    possesseur.inventaire.supprime_item(item)
                    agissant.inventaire.ramasse_item(item)
                    if isinstance(agissant,Heros):
                        affichage = agissant.affichage
                        affichage.message(f"Tu as volé avec succès un {item} à {possesseur} !")
                else :
                    possesseur.persecuteurs.append(agissant.ID)
                #refaire les autres vols sur le même modèle /!\



            elif isinstance(skill, Skill_ramasse):
                items = self.trouve_items_courants(agissant.get_position())
                latence = 1
                for ID_item in items:
                    item = self[ID_item]
                    latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
                    latence += latence_item
                    if reussite:
                        agissant.inventaire.ramasse_item(ID_item)
                agissant.add_latence(latence)



            elif isinstance(skill, Skill_ramasse_light):
                items = self.trouve_items_courants(agissant.get_position())
                latence = 1
                for ID_item in items:
                    item = self[ID_item]
                    if isinstance(item,ITEMS_LIGHTS):
                        latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
                        latence += latence_item
                        if reussite:
                            agissant.inventaire.ramasse_item(ID_item)
                agissant.add_latence(latence)



            elif isinstance(skill, Skill_stomp):
                #Une attaque qui se fait sans arme.
                force,affinite,direction,ID = agissant.get_stats_attaque(TERRE)
                latence,taux,portee = skill.utilise()

                degats = force*taux*affinite
                attaque = Attaque(ID,degats,TERRE,"contact",portee)

                agissant.add_latence(latence)
                agissant.effets.append(attaque)



            elif isinstance(skill, Skill_attaque):
                #Une attaque qui se fait avec une arme.
                arme = agissant.get_arme()
                if arme == None:
                    if isinstance(agissant,Heros):
                        affichage = agissant.affichage
                        affichage.message("Tu n'as pas d'arme ?") #Sans arme, on devrait utiliser le stomp.
                        affichage.message("Essaye le stomp !") # !! À modifier pour indiquer la touche courante du stomp, si elle existe !!!
                else:
                    arme = self[arme]
                    element,tranchant,portee = arme.get_stats_attaque()
                    force,affinite,direction,ID = agissant.get_stats_attaque(element)
                    latence,taux = skill.utilise()

                    taux_manipulation = 1
                    manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
                    if manipulation != None :
                        taux_manipulation = manipulation.utilise_attaque()

                    if isinstance(arme,Epee) :
                        if manipulation == None :
                            manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_epee)
                            if manipulation != None :
                                taux_manipulation = manipulation.utilise()

                        forme = "Sd_S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes

                    elif isinstance(arme,Lance) :
                        if manipulation == None :
                            manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_lance)
                            if manipulation != None :
                                taux_manipulation = manipulation.utilise()

                        forme = "R__S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes
                    else :
                        print("Quelle est cette arme ? " + agissant.arme)

                    degats = force*affinite*tranchant*taux*taux_manipulation
                    attaque = Attaque(ID,degats,element,"contact",portee,forme,direction)

                    agissant.add_latence(latence)
                    agissant.effets.append(attaque)



            elif type_skill == Skill_blocage :
                #Pour être protégé par le bouclier pendant les tours suivants.
                bouclier = agissant.get_bouclier()
                if bouclier == None:
                    if isinstance(agissant,Heros):
                        affichage = agissant.affichage
                        affichage.message("Tu n'as pas de bouclier !") #Sans bouclier, on devrait se mettre à couvert.
                        affichage.message("Tu devrais esquiver, plutôt.")
                else:
                    latence,taux_skill = skill.utilise()

                    taux_manipulation = 1
                    duree = 3
                    manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
                    if manipulation != None :
                        taux_manipulation,duree = manipulation.utilise()
                    else :
                        manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_bouclier)
                        if manipulation != None :
                            taux_manipulation,duree = manipulation.utilise()

                    taux = taux_skill * taux_manipulation

                    effet = Protection_general(duree,bouclier) #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres effets

                    for effet_prec in agissant.effets :
                        if isinstance(effet_prec,Protection_general):
                            agissant.effets.remove(effet_prec) #On ne peut pas avoir deux protections à la fois !

                    agissant.add_latence(latence)
                    agissant.effets.append(effet)
                    effet.execute(agissant) #On passe l'effet en phase "en cours"
                    bouclier.taux_defense["protection"] = taux



            elif issubclass(type_skill,Skills_projectiles) :
                projectile = agissant.get_item_lancer()

                if projectile != None :
                    if isinstance(projectile,int): #Un agissant bien élevé manipule le moins d'objets possible, et leur préfère leurs ID
                        projectile = self[projectile]
                    latence,hauteur,vitesse = skill.utilise()
                    agissant.add_latence(latence*projectile.poids)
                    projectile.position = agissant.get_position()
                    projectile.hauteur = hauteur*agissant.force/projectile.poids
                    projectile.taux_vitesse["lancementv"]=vitesse
                    projectile.direction = agissant.dir_regard
                    projectile.lanceur = agissant.ID
                    self.entitees_courantes.add(projectile.ID)
                    if projectile.controleur == None:
                        projectile.active(self)
                else :
                    if isinstance(agissant,Heros):
                        affichage = agissant.affichage
                        affichage.message("J'ai dû mal comprendre...")
                        affichage.message("Tu veux lancer un item que tu n'as pas ?")



            elif type_skill in [Skill_deplacement,Skill_course,Skanda,Lesser_Skanda]:
                latence,niveau = skill.utilise()
                direction = agissant.get_direction()
                position = agissant.get_position()
                agissant.add_latence(latence)

                lab = self[position.lab]
                lab.veut_passer(agissant,direction)



            elif type_skill == Skill_soin :
                latence,soin,portee = skill.utilise()
                agissant.add_latence(latence)
                self.soigne(agissant,agissant.get_position(),portee,soin)



            elif type_skill == Skill_regeneration_MP :
                latence,regen,portee = skill.utilise()
                agissant.add_latence(latence)
                self.regenere(agissant,agissant.get_position(),portee,regen)



            elif type_skill in [Skill_reanimation,Skill_reanimation_renforcee] :
                cadavre = self[agissant.cible]
                latence,taux,sup = skill.utilise()
                agissant.add_latence(latence)
                if cadavre.priorite + sup < agissant.priorite :
                    esprit = self.get_esprit(agissant)
                    cadavre.effets.append(Reanimation(taux,esprit))
                else:
                    cadavre.effets.append(Reanimation(taux,self.get_esprit(cadavre)))


            elif issubclass(type_skill,Skills_magiques) :
                nom_magie = agissant.magie_courante
                latence,magie = skill.utilise(nom_magie)
                if magie != None:
                    cout = magie.cout_pm
                    if agissant.peut_payer(cout) :
                        agissant.effets.append(magie)
                        reussite = True
                        #if isinstance(agissant,Heros):
                        #    malchance = trouve_skill(agissant.classe_principale,Skill_malchanceux)
                        #else:
                        #    malchance = None
                        #if malchance != None:
                        #    reussite = malchance.utilise("cast_magic")
                        if isinstance(magie,Magie_cible) :
                            self.select_cible(magie,agissant)
                        if isinstance(magie,Magie_dirigee) :
                            self.select_direction(magie,agissant)
                        if isinstance(magie,Magie_cout) :
                            self.select_cout(magie,agissant)
                        agissant.paye(magie.cout_pm)
                        agissant.add_latence(latence)
                        if not reussite :
                            magie.miss_fire(agissant)
                else:
                    print("On ne peut pas utiliser une magie que l'on a pas !")
                    print(nom_magie,agissant)



            elif type_skill in [Divine_Thread_Weaving,Lesser_Divine_Thread_Weaving] :
                action = agissant.action
                latence,item = skill.utilise(action)
                agissant.add_latence(latence)
                self.items.append(item)



            elif type_skill in [Scythe,Lesser_Scythe] :
                perce,element,taux = skill.utilise()
                attaque = Attaque(agissant.ID,agissant.force*taux,element,"contact",1,"R__T_Pb",agissant.direction,"piercing",perce)
                self.tentative_attaque(attaque)



            elif isinstance(skill, Egg_Laying):
                latence, oeuf = skill.utilise()
                agissant.add_latence(latence)
                if oeuf != None :
                    self.ajoute_entitee(oeuf)



            elif isinstance(skill, Skill_merge):
                ID_cible = agissant.cible_merge
                latence = skill.utilise()
                if ID_cible != None:
                    esprit = self[ID_cible].esprit
                    self.get_esprit(agissant.esprit).merge(esprit) #/!\ Syntaxe probablement fausse et foireuse, à vérifier
                agissant.add_latence(latence)



            elif isinstance(skill, Skill_absorb):
                items = self.trouve_items_courants(agissant.get_position())
                latence = 1
                for ID_item in items:
                    item = self[ID_item]
                    latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
                    latence += latence_item
                    if reussite:
                        agissant.inventaire.ramasse_item(ID_item)
                        if item.get_classe() == Cadavre:
                            pass #/!\ Comment le skill est choisi ? Au hasard ? Comment différencier le type de slime (copie le skill au niveau 1, copie le skill à son niveau, vole le skill et laisse une copie au niveau 1, prend le skill mais le laisse quand même)
                agissant.add_latence(latence)



            elif isinstance(skill, Skill_divide):
                latence = skill.utilise()
                if agissant.peut_payer(20): #Insérer le cout ici d'une façon ou d'une autre /!\
                    new_slime = type(agissant)(agissant.position,agissant.niveau,True)
                    agissant.paye(20)
                    agissant.subit(20) # /!\ Ne pas utiliser subit() !
                agissant.add_latence(latence)



    def fait_voler(self,item:Item):
        direction = item.get_direction()
        position = item.get_position()
        lab = self[position.lab]
        lab.veut_passer(item,direction)

    def select_cible(self,magie:Magie_cible,agissant:Agissant):
        # if random.random() < agissant.talent :
            magie.cible = agissant.cible_magie
        
    def select_direction(self,magie:Magie_dirigee,agissant:Agissant):
        # if random.random() < agissant.talent :
            magie.direction = agissant.dir_magie

    def select_cout(self,magie:Magie_cout,agissant:Agissant):
        magie.cout_pm = agissant.cout_magie

    def select_cible_parchemin(self,magie:Magie_cible,agissant:Agissant):
        # if random.random() < agissant.talent :
            magie.cible = agissant.cible_magie_parchemin
        
    def select_direction_parchemin(self,magie:Magie_dirigee,agissant:Agissant):
        # if random.random() < agissant.talent :
            magie.direction = agissant.dir_magie_parchemin

    def select_cout_parchemin(self,magie:Magie_cout,agissant:Agissant):
        magie.cout_pm = agissant.cout_magie_parchemin

    def get_cibles_potentielles_agissants(self,magie:Magie_cible,joueur:Agissant):
        cibles_potentielles = []
        for case in self.esprits["heros"].vue:
            for ID_entitee in case.cibles:
                entitee = self[ID_entitee]
                if issubclass(entitee.get_classe(),Agissant):
                    cibles_potentielles.append(entitee)
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
            cibles = []
            for agissant in cibles_potentielles:
                if agissant.position in poss:
                    cibles.append(agissant.ID)
        else:
            cibles = []
            for agissant in cibles_potentielles:
                cibles.append(agissant.ID)
        return cibles

    def get_cibles_potentielles_items(self,magie:Magie_cible,joueur:Agissant):
        cibles_potentielles = []
        for case in self.esprits["heros"].vue:
            for ID_entitee in case.cibles:
                entitee = self[ID_entitee]
                if issubclass(entitee.get_classe(),Item):
                    cibles_potentielles.append(entitee)
                else:
                    cibles_potentielles += entitee.inventaire.get_items() #/!\ Rajouter une condition d'observation ! Mais ne pas l'appliquer à soi-même !
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
            cibles = []
            for item in cibles_potentielles:
                if item.position in poss:
                    cibles.append(item.ID)
        else:
            cibles = []
            for item in cibles_potentielles:
                cibles.append(item.ID)
        return cibles

    def get_cibles_potentielles_cases(self,magie:Magie_cible,joueur:Agissant):
        cibles_potentielles = []
        for case in self.esprits["heros"].vue:
            cibles_potentielles.append(case[0])
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
            cibles = []
            for pos in cibles_potentielles:
                if pos in poss:
                    cibles.append(pos)
        else:
            cibles = cibles_potentielles
        return cibles

    def get_esprit(self,nom:str):
        if nom != None:
            return self.esprits[nom]
        else:
            return None

    def get_nom_esprit(self,corp:Agissant):
        return self[corp].get_esprit()

    def get_entitee(self,ID):
        return self.entitees[ID]

    def get_especes(self,ID:int) -> List[str]:
        entitee = self[ID]
        if issubclass(entitee.get_classe(),Agissant):
            return entitee.especes
        else:
            return []

    def ajoute_entitees(self,entitees:List[Entitee]):
        for entitee in entitees:
            self.ajoute_entitee(entitee)

    def ajoute_entitee(self,entitee:Entitee):
        self[entitee.ID]=entitee
        if entitee.position != None:
            if entitee.position.lab in self.labs_courants:
                entitee.active(self)
                self.entitees_courantes.add(entitee.ID)

    def get_entitees_etage(self,num_lab:str):
        entitees:List[Entitee] = []
        for ID_entitee in self.entitees_courantes:
            entitee = self[ID_entitee]
            if entitee.position != None:
                if entitee.position.lab==num_lab:
                    entitees.append(ID_entitee)
        return entitees

    def get_agissants_items_labs_esprits(self) -> Tuple[List[Agissant],List[Item],List[Labyrinthe],List[Esprit]]:
        self.nb_tours+=1
        agissants:List[Agissant] = []
        items:List[Item] = []
        labs:List[Labyrinthe] = []
        esprits:List[Esprit] = []
        noms_esprits = []
        for ID_entitee in self.entitees_courantes :
            entitee = self[ID_entitee]
            if isinstance(entitee,Agissant):
                if entitee is self.joueur:
                    agissants.insert(0,entitee)
                    esprit = entitee.get_esprit()
                    if esprit != None:
                        if not esprit in noms_esprits:
                            noms_esprits.append(esprit)
                elif entitee.etat == "vivant":
                    agissants.append(entitee)
                    esprit = entitee.get_esprit()
                    if esprit != None:
                        if not esprit in noms_esprits:
                            noms_esprits.append(esprit)
                else:
                    items.append(entitee)
            elif isinstance(entitee,Item):
                if entitee.etat == "intact":
                    items.append(entitee)
                elif entitee.etat == "suspens":
                    items.append(entitee)
                else:
                    self.entitees_courantes.remove(ID_entitee)
                    self.entitees.pop(ID_entitee)
                    entitee.desactive()
        for niveau_lab in self.labs_courants:
            labs.append(self.labs[niveau_lab])
        for nom in noms_esprits:
            esprits.append(self.get_esprit(nom))
        return agissants, items, labs, esprits

    def get_touches(self,responsable:int,position:Position,portee=1,propagation="CD_S___",direction:Direction=None,bloquable = True): #Trouve les agissants affectés par une attaque
        attaquant:Agissant = self[responsable]
        nom_esprit = attaquant.esprit
        intouchables = []
        if nom_esprit != None:
            esprit = self.get_esprit(nom_esprit)
            intouchables = esprit.get_corps()
        else:
            intouchables = [responsable]
        labyrinthe = self.labs[position.lab]
        victimes_possibles = self.get_entitees_etage(position.lab)
        obstacles = []
        for i in range(len(victimes_possibles)-1,-1,-1) :
            victime_possible = victimes_possibles[i]
            if victime_possible in intouchables :
                victimes_possibles.remove(victime_possible)
            elif bloquable:
                victime = self[victime_possible]
                if issubclass(victime.get_classe(),Agissant):
                    position_v = victime.get_position()
                    obstacles.append(position_v)
        labyrinthe.attaque(position,portee,propagation,direction,obstacles)
        victimes:List[Agissant] = []
        for victime_possible in victimes_possibles :
            victime = self[victime_possible]
            if issubclass(victime.get_classe(),Agissant):
                position_v = victime.get_position()
                if labyrinthe[position_v].clarte > 0 :
                    victimes.append(victime)
        return victimes

    def get_touches_pos(self,responsable:int,position:Position,portee=1,propagation = "C__S___",direction=None): #La même, mais pour les effets positifs comme les soins
        bienfaiteur:Agissant = self[responsable]
        nom_esprit = bienfaiteur.esprit
        intouchables = []
        if nom_esprit != None:
            esprit = self.get_esprit(nom_esprit)
            intouchables = esprit.get_ennemis()
        else:
            intouchables = []
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,[])
        beneficiaires_possibles = self.get_entitees_etage(position.lab)
        beneficiaires:List[Agissant] = []
        for i in range(len(beneficiaires_possibles)-1,-1,-1) :
            beneficiaire_possible = beneficiaires_possibles[i]
            if beneficiaire_possible in intouchables :
                beneficiaires_possibles.remove(beneficiaires_possibles)
            else:
                beneficiaire = self[beneficiaire_possible]
                if issubclass(beneficiaire.get_classe(),Agissant):
                    position_b = beneficiaire.get_position()
                    if labyrinthe[position_b].clarte > 0 :
                        beneficiaires.append(beneficiaire)
        return beneficiaires

    def get_cadavres_touches(self,position:Position,portee=1,propagation = "C__S___",direction = None): #La même, mais pour les effets sur les cadavres comme la réanimation
        cadavres:List[Agissant] = []
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,[])
        cadavres_possibles = self.get_entitees_etage(position.lab)
        for i in range(len(cadavres_possibles)-1,-1,-1) :
            cadavre_possible = self[cadavres_possibles[i]]
            if cadavre_possible.get_classe() == Cadavre:
                position_c = cadavre_possible.get_position()
                if labyrinthe[position_c].clarte > 0 :
                    cadavres.append(cadavre_possible)
        return cadavres

    def get_cases_touches(self,position:Position,portee=1,propagation = "C__S___",direction = None,traverse="tout",responsable=0): #La même, mais pour les effets sur les cases
        cases = []
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,[])
        for pos in labyrinthe :
            case = labyrinthe[pos]
            if case.clarte > 0 :
                cases.append(case)
        return cases

    def get_pos_touches(self,position:Position,portee:int,propagation = "C__S___",direction = None,traverse="tout",responsable=0): #La même, mais pour les positions
        #On décide des obstacles:
        pos_obstacles = []
        if traverse == "rien":
            obstacles = self.get_entitees_etage(position.lab)
            for ID_obstacle in obstacles:
                obstacle = self[ID_obstacle]
                if issubclass(obstacle.get_classe(),Non_superposable):
                    pos_obstacles.append(obstacle.get_position())
        elif traverse == "alliés":
            obstacles_possibles = self.get_entitees_etage(position.lab)
            nom_esprit = self[responsable].esprit
            if nom_esprit != None:
                for ID_obstacle in obstacles_possibles:
                    obstacle = self[ID_obstacle]
                    if issubclass(obstacle.get_classe(),Non_superposable):
                        if issubclass(obstacle.get_classe(),Agissant):
                            if obstacle.esprit != nom_esprit:
                                pos_obstacles.append(obstacle.get_position())
                        else:
                            pos_obstacles.append(obstacle.get_position())
        elif traverse == "ennemis":
            obstacles_possibles = self.get_entitees_etage(position.lab)
            nom_esprit = self[responsable].esprit
            if nom_esprit != None:
                for ID_obstacle in obstacles_possibles:
                    obstacle = self[ID_obstacle]
                    if issubclass(obstacle.get_classe(),Non_superposable):
                        if issubclass(obstacle.get_classe(),Agissant):
                            if obstacle.esprit == nom_esprit:
                                pos_obstacles.append(obstacle.get_position())
                        else:
                            pos_obstacles.append(obstacle.get_position())
        elif traverse == "tout":
            pass
        else:
            print("Quelle est cette traversée ?")
        poss:List[Position] = []
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,pos_obstacles)
        for position in labyrinthe:
            if labyrinthe[position].clarte > 0:
                poss.append(position)
        return poss

    # def clear(self):
    #     for ID_entitee in self.entitees:
    #         self[ID_entitee].clear()
