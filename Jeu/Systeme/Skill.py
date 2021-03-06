#Les skills sont la base des actions qui ont lieu dans le jeu (action voulues ou automatiques). Les skills normaux montent de niveau au fur et à mesure des utilisations (par le biais de l'xp en général).

from Jeu.Systeme.Skill_intrasec import *

class Skill(Skill_intrasec): #Les skills ne sont pas des skills intrasecs, mais ils en ont toutes les méthodes, avec certaines en plus.
    """!!! Skill != skille !!! (Private joke)"""
    def __init__(self,conditions_evo=[0,10,20,30,40,50,60,70,80,90],cadeaux_evo=[[],[],[],[],[],[],[],[],[],[]]):
        """conditions_evo : les conditions d'évolution du skill au niveau supérieur ; si c'est un nombre, indique l'xp nécessaire à l'évolution, si c'est une chaine de caractère, indique la fonction capable d'évaluer la condition
           cadeux_evo : les récompenses d'évolution ; peuvent être des skills (?), des classes (?) ou de l'xp"""
        Skill_intrasec.__init__(self,cadeaux_evo)
        self.cond_evo=conditions_evo
        self.xp=0 #L'xp commence à 0, évidemment
        self.prep_next_evo() #On prépare déjà la prochaine évolution
        
    def gagne_xp(self):
        #On propage l'xp accumulé au cours du tour vers la classe mère
        res = self.xp_new*self.propagation
        #On l'ajoute aussi à son propre xp
        self.xp+=self.xp_new
        self.xp_new=0
        #On en profite pour vérifier si on peut évoluer
        if self.next_evo=="xp":
            self.check_evo()
        return res

    def prep_next_evo(self):
        """fonction qui permet de savoir comment vérifier la prochaine évolution"""
        if self.niveau<10:
            if isinstance(self.cond_evo[self.niveau],int):
                self.next_evo="xp"
            else:
                self.next_evo="fonction"
        else:
            self.next_evo=None

    def check_evo(self):
        """fonction qui vérifie que les conditions d'évolution sont vérifiées"""
        if self.niveau<10:
            if self.next_evo=="xp":
                if self.xp>=self.cond_evo[self.niveau]:
                    self.evo()
                    self.prep_next_evo()
            elif eval(self.cond_evo[self.niveau]):
                self.evo()
                self.prep_next_evo()

class Skill_magie(Skill):
    """Le skill utilisé pour faire de la magie. Le seul autorisé à consommer du mana (?).
       On le sélectionne en passant en argument la magie souhaitée, puis on précise éventuellement les cibles.
       C'est un skill actif, qui s'actionne quand on le réclame."""
    def __init__(self): #On précise les magies directement disponibles. D'autres peuvent être acquisent en cours de jeu dans le cas du joueur. magies est un dictionnaire, les clées sont les noms des magies.
        Skill.__init__(self) #Il faudra penser à ajouter des cadeaux magiques
        self.magies={}
        self.latence = 0 #La latence dépend du sort utilisé
        self.gain_xp = 0 #L'xp dépend du sort utilisé et du mana dépensé
        self.nom = "Magie"

    def get_skin(self):
        return SKIN_SKILL_MAGIE_GRIS

    def menu_magie(self):
        res = []
        for nom in self.magies.keys():
            type_magie = self.magies[nom]
            magie = type_magie(self.niveau)
            res.append(magie)
        return res

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
                    self.xp.append(cadeau)
                elif isinstance(cadeau,magie): #On peut gagner une magie avec la montée de niveau du skill !
                    self.ajoute(magie)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def ajoute(self,magie):
        """Focntion qui ajoute une magie. Utilisée lors des montées de niveau ou par le joueur (le joueur peut choisir de nouvelles magies lors de l'évolution de sa classe principale)."""
        self.magies[magie.nom]=magie #Les magies sont répérées par leur nom

    def utilise(self,nom):
        if nom in self.magies.keys():
            magie = self.magies[nom](self.niveau) #Les caractéristiques des magies s'améliorent avec le niveau du skill
            self.gain_xp = magie.gain_xp + magie.cout_pm*0.1
            self.xp_new+=self.gain_xp #On gagne de l'xp, mais combien ? 0.1, est-ce assez ? trop ?
            self.latence = magie.latence
            return self.latence, magie #On renvoie le temps que prendra l'action, pour savoir combien de temps l'agissant attendra et la magie (il y a plein de types de magies différentes, avec ou sans cible, etc. alors on laisse le controleur et la magie se débrouiller (attention quand même, il y a un risque de misfire ou même de backfire si ces détails de visée et autres ne sont pas réglés à temps)).
        else:
            return 0, None

