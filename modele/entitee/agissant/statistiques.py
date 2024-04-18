"""
Contient la classe Statistiques.
"""

# TODO : Les statistiques devraient aussi dépendre des skills

from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des valeurs par défaut des paramètres
from ...commons.elements import Element

from ..item.equippement.role.elementaires import Elementaire
from ..item.equippement.role.accelerateur import Accelerateur
from ..item.equippement.role.anoblisseur import Anoblisseur
from ..item.equippement.role.reparateur.reparateur import Reparateur
from ..item.equippement.role.reparateur_magique.reparateur_magique import ReparateurMagique
from ...effet import EffetForce, EffetAffinite, EffetVision, EffetPv, EffetPm, EffetVitesse, Maladie, FamilleMaladie, EffetNonContagieux, EffetNonInfectable, EffetNonAffecte

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .agissant import Agissant

class Statistiques:
    """Les statistiques d'un agissant."""
    def __init__(self,possesseur:Agissant, priorite:float, vitesse:float, force:float, pv:float, regen_pv_max:float, regen_pv_min:float, restauration_regen_pv:float, pm:float, regen_pm:float, affinites:dict[Element,float], immunites:set[Element], non_contagieux:dict[str,float], non_infectable:dict[str,float], non_affecte:dict[str,float]):
        self.possesseur = possesseur #Entité possédant ces statistiques (utilisé pour chercher des effets par exemple)

        self.priorite = priorite #La priorité sert à bloquer ou forcer certaines actions (ex: le vol, l'instakill, etc.)

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

        self.non_contagieux = non_contagieux #Maladies qui ne peuvent pas être transmises
        self.non_infectable = non_infectable #Maladies qui ne peuvent pas être attrapées
        self.non_affecte = non_affecte #Maladies qui n'ont pas d'effet sur l'agissant

    def get_vitesse(self) -> float:
        """Retourne la vitesse de l'agissant."""
        vitesse = self.vitesse
        for item in self.possesseur.equipement:
            if isinstance(item, Accelerateur):
                vitesse = item.augmente_vitesse(vitesse) # Les modifications peuvent être additives ou multiplicatives ou quoi que ce soit d'autre, ce n'est pas notre problème
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetVitesse):
                vitesse = effet.modifie_vitesse(vitesse)
        return vitesse

    def get_force(self) -> float:
        """Retourne la force de l'agissant."""
        force = self.force
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetForce):
                force = effet.modifie_force(force)
        return force

    def get_affinite(self, element:Element) -> float:
        """Retourne l'affinité de l'agissant pour l'élément donné."""
        affinite = self.affinites[element]
        for item in self.possesseur.equipement:
            if isinstance(item, Elementaire) and item.element == element:
                affinite = item.augmente_affinite(affinite)
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetAffinite) and effet.element == element:
                affinite = effet.modifie_affinite(affinite)
        return affinite

    def get_priorite(self) -> float:
        """Retourne la priorité de l'agissant."""
        priorite = self.priorite
        for item in self.possesseur.equipement:
            if isinstance(item, Anoblisseur):
                priorite = item.augmente_priorite(priorite)
        return priorite

    def get_vision(self) -> float:
        """Retourne la vision de l'agissant."""
        skill = self.possesseur.get_skill_vision()
        vision = skill.portee
        vision *= self.possesseur.affinite(Element.OMBRE) # La vision est augmentée par l'affinité à l'ombre
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetVision):
                vision = effet.modifie_vision(vision)
        return vision

    def get_regen_pv(self) -> float:
        """Retourne la régénération de points de vie de l'agissant."""
        regen_pv = self.regen_pv
        for item in self.possesseur.equipement:
            if isinstance(item, Reparateur):
                regen_pv = item.regen_pv(regen_pv)
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetPv):
                regen_pv = effet.modifie_pv(regen_pv)
        return regen_pv

    def get_regen_pm(self) -> float:
        """Retourne la régénération de points de magie de l'agissant."""
        regen_pm = self.regen_pm
        for item in self.possesseur.equipement:
            if isinstance(item, ReparateurMagique):
                regen_pm = item.regen_pm(regen_pm)
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetPm):
                regen_pm = effet.modifie_pm(regen_pm)
        return regen_pm
    
    def get_non_contagieux(self, maladie:type[Maladie]) -> float:
        """Retourne la priorité de l'immunité à la contagion de la maladie donnée."""
        priorite = max(self.non_contagieux.get(maladie.nom, 0), self.non_contagieux.get(maladie.famille.nom, 0))
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetNonContagieux):
                if effet.maladie == maladie or effet.maladie == maladie.famille:
                    priorite = max(priorite, effet.priorite)
        return priorite
    
    def get_non_infectable(self, maladie:type[Maladie]) -> float:
        """Retourne la priorité de l'immunité à l'infection de la maladie donnée."""
        priorite = max(self.non_infectable.get(maladie.nom, 0), self.non_infectable.get(maladie.famille.nom, 0))
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetNonInfectable):
                if effet.maladie == maladie or effet.maladie == maladie.famille:
                    priorite = max(priorite, effet.priorite)
        return priorite
    
    def get_non_affecte(self, maladie:type[Maladie]) -> float:
        """Retourne la priorité de l'immunité à l'effet de la maladie donnée."""
        priorite = max(self.non_affecte.get(maladie.nom, 0), self.non_affecte.get(maladie.famille.nom, 0))
        for effet in self.possesseur.effets:
            if isinstance(effet, EffetNonAffecte):
                if effet.maladie == maladie or effet.maladie == maladie.famille:
                    priorite = max(priorite, effet.priorite)
        return priorite
    
    def set_non_contagieux(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        """Définit la priorité de l'immunité à la contagion de la maladie donnée."""
        if priorite > self.non_contagieux.get(maladie.nom, 0):
            self.non_contagieux[maladie.nom] = priorite

    def set_non_infectable(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        """Définit la priorité de l'immunité à l'infection de la maladie donnée."""
        if priorite > self.non_infectable.get(maladie.nom, 0):
            self.non_infectable[maladie.nom] = priorite

    def set_non_affecte(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        """Définit la priorité de l'immunité à l'effet de la maladie donnée."""
        if priorite > self.non_affecte.get(maladie.nom, 0):
            self.non_affecte[maladie.nom] = priorite

    def augmente_non_contagieux(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        """Augmente la priorité de l'immunité à la contagion de la maladie donnée."""
        self.set_non_contagieux(maladie, self.non_contagieux.get(maladie.nom, 0) + priorite)

    def augmente_non_infectable(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        """Augmente la priorité de l'immunité à l'infection de la maladie donnée."""
        self.set_non_infectable(maladie, self.non_infectable.get(maladie.nom, 0) + priorite)

    def augmente_non_affecte(self, maladie:type[Maladie]|FamilleMaladie, priorite:float):
        """Augmente la priorité de l'immunité à l'effet de la maladie donnée."""
        self.set_non_affecte(maladie, self.non_affecte.get(maladie.nom, 0) + priorite)

    def soigne(self, pv:float):
        """Soigne l'agissant de pv points de vie."""
        self.pv += pv
        self.pv = min(self.pv, self.pv_max)

    def blesse(self, pv:float):
        """Blesse l'agissant de pv points de vie."""
        self.pv -= pv
        self.regen_pv = self.regen_pv_min

    def debut_tour(self):
        """L'agissant commence son tour."""
        self.pv += self.get_regen_pv()
        self.pv = min(self.pv, self.pv_max)
        self.regen_pv += self.restauration_regen_pv
        self.regen_pv = min(self.regen_pv, self.regen_pv_max)
        self.pm += self.get_regen_pm()
        self.pm = min(self.pm, self.pm_max)

    def depense_pm(self, pm:float):
        """L'agissant dépense pm points de magie."""
        self.pm -= pm
