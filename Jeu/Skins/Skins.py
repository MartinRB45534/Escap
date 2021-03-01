import pygame

class Illustration:
    def __init__(self,nom_fichier):
        self.image = pygame.image.load("Jeu/Skins/"+nom_fichier).convert_alpha()

    def dessine_toi(self,screen,position):
        screen.blit(self.image,position)

class Skin(Illustration):
    def dessine_toi(self,screen,position,taille=40,direction=(0)):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,direction*-90),(taille,taille)),position)

global SKIN_VIDE
SKIN_VIDE = Skin("vide.png")
global SKIN_DIRECTION
SKIN_DIRECTION = Skin("direction.png")
global SKIN_BROUILLARD
SKIN_BROUILLARD = Skin("brouillard.png")
global SKIN_MUR_BROUILLARD
SKIN_MUR_BROUILLARD = Skin("brouillard_mur_transparent.png")
global SKIN_CASE
SKIN_CASE = Skin("case.png")
global SKIN_CASE_1
SKIN_CASE_1 = Skin("case_1.png")
global SKIN_CASE_2
SKIN_CASE_2 = Skin("case_2.png")
global SKIN_CASE_3
SKIN_CASE_3 = Skin("case_3.png")
global SKIN_CASE_4
SKIN_CASE_4 = Skin("case_4.png")
global SKIN_CASE_5
SKIN_CASE_5 = Skin("case_5.png")
global SKIN_CASE_6
SKIN_CASE_6 = Skin("case_6.png")
global SKIN_CASE_7
SKIN_CASE_7 = Skin("case_7.png")
global SKIN_CASE_8
SKIN_CASE_8 = Skin("case_8.png")
global SKIN_AGISSANT
SKIN_AGISSANT = Skin("agissant.png")
global SKIN_ROUGE
SKIN_ROUGE = Skin("rouge.png")
global SKIN_VERT
SKIN_VERT = Skin("vert.png")
global SKIN_CADAVRE
SKIN_CADAVRE = Skin("cadavre.png")
global SKIN_CRANE
SKIN_CRANE = Skin("crane.png")
global SKIN_OEUF
SKIN_OEUF = Skin("oeuf.png")
global SKIN_BLESSURE
SKIN_BLESSURE = Skin("blessure.png")
global SKIN_JOUEUR
SKIN_JOUEUR = Skin("joueur.png")
global SKIN_RECEPTIONNISTE
SKIN_RECEPTIONNISTE = Skin("agissant.png")
global SKIN_PAUME
SKIN_PAUME = Skin("agissant.png")
global SKIN_PEUREUSE
SKIN_PEUREUSE = Skin("agissant.png")
global SKIN_CODEUR
SKIN_CODEUR = Skin("agissant.png")
global SKIN_ENCOMBRANT
SKIN_ENCOMBRANT = Skin("agissant.png")
global SKIN_ALCHIMISTE
SKIN_ALCHIMISTE = Skin("agissant.png")
global SKIN_PESTE
SKIN_PESTE = Skin("agissant.png")
global SKIN_BOMBE_ATOMIQUE
SKIN_BOMBE_ATOMIQUE = Skin("agissant.png")
global SKIN_MARCHAND
SKIN_MARCHAND = Skin("agissant.png")
global SKIN_HUMAIN
SKIN_HUMAIN = Skin("humain.png")
global SKIN_MYSTERE
SKIN_MYSTERE = Skin("mystere.png")
global SKIN_BOUCLIER
SKIN_BOUCLIER = Skin("bouclier.png")
global SKIN_BOUCLIER_BIS
SKIN_BOUCLIER_BIS = Skin("bouclier_bis.png")
global SKIN_CLE
SKIN_CLE = Skin("cle.png")
global SKIN_POTION
SKIN_POTION = Skin("potion.png")
global SKIN_POTION_POISON
SKIN_POTION_POISON = Skin("potion_poison.png")
global SKIN_PARCHEMIN
SKIN_PARCHEMIN = Skin("parchemin.png")
global SKIN_EPEE
SKIN_EPEE = Skin("epee.png")
global SKIN_LANCE
SKIN_LANCE = Skin("lance.png")
global SKIN_ARME
SKIN_ARME = Skin("arme.png")
global SKIN_ARMURE
SKIN_ARMURE = Skin("armure.png")
global SKIN_ARMURE_BIS
SKIN_ARMURE_BIS = Skin("armure_bis.png")
global SKIN_CASQUE
SKIN_CASQUE = Skin("casque.png")
global SKIN_ANNEAU
SKIN_ANNEAU = Skin("anneau.png")
global SKIN_PROJECTILE
SKIN_PROJECTILE = Skin("projectile.png")
global SKIN_FLECHE
SKIN_FLECHE = Skin("fleche.png")
global SKIN_EXPLOSIF
SKIN_EXPLOSIF = Skin("explosif.png")
global SKIN_EXPLOSE
SKIN_EXPLOSE = Skin("explose.png")
global SKIN_ROCHER
SKIN_ROCHER = Skin("rocher.png")
global SKIN_BOULE_DE_FEU
SKIN_BOULE_DE_FEU = Skin("boule_de_feu.png")
global SKIN_FLECHE_DE_GLACE
SKIN_FLECHE_DE_GLACE = Skin("fleche_de_glace.png")
global SKIN_OMBRE_FURTIVE
SKIN_OMBRE_FURTIVE = Skin("ombre_furtive.png")
global SKIN_EFFET
SKIN_EFFET = Skin("effet.png")
global SKIN_MUR
SKIN_MUR = Skin("mur.png")
global SKIN_MUR_CASSE
SKIN_MUR_CASSE = Skin("mur_casse.png")
global SKIN_ESALIER
SKIN_ESCALIER = Skin("escalier.png")
global SKIN_ESALIER_BAS
SKIN_ESCALIER_BAS = Skin("escalier_bas.png")
global SKIN_ESALIER_HAUT
SKIN_ESCALIER_HAUT = Skin("escalier_haut.png")
global SKIN_PORTE
SKIN_PORTE = Skin("porte.png")
global SKIN_PORTE_OUVERTE
SKIN_PORTE_OUVERTE = Skin("porte_ouverte.png")
global SKIN_BARRIERE
SKIN_BARRIERE = Skin("barriere.png")
global SKIN_PORTAIL
SKIN_PORTAIL = Skin("portail.png")
global SKIN_HAUT
SKIN_HAUT = Skin("haut.png")
global SKIN_DROITE
SKIN_DROITE = Skin("droite.png")
global SKIN_BAS
SKIN_BAS = Skin("bas.png")
global SKIN_GAUCHE
SKIN_GAUCHE = Skin("gauche.png")
global SKIN_IN
SKIN_IN = Skin("in.png")
global SKIN_OUT
SKIN_OUT = Skin("out.png")
global SKIN_QUITTER
SKIN_QUITTER = Skin("quitter.png")
global SKIN_ZONES
SKIN_ZONES = Skin("zones.png")
global SKIN_ATTAQUE_TERRE
SKIN_ATTAQUE_TERRE = Skin("attaque_1.png")
global SKIN_ATTAQUE_FEU
SKIN_ATTAQUE_FEU = Skin("attaque_2.png")
global SKIN_ATTAQUE_GLACE
SKIN_ATTAQUE_GLACE = Skin("attaque_4.png")
global SKIN_ATTAQUE_OMBRE
SKIN_ATTAQUE_OMBRE = Skin("attaque_8.png")