class Skill_essence_magique(Skill):
    """Ce skill permet d'utiliser les PM comme deuxième barre de PV si les PV sont à 0. Inspiré du skill persévérance dans komu desu ga, nanika ? et point de départ de l'une des quatre branches d'évolution du joueur.
       C'est un skill semi-passif, qui s'actionne quand on a des PV négatifs après avoir reçu des dégats (presque comme un sort de soin instantanné automatique)."""
    def __init__(self): #Seul le joueur et un boss peuvent posséder ce skill, donc il n'y a pas besoin d'en prévoir différentes versions
        Skill.__init__(self)
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

class Skill_immortel(Skill):
    """ 'évolution' du skill précédent essence magique. Permet de survivre avec - de 0 PV, sans perdre de PM, mais avec une réduction de toutes les stats (possibilité de choisir entre les deux skills ?).
       C'est un skill semi-passif, qui s'actionne quand on a des PV négatifs à la fin du tour (la présence du skill suffit au controleur, mais il sera quand même "utilisé" pour qu'il puisse gagner son xp) (son coefficient sera extrait directement, sans procédure, pour éviter de lui faire gagner des xp à chaque fois qu'une valeur est utilisée)."""
    def __init__(self): #Seul le joueur peut avoir ce skill (?), donc il n'y a qu'une version
        Skill.__init__(self)
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

class Skill_magie_infinie(Skill):
    """L'opposé de l'essence magique, permet de consommer plus de mana qu'on en possède, avec des PM qui deviennent négatifs. Pour chaque PM en dessous de 0, la régénération des PV est réduite d'autant, elle peut devenir négative.
       C'est un skill semi-passif, qui s'actionne quand l'agissant a des PM négatifs à la fin du tour (la présence du skill suffit au controleur pour autoriser des sorts même s'il n'y a pas assez de mana, le skill n'est "utilisé" que pour calculer la régén des PV une fois par tour)."""
    def __init__(self): #Seul le joueur peut avoir ce skill, donc il n'y a qu'une version
        Skill.__init__(self)
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

class Skill_manipulation_epee(Skill):
    """Renforce les attaques réalisées à l'aide d'armes de type épée. Quand le niveau augmente, les dégats infligés avec une épée, la portée des attaques d'épée, la vitesse des attaques d'épée, la priorité des attaques d'épée, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois qu'une attaque est réalisée à l'aide d'une épée."""
    def __init__(self):
        Skill.__init__(self)
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

class Skill_manipulation_lance(Skill):
    """Renforce les attaques réalisées à l'aide d'armes de type lance. Quand le niveau augmente, les dégats infligés avec une lance, la portée des attaques de lance, la vitesse des attaques de lance, la priorité des attaques de lance, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois qu'une attaque est réalisée à l'aide d'une lance."""
    def __init__(self):
        Skill.__init__(self)
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

class Skill_manipulation_bouclier(Skill):
    """Renforce la défense des items de type bouclier. Quand le niveau augmente, les dégats bloqués avec un bouclier, la portée des boucliers (pour un bouclier, la portée permet de protéger une plus grande zone), la vitesse d'utilisation des boucliers, la priorité des boucliers, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois que le skill de bloquage d'attaque est utilisé."""
    def __init__(self):
        Skill.__init__(self)
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

