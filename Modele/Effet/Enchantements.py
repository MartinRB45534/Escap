from __future__ import annotations
from typing import TYPE_CHECKING
import carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..entitee.agissant.agissant import Agissant
    from ..entitee.item.item import Item
    from ..entitee.item.equippement.degainable.degainable import Arme

# Imports des classes parentes
from .effet import Enchantement, OnDebutTour, OnPostDecision
from .effets_items import OnHit
from .effets_agissants import EffetForce, EffetVision, EffetPv, EffetPm, EffetVitesse, EffetAffinite

# Imports des valeurs par défaut des paramètres
from ..systeme.elements import Element

class EnchantementForce(Enchantement,OnDebutTour,EffetForce):
    """Les enchantements qui affectent la force (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_force:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_force = gain_force

    def action(self,agissant:Agissant):
        pass

    def modifie_force(self, force:float) -> float:
        return force + self.gain_force

class EnchantementVision(Enchantement,OnDebutTour,EffetVision):
    """Les enchantements qui affectent le champ de vision (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_vision:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vision = gain_vision

    def action(self,agissant:Agissant):
        pass

    def modifie_vision(self, vision:float) -> float:
        return vision + self.gain_vision

class EnchantementPv(Enchantement,OnDebutTour,EffetPv):
    """Les enchantements qui affectent la régénération des PV (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_pv:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pv = gain_pv

    def action(self,agissant:Agissant):
        pass

    def modifie_pv(self, pv:float) -> float:
        return pv + self.gain_pv

class EnchantementPm(Enchantement,OnDebutTour,EffetPm):
    """Les enchantements qui affectent la régénération des PM (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_pm:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pm = gain_pm

    def action(self,agissant:Agissant):
        pass

    def modifie_pm(self, pm:float) -> float:
        return pm + self.gain_pm

class EnchantementConfusion(Enchantement,OnPostDecision):
    """Les enchantements qui provoque des erreurs de direction."""
    def __init__(self,temps_restant:float,taux_erreur:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_erreur = taux_erreur

    def action(self,agissant:Agissant):
        if self.phase == "en cours":
            if isinstance(agissant.action, Deplace) :
                dir_voulue = agissant.action.direction
                if random.random() < self.taux_erreur and dir_voulue is not None:
                    dir_possibles = [dir for dir in crt.Direction if dir is not dir_voulue]
                    agissant.action.direction = random.choice(dir_possibles)

    def execute(self,agissant:Agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class EnchantementPochesTrouees(Enchantement,OnDebutTour):
    """Les enchantements qui fait droper des items involontairement."""
    def __init__(self,temps_restant:float,taux_drop:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_drop = taux_drop

    def action(self,agissant:Agissant):
        if self.phase == "en cours":
            if random.random() < self.taux_drop :
                agissant.inventaire.drop_random(agissant.labyrinthe.position_case[agissant.position])

    def execute(self,agissant:Agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class EnchantementVitesse(Enchantement,OnDebutTour,EffetVitesse):
    """Les enchantements qui affectent la vitesse (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_vitesse:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vitesse = gain_vitesse

    def action(self,agissant:Agissant):
        pass

    def modifie_vitesse(self, vitesse:float) -> float:
        return vitesse + self.gain_vitesse

class EnchantementImmunite(Enchantement,OnDebutTour):
    """Enchantement qui confère une immunité aux maladies, à condition de disposer de suffisamment de priorité."""
    def __init__(self,temps_restant:float,superiorite:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.superiorite = superiorite

    def action(self,agissant:Agissant):
        if self.phase == "en cours":
            for effet in agissant.effets :
                if isinstance(effet,Maladie):
                    if effet.virulence + self.superiorite < agissant.priorite :
                        effet.phase = "terminé"
                        effet.action(agissant)
                        agissant.effets.remove(effet)

    def execute(self,agissant:Agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class EnchantementFlamme(Enchantement,OnDebutTour,EffetAffinite):
    """Enchantement qui augmente l'affinité à l'élément feu."""
    element = Element.FEU
    def __init__(self,temps_restant:float,gain_aff:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        pass

    def modifie_affinite(self, affinite:float) -> float:
        return affinite + self.gain_aff

class EnchantementNeige(Enchantement,OnDebutTour):
    """Enchantement qui augmente l'affinité à l'élément glace."""
    element = Element.GLACE
    def __init__(self,temps_restant:float,gain_aff:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        pass

    def modifie_affinite(self, affinite:float) -> float:
        return affinite + self.gain_aff

class EnchantementSable(Enchantement,OnDebutTour):
    """Enchantement qui augmente l'affinité à l'élément terre."""
    element = Element.TERRE
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        pass

    def modifie_affinite(self, affinite:float) -> float:
        return affinite + self.gain_aff

class EnchantementTenebre(Enchantement,OnDebutTour):
    """Enchantement qui augmente l'affinité à l'élément ombre."""
    element = Element.OMBRE
    def __init__(self,temps_restant:float,gain_aff:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        pass

    def modifie_affinite(self, affinite:float) -> float:
        return affinite + self.gain_aff

class EnchantementArme(Enchantement,OnDebutTour):
    """Enchantement qui modifie les statistiques d'une arme (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_force:float,gain_portee:float):
        self.temps_restant = temps_restant
        self.affiche = False
        self.phase = "démarrage"
        self.gain_force = gain_force
        self.gain_portee = gain_portee

    def action(self,arme:Arme):
        if self.phase == "démarrage" and "enchantf" not in arme.taux_tranchant :
            arme.taux_tranchant["enchantf"] = self.gain_force
        elif self.phase == "terminé":
            arme.taux_tranchant.pop("enchantf")
        if self.phase == "démarrage" and "enchantp" not in arme.taux_portee :
            arme.taux_portee["enchantp"] = self.gain_portee
        elif self.phase == "terminé":
            arme.taux_portee.pop("enchantp")

class EnchantementBombe(Enchantement,OnDebutTour):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,temps_restant:float,effet:OnHit):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.charge = effet

    def action(self,item:Item):
        if self.phase == "démarrage" :
            item.effets.append(self.charge)
        elif self.phase == "terminé":
            item.effets.remove(self.charge)

# Imports utilisés dans le code
import random
from ..effet.sante.maladies.maladie import Maladie
from .action.deplacement import Deplace