# Skills :

global SKIN_SKILL
SKIN_SKILL = Skin("skill.png")
global SKIN_SKILL_ANALYSE
SKIN_SKILL_ANALYSE = Skin("skill_analyse.png")
global SKIN_SKILL_ATTAQUE
SKIN_SKILL_ATTAQUE = Skin("skill_attaque.png")
global SKIN_SKILL_AURA_MORTELLE
SKIN_SKILL_AURA_MORTELLE = Skin("skill_aura_mortelle.png")
global SKIN_SKILL_BLOCAGE
SKIN_SKILL_BLOCAGE = Skin("skill_blocage.png")
global SKIN_SKILL_BOOST_AURA
SKIN_SKILL_BOOST_AURA = Skin("skill_boost_aura.png")
global SKIN_SKILL_BOOST_DEGATS_FLECHES
SKIN_SKILL_BOOST_DEGATS_FLECHES = Skin("skill_boost_degats_fleches.png")
global SKIN_SKILL_BOOST_DEGATS_PROJECTILES
SKIN_SKILL_BOOST_DEGATS_PROJECTILES = Skin("skill_boost_degats_projectiles.png")
global SKIN_SKILL_BOOST_ENCHANTEMENT
SKIN_SKILL_BOOST_ENCHANTEMENT = Skin("skill_boost_enchantement.png")
global SKIN_SKILL_BOOST_EPEE
SKIN_SKILL_BOOST_EPEE = Skin("skill_boost_epee.png")
global SKIN_SKILL_BOOST_LANCE
SKIN_SKILL_BOOST_LANCE = Skin("skill_boost_lance.png")
global SKIN_SKILL_BOOST_PRIORITE_AURA
SKIN_SKILL_BOOST_PRIORITE_AURA = Skin("skill_boost_priorite_aura.png")
global SKIN_SKILL_BOOST_PRIORITE_FLECHE
SKIN_SKILL_BOOST_PRIORITE_FLECHE = Skin("skill_boost_priorite_fleches.png")
global SKIN_SKILL_BOOST_PRIORITE_MAGIQUE
SKIN_SKILL_BOOST_PRIORITE_MAGIQUE = Skin("skill_boost_priorite_magique.png")
global SKIN_SKILL_BOOST_RESTAURATIONS
SKIN_SKILL_BOOST_RESTAURATIONS = Skin("skill_boost_restaurations.png")
global SKIN_SKILL_BOOST_SOIN
SKIN_SKILL_BOOST_SOIN = Skin("skill_boost_soin.png")
global SKIN_SKILL_BOOST_ZONE_RESTAURATION
SKIN_SKILL_BOOST_ZONE_RESTAURATION = Skin("skill_boost_zone_restaurations.png")
global SKIN_SKILL_CREATION_EXPLOSIF
SKIN_SKILL_CREATION_EXPLOSIF = Skin("skill_creation_explosif.png")
global SKIN_SKILL_CREATION_FLECHES
SKIN_SKILL_CREATION_FLECHES = Skin("skill_creation_fleches.png")
global SKIN_SKILL_DEFENSE
SKIN_SKILL_DEFENSE = Skin("skill_defense.png")
global SKIN_SKILL_DEPLACEMENT
SKIN_SKILL_DEPLACEMENT = Skin("skill_deplacement.png")
global SKIN_SKILL_ECRASEMENT
SKIN_SKILL_ECRASEMENT = Skin("skill_ecrasement.png")
global SKIN_SKILL_ESSENCE_MAGIQUE
SKIN_SKILL_ESSENCE_MAGIQUE = Skin("skill_essence_magique.png")
global SKIN_SKILL_IMMORTALITE
SKIN_SKILL_IMMORTALITE = Skin("skill_immortalite.png")
global SKIN_SKILL_INSTAKILL
SKIN_SKILL_INSTAKILL = Skin("skill_instakill.png")
global SKIN_SKILL_LANCER
SKIN_SKILL_LANCER = Skin("skill_lancer.png")
global SKIN_SKILL_LANCER_GRIS
SKIN_SKILL_LANCER_GRIS = Skin("skill_lancer_gris.png")
global SKIN_SKILL_MAGIE
SKIN_SKILL_MAGIE = Skin("skill_magie.png")
global SKIN_SKILL_MAGIE_GRIS
SKIN_SKILL_MAGIE_GRIS = Skin("skill_magie_gris.png")
global SKIN_SKILL_MAGIE_INFINIE
SKIN_SKILL_MAGIE_INFINIE = Skin("skill_magie_infinie.png")
global SKIN_SKILL_MANIPULATION_ARME
SKIN_SKILL_MANIPULATION_ARME = Skin("skill_manipulation_arme.png")
global SKIN_SKILL_MANIPULATION_BOUCLIER
SKIN_SKILL_MANIPULATION_BOUCLIER = Skin("skill_manipulation_bouclier.png")
global SKIN_SKILL_MANIPULATION_EPEE
SKIN_SKILL_MANIPULATION_EPEE = Skin("skill_manipulation_epee.png")
global SKIN_SKILL_OBSERVATION
SKIN_SKILL_OBSERVATION = Skin("skill_observation.png")
global SKIN_SKILL_RAMASSE
SKIN_SKILL_RAMASSE = Skin("skill_ramasse.png")
global SKIN_SKILL_REANIMATION
SKIN_SKILL_REANIMATION = Skin("skill_reanimation.png")
global SKIN_SKILL_REANIMATION_RENFORCEE
SKIN_SKILL_REANIMATION_RENFORCEE = Skin("skill_reanimation_renforcee.png")
global SKIN_SKILL_REGENERATION_MP
SKIN_SKILL_REGENERATION_MP = Skin("skill_regeneration_mp.png")
global SKIN_SKILL_SOIN
SKIN_SKILL_SOIN = Skin("skill_soin.png")
global SKIN_SKILL_STOMP
SKIN_SKILL_STOMP = Skin("skill_stomp.png")
global SKIN_SKILL_VOL
SKIN_SKILL_VOL = Skin("skill_vol.png")
global SKIN_SKILL_VOL_PRIORITE
SKIN_SKILL_VOL_PRIORITE = Skin("skill_vol_priorite.png")

