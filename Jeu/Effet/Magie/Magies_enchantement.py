from __future__ import annotations
from typing import TYPE_CHECKING

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports des classes parentes
from Jeu.Effet.Magie.Magie import Enchante_agissant, Enchante_item

class Magie_enchantement_faiblesse(Enchante_agissant):
    """La magie qui place un enchantement de faiblesse sur un agissant."""
    nom = "magie faiblesse"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_faiblesse[niveau-1]
        self.cout_pm = cout_pm_faiblesse[niveau-1]
        self.latence = latence_faiblesse[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_force(duree_faiblesse[self.niveau-1],gain_force_faiblesse[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_FAIBLESSE

    def get_titre(self,observation=0):
        return f"Enchantement de faiblesse (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de faiblesse réduit la force de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Réduction de la force : {gain_force_faiblesse[self.niveau-1]}",f"Durée de l'enchantement : {duree_faiblesse[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_cecite(Enchante_agissant):
    """La magie qui place un enchantement de cécité sur un agissant."""
    nom = "magie cecite"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_cecite[niveau-1]
        self.cout_pm = cout_pm_cecite[niveau-1]
        self.latence = latence_cecite[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_vision(duree_cecite[self.niveau-1],gain_vision_cecite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_CECITE

    def get_titre(self,observation=0):
        return f"Enchantement de cécité (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de cécité réduit la portée de la vision de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Réduction de la vision : {gain_vision_cecite[self.niveau-1]}",f"Durée de l'enchantement : {duree_cecite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_perte_de_pv(Enchante_agissant):
    """La magie qui place un enchantement de perte de pv sur un agissant."""
    nom = "magie perte de pv"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_perte_de_pv[niveau-1]
        self.cout_pm = cout_pm_perte_de_pv[niveau-1]
        self.latence = latence_perte_de_pv[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_pv(duree_perte_de_pv[self.niveau-1],gain_pv_perte_de_pv[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PV

    def get_titre(self,observation=0):
        return f"Enchantement de perte de PVs (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de perte de PVs retire des PVs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PVs perdus par tour : {gain_pv_perte_de_pv[self.niveau-1]}",f"Durée de l'enchantement : {duree_perte_de_pv[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_perte_de_pm(Enchante_agissant):
    """La magie qui place un enchantement de perte de pm sur un agissant."""
    nom = "magie perte de pm"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_perte_de_pm[niveau-1]
        self.cout_pm = cout_pm_perte_de_pm[niveau-1]
        self.latence = latence_perte_de_pm[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_pm(duree_perte_de_pm[self.niveau-1],gain_pm_perte_de_pm[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_PERTE_DE_PM

    def get_titre(self,observation=0):
        return f"Enchantement de perte de PMs (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de perte de PMs retire des PMs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PMs perdus par tour : {gain_pm_perte_de_pm[self.niveau-1]}",f"Durée de l'enchantement : {duree_perte_de_pm[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_confusion(Enchante_agissant):
    """La magie qui place un enchantement de confusion sur un agissant."""
    nom = "magie confusion"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_confusion[niveau-1]
        self.cout_pm = cout_pm_confusion[niveau-1]
        self.latence = latence_confusion[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_confusion(duree_confusion[self.niveau-1],taux_erreur_confusion[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_CONFUSION

    def get_titre(self,observation=0):
        return f"Enchantement de confusion (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de confusion pousse l'agissant à se tromper parfois de direction pour une certaine durée.","L'enchantement ne choisi pas la plus mauvaise direction, mais se contente de modifier la direction de l'agissant, l'agissant peut être quand-même efficace.",f"Coût : {self.cout_pm} PMs",f"Probabilité de se tromper de direction : {taux_erreur_confusion[self.niveau-1]}",f"Durée de l'enchantement : {duree_confusion[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_poches_trouees(Enchante_agissant):
    """La magie qui place un enchantement de poches trouees sur un agissant."""
    nom = "magie poches trouees"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_poches_trouees[niveau-1]
        self.cout_pm = cout_pm_poches_trouees[niveau-1]
        self.latence = latence_poches_trouees[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_poches_trouees(duree_poches_trouees[self.niveau-1],taux_drop_poches_trouees[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_POCHES_TROUEES

    def get_titre(self,observation=0):
        return f"Enchantement de poches trouées (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de poches trouées pousse l'agissant à laisser parfois tomber des items de son inventaire pour une certaine durée.","L'item laché est choisi aléatoirement, et peut faire partie de l'équippement de l'agissant.",f"Coût : {self.cout_pm} PMs",f"Probabilité de laisser tomber un item : {taux_drop_poches_trouees[self.niveau-1]}",f"Durée de l'enchantement : {duree_poches_trouees[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_force(Enchante_agissant):
    """La magie qui place un enchantement de force sur un agissant."""
    nom = "magie force"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_force[niveau-1]
        self.cout_pm = cout_pm_force[niveau-1]
        self.latence = latence_force[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_force(duree_force[self.niveau-1],gain_force[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_FORCE

    def get_titre(self,observation=0):
        return f"Enchantement de force (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de force augmente la force de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la force : {gain_force[self.niveau-1]}",f"Durée de l'enchantement : {duree_force[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_vision(Enchante_agissant):
    """La magie qui place un enchantement de vision sur un agissant."""
    nom = "magie vision"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_vision[niveau-1]
        self.cout_pm = cout_pm_vision[niveau-1]
        self.latence = latence_vision[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_vision(duree_vision[self.niveau-1],gain_vision[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_VISION

    def get_titre(self,observation=0):
        return f"Enchantement de vision (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de vision augmente la portée de la vision de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la vision : {gain_vision[self.niveau-1]}",f"Durée de l'enchantement : {duree_vision[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_vitalite(Enchante_agissant):
    """La magie qui place un enchantement de vitalité sur un agissant."""
    nom = "magie vitalite"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_vitalite[niveau-1]
        self.cout_pm = cout_pm_vitalite[niveau-1]
        self.latence = latence_vitalite[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_pv(duree_vitalite[self.niveau-1],gain_pv_vitalite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_VITALITE

    def get_titre(self,observation=0):
        return f"Enchantement de vitalité (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de vitalité donne des PVs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PVs gagnés par tour : {gain_pv_vitalite[self.niveau-1]}",f"Durée de l'enchantement : {duree_vitalite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_absorption(Enchante_agissant):
    """La magie qui place un enchantement d'absorption sur un agissant."""
    nom = "magie absorption"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_absorption[niveau-1]
        self.cout_pm = cout_pm_absorption[niveau-1]
        self.latence = latence_absorption[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_pm(duree_absorption[self.niveau-1],gain_pm_absorption[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_ABSORPTION

    def get_titre(self,observation=0):
        return f"Enchantement d'absorption (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement d'absorption donne des PMs à l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"PMs gagnés par tour : {gain_pm_absorption[self.niveau-1]}",f"Durée de l'enchantement : {duree_absorption[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_celerite(Enchante_agissant):
    """La magie qui place un enchantement de célérité sur un agissant."""
    nom = "magie celerite"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_celerite[niveau-1]
        self.cout_pm = cout_pm_celerite[niveau-1]
        self.latence = latence_celerite[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_vitesse(duree_celerite[self.niveau-1],gain_vitesse_celerite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_CELERITE

    def get_titre(self,observation=0):
        return f"Enchantement de célérité (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de célérité augmente la vitesse (le taux de diminution de la latence) de l'agissant à chaque tour pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la vitesse : {gain_vitesse_celerite[self.niveau-1]}",f"Durée de l'enchantement : {duree_celerite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_immunite(Enchante_agissant):
    """La magie qui place un enchantement d'immunité sur un agissant."""
    nom = "magie immunite"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_immunite[niveau-1]
        self.cout_pm = cout_pm_immunite[niveau-1]
        self.latence = latence_immunite[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_immunite(duree_immunite[self.niveau-1],superiorite_immunite[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_IMMUNITE

    def get_titre(self,observation=0):
        return f"Enchantement d'immunité (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement d'immunité retire les maladies de l'agissant à chaque tour pour une certaine durée.","Le retrait peut échouer si la priorité de la maladie est trop grande par rapport à celle de l'agissant.",f"Coût : {self.cout_pm} PMs",f"Différence de priorité : {superiorite_immunite[self.niveau-1]}",f"Durée de l'enchantement : {duree_immunite[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_flamme(Enchante_agissant):
    """La magie qui place un enchantement de flamme sur un agissant."""
    nom = "magie flamme"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_flamme[niveau-1]
        self.cout_pm = cout_pm_flamme[niveau-1]
        self.latence = latence_flamme[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_flamme(duree_flamme[self.niveau-1],gain_affinite_flamme[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_FLAMME

    def get_titre(self,observation=0):
        return f"Enchantement de flamme (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de flamme augmente l'affinité au feu de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_flamme[self.niveau-1]}",f"Durée de l'enchantement : {duree_flamme[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_neige(Enchante_agissant):
    """La magie qui place un enchantement de neige sur un agissant."""
    nom = "magie neige"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_neige[niveau-1]
        self.cout_pm = cout_pm_neige[niveau-1]
        self.latence = latence_neige[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_neige(duree_neige[self.niveau-1],gain_affinite_neige[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_NEIGE

    def get_titre(self,observation=0):
        return f"Enchantement de neige (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de neige augmente l'affinité à la glace de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_neige[self.niveau-1]}",f"Durée de l'enchantement : {duree_neige[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_sable(Enchante_agissant):
    """La magie qui place un enchantement de sable sur un agissant."""
    nom = "magie sable"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_sable[niveau-1]
        self.cout_pm = cout_pm_sable[niveau-1]
        self.latence = latence_sable[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_sable(duree_sable[self.niveau-1],gain_affinite_sable[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_SABLE

    def get_titre(self,observation=0):
        return f"Enchantement de sable (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de sable augmente l'affinité à la terre de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_sable[self.niveau-1]}",f"Durée de l'enchantement : {duree_sable[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_tenebre(Enchante_agissant):
    """La magie qui place un enchantement de ténèbre sur un agissant."""
    nom = "magie tenebre"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_tenebre[niveau-1]
        self.cout_pm = cout_pm_tenebre[niveau-1]
        self.latence = latence_tenebre[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Agissant] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_tenebre(duree_tenebre[self.niveau-1],gain_affinite_tenebre[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_TENEBRE

    def get_titre(self,observation=0):
        return f"Enchantement de ténèbre (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un agissant à proximité du lanceur.","L'enchantement de ténèbre augmente l'affinité à l'ombre de l'agissant pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Gain d'affinité : {gain_affinite_tenebre[self.niveau-1]}",f"Durée de l'enchantement : {duree_tenebre[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_rouille(Enchante_item): #Il faudrait cibler un item visible, équippé par un agissant proche
    """La magie qui place un enchantement de rouille sur un item."""
    nom = "magie rouille"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_rouille[niveau-1]
        self.cout_pm = cout_pm_rouille[niveau-1]
        self.latence = latence_rouille[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Item] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_arme(duree_rouille[self.niveau-1],gain_force_rouille[self.niveau-1],gain_portee_rouille[self.niveau-1])) #Comment affecter aussi les autres types d'équippement ?

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_ROUILLE

    def get_titre(self,observation=0):
        return f"Enchantement de rouille (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un item à proximité du lanceur.","L'enchantement de rouille diminue l'efficacité de l'item pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Réduction de la force (pour une arme) : {gain_force_rouille[self.niveau-1]}",f"Réduction de la portee (pour une arme) : {gain_portee_rouille[self.niveau-1]}",f"Durée de l'enchantement : {duree_rouille[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_renforcement(Enchante_item):
    """La magie qui place un enchantement de renforcement sur un item."""
    nom = "magie renforcement"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_renforcement[niveau-1]
        self.cout_pm = cout_pm_renforcement[niveau-1]
        self.latence = latence_renforcement[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Item] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_arme(duree_renforcement[self.niveau-1],gain_force_renforcement[self.niveau-1],gain_portee_renforcement[self.niveau-1]))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT

    def get_titre(self,observation=0):
        return f"Enchantement de renforcement (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un item à proximité du lanceur.","L'enchantement de renforcement augmente l'efficacité de l'item pour une certaine durée.",f"Coût : {self.cout_pm} PMs",f"Augmentation de la force (pour une arme) : {gain_force_renforcement[self.niveau-1]}",f"Augmentation de la portee (pour une arme) : {gain_portee_renforcement[self.niveau-1]}",f"Durée de l'enchantement : {duree_renforcement[self.niveau-1]}",f"Latence : {self.latence}"]

class Magie_enchantement_bombe(Enchante_item):
    """La magie qui place un enchantement de bombe sur un item."""
    nom = "magie bombe"
    def __init__(self,niveau:int):
        self.phase = "démarrage"
        self.gain_xp = gain_xp_bombe[niveau-1]
        self.cout_pm = cout_pm_bombe[niveau-1]
        self.latence = latence_bombe[niveau-1]
        self.niveau = niveau
        self.cible:Optional[Item] = None
        self.temps = 10000
        self.affiche = True

    def action(self,porteur:Agissant):
        assert self.cible is not None
        self.cible.effets.append(Enchantement_bombe(duree_bombe[self.niveau-1],On_hit(portee_bombe[self.niveau-1],degats_bombe[self.niveau-1])))

    def get_image(self):
        return SKIN_MAGIE_ENCHANTEMENT_BOMBE

    def get_titre(self,observation=0):
        return f"Enchantement de bombe (niveau {self.niveau})"

    def get_description(self,observation=0):
        return ["Un enchantement","Affecte un item à proximité du lanceur.","L'enchantement de bombe confère un effet explosif à l'item pour une certaine durée (s'il est lancé, il explose au contact d'un agissant ou d'un mur et inflige des dégats de terre aux agissants à proximité).",f"Coût : {self.cout_pm} PMs",f"Dégats de l'explosion : {degats_bombe[self.niveau-1]}",f"Portee de l'explosion : {portee_bombe[self.niveau-1]}",f"Durée de l'enchantement : {duree_bombe[self.niveau-1]}",f"Latence : {self.latence}"]

# Imports utilisés dans le code
from Jeu.Effet.Enchantements import *
from Jeu.Effet.Effets_items import On_hit
from Jeu.Systeme.Constantes_magies.Magies import *
from Affichage.Skins.Skins import SKIN_MAGIE_ENCHANTEMENT_BOMBE,SKIN_MAGIE_ENCHANTEMENT_RENFORCEMENT,SKIN_MAGIE_ENCHANTEMENT_ROUILLE