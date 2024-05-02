from __future__ import annotations
from typing import TYPE_CHECKING, Any
from modele.action import ActionSkill

# Imports des classes parentes
from .skill import Skill

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...action import Magie, ActionSkill, DerobeItem, DerobeSkill, DerobeStat, DerobeMagie, Blocage, Alchimie, Attaque, AttaqueArme, Marche, Ramasse, LancerItem

class Actif(Skill):
    """
    Les skills qui genèrent les actions.
    """
    def fait(self, nom:str="") -> type[ActionSkill]:
        """Fait l'action"""
        raise NotImplementedError

class SkillDeplacement(Actif):
    """
    Un skill qui permet de se déplacer vers une case adjacente.
    """
    deplacements: list[dict[str, type[Marche]]]
    def fait(self, nom:str="") -> type[Marche]:
        """Fait le déplacement"""
        return self.deplacements[self.niveau - 1][nom]

class SkillRamasse(Actif):
    """
    Un skill qui permet de ramasser des objets sur sa case.
    """
    ramasses: list[dict[str, type[Ramasse]]]
    def fait(self, nom:str="") -> type[Ramasse]:
        """Fait le ramassage"""
        return self.ramasses[self.niveau - 1][nom]

class SkillAttaque(Actif):
    """
    Un skill qui genère une attaque (hors attaque magique).
    """
    attaques: list[dict[str, type[Attaque]]]
    def fait(self, nom:str="") -> type[Attaque]:
        """Fait l'attaque"""
        return self.attaques[self.niveau - 1][nom]

class SkillAttaqueArme(Actif):
    """
    Un skill qui genère une attaque (hors attaque magique) avec une arme.
    """
    attaques: list[dict[str, type[AttaqueArme]]]
    def fait(self, nom:str="") -> type[AttaqueArme]:
        """Fait l'attaque"""
        return self.attaques[self.niveau - 1][nom]

class SkillMagie(Actif):
    """
    Un skill qui permet de lancer des magies.
    """
    magies: list[dict[str, type[Magie]]]
    def fait(self, nom:str="") -> type[Magie]:
        """Fait la magie"""
        return self.magies[self.niveau - 1][nom]

class SkillLancer(Actif):
    """
    Un skill qui lance un objet.
    """
    lancers: list[dict[str, type[LancerItem]]]
    def fait(self, nom:str="") -> type[LancerItem]:
        """Utilise le skill, et renvoie l'objet lancé"""
        return self.lancers[self.niveau - 1][nom]

class SkillVolItem(Actif):
    """
    Un skill qui permet de voler un objet à un autre agissant.
    """
    derobes: list[dict[str, type[DerobeItem]]]
    def fait(self, nom:str="") -> type[DerobeItem]:
        """Fait le dérobage"""
        return self.derobes[self.niveau - 1][nom]

class SkillVolMagie(Actif):
    """
    Un skill qui permet de voler une magie à un autre agissant.
    """
    derobes: list[dict[str, type[DerobeMagie]]]
    def fait(self, nom:str="") -> type[DerobeMagie]:
        """Fait le dérobage"""
        return self.derobes[self.niveau - 1][nom]

class SkillVolStat(Actif):
    """
    Un skill qui permet de voler une statistique à un autre agissant.
    """
    derobes: list[dict[str, type[DerobeStat]]]
    def fait(self, nom:str="") -> type[DerobeStat]:
        """Fait le dérobage"""
        return self.derobes[self.niveau - 1][nom]

class SkillVolSkill(Actif):
    """
    Un skill qui permet de voler un skill à un autre agissant.
    """
    derobes: list[dict[str, type[DerobeSkill]]]
    def fait(self, nom:str="") -> type[DerobeSkill]:
        """Fait le dérobage"""
        return self.derobes[self.niveau - 1][nom]
    
class SkillBlocage(Actif):
    """
    Un skill qui permet de bloquer les attaques avec un bouclier.
    """
    blocages: list[dict[str, type[Blocage]]]
    def fait(self, nom:str="") -> type[Blocage]:
        """Fait le blocage"""
        return self.blocages[self.niveau - 1][nom]
    
class SkillAlchimie(Actif):
    """
    Un skill qui permet de fabriquer des objets.
    """
    alchimies: list[dict[str, type[Alchimie]]]
    def fait(self, nom:str="") -> type[Alchimie]:
        """Fait l'alchimie"""
        return self.alchimies[self.niveau - 1][nom]

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
    def __equal__(self, other: Any):
        return isinstance(other, SkillIssue)

    def fait(self, nom:str="") -> type[ActionSkill]:
        """Fait l'action"""
        raise NotImplementedError

SKILL_ISSUE = SkillIssue()