# Magies :

global SKIN_MAGIE_ACCELERATION
SKIN_MAGIE_ACCELERATION = Skin("magie_acceleration.png")
global SKIN_MAGIE_AUTO_SOIN
SKIN_MAGIE_AUTO_SOIN = Skin("magie_auto_soin.png")
global SKIN_MAGIE_AVALANCHE
SKIN_MAGIE_AVALANCHE = Skin("magie_avalanche.png")
global SKIN_MAGIE_BLIZZARD
SKIN_MAGIE_BLIZZARD = Skin("magie_blizzard.png")
global SKIN_MAGIE_BOULE_DE_FEU
SKIN_MAGIE_BOULE_DE_FEU = Skin("magie_boule_de_feu.png")
global SKIN_MAGIE_BRASIER
SKIN_MAGIE_BRASIER = Skin("magie_brasier.png")
global SKIN_MAGIE_DOPAGE
SKIN_MAGIE_DOPAGE = Skin("magie_dopage.png")
global SKIN_MAGIE_ECLAIR_NOIR
SKIN_MAGIE_ECLAIR_NOIR = Skin("magie_eclair_noir.png")
global SKIN_MAGIE_EXPLOSION_DE_MANA
SKIN_MAGIE_EXPLOSION_DE_MANA = Skin("magie_explosion_de_mana.png")
global SKIN_MAGIE_FLECHE_DE_GLACE
SKIN_MAGIE_FLECHE_DE_GLACE = Skin("magie_fleche_de_glace.png")
global SKIN_MAGIE_INSTAKILL
SKIN_MAGIE_INSTAKILL = Skin("magie_instakill.png")
global SKIN_MAGIE_INVESTISSEMENT
SKIN_MAGIE_INVESTISSEMENT = Skin("magie_investissement.png")
global SKIN_MAGIE_JET_DE_MANA
SKIN_MAGIE_JET_DE_MANA = Skin("magie_jet_de_mana.png")
global SKIN_MAGIE_LASER
SKIN_MAGIE_LASER = Skin("magie_laser.png")
global SKIN_MAGIE_OBSCURITE
SKIN_MAGIE_OBSCURITE = Skin("magie_obscurite.png")
global SKIN_MAGIE_OMBRE_FURTIVE
SKIN_MAGIE_OMBRE_FURTIVE = Skin("magie_ombre_furtive.png")
global SKIN_MAGIE_ONDE_DE_CHOC
SKIN_MAGIE_ONDE_DE_CHOC = Skin("magie_onde_de_choc.png")
global SKIN_MAGIE_PROTECTION
SKIN_MAGIE_PROTECTION = Skin("magie_protection.png")
global SKIN_MAGIE_REANIMATION_ZONE
SKIN_MAGIE_REANIMATION_ZONE = Skin("magie_reanimation_zone.png")
global SKIN_MAGIE_RESERVE
SKIN_MAGIE_RESERVE = Skin("magie_reserve.png")
global SKIN_MAGIE_RESTAURATION_PM
SKIN_MAGIE_RESTAURATION_PM = Skin("magie_restauration_pm.png")
global SKIN_MAGIE_RESURECTION
SKIN_MAGIE_RESURECTION = Skin("magie_resurection.png")
global SKIN_MAGIE_ROCHER
SKIN_MAGIE_ROCHER = Skin("magie_rocher.png")
global SKIN_MAGIE_SOIN
SKIN_MAGIE_SOIN = Skin("magie_soin.png")
global SKIN_MAGIE_SOIN_SUPERIEUR
SKIN_MAGIE_SOIN_SUPERIEUR = Skin("magie_soin_superieur.png")
global SKIN_MAGIE_SOIN_ZONE
SKIN_MAGIE_SOIN_ZONE = Skin("magie_soin_zone.png")
global SKIN_MAGIE_VISION
SKIN_MAGIE_VISION = Skin("magie_vision.png")

