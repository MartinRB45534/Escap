from Jeu.Entitee.Agissant.Agissants import *
from Jeu.Esprit.Representation_spatiale import *

from typing import Dict, Literal, Self, Tuple
import operator

class Esprit :
    """La classe des esprits, qui manipulent les agisants."""
    def __init__(self,nom:str): #On identifie les esprits par des noms (en fait on s'en fout, vu qu'on ne fait pas d'opérations dessus on pourrait avoir des labs, des entitees et des esprits nommés avec des str, des int, des float, des bool, etc.)
        self.corps:Dict[int,str] = {}
        self.vue = Vues()
        self.salles:List[Salle] = []
        self.couloirs:List[Couloir] = []
        self.entrees:Dict[Position,List[Espace_schematique]] = {}
        self.zones_inconnues:List[Zone_inconnue] = []
        self.ennemis:Dict[int,List[float]] = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.oubli = 1
        self.resolution = 0 #0 pour se déplacer normalement, 1 pour passer les portes dont on a les clés, 2 pour traverser les portails, 3 pour passer les protes et les portails, 4 pour passer partout (portes, portails, changer d'étage)
        self.nom = nom
        self.controleur:Controleur = None

    def ajoute_corp(self,corp:int):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            self.controleur[corp].rejoint(self.nom)

    def ajoute_corps(self,corps:List[int]):
        for corp in corps:
            self.ajoute_corp(corp)

    def retire_corp(self,corp:int):
        if corp in self.corps:
            self.corps.pop(corp)

    def retire_corps(self,corps:List[int]):
        for corp in corps:
            self.retire_corp(corp)

    def get_corps(self):
        corps:List[int] = []
        for corp in self.corps.keys():
            corps.append(corp)
        return corps

    def get_importance(self,position:Position):
        importance = 0
        if position in self.vue:
            case = self.vue[position]
            for ID in case[6]:
                if self.controleur[ID].etat == "vivant":
                    if ID in self.ennemis:
                        new_importance = self.ennemis[ID][0]
                        if new_importance > importance:
                            importance = new_importance
        return importance

    def ajoute_vue(self,vue:Vue):
        self.vue[vue.id] = vue
        nouvelles_cases = []
        cases_limites = []
        for decalage in vue.decalage:
            case = vue[decalage]
            if case[1] > 0:
                self.vue[case[0]][2] = self.oubli
                nouvelles_cases.append(case[0])
            else:
                if case[1] == -1:
                    cases_limites.append(case[0])
                self.vue[case[0]][1] = 0
                self.vue[case[0]][2] = 0
                self.vue[case[0]][4] = 0
                self.vue[case[0]][5] = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
                self.vue[case[0]][6] = []
        return nouvelles_cases, cases_limites

    def maj_vue(self,vue:Vue):
        cases_vues:List[Position] = []
        nouvelles_cases:List[Position] = []
        cases_limites:List[Position] = []
        for decalage in vue.decalage:
            case = vue[decalage]
            if case[1] > 0: #Si la clarté est positive
                cases_vues.append(case[0]) 
                if case[5] != self.vue[case[0]][5]: #/!\ Réduire ça proprement
                    nouvelles_cases.append(case[0])
                case[2] = self.oubli
                self.vue[case[0]] = case #On remplace par la dernière version de la vision /!\ Et si certains n'y voient pas les mêmes choses ? (Genre des agissants invisibles ?)
            elif case[1] == -1: #On est à la limite de la vision de quelqu'un
                cases_limites.append(case[0])
        return cases_vues, nouvelles_cases, cases_limites

    def merge_vue(self,vue:Vue):
        cases_self:List[Position] = []
        cases_other:List[Position] = []
        for decalage in vue.decalage:
            case_other = vue[decalage]
            case_self = self.vue[case_other[0]]
            if case_other[1] > 0 and case_self[1] <= 0: # Si ça apparait chez l'autre et pas chez nous
                cases_other.append(case_other[0])
            elif case_other[1] <= 0 and case_self[1] > 0: # Si ça apparait chez nous et pas chez l'autre
                cases_self.append(case_self[0])
            if case_other[1] > 0: # SI la clarté est positive
                case_other[2] = self.oubli
                self.vue[case_other[0]] = case_other #On remplace par la dernière version de la vision /!\ Et si certains n'y voient pas les mêmes choses ? (Genre des agissants invisibles ?)
        return cases_self, cases_other

    def trouve_agissants_vue(self,vue:Vue):
        vus:List[int] = []
        oublies:List[Tuple[int,Position]] = []
        for decalage in vue.decalage:
            case = vue[decalage]
            vus += case[6]
            if case[0] in self.vue:
                oublies += [(ID,case[0]) for ID in self.vue[case[0]][6] if not ID in case[6]]
        return vus, oublies

    def trouve_agissants(self):
        agissants = []
        for case in self.vue:
            agissants += case[6]
        return sorted(agissants)

    def get_corps_vus(self):
        corps = []
        for agissant in self.trouve_agissants():
            if agissant in self.corps.keys() and self.controleur.est_agissant(agissant):
                corps.append(agissant)
        return corps

    def get_ennemis_vus(self):
        ennemis = []
        for agissant in self.trouve_agissants():
            if agissant in self.ennemis.keys() and self.controleur.est_agissant(agissant):
                ennemis.append(agissant)
        return ennemis

    def get_neutres_vus(self):
        neutres = []
        for agissant in self.trouve_agissants():
            if agissant not in self.corps.keys() and agissant not in self.ennemis.keys() and self.controleur.est_agissant(agissant):
                neutres.append(agissant)
        return neutres

    def oublie_agissants(self,agissants:List[int]):
        for case in self.vue:
            for ID in agissants:
                if ID in case[6]:
                    case[6].remove(ID)
        for zone in self.zones_inconnues:
            for ID in agissants:
                if ID in zone.occupants:
                    zone.occupants.remove(ID)

    def refait_vue(self):
        vues:List[Vue] = []
        agissants_vus:List[int] = []
        agissants_oublies:List[Tuple[int,Position]] = []
        for corp in self.corps.keys(): #On récupère les vues
            if self.corps[corp] != "incapacite":
                agissant:Agissant = self.controleur[corp]
                vues.append(agissant.vue)
                vus, oublies = self.trouve_agissants_vue(agissant.vue)
                agissants_vus += vus
                agissants_oublies += oublies
        agissants_vus = [*set(agissants_vus)] #On enlève les doublons
        agissants_oublies = [*set([tup for tup in agissants_oublies if not tup[0] in agissants_vus])] #On enlève les doublons et les agissants vus
        self.oublie_agissants(agissants_vus) #Puisqu'on les a vus, on n'a plus besoin de garder en mémoire leur position précédente. /!\ À modifier plus tard
        for ID_agissant in agissants_vus:
            if not(ID_agissant in self.ennemis.keys() or ID_agissant in self.corps.keys()):
                for espece in self.controleur.get_especes(ID_agissant):
                    if espece in self.prejuges:
                        self.ennemis[ID_agissant] = [0.01,0]
        cases_vues = []
        nouvelles_cases = []
        cases_limites = []
        for vue in vues :
            if vue.id in self.vue.keys():
                cases, nouvelles, limites = self.maj_vue(vue)
                cases_vues+=cases
                nouvelles_cases+=nouvelles
                cases_limites+=limites
            else:
                nouvelles, limites = self.ajoute_vue(vue)
                cases_vues+=nouvelles
                nouvelles_cases+=nouvelles
                cases_limites+=limites
        cases_vues = [*set(cases_vues)]
        nouvelles_cases = [*set(nouvelles_cases)] #Pour retirer les doublons
        self.update_zones(cases_vues, nouvelles_cases, cases_limites, agissants_oublies)
        self.update_representation(nouvelles_cases)

    def update_zones(self,cases:List[Position],nouvelles_cases:List[Position],cases_limites:List[Position],agissants_oublies:List[Tuple[int,Position]]):
        cases_memorisees = [case[0] for case in self.vue if case[2] and not case[0] in cases]
        # print(cases)
        # print(nouvelles_cases)
        zones_mod:List[Zone_inconnue] = []
        for case in nouvelles_cases:
            for zone in self.zones_inconnues:
                if case in zone.cases:
                    # print("Scinde")
                    zones_mod += self.scinde_zone(zone,case)
        for zone in self.zones_inconnues:
            for case in zone.cases:
                if case in cases_memorisees:
                    cases_memorisees.remove(case)
                # else:
                #     print("I'm useful !")
        for case in cases_memorisees:
            zone = Zone_inconnue(case)
            self.zones_inconnues.append(zone)
            for zone_ in self.zones_inconnues:
                if zone_ != zone:
                    for DIR in DIRECTIONS:
                        voisin = self.vue[case][5][DIR][4]
                        if voisin and voisin in zone_.cases:
                            zone = self.fusionne_zones(zone,zone_)
                            break
                if zone not in zones_mod:
                    zones_mod.append(zone)
        for case in cases_limites:
            if self.vue[case][1] == 0:
                zone = Zone_inconnue(case)
                self.zones_inconnues.append(zone)
                for zone_ in self.zones_inconnues:
                    if zone_ != zone:
                        for DIR in DIRECTIONS:
                            voisin = self.vue[case][5][DIR][4]
                            if voisin and voisin in zone_.cases:
                                zone = self.fusionne_zones(zone,zone_)
                                break
                    if zone not in zones_mod:
                        zones_mod.append(zone)
            elif self.vue[case][1] < 0:
                print("Why !!?")
        for zone in self.zones_inconnues:
            zone.entrees = []
            zone.sorties = []
            for tup in agissants_oublies:
                if tup[1] in zone.cases:
                    zone.occupants.append(tup[0])
                for DIR in DIRECTIONS:
                    voisin = self.vue[tup[1]][5][DIR][4]
                    if voisin and voisin in zone.cases:
                        zone.occupants.append(tup[0])
            for case in zone.cases:
                for DIR in DIRECTIONS:
                    voisin = self.vue[case][5][DIR][4]
                    if voisin and ((not voisin in self.vue) or self.vue[voisin][1] == 0):
                        zone.sorties.append(voisin)
                        zones_mod.append(zone)
            for case in cases_limites:
                if case in zone.cases:
                    zone.cases.remove(case)
                    zone.entrees.append(case)
                    cases_limites.remove(case)
                    zones_mod.append(zone)
            if zone.cases == [] and zone.entrees == []:
                self.remove_zone(zone)

    def update_representation(self,cases:List[Position]):
        carres_pot:List[Position] = []
        for case in cases:
            for dec in Decalage(2,2):
                if case-dec in self.vue and case-dec+Decalage(1,1) in self.vue:
                    carres_pot.append(case-dec)
        carres_pot = [*set(carres_pot)]
        carres:List[Position] = []
        for carre_pot in carres_pot:
            if self.vue[carre_pot][5][DROITE][0] and self.vue[carre_pot+DROITE][5][GAUCHE][0] and self.vue[carre_pot][5][BAS][0] and self.vue[carre_pot+BAS][5][HAUT][0] and self.vue[carre_pot+BAS][5][DROITE][0] and self.vue[carre_pot+DROITE+BAS][5][GAUCHE][0] and self.vue[carre_pot+DROITE][5][BAS][0] and self.vue[carre_pot+BAS+DROITE][5][HAUT][0] :
                carres.append(carre_pot)
                if carre_pot.lab == "Étage 3 : combat":
                    if carre_pot.x in range(2,5) and carre_pot.y in range(7,10):
                        print("Check1")
        salles_mod:List[Salle] = [] #Les salles qu'on a modifiées
        couloirs_mod:List[Couloir] = []
        # print("Salles :")
        # print(len(self.salles))
        for carre in carres:
            # if self.nom == "heros":
            #     print(carre)
            libre = True
            for salle in self.salles:
                if carre in salle.carres:
                    libre = False #Arrive par exemple lorsqu'on ouvre une porte à côté d'une case déjà dans une salle
                    if salle not in salles_mod:
                        salles_mod.append(salle) #Si on a ouvert une porte, on veut rajouter cette case aux entrées (sinon on a des problèmes de résolution)
                    break
            if libre:
                # print("Nouvelle salle !")
                salle = Salle(carre)
                # print(len(salle.carres))
                self.salles.append(salle)
                for salle_ in self.salles:
                    if salle_ != salle: #Peut arriver si on partage plusieurs cases avec une salle existante
                        for dir in DIRECTIONS:
                            if carre+dir in salle_.carres: #Ces deux carrés partagent deux cases : les deux salles n'en forment qu'une seule
                                salle = self.fusionne_salles(salle_,salle)
                                # print("Fusion de salles !")
                                # print(len(salle.carres))
                                break
                if salle not in salles_mod:
                    salles_mod.append(salle)
            for dec in Decalage(2,2):
                for couloir in self.couloirs:
                    if carre+dec in couloir.cases: #Cette case appartenait à un couloir. Ce n'est plus le cas car des murs ont été ouverts (portes, écrasement, etc.) et elle appartient désormais à une salle
                        couloirs_mod += self.scinde_couloir(couloir,carre+dec)
        # print("Salles :")
        # print(len(self.salles))
        # print("Salles modifiées :")
        # print(len(salles_mod))
        # print("Intersection")
        # print(len([salle for salle in salles_mod if salle in self.salles]))
        for salle in salles_mod[::-1]:
            if salle in self.salles: #On peut en avoir retirées
                # print("Salle modifiée !")
                # print(len(salle.carres))
                salle.add_cases()
                salle.make_bord()
                for entree in salle.entrees:
                    if entree in self.entrees:
                        self.entrees[entree].remove(salle)
                        if self.entrees[entree] == []:
                            self.entrees.pop(entree)
                salle.entrees = [*set([bord.emplacement for bord in salle.frontiere if self.vue[bord.emplacement][5][bord.direction][4]])]
                salle.calcule_distances()
                for case in salle.cases:
                    if case in cases:
                        cases.remove(case)
                    if case.lab == "Étage 3 : combat":
                        if case.x in range(2,5) and case.y in range(7,10):
                            print("Check2")
                            print(case.x,case.y)
                    if case in cases:
                        print("Toujours là")
                for entree in salle.entrees:
                    salle.cases.remove(entree)
            else:
                # print("Salle supprimée !")
                # print(len(salle.carres))
                salles_mod.remove(salle)
        # print("Salles :")
        # for salle in self.salles:
        #     print("Salle : ")
        #     print(salle.cases)
        #     print(salle.carres)
        for case in cases:
            if sum([int(not(not(self.vue[case][5][dir][4]))) for dir in DIRECTIONS]) < 3:
                libre = True
                for couloir in self.couloirs:
                    if case in couloir.cases:
                        libre = False
                        break
                if libre:
                    couloir = Couloir(case)
                    self.couloirs.append(couloir)
                    for couloir_ in self.couloirs:
                        if couloir_ != couloir:
                            for dir in DIRECTIONS:
                                if case+dir in couloir_.cases and self.vue[case][5][dir][4] and self.vue[case+dir][5][dir.oppose()][4]:
                                    couloir = self.fusionne_couloirs(couloir_,couloir)
                                    break
                if couloir not in couloirs_mod:
                    couloirs_mod.append(couloir)
            else:
                for couloir in self.couloirs:
                    if case in couloir.cases: #Cette case appartenait à un couloir. Ce n'est plus le cas car des murs ont été ouverts (portes, écrasement, etc.)
                        couloirs_mod += self.scinde_couloir(couloir,case)
                        break
            if case.lab == "Étage 3 : combat":
                if case.x in range(2,5) and case.y in range(7,10):
                    print("Bad check")
                    print(case.x, case.y)
        for couloir in couloirs_mod:
            if couloir in self.couloirs:
                couloir.entrees = []
                for dir in DIRECTIONS:
                    case1 = self.vue[couloir.cases[0]][5][dir][4]
                    if case1 and case1 not in couloir.cases: #Un mur vers l'extérieur !
                        couloir.entrees.append(case1)
                    case2 = self.vue[couloir.cases[-1]][5][dir][4]
                    if len(couloir.cases)>1 and case2 and case2 not in couloir.cases: #Un mur vers l'extérieur !
                        couloir.entrees.append(case2)
            else:
                couloirs_mod.remove(couloir)
        for espace in salles_mod + couloirs_mod:
            for entree in espace.entrees:
                if espace not in self.entrees.get(entree,[]) and espace in self.salles+self.couloirs:
                    self.entrees[entree] = self.entrees.get(entree,[])+[espace]

    def downdate_zones(self,cases:List[Position]):
        zones_mod:List[Zone_inconnue] = []
        for case in cases:
            for zone in self.zones_inconnues:
                if case in zone.cases:
                    zones_mod += self.scinde_zone(zone,case)
        for zone in zones_mod:
            if zone in self.zones_inconnues:
                zone.sorties = []
                for case in zone.cases:
                    for DIR in DIRECTIONS:
                        voisin = self.vue[case][5][DIR][4]
                        if voisin and ((not voisin in self.vue) or self.vue[voisin][1] == 0):
                            zone.sorties.append(voisin)

    def downdate_representation(self,cases:List[Position]):
        carres_pot:List[Position] = []
        for case in cases:
            for dec in Decalage(2,2):
                if case-dec in self.vue and case-dec+Decalage(1,1) in self.vue:
                    carres_pot.append(case-dec)
        carres_pot = [*set(carres_pot)]
        carres_suppr:List[Position] = []
        for carre_pot in carres_pot:
            if not(self.vue[carre_pot][5][DROITE][0] and self.vue[carre_pot+DROITE][5][GAUCHE][0] and self.vue[carre_pot+BAS][5][DROITE][0] and self.vue[carre_pot+DROITE+BAS][5][GAUCHE][0] and self.vue[carre_pot][5][BAS][0] and self.vue[carre_pot+BAS][5][HAUT][0] and self.vue[carre_pot+DROITE][5][BAS][0] and self.vue[carre_pot+BAS+DROITE][5][HAUT][0]):
                carres_suppr.append(carre_pot)
        salles_mod:List[Salle] = [] #Les salles qu'on a modifiées
        for carre in carres_suppr:
            for salle in self.salles:
                if carre in salle.carres:
                    salles_mod += self.scinde_salle(salle,carre)
        couloirs_mod:List[Couloir] = []
        for salle in salles_mod:
            if salle in self.salles: #On peut en avoir retirées
                salle.add_cases()
                salle.make_bord()
                for entree in salle.entrees:
                    if entree in self.entrees:
                        self.entrees[entree].remove(salle)
                        if self.entrees[entree] == []:
                            self.entrees.pop(entree)
                salle.entrees = [*set([bord.emplacement for bord in salle.frontiere if self.vue[bord.emplacement][5][bord.direction][4]])]
                salle.calcule_distances()
        for case in cases:
            for couloir in self.couloirs:
                if case in couloir.cases:
                    couloirs_mod += self.scinde_couloir(couloir,case)
        for couloir in couloirs_mod:
            if couloir in self.couloirs:
                couloir.entrees = []
                for dir in DIRECTIONS:
                    case = self.vue[couloir.cases[0]][5][dir][4]
                    if case and case not in couloir.cases: #Un mur vers l'extérieur !
                        couloir.entrees.append(case)
                    case = self.vue[couloir.cases[-1]][5][dir][4]
                    if case and case not in couloir.cases: #Un mur vers l'extérieur !
                        couloir.entrees.append(case)
        for espace in salles_mod + couloirs_mod:
            for entree in espace.entrees:
                self.entrees[entree] = self.entrees.get(entree,[])+[espace]

    def merge_zones(self,esprit:Self,cases_self:List[Position],cases_esprit:List[Position]):
        zones_mod:List[Zone_inconnue] = []
        entrees:List[Position] = []
        for zone in self.zones_inconnues+esprit.zones_inconnues:
            entrees += zone.entrees
        entrees = [*set(entrees)]
        for zone in self.zones_inconnues + esprit.zones_inconnues:
            zone.cases += zone.entrees
            zone.entrees = []
        for case in cases_self:
            for zone in esprit.zones_inconnues:
                if case in zone.cases:
                    zones_mod += esprit.scinde_zone(zone,case)
                    break
        for case in cases_esprit:
            for zone in self.zones_inconnues:
                if case in zone.cases:
                    zones_mod += self.scinde_zone(zone,case)
                    break
        for zone in self.zones_inconnues:
            for zone_ in esprit.zones_inconnues:
                for case in zone.cases:
                    if case in zone_.cases:
                        zones_mod += esprit.fusionne_zones(zone,zone_)
                        break
        self.zones_inconnues += esprit.zones_inconnues
        for zone in self.zones_inconnues:
            for entree in entrees:
                if entree in zone.cases:
                    zone.cases.remove(entree)
                    zone.entrees.append(entree)
        for zone in zones_mod:
            if zone in self.zones_inconnues:
                zone.sorties = []
                for case in zone.cases:
                    for DIR in DIRECTIONS:
                        voisin = self.vue[case][5][DIR][4]
                        if voisin and ((not voisin in self.vue) or self.vue[voisin][1] == 0):
                            zone.sorties.append(voisin)
        
    def merge_representation(self,esprit:Self,cases_self:List[Position],cases_esprit:List[Position]):
        salles_mod:List[Salle] = []
        carres_pot_esprit:List[Position] = []
        carres_pot_self:List[Position] = []
        for case in cases_self:
            for dec in Decalage(2,2):
                if case-dec in self.vue and case-dec+Decalage(1,1) in self.vue:
                    carres_pot_esprit.append(case-dec)
        for case in cases_esprit:
            for dec in Decalage(2,2):
                if case-dec in esprit.vue and case-dec+Decalage(1,1) in esprit.vue:
                    carres_pot_self.append(case-dec)
        carres_esprit:List[Position] = []
        carres_self:List[Position] = []
        for carre in carres_pot_esprit:
            if self.vue[carre][5][DROITE][0] and self.vue[carre+DROITE][5][GAUCHE][0] and self.vue[carre][5][BAS][0] and self.vue[carre+BAS][5][HAUT][0] and self.vue[carre+BAS][5][DROITE][0] and self.vue[carre+DROITE+BAS][5][GAUCHE][0] and self.vue[carre+DROITE][5][BAS][0] and self.vue[carre+BAS+DROITE][5][HAUT][0] :
                if not all([carre+dec in cases_self for dec in Decalage(2,2)]): # Si le carré était déjà entièrement visible par self, on s'en est déjà occupé plus tôt
                    carres_esprit.append(carre)
        for carre in carres_pot_self:
            if esprit.vue[carre][5][DROITE][0] and esprit.vue[carre+DROITE][5][GAUCHE][0] and esprit.vue[carre][5][BAS][0] and esprit.vue[carre+BAS][5][HAUT][0] and esprit.vue[carre+BAS][5][DROITE][0] and esprit.vue[carre+DROITE+BAS][5][GAUCHE][0] and esprit.vue[carre+DROITE][5][BAS][0] and esprit.vue[carre+BAS+DROITE][5][HAUT][0] :
                if not all([carre+dec in cases_esprit for dec in Decalage(2,2)]):
                    carres_self.append(carre)
        couloirs_mod:List[Couloir] = []
        for carre in carres_esprit:
            libre = True
            for salle in esprit.salles:
                if carre in salle.carres: # Ne devrait pas arriver
                    libre = False #Arrive par exemple lorsqu'on ouvre une porte à côté d'une case déjà dans une salle
                    if salle not in salles_mod:
                        salles_mod.append(salle) #Si on a ouvert une porte, on veut rajouter cette case aux entrées (sinon on a des problèmes de résolution)
                    print("Euh... C'est normal ça ?")
                    break
            if libre:
                salle = Salle(carre)
                esprit.salles.append(salle)
                for salle_ in esprit.salles:
                    if salle_ != salle: #Peut arriver si on partage plusieurs cases avec une salle existante
                        for dir in DIRECTIONS:
                            if carre+dir in salle_.carres: #Ces deux carrés partagent deux cases : les deux salles n'en forment qu'une seule
                                salle = esprit.fusionne_salles(salle_,salle)
                                break
                if salle not in salles_mod:
                    salles_mod.append(salle)
            for dec in Decalage(2,2):
                for couloir in esprit.couloirs:
                    if carre+dec in couloir.cases: #Cette case appartenait à un couloir. Ce n'est plus le cas car des murs ont été ouverts (portes, écrasement, etc.) et elle appartient désormais à une salle
                        couloirs_mod += esprit.scinde_couloir(couloir,carre+dec)
                        break
                for couloir in self.couloirs:
                    if carre+dec in couloir.cases:
                        couloirs_mod += self.scinde_couloir(couloir,carre+dec)
                        break
        for carre in carres_self:
            libre = True
            for salle in self.salles:
                if carre in salle.carres:
                    libre = False
                    if salle not in salles_mod:
                        salles_mod.append(salle)
                    print("Euh... C'est normal ça ?")
                    break
            if libre:
                salle = Salle(carre)
                self.salles.append(salle)
                for salle_ in self.salles:
                    if salle_ != salle:
                        for dir in DIRECTIONS:
                            if carre+dir in salle_.carres:
                                salle = self.fusionne_salles(salle_,salle)
                                break
                if salle not in salles_mod:
                    salles_mod.append(salle)
            for dec in Decalage(2,2):
                for couloir in self.couloirs:
                    if carre+dec in couloir.cases:
                        couloirs_mod += self.scinde_couloir(couloir,carre+dec)
                        break
                for couloir in esprit.couloirs:
                    if carre+dec in couloir.cases:
                        couloirs_mod += esprit.scinde_couloir(couloir,carre+dec)
                        break
        for salle in esprit.salles:
            self.salles.append(salle)
            for salle_ in self.salles[::-1]:
                if salle_ != salle:
                    for carre in salle.carres:
                        for dir in DIRECTIONS:
                            if carre+dir in salle_.carres:
                                salle = self.fusionne_salles(salle,salle_)
                                break
                        else:
                            continue
                        break
            if salle not in salles_mod:
                salles_mod.append(salle)
        self.entrees.update(esprit.entrees)
        for salle in salles_mod[::-1]:
            if salle in self.salles:
                salle.add_cases()
                salle.make_bord()
                for entree in salle.entrees:
                    if entree in self.entrees:
                        self.entrees[entree].remove(salle)
                        if self.entrees[entree] == []:
                            self.entrees.pop(entree)
                salle.entrees = [*set([bord.emplacement for bord in salle.frontiere if self.vue[bord.emplacement][5][bord.direction][4]])]
                salle.calcule_distances()
                for case in salle.cases:
                    if case in cases_self:
                        cases_self.remove(case)
                    if case in cases_esprit:
                        cases_esprit.remove(case)
                for entree in salle.entrees:
                    salle.cases.remove(entree)
            else:
                salles_mod.remove(salle)
        for case in cases_self + cases_esprit:
            if sum([int(not(not(self.vue[case][5][dir][4]))) for dir in DIRECTIONS]) < 3:
                libre = True
                for couloir in self.couloirs + esprit.couloirs:
                    if case in couloir.cases:
                        libre = False
                        break
                if libre:
                    print("Hum... C'est normal ça ?")
                    couloir = Couloir(case)
                    self.couloirs.append(couloir)
                    for couloir_ in self.couloirs:
                        if couloir_ != couloir:
                            for dir in DIRECTIONS:
                                if case+dir in couloir_.cases and self.vue[case][5][dir][4] and self.vue[case+dir][5][dir.oppose()][4]:
                                    couloir = self.fusionne_couloirs(couloir_,couloir)
                                    break
                    for couloir_ in esprit.couloirs[::-1]:
                        if couloir_ != couloir:
                            for dir in DIRECTIONS:
                                if case+dir in couloir_.cases and self.vue[case][5][dir][4] and self.vue[case+dir][5][dir.oppose()][4]:
                                    couloir = self.fusionne_couloirs(couloir_,couloir)
                                    self.couloirs.append(couloir)
                                    esprit.couloirs.remove(couloir)
                                    break
                if couloir not in couloirs_mod:
                    couloirs_mod.append(couloir)
        for couloir in esprit.couloirs:
            self.couloirs.append(couloir)
            for couloir_ in self.couloirs:
                if couloir_ != couloir:
                    for case in couloir.cases:
                        for dir in DIRECTIONS:
                            if case+dir in couloir_.cases and self.vue[case][5][dir][4] and self.vue[case+dir][5][dir.oppose()][4]:
                                couloir = self.fusionne_couloirs(couloir_,couloir)
                                break
                        else:
                            continue
                        break
            if couloir not in couloirs_mod:
                couloirs_mod.append(couloir)
        for couloir in couloirs_mod:
            if couloir in self.couloirs:
                couloir.entrees = []
                for dir in DIRECTIONS:
                    case1 = self.vue[couloir.cases[0]][5][dir][4]
                    if case1 and case1 not in couloir.cases: #Un mur vers l'extérieur !
                        couloir.entrees.append(case1)
                    case2 = self.vue[couloir.cases[-1]][5][dir][4]
                    if len(couloir.cases)>1 and case2 and case2 not in couloir.cases: #Un mur vers l'extérieur !
                        couloir.entrees.append(case2)
            else:
                couloirs_mod.remove(couloir)
        for espace in salles_mod + couloirs_mod:
            for entree in espace.entrees:
                if espace not in self.entrees.get(entree,[]) and espace in self.salles+self.couloirs:
                    self.entrees[entree] = self.entrees.get(entree,[])+[espace]

    def fusionne_salles(self,salle1:Salle,salle2:Salle): #salle1 est probablement plus grosse que salle2
        salle1.carres = [*set(salle1.carres+salle2.carres)] # Et c'est tout ?
        self.remove_salle(salle2)
        return salle1

    def fusionne_couloirs(self,couloir1:Couloir,couloir2:Couloir): #couloir1 est probablement plus gros que couloir2
        for dir in DIRECTIONS:
            if self.vue[couloir1.cases[0]][5][dir][4] == couloir2.cases[0] and self.vue[couloir2.cases[0]][5][dir.oppose()][4] == couloir1.cases[0]:
                couloir1.cases = list(reversed(couloir1.cases)) + couloir2.cases # Et c'est tout ?
                self.remove_couloir(couloir2)
                return couloir1
            if self.vue[couloir1.cases[-1]][5][dir][4] == couloir2.cases[0] and self.vue[couloir2.cases[0]][5][dir.oppose()][4] == couloir1.cases[-1]:
                couloir1.cases = couloir1.cases + couloir2.cases # Et c'est tout ?
                self.remove_couloir(couloir2)
                return couloir1
            if self.vue[couloir1.cases[0]][5][dir][4] == couloir2.cases[-1] and self.vue[couloir2.cases[-1]][5][dir.oppose()][4] == couloir1.cases[0]:
                couloir1.cases = couloir2.cases + couloir1.cases # Et c'est tout ?
                self.remove_couloir(couloir2)
                return couloir1
            if self.vue[couloir1.cases[-1]][5][dir][4] == couloir2.cases[-1] and self.vue[couloir2.cases[-1]][5][dir.oppose()][4] == couloir1.cases[-1]:
                couloir1.cases = couloir1.cases + list(reversed(couloir2.cases)) # Et c'est tout ?
                self.remove_couloir(couloir2)
                return couloir1
        print(couloir1.cases)
        print(couloir2.cases)
        print("Oops! How did I get there?")

    def fusionne_zones(self,zone1:Zone_inconnue,zone2:Zone_inconnue):
        zone1.fusionne(zone2)
        self.remove_zone(zone2)
        return zone1

    def scinde_salle(self,salle:Salle,carre:Position):
        salle.carres.remove(carre)
        voisins = [carre+dir for dir in DIRECTIONS if carre+dir in salle.carres]
        salles = []
        while voisins != []:
            depart = voisins.pop(0)
            queue = [depart]
            salle.carres.remove(depart)
            new_salle = Salle(depart)
            while len(queue):
                position = queue.pop(0)
                for dir in DIRECTIONS:
                    voisin = position+dir
                    if voisin in salle.carres:
                        salle.carres.remove(voisin)
                        queue.append(voisin)
                        new_salle.carres.append(voisin)
                        if voisin in voisins:
                            voisins.remove(voisin)
            salles.append(new_salle)
        self.remove_salle(salle)
        self.salles += salles
        return salles

    def scinde_couloir(self,couloir:Couloir,case:Position):
        i = couloir.cases.index(case)
        cases1,cases2 = couloir.cases[:i],couloir.cases[i+1:]
        couloirs = []
        if cases1 != []:
            couloir1 = Couloir()
            couloir1.cases = cases1
            self.couloirs.append(couloir1)
            couloirs.append(couloir1)
        if cases2 != []:
            couloir2 = Couloir()
            couloir2.cases = cases2
            self.couloirs.append(couloir2)
            couloirs.append(couloir2)
        self.remove_couloir(couloir)
        return couloirs

    def scinde_zone(self,zone:Zone_inconnue,case:Position):
        zone.cases.remove(case)
        voisins = [case+dir for dir in DIRECTIONS if case+dir in zone.cases]
        zones = []
        while voisins != []:
            depart = voisins.pop(0)
            queue = [depart]
            zone.cases.remove(depart)
            new_zone = Zone_inconnue(depart,zone)
            while len(queue):
                position = queue.pop(0)
                for dir in DIRECTIONS:
                    voisin = position+dir
                    if voisin in zone.cases and self.vue[position][5][dir][4]: # /!\ 4 ou 0 ?
                        zone.cases.remove(voisin)
                        queue.append(voisin)
                        new_zone.cases.append(voisin)
                        if voisin in voisins:
                            voisins.remove(voisin)
            zones.append(new_zone)
        self.remove_zone(zone)
        self.zones_inconnues += zones
        return zones

    def remove_salle(self,salle:Salle):
        self.salles.remove(salle)
        for entree in salle.entrees:
            if entree in self.entrees and salle in self.entrees[entree]:
                self.entrees[entree].remove(salle)
                if self.entrees[entree] == []: #Si la salle était la seule à avoir cette entrée
                    self.entrees.pop(entree) #On la supprime

    def remove_couloir(self,couloir:Couloir):
        self.couloirs.remove(couloir)
        for entree in couloir.entrees:
            if entree in self.entrees and couloir in self.entrees[entree]:
                self.entrees[entree].remove(couloir)
                if self.entrees[entree] == []: #Si le couloir était le seul à avoir cette entrée
                    self.entrees.pop(entree) #On le supprime

    def remove_zone(self,zone:Zone_inconnue):
        self.zones_inconnues.remove(zone)
        # print(len(self.zones_inconnues))
        for entree in zone.entrees:
            if entree in self.entrees and zone in self.entrees[entree]:
                self.entrees[entree].remove(zone)
                if self.entrees[entree] == []: #Si la zone était la seule à avoir cette entrée
                    self.entrees.pop(entree) #On la supprime
            # /!\ Regarder avec attention ce qui se passe pour les entrées

    def get_offenses(self):
        for corp in self.corps.keys(): #On vérifie si quelqu'un nous a offensé
            agissant:Agissant = self.controleur[corp]
            offenses,etat = agissant.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                self.antagonise_attaquant(offense)
                self.antagonise_supports(offense)
        
    def antagonise_attaquant(self,offense:Tuple[int,float,float]):
        ID_offenseur = offense[0]
        gravite = offense[1]
        degats = offense[2]
        if ID_offenseur in self.ennemis:
            self.ennemis[ID_offenseur][0] += gravite
            if self.ennemis[ID_offenseur][1] < degats:
                self.ennemis[ID_offenseur][1] = degats
        else:
            self.ennemis[ID_offenseur] = [gravite,degats]

    def antagonise_supports(self,offense:Tuple[int,float]):
        pass

    def get_pos_vues(self):
        positions = []
        for corp in self.corps.keys():
            if self.corps[corp] != "incapacite":
                agissant = self.controleur[corp]
                positions.append(agissant.position)
        return positions

    def trouve_strateges(self):
        # On détermine comment on va réfléchir (en fonction des stratèges qu'on a)
        # (Pour l'instant juste pour la traversée des portes, portails, escaliers)
        self.resolution = 0
        for ID_corp in self.corps.keys():
            corp = self.controleur[ID_corp]
            if isinstance(corp,Stratege): # Comment faire quand on a plusieurs stratèges ? /!\
                self.resolution = corp.resolution

    def unset_skip(self):
        for espace in self.salles+self.couloirs:
            espace.skip = False

    def set_skip(self,sources:List[Position],recepteurs:List[Position]):
        for espace in self.salles+self.couloirs:
            espace.skip = True
            for source in sources:
                if source in espace.get_cases():
                    espace.skip = False
            for recepteur in recepteurs:
                if recepteur in espace.get_all_cases():
                    espace.skip = False

    def calcule_trajets(self):
        # On détermine la dangerosité de chaque case en fonction des dégats qui vont y avoir lieu
        pos_corps = [self.controleur[corp].get_position() for corp in self.corps.keys() if self.corps[corp] != "incapacite"]
        coef=7 #/!\ Expérimenter avec ce coef à l'occasion
        for case in self.vue:
            for effet in case[7]:
                dangerosite = coef*effet[2]/(effet[1]+coef)
                case[3][2] += dangerosite
                case[3][3] += dangerosite

        # On modifie légèrement pour pouvoir sortir des zones concernées
        coef_croissant = 1.1
        # On commence par trouver les seuils, vers lesquels on va vouloir aller
        self.unset_skip()
        seuils = self.trouve_seuils(self.get_pos_vues()) # On part des différents endroit d'où l'on voit, qui devraient théoriquement nous donner accès à toute notre vision
        self.set_skip(seuils,pos_corps)
        self.propage(seuils,coef_croissant,3,False,-1) # On propage de façon croissante à partir des seuils (à l'intérieur)
        self.propage(seuils,coef_croissant,2,True,-1) # On propage de façon croissante à partir des seuils (à l'intérieur), en contournant les obstacles

        # On rajoute les ennemis
        coef_importance = 0.9
        coef_dangerosite = 0.9
        dangerosites = seuils
        importances = []
        for ID_ennemi in self.ennemis.keys():
            ennemi = self.controleur[ID_ennemi]
            if ennemi.etat == "vivant":
                position = ennemi.get_position()
                if position.lab in self.vue.keys():
                    importance = self.ennemis[ID_ennemi][0]
                    dangerosite = self.ennemis[ID_ennemi][1]
                    if importance > self.vue[position][3][0]:
                        self.vue[position][3][0]=importance
                        self.vue[position][3][1]=importance
                        importances.append(position)
                    if dangerosite > self.vue[position][3][2]:
                        self.vue[position][3][2]=dangerosite
                        if not position in dangerosites: # On peut avoir des doublons (ennemis sur les seuils par exemple)
                            dangerosites.append(position)
                    if dangerosite > self.vue[position][3][3]:
                        self.vue[position][3][3]=dangerosite
                        if not position in dangerosites:
                            dangerosites.append(position)
        # On propage l'importance de façon décroissante à partir des ennemis
        self.set_skip(importances,pos_corps)
        self.propage(importances,coef_importance) #Traversée
        self.propage(importances,coef_importance,0,True) #Contournement (<= Traversée)
        # On propage la dangerosité de façon décroissante à partir des ennemis et des seuils
        self.set_skip(dangerosites,pos_corps)
        self.propage(dangerosites,coef_dangerosite,3) #Traversée
        self.propage(dangerosites,coef_dangerosite,2,True) #Contournement

        # /!\ Prendre aussi en compte les alliés, et les cases inconnues (mais on va déjà tester ça)

    def resoud(self,position:Position,valeur:int,indice=1,dead_ends=False):
        """'Résoud' un labyrinthe à partir d'une case donnée."""

        if position in self.vue:

            if indice == 4:
                for case in self.vue:
                    case[3][4] = 0

            self.vue[position][3][indice] = valeur
            self.propage([position],self.dispersion_spatiale,indice,dead_ends)

    def propage(self,positions:List[Position],coef:float,indice=1,dead_ends=False,comparateur=1):
        """'Résoud' un labyrinthe à partir de plusieurs points"""

        #la queue est une liste de positions
        queue = [position for position in positions]

        arret_obstacle = False

        departs = len(positions)

        while len(queue) :
            position = queue.pop(0)

            if departs:
                departs -= 1
            else:
                arret_obstacle = dead_ends

            pos_explorables = self.positions_utilisables(position,arret_obstacle)

            for pos in pos_explorables:
                valeur = self.vue[position][3][indice]*coef**pos[1]
                if valeur*comparateur > self.vue[pos[0]][3][indice]*comparateur:
                    #on marque la case comme visitée
                    self.vue[pos[0]][3][indice] = valeur

                    #on ajoute toutes les directions explorables
                    queue.append(pos[0])

    def trouve_seuils(self,positions:List[Position],indice=2,dead_ends=False):
        """Fonction qui trouve les 'seuils', c'est à  dire les cases qui ont une valeur plus grande que leurs voisines"""

        for case in self.vue:
            case[3][5] = False

        seuils:List[Position] = []

        #la queue est une liste de positions
        queue = [position for position in positions]

        arret_obstacle = False

        departs = len(positions)

        while len(queue) :

            position = queue.pop(0)            

            #trouver les positions explorables

            if departs == 0:
                arret_obstacle = dead_ends
            else:
                departs -= 1

            pos_explorables = self.positions_utilisables(position,arret_obstacle)

            for pos in pos_explorables:
                if self.vue[position][3][indice] > self.vue[pos[0]][3][indice] and not position in seuils:
                    seuils.append(position)
                elif self.vue[position][3][indice] < self.vue[pos[0]][3][indice] and not pos[0] in seuils:
                    seuils.append(pos[0])
                if not self.vue[pos[0]][3][5]:
                    #on marque la case comme visitée
                    self.vue[pos[0]][3][5] = True
                        
                    #on ajoute toutes les directions explorables
                    queue.append(pos[0])
        return seuils

    def print_vue(self):
        for etage in self.vue.keys():
            matrice = self.vue[etage]
            print("Vue de l'esprit :")
            print(self.nom)
            for i in range(len(matrice)):
                haut = ""
                centre = ""
                bas = ""
                for j in range(len(matrice[0])):
                    case = matrice[i][j]
                    if case[1] == 0:
                        haut += " ~~~ "
                        centre += ": ? :"
                        bas += " ~~~ "
                    else:
                        haut+= " "
                        if case[5][0]:
                            haut += "   "
                        else:
                            haut += "---"
                        haut += " "
                        if case[5][3]:
                            centre += " "
                        else:
                            centre += "|"
                        if case[5] > 0:
                            centre += "x"
                        else:
                            centre += " "
                        if case[6] != []:
                            occ = " "
                            for occupant in case[6]:
                                if occupant in self.corps.keys():
                                    occ = "O"
                                elif occupant in self.ennemis.keys():
                                    occ = "X"
                            centre += occ
                        else:
                            centre += " "
                        if case[3][1] > 0:
                            centre += "x"
                        else:
                            centre += " "
                        if case[5][1]:
                            centre += " "
                        else:
                            centre += "|"
                        bas += " "
                        if case[5][2]:
                            bas += "   "
                        else:
                            bas += "---"
                        bas += " "
                print(haut)
                print(centre)
                print(bas)

    def print_zones(self):
        print(f"Vue de l'esprit {self.nom} :")
        zones_visibles = self.salles + self.couloirs
        zones_inconnues = self.zones_inconnues
        for etage in self.vue.keys():
            vue = self.vue[etage]
            print(f"Zones de l'étage {etage} :")
            for zones in [zones_visibles,zones_inconnues]:
                for j in range(vue.decalage.y):
                    haut = ""
                    milieu = ""
                    bas = ""
                    for i in range(vue.decalage.x):
                        case = vue[i,j]
                        # Le haut
                        haut+= " "
                        if case[5][0][4]:
                            haut += "   "
                        else:
                            haut += "---"
                        haut += " "
                        # La gauche
                        if case[5][3][4]:
                            gauche = " "
                        else:
                            gauche = "|"
                        # La droite
                        if case[5][1][4]:
                            droite = " "
                        else:
                            droite = "|"
                        # Le bas
                        bas += " "
                        if case[5][2][4]:
                            bas += "   "
                        else:
                            bas += "---"
                        bas += " "
                        # Le centre
                        for i in range(len(zones)):
                            if case[0] in zones[i].cases or case[0] in zones[i].entrees:
                                centre = f"{i:^{3}}"
                                break
                        else:
                            if case[1] > 0:
                                centre = "   "
                            else:
                                centre = " ? "
                        milieu += gauche + centre + droite
                    print(haut)
                    print(milieu)
                    print(bas)
                print("")

    def positions_utilisables(self,position:Position,dead_ends:bool):
        pos_utilisables:List[tuple[Position,int]]=[]

        case = self.vue[position]
        if position in self.entrees.keys():
            for direction in DIRECTIONS:
                if any(case[5][direction]) and not(dead_ends and case[6]!=[]) and not any([case[5][direction][4] in espace.cases and espace.skip for espace in self.entrees[position]]) and case[5][direction][4] in self.vue:
                    pos_utilisables.append((case[5][direction][4],1))
            for espace in self.entrees[position]:
                if espace.skip:
                    for entree in espace.entrees:
                        if entree in self.vue:
                            pos_utilisables.append((entree,espace.dist(position,entree)))
        else:
            for direction in DIRECTIONS:
                if any(case[5][direction]) and not(dead_ends and case[6]!=[]) and case[5][direction][4] in self.vue:
                    pos_utilisables.append((case[5][direction][4],1))

        return pos_utilisables

    def merge(self,nom_esprit:str):
        if nom_esprit != self.nom:
            esprit = self.controleur.esprits.pop(nom_esprit)
            self.merge_corps(esprit)
            self.merge_enemies(esprit)
            self.merge_vision(esprit)

    def merge_corps(self,esprit:Self):
        for corps in esprit.corps.keys():
            if corps not in self.corps.keys():
                self.corps[corps] = esprit.corps[corps]
                self.controleur[corps].rejoint(self.nom)

    def merge_enemies(self,esprit:Self):
        for ennemi in esprit.ennemis.keys():
            if ennemi not in self.corps.keys():
                self.ennemis[ennemi] = max(esprit.ennemis[ennemi],self.ennemis[ennemi])

    def merge_vision(self,esprit:Self):
        cases_self:List[Position] = []
        cases_other:List[Position] = []
        for etage in esprit.vue.keys():
            if etage not in self.vue:
                self.vue[etage] = esprit.vue[etage]
            else:
                selfs, others = self.merge_vue(esprit.vue[etage])
                cases_self += selfs
                cases_other += others                
        self.merge_representation(esprit,cases_self,cases_other)
        self.merge_zones(esprit,cases_self,cases_other)

    def antagonise(self,nom_esprit:str):
        for corp in self.controleur.get_esprit(nom_esprit).get_corps():
            if not corp in self.ennemis.keys():
                self.ennemis[corp] = [0.1,0]

    def decide(self):
        for corp in self.corps.keys():
            if self.corps[corp] in ["attaque","fuite","soin","soutien"]:
                self.deplace(corp)
            elif self.corps[corp] == "PNJ":
                self.deplace_pnj(corp)
            elif self.corps[corp] == "PJ":
                self.deplace_pj(corp)

    def fuite_utile(self,ID:int): #TODO inclure l'accessibilité
        for corp in self.corps.keys():
            if corp != ID and self.corps[corp] not in ["fuite","incapacite","mort"]:
                return True
        return False

    def deplace(self,ID:int):
        corp:Agissant = self.controleur[ID]
        position = corp.position
        case = corp.vue[position]
        tcase = self.vue[position]
        repoussante = tcase[8]
        cases = [[-1,tcase[0],tcase[3][0],tcase[3][1],-tcase[3][2],tcase[3][2],-tcase[3][3],tcase[3][3]]]
        dirs = []
        importance = 0
        fuite = corp.veut_fuir(tcase[3][2])
        attaque = corp.veut_attaquer(tcase[3][2])
        res = "attente"
        for i in DIRECTIONS: #On commence par se renseigner sur les possibilités :
            mur:Union[Position,Literal[False]] = case[5][i][self.resolution]
            if mur:
                if mur in position and corp.vue[mur][1]>0:
                    case_pot = self.vue[mur]
                    entitees = case_pot[6]
                    libre = True #On n'y va pas pour s'en enfuir après
                    for ID_entitee in entitees:
                        entitee = self.controleur[ID_entitee]
                        if issubclass(entitee.get_classe(),Non_superposable): #On ne peut pas aller sur cette case
                            libre = False
                            if issubclass(entitee.get_classe(),Agissant): #Elle est occupée par un agissant
                                if ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                    if corp.peut_voir(i) and (attaque or (fuite and not self.fuite_utile(ID))) : #On veut attaquer lorsqu'on croise un ennemi au corps à corps (et on a assez de mana pour, si on utilise la magie)
                                        if self.ennemis[ID_entitee][0] > importance:
                                            importance = self.ennemis[ID_entitee][0]
                                            corp.attaque(i)
                                            res = "attaque"
                                    elif fuite and self.fuite_utile(ID): #On veut fuire lorsqu'on croise un ennemi au corps à corps
                                        res = "fuite"
                    if libre:
                        cases.append([i,case_pot[0],case_pot[3][0],case_pot[3][1],-case_pot[3][2],case_pot[3][2],-case_pot[3][3],case_pot[3][3]])
                        dirs.append(i)
        if res == "attente": #Quelques comportements possibles :
            comportement = corp.comporte_distance(tcase[3][2])
            if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                res = "deplacement"
            elif comportement == 1 or (comportement > 1 and not self.fuite_utile(ID)): #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                res = corp.agit_en_vue(self,"deplacement")
                if repoussante:
                    res = "deplacement"
            elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                res = corp.agit_en_vue(self,"fuite")
                if repoussante:
                    res = "fuite"
            elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                res = "fuite"
        if res in ["deplacement","fuite"] and corp.latence <= 0:
            if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                res = "bloqué"
                corp.skill_courant = None
                importance = 0
                for i in DIRECTIONS:
                    mur:Union[Position,Literal[False]] = case[5][i][self.resolution]
                    if mur:
                        if mur.lab in self.vue.keys():
                            case_pot = self.vue[mur]
                            entitees = case_pot[6]
                            for ID_entitee in entitees:
                                entitee = corp.controleur[ID_entitee]
                                if issubclass(entitee.get_classe(),Agissant): #Cette case est occupée par un agissant
                                    if corp.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                        if self.ennemis[ID_entitee][0] > importance:
                                            importance = self.ennemis[ID_entitee][0]
                                            corp.attaque(i)
                                            res = "attaque"
            elif tcase[3][1] == 0: #Et tcase[3] forcément aussi par la même occasion, donc on est totalement libre de chercher
                res = "paix"
                if not isinstance(corp,Sentinelle) or isinstance(corp,Humain) or repoussante:
                    res = "exploration"
                    if len(dirs)>1: #On peut se permettre de choisir
                        if corp.dir_regard != None: #L'agissant regarde quelque part
                            dir_back = corp.dir_regard+2
                            if dir_back in dirs: #On ne veut pas y retourner
                                dirs.remove(dir_back)
                    corp.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                    if ID == 4: # /!\ Ne pas nettoyer, c'est très utile par moment
                        constantes_deplacements.append([self.controleur.nb_tours,"cherche",corp.dir_regard,cases])
            else:
                if repoussante: #On ne veut pas rester en place
                    cases.pop(0)
                if res == "deplacement":
                    new_cases = sorted(cases,key=operator.itemgetter(2,3,4,6)) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    res = "approche"
                    if new_cases[-1][0] != -1: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                        corp.va(new_cases[-1][0])
                        if ID == 4:
                            constantes_deplacements.append([self.controleur.nb_tours,"deplacement",corp.dir_regard,new_cases])
                    else:
                        res = corp.agit_en_vue(self)
                elif res == "fuite":
                    new_cases = sorted(cases,key=operator.itemgetter(5,7,2,3)) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    if new_cases[0][0] != -1: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                        corp.va(new_cases[0][0])
                        if ID == 4:
                            constantes_deplacements.append([self.controleur.nb_tours,"fuite",corp.dir_regard,new_cases])
                    else:
                        res = corp.agit_en_vue(self)
        corp.statut = res

    def deplace_pnj(self,ID:int):
        pnj:PNJ = self.controleur[ID]
        pnj.skill_courant = None
        pnj.statut_pnj = "proximite"
        if pnj.mouvement == 0: #0 pour aller vers, 1 pour chercher et 2 pour aller au contact
            if isinstance(pnj.cible_deplacement,int):
                if not(self.controleur.est_item(pnj.cible_deplacement)):
                    cible = self.controleur[pnj.cible_deplacement].get_position()
                    portee = 7
                else:
                    cible = pnj.get_position()
                    portee = 1 #C'est juste pour qu'il puisse aller où il veut
            else:
                cible = pnj.cible_deplacement
                portee = 5
            pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
        elif pnj.mouvement == 1:
            cible = pnj.get_position()
            portee = 1 #C'est juste pour qu'il puisse aller où il veut
            pnj.statut_pnj = "exploration"
        elif pnj.mouvement == 2:
            if isinstance(pnj.cible_deplacement,int):
                if not(self.controleur.est_item(pnj.cible_deplacement)):
                    cible = self.controleur[pnj.cible_deplacement].get_position()
                    portee = 0
                else:
                    cible = pnj.get_position()
                    portee = 1 #C'est juste pour qu'il puisse aller où il veut
            else:
                cible = pnj.cible_deplacement
                portee = 0
        elif pnj.mouvement == 3:
            pnj.statut_pnj = "attente"
            return
        pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
        if pnj.position in pos_cibles: #Tout va bien, on y est ! On peut combattre, par exemple.
            Esprit.deplace(self,ID)
        else:
            res = "recherche"
            position = pnj.get_position()
            self.set_skip([cible],[position])
            self.resoud(cible,10,4)
            case = self.vue[position]
            repoussante = case[8]
            cases = [[-1,case[0],case[3][0],case[3][1],-case[3][2],case[3][2],-case[3][3],case[3][3],case[3][4]]]
            dirs = []
            importance = 0
            fuite = pnj.veut_fuir(case[3][2])
            attaque = pnj.veut_attaquer(case[3][2])
            pnj.statut_pnj = "en chemin"
            if case[3][4] == 0:
                pnj.statut_pnj = "perdu"
                if pnj.ID == 4:
                    pnj.statut_pnj = "paume"
            for i in DIRECTIONS:
                mur = case[5][i][self.resolution]
                if mur:
                    if mur.lab in self.vue.keys():
                        case_pot = self.vue[mur]
                        entitees = case_pot[6]
                        libre = True
                        for ID_entitee in entitees:
                            entitee = pnj.controleur[ID_entitee]
                            if issubclass(entitee.get_classe(),Non_superposable): #On ne peut pas aller sur cette case
                                libre = False
                                if issubclass(entitee.get_classe(),Agissant): #Elle est occupée par un agissant
                                    if pnj.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                        if attaque: #Et le feu vert pour l'attaquer
                                            if self.ennemis[ID_entitee][0] > importance:
                                                importance = self.ennemis[ID_entitee][0]
                                                pnj.attaque(i)
                                                res = "attaque"
                                        elif fuite : #Et un ordre de fuite !
                                            res = "fuite"
                                    elif pnj.mouvement == 2 and ID_entitee == pnj.cible_deplacement and ID_entitee == self.controleur.joueur.ID and pnj.peut_voir(i): #Le PNJs peut enfin parler au joueur
                                        self.controleur.joueur.interlocuteur = pnj
                                        self.controleur.set_phase(DIALOGUE)
                                        pnj.start_dialogue()
                                        pnj.dir_regard = i
                                        self.controleur.joueur.dir_regard = i.oppose()
                                        pnj.mouvement = 0
                                    elif pnj.mouvement == 2 and ID_entitee == pnj.cible_deplacement and isinstance(self.controleur[ID_entitee], PNJ) and pnj is self.controleur.joueur and pnj.peut_voir(i): #Le joueur peut enfin parler au PNJ
                                        pnj.interlocuteur = self.controleur[ID_entitee]
                                        self.controleur.set_phase(DIALOGUE)
                                        self.controleur[ID_entitee].start_dialogue()
                                        pnj.dir_regard = i
                                        self.controleur[ID_entitee].dir_regard = i.oppose()
                                        pnj.mouvement = 0
                        if libre:
                            cases.append([i,case_pot[0],case_pot[3][0],case_pot[3][1],-case_pot[3][2],case_pot[3][2],-case_pot[3][3],case_pot[3][3],case_pot[3][4]])
                            dirs.append(i)
            if res == "recherche": #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer ni fuir)
                comportement = pnj.comporte_distance(case[3][2])
                if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                    res = "deplacement"
                elif comportement == 1: #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                    res = pnj.agit_en_vue(self,"deplacement")
                    if repoussante:
                        res = "deplacement"
                elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                    res = pnj.agit_en_vue(self,"fuite")
                    if repoussante:
                        res = "fuite"
                elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                    res = "fuite"
                if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                    pnj.skill_courant = None
                    importance = 0
                    for i in DIRECTIONS:
                        mur = case[5][i][self.resolution]
                        if mur:
                            if mur.lab in self.vue.keys():
                                case_pot = self.vue[mur]
                                entitees = case_pot[6]
                                libre = True
                                for ID_entitee in entitees:
                                    entitee = pnj.controleur[ID_entitee]
                                    if issubclass(entitee.get_classe(),Agissant): #Cette case est occupée par un agissant
                                        if pnj.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                            if self.ennemis[ID_entitee][0] > importance:
                                                importance = self.ennemis[ID_entitee][0]
                                                pnj.attaque(i)
                                                res = "attaque"
                elif not(case[3] or case[5]) and pnj.statut_pnj == "perdu":
                    res = "paix"
                    if not isinstance(pnj,Sentinelle) or repoussante:
                        res = "exploration"
                        if len(dirs)>1: #On peut se permettre de choisir
                            if pnj.dir_regard != None: #L'agissant regarde quelque part
                                dir_back = pnj.dir_regard+2
                                if dir_back in dirs: #On ne veut pas y retourner
                                    dirs.remove(dir_back)
                        pnj.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                elif pnj.statut_pnj == "paume":
                    res = "paix"
                    if repoussante:
                        res = "exploration"
                        if len(dirs)>1: #On peut se permettre de choisir
                            if pnj.dir_regard != None: #L'agissant regarde quelque part
                                dir_back = pnj.dir_regard+2
                                if dir_back in dirs: #On ne veut pas y retourner
                                    dirs.remove(dir_back)
                        pnj.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                else:
                    if repoussante:
                        cases.pop(0)
                    if res == "deplacement":
                        res = "approche"
                        new_cases = sorted(cases,key=operator.itemgetter(8,2,3,4,6))
                        if new_cases[-1][0] != -1: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                            pnj.va(new_cases[-1][0])
                            if ID == 4:
                                constantes_deplacements.append([self.controleur.nb_tours,"deplacement loin",pnj.dir_regard,new_cases])
                        else:
                            res = pnj.agit_en_vue(self)
                    elif res == "fuite":
                        for case in cases:
                            case[8] *= -1
                        new_cases = sorted(cases,key=operator.itemgetter(8,5,7,2,3))
                        if new_cases[0][0] != -1: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                            pnj.va(new_cases[0][0])
                            if ID == 4:
                                constantes_deplacements.append([self.controleur.nb_tours,"fuite loin",pnj.dir_regard,new_cases])
                        else:
                            res = pnj.agit_en_vue(self)
            pnj.statut = res

    def deplace_pj(self,ID:int):
        pj:PJ = self.controleur[ID]
        pj.statut_pnj = "proximite"
        if pj.mouvement == 0: #0 pour aller vers, 1 pour chercher et 2 pour aller au contact
            if isinstance(pj.cible_deplacement,int):
                if not(self.controleur.est_item(pj.cible_deplacement)):
                    cible = self.controleur[pj.cible_deplacement].get_position()
                    portee = 7
                else:
                    cible = pj.get_position()
                    portee = 2 #C'est juste pour qu'il puisse aller où il veut
            else:
                cible = pj.cible_deplacement
                portee = 5
            pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
        elif pj.mouvement == 1:
            cible = pj.get_position()
            portee = 2 #C'est juste pour qu'il puisse aller où il veut
            pj.statut_pnj = "exploration"
        elif pj.mouvement == 2:
            if isinstance(pj.cible_deplacement,int):
                if not(self.controleur.est_item(pj.cible_deplacement)):
                    cible = self.controleur[pj.cible_deplacement].get_position()
                    portee = 1
                else:
                    cible = pj.get_position()
                    portee = 2 #C'est juste pour qu'il puisse aller où il veut
            else:
                cible = pj.cible_deplacement
                portee = 1
        elif pj.mouvement == 3:
            pj.statut_pnj = "attente"
            return
        pos_cibles = self.controleur.get_pos_touches(cible,portee,propagation = "C__S___",direction = None,traverse="tout",responsable=0)
        if pj.position in pos_cibles: #Tout va bien, on y est ! On peut combattre, par exemple.
            self.simule_deplace(ID)
        else:
            res = "recherche"
            position = pj.get_position()
            self.set_skip([cible],[position])
            self.resoud(cible,10,4)
            case = self.vue[position]
            repoussante = case[8]
            cases = [[-1,case[0],case[3][0],case[3][1],-case[3][2],case[3][2],-case[3][3],case[3][3],case[3][4]]]
            dirs = []
            importance = 0
            fuite = pj.veut_fuir(case[3][2])
            attaque = pj.veut_attaquer(case[3][2])
            pj.statut_pnj = "en chemin"
            if case[3][4] == 0:
                pj.statut_pnj = "perdu"
                if pj.ID == 4:
                    pj.statut_pnj = "paume"
            for i in DIRECTIONS:
                mur = case[5][i][self.resolution]
                if mur:
                    if mur.lab in self.vue.keys():
                        case_pot = self.vue[mur]
                        entitees = case_pot[6]
                        libre = True
                        for ID_entitee in entitees:
                            entitee = pj.controleur[ID_entitee]
                            if issubclass(entitee.get_classe(),Non_superposable): #On ne peut pas aller sur cette case
                                libre = False
                                if issubclass(entitee.get_classe(),Agissant): #Elle est occupée par un agissant
                                    if pj.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                        if attaque: #Et le feu vert pour l'attaquer
                                            if self.ennemis[ID_entitee][0] > importance:
                                                importance = self.ennemis[ID_entitee][0]
                                                pj.simule_attaque(i)
                                                res = "attaque"
                                        elif fuite : #Et un ordre de fuite !
                                            res = "fuite"
                        if libre:
                            cases.append([i,case_pot[0],case_pot[3][0],case_pot[3][1],-case_pot[3][2],case_pot[3][2],-case_pot[3][3],case_pot[3][3],case_pot[3][4]])
                            dirs.append(i)
            if res == "recherche": #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer ni fuir)
                comportement = pj.comporte_distance(case[3][2])
                if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                    res = "deplacement"
                elif comportement == 1: #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                    res = pj.simule_agit_en_vue(self,"deplacement")
                    if repoussante:
                        res = "deplacement"
                elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                    res = pj.simule_agit_en_vue(self,"fuite")
                    if repoussante:
                        res = "fuite"
                elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                    res = "fuite"
                if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                    pj.skill_courant = None
                    importance = 0
                    for i in DIRECTIONS:
                        mur = case[5][i][self.resolution]
                        if mur:
                            if mur.lab in self.vue.keys():
                                case_pot = self.vue[mur]
                                entitees = case_pot[6]
                                libre = True
                                for ID_entitee in entitees:
                                    entitee = pj.controleur[ID_entitee]
                                    if issubclass(entitee.get_classe(),Agissant): #Cette case est occupée par un agissant
                                        if pj.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                            if self.ennemis[ID_entitee][0] > importance:
                                                importance = self.ennemis[ID_entitee][0]
                                                pj.simule_attaque(i)
                                                res = "attaque"
                elif not(case[3] or case[5]) and pj.statut_pnj == "perdu":
                    res = "paix"
                    if not isinstance(pj,Sentinelle) or repoussante:
                        res = "exploration"
                        if len(dirs)>1: #On peut se permettre de choisir
                            if pj.dir_regard != None: #L'agissant regarde quelque part
                                dir_back = pj.dir_regard+2
                                if dir_back in dirs: #On ne veut pas y retourner
                                    dirs.remove(dir_back)
                        pj.simule_va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                elif pj.statut_pnj == "paume":
                    res = "paix"
                    if repoussante:
                        res = "exploration"
                        if len(dirs)>1: #On peut se permettre de choisir
                            if pj.dir_regard != None: #L'agissant regarde quelque part
                                dir_back = pj.dir_regard+2
                                if dir_back in dirs: #On ne veut pas y retourner
                                    dirs.remove(dir_back)
                        pj.simule_va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                else:
                    if repoussante:
                        cases.pop(0)
                    if res == "deplacement":
                        res = "approche"
                        new_cases = sorted(cases,key=operator.itemgetter(8,2,3,4,6))
                        if new_cases[-1][0] != -1: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                            pj.simule_va(new_cases[-1][0])
                        else:
                            res = pj.simule_agit_en_vue(self)
                    elif res == "fuite":
                        for case in cases:
                            case[8] *= -1
                        new_cases = sorted(cases,key=operator.itemgetter(8,5,7,2,3))
                        if new_cases[0][0] != -1: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                            pj.simule_va(new_cases[0][0])
                        else:
                            res = pj.simule_agit_en_vue(self)

    def simule_deplace(self,ID:int):
        pj:PJ = self.controleur[ID]
        position = pj.position
        case = pj.vue[position]
        tcase = self.vue[position]
        repoussante = tcase[8]
        cases = [[-1,tcase[0],tcase[3][0],tcase[3][1],-tcase[3][2],tcase[3][2],-tcase[3][3],tcase[3][3]]]
        dirs = []
        importance = 0
        fuite = pj.veut_fuir(tcase[3][2])
        attaque = pj.veut_attaquer(tcase[3][2])
        res = "attente"
        for i in DIRECTIONS: #On commence par se renseigner sur les possibilités :
            mur:Union[Position,Literal[False]] = case[5][i][self.resolution]
            if mur:
                if mur in position and pj.vue[mur][1]>0:
                    case_pot = self.vue[mur]
                    entitees = case_pot[6]
                    libre = True #On n'y va pas pour s'en enfuir après
                    for ID_entitee in entitees:
                        entitee = self.controleur[ID_entitee]
                        if issubclass(entitee.get_classe(),Non_superposable): #On ne peut pas aller sur cette case
                            libre = False
                            if issubclass(entitee.get_classe(),Agissant): #Elle est occupée par un agissant
                                if ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                    if pj.peut_voir(i) and (attaque or (fuite and not self.fuite_utile(ID))) : #On veut attaquer lorsqu'on croise un ennemi au corps à corps (et on a assez de mana pour, si on utilise la magie)
                                        if self.ennemis[ID_entitee][0] > importance:
                                            importance = self.ennemis[ID_entitee][0]
                                            pj.simule_attaque(i)
                                            res = "attaque"
                                    elif fuite and self.fuite_utile(ID): #On veut fuire lorsqu'on croise un ennemi au corps à corps
                                        res = "fuite"
                    if libre:
                        cases.append([i,case_pot[0],case_pot[3][0],case_pot[3][1],-case_pot[3][2],case_pot[3][2],-case_pot[3][3],case_pot[3][3]])
                        dirs.append(i)
        if res == "attente": #Quelques comportements possibles :
            comportement = pj.comporte_distance(tcase[3][2])
            if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                res = "deplacement"
            elif comportement == 1 or (comportement > 1 and not self.fuite_utile(ID)): #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                res = pj.simule_agit_en_vue(self,"deplacement")
                if repoussante:
                    res = "deplacement"
            elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                res = pj.simule_agit_en_vue(self,"fuite")
                if repoussante:
                    res = "fuite"
            elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                res = "fuite"
        if res in ["deplacement","fuite"] and pj.latence <= 0:
            if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                res = "bloqué"
                pj.skill_courant = None
                importance = 0
                for i in DIRECTIONS:
                    mur:Union[Position,Literal[False]] = case[5][i][self.resolution]
                    if mur:
                        if mur.lab in self.vue.keys():
                            case_pot = self.vue[mur]
                            entitees = case_pot[6]
                            for ID_entitee in entitees:
                                entitee = pj.controleur[ID_entitee]
                                if issubclass(entitee.get_classe(),Agissant): #Cette case est occupée par un agissant
                                    if pj.peut_voir(i) and ID_entitee in self.ennemis.keys(): #Et c'est un ennemi !
                                        if self.ennemis[ID_entitee][0] > importance:
                                            importance = self.ennemis[ID_entitee][0]
                                            pj.simule_attaque(i)
                                            res = "attaque"
            elif tcase[3][1] == 0: #Et tcase[3] forcément aussi par la même occasion, donc on est totalement libre de chercher
                res = "paix"
                if not isinstance(pj,Sentinelle) or isinstance(pj,Humain) or repoussante:
                    res = "exploration"
                    if len(dirs)>1: #On peut se permettre de choisir
                        if pj.dir_regard != None: #L'agissant regarde quelque part
                            dir_back = pj.dir_regard+2
                            if dir_back in dirs: #On ne veut pas y retourner
                                dirs.remove(dir_back)
                    pj.simule_va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                    if ID == 4: # /!\ Ne pas nettoyer, c'est très utile par moment
                        constantes_deplacements.append([self.controleur.nb_tours,"cherche",pj.dir_regard,cases])
            else:
                if repoussante: #On ne veut pas rester en place
                    cases.pop(0)
                if res == "deplacement":
                    new_cases = sorted(cases,key=operator.itemgetter(2,3,4,6)) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    res = "approche"
                    if new_cases[-1][0] != -1: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                        pj.simule_va(new_cases[-1][0])
                    else:
                        res = pj.simule_agit_en_vue(self)
                elif res == "fuite":
                    new_cases = sorted(cases,key=operator.itemgetter(5,7,2,3)) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    if new_cases[0][0] != -1: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                        pj.simule_va(new_cases[0][0])
                        if ID == 4:
                            constantes_deplacements.append([self.controleur.nb_tours,"fuite",pj.dir_regard,new_cases])
                    else:
                        res = pj.simule_agit_en_vue(self)

    def oublie(self):
        anciennes_cases = []
        for case in self.vue:
            if case[2] > 1:
                case[2] -= 1
            elif case[2] > 0:
                case[1] = 0
                case[2] = 0
                case[4] = 0
                case[5] = [[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]]
                case[6] = []
                anciennes_cases.append(case[0])
            case[3] = [0,0,0,0,0,False]
            case[7] = []
            case[8] = False
            
        self.downdate_zones(anciennes_cases)
        self.downdate_representation(anciennes_cases)

    #Découvront le déroulé d'un tour avec esprit-sensei :
    def debut_tour(self):
        #On va faire plein de choses pendant ce tour (est-ce vraiment nécessaire de prendre des décisions si aucun des corps ne va jouer à ce tour ?
        self.get_offenses() #On s'insurge à grands cris (s'il y a lieu)
        self.refait_vue() #On prend connaissance de son environnement
        #Il faudra éventuellement définir une stratégie
        self.trouve_strateges()
        self.calcule_trajets() #On dresse les plans de bataille (s'il y a lieu)
        self.decide() #On donne les ordres

    def pseudo_debut_tour(self):
        pass

    #Tout le monde agit, nos bon-à-rien d'agissants se font massacrer à cause de leurs capacités médiocres ou remportent la victoire grâce à nos ordres brillants

    def fin_tour(self):
        #Le tour est fini, on réfléchira pendant le prochain. Comment ça, c'est mauvais pour la mémoire ?
        self.oublie()