class Skill_manipulation_arme(Skill):
    """Renforce les attaques réalisées à l'aide d'armes (exclue la magie, le stomp, les auras). Quand le niveau augmente, les dégats infligés avec une arme, la portée des attaques d'arme, la vitesse des attaques d'arme, la priorité des attaques d'arme, etc. peuvent être améliorée (juste les dégats pour l'instant).
       C'est un skill semi-passif, qui s'actionne à chaque fois qu'une attaque est réalisée à l'aide d'une arme."""
    def __init__(self):
        Skill.__init__(self)
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

class Skill_ecrasement(Skill):
    """Permet d'écraser (détruire) d'autres agissants ou des murs sur son chemin. Plus le niveau est élevé, moins la différence de priorité entre l'écrseur et l'écrasé doit être élevée pour permettre l'écrasement.
       C'est un skill semi-passif, qui s'actionne quand il y a collision entre l'agissant et un autre agissant ou un mur."""
    def __init__(self):
        Skill.__init__(self)
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

class Skill_observation(Skill):
    """Complément du skill de vision. Permet d'afficher des informations sur ce que voit le skill de vision (PV d'un ennemi ou priorité d'un mur par exemple). Peut aussi rendre visible (certains sorts, objets ou ennemis furtifs par exemple) ou révéler la vraie forme (certains ennemis portent plusieurs couches de déguisements, et le skill d'observation peut donc révéler une fausse forme différente de la forme affichée sans le skill).
       C'est un skill passif, qui s'actionne à chaque tour, après le skill vision. Il renvoit uniquement son niveau, et tous les objets ont différentes informations à afficher selon le niveau de l'observation (faire intervenir la priorité dans le calcul !)."""
    def __init__(self):
        Skill.__init__(self)
        self.gain_xp=0.1 #Il faut observer 100 objets (murs, cases, items, cailloux, agissants, projectiles) pour passer au niveau suivant (progression trop rapide ? ne compter qu'une fois chaque case, objet, etc.)
        self.nom = "Observation"

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau+=1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.niveau

class Skill_analyse(Skill):
    """Fournit des informations sur un mot ou une expression affichée à l'écran. La récurrence est possible, si un ou plusieurs termes de l'analyse sont analysables. Le niveau de l'analyse diminue à chaque récurrence. Le niveau de la première analyse détermine la diminution à chaque récurrence (aucune pour une analyse de niveau 10) et le niveau de chaque analyse détermine les informations affichées.
       Une analyse de niveau 10 permet d'obtenir, par récurrence à partir de n'importe quel terme basique (comme les PV ou les PM qui sont toujours visibles par le joueur), toutes les informations sur les mécaniques du système (les classes, titres, skills et personnages en dehors du système, comme les titres uniques divins/démoniaques, dev ou le skill chanceux ne sont pas analysables par ce skill et leurs effets pourront contredire des vérités générales exprimées dans les descriptions des mécaniques du système).
       C'est un skill actif, qui s'actionne gratuitement, sans temps de latence, fige le jeu pendant son utilisation mais ne l'affecte d'aucune façon."""
    def __init__(self):
        Skill.__init__(self)
        self.mallus_recurrence=10
        self.gain_xp=0.1 #Il faut analyser 100 termes du système pour passer au niveau suivant (combien de termes au total dans le système ? progression trop lente ? ne compter qu'une fois chaque terme et augmenter le niveau en fonction du pourcentage découvert)
        self.nom = "Analyse"

    def get_skin(self):
        return SKIN_SKILL_ANALYSE

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.mallus_recurrence-=1 #Peut-être rendre la progression du mallus moins linéaire ?
            self.niveau+=1

    def utilise(self):
        self.xp_new += self.gain_xp
        return self.mallus_recurrence, self.niveau

