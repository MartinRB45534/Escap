from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Jeu.Entitee.Entitees import *

from Jeu.Esprit.Esprit import *

class Esprit_type(Esprit):
    """Un esprit caricatural, pour les besoins de mes expériences."""
    def __init__(self,nom:str,niveau:int,controleur:Controleur,position:Position):
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        corps:List[Agissant] = []
        if niveau == 1:
            corps = [Tank(position,1),Dps(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Tank(position,2),Tank(position,1),Dps(position,2),Dps(position,2),Soigneur(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = position+i*BAS
            i+=1

class Esprit_sans_scrupule(Esprit_type):
    """Un esprit qui s'en prend principalement aux soigneurs et aux soutiens."""

    def antagonise_supports(self,offense):
        offenseur = self.controleur[offense[0]]
        for effet in offenseur.effets:
            if isinstance(effet,Dopage):
                ID = effet.responsable
                if ID != offense[0] and effet.phase == "affiche":
                    responsabilite = (effet.taux_degats-1)*offense[1]
                    if ID in self.ennemis:
                        self.ennemis[ID][0] += responsabilite
                    else:
                        self.ennemis[ID] = [responsabilite,0]
            elif isinstance(effet,Soin):
                ID = effet.responsable
                if ID != offense[0] and effet.phase == "affiche":
                    responsabilite = (effet.gain_pv/offenseur.pv)*offense[1]
                    if ID in self.ennemis:
                        self.ennemis[ID][0] += responsabilite
                    else:
                        self.ennemis[ID] = [responsabilite,0]

class Esprit_bourrin(Esprit_type): #À supprimer, plus nécessaire
    """Un esprit sans soigneurs ni soutiens."""
    def __init__(self,nom:str,niveau:int,controleur:Controleur,position:Position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        corps:List[Agissant] = []
        if niveau == 1:
            corps = [Dps(position,1),Dps(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Dps(position,2),Dps(position,2),Dps(position,2),Dps(position,1),Dps(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = position+i*BAS
            i+=1

class Esprit_defensif(Esprit_type): #À supprimer, plus nécessaire
    """Un esprit sans soigneurs ni soutiens."""
    def __init__(self,nom:str,niveau:int,controleur:Controleur,position,Position):
        # Tout le monde spawn au même endroit, changer ça !
        self.nom = nom
        self.controleur = controleur
        self.oubli = niveau
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        corps:List[Agissant] = []
        if niveau == 1:
            corps = [Tank(position,1),Tank(position,1),Dps(position,1)]
        if niveau == 2:
            corps = [Tank(position,2),Tank(position,2),Dps(position,2),Tank(position,1),Dps(position,1)]
        controleur.ajoute_entitees(corps)
        IDs = [corp.ID for corp in corps]
        self.ajoute_corps(IDs)
        i = 0
        random.shuffle(corps)
        for corp in corps:
            corp.position = position+i*BAS
            i+=1

class Esprit_solitaire(Esprit_type):
    """Un esprit avec un unique corp."""
    def __init__(self,nom:str,corp:int,controleur:Controleur):
        self.nom = nom
        self.controleur = controleur
        self.oubli = 5
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        self.ajoute_corp(corp)

class Esprit_simple(Esprit_type):
    """Un esprit avec les corps qu'on lui donne."""
    def __init__(self,nom:str,corps:List[int],prejuges:List[str],controleur:Controleur):
        self.nom = nom
        self.controleur = controleur
        self.oubli = 5
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = prejuges
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        self.ajoute_corps(corps)

class Esprit_humain(Esprit_type):
    """Un esprit qui dirige un ou plusieurs humains. Peut interragir avec d'autres esprits humains."""
    def __init__(self,corp:int,controleur:Controleur): #Les humains commencent tous séparément, donc ils ont leur propre esprit au début
        self.nom:str = controleur[corp].identite
        self.controleur = controleur
        self.oubli = 5 #Faire dépendre de l'humain
        self.ennemis = {}
        self.dispersion_spatiale = 0.9
        self.prejuges = [] #Peut-être quelques boss ?
        self.pardon = 0.9
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        Esprit_type.ajoute_corp(self,corp)
        self.chef = corp #Les humains ne peuvent pas s'empêcher d'avoir des chefs

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant:Agissant = self.controleur[corp]
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                self.antagonise_attaquant(offense)
                self.antagonise_supports(offense)
                if self.peureuse():
                    for coennemi in self.controleur.get_esprit(self.controleur[offense[0]].esprit).corps.keys():
                        if not coennemi in self.ennemis:
                            self.ennemis[coennemi] = [0.01,0]

    def merge(self,nom:str): #Regroupe deux esprits, lorsque des humains forment un groupe
        if self.nom != nom:
            esprit = self.controleur.get_esprit(nom)
            for corp in esprit.corps.keys():
                self.ajoute_corp(corp)
                if corp in self.ennemis.keys():
                    self.ennemis.pop(corp)
            for ennemi in esprit.ennemis.keys():
                if ennemi in self.corps.keys():
                    self.ennemis.pop(ennemi)
                elif ennemi in self.ennemis.keys():
                    self.ennemis[ennemi] = max(self.ennemis[ennemi],esprit.ennemis[ennemi])
                else:
                    self.ennemis[ennemi] = esprit.ennemis[ennemi]
            for vue in esprit.vue.values():
                if vue.id in self.vue:
                    self.maj_vue(vue)
                else:
                    self.ajoute_vue(vue)
            self.controleur.esprits.pop(nom)
            self.chef = self.elit()

    def elit(self):
        if 2 in self.corps.keys():
            self.chef = 2 #Le joueur est le chef par défaut ! Ah mais non mais !
        else:
            self.chef = None
            candidats:List[Humain] = []
            for corp in self.corps.keys():
                agissant:Agissant = self.controleur[corp]
                if "humain" in agissant.get_especes():
                    candidats.append(agissant) #Les humains sont les seuls à pouvoir diriger un esprit d'humain. Et les seuls à voter, aussi.
            votes_max = 0
            for candidat in candidats:
                votes = 0
                place = candidat.place
                for votant in candidats:
                    votes += votant.appreciations(place)
                if votes > votes_max:
                    self.chef = candidat.ID #/!\ Éviter les chefs morts, à l'occasion /!\
                    votes_max = votes

    def exclus(self,corp): #C'est super sympa, les relations humaines !
        #Il va falloir créer un nouvel esprit pour l'humain exclus
        #Et il va falloir donner un nom à ce nouvel esprit
        #Les esprits humains sont nommés d'après leur porteur originel
        humain:Humain = self.controleur[corp]
        if humain.identite != self.nom: #Tout va bien
            self.controleur.esprits[humain.identite]=Esprit_humain(corp,self.controleur)
        else:
            self.controleur.esprits[humain.identite]=Esprit_humain(corp,self.controleur)
            self.elit() #Autant changer tous les rapports de force d'un coup
            self.nom = self.controleur[self.chef].identite
            self.controleur.esprits[self.nom] = self

    def oublie(self):
        for case in self.vue:
            if case[2] > 0:
                if self.peureuse():
                    case[2] = self.oubli
                else:
                    case[2] -= 1
            if case[2] <= 0:
                case[1] = 0
                case[4] = 0
                case[5] = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
                case[6] = []
            case[3] = [0,0,0,0,0,False]
            case[7] = []
            case[8] = False

    def peureuse(self):
        return 5 in self.corps.keys() and self.corps[5] in ["humain","attente","fuite","deplacement","attaque","vivant"] #J'ai un doute sur la possibilité des deux derniers mais bon...

    def decide(self):
        for corp in self.corps.keys():
            if corp == 2:
                joueur = self.controleur.joueur
                # joueur.recontrole()
                if joueur.skill_courant != None and issubclass(joueur.skill_courant,(Skill_course,Skill_deplacement)) and joueur.position.lab in self.vue.keys():
                    cible = self.vue[joueur.position][5][joueur.dir_regard][4]
                    if cible and cible.lab in self.vue.keys():
                        self.vue[cible][8]=True
            elif self.corps[corp] in ["attaque","fuite","soin","soutien"]:
                Esprit.deplace(self,corp)
            elif self.corps[corp] == "humain":
                self.deplace_humain(corp)
            elif self.corps[corp] == "attente": #Les pnjs avant de rejoindre le joueur
                if self.ennemis != {}: #Si on a des ennemis, c'est qu'on a été attaqué !
                    Esprit.deplace(self,corp)

    def deplace_humain(self,ID_humain):
        humain:Humain = self.controleur[ID_humain]
        humain.skill_courant = None
        if humain.identite == "heros":
            # humain.recontrole() #Encore ?
            humain.statut_humain = "joueur"
        else:
            humain.statut_humain = "proximite"
            if humain.mouvement == 0: #0 pour aller vers, et 1 pour chercher
                if isinstance(humain.cible_deplacement,int):
                    if not(self.controleur.est_item(humain.cible_deplacement)):
                        cible = self.controleur[humain.cible_deplacement].get_position()
                        portee = 7
                    else:
                        cible = humain.get_position()
                        portee = 2 #C'est juste pour qu'il puisse aller où il veut
                else:
                    cible = humain.cible_deplacement
                    portee = 5
                pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
            elif humain.mouvement == 1:
                pos_cibles = [humain.get_position()]
                humain.statut_humain = "exploration"
            else:
                if isinstance(humain.cible_deplacement,int):
                    if not(self.controleur.est_item(humain.cible_deplacement)):
                        cible = self.controleur[humain.cible_deplacement].get_position()
                        portee = 1
                    else:
                        cible = humain.get_position()
                        portee = 2 #C'est juste pour qu'il puisse aller où il veut
                else:
                    cible = humain.cible_deplacement
                    portee = 1
                pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
            if humain.position in pos_cibles: #Tout va bien, on y est ! On peut combattre, par exemple.
                Esprit.deplace(self,ID_humain)
            else:
                res = "recherche"
                self.resoud(cible,10,4)
                position = humain.get_position()
                case = self.vue[position]
                repoussante = case[8]
                cases = [[-1,case[0],case[3][0],case[3][1],-case[3][2],case[3][2],-case[3][3],case[3][3],case[3][4]]]
                dirs = []
                importance = 0
                fuite = humain.veut_fuir(case[3][2])
                attaque = humain.veut_attaquer(case[3][2])
                humain.statut_humain = "en chemin"
                if case[3][4] == 0:
                    humain.statut_humain = "perdu"
                    if humain.ID == 4:
                        humain.statut_humain = "paume"
                for i in DIRECTIONS:
                    mur = case[5][i][self.resolution]
                    if mur:
                        if mur.lab in self.vue.keys():
                            case_pot = self.vue[mur]
                            entitees = case_pot[6]
                            libre = True
                            for ID_entitee in entitees:
                                entitee = humain.controleur[ID_entitee]
                                if issubclass(entitee.get_classe(),Non_superposable): #On ne peut pas aller sur cette case
                                    libre = False
                                    if issubclass(entitee.get_classe(),Agissant): #Elle est occupée par un agissant
                                        if humain.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                            if attaque: #Et le feu vert pour l'attaquer
                                                if self.ennemis[ID_entitee][0] > importance:
                                                    importance = self.ennemis[ID_entitee][0]
                                                    humain.attaque(i)
                                                    res = "attaque"
                                            elif fuite : #Et un ordre de fuite !
                                                res = "fuite"
                                        elif humain.mouvement == 2 and ((ID_entitee == humain.cible_deplacement and ID_entitee == 2) and humain.peut_voir(i)): #Le PNJs peut enfin parler au joueur
                                            self.controleur.joueur.interlocuteur = humain
                                            self.controleur.set_phase(DIALOGUE)
                                            humain.start_dialogue()
                                            humain.dir_regard = i
                                            self.controleur.joueur.dir_regard = i+2
                            if libre:
                                cases.append([i,case_pot[0],case_pot[3][0],case_pot[3][1],-case_pot[3][2],case_pot[3][2],-case_pot[3][3],case_pot[3][3],case_pot[3][4]])
                                dirs.append(i)
                if res == "recherche": #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer ni fuir)
                    comportement = humain.comporte_distance(case[3][2])
                    if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                        res = "deplacement"
                    elif comportement == 1: #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                        res = humain.agit_en_vue(self,"deplacement")
                        if repoussante:
                            res = "deplacement"
                    elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                        res = humain.agit_en_vue(self,"fuite")
                        if repoussante:
                            res = "fuite"
                    elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                        res = "fuite"
                    if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                        humain.skill_courant = None
                        importance = 0
                        for i in DIRECTIONS:
                            mur = case[5][i][self.resolution]
                            if mur:
                                if mur.lab in self.vue.keys():
                                    case_pot = self.vue[mur]
                                    entitees = case_pot[6]
                                    libre = True
                                    for ID_entitee in entitees:
                                        entitee = humain.controleur[ID_entitee]
                                        if issubclass(entitee.get_classe(),Agissant): #Cette case est occupée par un agissant
                                            if humain.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                                if self.ennemis[ID_entitee][0] > importance:
                                                    importance = self.ennemis[ID_entitee][0]
                                                    humain.attaque(i)
                                                    res = "attaque"
                    elif not(case[3] or case[5]) and humain.statut_humain == "perdu":
                        res = "paix"
                        if not isinstance(humain,Sentinelle) or repoussante:
                            res = "exploration"
                            if len(dirs)>1: #On peut se permettre de choisir
                                if humain.dir_regard != None: #L'agissant regarde quelque part
                                    dir_back = humain.dir_regard+2
                                    if dir_back in dirs: #On ne veut pas y retourner
                                        dirs.remove(dir_back)
                            humain.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                    elif humain.statut_humain == "paume":
                        res = "paix"
                        if repoussante:
                            res = "exploration"
                            if len(dirs)>1: #On peut se permettre de choisir
                                if humain.dir_regard != None: #L'agissant regarde quelque part
                                    dir_back = humain.dir_regard+2
                                    if dir_back in dirs: #On ne veut pas y retourner
                                        dirs.remove(dir_back)
                            humain.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                    else:
                        if repoussante:
                            cases.pop(0)
                        if res == "deplacement":
                            res = "approche"
                            new_cases = sorted(cases,key=operator.itemgetter(8,2,3,4,6))
                            if new_cases[-1][0] != -1: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                                humain.va(new_cases[-1][0])
                                if ID_humain == 4:
                                    constantes_deplacements.append([self.controleur.nb_tours,"deplacement loin",humain.dir_regard,new_cases])
                            else:
                                res = humain.agit_en_vue(self)
                        elif res == "fuite":
                            for case in cases:
                                case[8] *= -1
                            new_cases = sorted(cases,key=operator.itemgetter(8,5,7,2,3))
                            if new_cases[0][0] != -1: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                                humain.va(new_cases[0][0])
                                if ID_humain == 4:
                                    constantes_deplacements.append([self.controleur.nb_tours,"fuite loin",humain.dir_regard,new_cases])
                            else:
                                res = humain.agit_en_vue(self)
                humain.statut = res

class Esprit_slime(Esprit_type):
    """Un esprit qui dirige un ou plusieurs slimes. Peut interragir avec d'autres esprits slimes."""
    def __init__(self,corp:int,controleur:Controleur): #Les slimes commencent tous séparément, donc ils ont leur propre esprit au début
        self.nom = "esprit_slime_"+str(corp)
        self.controleur = controleur
        self.oubli = 5 #Faire dépendre des skills
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = ["humain"] #Vraiment ?
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        self.classe:Classe_principale = controleur[corp].classe_principale
        self.ajoute_corp(corp)

    def merge(self,nom:str): #Regroupe deux esprits, lorsque des slimes se regroupent
        esprit:Esprit_slime = self.controleur.get_esprit(nom)
        for corp in esprit.corps.keys():
            self.ajoute_corp(corp)
        for ennemi in esprit.ennemis.keys():
            if ennemi in self.ennemis.keys():
                self.ennemis[ennemi] = [max(self.ennemis[ennemi][0],esprit.ennemis[ennemi][0]),max(self.ennemis[ennemi][0],esprit.ennemis[ennemi][0])]
            else:
                self.ennemis[ennemi] = esprit.ennemis[ennemi]
        for vue in esprit.vue.values():
            if vue.id in self.vue.keys(): 
                self.maj_vue(vue)
            else:
                self.ajoute_vue(vue)
        self.controleur.esprits.pop(nom)
        self.merge_classe(esprit.classe)

    def merge_classe(self,classe:Classe):
        #On va comparer tous les skills de chaque classe
        #Les slimes ont trois skills intrasecs : la fusion, pour unir deux groupes de slimes en un seul, la division, pour créer un nouveau slime, et l'absorption, pour ramasser un cadavre et voler ses skills
        #Ils peuvent avoir beaucoup de skills non-intrasecs, et n'utilisent souvent que les passifs
        #Ils ne peuvent pas avoir de sous-classes

        if classe.niveau > self.classe.niveau:
            self.classe.skills_intrasecs = classe.skills_intrasecs
            self.classe.niveau = classe.niveau
            self.classe.xp = classe.xp
        # for skill_intrasec in classe.skills_intrasecs:
        #     autre_skill_intrasec:Skill_intrasec = trouve_skill(self.classe,type(skill_intrasec))
        #     if autre_skill_intrasec != None:
        #         if skill_intrasec.niveau > autre_skill_intrasec.niveau:
        #             self.classe.skills_intrasecs.remove(autre_skill_intrasec)
        #             self.classe.skills_intrasecs.append(skill_intrasec)
        #         elif skill_intrasec.xp > autre_skill_intrasec.xp:
        #             self.classe.skills_intrasecs.remove(autre_skill_intrasec)
        #             self.classe.skills_intrasecs.append(skill_intrasec)
        #     else: #Ça ne devrait pas arriver dans les intrasecs, mais sait-on jamais...
        #         print("Le slime receveur n'avait de skill intrasec correspondant à celui-ci :")
        #         print(skill_intrasec)
        #         self.classe.skills_intrasecs.append(skill_intrasec)

        for skill in classe.skills:
            autre_skill:Skill = trouve_skill(self.classe,type(skill))
            if autre_skill != None:
                if skill.niveau > autre_skill.niveau or (skill.niveau == autre_skill.niveau and skill.xp > autre_skill.xp):
                    self.classe.skills.remove(autre_skill)
                    self.classe.skills.append(skill)
                elif skill.niveau == autre_skill.niveau and skill.xp > autre_skill.xp:
                    self.classe.skills.remove(autre_skill)
                    self.classe.skills.append(skill)
            else:
                self.classe.skills.append(skill)

    def ajoute_corp(self,corp:int):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            slime:Slime=self.controleur[corp]
            slime.rejoint(self.nom)
            slime.classe_principale = self.classe #C'est la plus grande force des slimes : progresser ensemble !

    #/!\ Faire un processus de décision propre aux slimes, qui prend en compte les capacités (communes heureusement) et la situation de chacun

