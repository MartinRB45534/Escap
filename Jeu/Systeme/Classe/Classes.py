from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar, Optional, Type

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Systeme.Skill.Skill import Skill

# Imports des classes parentes
from Jeu.Systeme.Classe.Classe import Classe

# class Artificier(Classe):
#     """La classe des utilisateurs d'explosifs de haut niveau. Le skill de création d'explosif peut lui être transféré. La classe apporte des bonus lors de l'utilisation d'explosifs."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         creation_explo = Skill_creation_d_explosifs()
#         lancer = Skill_lancer()
#         skills:List[Skill] = [lancer,creation_explo] #Les skills sont au niveau 0, ainsi le controleur proposera de les réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_explosifs()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         cad_evo = [[],[],[],[],[],[],[],[],[],[]] #Rajouter des explosifs

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills,cad_evo)

#         self.nom = "Artificier"

# class Archer(Classe):
#     """La classe des utilisateurs de flèches de haut niveau. Le skill de création de flèches peut lui être transféré. La classe apporte des bonus lors de l'utilisation de flèches."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         creation_fleches = Skill_creation_de_fleches()
#         lancer = Skill_lancer()
#         skills:List[Skill] = [lancer,creation_fleches] #Les skills sont au niveau 0, ainsi le controleur proposera de les réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_fleches()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         cad_evo = [[],[],[],[],[],[],[],[],[],[]] #Rajouter des flèches

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills,cad_evo)

#         self.nom = "Archer"

# class Sniper(Classe):
#     """La classe des utilisateurs de flèches de très haut niveau. Le skill de création de flèches peut lui être transféré. La classe apporte des bonus lors de l'utilisation de flèches."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         creation_fleches = Skill_creation_de_fleches()
#         lancer = Skill_lancer() #Peut-être le remplacer par une version plus puissante, mais lente ?
#         skills:List[Skill] = [lancer,creation_fleches] #Les skills sont au niveau 0, ainsi le controleur proposera de les réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_fleches_sniper()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         cad_evo = [[],[],[],[],[],[],[],[],[],[]] #Rajouter des flèches

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills,cad_evo)

#         self.nom = "Sniper"

# class Epeiste(Classe):
#     """La classe des utilisateurs d'épées. Le skill de manipulation d'épée ou le skill de manipulation d'armes peut lui être transféré. La classe apporte des bonus lors de l'utilisation d'épées (pour l'instant juste des dégats)"""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         epee = Skill_manipulation_epee()
#         arme = Skill_manipulation_arme()
#         skills:List[Skill] = [epee,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_epee()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Epéiste"

# class Lancier(Classe):
#     """La classe des utilisateurs de lances. Le skill de manipulation de lance ou le skill de manipulation d'armes peut lui être transféré. La classe apporte des bonus lors de l'utilisation de lances (pour l'instant juste des dégats)"""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         lance = Skill_manipulation_lance()
#         arme = Skill_manipulation_arme()
#         skills:List[Skill] = [lance,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_lance()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Lancier"

# class Porteur_de_bouclier(Classe):
#     """La classe des utilisateurs de boucliers. Le skill de manipulation de bouclier ou le skill de manipulation d'armes peut lui être transféré. La classe apporte des bonus lors de l'utilisation de boucliers (pour l'instant juste des dégats bloqués en plus)"""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         bouclier = Skill_manipulation_bouclier()
#         arme = Skill_manipulation_arme()
#         skills:List[Skill] = [bouclier,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_bouclier()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Porteur_de_bouclier"

# class Homme_d_arme(Classe):
#     """La classe des utilisateurs d'arme. Les skill de manipulation d'épée, de lance et de bouclier ou le skill de manipulation d'armes peuvent lui être transféré. La classe apporte des bonus lors de l'utilisation d'armes (pour l'instant juste des dégats supplémentaires/ dégats bloqués en plus)"""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         epee = Skill_manipulation_epee()
#         lance = Skill_manipulation_lance()
#         bouclier = Skill_manipulation_bouclier()
#         arme = Skill_manipulation_arme()
#         skills:List[Skill] = [epee,lance,bouclier,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

#         boosts = Skill_boost_armes()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Homme d'armes"

# class Enchanteur(Classe):
#     """La classe des utilisateurs d'enchantements. Améliore l'efficacité des enchantements."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         boosts = Skill_boost_enchantements()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs)

#         self.nom = "Enchanteur"

# class Soutien(Classe):
#     """La classe des soutiens (par opposition aux tanks et aux dps). Boost les sorts de soutien (buff et soin des alliés, débuff des ennemis)."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

#         boosts = Skill_boost_soutien()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs)

#         self.nom = "Soutien"

# class Ange(Classe):
#     """La classe des soutiens de haut niveau. Offre des skills (donc sans coût de mana) équivalents aux sorts de soutien classiques (débuffs exclus). Réduit drastiquement le temps nécessaire pour lancer les sorts de soutien classiques (débuffs exclus)."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre des bonnes actions (soin, résurection, etc.) en guise de conditions ?

#         boost = Skill_boost_ange()
#         soin = Skill_soin()
#         regen_MP = Skill_regeneration_MP()
#         aura = Skill_aura_divine(None) #/*\ À adapter /*\

#         skills_intrasecs:List[Skill_intrasec] = [boost,soin,regen_MP,aura]

#         Classe.__init__(self,cond_evo,skills_intrasecs)

