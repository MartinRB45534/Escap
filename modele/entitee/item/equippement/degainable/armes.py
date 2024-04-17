"""
Ce fichier contient les classes des armes dégainables.
"""

from __future__ import annotations

# Imports des classes parentes
from .degainable import Arme
from ..role import EquippementTribal

class Lance(Arme):
    """Une lance. Interagit différemment avec certains skills."""

class Epee(Arme):
    """Une épée. Interagit différemment avec certains skills."""

class ArmeTribale(Arme, EquippementTribal):
    """Une arme tribale. Réduit ses statistiques si l'espèce n'est pas la bonne."""

class LanceTribale(ArmeTribale):
    """Une lance tribale. Interagit différemment avec certains skills. Réduit ses statistiques si l'espèce n'est pas la bonne."""

class EpeeTribale(ArmeTribale):
    """Une épée tribale. Interagit différemment avec certains skills. Réduit ses statistiques si l'espèce n'est pas la bonne."""

armes: dict[tuple[str, bool], type[Arme]] = {
    ("Lance", False): Lance,
    ("Epee", False): Epee,
    ("Autre", False): Arme,
    ("Lance", True): LanceTribale,
    ("Epee", True): EpeeTribale,
    ("Autre", True): ArmeTribale,
}
"""
nom de l'arme -> classe de l'arme
"""
