from __future__ import annotations
# Pas d'imports pour les annotations 

# Imports des classes parentes
from .Skill import Skill

class Passif(Skill):
    """
    Les skills qui se déclenchent automatiquement.
    """
    def utilise(self):
        """En général, accumule l'xp"""
        raise NotImplementedError

class Skill_debut_tour(Passif):
    """La classe des skills appelés au début de chaque tour (principalement les skills d'aura)."""

class Skill_vision(Passif):
    """Le skill utilisé pour observer son environnement. Lorsqu'il augmente de niveau, on peut voir plus loin. C'est un skill intrasec à la classe principale. !!!Ne pas confondre avec observation, qui permet d'obtenir des informations sur ce que l'on voit.!!!
       C'est un skill semi-passif, qui s'actionne à chaque tour."""
    def __init__(self): #Pour l'instant le skill est générique, identique pour tous
        Passif.__init__(self)
        self.nom="Vision"
        self.portee:float

    def utilise(self): #Le skill ne fait que donner des infos, il ne peut pas manipuler d'objet labyrinthe ou autres
        raise NotImplementedError

class Skill_aura(Skill_debut_tour): #Toutes les auras ne sont pas des skills intrasecs, mais par rapport aux méthodes c'est plus logique comme ça.
    """Offre une aura qui se matérialise autour de l'agissant. Les effets de l'aura diffèrent selon l'aura. Skill aura est une classe parente et ne doit pas être instanciée.
       Les auras sont des skills passifs, qui s'actionne à chaque tour."""
    def __init__(self,effet):
        Passif.__init__(self)
        self.effet = effet #L'effet qui distribuera l'aura sur la zone (il ira chercher la portée tout seul comme un grand)
        self.gain_xp = 0.1 #Il faut 100 tours pour augmenter le niveau d'un skill d'aura. C'est trop peu...
        self.nom="Aura"

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.effet(self.niveau)

