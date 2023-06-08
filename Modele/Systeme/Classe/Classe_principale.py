from __future__ import annotations
from typing import TYPE_CHECKING, Set, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Skill.Skill import Skill_intrasec, Skill_extra

# Imports des classes parentes
from .Classe import Classe

class Classe_principale(Classe):
    """La classe principale de l'agissant. Le niveau d'un agissant est égal au niveau de sa classe principale. Pour les agissants capables de s'améliorer, l'utilisation de la procédure gagne_xp de la classe principale provoque récursivement l'utilisation de cette procédure sur tous les sous-classe est skills de l'agissant. L'amélioration de la classe principale provoque une amélioration des statistiques de l'agissant.
       Pour le joueur, une amélioration de la classe principale permet de choisir une récompense dans l'arbre de compétence ou dans l'arbre élémental (ou deux dans l'arbre élémental avec la classe élémentaliste)."""
    def __init__(self,cond_evo:List,skills_intrasecs:Set[Skill_intrasec],skills:Set[Skill_extra]=set(),niveau:int=1,evolutif:bool=False):
        Classe.__init__(self,cond_evo,skills_intrasecs,skills)
        self.evo(niveau)
        self.evolutif = evolutif

    def gagne_xp(self):
        if self.evolutif :
            Classe.gagne_xp(self)
        else:
            Classe.vire_xp(self)
