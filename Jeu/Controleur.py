from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Optional, Set, Any

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Labyrinthe.Labyrinthe import Labyrinthe
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Decalage import Decalage
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Labyrinthe.Structure_spatiale.Cote import Cote_position,Cote_decalage
    from Jeu.Labyrinthe.Pattern import Pattern
    from Jeu.Labyrinthe.Case import Case
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Agissant.PNJ.PNJs import PJ
    from Jeu.Entitee.Item.Item import Item
    from Jeu.Entitee.Entitee import Mobile
    from Jeu.Entitee.Decors.Decor import Decors
    from Jeu.Esprit.Esprit import Esprit

# Pas de classe parente

# Valeurs par défaut des paramètres
from Jeu.Effet.Effets_mouvement.Deplacements import Teleport, Escalier
from Jeu.Entitee.Agissant.Agissant import NoOne

# Constantes
from Jeu.Constantes import *
from Jeu.Systeme.Constantes_decors.Decors import *
from Jeu.Systeme.Constantes_items.Items import *
from Jeu.Systeme.Constantes_magies.Magies import *
from Jeu.Systeme.Constantes_projectiles.Projectiles import *
from Jeu.Systeme.Constantes_skills.Skills import *
from Jeu.Systeme.Constantes_stats import *

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
    def __init__(self,parametres:Optional[Dict[str,Any]] = None):
        #print("Initialisation du controleur")
        self.labs:Dict[str,Labyrinthe] = {} #Un dictionnaire avec tous les labyrinthes, indéxés par leur identifiant dans les positions.
        self.agissants:Dict[int,Agissant] = {}
        self.decors:Dict[int,Decors] = {}
        self.items:Dict[int,Item] = {}
        self.esprits:Dict[str,Esprit] = {}
        self.labs_courants:Set[str] = set()
        self.agissants_courants:Set[Agissant] = set()
        self.decors_courants:Set[Decors] = set()
        self.items_courants:Set[Item] = set()
        self.esprits_courants:Set[str] = set()
        self.joueur:PJ
        self.pause = False
        self.nb_tours = 0
        self.phase:int = TOUR
        self.phases = [self.phase]
        if parametres is None:
            self.tour_par_seconde = 0
        else:
            self.tour_par_seconde = parametres["tours_par_seconde"]

    def case_from_tuple(self,tuple:Tuple[str,int,int]):
        return self.labs[tuple[0]].case_from_tuple(tuple[1:])
    
    def mur_from_tuple(self,tuple:Tuple[str,int,int,Direction]):
        return self.labs[tuple[0]].mur_from_tuple(tuple[1:])
    
    def case_from_position(self,position:Position):
        return self.labs[position.lab].case_from_position(position)

    def mur_from_cote(self,cote:Cote_position):
        return self.labs[cote.emplacement.lab].mur_from_cote(cote)

    # def jeu(self):

    #     self.esprits["heros"] = Esprit_humain(2,self)

    #     autre = Alchimiste(self,Position("Étage 1 : test",1,0))
    #     self.ajoute_entitee(autre)
    #     self.esprits["alchimiste"] = Esprit_humain(autre,self)

    #     chaudron = Chaudron_gobelin(self,Position("Étage 1 : test",1,3))
    #     self.ajoute_entitee(chaudron)

    #     peaux:List[Entitee] = [Peau_gobelin(self,Position("Étage 1 : test",1,2)),Peau_gobelin(self,Position("Étage 1 : test",1,4))]
    #     self.ajoute_entitees(peaux)

    #     gobel1 = Chef_gobelin(self,Position("Étage 1 : test",11,15),1)
    #     self.ajoute_entitee(gobel1)
    #     #self.esprits["gobel1"]=Esprit_simple("gobel1",[gobel1],["humain"],self)

    #     gobel2 = Sentinelle_gobelin(self,Position("Étage 1 : test",2,6),1)
    #     self.ajoute_entitee(gobel2)
    #     self.esprits["gobel2"]=Esprit_simple("gobel2",[gobel1,gobel2],[],self)

    #     self.ajoute_entitee(Parchemin_vierge(Position("Étage 1 : test",1,5)))

    #     paterns1 = [Pattern(Position("Étage 1 : test",0,0),Decalage(20,20),[])]
    #     self.labs["Étage 1 : test"]=Labyrinthe(self,"Étage 1 : test",Decalage(20,20),Position("Étage 1 : test",0,0),paterns1,1,1,TERRE,1)

    #     self.joueur.position = Position("Étage 1 : test",0,0)
    #     self.active_lab("Étage 1 : test")

    # def experience5(self):
    #     #Une expérience sur les paramètres optimaux des esprits



    #     #L'équipe 1 est très mal disposée, avec les DPS/Tank à l'arrière et les shamans à l'avant
    #     gobel1 = Sentinelle_gobelin(self,("Labo",1,2),1)
    #     self.ajoute_entitee(gobel1)
    #     gobel2 = Sentinelle_gobelin(self,("Labo",3,0),1)
    #     self.ajoute_entitee(gobel2)
    #     gobel3 = Gobelin(self,("Labo",4,4),1)
    #     self.ajoute_entitee(gobel3)
    #     gobel4 = Guerrier_gobelin(self,("Labo",2,1),1)
    #     self.ajoute_entitee(gobel4)
    #     gobel5 = Guerrier_gobelin(self,("Labo",0,1),1)
    #     self.ajoute_entitee(gobel5)
    #     gobel6 = Mage_gobelin(self,("Labo",3,6),1)
    #     self.ajoute_entitee(gobel6)
    #     gobel7 = Mage_gobelin(self,("Labo",8,2),1)
    #     self.ajoute_entitee(gobel7)
    #     gobel8 = Shaman_gobelin(self,("Labo",9,7),1)
    #     self.ajoute_entitee(gobel8)
    #     gobel9 = Shaman_gobelin(self,("Labo",9,8),1)
    #     self.ajoute_entitee(gobel9)
    #     boss = Chef_gobelin(self,("Labo",0,0),1)
    #     self.ajoute_entitee(boss)
    #     self.esprits["Equipe 1"]=Esprit_simple("Equipe 1",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9,boss],["gobelin"],self)


    #     #L'équipe 2 est disposée de façon optimale, avec les DPS/Tank à l'avant et les shamans à l'arrière
    #     gobel1 = Sentinelle_gobelin(self,("Labo",10,10),1)
    #     self.ajoute_entitee(gobel1)
    #     gobel2 = Sentinelle_gobelin(self,("Labo",10,11),1)
    #     self.ajoute_entitee(gobel2)
    #     gobel3 = Gobelin(self,("Labo",12,12),1)
    #     self.ajoute_entitee(gobel3)
    #     gobel4 = Guerrier_gobelin(self,("Labo",11,10),1)
    #     self.ajoute_entitee(gobel4)
    #     gobel5 = Guerrier_gobelin(self,("Labo",11,11),1)
    #     self.ajoute_entitee(gobel5)
    #     gobel6 = Mage_gobelin(self,("Labo",13,13),1)
    #     self.ajoute_entitee(gobel6)
    #     gobel7 = Mage_gobelin(self,("Labo",14,14),1)
    #     self.ajoute_entitee(gobel7)
    #     gobel8 = Shaman_gobelin(self,("Labo",19,19),1)
    #     self.ajoute_entitee(gobel8)
    #     gobel9 = Shaman_gobelin(self,("Labo",19,18),1)
    #     self.ajoute_entitee(gobel9)
    #     boss = Chef_gobelin(self,("Labo",12,11),1)
    #     self.ajoute_entitee(boss)
    #     self.esprits["Equipe 2"]=Esprit_simple("Equipe 2",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9,boss],["gobelin"],self)



    #     #Le labyrinthe est partiellement fermé
    #     self.labs["Labo"]=Labyrinthe(self,"Labo",Decalage(20,20),Position("Labo",0,0),[],1,1,TERRE,0.5)
    #     self.active_lab("Labo")

    # def check_exp5(self):
    #     mort1 = 0
    #     for ID in self.esprits["Equipe 1"].corps:
    #         if self[ID].etat == "mort":
    #             mort1 += 1

    #     mort2 = 0
    #     for ID in self.esprits["Equipe 2"].corps:
    #         if self[ID].etat == "mort":
    #             mort2 += 1

    #     if (mort1 == 10 and mort2 == 10) or self.nb_tours >= 200:
    #         return [mort1,mort2,self.nb_tours]
    #     if mort1 == 10:
    #         return [mort1,mort2,self.nb_tours]
    #     if mort2 == 10:
    #         return [mort1,mort2,self.nb_tours]
    #     return False

    def tuto(self):

        #On crée le premier étage et son occupant :
        receptionniste = Receptionniste(self,Position("Étage 1 : couloir",14,0))
        self.ajoute_entitee(receptionniste)
        self.esprits["receptionniste"] = Esprit_humain(receptionniste,self)
        paterns1 = [Pattern(Position("Étage 1 : couloir",9,0),Decalage(0,3),[Cote_decalage(Decalage(0,1),GAUCHE)],["clé_couloir"])]
        self.labs["Étage 1 : couloir"]=Labyrinthe(self,"Étage 1 : couloir",Decalage(19,3),Position("Étage 1 : couloir",0,0),paterns1,1,1,TERRE,1)

        #On crée le deuxième étage et son occupant :
        paume = Paume(self,Position("Étage 2 : labyrinthe",1,0))
        self.ajoute_entitee(paume)
        self.esprits["paume"] = Esprit_humain(paume,self)
        paterns2 = [Pattern(Position("Étage 2 : labyrinthe",0,0),Decalage(5,5),[Cote_decalage(Decalage(4,0),DROITE),Cote_decalage(Decalage(4,1),DROITE),Cote_decalage(Decalage(4,2),DROITE),Cote_decalage(Decalage(4,3),DROITE),Cote_decalage(Decalage(4,4),DROITE)]),
                    Pattern(Position("Étage 2 : labyrinthe",5,5),Decalage(5,5),[Cote_decalage(Decalage(0,0),GAUCHE)],["Porte_centre_2"])]
        self.labs["Étage 2 : labyrinthe"]=Labyrinthe(self,"Étage 2 : labyrinthe",Decalage(15,15),Position("Étage 2 : labyrinthe",0,0),paterns2,1,1,TERRE,0.2)
        self.construit_escalier(Cote_position(Position("Étage 1 : couloir",18,1),DROITE),Cote_position(Position("Étage 2 : labyrinthe",0,0),GAUCHE))

        #On crée le troisième étage et son occupante :
        peureuse = Peureuse(self,Position("Étage 3 : combat",8,8))
        self.ajoute_entitee(peureuse)
        self.esprits["peureuse"] = Esprit_humain(peureuse,self)
        cle1 = Cle(self,["Porte_avant_prison_5"],Position("Étage 3 : combat",12,13))
        self.ajoute_entitee(cle1)
        peureuse.inventaire.ajoute(cle1)
        gobel1 = Premier_monstre(self,1,Position("Étage 3 : combat",3,8))
        self.ajoute_entitee(gobel1)
        self.esprits["gobelins_combat"]=Esprit_simple("gobelins_combat",[gobel1],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns3 = [Pattern(Position("Étage 3 : combat",4,4),Decalage(7,7),[Cote_decalage(Decalage(0,3),GAUCHE),Cote_decalage(Decalage(0,4),GAUCHE),Cote_decalage(Decalage(0,5),GAUCHE),Cote_decalage(Decalage(3,0),HAUT),Cote_decalage(Decalage(4,0),HAUT),Cote_decalage(Decalage(5,0),HAUT),Cote_decalage(Decalage(0,0),HAUT),Cote_decalage(Decalage(1,0),HAUT),Cote_decalage(Decalage(0,0),GAUCHE),Cote_decalage(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 3 : combat",3,3),Decalage(3,3),[Cote_decalage(Decalage(0,0),HAUT),Cote_decalage(Decalage(2,2),BAS),Cote_decalage(Decalage(0,0),GAUCHE),Cote_decalage(Decalage(2,2),DROITE)]),
                    Pattern(Position("Étage 3 : combat",7,2),Decalage(3,3),[Cote_decalage(Decalage(1,0),HAUT),Cote_decalage(Decalage(1,2),BAS)]),
                    Pattern(Position("Étage 3 : combat",8,8),Decalage(3,3),[Cote_decalage(Decalage(0,0),HAUT),Cote_decalage(Decalage(0,0),GAUCHE)]),
                    Pattern(Position("Étage 3 : combat",0,3),Decalage(1,0)),
                    Pattern(Position("Étage 3 : combat",1,3),Decalage(0,3)),
                    Pattern(Position("Étage 3 : combat",1,6),Decalage(2,0)),
                    Pattern(Position("Étage 3 : combat",2,7),Decalage(3,3),[Cote_decalage(Decalage(0,1),GAUCHE),Cote_decalage(Decalage(2,1),DROITE)])]
        self.labs["Étage 3 : combat"]=Labyrinthe(self,"Étage 3 : combat",Decalage(11,11),Position("Étage 3 : combat",0,0),paterns3,1,1,TERRE,0.2)
        self.construit_escalier(Cote_position(Position("Étage 2 : labyrinthe",1,5),HAUT),Cote_position(Position("Étage 3 : combat",10,10),BAS))

        #On crée le quatrième étage et ses occupants :
        codeur = Codeur(self,Position("Étage 4 : monstres",15,1))
        self.ajoute_entitee(codeur)
        self.esprits["codeur"] = Esprit_humain(codeur,self)
        gobel1 = Troisieme_monstre(self,1,Position("Étage 4 : monstres",15,8)) #Une sentinelle garde les abords
        self.ajoute_entitee(gobel1)
        gobel2 = Deuxieme_monstre(self,1,Position("Étage 4 : monstres",10,4)) #Ainsi qu'un mage,
        self.ajoute_entitee(gobel2)
        self.esprits["gobelins_monstres"]=Esprit_simple("gobelins_monstres",[gobel1,gobel2],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns4 = [Pattern(Position("Étage 4 : monstres",4,0),Decalage(10,2),[Cote_decalage(Decalage(0,1),GAUCHE),Cote_decalage(Decalage(9,1),DROITE)],[],False),
                    Pattern(Position("Étage 4 : monstres",7,6),Decalage(10,0),[Cote_decalage(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 4 : monstres",14,0),Decalage(3,3),[Cote_decalage(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 4 : monstres",0,7),Decalage(4,3),[Cote_decalage(Decalage(3,1),DROITE)],["Porte_coin_4"])]
        self.labs["Étage 4 : monstres"]=Labyrinthe(self,"Étage 4 : monstres",Decalage(17,10),Position("Étage 4 : monstres",0,0),paterns4,1,1,TERRE,0.1,[1,5,1,5])
        self.construit_escalier(Cote_position(Position("Étage 3 : combat",0,3),GAUCHE),Cote_position(Position("Étage 4 : monstres",16,5),DROITE))

        #On crée le cinquième étage et ses occupants :
        encombrant = Encombrant(self,Position("Étage 5 : portes",2,3))
        self.ajoute_entitee(encombrant)
        self.esprits["encombrant"] = Esprit_humain(encombrant,self)
        cle1 = Cle(self,["Porte_sortie_encombrant_5"],Position("Étage 5 : portes",2,3))
        self.ajoute_entitee(cle1)
        encombrant.inventaire.ajoute(cle1)
        passepartout1 = Cle(self,["Porte_première_cellule_5","Porte_double_cellule_première_5","Porte_grande_cellule_5","Porte_cellule_biscornue_5","Porte_entree_encombrant_5"],Position("Étage 5 : portes",5,5))
        self.ajoute_entitee(passepartout1)
        cle2 = Cle(self,["Porte_couloir_5"],Position("Étage 5 : portes",1,9))
        self.ajoute_entitee(cle2)
        cle3 = Cle(self,["Porte_fin_couloir_5"],Position("Étage 5 : portes",1,2))
        self.ajoute_entitee(cle3)
        cle5 = Cle(self,["Porte_armurerie_6"],Position("Étage 5 : portes",3,6))
        self.ajoute_entitee(cle5)
        cle6 = Cle(self,["Porte_quatrième_armurerie_9"],Position("Étage 5 : portes",0,6))
        self.ajoute_entitee(cle6)
        cle7 = Cle(self,["Porte_annexe_droite_7"],Position("Étage 5 : portes",0,12))
        self.ajoute_entitee(cle7)
        cle8 = Cle(self,["Porte_troisième_armurerie_9"],Position("Étage 5 : portes",0,6))
        self.ajoute_entitee(cle8)
        cle9 = Cle(self,["Porte_anti_anti_chambre_8"],Position("Étage 5 : portes",9,13))
        self.ajoute_entitee(cle9)
        gobel1 = Sentinelle_gobelin(self,1,Position("Étage 5 : portes",6,10)) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,1,Position("Étage 5 : portes",5,5)) #Une sentinelle veille sur la prison
        self.ajoute_entitee(gobel2)
        gobel2.inventaire.ajoute(passepartout1)
        gobel3 = Guerrier_gobelin(self,1,Position("Étage 5 : portes",8,1)) #Un renégat mis à l'isolement pour le mater, ou un piège diabolique dirigé contre le joueur ?
        self.ajoute_entitee(gobel3)
        slime = Slime(self,1,Position("Étage 5 : portes",8,7)) #Un slime ! Est-ce que les gobelins ont pris soin de l'affaiblir ?
        self.ajoute_entitee(slime)
        ombriul = Ombriul(self,1,Position("Étage 5 : portes",5,7)) #Un prisonnier de guerre
        self.ajoute_entitee(ombriul)
        #Rajouter quelques cadavres pour le nécromancien
        self.esprits["gobelins_portes"]=Esprit_simple("gobelins_portes",[gobel1,gobel2,gobel3],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        self.esprits["ombriul_captif"]=Esprit_simple("ombriul_captif",[ombriul],["humain"],self)
        esprit_slime = Esprit_slime(slime,self)
        self.esprits[esprit_slime.nom]=esprit_slime #Les esprits des slimes sont presque aussi compliqués que ceux des humains, les ruptures en moins.
        paterns5 = [Pattern(Position("Étage 5 : portes",7,11),Decalage(3,3),[Cote_decalage(Decalage(0,1),GAUCHE)]),
                    Pattern(Position("Étage 5 : portes",0,5),Decalage(5,3),[Cote_decalage(Decalage(1,2),BAS)]),
                    Pattern(Position("Étage 5 : portes",0,1),Decalage(5,4),[Cote_decalage(Decalage(0,0),HAUT),Cote_decalage(Decalage(4,2),DROITE)],["Porte_sortie_encombrant_5","Porte_entree_encombrant_5"]),
                    Pattern(Position("Étage 5 : portes",0,8),Decalage(3,3),[Cote_decalage(Decalage(1,0),HAUT),Cote_decalage(Decalage(2,1),DROITE),Cote_decalage(Decalage(2,2),BAS)],["Porte_première_cellule_5","Porte_couloir_5"]),
                    Pattern(Position("Étage 5 : portes",0,11),Decalage(4,3),[Cote_decalage(Decalage(2,0),HAUT)],["Porte_avant_prison_5"]),
                    Pattern(Position("Étage 5 : portes",4,11),Decalage(3,3),[Cote_decalage(Decalage(1,0),HAUT),Cote_decalage(Decalage(2,1),DROITE)],["Porte_double_cellule_première_5","Porte_double_cellule_deuxième_5"]),
                    Pattern(Position("Étage 5 : portes",6,0),Decalage(4,5),[Cote_decalage(Decalage(2,4),BAS)],["Porte_grande_cellule_5"]),
                    Pattern(Position("Étage 5 : portes",5,6),Decalage(4,4),[Cote_decalage(Decalage(3,2),DROITE)],["Porte_cellule_biscornue_5"]), #/!\ À corriger /!\
                    Pattern(Position("Étage 5 : portes",3,7),Decalage(2,2),[Cote_decalage(Decalage(1,1),BAS),Cote_decalage(Decalage(1,1),DROITE)]),
                    Pattern(Position("Étage 5 : portes",4,8),Decalage(2,2),[Cote_decalage(Decalage(0,0),HAUT),Cote_decalage(Decalage(0,0),GAUCHE)]),
                    Pattern(Position("Étage 5 : portes",5,6),Decalage(2,2),[Cote_decalage(Decalage(0,1),GAUCHE)])]
        self.labs["Étage 5 : portes"]=Labyrinthe(self,"Étage 5 : portes",Decalage(10,14),Position("Étage 5 : portes",0,0),paterns5,1,1,TERRE,1)
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",6,5),BAS)).cree_porte("Porte_cellule_plus_biscornue_5")
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",6,6),HAUT)).cree_porte("Porte_cellule_plus_biscornue_5")
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",4,0),DROITE)).cree_porte("Porte_fin_couloir_5")
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",5,0),GAUCHE)).cree_porte("Porte_fin_couloir_5")
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",2,11),HAUT)).cree_porte("Porte_avant_prison_5",Premiere_porte)
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",4,3),DROITE)).get_porte().auto = True
        self.mur_from_cote(Cote_position(Position("Étage 5 : portes",5,3),GAUCHE)).get_porte().auto = True
        self.construit_escalier(Cote_position(Position("Étage 4 : monstres",16,7),DROITE),Cote_position(Position("Étage 5 : portes",0,13),GAUCHE),Premiere_marche)

        #On crée le sixième étage et son occupant :
        #Nouvelle version :
        alchimiste = Alchimiste(self,Position("Étage 6 : potions",13,1))
        self.ajoute_entitee(alchimiste)
        self.esprits["alchimiste"] = Esprit_humain(alchimiste,self)

        chaudrons_6:Set[Entitee] = set()
        chaudrons_6.update({
            Chaudron_gobelin(self,Position("Étage 6 : potions",12,4)),
            Chaudron_gobelin(self,Position("Étage 6 : potions",14,8))
        })
        
        self.ajoute_entitees(chaudrons_6)

        cle_gobel2 = Cle(self,["Porte_inutile_potion"],Position("Étage 6 : potions",13,10))
        cle_gobel3 = Cle(self,["Deuxième_porte_potions"],Position("Étage 6 : potions",4,4))

        cles_6:Set[Entitee] = {
            Cle(self,["Porte_cuisine"],Position("Étage 6 : potions",4,1)), #(0)
            Cle(self,["Première_porte_potions"],Position("Étage 6 : potions",11,6)), #(1)
            cle_gobel2, #(2)
            cle_gobel3, #(3)
            Cle(self,["Troisième_porte_potions"],Position("Étage 6 : potions",3,9)), #(4)
            Cle(self,["Porte_double_cellule_deuxième_5"],Position("Étage 6 : potions",0,11)),
            Cle(self,["Porte_salle_commune_7"],Position("Étage 6 : potions",11,10))
        }
        self.ajoute_entitees(cles_6)

        consomables_6:Set[Entitee] = set()
        consomables_6.update({
            Parchemin_protection(self,Position("Étage 6 : potions",2,13)),
            Potion_force(self,Position("Étage 6 : potions",1,13))
        })
        self.ajoute_entitees(consomables_6)

        ingredients_6:Set[Entitee] = set()
        ingredients_6.update({
            Peau_gobelin(self,Position("Étage 6 : potions",12,6)),
            Dent_gobelin(self,Position("Étage 6 : potions",14,8)),
            Pierre_solide(self,Position("Étage 6 : potions",9,1)),
            Hypokute(self,Position("Étage 6 : potions",6,7))
        })
        self.ajoute_entitees(ingredients_6)

        gobel1 = Gobelin(self,1,Position("Étage 6 : potions",11,6))
        self.ajoute_entitee(gobel1)
        gobel2 = Mage_gobelin(self,1,Position("Étage 6 : potions",13,10))
        self.ajoute_entitee(gobel2)
        gobel2.inventaire.ajoute(cle_gobel2)
        gobel3 = Sentinelle_gobelin(self,1,Position("Étage 6 : potions",4,4))
        self.ajoute_entitee(gobel3)
        gobel3.inventaire.ajoute(cle_gobel3)
        gobel4 = Mage_gobelin(self,1,Position("Étage 6 : potions",6,6))
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,1,Position("Étage 6 : potions",4,10))
        self.ajoute_entitee(gobel5)
        gobel6 = Guerrier_gobelin(self,1,Position("Étage 6 : potions",12,4))
        self.ajoute_entitee(gobel6)
        gobel7 = Guerrier_gobelin(self,1,Position("Étage 6 : potions",14,4))
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,1,Position("Étage 6 : potions",13,7))
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,1,Position("Étage 6 : potions",10,9))
        self.ajoute_entitee(gobel9)
        self.esprits["gobelins_potions"]=Esprit_simple("gobelins_potions",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)

        paterns6 = [Pattern(Position("Étage 6 : potions",9,3),Decalage(6,8),[Cote_decalage(Decalage(0,0),GAUCHE),Cote_decalage(Decalage(0,1),GAUCHE),Cote_decalage(Decalage(0,2),GAUCHE),Cote_decalage(Decalage(0,3),GAUCHE),Cote_decalage(Decalage(3,0),HAUT),Cote_decalage(Decalage(4,0),HAUT),Cote_decalage(Decalage(5,0),HAUT),Cote_decalage(Decalage(0,7),GAUCHE),Cote_decalage(Decalage(0,7),BAS),Cote_decalage(Decalage(3,7),BAS),Cote_decalage(Decalage(4,7),BAS),Cote_decalage(Decalage(5,7),BAS)]), #La cuisine, avec le shaman et les derniers gobelins (0)
                    Pattern(Position("Étage 6 : potions",6,0),Decalage(3,2),[]), #(5)
                    Pattern(Position("Étage 6 : potions",3,0),Decalage(3,2),[Cote_decalage(Decalage(0,1),GAUCHE)]), #(12) /!\ Il y a un problème ici ?
                    Pattern(Position("Étage 6 : potions",0,3),Decalage(2,3),[Cote_decalage(Decalage(1,0),HAUT)]), #(10)
                    Pattern(Position("Étage 6 : potions",0,0),Decalage(3,3),[Cote_decalage(Decalage(1,2),BAS),Cote_decalage(Decalage(2,1),DROITE),Cote_decalage(Decalage(2,2),DROITE),Cote_decalage(Decalage(2,2),BAS)],["Deuxième_porte_potions","Troisième_porte_potions"]), #(11)
                    Pattern(Position("Étage 6 : potions",3,7),Decalage(3,2),[Cote_decalage(Decalage(0,1),GAUCHE)]), #(4) /!\ QUOI ?!?
                    Pattern(Position("Étage 6 : potions",0,6),Decalage(3,3),[Cote_decalage(Decalage(2,1),DROITE),Cote_decalage(Decalage(2,0),DROITE),Cote_decalage(Decalage(2,0),HAUT)],["Première_porte_potions"]), #(3)
                    Pattern(Position("Étage 6 : potions",0,9),Decalage(3,3),[Cote_decalage(Decalage(2,1),DROITE)]), #(8)
                    Pattern(Position("Étage 6 : potions",3,9),Decalage(3,3),[Cote_decalage(Decalage(0,1),GAUCHE)],["Porte_inutile_potion"]), #(9)
                    Pattern(Position("Étage 6 : potions",2,2),Decalage(5,5),[]), #(7)
                    Pattern(Position("Étage 6 : potions",12,9),Decalage(3,3),[]), #(6)
                    Pattern(Position("Étage 6 : potions",11,0),Decalage(4,4),[Cote_decalage(Decalage(2,3),BAS),Cote_decalage(Decalage(0,3),GAUCHE),Cote_decalage(Decalage(0,3),BAS)],["Porte_cuisine"]), #(1)
                    Pattern(Position("Étage 6 : potions",8,3),Decalage(4,4),[]), #(2)
                    Pattern(Position("Étage 6 : potions",0,12),Decalage(5,3),[Cote_decalage(Decalage(4,1),DROITE)],["Porte_armurerie_6"])]
        self.labs["Étage 6 : potions"]=Labyrinthe(self,"Étage 6 : potions",Decalage(15,15),Position("Étage 6 : potions",14,14),paterns6,1,1,TERRE,0.2)

        self.set_teleport(Cote_position(Position("Étage 6 : potions",11,2),GAUCHE),Cote_position(Position("Étage 6 : potions",8,3),HAUT),Premier_portail) # 1,2
        self.set_teleport(Cote_position(Position("Étage 6 : potions",13,0),HAUT),Cote_position(Position("Étage 6 : potions",1,6),DROITE),Premier_portail) # 1,3
        self.set_teleport(Cote_position(Position("Étage 6 : potions",3,8),BAS),Cote_position(Position("Étage 6 : potions",6,0),GAUCHE)) # 4,5
        self.set_teleport(Cote_position(Position("Étage 6 : potions",4,8),BAS),Cote_position(Position("Étage 6 : potions",13,9),HAUT)) # 4,6
        self.set_teleport(Cote_position(Position("Étage 6 : potions",5,8),BAS),Cote_position(Position("Étage 6 : potions",4,11),BAS)) # 4,9
        self.set_teleport(Cote_position(Position("Étage 6 : potions",12,10),GAUCHE),Cote_position(Position("Étage 6 : potions",7,0),HAUT)) # 6,5
        self.set_teleport(Cote_position(Position("Étage 6 : potions",13,11),BAS),Cote_position(Position("Étage 6 : potions",4,2),HAUT)) # 6,7
        self.set_teleport(Cote_position(Position("Étage 6 : potions",2,2),GAUCHE),Cote_position(Position("Étage 6 : potions",6,1),BAS)) # 7,5
        self.set_teleport(Cote_position(Position("Étage 6 : potions",6,5),DROITE),Cote_position(Position("Étage 6 : potions",0,11),BAS)) # 7,8
        self.set_teleport(Cote_position(Position("Étage 6 : potions",2,9),DROITE),Cote_position(Position("Étage 6 : potions",8,1),BAS)) # 8,5
        self.set_teleport(Cote_position(Position("Étage 6 : potions",5,11),BAS),Cote_position(Position("Étage 6 : potions",8,0),DROITE)) # 9,5
        self.set_teleport(Cote_position(Position("Étage 6 : potions",5,10),DROITE),Cote_position(Position("Étage 6 : potions",0,4),GAUCHE)) # 9,10

        self.construit_escalier(Cote_position(Position("Étage 5 : portes",0,0),GAUCHE),Cote_position(Position("Étage 6 : potions",14,0),DROITE))

        #On crée le septième étage et son occupante :
        peste = Peste(self,Position("Étage 7 : meutes",2,0))
        self.ajoute_entitee(peste)
        self.esprits["peste"] = Esprit_humain(peste,self)
        cle1 = Cle(self,["Porte_sixième_armurerie_9"],Position("Étage 7 : meutes",14,6))
        self.ajoute_entitee(cle1)
        gobel1 = Guerrier_gobelin(self,1,Position("Étage 7 : meutes",4,3))
        self.ajoute_entitee(gobel1)
        gobel2 = Guerrier_gobelin(self,1,Position("Étage 7 : meutes",10,3))
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,1,Position("Étage 7 : meutes",6,4))
        self.ajoute_entitee(gobel3)
        gobel4 = Gobelin(self,1,Position("Étage 7 : meutes",4,4))
        self.ajoute_entitee(gobel4)
        gobel5 = Gobelin(self,1,Position("Étage 7 : meutes",10,4))
        self.ajoute_entitee(gobel5)
        gobel6 = Gobelin(self,1,Position("Étage 7 : meutes",9,4))
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,1,Position("Étage 7 : meutes",5,5))
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,1,Position("Étage 7 : meutes",7,5))
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,1,Position("Étage 7 : meutes",4,5))
        self.ajoute_entitee(gobel9)
        gobel10 = Shaman_gobelin(self,1,Position("Étage 7 : meutes",10,5))
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_meutes"]=Esprit_simple("gobelins_meutes",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9,gobel10],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns7 = [Pattern(Position("Étage 7 : meutes",0,0),Decalage(15,2),[Cote_decalage(Decalage(1,1),BAS),Cote_decalage(Decalage(13,1),BAS)]),
                    Pattern(Position("Étage 7 : meutes",0,2),Decalage(4,3),[Cote_decalage(Decalage(1,0),HAUT),Cote_decalage(Decalage(2,2),BAS)],["Porte_annexe_gauche_7"]),
                    Pattern(Position("Étage 7 : meutes",4,2),Decalage(7,4),[Cote_decalage(Decalage(3,0),HAUT)],["Porte_salle_commune_7"]),
                    Pattern(Position("Étage 7 : meutes",11,2),Decalage(4,3),[Cote_decalage(Decalage(2,0),HAUT),Cote_decalage(Decalage(1,2),BAS)],["Porte_annexe_droite_7"])]
        self.labs["Étage 7 : meutes"]=Labyrinthe(self,"Étage 7 : meutes",Decalage(15,10),Position("Étage 7 : meutes",0,9),paterns7,1,1,TERRE,0.3,[1,3,1,3])
        self.construit_escalier(Cote_position(Position("Étage 6 : potions",12,14),BAS),Cote_position(Position("Étage 7 : meutes",7,0),HAUT))

        #On crée le huitième étage et son occupante :
        bombe_atomique = Bombe_atomique(self,Position("Étage 8 : magie",8,7))
        self.ajoute_entitee(bombe_atomique)
        self.esprits["bombe_atomique"] = Esprit_humain(bombe_atomique,self)
        cle1 = Cle(self,["Porte_deuxième_armurerie_9"],Position("Étage 8 : magie",0,7))
        self.ajoute_entitee(cle1)
        cle2 = Cle(self,["Porte_anti_chambre_8"],Position("Étage 8 : magie",12,8))
        self.ajoute_entitee(cle3)
        cle3 = Cle(self,["Porte_annexe_gauche_7"],Position("Étage 8 : magie",3,2))
        self.ajoute_entitee(cle2)
        gobel1 = Mage_gobelin(self,1,Position("Étage 8 : magie",1,1))
        self.ajoute_entitee(gobel1)
        gobel2 = Mage_gobelin(self,1,Position("Étage 8 : magie",1,3))
        self.ajoute_entitee(gobel2)
        gobel3 = Mage_gobelin(self,1,Position("Étage 8 : magie",2,0))
        self.ajoute_entitee(gobel3)
        gobel4 = Mage_gobelin(self,1,Position("Étage 8 : magie",4,3))
        self.ajoute_entitee(gobel4)
        gobel5 = Mage_gobelin(self,1,Position("Étage 8 : magie",5,7))
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,1,Position("Étage 8 : magie",6,2))
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,1,Position("Étage 8 : magie",8,0))
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,1,Position("Étage 8 : magie",9,2))
        self.ajoute_entitee(gobel8)
        gobel9 = Mage_gobelin(self,1,Position("Étage 8 : magie",5,5))
        self.ajoute_entitee(gobel9)
        gobel10 = Mage_gobelin(self,1,Position("Étage 8 : magie",10,9))
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_magie"]=Esprit_simple("gobelins_magie",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9,gobel10],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns8 = [Pattern(Position("Étage 8 : magie",10,0),Decalage(5,4),[Cote_decalage(Decalage(0,1),GAUCHE),Cote_decalage(Decalage(3,3),BAS)]),
                    Pattern(Position("Étage 8 : magie",7,6),Decalage(4,3),[Cote_decalage(Decalage(0,1),GAUCHE),Cote_decalage(Decalage(3,1),DROITE)],["Porte_anti_chambre_8"]),
                    Pattern(Position("Étage 8 : magie",11,4),Decalage(4,6),[Cote_decalage(Decalage(2,0),HAUT),Cote_decalage(Decalage(0,4),GAUCHE)],["Porte_sas_8","Porte_anti_anti_chambre_8"])]
        self.labs["Étage 8 : magie"]=Labyrinthe(self,"Étage 8 : magie",Decalage(15,10),Position("Étage 8 : magie",0,0),paterns8,1,1,TERRE,0.4)
        self.construit_escalier(Cote_position(Position("Étage 7 : meutes",0,9),GAUCHE),Cote_position(Position("Étage 8 : magie",14,7),DROITE)) #/!\ Rajouter un parchemin

        #On crée le neuvième étage et son occupant :
        marchand = Marchand(self,Position("Étage 9 : équippement",6,2))
        self.ajoute_entitee(marchand)
        cle1 = Cle(self,["Porte_première_armurerie_9"],Position("Étage 9 : équippement",2,0))
        self.ajoute_entitee(cle1)
        marchand.inventaire.ajoute(cle1)
        self.esprits["marchand"] = Esprit_humain(marchand,self)
        cle2 = Cle(self,["Porte_cinquième_armurerie_9"],Position("Étage 9 : équippement",38,8))
        self.ajoute_entitee(cle2)
        cle1 = Cle(self,["Porte_sas_8"],Position("Étage 9 : équippement",0,1))
        self.ajoute_entitee(cle1)
        #On crée aussi quelques items :
        #Pas d'item dans l'armurerie où est le marchand, il l'a déjà dévalisée !
        #Dans la deuxième armurerie, une armure :
        armure = Armure_sentinelle_gobelin(self,1,Position("Étage 9 : équippement",5,9))
        self.ajoute_entitee(armure)
        #Dans la troisième, une lance :
        lance = Lance_de_gobelin(self,1,Position("Étage 9 : équippement",16,3))
        self.ajoute_entitee(lance)
        #Dans la quatrième, huit anneaux :
        anneau_1 = Anneau_magique_gobelin(self,1,Position("Étage 9 : équippement",22,7))
        self.ajoute_entitee(anneau_1)
        anneau_2 = Anneau_magique_gobelin(self,1,Position("Étage 9 : équippement",22,9))
        self.ajoute_entitee(anneau_2)
        anneau_3 = Anneau_soin_gobelin(self,1,Position("Étage 9 : équippement",20,7))
        self.ajoute_entitee(anneau_3)
        anneau_4 = Anneau_soin_gobelin(self,1,Position("Étage 9 : équippement",20,9))
        self.ajoute_entitee(anneau_4)
        anneau_5 = Anneau_vitesse_gobelin(self,1,Position("Étage 9 : équippement",18,7))
        self.ajoute_entitee(anneau_5)
        anneau_6 = Anneau_vitesse_gobelin(self,1,Position("Étage 9 : équippement",18,9))
        self.ajoute_entitee(anneau_6)
        anneau_7 = Anneau_terrestre_gobelin(self,1,Position("Étage 9 : équippement",16,7))
        self.ajoute_entitee(anneau_7)
        anneau_8 = Sceau_roi_gobelin(self,1,Position("Étage 9 : équippement",15,9))
        self.ajoute_entitee(anneau_8)
        #/!\ Rajouter un cadavre de roi gobelin et une couronne
        #Dans la cinquième, un haume :
        haume = Haume_de_gobelin(self,1,Position("Étage 9 : équippement",25,1))
        self.ajoute_entitee(haume)
        #Dans la sixième, une épée :
        epee = Epee_de_gobelin(self,1,Position("Étage 9 : équippement",39,0))
        self.ajoute_entitee(epee)
        gobel1 = Sentinelle_gobelin(self,1,Position("Étage 9 : équippement",15,0))
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,1,Position("Étage 9 : équippement",15,6))
        self.ajoute_entitee(gobel2)
        gobel3 = Guerrier_gobelin(self,1,Position("Étage 9 : équippement",17,2))
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,1,Position("Étage 9 : équippement",17,6))
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,1,Position("Étage 9 : équippement",19,4))
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,1,Position("Étage 9 : équippement",20,1))
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,1,Position("Étage 9 : équippement",17,3))
        self.ajoute_entitee(gobel7)
        gobel8 = Mage_gobelin(self,1,Position("Étage 9 : équippement",18,6))
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,1,Position("Étage 9 : équippement",21,3))
        self.ajoute_entitee(gobel9)
        gobel10 = Shaman_gobelin(self,1,Position("Étage 9 : équippement",26,9))
        self.ajoute_entitee(gobel10)
        self.esprits["gobelins_equippement"]=Esprit_simple("gobelins_equippement",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9,gobel10],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns9 = [Pattern(Position("Étage 9 : équippement",0,0),Decalage(7,4),[Cote_decalage(Decalage(5,3),BAS)],["Porte_première_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",3,5),Decalage(4,5),[Cote_decalage(Decalage(2,0),HAUT)],["Porte_deuxième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",11,2),Decalage(6,4),[Cote_decalage(Decalage(0,2),GAUCHE)],["Porte_troisième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",15,7),Decalage(10,3),[Cote_decalage(Decalage(8,0),HAUT)],["Porte_quatrième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",28,0),Decalage(0,10),[Cote_decalage(Decalage(0,0),GAUCHE),Cote_decalage(Decalage(0,1),GAUCHE),Cote_decalage(Decalage(0,2),GAUCHE),Cote_decalage(Decalage(0,3),GAUCHE),Cote_decalage(Decalage(0,4),GAUCHE)],[],False),
                    Pattern(Position("Étage 9 : équippement",23,1),Decalage(8,4),[Cote_decalage(Decalage(3,0),HAUT)],["Porte_cinquième_armurerie_9"]),
                    Pattern(Position("Étage 9 : équippement",36,0),Decalage(4,4),[Cote_decalage(Decalage(1,3),BAS)],["Porte_sixième_armurerie_9"]),
                    ]
        self.labs["Étage 9 : équippement"]=Labyrinthe(self,"Étage 9 : équippement",Decalage(40,10),Position("Étage 9 : équippement",0,0),paterns9,1,1,TERRE,0.1)
        self.mur_from_cote(Cote_position(Position("Étage 9 : équippement",5,4),HAUT)).get_porte().ferme = False
        self.mur_from_cote(Cote_position(Position("Étage 9 : équippement",5,3),BAS)).get_porte().ferme = False
        self.construit_escalier(Cote_position(Position("Étage 8 : magie",13,0),HAUT),Cote_position(Position("Étage 9 : équippement",1,9),BAS)) #/!\ Rajouter les ennemis !

        #On crée le dixième étage
        gobel1 = Sentinelle_gobelin(self,1,Position("Étage 10 : Boss",5,5))
        self.ajoute_entitee(gobel1)
        gobel2 = Sentinelle_gobelin(self,1,Position("Étage 10 : Boss",5,13))
        self.ajoute_entitee(gobel2)
        gobel3 = Gobelin(self,1,Position("Étage 10 : Boss",7,9))
        self.ajoute_entitee(gobel3)
        gobel4 = Guerrier_gobelin(self,1,Position("Étage 10 : Boss",5,0))
        self.ajoute_entitee(gobel4)
        gobel5 = Guerrier_gobelin(self,1,Position("Étage 10 : Boss",5,18))
        self.ajoute_entitee(gobel5)
        gobel6 = Mage_gobelin(self,1,Position("Étage 10 : Boss",8,6))
        self.ajoute_entitee(gobel6)
        gobel7 = Mage_gobelin(self,1,Position("Étage 10 : Boss",8,12))
        self.ajoute_entitee(gobel7)
        gobel8 = Shaman_gobelin(self,1,Position("Étage 10 : Boss",9,0))
        self.ajoute_entitee(gobel8)
        gobel9 = Shaman_gobelin(self,1,Position("Étage 10 : Boss",9,18))
        self.ajoute_entitee(gobel9)
        boss = Chef_gobelin(self,1,Position("Étage 10 : Boss",9,9))
        self.ajoute_entitee(boss)
        self.esprits["gobelins_boss"]=Esprit_simple("gobelins_boss",[gobel1,gobel2,gobel3,gobel4,gobel5,gobel6,gobel7,gobel8,gobel9,boss],["humain"],self) #/!\ Remplacer à l'occasion par un esprit + adéquat (niveau mémoire, etc.)
        paterns10 = [Pattern(Position("Étage 10 : Boss",10,0),Decalage(0,19),[Cote_decalage(Decalage(0,9),GAUCHE)],["Porte_boss_10"]),
                     Pattern(Position("Étage 10 : Boss",20,0),Decalage(3,19),[Cote_decalage(Decalage(0,9),GAUCHE)],["Porte_dérobée_10"])]
        self.labs["Étage 10 : Boss"]=Labyrinthe(self,"Étage 10 : Boss",Decalage(23,19),Position("Étage 10 : Boss",0,0),paterns10,1,1,TERRE,1)
        self.construit_escalier(Cote_position(Position("Étage 9 : équippement",39,4),DROITE),Cote_position(Position("Étage 10 : Boss",0,9),GAUCHE)) #/!\ Rajouter les ennemis !

        #On lance la cinématique :
        #TODO: À rajouter
        #Et on active le lab du joueur
        self.joueur = Heros(self,Position("Étage 1 : couloir",13,0))
        self.joueur.position = Position("Étage 2 : labyrinthe",0,0)
        self.ajoute_entitee(self.joueur)
        self.esprits["heros"] = Esprit_humain(self.joueur,self)
        self.active_lab(self.joueur.position.lab)

    # def duel(self,esprit1: Esprit,esprit2: Esprit,niveau_1=1,niveau_2=1,tailles_lab=(20,20),vide=True,vue=False,screen=None):
    #     """Fonction qui crée les conditions d'un duel."""

    #     if vue : # On peut avoir des spectateurs, mais pas forcément
    #         self.ajoute_entitee(Heros(("arène",tailles_lab[0]//2,tailles_lab[1]//2),screen))
    #     # Première étape : créer l'arène
    #     self.labs["arène"]=Labyrinthe(self,"arène",Decalage(tailles_lab[0],tailles_lab[1]),("arène",0,0),[Pattern(("arène",0,0),tailles_lab[0],tailles_lab[1],[],[],vide)])
    #     # Deuxième étape : créer les opposants
    #     self.esprits["1"] = esprit1("1",niveau_1,self,("arène",0,0))
    #     self.esprits["2"] = esprit2("2",niveau_2,self,("arène",tailles_lab[0]-1,0))
    #     # Troisième étape : créer un conflit
    #     self.esprits["1"].antagonise("2")
    #     self.esprits["2"].antagonise("1")
    #     # Quatrième étape : admirer
    #     self.active_lab("arène")

    # def cree_agissants(self,classe,niveau: int,position: Position,largeur: int,hauteur: int,nombre: int):
    #     poss = [position+i*DROITE+j*BAS for i in range(largeur) for j in range(hauteur)] #Les positions possibles
    #     #Rajouter une  vérification pour ne prendre que les cases vides ?
    #     agissants = []
    #     for i in range(nombre):
    #         if poss:
    #             j = random.randrange(len(poss))
    #             pos = poss.pop(j) #On choisit aléatoirement la position de l'agissant et on ne veut pas la réutiliser
    #             agissant = classe(self,pos,niveau)
    #             self.ajoute_entitee(agissant)
    #             agissants.append(agissant)
    #     return agissants

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
        mur = self.mur_from_cote(Cote_position(position,direction))
        mur.brise()
        mur.effets.append(Barriere_classe(classe))
        mur_opp = mur.get_mur_oppose()
        if mur_opp is not None:
            mur_opp.brise()
            mur_opp.effets.append(Barriere_classe(classe))
        self.desactive_lab(position.lab)

    def active_lab(self,key: str):
        """Fonction appelée pour activer un nouveau labyrinthe. En entrée, la clé du labyrinthe à activer.
           Un étage, en règle générale, est "inactif", c'est à dire que ses occupants ne bougent pas. Il devient "actif" quand une entitée y entre, pour 5 tours si c'est une entitée basique, et jusqu'à 5 tours après son départ si c'est une entitée supérieure (joueur, dev, kumoko, etc.).
           Lorsque le labyrinthe est "activé", sa clé (qui l'indexe dans le dictionnaire des labs et se retrouve dans la coordonées de position verticale de ses occupants) est ajoutée aux labs_courants. On cherche parmis les entitées celles qui se trouvent dans ce lab et on rajoute leur identifiant aux entitées courantes.
           Dans la version définitive, cette fonction sera appelée à la fin de la chute pour passer le joueur dans le niveau 1."""
        #On active le lab :
        for agissant in self.agissants.values():
            position = agissant.get_position()
            if position is not None: #Il y a des agissants morts dans les inventaires
                if position.lab == key : #La position commence par la coordonnée verticale.
                    self.agissants_courants.add(agissant)
        for decor in self.decors.values():
            position = decor.get_position()
            if position is not None:
                if position.lab == key :
                    self.decors_courants.add(decor)
        for item in self.items.values():
            position = item.get_position()
            if position is not None:
                if position.lab == key :
                    self.items_courants.add(item)
        if not key in self.labs_courants:
            self.labs_courants.add(key)

    def desactive_lab(self,key: str): #Non utilisé dans la version de mi-juillet
        """Fonction appelée pour désactiver un labyrinthe actif. En entrée, la clé du labyrinthe à désactiver.
           Tout labyrinthe se désactive après 5 tours d'absence d'entitée supérieure (joueur, dev, kumoko, etc.).
           Le lab actif possédant le controleur en attribut, il appelle cette fonction lui-même quand son compteur interne tombe à 0."""
        #On desactive les occupants du lab :
        for agissant in self.agissants.values():
            position = agissant.get_position()
            if position is not None:
                if position.lab == key :
                    self.agissants_courants.remove(agissant)
        for decor in self.decors.values():
            position = decor.get_position()
            if position is not None:
                if position.lab == key :
                    self.decors_courants.remove(decor)
        for item in self.items.values():
            position = item.get_position()
            if position is not None:
                if position.lab == key :
                    self.items_courants.remove(item)
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
        for entitee_sup_pot in self.agissants_courants|self.items_courants|self.decors_courants :
            position_sup_pot = entitee_sup_pot.get_position()
            if position_sup_pot is not None:
                if (position_sup_pot.lab == ancien_lab) and isinstance(entitee_sup_pot,Entitee_superieure):
                    sup = True
        if not(sup): #On n'a pas d'entitee supérieure dans le labyrinthe
            self.labs[ancien_lab].quitte() #On lance le décompte de 5 tours (faire + de 5 tours ?)

    def set_teleport(self,cote_dep: Cote_position,cote_arr: Cote_position,portail: Type[Teleport]=Teleport):
        if isinstance(cote_dep.emplacement,Decalage) or isinstance(cote_arr.emplacement,Decalage):
            raise ValueError("Le coté d'arrivée ou de départ ne peuvent pas être des décalages !")
        self.case_from_position(cote_dep.emplacement).repoussante = True
        self.case_from_position(cote_arr.emplacement).repoussante = True
        self.mur_from_cote(cote_dep).detruit()
        self.mur_from_cote(cote_arr).detruit()
        self.mur_from_cote(cote_dep).set_cible(cote_arr.emplacement,True,portail)
        self.mur_from_cote(cote_arr).set_cible(cote_dep.emplacement,True,portail)

    def construit_escalier(self,cote_dep: Cote_position,cote_arr: Cote_position,escalier: Type[Escalier]=Escalier):
        if isinstance(cote_dep.emplacement,Decalage) or isinstance(cote_arr.emplacement,Decalage):
            raise ValueError("Le coté d'arrivée ou de départ ne peuvent pas être des décalages ! (Surtout pour un escalier !)")
        self.case_from_position(cote_dep.emplacement).repoussante = True
        self.case_from_position(cote_arr.emplacement).repoussante = True
        self.mur_from_cote(cote_dep).detruit()
        self.mur_from_cote(cote_arr).detruit()
        self.mur_from_cote(cote_dep).set_escalier(cote_arr.emplacement,HAUT,escalier) #Par convention, la première case est en bas
        self.mur_from_cote(cote_arr).set_escalier(cote_dep.emplacement,BAS,escalier)

    def get_trajet(self,pos:Position,direction:Direction):
        return self.case_from_position(pos)[direction].get_trajet()

    def make_vue(self,agissant: Agissant):
        if agissant.position is None:
            raise ValueError("L'agissant n'a pas de position !")
        labyrinthe = self.labs[agissant.position.lab]
        vue = labyrinthe.get_vue(agissant)
        for occupant in self.agissants_courants:
            pos = occupant.position
            if pos is ABSENT:
                raise ValueError("L'entitée courante n'a pas de position !")
            if pos in vue:
                if vue.case_from_position(pos).clarte > 0:
                    vue.case_from_position(pos).agissant = occupant
        for occupant in self.decors_courants:
            pos = occupant.position
            if pos is ABSENT:
                raise ValueError("L'entitée courante n'a pas de position !")
            if pos in vue:
                if vue.case_from_position(pos).clarte > 0:
                    vue.case_from_position(pos).decors = occupant
        for occupant in self.items_courants:
            pos = occupant.position
            if pos is ABSENT:
                raise ValueError("L'entitée courante n'a pas de position !")
            if pos in vue:
                if vue.case_from_position(pos).clarte > 0:
                    vue.case_from_position(pos).items.add(occupant)
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

    def trouve_classe(self,position:Position,classe:Type):
        entitees:Set[classe] = set()
        for entitee in self.agissants_courants|self.items_courants|self.decors_courants:
            if entitee.position == position and isinstance(entitee,classe):
                entitees.add(entitee)
        return entitees

    def trouve_items(self,position:Position) -> Set[Item]:
        return self.trouve_classe(position,Item)

    def trouve_non_superposables(self,position:Position) -> Set[Non_superposable]:
        return self.trouve_classe(position,Non_superposable)

    def trouve_interactifs(self,position:Position) -> Set[Interactif]:
        return self.trouve_classe(position,Interactif)

    def trouve_mobiles(self,position:Position) -> Set[Mobile]:
        return self.trouve_classe(position,Mobile)

    def trouve_agissants(self,position:Position) -> Set[Agissant]:
        return self.trouve_classe(position,Agissant)

    def trouve_occupants(self,position:Position) -> Set[Entitee]:
        occupants:Set[Entitee] = set()
        for entitee in {*self.agissants.values()}|{*self.items.values()}|{*self.decors.values()}:
            if entitee.position == position:
                occupants.add(entitee)
        return occupants

    def trouve_classe_courants(self,position:Position,classe:Type[Entitee]):
        entitees:Set[classe] = set()
        for entitee in self.agissants_courants|self.items_courants|self.decors_courants:
            if entitee.position == position and isinstance(entitee,classe):
                entitees.add(entitee)
        return entitees
    
    def trouve_items_classe_courants(self,position:Position,classe:Type[Item]=Item):
        entitees:Set[classe] = set()
        for entitee in self.items_courants:
            if entitee.position == position and isinstance(entitee,classe):
                entitees.add(entitee)
        return entitees

    def trouve_agissants_classe_courants(self,position:Position,classe:Type[Agissant]=Agissant):
        entitees:Set[classe] = set()
        for entitee in self.agissants_courants:
            if entitee.position == position and isinstance(entitee,classe):
                entitees.add(entitee)
        return entitees
    
    def trouve_decors_classe_courants(self,position:Position,classe:Type[Decors]=Decors):
        entitees:Set[classe] = set()
        for entitee in self.decors_courants:
            if entitee.position == position and isinstance(entitee,classe):
                entitees.add(entitee)
        return entitees

    def trouve_non_superposables_courants(self,position:Position):
        return self.trouve_classe_courants(position,Non_superposable)

    def trouve_interactifs_courants(self,position:Position):
        return self.trouve_classe_courants(position,Interactif)

    def trouve_mobiles_courants(self,position:Position):
        return self.trouve_classe_courants(position,Mobile)

    def trouve_occupants_courants(self,position:Position):
        occupants:Set[Entitee] = set()
        for entitee in self.agissants_courants|self.items_courants|self.decors_courants:
            if entitee.position == position:
                occupants.add(entitee)
        return occupants

    # def fait_agir(self,agissant:Agissant):
    #     agissant.set_statut("passif")
    #     if agissant is self.joueur:
    #         assert isinstance(agissant, PJ)
    #         agissant.nouvel_ordre = False
    #     type_skill = agissant.skill_courant
    #     assert type_skill is not None
    #     skill = trouve_skill(agissant.classe_principale,type_skill)
    #     if skill is None :
    #         print("On ne peut pas utiliser un skill que l'on n'a pas... et on ne devrait pas pouvoir le choisir d'ailleurs : "+str(type_skill))
    #     else :



    #         # if isinstance(skill, Skill_analyse): #À améliorer ! /!\
    #         #     mallus,niveau,cible = skill.utilise()
    #         #     self.lance_analyse(mallus,niveau,cible)



    #         # elif isinstance(skill, Skill_vol):
    #         #     possesseur,item = self.selectionne_item_vol()
    #         #     latence,reussite = skill.utilise(possesseur.priorite,agissant.priorite)
    #         #     agissant.add_latence(latence)
    #         #     if reussite :
    #         #         possesseur.inventaire.supprime_item(item)
    #         #         agissant.inventaire.ramasse_item(item)
    #         #         if isinstance(agissant,Heros):
    #         #             affichage = agissant.affichage
    #         #             affichage.message(f"Tu as volé avec succès un {item} à {possesseur} !")
    #         #     else :
    #         #         possesseur.persecuteurs.append(agissant)
    #         #     #refaire les autres vols sur le même modèle /!\



    #         if isinstance(skill, Skill_ramasse):
    #             pos = agissant.get_position()
    #             assert pos is not None
    #             items = self.trouve_items_courants(pos)
    #             latence = 1
    #             for item in items:
    #                 assert isinstance(item,Item)
    #                 latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
    #                 latence += latence_item
    #                 if reussite:
    #                     agissant.inventaire.ajoute(item)
    #             agissant.add_latence(latence)



    #         elif isinstance(skill, Skill_ramasse_light):
    #             pos = agissant.get_position()
    #             assert pos is not None
    #             items = self.trouve_items_courants(pos)
    #             latence = 1
    #             for item in items:
    #                 if isinstance(item,ITEMS_LIGHTS):
    #                     latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
    #                     latence += latence_item
    #                     if reussite:
    #                         agissant.inventaire.ajoute(item)
    #             agissant.add_latence(latence)



    #         elif isinstance(skill, Skill_stomp):
    #             #Une attaque qui se fait sans arme.
    #             force,affinite,direction,ID = agissant.get_stats_attaque(TERRE)
    #             latence,taux,portee = skill.utilise()

    #             degats = force*taux*affinite
    #             attaque = Attaque(ID,degats,TERRE,"contact",portee)

    #             agissant.add_latence(latence)
    #             agissant.effets.append(attaque)



    #         elif isinstance(skill, Skill_attaque):
    #             #Une attaque qui se fait avec une arme.
    #             arme = agissant.get_arme()
    #             if arme is None:
    #                 print("On ne peut pas utiliser un skill d'attaque sans arme...")
    #             else:
    #                 assert isinstance(arme,Arme)
    #                 element,tranchant,portee = arme.get_stats_attaque()
    #                 force,affinite,direction,ID = agissant.get_stats_attaque(element)
    #                 latence,taux = skill.utilise()

    #                 taux_manipulation = 1
    #                 manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
    #                 if manipulation is not None :
    #                     taux_manipulation = manipulation.utilise_attaque()

    #                 if isinstance(arme,Epee) :
    #                     if manipulation is None :
    #                         manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_epee)
    #                         if manipulation is not None :
    #                             taux_manipulation = manipulation.utilise()

    #                     forme = "Sd_S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes

    #                 elif isinstance(arme,Lance) :
    #                     if manipulation is None :
    #                         manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_lance)
    #                         if manipulation is not None :
    #                             taux_manipulation = manipulation.utilise()

    #                     forme = "R__S___" #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres formes
    #                 else :
    #                     raise ValueError(f"Quelle est cette arme ? {arme}")

    #                 degats = force*affinite*tranchant*taux*taux_manipulation
    #                 attaque = Attaque(ID,degats,element,"contact",portee,forme,direction)

    #                 agissant.add_latence(latence)
    #                 agissant.effets.append(attaque)



    #         elif isinstance(skill, Skill_blocage) :
    #             #Pour être protégé par le bouclier pendant les tours suivants.
    #             bouclier = agissant.get_bouclier()
    #             if bouclier is None:
    #                 print("On ne peut pas utiliser un skill de blocage sans bouclier...")
    #             else:
    #                 assert isinstance(bouclier,Bouclier)
    #                 latence,taux_skill = skill.utilise()

    #                 taux_manipulation = 1
    #                 duree = 3
    #                 manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_arme)
    #                 if manipulation is not None :
    #                     taux_manipulation,duree = manipulation.utilise()
    #                 else :
    #                     manipulation = trouve_skill(agissant.classe_principale,Skill_manipulation_bouclier)
    #                     if manipulation is not None :
    #                         taux_manipulation,duree = manipulation.utilise()

    #                 taux = taux_skill * taux_manipulation

    #                 effet = Protection_general(duree,bouclier) #Dans un monde idéal, les skills de manipulation donnerait accès à d'autres effets

    #                 for effet_prec in agissant.effets :
    #                     if isinstance(effet_prec,Protection_general):
    #                         agissant.effets.remove(effet_prec) #On ne peut pas avoir deux protections à la fois !

    #                 agissant.add_latence(latence)
    #                 agissant.effets.append(effet)
    #                 effet.execute(agissant) #On passe l'effet en phase "en cours"
    #                 bouclier.taux_degats = taux # /!\ Est-ce que c'est vraiment comme ça que ça s'utilise ?



    #         elif isinstance(skill,Skills_projectiles) :
    #             projectile = agissant.get_item_lancer()

    #             if projectile is not None :
    #                 if isinstance(projectile,int): #Un agissant bien élevé manipule le moins d'objets possible, et leur préfère leurs ID
    #                     projectile = self.items[projectile]
    #                 assert isinstance(projectile,Projectile)
    #                 latence,hauteur,vitesse = skill.utilise()
    #                 agissant.add_latence(latence*projectile.poids)
    #                 projectile.position = agissant.get_position()
    #                 projectile.hauteur = hauteur*agissant.force/projectile.poids
    #                 projectile.taux_vitesse["lancementv"]=vitesse
    #                 projectile.direction = agissant.dir_regard
    #                 projectile.lanceur = agissant
    #                 self.items_courants.add(projectile)
    #             else :
    #                 if isinstance(agissant,Heros):
    #                     print("J'ai dû mal comprendre...")
    #                     print("Tu veux lancer un item que tu n'as pas !?")



    #         elif isinstance(skill,Skill_deplacement) :
    #             latence,niveau = skill.utilise()
    #             direction = agissant.get_direction()
    #             position = agissant.get_position()
    #             agissant.add_latence(latence)

    #             lab = self.labs[position.lab]
    #             lab.veut_passer(agissant,direction)



    #         # elif isinstance(skill,Skill_soin) :
    #         #     latence,soin,portee = skill.utilise()
    #         #     agissant.add_latence(latence)
    #         #     position = agissant.get_position()
                
    #         #     assert position is not None
    #         #     poss = self.
    #         #     for pos in poss:
    #         #         self.case_from_position(pos).effets.append(Soin_case(soin,agissant))



    #         # elif isinstance(skill,Skill_regeneration_MP) :
    #         #     latence,regen,portee = skill.utilise()
    #         #     agissant.add_latence(latence)
    #         #     position = agissant.get_position()

    #         #     assert position is not None
    #         #     poss = self.
    #         #     for pos in poss:
    #         #         self.case_from_position(pos).effets.append(Re



    #         # elif isinstance(skill,Skill_reanimation) :
    #         #     cadavre = self[agissant.cible]
    #         #     latence,taux,sup = skill.utilise()
    #         #     agissant.add_latence(latence)
    #         #     if cadavre.priorite + sup < agissant.priorite :
    #         #         esprit = self.get_esprit(agissant)
    #         #         cadavre.effets.append(Reanimation(taux,esprit))
    #         #     else:
    #         #         cadavre.effets.append(Reanimation(taux,self.get_esprit(cadavre)))


    #         elif isinstance(skill,Skills_magiques) :
    #             magie = agissant.magie_courante
    #             assert magie is not None
    #             latence,magie = skill.utilise(magie.nom)
    #             if magie is not None:
    #                 cout = magie.cout_pm
    #                 if agissant.peut_payer(cout) :
    #                     agissant.effets.append(magie)
    #                     reussite = True
    #                     #if isinstance(agissant,Heros):
    #                     #    malchance = trouve_skill(agissant.classe_principale,Skill_malchanceux)
    #                     #else:
    #                     #    malchance = None
    #                     #if malchance is not None:
    #                     #    reussite = malchance.utilise("cast_magic")
    #                     if isinstance(magie,Magie_cible) :
    #                         self.select_cible(magie,agissant)
    #                     if isinstance(magie,Magie_dirigee) :
    #                         self.select_direction(magie,agissant)
    #                     if isinstance(magie,Magie_cout) :
    #                         self.select_cout(magie,agissant)
    #                     agissant.paye(magie.cout_pm)
    #                     agissant.add_latence(latence)
    #                     if not reussite :
    #                         magie.miss_fire(agissant)
    #             else:
    #                 print("On ne peut pas utiliser une magie que l'on a pas !")
    #                 print(magie,agissant)



    #         # elif type_skill in [Divine_Thread_Weaving,Lesser_Divine_Thread_Weaving] :
    #         #     action = agissant.action
    #         #     latence,item = skill.utilise(action)
    #         #     agissant.add_latence(latence)
    #         #     self.items.append(item)



    #         # elif type_skill in [Scythe,Lesser_Scythe] :
    #         #     perce,element,taux = skill.utilise()
    #         #     attaque = Attaque(agissant,agissant.force*taux,element,"contact",1,"R__T_Pb",agissant.direction,"piercing",perce)
    #         #     self.tentative_attaque(attaque)



    #         # elif isinstance(skill, Egg_Laying):
    #         #     latence, oeuf = skill.utilise()
    #         #     agissant.add_latence(latence)
    #         #     if oeuf is not None :
    #         #         self.ajoute_entitee(oeuf)



    #         # elif isinstance(skill, Skill_merge):
    #         #     ID_cible = agissant.cible_merge
    #         #     latence = skill.utilise()
    #         #     if ID_cible is not None:
    #         #         esprit = self.entitees[ID_cible].esprit
    #         #         self.get_esprit(agissant.esprit).merge(esprit) #/!\ Syntaxe probablement fausse et foireuse, à vérifier
    #         #     agissant.add_latence(latence)



    #         # elif isinstance(skill, Skill_absorb):
    #         #     items = self.trouve_items_courants(agissant.get_position())
    #         #     latence = 1
    #         #     for ID_item in items:
    #         #         item = self.entitees[ID_item]
    #         #         latence_item,reussite = skill.utilise(item.priorite-agissant.get_priorite())
    #         #         latence += latence_item
    #         #         if reussite:
    #         #             agissant.inventaire.ramasse_item(ID_item)
    #         #             if item.get_classe() == Cadavre:
    #         #                 pass #/!\ Comment le skill est choisi ? Au hasard ? Comment différencier le type de slime (copie le skill au niveau 1, copie le skill à son niveau, vole le skill et laisse une copie au niveau 1, prend le skill mais le laisse quand même)
    #         #     agissant.add_latence(latence)



    #         # elif isinstance(skill, Skill_divide):
    #         #     latence = skill.utilise()
    #         #     if agissant.peut_payer(20): #Insérer le cout ici d'une façon ou d'une autre /!\
    #         #         new_slime = type(agissant)(agissant.position,agissant.niveau,True)
    #         #         agissant.paye(20)
    #         #         agissant.subit(20) # /!\ Ne pas utiliser subit() !
    #         #     agissant.add_latence(latence)



    # def fait_voler(self,item:Item):
    #     direction = item.get_direction()
    #     position = item.get_position()
    #     assert position is not None
    #     lab = self.labs[position.lab]
    #     lab.veut_passer(item,direction)

    def fait_eclore(self,oeuf:Oeuf,couveur:Agissant):
        # On pose l'oeuf à l'emplacement de l'agissant
        poussin = oeuf.agissant
        poussin.position = couveur.position
        # On ajoute le poussin à la liste des entitees
        self.ajoute_entitee(poussin)
        # On retire l'oeuf de la liste des entitees

    # def select_cible(self,magie:Magie_cible,agissant:Agissant):
    #     # if random.random() < agissant.talent :
    #         magie.cible = agissant.cible_magie
        
    # def select_direction(self,magie:Magie_dirigee,agissant:Agissant):
    #     # if random.random() < agissant.talent :
    #         magie.direction = agissant.dir_magie

    # def select_cout(self,magie:Magie_cout,agissant:Agissant):
    #     magie.cout = agissant.cout_magie

    # def select_cible_parchemin(self,magie:Magie_cible,agissant:Agissant):
    #     # if random.random() < agissant.talent :
    #         magie.cible = agissant.cible_magie_parchemin
        
    # def select_direction_parchemin(self,magie:Magie_dirigee,agissant:Agissant):
    #     # if random.random() < agissant.talent :
    #         magie.direction = agissant.dir_magie_parchemin

    # def select_cout_parchemin(self,magie:Magie_cout,agissant:Agissant):
    #     magie.cout = agissant.cout_magie_parchemin

    def get_cibles_potentielles_agissants(self,magie:Magie_cible,joueur:PJ):
        cibles_potentielles = set()
        for case in self.esprits["heros"].vue:
            if case.agissant is not None:
                cibles_potentielles.add(case.agissant)
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
            cibles = set()
            for agissant in cibles_potentielles:
                if agissant.position in poss:
                    cibles.add(agissant)
        else:
            cibles = set()
            for agissant in cibles_potentielles:
                cibles.add(agissant)
        return cibles

    def get_cibles_potentielles_items(self,magie:Magie_cible,joueur:PJ):
        cibles_potentielles:Set[Item] = set()
        for case in self.esprits["heros"].vue:
            cibles_potentielles |= case.items
            if case.agissant is not None:
                cibles_potentielles |= case.agissant.inventaire.get_items() #/!\ Rajouter une condition d'observation ! Mais ne pas l'appliquer à soi-même !
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
            cibles = set()
            for item in cibles_potentielles:
                if item.position in poss:
                    cibles.add(item)
        else:
            cibles = set()
            for item in cibles_potentielles:
                cibles.add(item)
        return cibles

    def get_cibles_potentielles_cases(self,magie:Magie_cible,joueur:PJ):
        esprit = joueur.esprit
        cibles_potentielles = set()
        for case in esprit.vue:
            cibles_potentielles.add(case.case.position)
        if isinstance(magie,Portee_limitee):
            poss = self.get_pos_touches(joueur.position,magie.portee_limite)
            cibles = set()
            for pos in cibles_potentielles:
                if pos in poss:
                    cibles.add(pos)
        else:
            cibles = cibles_potentielles
        return cibles

    def get_esprit(self,nom:str):
        if nom is not None:
            return self.esprits[nom]
        else:
            return None

    def get_nom_esprit(self,corp:Agissant):
        return corp.esprit

    def get_entitee(self,ID):
        return self.agissants[ID]

    def get_especes(self,ID:int) -> List[str]:
        entitee = self.agissants[ID]
        return entitee.especes

    def ajoute_entitees(self,entitees:Set[Entitee]):
        for entitee in entitees:
            self.ajoute_entitee(entitee)

    def ajoute_items(self,items:Set[Item]):
        for item in items:
            self.ajoute_entitee(item)

    def ajoute_entitee(self,entitee:Entitee):
        if isinstance(entitee,Agissant):
            self.agissants[entitee.ID]=entitee
            if entitee.position is not None:
                if entitee.position.lab in self.labs_courants:
                    self.agissants_courants.add(entitee)
        elif isinstance(entitee,Item):
            self.items[entitee.ID]=entitee
            if entitee.position is not None:
                if entitee.position.lab in self.labs_courants:
                    self.items_courants.add(entitee)
        elif isinstance(entitee,Decors):
            self.decors[entitee.ID]=entitee
            if entitee.position is not None:
                if entitee.position.lab in self.labs_courants:
                    self.decors_courants.add(entitee)

    def get_entitees_etage(self,num_lab:str):
        entitees:Set[Entitee] = set()
        for entitee in self.agissants_courants|self.items_courants|self.decors_courants:
            if entitee.position is not None:
                if entitee.position.lab==num_lab:
                    entitees.add(entitee)
        return entitees

    def get_agissants_items_labs_esprits(self) -> Tuple[Set[Agissant],Set[Item],Set[Labyrinthe],Set[Esprit]]:
        self.nb_tours+=1
        agissants:Set[Agissant] = set()
        items:Set[Item] = set()
        labs:Set[Labyrinthe] = set()
        esprits:Set[Esprit] = set()
        for agissant in self.agissants_courants :
            if agissant.etat == "vivant":
                agissants.add(agissant)
                esprit = agissant.esprit
                esprits.add(esprit)
        for item in self.items_courants:
            if item.etat == "intact":
                items.add(item)
            elif item.etat == "suspens":
                items.add(item)
            else:
                self.items_courants.remove(item)
                self.items.pop(item.ID)
        for niveau_lab in self.labs_courants:
            labs.add(self.labs[niveau_lab])
        return agissants, items, labs, esprits

    def get_touches(self,attaquant:Agissant,position:Position,portee=1,propagation="CD_S___",direction:Optional[Direction]=None,bloquable = True): #Trouve les agissants affectés par une attaque
        if attaquant.esprit is not None:
            intouchables = attaquant.esprit.get_corps()
        else:
            intouchables = {attaquant}
        labyrinthe = self.labs[position.lab]
        victimes_possibles = self.get_entitees_etage(position.lab)
        obstacles = set()
        for victime_possible in victimes_possibles :
            if victime_possible in intouchables :
                victimes_possibles.remove(victime_possible)
            elif bloquable:
                if isinstance(victime_possible,Agissant):
                    position_v = victime_possible.get_position()
                    obstacles.add(position_v)
        labyrinthe.attaque(position,portee,propagation,direction,obstacles)
        victimes:Set[Agissant] = set()
        for victime_possible in victimes_possibles :
            if isinstance(victime_possible,Agissant):
                position_v = victime_possible.get_position()
                if labyrinthe.case_from_position(position_v).clarte > 0 :
                    victimes.add(victime_possible)
        return victimes

    def get_touches_pos(self,bienfaiteur:Agissant,position:Position,portee:float=1,propagation = "C__S___",direction=None): #La même, mais pour les effets positifs comme les soins
        if bienfaiteur.esprit is not None:
            intouchables = {*bienfaiteur.esprit.get_ennemis()}
        else:
            intouchables:Set[Agissant] = set()
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,set())
        beneficiaires_possibles = self.get_entitees_etage(position.lab)
        beneficiaires:Set[Agissant] = set()
        for beneficiaire_possible in beneficiaires_possibles :
            if beneficiaire_possible in intouchables :
                beneficiaires_possibles.remove(beneficiaire_possible)
            else:
                if isinstance(beneficiaire_possible,Agissant):
                    position_b = beneficiaire_possible.get_position()
                    if labyrinthe.case_from_position(position_b).clarte > 0 :
                        beneficiaires.add(beneficiaire_possible)
        return beneficiaires

    def get_touches_neutre(self,responsable:Agissant,position:Position,portee=1,propagation = "C__S___",direction=None): #La même, mais pour les effets positifs comme les soins
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,set())
        touches_possibles = self.get_entitees_etage(position.lab)
        touches:Set[Agissant] = set()
        for touche_possible in touches_possibles :
            if isinstance(touche_possible,Agissant):
                position_t = touche_possible.get_position()
                if labyrinthe.case_from_position(position_t).clarte > 0 :
                    touches.add(touche_possible)
        return touches

    def get_cadavres_touches(self,position:Position,portee=1,propagation = "C__S___",direction = None): #La même, mais pour les effets sur les cadavres comme la réanimation
        cadavres:Set[Cadavre] = set()
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,set())
        cadavres_possibles = self.get_entitees_etage(position.lab)
        for cadavre_possible in cadavres_possibles :
            if isinstance(cadavre_possible,Cadavre):
                position_c = cadavre_possible.get_position()
                if labyrinthe.case_from_position(position_c).clarte > 0 :
                    cadavres.add(cadavre_possible)
        return cadavres

    def get_cases_touches(self,position:Position,portee:float=1,propagation = "C__S___",direction = None,traverse="tout",responsable:Agissant=NoOne()): #La même, mais pour les effets sur les cases
        cases:Set[Case] = set()
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,set())
        for pos in labyrinthe :
            case = labyrinthe.case_from_position(pos)
            if case.clarte > 0 :
                cases.add(case)
        return cases

    def get_pos_touches(self,position:Position,portee:float,propagation = "C__S___",direction:Optional[Direction] = None,traverse="tout",responsable:Agissant=NoOne()): #La même, mais pour les positions
        #On décide des obstacles:
        pos_obstacles = set()
        if traverse == "rien":
            obstacles = self.get_entitees_etage(position.lab)
            for obstacle in obstacles:
                if isinstance(obstacle,Non_superposable):
                    pos_obstacles.add(obstacle.get_position())
        elif traverse == "alliés":
            obstacles_possibles = self.get_entitees_etage(position.lab)
            if responsable!=NoOne():
                if responsable.esprit is not None:
                    for obstacle in obstacles_possibles:
                        if isinstance(obstacle,Non_superposable):
                            if isinstance(obstacle,Agissant):
                                if obstacle.esprit != responsable.esprit:
                                    pos_obstacles.add(obstacle.get_position())
                            else:
                                pos_obstacles.add(obstacle.get_position())
        elif traverse == "ennemis":
            obstacles_possibles = self.get_entitees_etage(position.lab)
            if responsable:
                if isinstance(responsable,Agissant):
                    if responsable.esprit is not None:
                        for obstacle in obstacles_possibles:
                            if isinstance(obstacle,Non_superposable):
                                if isinstance(obstacle,Agissant):
                                    if obstacle.esprit == responsable.esprit:
                                        pos_obstacles.add(obstacle.get_position())
                                else:
                                    pos_obstacles.add(obstacle.get_position())
        elif traverse == "tout":
            pass
        else:
            print("Quelle est cette traversée ?")
        poss:Set[Position] = set()
        labyrinthe = self.labs[position.lab]
        labyrinthe.attaque(position,portee,propagation,direction,pos_obstacles)
        for position in labyrinthe:
            if labyrinthe.case_from_position(position).clarte > 0:
                poss.add(position)
        return poss

# Imports utilisés dans le code
from Jeu.Action.Actions import *
from Jeu.Effet.Effets import *
from Jeu.Entitee.Entitees import *
from Jeu.Esprit.Esprits import *
from Jeu.Labyrinthe.Labyrinthes import *
from Jeu.Systeme.Classe import *