class Skill_aura_divine(Skill_aura):
    """Offre une aura divine qui soigne et boost les alliés et blesse les ennemis maléfique (élémentaux de l'ombre, nécromanciens, créatures réanimées, etc.). C'est un skill intrasec à la classe Ange.
       C'est un skill passif (appelé à chaque tour)."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        self.nom="Aura divine"

class Skill_essence_magique(Passif):
    """Ce skill permet d'utiliser les PM comme deuxième barre de PV si les PV sont à 0. Inspiré du skill persévérance dans komu desu ga, nanika ? et point de départ de l'une des quatre branches d'évolution du joueur.
       C'est un skill semi-passif, qui s'actionne quand on a des PV négatifs après avoir reçu des dégats (presque comme un sort de soin instantanné automatique)."""
    def __init__(self): #Seul le joueur et un boss peuvent posséder ce skill, donc il n'y a pas besoin d'en prévoir différentes versions
        Passif.__init__(self)
        self.taux = 32 #Le taux de conversion PM:PV, actuellement 32 PM pour 1 PV (à ajuster finement)
        self.gain_xp = 0 #On gagne de l'xp pour le mana converti en PV, pas pour s'être pris un coup
        self.nom = "Essence magique"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.taux*=0.5 #Peut-être réduire moins mais commencer avec un taux plus avantageux, parce qu'on a peu de PM en bas niveau
            self.niveau+=1
            #Pas d'autre cadeau ?

    def utilise(self,pv):
        pm=pv*self.taux #Le nombre de PM qu'il faut pour compenser les PV manquants. Tout (sauf le taux) est en négatif ! D'où les xp en dessous !
        self.xp_new-=pm*0.1 #Plus on dépense de PM, plus le niveau augmente vite, donc le processus ralentit tout seul quand les niveaux augmentent. Peut-être ajuster quand même ?
        return pm #Le controleur veut juste savoir combien de PM il retire, et donc s'il doit tuer l'agissant.

class Skill_immortel(Passif):
    """ 'évolution' du skill précédent essence magique. Permet de survivre avec - de 0 PV, sans perdre de PM, mais avec une réduction de toutes les stats (possibilité de choisir entre les deux skills ?).
       C'est un skill semi-passif, qui s'actionne quand on a des PV négatifs à la fin du tour (la présence du skill suffit au controleur, mais il sera quand même "utilisé" pour qu'il puisse gagner son xp) (son coefficient sera extrait directement, sans procédure, pour éviter de lui faire gagner des xp à chaque fois qu'une valeur est utilisée)."""
    def __init__(self): #Seul le joueur peut avoir ce skill (?), donc il n'y a qu'une version
        Passif.__init__(self)
        self.coef = 0 #Toutes les statistiques sont multipliées par 0 (0.05 au premier niveau) lorsque les PV sont négatifs.
        self.gain_xp = 0.1 #Il faut passer 100 tours en dessous de 0 PV pour augmenter le niveau de ce skill.
        self.nom = "Immortalité"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.coef+=0.05 #Peut-être partir de +, progresser moins et non linéairement et arriver à -
            self.niveau+=1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.coef #Peut-être garder un multiplicateur dans les stats, et ne pas aller chercher l'attribut coef à chaque fois ?

class Skill_magie_infinie(Passif):
    """L'opposé de l'essence magique, permet de consommer plus de mana qu'on en possède, avec des PM qui deviennent négatifs. Pour chaque PM en dessous de 0, la régénération des PV est réduite d'autant, elle peut devenir négative.
       C'est un skill semi-passif, qui s'actionne quand l'agissant a des PM négatifs à la fin du tour (la présence du skill suffit au controleur pour autoriser des sorts même s'il n'y a pas assez de mana, le skill n'est "utilisé" que pour calculer la régén des PV une fois par tour)."""
    def __init__(self): #Seul le joueur peut avoir ce skill, donc il n'y a qu'une version
        Passif.__init__(self)
        self.taux = 1 #Au niveau 0, on perd 1PV par PM en dessous de 0. Attention, les PM ne sont pas régénérés par ce skill !
        self.gain_xp = 0.1 #Il faut passer 100 tours en dessous de 0 PM pour augmenter le niveau de ce skill.
        self.nom = "Magie infinie"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.taux-=0.1 #À ajuster
            self.niveau+=1

    def utilise(self,pm):
        self.xp_new+=self.gain_xp #Peut-être faire entrer les PM en dessous de 0 dans l'équation ?
        return pm*self.taux

class Skill_manipulation_epee(Passif):
    """Renforce les attaques réalisées à l'aide d'armes de type épée. Quand le niveau augmente, les dégats infligés avec une épée, la portée des attaques d'épée, la vitesse des attaques d'épée, la priorité des attaques d'épée, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois qu'une attaque est réalisée à l'aide d'une épée."""
    def __init__(self):
        Passif.__init__(self)
        self.boost_degats = 1 #Le coefficient appliqué aux dégats de base pour calculer les dégats réels
        self.gain_xp = 0.1 #Il faut 100 attaques à l'épée pour passer au niveau suivant
        self.nom = "Manipulation d'épée"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.boost_degats += 0.05 #On a au maximum 50% de dégats en plus.
            self.niveau += 1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.boost_degats

class Skill_manipulation_lance(Passif):
    """Renforce les attaques réalisées à l'aide d'armes de type lance. Quand le niveau augmente, les dégats infligés avec une lance, la portée des attaques de lance, la vitesse des attaques de lance, la priorité des attaques de lance, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois qu'une attaque est réalisée à l'aide d'une lance."""
    def __init__(self):
        Passif.__init__(self)
        self.boost_degats = 1 #Le coefficient appliqué aux dégats de base pour calculer les dégats réels
        self.gain_xp = 0.1 #Il faut 100 attaques à la lance pour passer au niveau suivant
        self.nom = "Manipulation de lance"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.boost_degats += 0.05 #On a au maximum 50% de dégats en plus.
            self.niveau += 1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.boost_degats

