from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Tuple, Type
from Jeu.Action.Action_skill import Action_skill
from Jeu.Entitee.Agissant.Agissant import Agissant

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Action.Magie.Magie import Magie
    from Jeu.Entitee.Item.Equippement.Degainable.Degainable import Arme
    from Affichage.Skins.Skins import *
    from Jeu.Constantes import *
    from Jeu.Systeme.Constantes_skills.Skills import *
    from Jeu.Action.Action_skill import Action_skill
    from Jeu.Action.Attaque import Attaque, Attaque_arme, Attaque_final
    from Jeu.Action.Deplacement import Marche, Cours
    from Jeu.Action.Action_skill import Ramasse

# Imports des classes parentes
from Jeu.Systeme.Skill.Skill import Skill

class Actif(Skill):
    """
    Les skills qui genèrent les actions.
    """
    def fait(self,agissant:Agissant) -> Action_skill:
        """Fait l'action"""
        raise NotImplementedError

class Skills_offensifs(Actif):
    """
    Un skill qui genère une attaque (hors attaque magique).
    """
    def fait(self,agissant:Agissant) -> Attaque:
        """Fait l'attaque"""
        raise NotImplementedError

class Skills_projectiles(Actif): #/!\ Retravailler un jour
    """
    Un skill qui lance un objet.
    """

    def utilise(self) -> Tuple[float, float, float]:
        """Utilise le skill, et renvoie l'objet lancé"""
        raise NotImplementedError

class Skills_magiques(Actif):
    """
    Un skill qui permet de lancer des magies.
    """
    def __init__(self): #On précise les magies directement disponibles. D'autres peuvent être acquisent en cours de jeu dans le cas du joueur. magies est un dictionnaire, les clées sont les noms des magies.
        self.magies={}
        self.latence = 0 #La latence dépend du sort utilisé
        self.gain_xp = 0 #L'xp dépend du sort utilisé et du mana dépensé

    def ajoute(self,magie:Type[Magie]):
        """Ajoute une magie au skill"""
        self.magies[magie.nom]=magie

    def menu_magie(self) -> List[Magie]:
        """Renvoie la liste des magies que le skill peut lancer"""
        raise NotImplementedError
    
    def fait(self,nom:str,agissant:Agissant) -> Magie:
        """Fait la magie nommée nom"""
        return self.magies[nom](self,agissant,self.niveau)

class Skill_deplacement(Actif):
    """
    Un skill qui permet de se déplacer vers une case adjacente.
    """
    
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Actif.__init__(self)
        self.nom="Deplacement"

    def get_skin(self):
        return SKIN_SKILL_DEPLACEMENT

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau

    def fait(self,agissant,direction,course=False) -> Marche:
        """Fait le déplacement"""
        raise NotImplementedError

class Skill_ramasse(Actif):
    """
    Un skill qui permet de ramasser des objets sur sa case.
    """
    def __init__(self):
        Actif.__init__(self)
        self.nom="Ramassage"

    def get_skin(self):
        return SKIN_SKILL_RAMASSE

    def fait(self, agissant: Agissant) -> Ramasse:
        """Fait le ramassage"""
        raise NotImplementedError

class Skill_merge(Actif):
    """
    Un skill qui permet à deux groupes de fusionner. Unique aux slimes.
    """
    def __init__(self):
        Actif.__init__(self)
        self.nom="Fusion de slimes"

    # /!\ À compléter

class Skill_absorb(Actif):
    """Un skill qui permet d'absorber un cadavre (le ramasser et récupérer un skill). Unique aux slimes."""
    def __init__(self):
        Actif.__init__(self)
        self.nom="Absorption de cadavre"

class Skill_divide(Actif):
    """Un skill qui permet à un agissant de se séparer en deux. Unique aux slimes."""
    def __init__(self):
        Actif.__init__(self)
        self.nom="Division"

class Skill_attaque(Skills_offensifs):
    """Un skill qui permet d'attaquer."""
    def __init__(self):
        Skills_offensifs.__init__(self)
        self.nom = "Attaque"

    def fait(self,agissant:Agissant, direction:Optional[Direction] = None) -> Attaque:
        """Fait l'attaque"""
        raise NotImplementedError
    