# Enchantement :

global SKIN_MAGIE_ENCHANTEMENT_ABSORPTION
SKIN_MAGIE_ENCHANTEMENT_ABSORPTION = Skin("magie_enchantement_absorption.png")
global SKIN_MAGIE_ENCHANTEMENT_BOMBE
SKIN_MAGIE_ENCHANTEMENT_BOMBE = Skin("magie_enchantement_bombe.png")
global SKIN_MAGIE_ENCHANTEMENT_CECITE
SKIN_MAGIE_ENCHANTEMENT_CECITE = Skin("magie_enchantement_cecite.png")
global SKIN_MAGIE_ENCHANTEMENT_CELERITE
SKIN_MAGIE_ENCHANTEMENT_CELERITE = Skin("magie_enchantement_celerite.png")
global SKIN_MAGIE_ENCHANTEMENT_CONFUSION
SKIN_MAGIE_ENCHANTEMENT_CONFUSION = Skin("magie_enchantement_confusion.png")
global SKIN_MAGIE_ENCHANTEMENT_DEFENSE
SKIN_MAGIE_ENCHANTEMENT_DEFENSE = Skin("magie_enchantement_defense.png")
global SKIN_MAGIE_ENCHANTEMENT_DEFENSIF
SKIN_MAGIE_ENCHANTEMENT_DEFENSIF = Skin("magie_enchantement_defensif.png")
global SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE
SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE = Skin("magie_enchantement_faiblesse.png")
global SKIN_MAGIE_ENCHANTEMENT_FLAMME
SKIN_MAGIE_ENCHANTEMENT_FLAMME = Skin("magie_enchantement_flamme.png")
global SKIN_MAGIE_ENCHANTEMENT_FORCE
SKIN_MAGIE_ENCHANTEMENT_FORCE = Skin("magie_enchantement_force.png")
global SKIN_MAGIE_ENCHANTEMENT_IMMUNITE
SKIN_MAGIE_ENCHANTEMENT_IMMUNITE = Skin("magie_enchantement_immunite.png")
global SKIN_MAGIE_ENCHANTEMENT_NEIGE
SKIN_MAGIE_ENCHANTEMENT_NEIGE = Skin("magie_enchantement_neige.png")
global SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PM
SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PM = Skin("magie_enchantement_perte_de_pm.png")
global SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PV
SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PV = Skin("magie_enchantement_perte_de_pv.png")
global SKIN_MAGIE_ENCHANTEMENT_POCHES_TROUEES
SKIN_MAGIE_ENCHANTEMENT_POCHES_TROUEES = Skin("magie_enchantement_poches_trouees.png")
global SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT
SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT = Skin("magie_enchantement_renforcement.png")
global SKIN_MAGIE_ENCHANTEMENT_ROUILLE
SKIN_MAGIE_ENCHANTEMENT_ROUILLE = Skin("magie_enchantement_rouille.png")
global SKIN_MAGIE_ENCHANTEMENT_SABLE
SKIN_MAGIE_ENCHANTEMENT_SABLE = Skin("magie_enchantement_sable.png")
global SKIN_MAGIE_ENCHANTEMENT_TENEBRE
SKIN_MAGIE_ENCHANTEMENT_TENEBRE = Skin("magie_enchantement_tenebre.png")
global SKIN_MAGIE_ENCHANTEMENT_VISION
SKIN_MAGIE_ENCHANTEMENT_VISION = Skin("magie_enchantement_vision.png")
global SKIN_MAGIE_ENCHANTEMENT_VITALITE
SKIN_MAGIE_ENCHANTEMENT_VITALITE = Skin("magie_enchantement_vitalite.png")

# Créations d'items :

global SKIN_CREE_FLECHE_DE_BASE
SKIN_CREE_FLECHE_DE_BASE = Skin("cree_fleche_de_base.png")
global SKIN_CREE_FLECHE_FANTOME
SKIN_CREE_FLECHE_FANTOME = Skin("cree_fleche_fantome.png")
global SKIN_CREE_FLECHE_LOURDE
SKIN_CREE_FLECHE_LOURDE = Skin("cree_fleche_lourde.png")
global SKIN_CREE_FLECHE_LEGERE
SKIN_CREE_FLECHE_LEGERE = Skin("cree_fleche_legere.png")
global SKIN_CREE_FLECHE_EXPLOSIVE
SKIN_CREE_FLECHE_EXPLOSIVE = Skin("cree_fleche_explosive.png")
global SKIN_CREE_CHARGE_DE_BASE
SKIN_CREE_CHARGE_DE_BASE = Skin("cree_charge_de_base.png")
global SKIN_CREE_CHARGE_LOURDE
SKIN_CREE_CHARGE_LOURDE = Skin("cree_charge_lourde.png")
global SKIN_CREE_CHARGE_ETENDUE
SKIN_CREE_CHARGE_ETENDUE = Skin("cree_charge_etendue.png")