class Skill_manipulation_bouclier(Passif):
    """Renforce la défense des items de type bouclier. Quand le niveau augmente, les dégats bloqués avec un bouclier, la portée des boucliers (pour un bouclier, la portée permet de protéger une plus grande zone), la vitesse d'utilisation des boucliers, la priorité des boucliers, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois que le skill de bloquage d'attaque est utilisé."""
    def __init__(self):
        Passif.__init__(self)
        self.boost_defense = 1 #Le coefficient appliqué au taux de dégats non bloqués de base pour connaitre le taux réel de dégats non bloqués
        self.duree_protection = 3
        self.gain_xp = 0.1 #Il faut se protéger 100 fois derrière son bouclier pour passer au niveau suivant
        self.nom = "Manipulation de bouclier"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.boost_defense -= 0.05 #On a au maximum 50% de dégats bloqués par le biais du skill
            self.duree_protection += 1
            self.niveau += 1

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.duree_protection,self.boost_defense

class Skill_manipulation_arme(Passif):
    """Renforce les attaques réalisées à l'aide d'armes (exclue la magie, le stomp, les auras). Quand le niveau augmente, les dégats infligés avec une arme, la portée des attaques d'arme, la vitesse des attaques d'arme, la priorité des attaques d'arme, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois qu'une attaque est réalisée à l'aide d'une arme."""
    def __init__(self):
        Passif.__init__(self)
        self.boost_degats = 0 #Le coefficient appliqué aux dégats de base pour calculer les dégats supplémentaires
        self.boost_defense = 1 #Le coefficient appliqué au taux de dégats non bloqués de base pour connaitre le taux réel de dégats non bloqués
        self.duree_protection = 3
        self.gain_xp = 0.1 #Il faut 100 attaques avec une arme pour passer au niveau suivant
        self.nom = "Manipulation d'armes"

#Avoir des effets pour chaque type d'arme ? Les boucliers n'ont évidemment pas besoin de boost de dégat...

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.boost_degats += 0.05 #On a au maximum 50% de dégats en plus.
            self.boost_defense -= 0.05 #On a au maximum 50% de dégats bloqués par le biais du skill
            self.duree_protection += 1
            self.niveau += 1

    def utilise_attaque(self): #Diviser en lance et épée quand les effets seront différenciés
        self.xp_new+=self.gain_xp
        return self.boost_degats

    def utilise(self):
        self.xp_new+=self.gain_xp
        return self.duree_protection,self.boost_defense

class Skill_ecrasement(Passif):
    """Permet d'écraser (détruire) d'autres agissants ou des murs sur son chemin. Plus le niveau est élevé, moins la différence de priorité entre l'écrseur et l'écrasé doit être élevée pour permettre l'écrasement.
       C'est un skill semi-passif, qui s'actionne quand il y a collision entre l'agissant et un autre agissant ou un mur."""
    def __init__(self):
        Passif.__init__(self)
        self.superiorite = 6 #la quantité de priorité que l'agissant doit avoir en plus par rapport à la cible qu'il écrase
        self.gain_xp = 0.1 #Il faut écraser 100 murs ou ennemis pour passer au niveau suivant
        self.nom = "Ecrasement"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.superiorite -= 1 #l'écart minimal nécessaire diminue quand le niveau du skill augmente
            self.niveau += 1

    def utilise(self,priorite_ecrase,priorite_ecrasant):
        fonctionne = priorite_ecrase + self.superiorite < priorite_ecrasant
        if fonctionne :
            self.xp_new+=self.gain_xp #est-ce que tous ces skills (déplacement, écrasement, etc.) ne gagnent de l'xp que quand ils fonctionnent ? Harmoniser !
        return fonctionne

