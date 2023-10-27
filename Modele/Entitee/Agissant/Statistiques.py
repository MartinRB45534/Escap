from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Set

# Imports des valeurs par défaut des paramètres
from ...commons.elements import Element

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .agissant import Agissant

class Statistiques:

    def __init__(self,possesseur:Agissant, priorite:float, vitesse:float, force:float, pv:float, regen_pv_max:float, regen_pv_min:float, restauration_regen_pv:float, pm:float = 0, regen_pm:float = 0, affinites:Dict[Element,float] = {element: 1 for element in Element}, immunites:Set[Element] = set()):
        self.possesseur = possesseur #Entité possédant ces statistiques (utilisé pour chercher des effets par exemple)

        self.priorite = priorite #La priorité sert à bloquer ou forcer certains actions (ex: le vol, l'instakill, etc.)

        self.vitesse = vitesse #Vitesse d'action (encore utilisé ?)
        self.force = force #Force d'attaques physiques

        self.pv_max = pv #Points de vie max
        self.pv = pv #Points de vie
        self.regen_pv_max = regen_pv_max #Régénération de points de vie quand on a pas pris de dégâts depuis longtemps
        self.regen_pv_min = regen_pv_min #Régénération de points de vie quand on a pris des dégâts récemment
        self.regen_pv = regen_pv_max #Régénération de points de vie actuelle
        self.restauration_regen_pv = restauration_regen_pv #Restauration de la régénération de points de vie
        self.pm_max = pm #Points de magie max
        self.pm = pm #Points de magie
        self.regen_pm = regen_pm #Régénération de points de magie

        self.affinites = affinites #Affinités élémentaires
        self.immunites = immunites #Immunites élémentaires

    def get_vitesse(self) -> float:
        vitesse = self.vitesse
        for item in self.possesseur.equipement:
            if isinstance(item, Accelerateur):
                vitesse = item.augmente_vitesse(vitesse) # Les modifications peuvent être additives ou multiplicatives ou quoi que ce soit d'autre, ce n'est pas notre problème
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetVitesse):
                vitesse = effet.modifie_vitesse(vitesse)
        return vitesse
    
    def get_force(self) -> float:
        force = self.force
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetForce):
                force = effet.modifie_force(force)
        return force
    
    def get_affinite(self, element:Element) -> float:
        affinite = self.affinites[element]
        for item in self.possesseur.equipement:
            if isinstance(item, Elementaire) and item.element == element:
                affinite = item.augmente_affinite(affinite)
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetAffinite) and effet.element == element:
                affinite = effet.modifie_affinite(affinite)
        return affinite
    
    def get_priorite(self) -> float:
        priorite = self.priorite
        for item in self.possesseur.equipement:
            if isinstance(item, Anoblisseur):
                priorite = item.augmente_priorite(priorite)
        return priorite
    
    def get_vision(self) -> float:
        skill = self.possesseur.get_skill_vision()
        vision = skill.portee
        vision *= self.possesseur.affinite(Element.OMBRE) # La vision est augmentée par l'affinité à l'ombre
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetVision):
                vision = effet.modifie_vision(vision)
        return vision
    
    def get_regen_pv(self) -> float:
        regen_pv = self.regen_pv
        for item in self.possesseur.equipement:
            if isinstance(item, Reparateur):
                regen_pv = item.regen_pv(regen_pv)
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetPv):
                regen_pv = effet.modifie_pv(regen_pv)
        return regen_pv
    
    def get_regen_pm(self) -> float:
        regen_pm = self.regen_pm
        for item in self.possesseur.equipement:
            if isinstance(item, Reparateur_magique):
                regen_pm = item.regen_pm(regen_pm)
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetPm):
                regen_pm = effet.modifie_pm(regen_pm)
        return regen_pm

    def soigne(self, pv:float):
        self.pv += pv
        self.pv = min(self.pv, self.pv_max)

    def blesse(self, pv:float):
        self.pv -= pv
        self.pv = max(self.pv, 0)
        self.regen_pv = self.regen_pv_min

    def debut_tour(self):
        self.pv += self.regen_pv
        self.pv = min(self.pv, self.pv_max)
        self.regen_pv += self.restauration_regen_pv
        self.regen_pv = min(self.regen_pv, self.regen_pv_max)
        self.pm += self.regen_pm
        self.pm = min(self.pm, self.pm_max)

    def depense_pm(self, pm:float):
        self.pm -= pm

from ..item.equippement.role.elementaires import Elementaire
from ..item.equippement.role.accelerateur import Accelerateur
from ..item.equippement.role.anoblisseur import Anoblisseur
from ..item.equippement.role.reparateur.reparateur import Reparateur
from ..item.equippement.role.reparateur_magique.reparateur_magique import Reparateur_magique
from ...effet.agissant.statistiques import EffetForce
from ...effet.agissant.statistiques import EffetAffinite
from ...effet.agissant.statistiques import EffetVision
from ...effet.agissant.statistiques import EffetPv
from ...effet.agissant.statistiques import EffetPm
from ...effet.agissant.statistiques import EffetVitesse