# Classes :

global SKIN_ANGE
SKIN_ANGE = Skin("ange.png")
global SKIN_ARCHER
SKIN_ARCHER = Skin("archer.png")
global SKIN_ARTIFICIER
SKIN_ARTIFICIER = Skin("artificier.png")
global SKIN_ASSASSIN
SKIN_ASSASSIN = Skin("assassin.png")
global SKIN_ELEMENTALISTE
SKIN_ELEMENTALISTE = Skin("elementaliste.png")
global SKIN_ENCHANTEUR
SKIN_ENCHANTEUR = Skin("enchanteur.png")
global SKIN_EPEISTE
SKIN_EPEISTE = Skin("epeiste.png")
global SKIN_FANTOME
SKIN_FANTOME = Skin("fantome.png")
global SKIN_INHUMANITE
SKIN_INHUMANITE = Skin("inhumanite.png")
global SKIN_MAGICIEN
SKIN_MAGICIEN = Skin("magicien.png")
global SKIN_NECROMANCIEN
SKIN_NECROMANCIEN = Skin("necromancien.png")
global SKIN_SOUTIEN
SKIN_SOUTIEN = Skin("soutien.png")

# Choix :

global SKIN_AJOUT_CHARGE_ETENDUE
SKIN_AJOUT_CHARGE_ETENDUE = Skin("ajout_charge_etendue.png")
global SKIN_AJOUT_CHARGE_LOURDE
SKIN_AJOUT_CHARGE_LOURDE = Skin("ajout_charge_lourde.png")
global SKIN_AJOUT_FLECHE_EXPLOSIVE
SKIN_AJOUT_FLECHE_EXPLOSIVE = Skin("ajout_fleche_explosive.png")
global SKIN_AJOUT_FLECHE_FANTOME
SKIN_AJOUT_FLECHE_FANTOME = Skin("ajout_fleche_fantome.png")
global SKIN_AJOUT_FLECHE_PERCANTE
SKIN_AJOUT_FLECHE_PERCANTE = Skin("ajout_fleche_percante.png")
global SKIN_AJOUT_FLECHES_LOURDE_LEGERE
SKIN_AJOUT_FLECHES_LOURDE_LEGERE = Skin("ajout_fleches_lourde_legere.png")
global SKIN_BOOST_ATTAQUE
SKIN_BOOST_ATTAQUE = Skin("boost_attaque.png")
global SKIN_BOOST_DE_PRIORITE_D_ATTAQUE
SKIN_BOOST_DE_PRIORITE_D_ATTAQUE = Skin("boost_de_priorite_d_attaque.png")
global SKIN_BOOST_DEGATS_MAGIQUES
SKIN_BOOST_DEGATS_MAGIQUES = Skin("boost_degats_magiques.png")
global SKIN_BOOST_FORCE
SKIN_BOOST_FORCE = Skin("boost_force.png")
global SKIN_BOOST_PM
SKIN_BOOST_PM = Skin("boost_pm.png")
global SKIN_BOOST_PORTEE
SKIN_BOOST_PORTEE = Skin("boost_portee.png")
global SKIN_BOOST_PORTEE_EXPLOSIFS
SKIN_BOOST_PORTEE_EXPLOSIFS = Skin("boost_portee_explosifs.png")
global SKIN_BOOST_PORTEE_MAGIE
SKIN_BOOST_PORTEE_MAGIE = Skin("boost_portee_magie.png")
global SKIN_BOOST_PRIORITE
SKIN_BOOST_PRIORITE = Skin("boost_priorite.png")
global SKIN_BOOST_PRIORITE_ANALYSE
SKIN_BOOST_PRIORITE_ANALYSE = Skin("boost_priorite_analyse.png")
global SKIN_BOOST_PRIORITE_DEPLACEMENT
SKIN_BOOST_PRIORITE_DEPLACEMENT = Skin("boost_priorite_deplacement.png")
global SKIN_BOOST_PRIORITE_EXPLOSIFS
SKIN_BOOST_PRIORITE_EXPLOSIFS = Skin("boost_priorite_explosifs.png")
global SKIN_BOOST_PRIORITE_OBSERVATION
SKIN_BOOST_PRIORITE_OBSERVATION = Skin("boost_priorite_observation.png")
global SKIN_BOOST_PV
SKIN_BOOST_PV = Skin("boost_pv.png")
global SKIN_BOOST_VITESSE_EXPLOSIFS
SKIN_BOOST_VITESSE_EXPLOSIFS = Skin("boost_vitesse_explosifs.png")
global SKIN_BOOST_REGEN_HP
SKIN_BOOST_REGEN_HP = Skin("lvl_up_regen_hp.png")
global SKIN_BOOST_REGEN_MP
SKIN_BOOST_REGEN_MP = Skin("lvl_up_regen_mp.png")

# Choix élémentaux :

