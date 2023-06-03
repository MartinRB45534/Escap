from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Controleur import Controleur
    from Old_Jeu.Labyrinthe.Structure_spatiale.Position import Position

# Imports des classes parentes
from Old_Jeu.Entitee.Item.Parchemin.Parchemin import Poly_de_cours

# Valeurs par défaut des paramètres
from Old_Jeu.Labyrinthe.Structure_spatiale.Position import ABSENT

class Poly_soin(Poly_de_cours):
    """Un parchemin qui enseigne la magie de soin."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_soin,50,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI407 Soin'","Qu'est-ce que c'est ?"]

class Poly_auto_soin(Poly_de_cours):
    """Un parchemin qui enseigne la magie de soin."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_auto_soin,30,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI304 Soin'","Qu'est-ce que c'est ?"]

class Poly_soin_zone(Poly_de_cours):
    """Un parchemin qui enseigne la magie de soin."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_soin_de_zone,75,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI507 Soin'","Qu'est-ce que c'est ?"]

class Poly_resurection(Poly_de_cours):
    """Un parchemin qui enseigne la magie de résurection."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_resurection,200,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI928 Résurection'","Qu'est-ce que c'est ?"]

class Poly_reanimation(Poly_de_cours):
    """Un parchemin qui enseigne la magie de réanimation de masse."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_reanimation_de_zone,199,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'BANI666 Réanimation'","Qu'est-ce que c'est ?"]

class Poly_boule_de_feu(Poly_de_cours):
    """Un parchemin qui enseigne la magie de boule de feu."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_boule_de_feu,80,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'FEU201 Boule de feu'","Qu'est-ce que c'est ?"]

class Poly_fleche_de_glace(Poly_de_cours):
    """Un parchemin qui enseigne la magie de flèche de glace."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_fleche_de_glace,85,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'GLAC201 Flèche de glace'","Qu'est-ce que c'est ?"]

class Poly_rocher(Poly_de_cours):
    """Un parchemin qui enseigne la magie de rocher."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_rocher,75,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'TERR201 Rocher'","Qu'est-ce que c'est ?"]

class Poly_ombre_furtive(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'ombre furtive."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_ombre_furtive,70,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'OMBR201 Ombre furtive'","Qu'est-ce que c'est ?"]

class Poly_jet_de_mana(Poly_de_cours):
    """Un parchemin qui enseigne la magie de jet de mana."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_jet_de_mana,100,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI303 Jet de mana'","Qu'est-ce que c'est ?"]

class Poly_eclair_noir(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'éclair noir."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_eclair_noir,300,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI902 Eclair noir'","Qu'est-ce que c'est ?"]

class Poly_faiblesse(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de faiblesse."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_faiblesse,20,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH101 Faiblesse'","Qu'est-ce que c'est ?"]

class Poly_cecite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de cécité."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_cecite,30,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH201 Cécité'","Qu'est-ce que c'est ?"]

class Poly_perte_de_pv(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de perte de pv."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_perte_de_pv,40,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH301 Perte de pv'","Qu'est-ce que c'est ?"]

class Poly_perte_de_pm(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de perte de pm."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_perte_de_pm,50,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH401 Perte de pm'","Qu'est-ce que c'est ?"]

class Poly_poches_trouees(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de poches trouées."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_poches_trouees,60,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH501 Poches trouées'","Qu'est-ce que c'est ?"]

class Poly_confusion(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de confusion."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_confusion,70,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH601 Confusion'","Qu'est-ce que c'est ?"]

class Poly_force(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de force."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_force,20,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH102 Force'","Qu'est-ce que c'est ?"]

class Poly_vision(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de vision."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_vision,30,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH202 Vision'","Qu'est-ce que c'est ?"]

class Poly_absorption(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement d'absorption."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_absorption,40,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH302 Absorption'","Qu'est-ce que c'est ?"]

class Poly_vitalite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de vitalité."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_vitalite,50,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH402 Vitalité'","Qu'est-ce que c'est ?"]

class Poly_celerite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de célérité."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_celerite,60,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH502 Célérité'","Qu'est-ce que c'est ?"]

class Poly_immunite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement d'immunite."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_immunite,70,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH602 Immunité'","Qu'est-ce que c'est ?"]

class Poly_flamme(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de flamme."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_flamme,40,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'FEU301 Flamme'","Qu'est-ce que c'est ?"]

class Poly_neige(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de neige."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_neige,40,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'GLAC301 Neige'","Qu'est-ce que c'est ?"]

class Poly_sable(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de sable."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_sable,40,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'TERR301 Sable'","Qu'est-ce que c'est ?"]

class Poly_tenebre(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de ténèbre."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_tenebre,40,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'OMBR301 Ténèbres'","Qu'est-ce que c'est ?"]

class Poly_rouille(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de rouille."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_rouille,70,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH203 Rouille'","Qu'est-ce que c'est ?"]

class Poly_renforcement(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de renforcement."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_renforcement,90,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH303 Renforcement'","Qu'est-ce que c'est ?"]

class Poly_bombe(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'enchantement de  bombe."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_enchantement_bombe,60,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ENCH103 Bombe'","Qu'est-ce que c'est ?"]

class Poly_reserve(Poly_de_cours):
    """Un parchemin qui enseigne la magie de reserve."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_reserve,100,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ECON501 Reserve'","Qu'est-ce que c'est ?"]

