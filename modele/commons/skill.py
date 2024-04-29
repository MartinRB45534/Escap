"""
Ce fichier contient les énumérations des compétences.
"""

from enum import StrEnum

class TypesCompetences(StrEnum):
    """Enumération des types de compétences."""

class TypesCompetencesGeneriques(TypesCompetences):
    """Enumération des types de compétences génériques (un joueur ne peut jamais en avoir plusieurs d'un même type simultanément)."""
    OFFENSIF = "Offensif"
    PROJECTILE = "Projectile"
    MAGIQUE = "Magique"
    VOL = "Vol" # Voler des items
    BLOQUE = "Bloque" # Bloquer des attaques avec un bouclier
    ALCHIMIE = "Alchimie"
    PERSEVERANCE = "Perseverance" # Ou essence magique
    IMMORTEL = "Immortel"
    MAGIE_INFINIE = "Magie infinie"
    ECRASEMENT = "Ecrasement"
    OBSERVATION = "Observation"
    DEFENSE = "Defense"
    FORCE = "Force"
    VISION = "Vision"
    PV = "PV"
    PM = "PM"
    VITESSE = "Vitesse"
    AFFINITES = "Affinites"
    STATS = "Stats"
    AURA_INSTAKILL = "Aura instakill"

class TypesCompetencesArmes(TypesCompetences):
    """Enumération des types de compétences d'armes (un joueur ne peut jamais en avoir plusieurs d'un même type et de même arme simultanément)."""
    OFFENSIF = "Offensif"

class TypesCompetencesElements(TypesCompetences):
    """Enumération des types de compétences élémentaires (un joueur ne peut jamais en avoir plusieurs d'un même type et de même élément simultanément)."""
    AFFINITE = "Affinite"
    AURA = "Aura"

class TypesCompetencesIntraseques(StrEnum):
    """Enumération des types de compétences intrinsèques génériques."""

class TypesCompetencesIntrasequesGeneriques(TypesCompetencesIntraseques):
    """Enumération des types de compétences intrinsèques (un joueur ne peut jamais en avoir plusieurs d'un même type simultanément)."""
    DEPLACEMENT = "Deplacement"
    RAMASSE = "Ramasse"
    VISION = "Vision"
    MANIPULATION_BOUCLIER = "Manipulation bouclier"

class TypesCompetencesIntrasequesArmes(TypesCompetencesIntraseques):
    """Enumération des types de compétences intrinsèques d'armes (un joueur ne peut jamais en avoir plusieurs d'un même type et de même arme simultanément)."""
    MANIPULATION_ARME = "Manipulation arme"

class TypesCompetencesIntrasequesElements(TypesCompetencesIntraseques):
    """Enumération des types de compétences intrinsèques élémentaires (un joueur ne peut jamais en avoir plusieurs d'un même type et de même élément simultanément)."""
    IMMUNITE = "Immunité"
