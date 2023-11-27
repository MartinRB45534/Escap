"""
Contient les classes mères des skills
"""

from __future__ import annotations
import affichage as af

# Pas d'import utilisés uniquement dans les annotations

# Pas d'import des classes parentes

class Skill:
    """!!! Skill != skille !!! (Vieille private joke)"""
    def __init__(self):
        self.niveau=0 #Le niveau devrais passer à 1 lorsqu'on acquiert le skill
        self.xp_new:float=0 #Contabilise l'xp obtenue pendant le tour, pour la propagation
        self.propagation=0.5 #Certains skills ont un taux de propagation plus important (?)
        self.nom="Skill anonyme"

    def gagne_xp(self):
        """fonction qui propage l'xp accumulé au cours du tour vers la classe mère"""
        #On propage l'xp accumulé au cours du tour vers la classe mère
        res = self.xp_new*self.propagation
        self.xp_new=0
        return res

    def evo(self,nb_evo:int=1):
        """fonction qui procède à l'évolution"""
        for _ in range(nb_evo):
            self.niveau+=1

    def get_skin(self):
        """Renvoie le skin du skill"""
        return af.SKIN_MYSTERE

class SkillIntrasec(Skill):
    """
    Les skills intrinsèques sont des skills qui sont liés à une classe. Ils évoluent avec la classe.
    """
    def gagne_xp(self):
        #On propage l'xp accumulé au cours du tour vers la classe mère
        res = self.xp_new*self.propagation
        self.xp_new=0
        return res

class SkillExtra(Skill):
    """
    Les skills extrinsèques sont indépendants de la classe. Ils évoluent selon leur propre utilisation, et peuvent changer de classe.
    """
    def __init__(self,conditions_evo:list[float]=[0,10,20,30,40,50,60,70,80,90]):
        super().__init__()
        self.cond_evo=conditions_evo
        self.xp=0 #L'xp commence à 0, évidemment

    def gagne_xp(self):
        #On propage l'xp accumulé au cours du tour vers la classe mère
        res = self.xp_new*self.propagation
        #On l'ajoute aussi à son propre xp
        self.xp+=self.xp_new
        self.xp_new=0
        #On en profite pour vérifier si on peut évoluer
        self.check_evo()
        return res

    def check_evo(self):
        """fonction qui vérifie que les conditions d'évolution sont vérifiées"""
        if self.niveau<len(self.cond_evo) and self.cond_evo[self.niveau]>0 and self.xp>=self.cond_evo[self.niveau]:
            self.evo()
