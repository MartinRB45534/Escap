import random
from Jeu.Constantes import *
from Jeu.Systeme.Kumo_desu_ga_nanika import *

class Classe:
    """!!! Classe != class !!! Correspond aux classes avec des niveaux, qui évoluent, contiennent des skills, etc."""
    def __init__(self,conditions_evo=[0,10,20,30,40,50,60,70,80,90],skills_intrasecs=[],skills=[],cadeaux_evo=[[],[],[],[],[],[],[],[],[],[]]):
        """conditions_evo : les conditions d'évolution de la classe au niveau supérieur ; si c'est un nombre, indique l'xp nécessaire à l'évolution, si c'est une chaine de caractère, indique la fonction capable d'évaluer la condition
           skills_intrasecs : les skills obtenus automatiquement avec la classe
           cadeux_evo : les récompenses d'évolution ; peuvent être des skills, des classes ou de l'xp""" #Plus vraiment, en fait... À rafraichir
        self.skills=skills
        self.skills_intrasecs=skills_intrasecs
        self.sous_classes=[] #Une classe peut posséder des sous-classes, qui contribueront à son évolution moins qu'à celle de la classe principale
        self.niveau=0 #Le niveau devrais passer à 1 lorsqu'on acquiert la classe
        self.cond_evo=conditions_evo
        self.cad_evo=cadeaux_evo
        self.xp=0 #L'xp commence à 0, évidemment
        self.xp_new=0 #Contabilise l'xp obtenue pendant le tour, pour la propagation
        self.propagation=0.1 #Certaines classes ont un taux de propagation plus important
        self.prep_next_evo() #On prépare déjà la prochaine évolution
        self.curseur = "skills"
        self.skill_courant = 0
        self.skill_intrasec_courant = 0
        self.classe_courante = 0
        self.nom = "classe anonyme"
        
    def gagne_xp(self):
        #On récupère l'xp propagé par les skills,
        for skill in self.skills:
            self.xp_new+=skill.gagne_xp()
        #les skills intrasecs
        for skill in self.skills_intrasecs:
            self.xp_new+=skill.gagne_xp()
        #et par les sous-classes
        for classe in self.sous_classes:
            self.xp_new+=classe.gagne_xp()
        #Qu'on propage vers la classe supérieure
        res = self.xp_new*self.propagation
        #On l'ajoute aussi à son propre xp
        self.xp+=self.xp_new
        self.xp_new=0
        #On en profite pour vérifier si on peut évoluer
        if self.next_evo=="xp" and self.niveau < 10:
            self.check_evo()
        return res
        
    def vire_xp(self):
        for skill in self.skills:
            skill.xp_new = 0
        for skill in self.skills_intrasecs:
            skill.xp_new = 0
        for classe in self.sous_classes:
            classe.vire_xp()
        self.xp_new=0 #Pas nécessaire, je suppose ?

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

    def evo(self,nb_evo=1):
        """fonction qui procède à l'évolution"""
        for i in range(nb_evo):
            for cadeau in self.cad_evo[self.niveau]:
                if issubclass(cadeau,Classe):
                    self.sous_classes.append(cadeau)
                    cadeau.evo() #La classe devrait encore être au niveau 0
                elif issubclass(cadeau,Skill):
                    self.skills.append(cadeau)
                    cadeau.evo() #Le skill devrait encore être au niveau 0
                elif isinstance(cadeau,int):
                    self.xp.append(cadeau)
                else:
                    print("Le père Noël s'est trompé...")
            self.niveau+=1
            for skill in self.skills_intrasecs:
                skill.evo()

    def utilise_courant(self):
        if self.curseur == "in_skills":
            return type(self.skills[self.skill_courant])
        elif self.curseur == "in_skills_intrasecs":
            return type(self.skills_intrasecs[self.skill_intrasec_courant])
        if self.curseur == "in_classes":
            return self.classes[self.classe_courante].utilise_courant()

    def deplace(self,direction):
        res = False
        if self.curseur == "skills":
            if direction == HAUT:
                self.curseur = "skills_intrasecs"
            elif direction == BAS:
                self.curseur = "classes"
            elif direction == IN:
                self.curseur = "in_skills"
            elif direction == OUT:
                res = True
        elif self.curseur == "skills_intrasecs":
            if direction == HAUT:
                self.curseur = "classes"
            elif direction == BAS:
                self.curseur = "skills"
            elif direction == IN:
                self.curseur = "in_skills_intrasecs"
            elif direction == OUT:
                res = True
        elif self.curseur == "classes":
            if direction == HAUT:
                self.curseur = "skills"
            elif direction == BAS:
                self.curseur = "skills_intrasecs"
            elif direction == IN:
                self.curseur = "in_classes"
            elif direction == OUT:
                res = True
        elif self.curseur == "in_skills":
            if direction == OUT:
                self.curseur = "skills"
            elif direction == BAS:
                self.skill_courant += 1
                if self.skill_courant >= len(self.skills):
                    self.skill_courant = 0
            elif direction == HAUT:
                self.skill_courant -= 1
                if self.skill_courant < 0:
                    self.skill_courant = len(self.skills)-1
        elif self.curseur == "in_skills_intrasecs":
            if direction == OUT:
                self.curseur = "skills_intrasecs"
            elif direction == BAS:
                self.skill_intrasec_courant += 1
                if self.skill_intrasec_courant >= len(self.skills_intrasecs):
                    self.skill_intrasec_courant = 0
            elif direction == HAUT:
                self.skill_intrasec_courant -= 1
                if self.skill_intrasec_courant < 0:
                    self.skill_intrasec_courant = len(self.skills_intrasecs)-1
        elif self.curseur == "in_classes":
            if direction == OUT:
                self.curseur = "classes"
            elif direction == IN:
                self.curseur = "in_classe"
            elif direction == BAS:
                self.classe_courante += 1
                if self.classe_courante >= len(self.sous_classes):
                    self.classe_courante = 0
            elif direction == HAUT:
                self.classe_courante -= 1
                if self.classe_courante < 0:
                    self.classe_courante = len(self.sous_classes)-1
        elif self.curseur == "in_classe":
            if self.sous_classes[self.classe_courante].deplace(direction):
                self.curseur = "in_classes"
        return res

    def get_skills_actifs(self):
        skills = []
        for skill in self.skills:
            if isinstance(skill,(Skill_magie,Skill_analyse,Skill_vol,Skill_stomp,Skill_attaque,Skill_blocage,Skill_lancer,Skill_course)):
                skills.append(skill) #Ne prend pas en compte la création d'items pour l'instant !
        for skill in self.skills_intrasecs:
            if isinstance(skill,(Skill_deplacement,Skill_ramasse,Skill_soin,Skill_regeneration_MP,Skill_reanimation,Skill_reanimation_renforcee)):
                skills.append(skill)
        for classe in self.sous_classes:
            skills += classe.get_skills_actifs()
        return skills

    def debut_tour(self):
        """Fonction qui renvoie tous les skills qui ont besoin d'être appelés au début du tour (juste les auras pour l'instant)."""
        skills = []
        for skill in self.skills:
            if isinstance(skill,Skill_debut_tour):
                skills.append(skill)
        for skill in self.skills_intrasecs:
            if isinstance(skill,Skill_debut_tour):
                skills.append(skill)
        for classe in self.sous_classes:
            skills += classe.debut_tour()
        return skills

