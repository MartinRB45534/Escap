from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Old_Jeu.Entitee.Agissant.Agissant import Agissant
    from Old_Jeu.Entitee.Item.Item import Item
    from Old_Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme
    from Old_Jeu.Labyrinthe.Structure_spatiale.Direction import Direction

# Imports des classes parentes
from Old_Jeu.Effet.Effet import Enchantement, On_debut_tour, On_post_decision
from Old_Jeu.Effet.Effets_items import On_hit

class Enchantement_force(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la force (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_force:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_force = gain_force

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_force :
            agissant.taux_force["enchantf"] = self.gain_force
        elif self.phase == "terminé":
            agissant.taux_force.pop("enchantf")

class Enchantement_vision(Enchantement,On_debut_tour):
    """Les enchantements qui affectent le champ de vision (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_vision:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vision = gain_vision

    def action(self,agissant:Agissant):
        skill = trouve_skill(agissant.classe_principale,Skill_vision)
        if skill is None:
            raise ValueError("L'agissant n'a pas de skill de vision")
        # if self.phase == "démarrage" :
        #     skill.portee += gain_vision
        # elif self.phase == "terminé":
        #     skill.portee -= gain_vision

class Enchantement_pv(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la régénération des PV (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_pv:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pv = gain_pv

    def action(self,agissant):
        if self.phase == "démarrage" :
            agissant.regen_pv += self.gain_pv
        elif self.phase == "terminé":
            agissant.regen_pv -= self.gain_pv

class Enchantement_pm(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la régénération des PM (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_pm:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_pm = gain_pm

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" :
            agissant.regen_pm += self.gain_pm
        elif self.phase == "terminé":
            agissant.regen_pm -= self.gain_pm

class Enchantement_confusion(Enchantement,On_post_decision):
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
                    dir_possibles = [Direction(i) for i in range(NB_DIRECTIONS)]
                    dir_possibles.remove(dir_voulue)
                    agissant.action.direction = random.choice(dir_possibles)

    def execute(self,agissant:Agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class Enchantement_poches_trouees(Enchantement,On_debut_tour):
    """Les enchantements qui fait droper des items involontairement."""
    def __init__(self,temps_restant:float,taux_drop:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.taux_drop = taux_drop

    def action(self,agissant:Agissant):
        if self.phase == "en cours":
            if random.random() < self.taux_drop :
                agissant.inventaire.drop_random(agissant.position)

    def execute(self,agissant:Agissant):
        self.temps_restant -= 1
        if self.phase == "démarrage" :
            self.phase = "en cours"
        elif self.temps_restant <= 0 :
            self.termine()
        else :
            self.action(agissant)

class Enchantement_vitesse(Enchantement,On_debut_tour):
    """Les enchantements qui affectent la vitesse (en positif ou négatif)."""
    def __init__(self,temps_restant:float,gain_vitesse:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_vitesse = gain_vitesse

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" and "enchantv" not in agissant.taux_vitesse :
            agissant.taux_vitesse["enchantv"] = self.gain_vitesse
        elif self.phase == "terminé":
            agissant.taux_vitesse.pop("enchantv")

class Enchantement_immunite(Enchantement,On_debut_tour):
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

class Enchantement_flamme(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément feu."""
    def __init__(self,temps_restant:float,gain_aff:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_aff_f :
            agissant.taux_aff_f["enchantf"] = self.gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_f.pop("enchantf")

class Enchantement_neige(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément glace."""
    def __init__(self,temps_restant:float,gain_aff:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" and "enchantf" not in agissant.taux_aff_g :
            agissant.taux_aff_g["enchantn"] = self.gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_g.pop("enchantn")

class Enchantement_sable(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément terre."""
    def __init__(self,temps_restant,gain_aff):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" and "enchants" not in agissant.taux_aff_t :
            agissant.taux_aff_t["enchants"] = self.gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_t.pop("enchants")

class Enchantement_tenebre(Enchantement,On_debut_tour):
    """Enchantement qui augmente l'affinité à l'élément ombre."""
    def __init__(self,temps_restant:float,gain_aff:float):
        self.affiche = False
        self.temps_restant = temps_restant
        self.phase = "démarrage"
        self.gain_aff = gain_aff

    def action(self,agissant:Agissant):
        if self.phase == "démarrage" and "enchantt" not in agissant.taux_aff_o :
            agissant.taux_aff_o["enchantt"] = self.gain_aff
        elif self.phase == "terminé":
            agissant.taux_aff_o.pop("enchantt")

class Enchantement_arme(Enchantement,On_debut_tour):
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

class Enchantement_bombe(Enchantement,On_debut_tour):
    """Enchantement qui confère des propriétés explosives à un item."""
    def __init__(self,temps_restant:float,effet:On_hit):
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
from Old_Jeu.Systeme.Constantes_magies.Magies import *
from Old_Jeu.Constantes import *
import random
from Old_Jeu.Effet.Sante.Maladies.Maladie import Maladie
from Old_Jeu.Systeme.Classe.Classes import trouve_skill
from Old_Jeu.Systeme.Skill.Skills import Skill_vision
from Old_Jeu.Action.Deplacement import Deplace