#         self.nom = "Ange"

# class Elementaliste(Classe):
#     """La classe des élémentalistes. Boost légèrement les affinités élémentales, renforce légèrement les skills et classes venues de l'arbe des éléments, permet de sélectionner deux feuilles de l'arbre des éléments par niveauau lieu d'une."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre la possession de classes d'élémental comme condition des niveaux 4,7 et 10 (respectivement 1, 2 et 3 classes) ?

#         skills:List[Skill] = []
#         for element in []: #remplacer par les éléments quand je les aurai créés, ainsi que les effets
#             skills.append(Skill_aura_elementale(element))
#             skills.append(Skill_affinite_elementale(element))

#         boosts = Skill_boost_elementaliste()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Elémentaliste"

# class Elemental(Classe):
#     """Le classe des élémentaux. Les skills d'aura élémentale et d'affinité élémentale peuvent lui être transférés."""
#     pass

# class Elemental_de_terre(Elemental):
#     """La classe des élémentaux de terre."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         skills:List[Skill] = []

#         boosts = Skill_boost_elemental_terre()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Elémental_de_terre"

# class Elemental_de_feu(Elemental):
#     """La classe des élémentaux de feu."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         skills:List[Skill] = []

#         boosts = Skill_boost_elemental_feu()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Elémental_de_feu"

# class Elemental_de_glace(Elemental):
#     """La classe des élémentaux de glace."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         skills:List[Skill] = []

#         boosts = Skill_boost_elemental_glace()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Elémental_de_glace"

# class Elemental_d_ombre(Elemental):
#     """La classe des élémentaux d'ombre."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         skills:List[Skill] = []

#         boosts = Skill_boost_elemental_ombre()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Elémental_d'ombre"

# class Magicien(Classe):
#     """La classe des utilisateurs de magie (hors enchantements). Plutôt axé sur l'attaque "brute". Renforce les magies (hors enchantements), particulièrement les magies d'attaques. Le skill magie peut lui être transféré."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         magie = Skill_magie()

#         skills:List[Skill] = [magie]

#         boosts = Skill_boost_magicien()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Magicien"

# class Necromancien(Classe):
#     """La classe des sorciers fantômes immortels inhumains avec une affinité à l'ombre et des magies d'ombre (les conditions pour que le joueur l'acquiert sont très strictes, mais les monstres nécromanciens sont plus courants). Les nécromanciens peuvent réanimer les cadavres et potentiellement les convertir à leur cause au passage."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre des conditions sur le nombre de morts vivants qui suivent le nécromancien ou le nombre de réanimations pratiquées ?

#         immortalite = Skill_immortel() #Les nécromanciens autres que le joueur ne possèdent pas ce skill, et ne peuvent donc pas le transférer.

#         skills:List[Skill] = [immortalite]

#         boosts = Skill_boost_necromancien()
#         reanimation = Skill_reanimation()

#         skills_intrasecs:List[Skill_intrasec] = [boosts,reanimation]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Nécromancien"

# class Maitre_de_la_mort(Classe):
#     """Classe rare, accordée aux Nécromanciens de niveau 10 (niveau de classe) qui remplissent certaines conditions (obtention par titre)."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre des conditions sur le nombre de morts vivants qui suivent le nécromancien ou le nombre de réanimations pratiquées ?

#         immortalite = Skill_immortel() #Seul le joueur peut obtenir cette classe. Il possède forcément le skill immortel pour en arriver là.

#         skills:List[Skill] = [immortalite]

#         boosts = Skill_boost_maitre_de_la_mort()
#         reanimation = Skill_reanimation_renforcee() #Les skills du maitre de la mort sont plus puissants que ceux du nécromancien

#         skills_intrasecs:List[Skill_intrasec] = [boosts,reanimation]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Maitre de la mort"

# class Assassin(Classe):
#     """La classe des sorciers axés sur l'assassinat. Renforce les effets de morts instantannée, comme le sort d'instakill ou l'aura d'instakill, en réduisant la supériroté nécessaire à leur fonctionnement."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         boosts = Skill_boost_instakill()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs)

#         self.nom = "Assassin"

# class Voleur(Classe):
#     """La classe des voleurs. Renforce les skills de vols. Les skills de vols peuvent lui être transférés."""
#     def __init__(self):
#         cond_evo = [0,10,20,30,40,50,60,70,80,90]

#         vol = Skill_vol()
#         vol_priorite = Skill_vol_de_priorite() #Rajouter les autres skills de vols s'ils ne sont pas inclus dans ceux là.

#         skills:List[Skill] = [vol,vol_priorite]

#         boosts = Skill_boost_vol()

#         skills_intrasecs:List[Skill_intrasec] = [boosts]

#         Classe.__init__(self,cond_evo,skills_intrasecs,skills)

#         self.nom = "Voleur"

# T is a type, and must be a subclass of Skill
if TYPE_CHECKING:
    T = TypeVar('T', bound=Skill)

def trouve_skill(classe:Classe,type_skill:Type[T]) -> Optional[T]:
    for skill in classe.skills:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
            return skill
    for skill in classe.skills_intrasecs:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
            return skill
    for sous_classe in classe.sous_classes: #On récurse la recherche dans les sous-classes.
        trouve_bis = trouve_skill(sous_classe,type_skill)
        if trouve_bis is not None:
            return trouve_bis

from Jeu.Systeme.Classe.Classe_principale import *