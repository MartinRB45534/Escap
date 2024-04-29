"""
Contient les classes mères des skills
"""

from __future__ import annotations

from ...commons import TypesCompetencesGeneriques, TypesCompetencesArmes, TypesCompetencesElements, TypesCompetencesIntraseques, TypesCompetencesIntrasequesArmes, TypesCompetencesIntrasequesElements, Element, CategoriesArmes

class Skill:
    """Les skills se répartissent en plusieurs catégories."""
    propagation: float
    gain_xp: float
    def __init__(self):
        self.niveau = 1
        self.xp_new: float = 0

    def gagne_xp(self):
        """Propage l'xp accumulé au cours du tour vers la classe mère"""
        res = self.xp_new*self.propagation
        self.xp_new=0
        return res

class SkillIntrasec(Skill):
    """
    Les skills intrinsèques sont des skills qui sont liés à une classe. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    niveau_min: int

class SkillIntrasecGenerique(SkillIntrasec):
    """
    Les skills intrinsèques génériques sont des skills qui sont liés à une classe. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    type_competence: TypesCompetencesIntraseques

class SkillIntrasecElement(SkillIntrasec):
    """
    Les skills intrinsèques élémentaires sont des skills qui sont liés à une classe et à un élément. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    element: Element
    type_competence: TypesCompetencesIntrasequesElements

class SkillIntrasecArme(SkillIntrasec):
    """
    Les skills intrinsèques d'arme sont des skills qui sont liés à une classe et à une arme. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    arme: CategoriesArmes
    type_competence: TypesCompetencesIntrasequesArmes

class SkillExtra(Skill):
    """
    Les skills extrinsèques sont indépendants de la classe. Ils évoluent selon leur propre utilisation, et peuvent changer de classe.
    """
    conditions_evo: list[float|bool]
    def __init__(self):
        Skill.__init__(self)
        self.xp: float = 0

    def gagne_xp(self):
        """Propage l'xp accumulé au cours du tour vers la classe mère, et en garde une partie pour lui-même."""
        res = self.xp_new * self.propagation
        self.xp += self.xp_new
        self.xp_new = 0
        if self.check_evo():
            self.evo()
        return res

    def check_evo(self):
        """Vérifie que les conditions d'évolution sont vérifiées - procède à l'évolution le cas échéant."""
        condition = self.conditions_evo[self.niveau-1]
        if isinstance(condition, bool):
            return condition
        return self.xp >= condition
    
    def evo(self):
        """Procède à l'évolution du skill."""
        self.niveau += 1

class SkillExtraGenerique(SkillExtra):
    """
    Les skills extrinsèques génériques sont des skills qui sont liés à une classe. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    type_competence: TypesCompetencesGeneriques

class SkillExtraElement(SkillExtra):
    """
    Les skills extrinsèques élémentaires sont des skills qui sont liés à une classe et à un élément. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    element: Element
    type_competence: TypesCompetencesElements

class SkillExtraArme(SkillExtra):
    """
    Les skills extrinsèques d'arme sont des skills qui sont liés à une classe et à une arme. Ils évoluent avec la classe (pas d'xp propre donc).
    """
    arme: CategoriesArmes
    type_competence: TypesCompetencesArmes
