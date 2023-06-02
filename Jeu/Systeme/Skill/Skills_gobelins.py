from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme

# Imports des classes parentes
from Jeu.Systeme.Skill.Skill import Skill, Skill_intrasec, Skill_extra
from Jeu.Systeme.Skill.Actif import Actif, Skill_deplacement, Skill_attaque, Skill_attaque_arme, Skills_magiques
from Jeu.Systeme.Skill.Passif import Passif, Skill_vision

class Skill_gobelin(Skill): # Vraiment utile ?
    """Les skills des gobelins."""
    pass

class Vision_gobelin(Skill_vision,Skill_intrasec,Skill_gobelin):
    """La vision des gobelins."""
    def utilise(self):
        self.xp_new+=gain_xp_vision[self.niveau-1] #On gagne de l'xp !
        return portee_vision[self.niveau-1] #Pour l'instant la portée est la seule chose qu'on veut savoir

class Deplacement_gobelin(Skill_deplacement,Skill_intrasec,Skill_gobelin):
    """Le déplacement des gobelins."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None, course:bool=False) -> Marche:
        return Marche(agissant, latence_deplacement[self.niveau-1], self, gain_xp_deplacement[self.niveau-1], direction or agissant.dir_regard)

class Stomp_gobelin(Skill_attaque, Skill_intrasec, Skill_gobelin):
    """Le stomp des gobelins."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None) -> Attaque_final:
        return Attaque_final(agissant, latence_stomp[self.niveau-1], self, gain_xp_stomp[self.niveau-1], taux_utilisation_stomp[self.niveau-1], direction or agissant.dir_regard, portee_stomp[self.niveau - 1])

class Attaque_gobelin(Skill_attaque_arme, Skill_intrasec, Skill_gobelin):
    """L'attaque des gobelins."""
    def fait(self, agissant:Agissant, arme:Optional[Arme], direction:Optional[Direction]) -> Attaque_arme_final:
        if arme is None:
            arme=agissant.inventaire.get_arme()
            assert arme is not None
        return Attaque_arme_final(agissant, latence_attaque[self.niveau-1], self, gain_xp_attaque[self.niveau-1], taux_utilisation_attaque[self.niveau-1], direction or agissant.dir_regard, arme)

class Magie_gobelin(Skills_magiques, Skill_intrasec, Skill_gobelin):
    """La magie des gobelins."""
    def __init__(self):
        Skill.__init__(self)
        Skills_magiques.__init__(self)
        # Ajouter les magies communes aux gobelins

# Imports utilisés dans le code
from Jeu.Systeme.Constantes_skills.Skills import *
from Jeu.Action.Deplacement import Marche
from Jeu.Action.Attaque import Attaque_final, Attaque_arme_final