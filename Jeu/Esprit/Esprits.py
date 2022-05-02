from Jeu.Esprit.Esprit import *

class Esprit_type(Esprit):
    """Un esprit caricatural, pour les besoins de mes expériences."""
    def __init__(self,nom,niveau,controleur,position):
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
        offenseur = self.controleur.get_entitee(offense[0])
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
    def __init__(self,nom,niveau,controleur,position):
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
    def __init__(self,nom,niveau,controleur,position):
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
    def __init__(self,nom,corp,controleur):
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
    def __init__(self,nom,corps,prejuges,controleur):
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
    def __init__(self,corp,controleur): #Les humains commencent tous séparément, donc ils ont leur propre esprit au début
        self.nom = controleur.get_entitee(corp).identite
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
        self.curseur = "corps"
        self.allies_vivants = 0
        self.allie_courant = 0
        self.ennemis_vus = []
        self.ennemi_courant = 0

    def deplace(self,direction):
        if self.curseur == "corps":
            if direction == BAS:
                self.curseur = "ennemis"
            elif direction == HAUT:
                self.curseur = "ennemis"
            elif direction == IN:
                self.curseur = "in_corps"
            elif direction == OUT:
                return True
        elif self.curseur == "in_corps":
            if direction == BAS:
                self.allie_courant += 1
                if self.allie_courant >= self.allies_vivants:
                    self.allie_courant = 0
            elif direction == HAUT:
                if self.allie_courant == 0:
                    self.allie_courant = self.allies_vivants
                self.allie_courant -= 1
            elif direction == OUT:
                self.curseur = "corps"
        elif self.curseur == "ennemis":
            if direction == BAS:
                self.curseur = "corps"
            elif direction == HAUT:
                self.curseur = "corps"
            elif direction == IN:
                self.curseur = "in_ennemis"
            elif direction == OUT:
                return True
        elif self.curseur == "in_ennemis":
            if direction == BAS:
                self.ennemi_courant += 1
                if self.ennemi_courant == len(self.ennemis_vus):
                    self.ennemi_courant = 0
            elif direction == HAUT:
                if self.ennemi_courant == 0:
                    self.ennemi_courant = len(self.ennemis_vus)
                self.ennemi_courant -= 1
            elif direction == OUT:
                self.curseur = "ennemis"

    def utilise_courant(self):
        """Lorsque le joueur veut interagir avec les PNJs."""
        if self.curseur == "corps" or self.curseur == "in_corps":
            ID = sorted(self.corps)[self.allie_courant]
            if ID == 2: #Le joueur est sélectionné. Il rappelle tous les PNJs.
                for ID_corp in self.corps.keys():
                    if ID_corp != 2 and ID_corp <= 10:
                        corp = self.controleur.get_entitee(ID_corp)
                        corp.mouvement = 2
                        corp.cible_deplacement = 2
                        corp.dialogue_courant = -1
            else: #Un PNJs est sélectionné, le joueur le rappelle
                corp = self.controleur.get_entitee(ID)
                corp.mouvement = 2
                corp.cible_deplacement = 2
                corp.dialogue_courant = -1
        elif len(self.ennemis_vus) > 0:
            ID = self.ennemis_vus[self.ennemi_courant] #Un ennemi est sélectionné. Il faut en faire une priorité !
            self.ennemis[ID] += 1 #/!\ On a peut-être plus subtil pour augmenter la priorité

    def retire_corp(self,corp):
        if corp in self.corps:
            if self.corps[corp] != "incapacite":
                if corp <= sorted(self.corps)[self.allie_courant] and self.allie_courant != 0: #Notre corp perdu est avant le courant, ou est le courant.
                    self.item_courant -= 1 #On décale pour rester sur le même/passer au précédent
            self.corps.pop(corp)

    def refait_vue(self):
        vues = []
        agissants_vus = []
        for corp in self.corps.keys(): #On récupère les vues
            if self.corps[corp] != "incapacite":
                agissant = self.controleur.get_entitee(corp)
                vues.append(agissant.vue)
                agissants_vus += self.trouve_agissants(agissant.vue)
        self.oublie_agissants(agissants_vus) #Puisqu'on les a vus, on n'a plus besoin de garder en mémoire leur position précédente
        if self.ennemis_vus != []:
            ennemi_courant = self.ennemis_vus[self.ennemi_courant]
            self.ennemi_courant = 0
            attr = False
        else:
            self.ennemi_courant = 0
            attr = True
        self.ennemis_vus = []
        for ID_agissant in agissants_vus:
            if not(ID_agissant in self.ennemis.keys() or ID_agissant in self.corps.keys()):
                for espece in self.controleur.get_especes(ID_agissant):
                    if espece in self.prejuges:
                        self.ennemis[ID_agissant] = [0.01,0]
            if ID_agissant in self.ennemis.keys() and not(ID_agissant in self.ennemis_vus or self.controleur.est_item(ID_agissant)):
                self.ennemis_vus.append(ID_agissant)
                if not attr:
                    if ID_agissant <= ennemi_courant:
                        self.ennemi_courant = len(self.ennemis_vus)-1
        for vue in vues :
            niveau = vue.id #La première coordonée de la position (première information) de la première case de la première colonne
            if niveau in self.vue.keys(): 
                self.maj_vue(vue,niveau)
            else:
                self.ajoute_vue(vue,niveau)

    def get_offenses(self):
        self.allies_vivants=0
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant = self.controleur.get_entitee(corp)
            offenses,etat = agissant.get_offenses()
            if self.corps[corp] == "incapacite" and etat != "incapacite":
                if corp < sorted(self.corps)[self.allie_courant]: #On rajoute un corps vivant à la liste
                    self.allie_courant += 1 #On décale pour rester sur le même
            elif self.corps[corp] != "incapacite" and etat == "incapacite":
                if corp <= sorted(self.corps)[self.allie_courant] and self.allie_courant != 0: #On retire un corps vivant de la liste
                    self.allie_courant -= 1 #On décale pour rester sur le même/passer au précédent
            if etat != "incapacite":
                self.allies_vivants += 1
            self.corps[corp] = etat
            for offense in offenses:
                self.antagonise_attaquant(offense)
                self.antagonise_supports(offense)
                if self.peureuse():
                    for coennemi in self.controleur.get_esprit(self.controleur.get_entitee(offense[0]).esprit).corps.keys():
                        if not coennemi in self.ennemis:
                            self.ennemis[coennemi] = [0.01,0]

    def merge(self,nom): #Regroupe deux esprits, lorsque des humains forment un groupe
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
                niveau = vue.id #La première coordonée de la position (première information) de la première case de la première colonne
                if niveau in self.vue.keys(): 
                    self.maj_vue(vue,niveau)
                else:
                    self.ajoute_vue(vue,niveau)
            self.controleur.esprits.pop(nom)
            self.chef = self.elit()

    def elit(self):
        if 2 in self.corps.keys():
            self.chef = 2 #Le joueur est le chef par défaut ! Ah mais non mais !
        else:
            self.chef = None
            candidats = []
            for corp in self.corps.keys():
                if "humain" in self.controleur.get_entitee(corp).get_especes():
                    candidats.append(self.controleur.get_entitee(corp)) #Les humains sont les seuls à pouvoir diriger un esprit d'humain. Et les seuls à voter, aussi.
            votes_max = 0
            for candidat in candidats:
                votes = 0
                place = candidat.get_place()
                for votant in candidats:
                    votes += votant.appreciation(place)
                if votes > votes_max:
                    self.chef = candidat.ID #/!\ Éviter les chefs morts, à l'occasion /!\
                    votes_max = votes

    def exclus(self,corp): #C'est super sympa, les relations humaines !
        #Il va falloir créer un nouvel esprit pour l'humain exclus
        #Et il va falloir donner un nom à ce nouvel esprit
        #Les esprits humains sont nommés d'après leur porteur originel
        if self.controleur.get_entitee(corp).identite != self.nom: #Tout va bien
            self.controleur.esprits[self.controleur.get_entitee(corp).identite]=Esprit_humain(corp,self.controleur)
        else:
            self.controleur.esprits[self.controleur.get_entitee(corp).identite]=Esprit_humain(corp,self.controleur)
            self.elit() #Autant changer tous les rapports de force d'un coup
            self.nom = self.controleur.get_entitee(self.chef).identite

    def get_agissants_vus(self,humain):
        agissants = []
        for case in self.vue:
            if case[2] > 0:
                for ID in case[6]:
                    if not(self.controleur.est_item(ID)):
                        agissants.append(ID)
        agissants.sort()
        return agissants

    def get_corps_vus(self):
        corps = []
        for corp in self.corps.keys():
            if self.corps[corp] != "incapacite":
                corps.append(corp)
        return corps

    def get_ennemis_vus(self):
        return self.ennemis_vus

    def get_cases_vues(self,humain):
        cases = []
        for case in self.vue[humain.position.lab]:
            if case[2] > 0:
                cases.append(case[0])
        return cases

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
                joueur = self.controleur.get_entitee(2)
                joueur.recontrole()
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
        humain:Humain = self.controleur.get_entitee(ID_humain)
        humain.skill_courant = None
        if humain.identite == "joueur":
            humain.recontrole()
            humain.statut_humain = "joueur"
        else:
            humain.statut_humain = "proximite"
            if humain.mouvement == 0: #0 pour aller vers, et 1 pour chercher
                if isinstance(humain.cible_deplacement,int):
                    if not(self.controleur.est_item(humain.cible_deplacement)):
                        cible = self.controleur.get_entitee(humain.cible_deplacement).get_position()
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
                        cible = self.controleur.get_entitee(humain.cible_deplacement).get_position()
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
                                entitee = humain.controleur.get_entitee(ID_entitee)
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
                                            self.controleur.get_entitee(2).interlocuteur = humain
                                            self.controleur.set_phase(EVENEMENT)
                                            self.controleur.get_entitee(2).event = DIALOGUE
                                            humain.start_dialogue()
                                            humain.dir_regard = i
                                            self.controleur.get_entitee(2).dir_regard = i+2
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
                                        entitee = humain.controleur.get_entitee(ID_entitee)
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
    def __init__(self,corp,controleur): #Les slimes commencent tous séparément, donc ils ont leur propre esprit au début
        self.nom = "esprit_slime"+str(corp)
        self.controleur = controleur
        self.oubli = 5 #Faire dépendre des skills
        self.ennemis = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = ["humain"] #Vraiment ?
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.vue = Vues()
        self.corps = {}
        self.classe = controleur.get_entitee(corp).classe_principale
        self.ajoute_corp(corp)

    def merge(self,nom): #Regroupe deux esprits, lorsque des slimes se regroupent
        esprit = self.controleur.get_esprit(nom)
        for corp in esprit.corps.keys():
            self.ajoute_corp(corp)
        for ennemi in esprit.ennemis.keys():
            if ennemi in self.ennemis.keys():
                self.ennemis[ennemi] = [max(self.ennemis[ennemi][0],esprit.ennemis[ennemi][0]),max(self.ennemis[ennemi][0],esprit.ennemis[ennemi][0])]
            else:
                self.ennemis[ennemi] = esprit.ennemis[ennemi]
        for vue in esprit.vue.values():
            niveau = vue.id
            if niveau in self.vue.keys(): 
                self.maj_vue(vue,niveau)
            else:
                self.ajoute_vue(vue,niveau)
        self.controleur.esprits.pop(nom)
        self.merge_classe(esprit.classe)

    def merge_classe(self,classe):
        #On va comparer tous les skills de chaque classe
        #Les slimes ont trois skills intrasecs : la fusion, pour unir deux groupes de slimes en un seul, la division, pour créer un nouveau slime, et l'absorption, pour ramasser un cadavre et voler ses skills
        #Ils peuvent avoir beaucoup de skills non-intrasecs, et n'utilisent souvent que les passifs
        #Ils ne peuvent pas avoir de sous-classes

        for skill_intrasec in classe.skills_intrasecs:
            autre_skill_intrasec = trouve_skill(self.classe_principale,type(skill_intrasec))
            if autre_skill_intrasec != None:
                if skill_intrasec.niveau > autre_skill_intrasec.niveau:
                    self.classe_principale.skill_intrasecs.remove(autre_skill_intrasec)
                    self.classe_principale.skill_intrasecs.append(skill_intrasec)
                elif skill_intrasec.xp > autre_skill_intrasec.xp:
                    self.classe_principale.skill_intrasecs.remove(autre_skill_intrasec)
                    self.classe_principale.skill_intrasecs.append(skill_intrasec)
            else: #Ça ne devrait pas arriver dans les intrasecs, mais sait-on jamais...
                print("Le slime receveur n'avait de skill intrasec correspondant à celui-ci :")
                print(skill_intrasec)
                self.classe_principale.skill_intrasecs.append(skill_intrasec)

        for skill in classe.skills:
            autre_skill = trouve_skill(self.classe_principale,type(skill))
            if autre_skill != None:
                if skill.niveau > autre_skill.niveau:
                    self.classe_principale.skill_intrasecs.remove(autre_skill)
                    self.classe_principale.skill_intrasecs.append(skill)
                elif skill.xp > autre_skill.xp:
                    self.classe_principale.skill_intrasecs.remove(autre_skill)
                    self.classe_principale.skill_intrasecs.append(skill)
            else:
                self.classe_principale.skill_intrasecs.append(skill)

    def ajoute_corp(self,corp):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            self.controleur.get_entitee(corp).rejoint(self.nom)
            self.controleur.get_entitee(corp).classe_principale = self.classe #C'est la plus grande force des slimes : progresser ensemble !

    #/!\ Faire un processus de décision propre aux slimes, qui prend en compte les capacités (communes heureusement) et la situation de chacun