class Classe_principale(Classe):
    """La classe principale de l'agissant. Le niveau d'un agissant est égal au niveau de sa classe principale. Pour les agissants capables de s'améliorer, l'utilisation de la procédure gagne_xp de la classe principale provoque récursivement l'utilisation de cette procédure sur tous les sous-classe est skills de l'agissant. L'amélioration de la classe principale provoque une amélioration des statistiques de l'agissant.
       Pour le joueur, une amélioration de la classe principale permet de choisir une récompense dans l'arbre de compétence ou dans l'arbre élémental (ou deux dans l'arbre élémental avec la classe élémentaliste)."""
    def __init__(self,identite,niveau):
        skills_intrasecs = []
        skills = []
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        if identite == 'joueur' :
            self.evolutif = False

            #Skills intrasecs (leur niveau est lié à celui de la classe principale) :
            deplacement = Skill_deplacement() #On crée un skill de déplacement
            skills_intrasecs.append(deplacement)
            vision = Skill_vision() #On crée un skill de vision
            skills_intrasecs.append(vision)
            ramasse = Skill_ramasse() #On crée une skill de ramassage
            skills_intrasecs.append(ramasse)

            #Autres skills :
            stomp = Skill_stomp() #On crée un skill de stomp
            stomp.evo() #On le passe au niveau 1
            skills.append(stomp)
            attaque = Skill_attaque() #On crée un skill d'attaque par le biais d'armes
            attaque.evo() #On le passe au niveau 1
            skills.append(attaque)
            magie = Skill_magie() #On crée un skill d'utilisation de magie
            magie.evo() #On le passe au niveau 1
            skills.append(magie)
            course = Skill_course() #On crée un skill de course
            course.evo() #On le passe au niveau 1
            skills.append(course)

