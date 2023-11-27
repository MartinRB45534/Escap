from __future__ import annotations
from typing import TYPE_CHECKING

from .classe import Classe

if TYPE_CHECKING:
    from ..skill.skill import SkillIntrasec, SkillExtra

class ClassePrincipale(Classe):
    """La classe principale de l'agissant. Le niveau d'un agissant est égal au niveau de sa classe principale. Pour les agissants capables de s'améliorer, l'utilisation de la procédure gagne_xp de la classe principale provoque récursivement l'utilisation de cette procédure sur tous les sous-classe est skills de l'agissant. L'amélioration de la classe principale provoque une amélioration des statistiques de l'agissant.
       Pour le joueur, une amélioration de la classe principale permet de choisir une récompense dans l'arbre de compétence ou dans l'arbre élémental (ou deux dans l'arbre élémental avec la classe élémentaliste)."""
    def __init__(self,cond_evo:list[float],skills_intrasecs:set[SkillIntrasec],skills:set[SkillExtra]=set(),niveau:int=1,evolutif:bool=False):
        Classe.__init__(self,cond_evo,skills_intrasecs,skills)
        self.evo(niveau)
        self.evolutif = evolutif

    def gagne_xp(self):
        if self.evolutif :
            Classe.gagne_xp(self)
        else:
            Classe.vire_xp(self)