class Skill_attaque_arme(Skills_offensifs):
    """Un skill qui permet d'attaquer avec une arme."""
    def __init__(self):
        Skills_offensifs.__init__(self)
        self.nom = "Attaque avec arme"

    def fait(self,agissant:Agissant, arme:Arme, direction:Optional[Direction] = None) -> Attaque_arme:
        """Fait l'attaque"""
        raise NotImplementedError

class Skill_vol(Actif):
    """Permet de dérober les drops d'un ennemi (sans devoir le tuer ni même le combattre). Nécessite le skill d'observation pour savoir ce qu'on peut voler.""" #Evolue vers les autres skills de vol ? Les offre au fur et à mesure de sa montée de niveau ? Les inclus à partir de certains niveaux ?
    def __init__(self):
        Actif.__init__(self)
        self.nom = "Vol"

    def fait(self, agissant: Agissant) -> Derobe:
        return super().fait(agissant)

class Skill_vol_de_priorite(Skill):
    """Permet de dérober la priorité d'un ennemi (ne fonctionne pas sur ceux qui en ont trop ?). Nécessite que le skill d'observation révèle la priorité de l'ennemi.
       C'est un skill actif."""
    def __init__(self):
        Skill.__init__(self)
        self.latence=11
        self.superiorite=11 #la quantité de priorité que l'agissant doit avoir en plus par rapport à la cible qu'il vole. Peut-être la faire passer en négatif ?
        self.gain_xp=0.1
        self.nom = "Vol de priorite"

    def get_skin(self):
        return SKIN_SKILL_VOL

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.latence-=1
            self.superiorite-=1 #Ajuster l'équilibrage et l'évolution des skills
            self.niveau+=1

    def utilise(self,priorite_vole,priorite_voleur):
        fonctionne = priorite_vole + self.superiorite < priorite_voleur
        latence = 0
        if fonctionne :
            self.xp_new+=self.gain_xp #est-ce que tous ces skills (déplacement, écrasement, vol, etc.) ne gagnent de l'xp que quand ils fonctionnent ? Harmoniser !
            latence=self.latence
        return latence, fonctionne

class Skill_defense(Skill):
    """Absorbe une partie des dégats infligés à l'agissant. La proportion de dégats bloqués augmente avec le niveau.
       C'est un skill semi-passif, il est activé à chaque fois que des dégats sont infligés à l'agissant."""
    def __init__(self):
        Skill.__init__(self)
        self.taux=1
        self.gain_xp=0.1
        self.nom = "Défense"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau+=1
            self.taux-=0.1 #Le skill bloque 100% des dégats au niveau 10, c'est un peu exagéré...

    def utilise(self):
        self.xp_new += self.gain_xp #Faire dépendre des dégats bloqués ?
        return self.taux

class Skill_blocage(Skill):
    """Permet de se cacher derrière son bouclier.
       C'est un skill actif."""
    def __init__(self):
        Skill.__init__(self)
        self.taux_utilisation = 1
        self.latence = 5
        self.gain_xp=0.1
        self.nom = "Blocage"

    def get_skin(self):
        return SKIN_SKILL_BLOCAGE

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.taux_utilisation -= 0.1
            if self.niveau in [3,5,8,10]:
                self.latence -= 1 #Une fois la latence écoulée, on peut faire autre chose tout en profitant de la protection (si elle dure encore).
            self.niveau += 1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.latence,self.taux_utilisation

class Skill_course(Skill,Skill_deplacement):
    """Le skill utilisé pour se déplacer. Lorsqu'il augmente de niveau, la vitesse de déplacement augmente aussi. C'est un skill intrasec à la classe principale.
       Les pnjs le sélectionnent lorsqu'il choisissent de se déplacer, alors que le joueur le sélectionne lorsqu'il appuie sur les touches. Le joueur peut aussi s'en servir lorsqu'il explore la minimap ou l'inventaire.
       C'est un skill actif, qui s'actionne quand on le réclame."""
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Skill.__init__(self)
        self.nom="Course"

    def get_skin(self):
        return SKIN_SKILL_DEPLACEMENT

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau+=1 #Le niveau augmente
            #Pas d'autre cadeau
        
    def utilise(self):
        """fonction qui utilise le skill"""
        self.xp_new+=gain_xp_course[self.niveau-1] #On gagne de l'xp !
        return latence_course[self.niveau-1], self.niveau #On renvoie le temps que prendra l'action, pour savoir combien de temps l'agissant attendra, et le niveau, pour les calculs du controleur, des collisions, du labyrinthe, etc.