##            #!!! Attention : ce qui se passe ici est extérieur au système !
##            if malchance_forcee : #Après la chance, la malchance...
##                malchanceux = Skill_malchanceux() #On crée un mystérieux skill de mauvais augure non-référencé...
##                malchanceux.evo() #On augmente même son niveau...
##                malchance_forcee = False #Mais on ne le fera pas la prochaine fois, promis !
##                skills.append(malchanceux)
##            elif random.random()<0.01 or chance_forcee : #On peut espérer, ou forcer le destin dans le fichier des constantes.
##                chanceux = Skill_chanceux() #On crée un mystérieux skill non-référencé, mais au moins son nom est encourageant !
##                chanceux.evo() #On le passe au niveau 1
##                malchance_forcee = True #Profitons bien de la partie, la prochaine risque d'être plus difficile...
##                skills.append(chanceux)
##            #Le système peut quand même voir les conséquences de ces actions mystérieuses.

        elif identite == 'receptionniste':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            attaque = Skill_attaque()
            attaque.evo()
            skills.append(attaque)

        elif identite == 'paume':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)

        elif identite == 'peureuse':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            magie = Skill_magie()
            magie.evo()
            skills.append(magie)

        elif identite == 'codeur':
            self.evolutif = False
            omnipotence = Invite_de_commande()
            omnipotence.evo()
            skills.append(omnipotence)
            omniscience = Skill_vision() #Lui faire un vrai skill d'omniscience à l'occasion
            skills_intrasecs.append(omniscience)

        elif identite == 'encombrant':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            attaque = Skill_attaque()
            attaque.evo()
            skills.append(attaque)

        elif identite == 'alchimiste':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            magie = Skill_magie()
            magie.evo()
            skills.append(magie)
            alchimie = Skill_alchimie()
            alchimie.evo()
            skills.append(alchimie)

        elif identite == 'peste':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            magie = Skill_magie()
            magie.evo()
            skills.append(magie)

        elif identite == 'bombe_atomique':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            magie = Skill_magie()
            magie.evo()
            skills.append(magie)

        elif identite == 'marchand':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            stomp.evo()
            skills.append(stomp)
            attaque = Skill_attaque()
            attaque.evo()
            skills.append(attaque)
            echange = Skill_echange()
            echange.evo()
            skills.append(echange)

        elif identite == 'gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)

        elif identite == 'sentinelle_gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)

        elif identite == 'premier_monstre':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)

        elif identite == 'troisieme_monstre':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)

        elif identite == 'guerrier_gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)

        elif identite == 'explorateur_gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)

        elif identite == 'mage_gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            magie = Skill_magie()
            skills_intrasecs.append(magie)

        elif identite == 'deuxieme_monstre':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            magie = Skill_magie()
            skills_intrasecs.append(magie)

        elif identite == 'shaman_gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            magie = Skill_magie()
            skills_intrasecs.append(magie)

        elif identite == 'chef_gobelin':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            attaque = Skill_attaque()
            skills_intrasecs.append(attaque)
            #Lui rajouter un skill de dirigeant ?

        elif identite == 'slime':
            self.evolutif = False #Changer ça à l'occasion
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            division = Skill_divide()
            skills_intrasecs.append(division)
            absorption = Skill_absorb()
            skills_intrasecs.append(absorption)
            fusion = Skill_merge()
            skills_intrasecs.append(fusion)

        elif identite == 'ombriul':
            self.evolutif = False
            deplacement = Skill_deplacement()
            skills_intrasecs.append(deplacement)
            vision = Skill_vision()
            skills_intrasecs.append(vision)
            stomp = Skill_stomp()
            skills_intrasecs.append(stomp)
            magie = Skill_magie()
            skills_intrasecs.append(magie)

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)
        self.evo(niveau)