global SKIN_CHOIX_ELEMENTAL_TERRE
SKIN_CHOIX_ELEMENTAL_TERRE = Skin("lvl_up_elemental_t.png")
global SKIN_CHOIX_ELEMENTAL_FEU
SKIN_CHOIX_ELEMENTAL_FEU = Skin("lvl_up_elemental_f.png")
global SKIN_CHOIX_ELEMENTAL_GLACE
SKIN_CHOIX_ELEMENTAL_GLACE = Skin("lvl_up_elemental_g.png")
global SKIN_CHOIX_ELEMENTAL_OMBRE
SKIN_CHOIX_ELEMENTAL_OMBRE = Skin("lvl_up_elemental_o.png")
global SKIN_CHOIX_AURA_TERRE
SKIN_CHOIX_AURA_TERRE = Skin("lvl_up_aura_t.png")
global SKIN_CHOIX_AURA_FEU
SKIN_CHOIX_AURA_FEU = Skin("lvl_up_aura_f.png")
global SKIN_CHOIX_AURA_GLACE
SKIN_CHOIX_AURA_GLACE = Skin("lvl_up_aura_g.png")
global SKIN_CHOIX_AURA_OMBRE
SKIN_CHOIX_AURA_OMBRE = Skin("lvl_up_aura_o.png")
global SKIN_CHOIX_AFFINITE_TERRE
SKIN_CHOIX_AFFINITE_TERRE = Skin("lvl_up_aff_t.png")
global SKIN_CHOIX_MAGIE_TERRE
SKIN_CHOIX_MAGIE_TERRE = Skin("lvl_up_magie_t.png")
global SKIN_CHOIX_AFFINITE_FEU
SKIN_CHOIX_AFFINITE_FEU = Skin("lvl_up_aff_f.png")
global SKIN_CHOIX_MAGIE_FEU
SKIN_CHOIX_MAGIE_FEU = Skin("lvl_up_magie_f.png")
global SKIN_CHOIX_AFFINITE_GLACE
SKIN_CHOIX_AFFINITE_GLACE = Skin("lvl_up_aff_g.png")
global SKIN_CHOIX_MAGIE_GLACE
SKIN_CHOIX_MAGIE_GLACE = Skin("lvl_up_magie_g.png")
global SKIN_CHOIX_AFFINITE_OMBRE
SKIN_CHOIX_AFFINITE_OMBRE = Skin("lvl_up_aff_o.png")
global SKIN_CHOIX_MAGIE_OMBRE
SKIN_CHOIX_MAGIE_OMBRE = Skin("lvl_up_magie_o.png")
global SKIN_BOURGEON_GAUCHE_EXTREME_GAUCHE
SKIN_BOURGEON_GAUCHE_EXTREME_GAUCHE = Illustration("bourgeon_gauche_extreme_gauche.png")
global SKIN_BOURGEON_GAUCHE_LOIN_GAUCHE
SKIN_BOURGEON_GAUCHE_LOIN_GAUCHE = Illustration("bourgeon_gauche_loin_gauche.png")
global SKIN_BOURGEON_GAUCHE_GAUCHE
SKIN_BOURGEON_GAUCHE_GAUCHE = Illustration("bourgeon_gauche_gauche.png")
global SKIN_BOURGEON_GAUCHE_CENTRE_GAUCHE
SKIN_BOURGEON_GAUCHE_CENTRE_GAUCHE = Illustration("bourgeon_gauche_centre_gauche.png")
global SKIN_BOURGEON_GAUCHE_CENTRE
SKIN_BOURGEON_GAUCHE_CENTRE = Illustration("bourgeon_gauche_centre.png")
global SKIN_BOURGEON_GAUCHE_CENTRE_DROIT
SKIN_BOURGEON_GAUCHE_CENTRE_DROIT = Illustration("bourgeon_gauche_centre_droit.png")
global SKIN_BOURGEON_GAUCHE_DROITE
SKIN_BOURGEON_GAUCHE_DROITE = Illustration("bourgeon_gauche_droite.png")
global SKIN_BOURGEON_GAUCHE_LOIN_DROIT
SKIN_BOURGEON_GAUCHE_LOIN_DROIT = Illustration("bourgeon_gauche_loin_droit.png")
global SKIN_BOURGEON_GAUCHE_EXTREME_DROITE
SKIN_BOURGEON_GAUCHE_EXTREME_DROITE = Illustration("bourgeon_gauche_extreme_droite.png")
global SKIN_BOURGEON_DROITE_EXTREME_GAUCHE
SKIN_BOURGEON_DROITE_EXTREME_GAUCHE = Illustration("bourgeon_droite_extreme_gauche.png")
global SKIN_BOURGEON_DROITE_LOIN_GAUCHE
SKIN_BOURGEON_DROITE_LOIN_GAUCHE = Illustration("bourgeon_droite_loin_gauche.png")
global SKIN_BOURGEON_DROITE_GAUCHE
SKIN_BOURGEON_DROITE_GAUCHE = Illustration("bourgeon_droite_gauche.png")
global SKIN_BOURGEON_DROITE_CENTRE_GAUCHE
SKIN_BOURGEON_DROITE_CENTRE_GAUCHE = Illustration("bourgeon_droite_centre_gauche.png")
global SKIN_BOURGEON_DROITE_CENTRE
SKIN_BOURGEON_DROITE_CENTRE = Illustration("bourgeon_droite_centre.png")
global SKIN_BOURGEON_DROITE_CENTRE_DROIT
SKIN_BOURGEON_DROITE_CENTRE_DROIT = Illustration("bourgeon_droite_centre_droit.png")
global SKIN_BOURGEON_DROITE_DROITE
SKIN_BOURGEON_DROITE_DROITE = Illustration("bourgeon_droite_droite.png")
global SKIN_BOURGEON_DROITE_LOIN_DROIT
SKIN_BOURGEON_DROITE_LOIN_DROIT = Illustration("bourgeon_droite_loin_droit.png")
global SKIN_BOURGEON_DROITE_EXTREME_DROITE
SKIN_BOURGEON_DROITE_EXTREME_DROITE = Illustration("bourgeon_droite_extreme_droite.png")
global SKIN_BOURGEONS
SKIN_BOURGEONS = Illustration("bourgeons.png")
global SKIN_BOURGEON_PHYSIQUE
SKIN_BOURGEON_PHYSIQUE = Illustration("bourgeon_physique.png")
global SKIN_BOURGEON_MAGIQUE
SKIN_BOURGEON_MAGIQUE = Illustration("bourgeon_magique.png")
global SKIN_FEUILLE_DROITE
SKIN_FEUILLE_DROITE = Illustration("feuille_droite.png")
global SKIN_FEUILLE_DROITE_PAR_DEFAUT
SKIN_FEUILLE_DROITE_PAR_DEFAUT = Illustration("feuille_droite_par_defaut.png")
global SKIN_FEUILLE_GAUCHE
SKIN_FEUILLE_GAUCHE = Illustration("feuille_gauche.png")
global SKIN_FEUILLE_GAUCHE_PAR_DEFAUT
SKIN_FEUILLE_GAUCHE_PAR_DEFAUT = Illustration("feuille_gauche_par_defaut.png")
global SKIN_FEUILLE_PHYSIQUE
SKIN_FEUILLE_PHYSIQUE = Illustration("feuille_physique.png")
global SKIN_FEUILLE_PHYSIQUE_PAR_DEFAUT
SKIN_FEUILLE_PHYSIQUE_PAR_DEFAUT = Illustration("feuille_physique_par_defaut.png")
global SKIN_FEUILLE_MAGIE
SKIN_FEUILLE_MAGIE = Illustration("feuille_magie.png")
global SKIN_FEUILLE_DEFENSE
SKIN_FEUILLE_DEFENSE = Illustration("feuille_defense.png")
global SKIN_FEUILLE_DEFENSE_PAR_DEFAUT
SKIN_FEUILLE_DEFENSE_PAR_DEFAUT = Illustration("feuille_defense_par_defaut.png")
global SKIN_FEUILLE_LANCER
SKIN_FEUILLE_LANCER = Illustration("feuille_lancer.png")
global SKIN_FEUILLE_ESSENCE_MAGIQUE
SKIN_FEUILLE_ESSENCE_MAGIQUE = Illustration("feuille_essence_magique.png")
global SKIN_FEUILLE_MAGIE_INFINIE
SKIN_FEUILLE_MAGIE_INFINIE = Illustration("feuille_magie_infinie.png")
global SKIN_FEUILLE_MAGIE_INFINIE_PAR_DEFAUT
SKIN_FEUILLE_MAGIE_INFINIE_PAR_DEFAUT = Illustration("feuille_magie_infinie_par_defaut.png")
global SKIN_RACINE_CLASSIQUE
SKIN_RACINE_CLASSIQUE = Illustration("racine.png")
global SKIN_RACINE_ELEMENTS
SKIN_RACINE_ELEMENTS = Illustration("racine_elementale.png")
global SKIN_BOURGEONS_TERRE
SKIN_BOURGEONS_TERRE = SKIN_VIDE
global SKIN_BOURGEON_TERRE_AFF
SKIN_BOURGEON_TERRE_AFF = SKIN_VIDE
global SKIN_BOURGEON_TERRE_MAGIE
SKIN_BOURGEON_TERRE_MAGIE = SKIN_VIDE
global SKIN_BOURGEON_TERRE_REAFF
SKIN_BOURGEON_TERRE_REAFF = SKIN_VIDE
global SKIN_BOURGEON_TERRE_REMAGIE
SKIN_BOURGEON_TERRE_REMAGIE = SKIN_VIDE
global SKIN_BOURGEON_TERRE_ELEM_AFF
SKIN_BOURGEON_TERRE_ELEM_AFF = SKIN_VIDE
global SKIN_BOURGEON_TERRE_ELEM_MAGIE
SKIN_BOURGEON_TERRE_ELEM_MAGIE = SKIN_VIDE
global SKIN_TERRE_COMPLET_AFF
SKIN_TERRE_COMPLET_AFF = SKIN_VIDE
global SKIN_TERRE_COMPLET_MAGIE
SKIN_TERRE_COMPLET_MAGIE = SKIN_VIDE
global SKIN_TERRE_QUASI_COMPLET_AFF
SKIN_TERRE_QUASI_COMPLET_AFF = SKIN_VIDE
global SKIN_TERRE_QUASI_COMPLET_MAGIE
SKIN_TERRE_QUASI_COMPLET_MAGIE = SKIN_VIDE
global SKIN_TERRE_AURA_AFF
SKIN_TERRE_AURA_AFF = SKIN_VIDE
global SKIN_TERRE_AURA_MAGIE
SKIN_TERRE_AURA_MAGIE = SKIN_VIDE
global SKIN_TERRE_AFF
SKIN_TERRE_AFF = SKIN_VIDE
global SKIN_TERRE_MAGIE
SKIN_TERRE_MAGIE = SKIN_VIDE
global SKIN_TERRE_VIDE
SKIN_TERRE_VIDE = SKIN_VIDE
global SKIN_BOURGEONS_FEU
SKIN_BOURGEONS_FEU = SKIN_VIDE
global SKIN_BOURGEON_FEU_AFF
SKIN_BOURGEON_FEU_AFF = SKIN_VIDE
global SKIN_BOURGEON_FEU_MAGIE
SKIN_BOURGEON_FEU_MAGIE = SKIN_VIDE
global SKIN_BOURGEON_FEU_REAFF
SKIN_BOURGEON_FEU_REAFF = SKIN_VIDE
global SKIN_BOURGEON_FEU_REMAGIE
SKIN_BOURGEON_FEU_REMAGIE = SKIN_VIDE
global SKIN_BOURGEON_FEU_ELEM_AFF
SKIN_BOURGEON_FEU_ELEM_AFF = SKIN_VIDE
global SKIN_BOURGEON_FEU_ELEM_MAGIE
SKIN_BOURGEON_FEU_ELEM_MAGIE = SKIN_VIDE
global SKIN_FEU_COMPLET_AFF
SKIN_FEU_COMPLET_AFF = SKIN_VIDE
global SKIN_FEU_COMPLET_MAGIE
SKIN_FEU_COMPLET_MAGIE = SKIN_VIDE
global SKIN_FEU_QUASI_COMPLET_AFF
SKIN_FEU_QUASI_COMPLET_AFF = SKIN_VIDE
global SKIN_FEU_QUASI_COMPLET_MAGIE
SKIN_FEU_QUASI_COMPLET_MAGIE = SKIN_VIDE
global SKIN_FEU_AURA_AFF
SKIN_FEU_AURA_AFF = SKIN_VIDE
global SKIN_FEU_AURA_MAGIE
SKIN_FEU_AURA_MAGIE = SKIN_VIDE
global SKIN_FEU_AFF
SKIN_FEU_AFF = SKIN_VIDE
global SKIN_FEU_MAGIE
SKIN_FEU_MAGIE = SKIN_VIDE
global SKIN_FEU_VIDE
SKIN_FEU_VIDE = SKIN_VIDE
global SKIN_BOURGEONS_GLACE
SKIN_BOURGEONS_GLACE = SKIN_VIDE
global SKIN_BOURGEON_GLACE_AFF
SKIN_BOURGEON_GLACE_AFF = SKIN_VIDE
global SKIN_BOURGEON_GLACE_MAGIE
SKIN_BOURGEON_GLACE_MAGIE = SKIN_VIDE
global SKIN_BOURGEON_GLACE_REAFF
SKIN_BOURGEON_GLACE_REAFF = SKIN_VIDE
global SKIN_BOURGEON_GLACE_REMAGIE
SKIN_BOURGEON_GLACE_REMAGIE = SKIN_VIDE
global SKIN_BOURGEON_GLACE_ELEM_AFF
SKIN_BOURGEON_GLACE_ELEM_AFF = SKIN_VIDE
global SKIN_BOURGEON_GLACE_ELEM_MAGIE
SKIN_BOURGEON_GLACE_ELEM_MAGIE = SKIN_VIDE
global SKIN_GLACE_COMPLET_AFF
SKIN_GLACE_COMPLET_AFF = SKIN_VIDE
global SKIN_GLACE_COMPLET_MAGIE
SKIN_GLACE_COMPLET_MAGIE = SKIN_VIDE
global SKIN_GLACE_QUASI_COMPLET_AFF
SKIN_GLACE_QUASI_COMPLET_AFF = SKIN_VIDE
global SKIN_GLACE_QUASI_COMPLET_MAGIE
SKIN_GLACE_QUASI_COMPLET_MAGIE = SKIN_VIDE
global SKIN_GLACE_AURA_AFF
SKIN_GLACE_AURA_AFF = SKIN_VIDE
global SKIN_GLACE_AURA_MAGIE
SKIN_GLACE_AURA_MAGIE = SKIN_VIDE
global SKIN_GLACE_AFF
SKIN_GLACE_AFF = SKIN_VIDE
global SKIN_GLACE_MAGIE
SKIN_GLACE_MAGIE = SKIN_VIDE
global SKIN_GLACE_VIDE
SKIN_GLACE_VIDE = SKIN_VIDE
global SKIN_BOURGEONS_OMBRE
SKIN_BOURGEONS_OMBRE = SKIN_VIDE
global SKIN_BOURGEON_OMBRE_AFF
SKIN_BOURGEON_OMBRE_AFF = SKIN_VIDE
global SKIN_BOURGEON_OMBRE_MAGIE
SKIN_BOURGEON_OMBRE_MAGIE = SKIN_VIDE
global SKIN_BOURGEON_OMBRE_REAFF
SKIN_BOURGEON_OMBRE_REAFF = SKIN_VIDE
global SKIN_BOURGEON_OMBRE_REMAGIE
SKIN_BOURGEON_OMBRE_REMAGIE = SKIN_VIDE
global SKIN_BOURGEON_OMBRE_ELEM_AFF
SKIN_BOURGEON_OMBRE_ELEM_AFF = SKIN_VIDE
global SKIN_BOURGEON_OMBRE_ELEM_MAGIE
SKIN_BOURGEON_OMBRE_ELEM_MAGIE = SKIN_VIDE
global SKIN_OMBRE_COMPLET_AFF
SKIN_OMBRE_COMPLET_AFF = SKIN_VIDE
global SKIN_OMBRE_COMPLET_MAGIE
SKIN_OMBRE_COMPLET_MAGIE = SKIN_VIDE
global SKIN_OMBRE_QUASI_COMPLET_AFF
SKIN_OMBRE_QUASI_COMPLET_AFF = SKIN_VIDE
global SKIN_OMBRE_QUASI_COMPLET_MAGIE
SKIN_OMBRE_QUASI_COMPLET_MAGIE = SKIN_VIDE
global SKIN_OMBRE_AURA_AFF
SKIN_OMBRE_AURA_AFF = SKIN_VIDE
global SKIN_OMBRE_AURA_MAGIE
SKIN_OMBRE_AURA_MAGIE = SKIN_VIDE
global SKIN_OMBRE_AFF
SKIN_OMBRE_AFF = SKIN_VIDE
global SKIN_OMBRE_MAGIE
SKIN_OMBRE_MAGIE = SKIN_VIDE
global SKIN_OMBRE_VIDE
SKIN_OMBRE_VIDE = SKIN_VIDE