class Poly_investissement(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'investissement."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_investissement,95,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'ECON502 Investissement'","Qu'est-ce que c'est ?"]

class Poly_explosion_de_mana(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'explosion de mana."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_explosion_de_mana,100,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI512 Explosion de mana'","Qu'est-ce que c'est ?"]

class Poly_laser(Poly_de_cours):
    """Un parchemin qui enseigne la magie de laser."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_laser,50,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI407 Laser'","Qu'est-ce que c'est ?"]

class Poly_brasier(Poly_de_cours):
    """Un parchemin qui enseigne la magie de brasier."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_brasier,60,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'FEU401 Brasier'","Qu'est-ce que c'est ?"]

class Poly_avalanche(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'avalanche."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_avalanche,60,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'TERR401 Avalanche'","Qu'est-ce que c'est ?"]

class Poly_blizzard(Poly_de_cours):
    """Un parchemin qui enseigne la magie de blizzard."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_blizzard,65,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'GLAC501 Blizzard'","Qu'est-ce que c'est ?"]

class Poly_obscurite(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'obscurité."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_obscurite,65,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'OMBR501 Obscurité'","Qu'est-ce que c'est ?"]

class Poly_dopage(Poly_de_cours):
    """Un parchemin qui enseigne la magie de dopage."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_dopage,30,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'MAGI201 Dopage'","Qu'est-ce que c'est ?"]

class Poly_instakill(Poly_de_cours):
    """Un parchemin qui enseigne la magie d'instakill."""
    def __init__(self,controleur:Controleur,position:Position=ABSENT):
        Poly_de_cours.__init__(self,controleur,Magie_instakill,120,position)

    def get_description(self,observation=0):
        return["Un parchemin de cours","Intitulé : 'BANI807 Instakill'","Qu'est-ce que c'est ?"]

# Imports utilisés dans le code
from Old_Jeu.Action.Magie.Magies_soin import Magie_auto_soin, Magie_soin, Magie_soin_de_zone, Magie_resurection, Magie_reanimation_de_zone
from Old_Jeu.Action.Magie.Magies_projectiles import Magie_boule_de_feu, Magie_eclair_noir, Magie_fleche_de_glace, Magie_jet_de_mana, Magie_ombre_furtive, Magie_rocher
from Old_Jeu.Action.Magie.Magies_enchantement import Magie_enchantement_bombe, Magie_enchantement_absorption, Magie_enchantement_cecite, Magie_enchantement_celerite, Magie_enchantement_confusion, Magie_enchantement_faiblesse, Magie_enchantement_flamme, Magie_enchantement_force, Magie_enchantement_immunite, Magie_enchantement_neige, Magie_enchantement_perte_de_pm, Magie_enchantement_perte_de_pv, Magie_enchantement_poches_trouees, Magie_enchantement_renforcement, Magie_enchantement_rouille, Magie_enchantement_sable, Magie_enchantement_tenebre, Magie_enchantement_vision, Magie_enchantement_vitalite
from Old_Jeu.Action.Magie.Magies_economie import Magie_investissement, Magie_explosion_de_mana, Magie_reserve
from Old_Jeu.Action.Magie.Magies_attaque.Attaques_corps_a_corps import Magie_laser, Magie_brasier, Magie_avalanche
from Old_Jeu.Action.Magie.Magies_attaque.Boosts import Magie_dopage
from Old_Jeu.Action.Magie.Magies_diverses import Magie_blizzard, Magie_obscurite, Magie_instakill