class Skill_observation(Passif):
    """Complément du skill de vision. Permet d'afficher des informations sur ce que voit le skill de vision (PV d'un ennemi ou priorité d'un mur par exemple). Peut aussi rendre visible (certains sorts, objets ou ennemis furtifs par exemple) ou révéler la vraie forme (certains ennemis portent plusieurs couches de déguisements, et le skill d'observation peut donc révéler une fausse forme différente de la forme affichée sans le skill).
       C'est un skill passif, qui s'actionne à chaque tour, après le skill vision. Il renvoit uniquement son niveau, et tous les objets ont différentes informations à afficher selon le niveau de l'observation (faire intervenir la priorité dans le calcul !)."""
    def __init__(self):
        Passif.__init__(self)
        self.gain_xp=0.1 #Il faut observer 100 objets (murs, cases, items, cailloux, agissants, projectiles) pour passer au niveau suivant (progression trop rapide ? ne compter qu'une fois chaque case, objet, etc.)
        self.nom = "Observation"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau+=1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.niveau

class Skill_defense(Passif):
    """Absorbe une partie des dégats infligés à l'agissant. La proportion de dégats bloqués augmente avec le niveau.
       C'est un skill semi-passif, il est activé à chaque fois que des dégats sont infligés à l'agissant."""
    def __init__(self):
        Passif.__init__(self)
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

class Skill_aura_elementale(Skill_aura,Skill):
    """La classe des skills d'aura élémentales. Les auras élémentales de deux agissants différents sont incompatibles."""
    pass # Ne doit pas être instanciée

class Skill_aura_elementale_terre(Skill_aura_elementale,Skill):
    """Offre une aura élémentale de terre."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Passif.__init__(self)
        self.nom = "Aura élémentale de terre"

class Skill_aura_elementale_feu(Skill_aura_elementale,Skill):
    """Offre une aura élémentale de feu."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Passif.__init__(self)
        self.nom = "Aura élémentale de feu"

class Skill_aura_elementale_glace(Skill_aura_elementale,Skill):
    """Offre une aura élémentale de glace."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Passif.__init__(self)
        self.nom = "Aura élémentale de glace"

class Skill_aura_elementale_ombre(Skill_aura_elementale,Skill):
    """Offre une aura élémentale d'ombre."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Passif.__init__(self)
        self.nom = "Aura élémentale d'ombre"

    # Idée : offrir un boost de distance de vision à chaque niveau de l'aura, pour compenser (au moins en partie) l'augmentation de l'opacité des cases avoisinnantes

class Skill_aura_mortelle(Skill_aura,Skill):
    """Offre une aura qui lance une attaque d'instakill sur tous les individus hostiles."""
    def __init__(self,effet):
        Skill_aura.__init__(self,effet)
        Passif.__init__(self)
        self.nom = "Aura mortelle"

class Skill_affinite_elementale(Passif):
    """Augmente l'affinité avec un élément. Une affinité élevée augmente les dégats infligés et diminue les dégats subits par le biais d'attaques de cet élément, réduit les coups de mana et les temps de latence des sorts de cet élément, etc. et une affinité faible a l'effet inverse. Les quatre stats d'affinité sont très légèrement affectées par les actions du joueur tout au long du jeu, et grandement affectées par les skills d'affinité.
       C'est un skill-passif (il est appelé une fois par tour pour déterminer les affinités effectives du joueur pour le tour."""
    def __init__(self,element):
        Passif.__init__(self) #Mettre des conditions d'évolutions plus liés aux actions ?
        self.affinite_bonus = 0 #Le bonus ajouté à la stat d'affinité à l'élément
        self.element = element
        self.gain_xp = 0.1
        self.nom = "Affinité élémentale"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            """fonction qui procède à l'évolution"""
            self.niveau+=1
            self.affinite_bonus += 1 #C'est beaucoup ? Peu ? À ajuster !

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.affinite_bonus
