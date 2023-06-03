from __future__ import annotations
from typing import TYPE_CHECKING, Optional

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Old_Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme

# Imports des classes parentes
from Old_Jeu.Systeme.Skill.Skill import Skill, Skill_intrasec, Skill_extra
from Old_Jeu.Systeme.Skill.Actif import Actif, Skill_deplacement, Skill_ramasse, Skill_attaque, Skill_attaque_arme, Skills_magiques, Skill_alchimie
from Old_Jeu.Systeme.Skill.Passif import Passif, Skill_vision

class Skill_humain(Skill): # Vraiment utile ?
    """Les skills des humains."""
    pass

class Vision_humain(Skill_vision,Skill_intrasec,Skill_humain):
    """La vision des humains."""
    def utilise(self):
        self.xp_new+=gain_xp_vision[self.niveau-1] #On gagne de l'xp !
        return portee_vision[self.niveau-1] #Pour l'instant la portée est la seule chose qu'on veut savoir

class Deplacement_humain(Skill_deplacement,Skill_intrasec,Skill_humain):
    """Le déplacement des humains."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None, course=False) -> Marche:
        return Marche(agissant, latence_deplacement[self.niveau-1], self, gain_xp_deplacement[self.niveau-1], direction or agissant.dir_regard)
    
class Deplacement_joueur(Deplacement_humain):
    """Le déplacement du joueur."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None, course=False) -> Marche:
        if course:
            return Cours(agissant, latence_course[self.niveau-1], self, gain_xp_deplacement[self.niveau-1], direction or agissant.dir_regard)
        return Marche(agissant, latence_deplacement[self.niveau-1], self, gain_xp_deplacement[self.niveau-1], direction or agissant.dir_regard)
    
class Ramasse_humain(Skill_ramasse,Skill_intrasec,Skill_humain):
    """Le ramassage des humains."""
    def fait(self,agissant:Agissant) -> Ramasse:
        items = []
        latences = []
        xp = 0
        for item in agissant.controleur.trouve_items(agissant.position):
            if priorite_ramasse[self.niveau-1]>=item.priorite:
                items.append(item)
                latences.append(latence_ramasse[self.niveau-1])
                xp+=gain_xp_ramasse[self.niveau-1]
        return Ramasse(agissant, latences, self, xp, items)
    
class Ramasse_joueur(Ramasse_humain):
    """Le ramassage du joueur."""
    def fait(self,agissant:Agissant,light=False) -> Ramasse:
        items = []
        latences = []
        xp = 0
        for item in agissant.controleur.trouve_items(agissant.position):
            if isinstance(item, ITEMS_LIGHTS) or not light:
                if priorite_ramasse[self.niveau-1]>=item.priorite:
                    items.append(item)
                    latences.append(latence_ramasse[self.niveau-1])
                    xp+=gain_xp_ramasse[self.niveau-1]
        return Ramasse(agissant, latences, self, xp, items)
    
class Stomp_humain(Skill_attaque, Skill_extra, Skill_humain):
    """Le stomp des humains."""
    def fait(self, agissant:Agissant, direction:Optional[Direction]=None) -> Attaque_final:
        return Attaque_final(agissant, latence_stomp[self.niveau-1], self, gain_xp_stomp[self.niveau-1], taux_utilisation_stomp[self.niveau-1], direction or agissant.dir_regard, portee_stomp[self.niveau - 1])

class Attaque_humain(Skill_attaque_arme, Skill_extra, Skill_humain):
    """L'attaque des humains."""
    def fait(self, agissant:Agissant, arme:Optional[Arme]=None, direction:Optional[Direction]=None) -> Attaque_arme_final:
        if arme is None:
            arme = agissant.inventaire.get_arme()
            assert arme is not None
        return Attaque_arme_final(agissant, latence_attaque[self.niveau-1], self, gain_xp_attaque[self.niveau-1], taux_utilisation_attaque[self.niveau-1], direction or agissant.dir_regard, arme)

class Magie_humain(Skills_magiques, Skill_extra, Skill_humain):
    """La magie des humains."""
    def __init__(self):
        Skill.__init__(self)
        Skills_magiques.__init__(self)
        # Ajouter les magies communes aux humains

class Alchimie_humain(Skill_alchimie, Skill_extra, Skill_humain):
    """L'alchimie des humains."""
    def __init__(self):
        Skill_alchimie.__init__(self)

    # def fait(self, agissant: Agissant, recette: str) -> Alchimie:
    #     if recette not in self.recettes:
    #         raise ValueError("La recette n'est pas dans les recettes disponibles.")
    #     recette = self.recettes[recette]
    #     return Alchimie(agissant, latence_alchimie[self.niveau-1], self, gain_xp_alchimie[self.niveau-1], recette)

# Imports utilisés dans le code
from Old_Jeu.Systeme.Constantes_skills.Skills import *
from Old_Jeu.Action.Deplacement import Marche, Cours
from Old_Jeu.Action.Action_skill import Alchimie, Ramasse
from Old_Jeu.Action.Attaque import Attaque_final, Attaque_arme_final
from Old_Jeu.Entitee.Item.Items import ITEMS_LIGHTS