##    def __init__(self,skills_intrasecs=[],skills=[],evolutif=False,identite=None,niveau=0): #Si l'agissant n'est pas capable d'évoluer, il n'a pas besoin de conditions ou de cadeaux d'évolution. Comme les agissants capables d'évoluer sont rares (pour l'instant seulement le joueur) on peut faire la liste exhaustive.
##        self.evolutif = evolutif
##        if self.evolutif :
##            elif identite == "kumoko" : #aka Nightmare of the Labyrinth, kumoko est le personnage pricipal de kumo desu ga, nanika. C'est une arraignée et la mère des Nightmare Vestiges. Elle réside dans un niveau rempli de fils d'arraignés, et devient hostile au joueur si 10 de ses enfants sont tués. Elle dispose de skills uniques et surpuissants qui la rendent très difficile à vaincre.
##                cond_evo = [0,10,20,30,40,50,60,70,80,90] #Est-ce qu'elle commence au niveau 1 ? Ou déjà plus puissante ? Même question pour ses skills.
##                #On ne peux pas reporter exactement les skills du light novel dans ce jeu, donc on va créer un skill par comportement possible :
##                deplacement = Skanda() #D'après le nom du skill qui lui permet d'améliorer sa vitesse plus efficacement.
##                vision = Wisdom() #D'après le nom du skill qu'elle a obtenu de D et qui lui permet de connaitre la position de tous ses ennemis.
##                magies = {} #Qaund j'aurai codé les magies, penser à ajouter : Heretic_Magic (attaque directement "l'âme", c'est-à-dire ignore toutes les défenses et affinités) ;
##                                                                             # Earth_magic (affinité à la terre) ;
##                                                                             # Dark_magic (affinité à l'ombre) ;
##                                                                             # Poison_magic ;
##                                                                             # Healing_magic ;
##                                                                             # Spacial_magic (principalement la téléportation) ;
##                                                                             # Abyss_magic (détruit et empêche toute résurrection/réanimation/immortalité, mais kumoko peut être prise dans l'attaque).
##                                                                             # en trouvant à chaque fois les sorts correspondants et ceux qui font sens dans ce jeu
##                magie = Height_of_Occultism(magies) #D'après le nom du skill qui lui sert à lancer des sorts
##                toile = Divine_Thread_Weaving() #D'après le nom du skill qui lui permet de produire et d'utiliser sa toile (ici utilisée pour immobiliser, bloquer un chemin, attaquer)
##                mauvais_oeil1 = Jinx_Evil_Eye() #D'après le nom du skill qui lui permet d'absorber les MP, PV, SP de ses ennemis.
##                mauvais_oeil2 = Inert_Evil_Eye() #D'après le nom du skill qui lui permet de paralyser ses ennemis.
##                mauvais_oeil3 = Repellent_Evil_Eye() #D'après le nom du skill qui lui permet d'appliquer une force dans une direction voulue (ici, pour déplacer un ennemi ou l'immobiliser).
##                mauvais_oeil4 = Annihilating_Evil_Eye() #D'après le nom du skill qui lui permet d'infliger une attaque de type Rot sur un ennemi au prix de l'un de ses yeux (ici pour éliminer un ennemi trop puissant au prix d'un oeil).
##                mauvais_yeux = Evil_Eye() #À chaque tour, décide des cibles des Evil_Eyes.
##                tranche = Scythe() #Du nom de ses pates avant, qui infligent beaucoup de dégats.
##                orgueil = Pride() #D'après le nom du skill qui lui permet de monter en niveau plus rapidement. Ici, augmente les xp gagnés et la propagation.
##                paresse = Sloth() #D'après le nom du skill qui lui permet de ralentir le monde autour d'elle et d'accélerer toutes les diminutions de valeurs du système. Ici juste le ralentissement ?
##                piege = Taboo() #D'après le nom du skill qui révèle la vérité sur le monde. Ici, utilisé comme un piège contre les voleurs, qui perdront la partie s'ils l'acquièrent.
##                immortel = Immortality() #D'après le nom du skill qui l'empêche de mourir à moins qu'on attaque son âme.
##                ponte = Egg_Laying() #D'après le nom du skill qui lui permet de pondre des oeufs. Ici, elle pond chacun de ses dix premiers oeufs au moment où une toile d'araignée est détruite, s'il n'y a pas d'autre oeufs. Après, elle attaque le joueur mais s'arrète de temps en temps pour pondre des oeufs, qui lui servent nottament à se protéger de l'Abyss_magic.
##                for skill in [deplacement,vision,magie,toile,mauvais_oeil1,mauvais_oeil2,mauvais_oeil3,mauvais_oeil4,mauvais_yeux,tranche,orgueil,paresse,piege,immortel,ponte]:
##                    skill.evo()
##                    skills.append(skill)
##                Classe.__init__(self,cond_evo,skills_intrasecs,skills)
##            else :
##                print(identite+" ? Qu'est-ce que c'est que ça ?")
##        else :
##            if identite == "nightmare_vestige": #Créés par les oeufs de kumoko quand ils éclosent, se battent pour kumoko mais sont capables de la tuer. Tous leurs skills sont intrasecs, et augmentent avec la classe principale au niveau de kumoko quand elle les crée.
##                skills = [Hatching()]
##                skills_intrasecs = [Lesser_Skanda(),Lesser_Wisdom(),Lesser_Height_of_Occultism({}),Lesser_Divine_Thread_Weaving(),Lesser_Scythe()] #Lui donner des magies de kumoko au hasard ? Pareil pour les Evil_Eyes ? En tous cas l'Abyss_magic.
##                Classe.__init__(self,[0]*10,skills_intrasecs,skills) #Hatching() est le compte à rebours avant l'éclosion. Tant qu'il est de niveau < 10, l'apparence du vestige est un oeuf (item). Quand il éclot, il prend son apparence d'arraignée blanche. S'il éclot dans un inventaire, il sera du côté de son possesseur.
##            self.evo(niveau)

    def gagne_xp(self):
        if self.evolutif :
            Classe.gagne_xp(self)
        else:
            Classe.vire_xp(self)

