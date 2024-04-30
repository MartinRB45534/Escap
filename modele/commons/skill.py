"""
Ce fichier contient les énumérations des compétences.
"""

from enum import StrEnum

class TypesCompetences(StrEnum):
    """Enumération des types de compétences."""

class TypesCompetencesGeneriques(TypesCompetences):
    """Enumération des types de compétences génériques (un joueur ne peut jamais en avoir plusieurs d'un même type simultanément)."""

    # Compétences actives de base
    DEPLACEMENT = "Deplacement"
    RAMASSE = "Ramasse"

    ATTAQUE = "Attaque"
    ATTAQUE_ARME = "Attaque arme" # Attaque avec une arme quelconque

    MAGIE = "Magie"

    # Compétences actives obtenables par le joueur
    BLOQUE = "Bloque" # Bloque une attaque avec un bouclier

    LANCER = "Lancer"

    VOL_ITEM = "Vol item" # Vole un item à un ennemi
    VOL_SKILL = "Vol skill" # Vole un skill à un ennemi
    VOL_MAGIE = "Vol magie" # Vole une magie à un ennemi
    VOL_STAT = "Vol stat" # Vole une statistique à un ennemi

    # Compétences passives de base
    VISION = "Vision" # Permet de percevoir le labyrinthe

    # Compétences passives obtenables par le joueur
    ECRASEMENT = "Ecrasement" # Permet d'écraser l'occupant d'une case

    PRIORITE_ECRASEMENT = "Priorite ecrasement" # Augmente la priorité d'écrasement

    PORTEE_ATTAQUE = "Portee attaque" # Augmente la portée des attaques
    DEGATS_ATTAQUE = "Degats attaque" # Augmente les dégâts des attaques
    VITESSE_ATTAQUE = "Vitesse attaque" # Augmente la vitesse des attaques

    PRIORITE_VOL = "Priorite vol" # Augmente la priorité des vols

    CREATION_PROJECTILE = "Creation projectile" # Crée un projectile

    PORTEE_PROJECTILE = "Portee projectile" # Augmente la portée des projectiles
    PORTEE_EXPLOSIF = "Portee explosif" # Augmente la portée des projectiles explosifs
    DEGATS_PROJECTILE = "Degats projectile" # Augmente les dégâts des projectiles
    VITESSE_PROJECTILE = "Vitesse projectile" # Augmente la vitesse des projectiles

    PORTEE_MAGIE = "Portee magie" # Augmente la portée des magies
    VITESSE_MAGIE = "Vitesse magie" # Augmente la vitesse des magies
    COUT_MAGIE = "Cout magie" # Diminue le coût des magies

    PORTEE_ENCHANTEMENT = "Portee enchantement" # Augmente la portée des enchantements
    VITESSE_ENCHANTEMENT = "Vitesse enchantement" # Augmente la vitesse des enchantements
    COUT_ENCHANTEMENT = "Cout enchantement" # Diminue le coût des enchantements
    DUREE_ENCHANTEMENT = "Duree enchantement" # Augmente la durée des enchantements

    AURA_DEGATS = "Aura degats" # Une aura qui inflige des dégâts
    AURA_SOIN = "Aura soin" # Une aura qui soigne les alliés
    AURA_BUFF = "Aura buff" # Une aura qui buff les alliés
    AURA_DEBUFF = "Aura debuff" # Une aura qui debuff les ennemis
    AURA_INSTAKILL = "Aura instakill" # Une aura qui tue instantanément
    AURA_REANIMATION = "Aura reanimation" # Une aura qui réanime

    PORTEE_AURA = "Portee aura" # Augmente la portée des auras
    PRIORITE_AURA = "Priorite aura" # Augmente la priorité des auras

class TypesCompetencesArmes(TypesCompetences):
    """Enumération des types de compétences d'armes (un joueur ne peut jamais en avoir plusieurs d'un même type et de même arme simultanément)."""
    # Compétences actives obtenables par le joueur
    ATTAQUE = "Attaque" # Attaque avec une arme spécifique

    # Compétences passives obtenables par le joueur
    DEGATS_ATTAQUE = "Degats attaque" # Augmente les dégâts des attaques
    VITESSE_ATTAQUE = "Vitesse attaque" # Augmente la vitesse des attaques
    PORTEE_ATTAQUE = "Portee attaque" # Augmente la portée des attaques

class TypesCompetencesElements(TypesCompetences):
    """Enumération des types de compétences élémentaires (un joueur ne peut jamais en avoir plusieurs d'un même type et de même élément simultanément)."""
    # Compétences passives obtenables par le joueur
    AFFINITE = "Affinite"
    AURA = "Aura"
