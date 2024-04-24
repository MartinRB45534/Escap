from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import carte as crt
from modele.action import ActionSkill

# Imports des classes parentes
from .skill import Skill

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...entitee import Agissant, Arme
    from ...action import Magie, ActionSkill, Derobe, Blocage, Alchimie, Attaque, AttaqueArme, Marche, Ramasse, LancerItem

class Actif(Skill):
    """
    Les skills qui genèrent les actions.
    """
    def fait(self) -> type[ActionSkill]:
        """Fait l'action"""
        raise NotImplementedError

class SkillsOffensifs(Actif):
    """
    Un skill qui genère une attaque (hors attaque magique).
    """
    def fait(self) -> type[Attaque]:
        """Fait l'attaque"""
        raise NotImplementedError

class SkillsProjectiles(Actif):
    """
    Un skill qui lance un objet.
    """

    def fait(self) -> type[LancerItem]:
        """Utilise le skill, et renvoie l'objet lancé"""
        raise NotImplementedError

class SkillsMagiques(Actif):
    """
    Un skill qui permet de lancer des magies.
    """
    def fait(self) -> type[Magie]:
        """Fait la magie"""
        raise NotImplementedError

class SkillDeplacement(Actif):
    """
    Un skill qui permet de se déplacer vers une case adjacente.
    """
    def fait(self) -> type[Marche]:
        """Fait le déplacement"""
        raise NotImplementedError

class SkillRamasse(Actif):
    """
    Un skill qui permet de ramasser des objets sur sa case.
    """
    def fait(self) -> type[Ramasse]:
        """Fait le ramassage"""
        raise NotImplementedError

# TODO : réfléchir aux skills des slimes
# class SkillMerge(Actif):
#     """
#     Un skill qui permet à deux groupes de fusionner. Unique aux slimes.
#     """
#     def __init__(self):
#         Actif.__init__(self)
#         self.nom="Fusion de slimes"

#     # /!\ À compléter

# class SkillAbsorb(Actif):
#     """Un skill qui permet d'absorber un cadavre (le ramasser et récupérer un skill). Unique aux slimes."""
#     def __init__(self):
#         Actif.__init__(self)
#         self.nom="Absorption de cadavre"

# class SkillDivide(Actif):
#     """Un skill qui permet à un agissant de se séparer en deux. Unique aux slimes."""
#     def __init__(self):
#         Actif.__init__(self)
#         self.nom="Division"

class SkillIssue(Actif):
    """The absence of a skill."""
    def __equal__(self, other:Any):
        return isinstance(other, SkillIssue)

SKILL_ISSUE = SkillIssue()
