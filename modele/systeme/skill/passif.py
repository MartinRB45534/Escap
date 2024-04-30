from __future__ import annotations
from typing import TYPE_CHECKING

# Imports des classes parentes
from .skill import Skill, SkillExtra, SkillIntrasec ,SkillGenerique, SkillElement, SkillArme
from ...commons import TypesCompetencesGeneriques, TypesCompetencesElements, CategoriesArmes

# Variables de classe

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...commons import Element
    from ...effet import Aura, AttaqueParticulier
    from ...entitee import Arme, Bouclier

class Passif(Skill):
    """
    Les skills qui se déclenchent automatiquement.
    """
    def utilise(self):
        """Méthode qui est appelée à chaque fois que le skill est utilisé."""
        self.xp_new+=self.gain_xp

class SkillVision(Passif, SkillIntrasecGenerique):
    """Le skill utilisé pour observer son environnement. Lorsqu'il augmente de niveau, on peut voir plus loin. C'est un skill intrasec à la classe principale. !!!Ne pas confondre avec observation, qui permet d'obtenir des informations sur ce que l'on voit.!!!
       C'est un skill semi-passif, qui s'actionne à chaque tour."""
    type_competence = TypesCompetencesIntrasequesGeneriques.VISION
    portee:list[float]
    def get_portee(self) -> float:
        """Renvoie la portée de vision du joueur."""
        self.utilise()
        return self.portee[self.niveau - 1]

class SkillAura(Passif): # TODO : Se décider pour les auras
    """Offre une aura qui se matérialise autour de l'agissant. Les effets de l'aura diffèrent selon l'aura. Skill aura est une classe parente et ne doit pas être instanciée.
       Les auras sont des skills passifs, qui s'actionne à chaque tour."""
    aura:type[Aura]

    def get_aura(self) -> type[Aura]:
        """Renvoie l'effet de l'aura."""
        self.utilise()
        return self.aura

class SkillEssenceMagique(Passif, SkillExtraGenerique):
    """Ce skill permet d'utiliser les PM comme deuxième barre de PV si les PV sont à 0. Inspiré du skill persévérance dans komu desu ga, nanika ? et point de départ de l'une des quatre branches d'évolution du joueur.
       C'est un skill semi-passif, qui s'actionne quand on a des PV négatifs après avoir reçu des dégats (presque comme un sort de soin instantanné automatique)."""
    type_competence = TypesCompetencesGeneriques.PERSEVERANCE
    taux:list[float]
    def get_taux(self) -> float:
        """Renvoie le taux de conversion des PM en PV."""
        self.utilise()
        return self.taux[self.niveau - 1]

class SkillImmortel(Passif, SkillExtraGenerique):
    """ 'évolution' du skill précédent essence magique. Permet de survivre avec - de 0 PV, sans perdre de PM, mais avec une réduction de toutes les stats (possibilité de choisir entre les deux skills ?).
       C'est un skill semi-passif, qui s'actionne quand on a des PV négatifs à la fin du tour (la présence du skill suffit au controleur, mais il sera quand même "utilisé" pour qu'il puisse gagner son xp) (son coefficient sera extrait directement, sans procédure, pour éviter de lui faire gagner des xp à chaque fois qu'une valeur est utilisée)."""
    type_competence = TypesCompetencesGeneriques.IMMORTEL
    taux:list[float]
    def get_taux(self) -> float:
        """Renvoie le taux de réduction des stats."""
        self.utilise()
        return self.taux[self.niveau - 1]

class SkillMagieInfinie(Passif, SkillExtraGenerique):
    """L'opposé de l'essence magique, permet de consommer plus de mana qu'on en possède, avec des PM qui deviennent négatifs. Pour chaque PM en dessous de 0, la régénération des PV est réduite d'autant, elle peut devenir négative.
       C'est un skill semi-passif, qui s'actionne quand l'agissant a des PM négatifs à la fin du tour (la présence du skill suffit au controleur pour autoriser des sorts même s'il n'y a pas assez de mana, le skill n'est "utilisé" que pour calculer la régén des PV une fois par tour)."""
    type_competence = TypesCompetencesGeneriques.MAGIE_INFINIE
    taux:list[float]
    def get_taux(self) -> float:
        """Renvoie le taux de réduction de la régénération des PV."""
        self.utilise()
        return self.taux[self.niveau - 1]

class SkillManipulationArme(Passif, SkillIntrasecArme):
    """
    Renforce les attaques réalisées à l'aide d'armes. Il y a un skill par type d'arme, et on peut en avoir plusieurs. Les skills sont cumulatifs, mais ne s'appliquent qu'à une seule arme à la fois.
    """
    arme:CategoriesArmes
    type_competence = TypesCompetencesIntrasequesArmes.MANIPULATION_ARME
    taux_stats:list[float]
    def boost_stats(self, arme:Arme):
        """Booste les stats de l'arme."""
        if arme.categorie == self.arme:
            arme.taux_stats["skill manip"] = self.taux_stats[self.niveau - 1]
            self.utilise()

class SkillManipulationBouclier(Passif, SkillIntrasecGenerique):
    """Renforce la défense des items de type bouclier. Quand le niveau augmente, les dégats bloqués avec un bouclier, la portée des boucliers (pour un bouclier, la portée permet de protéger une plus grande zone), la vitesse d'utilisation des boucliers, la priorité des boucliers, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois que le skill de bloquage d'attaque est utilisé."""
    type_competence = TypesCompetencesIntrasequesGeneriques.MANIPULATION_BOUCLIER
    taux_stats:list[float]
    def boost_stats(self, bouclier:Bouclier):
        """Booste les stats du bouclier."""
        bouclier.taux_stats["skill manip"] = self.taux_stats[self.niveau - 1]
        self.utilise()