class Skill_lancer(Skill,Skills_projectiles):
    """Permet de lancer un item. Le temps du lancer dépend du poid de l'item et du niveau du skill. La portée du lancer dépend de la portée de l'item, du niveau du skill et des capacités de l'agissant. L'item peut être dans l'inventaire ou créé au moment du lancer.
       C'est un skill actif."""
    def __init__(self):
        Skill.__init__(self)
        self.taux_latence = 1.1 #La latence dépend du poids du projectile.
        self.taux_hauteur = 0.9 #La portée dépend du poids du projectile (et des capacités de l'agissant). Elle est exprimé en temps (de vol).
        self.taux_vitesse = 0.9 #La vitesse dépend de l'aérodinamisme du projectile.
        self.gain_xp=0.1 #Faire varier en fonction des projectiles ?
        self.nom = "Lancer"

    def get_skin(self):
        return SKIN_SKILL_LANCER

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.taux_latence -= 0.1
            self.taux_hauteur += 0.1
            self.taux_vitesse += 0.05
            self.niveau += 1

    def boost_portee(self): #C'est un peu du bricolage...
        self.taux_vitesse += 0.25

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.taux_latence,self.taux_hauteur,self.taux_vitesse

class Skill_creation_de_fleches(Skill):
    """Permet de créer des projectiles de type flèche. La montée de niveau améliore les flèches.
       C'est un skill actif (souvent appelé par l'intermédiaire du skill de lancer ?)."""
    def __init__(self,fleches=[]):
        Skill.__init__(self)
        self.fleches=fleches
        self.gain_xp = 0.01
        self.nom = "Création de flèches"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #comment faire pour les autres types de cadeaux ?
                    self.xp_new+=cadeau
                # elif isinstance(cadeau,Fleche): #On peut gagner un type de flèche avec la montée de niveau du skill ? /!\ Un skill ne connait pas les autres objets du jeu /!\
                #     self.ajoute(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def ajoute(self,fleche):
        self.fleches.append(fleche)

    def utilise(self,xp):
        self.gain_xp = xp
        self.xp_new+=self.gain_xp #On gagne de l'xp, mais combien ? 0.1, est-ce assez ? trop ?
        return self.niveau

class Skill_creation_d_explosifs(Skill):
    """Permet de créer des projectiles de type explosif. La montée de niveau améliore les explosifs (diminue le coût de mana/le temps ?).
       C'est un skill actif (souvent appelé par l'intermédiaire du skill de lancer ?)."""
    def __init__(self,explosifs=[]): #Rajouter le projectile explosif de base quand je l'aurai créé.
        Skill.__init__(self)
        self.explosifs=explosifs
        self.latence = 0 #La latence dépend de l'explosif utilisée (s'il y en a)
        self.gain_xp = 0 #L'xp dépend de l'explosif utilisée
        self.nom = "Création d'explosifs"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #Comment faire pour les autres types de cadeaux ?
                    self.xp_new+=cadeau
                # elif isinstance(cadeau,Explosif): #On peut gagner un type d'explosif avec la montée de niveau du skill ?
                #     self.ajoute(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def ajoute(self,explosif):
        self.explosifs.append(explosif)

    def utilise(self,xp):
        self.gain_xp = xp
        self.xp_new+=self.gain_xp #On gagne de l'xp, mais combien ? 0.1, est-ce assez ? trop ?
        return self.niveau

class Skill_alchimie(Skill):
    """Permet de créer divers items. C'est un skill semi-passif au sens où son utilisation ne prend pas de temps."""
    def __init__(self):
        Skill.__init__(self)
        self.recettes = {}
        self.gain_xp = 0 #L'xp dépend de la potion créée
        self.nom = "Alchimie"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.recettes = recettes_alchimie[self.niveau]
            self.niveau+=1

    def utilise(self,xp):
        self.gain_xp = xp
        self.xp_new+=self.gain_xp