class Artificier(Classe):
    """La classe des utilisateurs d'explosifs de haut niveau. Le skill de création d'explosif peut lui être transféré. La classe apporte des bonus lors de l'utilisation d'explosifs."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        creation_explo = Skill_creation_d_explosifs()
        lancer = Skill_lancer()
        skills = [lancer,creation_explo] #Les skills sont au niveau 0, ainsi le controleur proposera de les réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_explosifs()

        skills_intrasecs = [boosts]

        cad_evo = [[],[],[],[],[],[],[],[],[],[]] #Rajouter des explosifs

        Classe.__init__(self,cond_evo,skills_intrasecs,skills,cad_evo)

        self.nom = "Artificier"

class Archer(Classe):
    """La classe des utilisateurs de flèches de haut niveau. Le skill de création de flèches peut lui être transféré. La classe apporte des bonus lors de l'utilisation de flèches."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        creation_fleches = Skill_creation_de_fleches()
        lancer = Skill_lancer()
        skills = [lancer,creation_fleches] #Les skills sont au niveau 0, ainsi le controleur proposera de les réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_fleches()

        skills_intrasecs = [boosts]

        cad_evo = [[],[],[],[],[],[],[],[],[],[]] #Rajouter des flèches

        Classe.__init__(self,cond_evo,skills_intrasecs,skills,cad_evo)

        self.nom = "Archer"