class SkillEcrasement(Passif, SkillExtraGenerique):
    """Permet d'écraser (détruire) d'autres agissants ou des murs sur son chemin. Plus le niveau est élevé, moins la différence de priorité entre l'écrseur et l'écrasé doit être élevée pour permettre l'écrasement.
       C'est un skill semi-passif, qui s'actionne quand il y a collision entre l'agissant et un autre agissant ou un mur."""
    type_competence = TypesCompetencesGeneriques.ECRASEMENT
    superiorite:list[float]
    def ecrase(self,priorite_ecrase:float,priorite_ecrasant:float):
        """Renvoie si l'écrasement a fonctionné."""
        fonctionne = priorite_ecrase + self.superiorite[self.niveau - 1] < priorite_ecrasant
        if fonctionne :
            self.utilise()
        return fonctionne

class SkillObservation(Passif, SkillExtraGenerique):
    """Complément du skill de vision. Permet d'afficher des informations sur ce que voit le skill de vision (PV d'un ennemi ou priorité d'un mur par exemple). Peut aussi rendre visible (certains sorts, objets ou ennemis furtifs par exemple) ou révéler la vraie forme (certains ennemis portent plusieurs couches de déguisements, et le skill d'observation peut donc révéler une fausse forme différente de la forme affichée sans le skill).
       C'est un skill passif, qui s'actionne à chaque tour, après le skill vision. Il renvoit uniquement son niveau, et tous les objets ont différentes informations à afficher selon le niveau de l'observation (faire intervenir la priorité dans le calcul !)."""
    type_competence = TypesCompetencesGeneriques.OBSERVATION
    # TODO : Penser à ce skill

class SkillDefense(Passif, SkillExtraGenerique):
    """Absorbe une partie des dégats infligés à l'agissant. La proportion de dégats bloqués augmente avec le niveau.
       C'est un skill semi-passif, il est activé à chaque fois que des dégats sont infligés à l'agissant."""
    type_competence = TypesCompetencesGeneriques.DEFENSE
    taux_degats:list[float]
    def intercepte(self,attaque:AttaqueParticulier):
        """Intercepte l'attaque. (Devrait en réduire les dégats.)"""
        degats_bloques = self.taux_degats[self.niveau - 1]
        attaque.degats *= (1-degats_bloques)
        self.utilise()

class SkillStatForce(Passif, SkillExtraGenerique):
    """Les skills qui augmentent la force de l'agissant."""
    type_competence = TypesCompetencesGeneriques.FORCE
    def modifie_force(self, force:float) -> float:
        """Modifie la stat force de l'agissant."""
        raise NotImplementedError
    
class SkillStatVision(Passif, SkillExtraGenerique):
    """Les skills qui augmentent la vision de l'agissant."""
    type_competence = TypesCompetencesGeneriques.VISION
    def modifie_vision(self, vision:float) -> float:
        """Modifie la stat vision de l'agissant."""
        raise NotImplementedError
    
class SkillStatPv(Passif, SkillExtraGenerique):
    """Les skills qui augmentent la régénération des PV de l'agissant."""
    type_competence = TypesCompetencesGeneriques.PV
    def modifie_pv(self, pv:float) -> float:
        """Modifie la stat pv de l'agissant."""
        raise NotImplementedError
    
class SkillStatPm(Passif, SkillExtraGenerique):
    """Les skills qui augmentent la régénération des PM de l'agissant."""
    type_competence = TypesCompetencesGeneriques.PM
    def modifie_pm(self, pm:float) -> float:
        """Modifie la stat pm de l'agissant."""
        raise NotImplementedError
    
class SkillStatVitesse(Passif, SkillExtraGenerique):
    """Les skills qui augmentent la vitesse de l'agissant."""
    type_competence = TypesCompetencesGeneriques.VITESSE
    def modifie_vitesse(self, vitesse:float) -> float:
        """Modifie la stat vitesse de l'agissant."""
        raise NotImplementedError

class SkillStatAffinite(Passif, SkillExtraElement):
    """Augmente l'affinité avec un élément. Une affinité élevée augmente les dégats infligés et diminue les dégats subits par le biais d'attaques de cet élément, réduit les coups de mana et les temps de latence des sorts de cet élément, etc. et une affinité faible a l'effet inverse. Les quatre stats d'affinité sont très légèrement affectées par les actions du joueur tout au long du jeu, et grandement affectées par les skills d'affinité.
       C'est un skill-passif (il est appelé une fois par tour pour déterminer les affinités effectives du joueur pour le tour."""
    type_competence = TypesCompetencesElements.AFFINITE
    element:Element
    def modifie_affinite(self, affinite:float) -> float:
        """Modifie l'affinité à l'élément de l'agissant."""
        raise NotImplementedError
    
class SkillStatAffinites(Passif, SkillExtraGenerique):
    """Les skills qui augmentent les affinités de l'agissant."""
    type_competence = TypesCompetencesGeneriques.AFFINITES
    def modifie_affinites(self, affinite:float, element:Element) -> float:
        """Modifie les affinités de l'agissant."""
        raise NotImplementedError
    
class SkillStatStats(Passif, SkillExtraGenerique):
    """Les skills qui augmentent les stats de l'agissant."""
    type_competence = TypesCompetencesGeneriques.STATS
    def modifie_stats(self, stats:dict[str, float]) -> dict[str, float]:
        """Modifie les stats de l'agissant."""
        raise NotImplementedError

class SkillImmunite(Passif, SkillIntrasecElement):
    """Les skills qui immunisent l'agissant contre un élément."""
    type_competence = TypesCompetencesIntrasequesElements.IMMUNITE
    element:Element