class Skill_echange(Skill):
    """Un skill d'échange d'objet. Permet au marchand (dans le labyrinthe) d'échanger des objets avec son patron (à l'extérieur) pour les vendre."""
    def __init__(self):
        Skill.__init__(self)
        self.items=None
        self.gain_xp = 0.1
        self.nom = "Échange"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #Comment faire pour les autres types de cadeaux ?
                    self.xp_new+=cadeau
                # elif isinstance(cadeau,Explosif): #On peut gagner un type d'explosif avec la montée de niveau du skill ?
                #     self.ajoute(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def utilise(self):
        self.xp_new+=self.gain_xp #On gagne de l'xp, mais combien ? 0.1, est-ce assez ? trop ?
        return self.niveau

class Skill_aura_elementale(Skill_aura,Skill):
    """La classe des skills d'aura élémentales. Les auras élémentales de deux agissants différents sont incompatibles."""
    pass # Ne doit pas être instanciée

class Skill_aura_elementale_terre(Skill_aura_elementale,Skill):
    """Offre une aura élémentale de terre."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Skill.__init__(self)
        self.nom = "Aura élémentale de terre"

class Skill_aura_elementale_feu(Skill_aura_elementale,Skill):
    """Offre une aura élémentale de feu."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Skill.__init__(self)
        self.nom = "Aura élémentale de feu"

class Skill_aura_elementale_glace(Skill_aura_elementale,Skill):
    """Offre une aura élémentale de glace."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Skill.__init__(self)
        self.nom = "Aura élémentale de glace"

class Skill_aura_elementale_ombre(Skill_aura_elementale,Skill):
    """Offre une aura élémentale d'ombre."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Skill.__init__(self)
        self.nom = "Aura élémentale d'ombre"

    # Idée : offrir un boost de distance de vision à chaque niveau de l'aura, pour compenser (au moins en partie) l'augmentation de l'opacité des cases avoisinnantes

class Skill_aura_mortelle(Skill_aura,Skill):
    """Offre une aura qui lance une attaque d'instakill sur tous les individus hostiles."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Skill.__init__(self)
        self.nom = "Aura mortelle"

class Skill_affinite_elementale(Skill):
    """Augmente l'affinité avec un élément. Une affinité élevée augmente les dégats infligés et diminue les dégats subits par le biais d'attaques de cet élément, réduit les coups de mana et les temps de latence des sorts de cet élément, etc. et une affinité faible a l'effet inverse. Les quatre stats d'affinité sont très légèrement affectées par les actions du joueur tout au long du jeu, et grandement affectées par les skills d'affinité.
       C'est un skill-passif (il est appelé une fois par tour pour déterminer les affinités effectives du joueur pour le tour."""
    def __init__(self,element):
        Skill.__init__(self) #Mettre des conditions d'évolutions plus liés aux actions ?
        self.affinite_bonus = 0 #Le bonus ajouté à la stat d'affinité à l'élément
        self.element = element
        self.gain_xp = 0.1
        self.nom = "Affinité élémentale"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            for cadeau in self.cad_evo[self.niveau]:
                """if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                el"""
                if isinstance(cadeau,int): #Comment faire pour les autres types de cadeaux ?
                    self.xp_new+=cadeau
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            self.affinite_bonus += 1 #C'est beaucoup ? Peu ? À ajuster !

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.affinite_bonus

class Invite_de_commande(Skill):
    """Un skill pour exécuter des commandes arbitraires."""
    def __init__(self):
        Skill.__init__(self)
        self.chaine = ""
        self.nom = "Invite de commande"

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            self.niveau+=1

    def utilise(self,touche):
        if touche == pygame.K_DELETE:
            if len(self.chaine) >= 1:
                self.chaine = self.chaine[:-1]
        elif touche == pygame.K_RETURN:
            eval(self.chaine) #/!\ Rajouter les variables globales pour que ça serve à quelque-chose !
            self.chaine = ""
        else: #On se limite aux trucs simples pour l'instant !
            self.chaine+=pygame.key.name(touche)