class Sniper(Classe):
    """La classe des utilisateurs de flèches de très haut niveau. Le skill de création de flèches peut lui être transféré. La classe apporte des bonus lors de l'utilisation de flèches."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        creation_fleches = Skill_creation_de_fleches()
        lancer = Skill_lancer() #Peut-être le remplacer par une version plus puissante, mais lente ?
        skills = [lancer,creation_fleches] #Les skills sont au niveau 0, ainsi le controleur proposera de les réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_fleches_sniper()

        skills_intrasecs = [boosts]

        cad_evo = [[],[],[],[],[],[],[],[],[],[]] #Rajouter des flèches

        Classe.__init__(self,cond_evo,skills_intrasecs,skills,cad_evo)

        self.nom = "Sniper"

class Epeiste(Classe):
    """La classe des utilisateurs d'épées. Le skill de manipulation d'épée ou le skill de manipulation d'armes peut lui être transféré. La classe apporte des bonus lors de l'utilisation d'épées (pour l'instant juste des dégats)"""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        epee = Skill_manipulation_epee()
        arme = Skill_manipulation_arme()
        skills = [epee,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_epee()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Epéiste"

class Lancier(Classe):
    """La classe des utilisateurs de lances. Le skill de manipulation de lance ou le skill de manipulation d'armes peut lui être transféré. La classe apporte des bonus lors de l'utilisation de lances (pour l'instant juste des dégats)"""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        lance = Skill_manipulation_lance()
        arme = Skill_manipulation_arme()
        skills_intrasecs = [lance,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_lance()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Lancier"

class Porteur_de_bouclier(Classe):
    """La classe des utilisateurs de boucliers. Le skill de manipulation de bouclier ou le skill de manipulation d'armes peut lui être transféré. La classe apporte des bonus lors de l'utilisation de boucliers (pour l'instant juste des dégats bloqués en plus)"""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        bouclier = Skill_manipulation_bouclier()
        arme = Skill_manipulation_arme()
        skills = [bouclier,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_bouclier()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Porteur_de_bouclier"

class Homme_d_arme(Classe):
    """La classe des utilisateurs d'arme. Les skill de manipulation d'épée, de lance et de bouclier ou le skill de manipulation d'armes peuvent lui être transféré. La classe apporte des bonus lors de l'utilisation d'armes (pour l'instant juste des dégats supplémentaires/ dégats bloqués en plus)"""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        epee = Skill_manipulation_epee()
        lance = Skill_manipulation_lance()
        bouclier = Skill_manipulation_bouclier()
        arme = Skill_manipulation_arme()
        skills = [epee,lance,bouclier,arme] #Le skill est au niveau 0, ainsi le controleur proposera de le réunir avec un skill identique de plus haut niveau si l'agissant en a, puis détruira tous les skills de niveau 0.

        boosts = Skill_boost_armes()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Homme d'armes"

class Enchanteur(Classe):
    """La classe des utilisateurs d'enchantements. Améliore l'efficacité des enchantements."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        boosts = Skill_boost_enchantements()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs)

        self.nom = "Enchanteur"

class Soutien(Classe):
    """La classe des soutiens (par opposition aux tanks et aux dps). Boost les sorts de soutien (buff et soin des alliés, débuff des ennemis)."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #À adapter

        boosts = Skill_boost_soutien()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs)

        self.nom = "Soutien"

class Ange(Classe):
    """La classe des soutiens de haut niveau. Offre des skills (donc sans coût de mana) équivalents aux sorts de soutien classiques (débuffs exclus). Réduit drastiquement le temps nécessaire pour lancer les sorts de soutien classiques (débuffs exclus)."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre des bonnes actions (soin, résurection, etc.) en guise de conditions ?

        boost = Skill_boost_ange()
        soin = Skill_soin()
        regen_MP = Skill_regeneration_MP()
        aura = Skill_aura_divine()

        skills_intrasecs = [boost,soin,regen_MP,aura]

        Classe.__init__(self,cond_evo,skills_intrasecs)

        self.nom = "Ange"

class Elementaliste(Classe):
    """La classe des élémentalistes. Boost légèrement les affinités élémentales, renforce légèrement les skills et classes venues de l'arbe des éléments, permet de sélectionner deux feuilles de l'arbre des éléments par niveauau lieu d'une."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre la possession de classes d'élémental comme condition des niveaux 4,7 et 10 (respectivement 1, 2 et 3 classes) ?

        skills = []
        for element in []: #remplacer par les éléments quand je les aurai créés, ainsi que les effets
            skills.append(Skill_aura_elementale(element))
            skills.append(Skill_affinite_elementale(element))

        boosts = Skill_boost_elementaliste()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Elémentaliste"

class Elemental(Classe):
    """Le classe des élémentaux. Les skills d'aura élémentale et d'affinité élémentale peuvent lui être transférés."""
    pass

class Elemental_de_terre(Elemental):
    """La classe des élémentaux de terre."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        skills = []

        boosts = Skill_boost_elemental_terre()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Elémental_de_terre"

class Elemental_de_feu(Elemental):
    """La classe des élémentaux de feu."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        skills = []

        boosts = Skill_boost_elemental_feu()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Elémental_de_feu"

class Elemental_de_glace(Elemental):
    """La classe des élémentaux de glace."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        skills = []

        boosts = Skill_boost_elemental_glace()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Elémental_de_glace"

class Elemental_d_ombre(Elemental):
    """La classe des élémentaux d'ombre."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        skills = []

        boosts = Skill_boost_elemental_ombre()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Elémental_d'ombre"

class Magicien(Classe):
    """La classe des utilisateurs de magie (hors enchantements). Plutôt axé sur l'attaque "brute". Renforce les magies (hors enchantements), particulièrement les magies d'attaques. Le skill magie peut lui être transféré."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        magie = Skill_magie()

        skills = [magie]

        boosts = Skill_boost_magicien()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Magicien"

class Necromancien(Classe):
    """La classe des sorciers fantômes immortels inhumains avec une affinité à l'ombre et des magies d'ombre (les conditions pour que le joueur l'acquiert sont très strictes, mais les monstres nécromanciens sont plus courants). Les nécromanciens peuvent réanimer les cadavres et potentiellement les convertir à leur cause au passage."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre des conditions sur le nombre de morts vivants qui suivent le nécromancien ou le nombre de réanimations pratiquées ?

        immortalite = Skill_immortel() #Les nécromanciens autres que le joueur ne possèdent pas ce skill, et ne peuvent donc pas le transférer.

        skills = [immortalite]

        boosts = Skill_boost_necromancien()
        reanimation = Skill_reanimation()

        skills_intrasecs = [boosts,reanimation]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Nécromancien"

class Maitre_de_la_mort(Classe):
    """Classe rare, accordée aux Nécromanciens de niveau 10 (niveau de classe) qui remplissent certaines conditions (obtention par titre)."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90] #Mettre des conditions sur le nombre de morts vivants qui suivent le nécromancien ou le nombre de réanimations pratiquées ?

        immortalite = Skill_immortel() #Seul le joueur peut obtenir cette classe. Il possède forcément le skill immortel pour en arriver là.

        skills = [immortalite]

        boosts = Skill_boost_maitre_de_la_mort()
        reanimation = Skill_reanimation_renforcee() #Les skills du maitre de la mort sont plus puissants que ceux du nécromancien

        skills_intrasecs = [boosts,reanimation]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Maitre de la mort"

class Assassin(Classe):
    """La classe des sorciers axés sur l'assassinat. Renforce les effets de morts instantannée, comme le sort d'instakill ou l'aura d'instakill, en réduisant la supériroté nécessaire à leur fonctionnement."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        boosts = Skill_boost_instakill()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs)

        self.nom = "Assassin"

class Voleur(Classe):
    """La classe des voleurs. Renforce les skills de vols. Les skills de vols peuvent lui être transférés."""
    def __init__(self):
        cond_evo = [0,10,20,30,40,50,60,70,80,90]

        vol = Skill_vol()
        vol_priorite = Skill_vol_de_priorite() #Rajouter les autres skills de vols s'ils ne sont pas inclus dans ceux là.

        skills = [vol,vol_priorite]

        boosts = Skill_boost_vol()

        skills_intrasecs = [boosts]

        Classe.__init__(self,cond_evo,skills_intrasecs,skills)

        self.nom = "Voleur"

def trouve_skill(classe,type_skill):
    trouve = None
    for skill in classe.skills:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
            trouve = skill
    for skill in classe.skills_intrasecs:
        if isinstance(skill,type_skill) and skill.niveau > 0: #On ne devrait pas avoir de skill a 0 mais on ne sait jamais.
            trouve = skill
    if trouve == None:
        for sous_classe in classe.sous_classes: #On récurse la recherche dans les sous-classes.
            trouve_bis = trouve_skill(sous_classe,type_skill)
            if trouve_bis != None:
                trouve = trouve_bis
    return trouve