class Skill_vol(Skill):
    """Permet de dérober les drops d'un ennemi (sans devoir le tuer ni même le combattre). Nécessite le skill d'observation pour savoir ce qu'on peut voler. 
       C'est un skill actif.""" #Evolue vers les autres skills de vol ? Les offre au fur et à mesure de sa montée de niveau ? Les inclus à partir de certains niveaux ?
    def __init__(self):
        Skill.__init__(self)
        self.latence=11
        self.supériorite=11 #la quantité de priorité que l'agissant doit avoir en plus par rapport à la cible qu'il vole
        self.gain_xp=0.1
        self.nom = "Vol"

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

class Skill_vol_de_priorite(Skill):
    """Permet de dérober la priorité d'un ennemi (ne fonctionne pas sur ceux qui en ont trop ?). Nécessite que le skill d'observation révèle la priorité de l'ennemi.
       C'est un skill actif."""
    def __init__(self):
        Skill.__init__(self)
        self.latence=11
        self.supériorite=11 #la quantité de priorité que l'agissant doit avoir en plus par rapport à la cible qu'il vole. Peut-être la faire passer en négatif ?
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

class Skill_attaque(Skill):
    """Permet d'attaquer avec une arme.
       C'est un skill actif."""
    def __init__(self):
        Skill.__init__(self)
        self.nom = "Attaque"

    def get_skin(self):
        return SKIN_SKILL_ATTAQUE

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau += 1

    def utilise(self):
        self.xp_new += gain_xp_attaque[self.niveau-1]
        return latence_attaque[self.niveau-1],taux_utilisation_attaque[self.niveau-1]

class Skill_stomp(Skill_attaque):
    """Permet d'attaquer la zone avoisinnante sans arme.
       C'est un skill actif."""
    def __init__(self):
        Skill.__init__(self)
        self.nom = "Stomp"

    def get_skin(self):
        return SKIN_SKILL_STOMP

    def evo(self,nb_evo=1):
        for i in range(nb_evo):
            self.niveau += 1

    def utilise(self):
        self.xp_new += gain_xp_stomp[self.niveau-1]
        return latence_stomp[self.niveau-1],taux_utilisation_stomp[self.niveau-1],portee_stomp[self.niveau-1]

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

class Skill_course(Skill):
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

class Skill_lancer(Skill):
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
                    self.xp.append(cadeau)
                elif isinstance(cadeau,Fleche): #On peut gagner un type de flèche avec la montée de niveau du skill ? /!\ Un skill ne connait pas les autres objets du jeu /!\
                    self.ajoute(fleche)
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
                    self.xp.append(cadeau)
                elif isinstance(cadeau,Explosif): #On peut gagner un type d'explosif avec la montée de niveau du skill ?
                    self.ajoute(explosif)
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
    """Permet de créer diverses potions. Coûte du mana ?""" #/!\ À retravailler en profondeur /!\
    def __init__(self,potions=[]):
        Skill.__init__(self)
        self.potions=potions
        self.gain_xp = 0 #L'xp dépend de la potion créée
        self.nom = "Alchimie"

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
                    self.xp.append(cadeau)
                elif isinstance(cadeau,Explosif): #On peut gagner un type d'explosif avec la montée de niveau du skill ?
                    self.ajoute(explosif)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1

    def ajoute(self,potion):
        self.potions.append(potion)

    def utilise(self,xp):
        self.gain_xp = xp
        self.xp_new+=self.gain_xp #On gagne de l'xp, mais combien ? 0.1, est-ce assez ? trop ?
        return self.niveau

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
                    self.xp.append(cadeau)
                elif isinstance(cadeau,Explosif): #On peut gagner un type d'explosif avec la montée de niveau du skill ?
                    self.ajoute(explosif)
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
                    self.xp.append(cadeau)
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
            if len(self.chaine >= 1):
                self.chaine = self.chaine[:-1]
        elif touche == pygame.K_ENTER:
            eval(self.chaine) #/!\ Rajouter les variables globales pour que ça serve à quelque-chose !
            self.chaine = ""
        elif self.chaine.append(pygame.key.name(touche)): #On se limite aux trucs simples pour l'instant !
            self.chaine.append(pygame.key.name(touche))
