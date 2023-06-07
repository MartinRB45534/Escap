from __future__ import annotations
from typing import TYPE_CHECKING, Set

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Systeme.Skill.Skill import Skill_intrasec, Skill_extra

# Imports des classes parentes
from ..Systeme.Classe.Classe import Classe

class Classe_principale(Classe):
    """La classe principale de l'agissant. Le niveau d'un agissant est égal au niveau de sa classe principale. Pour les agissants capables de s'améliorer, l'utilisation de la procédure gagne_xp de la classe principale provoque récursivement l'utilisation de cette procédure sur tous les sous-classe est skills de l'agissant. L'amélioration de la classe principale provoque une amélioration des statistiques de l'agissant.
       Pour le joueur, une amélioration de la classe principale permet de choisir une récompense dans l'arbre de compétence ou dans l'arbre élémental (ou deux dans l'arbre élémental avec la classe élémentaliste)."""
    def __init__(self,identite,niveau:int):
        skills_intrasecs:Set[Skill_intrasec] = set()
        skills:Set[Skill_extra] = set()
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        if identite == 'heros' :
            self.evolutif = False

            #Skills intrasecs (leur niveau est lié à celui de la classe principale) :
            deplacement = Deplacement_joueur() #On crée un skill de déplacement
            skills_intrasecs.add(deplacement)
            vision = Vision_humain() #On crée un skill de vision
            skills_intrasecs.add(vision)
            ramasse = Ramasse_humain() #On crée une skill de ramassage
            skills_intrasecs.add(ramasse)

            #Autres skills :
            stomp = Stomp_humain() #On crée un skill de stomp
            stomp.evo() #On le passe au niveau 1
            skills.add(stomp)
            attaque = Attaque_humain() #On crée un skill d'attaque par le biais d'armes
            attaque.evo() #On le passe au niveau 1
            skills.add(attaque)
            magie = Magie_humain() #On crée un skill d'utilisation de magie
            magie.evo() #On le passe au niveau 1
            skills.add(magie)
            #Pour pouvoir tester et parcourir les labyrinthes même quand la génération est cassée :
            # ecrasement = Skill_ecrasement()
            # ecrasement.evo()
            # skills.add(ecrasement)

##            #!!! Attention : ce qui se passe ici est extérieur au système !
##            if malchance_forcee : #Après la chance, la malchance...
##                malchanceux = Skill_malchanceux() #On crée un mystérieux skill de mauvais augure non-référencé...
##                malchanceux.evo() #On augmente même son niveau...
##                malchance_forcee = False #Mais on ne le fera pas la prochaine fois, promis !
##                skills.add(malchanceux)
##            elif random.random()<0.01 or chance_forcee : #On peut espérer, ou forcer le destin dans le fichier des constantes.
##                chanceux = Skill_chanceux() #On crée un mystérieux skill non-référencé, mais au moins son nom est encourageant !
##                chanceux.evo() #On le passe au niveau 1
##                malchance_forcee = True #Profitons bien de la partie, la prochaine risque d'être plus difficile...
##                skills.add(chanceux)
##            #Le système peut quand même voir les conséquences de ces actions mystérieuses.

        elif identite == 'receptionniste':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            attaque = Attaque_humain()
            attaque.evo()
            skills.add(attaque)

        elif identite == 'paume':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)

        elif identite == 'peureuse':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            magie = Magie_humain()
            magie.evo()
            skills.add(magie)

        elif identite == 'codeur':
            self.evolutif = False
            # omnipotence = Invite_de_commande()
            # omnipotence.evo()
            # skills.add(omnipotence)
            omniscience = Vision_humain() #Lui faire un vrai skill d'omniscience à l'occasion
            skills_intrasecs.add(omniscience)

        elif identite == 'encombrant':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            attaque = Attaque_humain()
            attaque.evo()
            skills.add(attaque)

        elif identite == 'alchimiste':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            magie = Magie_humain()
            magie.evo()
            skills.add(magie)
            alchimie = Alchimie_humain()
            alchimie.evo()
            skills.add(alchimie)

        elif identite == 'peste':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            magie = Magie_humain()
            magie.evo()
            skills.add(magie)

        elif identite == 'bombe_atomique':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            magie = Magie_humain()
            magie.evo()
            skills.add(magie)

        elif identite == 'marchand':
            self.evolutif = False
            deplacement = Deplacement_humain()
            skills_intrasecs.add(deplacement)
            vision = Vision_humain()
            skills_intrasecs.add(vision)
            stomp = Stomp_humain()
            stomp.evo()
            skills.add(stomp)
            attaque = Attaque_humain()
            attaque.evo()
            skills.add(attaque)
            # echange = Skill_echange()
            # echange.evo()
            # skills.add(echange)

        elif identite == 'gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)

        elif identite == 'sentinelle_gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)

        elif identite == 'premier_monstre':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)

        elif identite == 'troisieme_monstre':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)

        elif identite == 'guerrier_gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)

        elif identite == 'explorateur_gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)

        elif identite == 'mage_gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            magie = Magie_gobelin()
            skills_intrasecs.add(magie)

        elif identite == 'deuxieme_monstre':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            magie = Magie_gobelin()
            skills_intrasecs.add(magie)

        elif identite == 'shaman_gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            magie = Magie_gobelin()
            skills_intrasecs.add(magie)

        elif identite == 'chef_gobelin':
            self.evolutif = False
            deplacement = Deplacement_gobelin()
            skills_intrasecs.add(deplacement)
            vision = Vision_gobelin()
            skills_intrasecs.add(vision)
            stomp = Stomp_gobelin()
            skills_intrasecs.add(stomp)
            attaque = Attaque_gobelin()
            skills_intrasecs.add(attaque)
            #Lui rajouter un skill de dirigeant ?

        elif identite == 'slime':
            self.evolutif = False #Changer ça à l'occasion
            deplacement = Deplacement_slime()
            skills_intrasecs.add(deplacement)
            vision = Vision_slime()
            skills_intrasecs.add(vision)
            stomp = Stomp_slime()
            skills_intrasecs.add(stomp)
            division = Divide_slime()
            skills_intrasecs.add(division)
            absorption = Absorb_slime()
            skills_intrasecs.add(absorption)
            fusion = Merge_slime()
            skills_intrasecs.add(fusion)

        elif identite == 'ombriul':
            self.evolutif = False
            deplacement = Deplacement_ombriul()
            skills_intrasecs.add(deplacement)
            vision = Vision_ombriul()
            skills_intrasecs.add(vision)
            stomp = Stomp_ombriul()
            skills_intrasecs.add(stomp)
            magie = Magie_ombriul()
            skills_intrasecs.add(magie)

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)
        self.evo(niveau)

    def gagne_xp(self):
        if self.evolutif :
            Classe.gagne_xp(self)
        else:
            Classe.vire_xp(self)

# Imports utilisés dans le code
from ..Systeme.Skill.Skills import *