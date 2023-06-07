from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Labyrinthe.Structure_spatiale.Direction import Direction
    from ..Entitee.Item.Equippement.Degainable.Degainable import Arme

# Imports des classes parentes
from ..Systeme.Skill.Skill import Skill, Skill_intrasec, Skill_extra
from ..Systeme.Skill.Actif import Actif, Skill_deplacement, Skill_attaque, Skill_attaque_arme, Skills_magiques
from ..Systeme.Skill.Passif import Passif, Skill_vision

class Skill_ombriul(Skill): # Vraiment utile ?
    """Les skills des ombriuls."""
    pass

class Vision_ombriul(Skill_vision,Skill_intrasec,Skill_ombriul):
    """La vision des ombriuls."""
    def utilise(self):
        self.xp_new+=gain_xp_vision[self.niveau-1] #On gagne de l'xp !
        return portee_vision[self.niveau-1] #Pour l'instant la portée est la seule chose qu'on veut savoir

class Deplacement_ombriul(Skill_deplacement,Skill_intrasec,Skill_ombriul):
    """Le déplacement des ombriuls."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None, course=False) -> Marche:
        return Marche(agissant, latence_deplacement[self.niveau-1], self, gain_xp_deplacement[self.niveau-1], direction or agissant.dir_regard)

class Stomp_ombriul(Skill_attaque, Skill_intrasec, Skill_ombriul):
    """Le stomp des ombriuls."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None) -> Attaque_final:
        return Attaque_final(agissant, latence_stomp[self.niveau-1], self, gain_xp_stomp[self.niveau-1], taux_utilisation_stomp[self.niveau-1], direction or agissant.dir_regard, portee_stomp[self.niveau - 1])

class Attaque_ombriul(Skill_attaque_arme, Skill_intrasec, Skill_ombriul):
    """L'attaque des ombriuls."""
    def fait(self, agissant:Agissant, arme:Optional[Arme]=None, direction:Optional[Direction]=None) -> Attaque_arme_final:
        if arme is None:
            arme = agissant.inventaire.get_arme()
            assert arme is not None
        return Attaque_arme_final(agissant, latence_attaque[self.niveau-1], self, gain_xp_attaque[self.niveau-1], taux_utilisation_attaque[self.niveau-1], direction or agissant.dir_regard, arme)

class Magie_ombriul(Skills_magiques, Skill_intrasec, Skill_ombriul):
    """La magie des ombriuls."""
    def __init__(self):
        Skill.__init__(self)
        Skills_magiques.__init__(self)
        # Ajouter les magies communes aux ombriuls

# Imports utilisés dans le code
from ..Systeme.Constantes_skills.Skills import *
from ..Action.Deplacement import Marche
from ..Action.Attaque import Attaque_final, Attaque_arme_final