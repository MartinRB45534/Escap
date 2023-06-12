from __future__ import annotations
from typing import TYPE_CHECKING, List, Dict, Set, Tuple, Self, Literal
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Agissant.Vue.Vue import Vue
    from .Vision.Vision import Vision
    # from ..Esprit.Representation_spatiale import Espace_schematique

# Pas de classe parente

class Esprit :
    """La classe des esprits, qui manipulent les agisants."""
    def __init__(self,nom:str): #On identifie les esprits par des noms (en fait on s'en fout, vu qu'on ne fait pas d'opérations dessus on pourrait avoir des labs, des entitees et des esprits nommés avec des str, des int, des float, des bool, etc.)
        self.corps:Dict[Agissant,str] = {}
        self.vision = Vision(set(),0)
        self.tour = 0 # Chaque esprit a son horloge interne
        self.ennemis:Dict[Agissant,Dict[str,float]] = {}
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = []
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.oubli = 0
        self.resolution = 0 #0 pour se déplacer normalement, 1 pour passer les portes dont on a les clés, 2 pour traverser les portails, 3 pour passer les portes et les portails, 4 pour passer partout (portes, portails, changer d'étage)
        self.nom = nom

    def ajoute_corp(self,corp:Agissant):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            corp.rejoint(self)

    def ajoute_corps(self,corps:List[Agissant]):
        for corp in corps:
            self.ajoute_corp(corp)

    def retire_corp(self,corp:Agissant):
        if corp in self.corps:
            self.corps.pop(corp)

    def retire_corps(self,corps:List[Agissant]):
        for corp in corps:
            self.retire_corp(corp)

    def get_corps(self):
        return {*self.corps.keys()}

    def get_ennemis(self):
        return {*self.ennemis.keys()}

    # def get_importance(self,position:crt.Position) -> float:
    #     importance = 0
    #     if position in self.vue:
    #         case = self.vue.case_from_position(position)
    #         if case.agissant is not None:
    #             if case.agissant in self.ennemis:
    #                 new_importance = self.ennemis[case.agissant]["importance"]
    #                 if new_importance > importance:
    #                     importance = new_importance
    #     return importance

    # def trouve_agissants(self) -> Set[Agissant]:
    #     agissants = set()
    #     for case in self.vue:
    #         agissants.add(case.agissant) if case.agissant is not None else None
    #     return agissants

    # def get_corps_vus(self) -> Set[Agissant]:
    #     return {corp for corp in self.trouve_agissants() if corp in self.corps}

    # def get_ennemis_vus(self) -> Set[Agissant]:
    #     return {ennemi for ennemi in self.trouve_agissants() if ennemi in self.ennemis}

    # def get_neutres_vus(self) -> Set[Agissant]:
    #     return {neutre for neutre in self.trouve_agissants() if neutre not in self.corps and neutre not in self.ennemis}

    # def oublie_agissants(self,agissants:Set[Agissant]):
    #     for case in self.vue:
    #         if case.agissant in agissants:
    #             case.agissant = None
    #     for zone in self.zones_inconnues:
    #         zone.occupants -= agissants

    def refait_vue(self):
        vues:Set[Vue] = set()
        for corp in self.corps:
            if self.corps[corp] != "incapacite":
                vues.add(corp.vue)
        self.vision.voit(vues, self.tour)
        # TODO : préjugés & zones

    # def update_zones(self,cases:Set[Representation_case],nouvelles_cases:Set[Representation_case],cases_limites:Set[Representation_case],agissants_oublies:Set[Tuple[Agissant,Representation_case]]):
    #     cases_memorisees = {case for case in self.vue if case.oubli>0} - cases
    #     # print(cases)
    #     # print(nouvelles_cases)
    #     zones_mod:Set[Zone_inconnue] = set()
    #     for case in nouvelles_cases:
    #         for zone in self.zones_inconnues:
    #             if case in zone.cases:
    #                 # print("Scinde")
    #                 zones_mod |= self.scinde_zone(zone,case)
    #     for zone in self.zones_inconnues:
    #         for case in zone.cases:
    #             if case in cases_memorisees:
    #                 cases_memorisees.remove(case)
    #             # else:
    #             #     print("I'm useful !")
    #     for case in cases_memorisees:
    #         zone = Zone_inconnue(case.case.position)
    #         self.zones_inconnues.add(zone)
    #         for zone_ in [*self.zones_inconnues]:
    #             if zone_ != zone:
    #                 for DIR in DIRECTIONS:
    #                     voisin = case.cibles[DIR][PASSE_ESCALIER]
    #                     if voisin and voisin in zone_.cases:
    #                         zone = self.fusionne_zones(zone,zone_)
    #                         break
    #             if zone not in zones_mod:
    #                 zones_mod.add(zone)
    #     for case in cases_limites:
    #         if case.clarte == 0:
    #             zone = Zone_inconnue(case.case.position)
    #             self.zones_inconnues.add(zone)
    #             for zone_ in self.zones_inconnues:
    #                 if zone_ != zone:
    #                     for DIR in DIRECTIONS:
    #                         voisin = case.cibles[DIR][PASSE_ESCALIER]
    #                         if voisin and voisin in zone_.cases:
    #                             zone = self.fusionne_zones(zone,zone_)
    #                             break
    #                 if zone not in zones_mod:
    #                     zones_mod.add(zone)
    #         elif case.clarte < 0:
    #             if case.clarte != -1:
    #                 print("Why !!?")
    #     for zone in self.zones_inconnues:
    #         zone.entrees = set()
    #         zone.sorties = set()
    #         for tup in agissants_oublies:
    #             if tup[1] in zone.cases:
    #                 zone.occupants.add(tup[0])
    #             for DIR in DIRECTIONS:
    #                 voisin = tup[1].cibles[DIR][PASSE_ESCALIER]
    #                 if voisin and voisin in zone.cases:
    #                     zone.occupants.add(tup[0])
    #         for case in zone.cases:
    #             for DIR in DIRECTIONS:
    #                 voisin = self.vue.case_from_position(case).cibles[DIR][PASSE_ESCALIER]
    #                 if voisin and ((not voisin in self.vue) or self.vue.case_from_position(voisin).clarte == 0):
    #                     zone.sorties.add(voisin)
    #                     zones_mod.add(zone)
    #         for case in [*cases_limites]:
    #             if case in zone.cases:
    #                 zone.cases.remove(case)
    #                 zone.entrees.add(case)
    #                 cases_limites.remove(case)
    #                 zones_mod.add(zone)
    #         if zone.cases == set() and zone.entrees == set():
    #             self.remove_zone(zone)

    # def update_representation(self,cases:Set[Representation_case]):
    #     carres_pot:Set[Position] = set()
    #     for case in cases:
    #         pos = case.case.position
    #         for dec in Decalage(2,2):
    #             if pos-dec in self.vue and pos-dec+Decalage(1,1) in self.vue:
    #                 carres_pot.add(pos-dec)
    #     carres:Set[Position] = set()
    #     for carre_pot in carres_pot:
    #         if self.vue.case_from_position(carre_pot).cibles[DROITE][BASIQUE] and self.vue.case_from_position(carre_pot+DROITE).cibles[GAUCHE][BASIQUE] and self.vue.case_from_position(carre_pot).cibles[BAS][BASIQUE] and self.vue.case_from_position(carre_pot+BAS).cibles[HAUT][BASIQUE] and self.vue.case_from_position(carre_pot+BAS).cibles[DROITE][BASIQUE] and self.vue.case_from_position(carre_pot+DROITE+BAS).cibles[GAUCHE][BASIQUE] and self.vue.case_from_position(carre_pot+DROITE).cibles[BAS][BASIQUE] and self.vue.case_from_position(carre_pot+BAS+DROITE).cibles[HAUT][BASIQUE] :
    #             carres.add(carre_pot)
    #             if carre_pot.lab == "Étage 3 : combat":
    #                 if carre_pot.x in range(2,5) and carre_pot.y in range(7,10):
    #                     print("Check1")
    #     salles_mod:Set[Salle] = set() #Les salles qu'on a modifiées
    #     couloirs_mod:Set[Couloir] = set() #Les couloirs qu'on a modifiés
    #     # print("Salles :")
    #     # print(len(self.salles))
    #     for carre in carres:
    #         # if self.nom == "heros":
    #         #     print(carre)
    #         libre = True
    #         for salle in self.salles:
    #             if carre in salle.carres:
    #                 libre = False #Arrive par exemple lorsqu'on ouvre une porte à côté d'une case déjà dans une salle
    #                 salles_mod.add(salle) #Si on a ouvert une porte, on veut rajouter cette case aux entrées (sinon on a des problèmes de résolution)
    #                 break
    #         if libre:
    #             # print("Nouvelle salle !")
    #             salle = Salle(carre)
    #             # print(len(salle.carres))
    #             self.salles.add(salle)
    #             for salle_ in [*self.salles]:
    #                 if salle_ != salle: #Peut arriver si on partage plusieurs cases avec une salle existante
    #                     for dir in DIRECTIONS:
    #                         if carre+dir in salle_.carres: #Ces deux carrés partagent deux cases : les deux salles n'en forment qu'une seule
    #                             salle = self.fusionne_salles(salle_,salle)
    #                             # print("Fusion de salles !")
    #                             # print(len(salle.carres))
    #                             break
    #             salles_mod.add(salle)
    #         for dec in Decalage(2,2):
    #             for couloir in [*self.couloirs]:
    #                 if carre+dec in couloir.cases: #Cette case appartenait à un couloir. Ce n'est plus le cas car des murs ont été ouverts (portes, écrasement, etc.) et elle appartient désormais à une salle
    #                     couloirs_mod |= self.scinde_couloir(couloir,carre+dec)
    #     # print("Salles :")
    #     # print(len(self.salles))
    #     # print("Salles modifiées :")
    #     # print(len(salles_mod))
    #     # print("Intersection")
    #     # print(len([salle for salle in salles_mod if salle in self.salles]))
    #     for salle in [*salles_mod]:
    #         if salle in self.salles: #On peut en avoir retirées
    #             # print("Salle modifiée !")
    #             # print(len(salle.carres))
    #             salle.add_cases()
    #             salle.make_bord()
    #             for entree in salle.entrees:
    #                 if entree in self.entrees:
    #                     self.entrees[entree].remove(salle)
    #                     if self.entrees[entree] == []:
    #                         self.entrees.pop(entree)
    #             salle.entrees = {bord.emplacement for bord in salle.frontiere if self.vue.case_from_position(bord.emplacement).cibles[bord.direction][4]}
    #             salle.calcule_distances()
    #             for case in salle.cases:
    #                 if case in cases:
    #                     cases.remove(case)
    #                 if case.lab == "Étage 3 : combat":
    #                     if case.x in range(2,5) and case.y in range(7,10):
    #                         print("Check2")
    #                         print(case.x,case.y)
    #                 if case in cases:
    #                     print("Toujours là")
    #             for entree in salle.entrees:
    #                 salle.cases.remove(entree)
    #         else:
    #             # print("Salle supprimée !")
    #             # print(len(salle.carres))
    #             salles_mod.remove(salle)
    #     # print("Salles :")
    #     # for salle in self.salles:
    #     #     print("Salle : ")
    #     #     print(salle.cases)
    #     #     print(salle.carres)
    #     for case in cases:
    #         if sum([int(not(not(case.cibles[dir][PASSE_ESCALIER]))) for dir in DIRECTIONS]) < 3:
    #             libre = True
    #             for couloir in self.couloirs:
    #                 if case in couloir.cases:
    #                     break
    #             else:
    #                 couloir = Couloir(case.case.position)
    #                 self.couloirs.add(couloir)
    #                 for couloir_ in [*self.couloirs]:
    #                     if couloir_ != couloir:
    #                         for dir in DIRECTIONS:
    #                             if case.case.position+dir in couloir_.cases and case.cibles[dir][PASSE_ESCALIER] and self.vue.case_from_position(case.case.position+dir).cibles[dir.oppose()][PASSE_ESCALIER]:
    #                                 couloir = self.fusionne_couloirs(couloir_,couloir)
    #                                 break
    #             if couloir not in couloirs_mod:
    #                 couloirs_mod.add(couloir)
    #         else:
    #             for couloir in self.couloirs:
    #                 if case in couloir.cases: #Cette case appartenait à un couloir. Ce n'est plus le cas car des murs ont été ouverts (portes, écrasement, etc.)
    #                     couloirs_mod |= self.scinde_couloir(couloir,case)
    #                     break
    #         # if case.case.position.lab == "Étage 3 : combat":
    #         #     if case.case.position.x in range(2,5) and case.case.position.y in range(7,10):
    #         #         print("Bad check")
    #         #         print(case.case.position.x, case.case.position.y)
    #     for couloir in [*couloirs_mod]:
    #         if couloir in self.couloirs:
    #             couloir.entrees = set()
    #             for dir in DIRECTIONS:
    #                 case1 = self.vue.case_from_position(couloir.cases[0]).cibles[dir][PASSE_ESCALIER]
    #                 if case1 and case1 not in couloir.cases: #Un mur vers l'extérieur !
    #                     couloir.entrees.add(case1)
    #                 case2 = self.vue.case_from_position(couloir.cases[-1]).cibles[dir][PASSE_ESCALIER]
    #                 if len(couloir.cases)>1 and case2 and case2 not in couloir.cases: #Un mur vers l'extérieur !
    #                     couloir.entrees.add(case2)
    #         else:
    #             couloirs_mod.remove(couloir)
    #     for espace in salles_mod | couloirs_mod:
    #         for entree in espace.entrees:
    #             if espace not in self.entrees.get(entree,set()) and espace in self.salles|self.couloirs:
    #                 self.entrees[entree] = self.entrees.get(entree,set())|{espace}

    # def downdate_zones(self,cases:List[Position]):
    #     zones_mod:List[Zone_inconnue] = []
    #     for case in cases:
    #         for zone in [*self.zones_inconnues]:
    #             if case in zone.cases:
    #                 zones_mod += self.scinde_zone(zone,case)
    #     for zone in zones_mod:
    #         if zone in self.zones_inconnues:
    #             zone.sorties = set()
    #             for case in zone.cases:
    #                 for DIR in DIRECTIONS:
    #                     voisin = self.vue.case_from_position(case).cibles[DIR][PASSE_ESCALIER]
    #                     if voisin and ((not voisin in self.vue) or self.vue.case_from_position(voisin).clarte == 0):
    #                         zone.sorties.add(voisin)

    # def downdate_representation(self,cases:List[Position]):
    #     carres_pot:List[Position] = []
    #     for case in cases:
    #         for dec in Decalage(2,2):
    #             if case-dec in self.vue and case-dec+Decalage(1,1) in self.vue:
    #                 carres_pot.append(case-dec)
    #     carres_pot = [*set(carres_pot)]
    #     carres_suppr:List[Position] = []
    #     for carre_pot in carres_pot:
    #         if not(self.vue.case_from_position(carre_pot).cibles[DROITE][BASIQUE] and self.vue.case_from_position(carre_pot+DROITE).cibles[GAUCHE][BASIQUE] and self.vue.case_from_position(carre_pot+BAS).cibles[DROITE][BASIQUE] and self.vue.case_from_position(carre_pot+DROITE+BAS).cibles[GAUCHE][BASIQUE] and self.vue.case_from_position(carre_pot).cibles[BAS][BASIQUE] and self.vue.case_from_position(carre_pot+BAS).cibles[HAUT][BASIQUE] and self.vue.case_from_position(carre_pot+DROITE).cibles[BAS][BASIQUE] and self.vue.case_from_position(carre_pot+BAS+DROITE).cibles[HAUT][BASIQUE]):
    #             carres_suppr.append(carre_pot)
    #     salles_mod:List[Salle] = [] #Les salles qu'on a modifiées
    #     for carre in carres_suppr:
    #         for salle in [*self.salles]:
    #             if carre in salle.carres:
    #                 salles_mod += self.scinde_salle(salle,carre)
    #     couloirs_mod:List[Couloir] = []
    #     for salle in salles_mod:
    #         if salle in self.salles: #On peut en avoir retirées
    #             salle.add_cases()
    #             salle.make_bord()
    #             for entree in salle.entrees:
    #                 if entree in self.entrees:
    #                     self.entrees[entree].remove(salle)
    #                     if self.entrees[entree] == []:
    #                         self.entrees.pop(entree)
    #             salle.entrees = {bord.emplacement for bord in salle.frontiere if self.vue.case_from_position(bord.emplacement).cibles[bord.direction][4]}
    #             salle.calcule_distances()
    #     for case in cases:
    #         for couloir in [*self.couloirs]:
    #             if case in couloir.cases:
    #                 couloirs_mod += self.scinde_couloir(couloir,case)
    #     for couloir in couloirs_mod:
    #         if couloir in self.couloirs:
    #             couloir.entrees = set()
    #             for dir in DIRECTIONS:
    #                 case = self.vue.case_from_position(couloir.cases[0]).cibles[dir][PASSE_ESCALIER]
    #                 if case and case not in couloir.cases: #Un mur vers l'extérieur !
    #                     couloir.entrees.add(case)
    #                 case = self.vue.case_from_position(couloir.cases[-1]).cibles[dir][PASSE_ESCALIER]
    #                 if case and case not in couloir.cases: #Un mur vers l'extérieur !
    #                     couloir.entrees.add(case)
    #     for espace in salles_mod + couloirs_mod:
    #         for entree in espace.entrees:
    #             self.entrees[entree] = self.entrees.get(entree,set())|{espace}

    # def merge_zones(self,esprit:Self,cases_self:Set[Representation_case],cases_esprit:Set[Representation_case]):
    #     zones_mod:Set[Zone_inconnue] = set()
    #     entrees:Set[Position] = set()
    #     for zone in self.zones_inconnues|esprit.zones_inconnues:
    #         entrees |= zone.entrees
    #     for zone in self.zones_inconnues|esprit.zones_inconnues:
    #         zone.cases |= zone.entrees
    #         zone.entrees = set()
    #     for case in cases_self:
    #         for zone in esprit.zones_inconnues:
    #             if case in zone.cases:
    #                 zones_mod |= esprit.scinde_zone(zone,case)
    #                 break
    #     for case in cases_esprit:
    #         for zone in self.zones_inconnues:
    #             if case in zone.cases:
    #                 zones_mod |= self.scinde_zone(zone,case)
    #                 break
    #     for zone in [*self.zones_inconnues]:
    #         for zone_ in [*esprit.zones_inconnues]:
    #             for case in zone.cases:
    #                 if case in zone_.cases:
    #                     zones_mod.add(esprit.fusionne_zones(zone,zone_))
    #                     break
    #     self.zones_inconnues |= esprit.zones_inconnues
    #     for zone in self.zones_inconnues:
    #         for entree in entrees:
    #             if entree in zone.cases:
    #                 zone.cases.remove(entree)
    #                 zone.entrees.add(entree)
    #     for zone in zones_mod:
    #         if zone in self.zones_inconnues:
    #             zone.sorties = set()
    #             for case in zone.cases:
    #                 for DIR in DIRECTIONS:
    #                     voisin = self.vue.case_from_position(case).cibles[DIR][PASSE_ESCALIER]
    #                     if voisin and ((not voisin in self.vue) or self.vue.case_from_position(voisin).clarte == 0):
    #                         zone.sorties.add(voisin)
        
    # def merge_representation(self,esprit:Self,cases_self:Set[Representation_case],cases_esprit:Set[Representation_case]):
    #     salles_mod:List[Salle] = []
    #     carres_pot_esprit:List[Position] = []
    #     carres_pot_self:List[Position] = []
    #     for case in cases_self:
    #         for dec in Decalage(2,2):
    #             if case.case.position-dec in self.vue and case.case.position-dec+Decalage(1,1) in self.vue:
    #                 carres_pot_esprit.append(case.case.position-dec)
    #     for case in cases_esprit:
    #         for dec in Decalage(2,2):
    #             if case.case.position-dec in esprit.vue and case.case.position-dec+Decalage(1,1) in esprit.vue:
    #                 carres_pot_self.append(case.case.position-dec)
    #     carres_esprit:List[Position] = []
    #     carres_self:List[Position] = []
    #     for carre in carres_pot_esprit:
    #         if self.vue.case_from_position(carre).cibles[DROITE][BASIQUE] and self.vue.case_from_position(carre+DROITE).cibles[GAUCHE][BASIQUE] and self.vue.case_from_position(carre).cibles[BAS][BASIQUE] and self.vue.case_from_position(carre+BAS).cibles[HAUT][BASIQUE] and self.vue.case_from_position(carre+BAS).cibles[DROITE][BASIQUE] and self.vue.case_from_position(carre+DROITE+BAS).cibles[GAUCHE][BASIQUE] and self.vue.case_from_position(carre+DROITE).cibles[BAS][BASIQUE] and self.vue.case_from_position(carre+BAS+DROITE).cibles[HAUT][BASIQUE] :
    #             if not all([carre+dec in cases_self for dec in Decalage(2,2)]): # Si le carré était déjà entièrement visible par self, on s'en est déjà occupé plus tôt
    #                 carres_esprit.append(carre)
    #     for carre in carres_pot_self:
    #         if esprit.vue.case_from_position(carre).cibles[DROITE][BASIQUE] and esprit.vue.case_from_position(carre+DROITE).cibles[GAUCHE][BASIQUE] and esprit.vue.case_from_position(carre).cibles[BAS][BASIQUE] and esprit.vue.case_from_position(carre+BAS).cibles[HAUT][BASIQUE] and esprit.vue.case_from_position(carre+BAS).cibles[DROITE][BASIQUE] and esprit.vue.case_from_position(carre+DROITE+BAS).cibles[GAUCHE][BASIQUE] and esprit.vue.case_from_position(carre+DROITE).cibles[BAS][BASIQUE] and esprit.vue.case_from_position(carre+BAS+DROITE).cibles[HAUT][BASIQUE] :
    #             if not all([carre+dec in cases_esprit for dec in Decalage(2,2)]):
    #                 carres_self.append(carre)
    #     couloirs_mod:List[Couloir] = []
    #     for carre in carres_esprit:
    #         libre = True
    #         for salle in esprit.salles:
    #             if carre in salle.carres: # Ne devrait pas arriver
    #                 libre = False #Arrive par exemple lorsqu'on ouvre une porte à côté d'une case déjà dans une salle
    #                 if salle not in salles_mod:
    #                     salles_mod.append(salle) #Si on a ouvert une porte, on veut rajouter cette case aux entrées (sinon on a des problèmes de résolution)
    #                 break
    #         if libre:
    #             salle = Salle(carre)
    #             esprit.salles.add(salle)
    #             for salle_ in [*esprit.salles]:
    #                 if salle_ != salle: #Peut arriver si on partage plusieurs cases avec une salle existante
    #                     for dir in DIRECTIONS:
    #                         if carre+dir in salle_.carres: #Ces deux carrés partagent deux cases : les deux salles n'en forment qu'une seule
    #                             salle = esprit.fusionne_salles(salle_,salle)
    #                             break
    #             if salle not in salles_mod:
    #                 salles_mod.append(salle)
    #         for dec in Decalage(2,2):
    #             for couloir in esprit.couloirs:
    #                 if carre+dec in couloir.cases: #Cette case appartenait à un couloir. Ce n'est plus le cas car des murs ont été ouverts (portes, écrasement, etc.) et elle appartient désormais à une salle
    #                     couloirs_mod += esprit.scinde_couloir(couloir,carre+dec)
    #                     break
    #             for couloir in self.couloirs:
    #                 if carre+dec in couloir.cases:
    #                     couloirs_mod += self.scinde_couloir(couloir,carre+dec)
    #                     break
    #     for carre in carres_self:
    #         libre = True
    #         for salle in self.salles:
    #             if carre in salle.carres:
    #                 libre = False
    #                 if salle not in salles_mod:
    #                     salles_mod.append(salle)
    #                 break
    #         if libre:
    #             salle = Salle(carre)
    #             self.salles.add(salle)
    #             for salle_ in [*self.salles]:
    #                 if salle_ != salle:
    #                     for dir in DIRECTIONS:
    #                         if carre+dir in salle_.carres:
    #                             salle = self.fusionne_salles(salle_,salle)
    #                             break
    #             if salle not in salles_mod:
    #                 salles_mod.append(salle)
    #         for dec in Decalage(2,2):
    #             for couloir in self.couloirs:
    #                 if carre+dec in couloir.cases:
    #                     couloirs_mod += self.scinde_couloir(couloir,carre+dec)
    #                     break
    #             for couloir in esprit.couloirs:
    #                 if carre+dec in couloir.cases:
    #                     couloirs_mod += esprit.scinde_couloir(couloir,carre+dec)
    #                     break
    #     for salle in esprit.salles:
    #         self.salles.add(salle)
    #         for salle_ in [*self.salles]:
    #             if salle_ != salle:
    #                 for carre in salle.carres:
    #                     for dir in DIRECTIONS:
    #                         if carre+dir in salle_.carres:
    #                             salle = self.fusionne_salles(salle,salle_)
    #                             break
    #                     else:
    #                         continue
    #                     break
    #         if salle not in salles_mod:
    #             salles_mod.append(salle)
    #     self.entrees.update(esprit.entrees)
    #     for salle in salles_mod[::-1]:
    #         if salle in self.salles:
    #             salle.add_cases()
    #             salle.make_bord()
    #             for entree in salle.entrees:
    #                 if entree in self.entrees:
    #                     self.entrees[entree].remove(salle)
    #                     if self.entrees[entree] == []:
    #                         self.entrees.pop(entree)
    #             salle.entrees = {bord.emplacement for bord in salle.frontiere if self.vue.case_from_position(bord.emplacement).cibles[bord.direction][PASSE_ESCALIER]}
    #             salle.calcule_distances()
    #             for case in salle.cases:
    #                 if case in cases_self:
    #                     cases_self.remove(case)
    #                 if case in cases_esprit:
    #                     cases_esprit.remove(case)
    #             for entree in salle.entrees:
    #                 salle.cases.remove(entree)
    #         else:
    #             salles_mod.remove(salle)
    #     for case in cases_self | cases_esprit:
    #         if sum([int(not(not(case.cibles[dir][PASSE_ESCALIER]))) for dir in DIRECTIONS]) < 3:
    #             libre = True
    #             for couloir in self.couloirs | esprit.couloirs:
    #                 if case in couloir.cases:
    #                     break
    #             else:
    #                 couloir = Couloir(case.case.position)
    #                 self.couloirs.add(couloir)
    #                 for couloir_ in [*self.couloirs]:
    #                     if couloir_ != couloir:
    #                         for dir in DIRECTIONS:
    #                             if case.case.position+dir in couloir_.cases and case.cibles[dir][PASSE_ESCALIER] and self.vue.case_from_position(case.case.position+dir).cibles[dir.oppose()][PASSE_ESCALIER]:
    #                                 couloir = self.fusionne_couloirs(couloir_,couloir)
    #                                 break
    #                 for couloir_ in [*esprit.couloirs]:
    #                     if couloir_ != couloir:
    #                         for dir in DIRECTIONS:
    #                             if case.case.position+dir in couloir_.cases and case.cibles[dir][PASSE_ESCALIER] and self.vue.case_from_position(case.case.position+dir).cibles[dir.oppose()][PASSE_ESCALIER]:
    #                                 couloir = self.fusionne_couloirs(couloir_,couloir)
    #                                 self.couloirs.add(couloir)
    #                                 esprit.couloirs.remove(couloir)
    #                                 break
    #             if couloir not in couloirs_mod:
    #                 couloirs_mod.append(couloir)
    #     for couloir in esprit.couloirs:
    #         self.couloirs.add(couloir)
    #         for couloir_ in self.couloirs:
    #             if couloir_ != couloir:
    #                 for case in couloir.cases:
    #                     for dir in DIRECTIONS:
    #                         if case+dir in couloir_.cases and self.vue.case_from_position(case).cibles[dir][PASSE_ESCALIER] and self.vue.case_from_position(case+dir).cibles[dir.oppose()][PASSE_ESCALIER]:
    #                             couloir = self.fusionne_couloirs(couloir_,couloir)
    #                             break
    #                     else:
    #                         continue
    #                     break
    #         if couloir not in couloirs_mod:
    #             couloirs_mod.append(couloir)
    #     for couloir in couloirs_mod[::-1]:
    #         if couloir in self.couloirs:
    #             couloir.entrees = set()
    #             for dir in DIRECTIONS:
    #                 case1 = self.vue.case_from_position(couloir.cases[0]).cibles[dir][PASSE_ESCALIER]
    #                 if case1 and case1 not in couloir.cases: #Un mur vers l'extérieur !
    #                     couloir.entrees.add(case1)
    #                 case2 = self.vue.case_from_position(couloir.cases[-1]).cibles[dir][PASSE_ESCALIER]
    #                 if len(couloir.cases)>1 and case2 and case2 not in couloir.cases: #Un mur vers l'extérieur !
    #                     couloir.entrees.add(case2)
    #         else:
    #             couloirs_mod.remove(couloir)
    #     for espace in salles_mod + couloirs_mod:
    #         for entree in espace.entrees:
    #             if espace not in self.entrees.get(entree,set()) and espace in self.salles|self.couloirs:
    #                 self.entrees[entree] = self.entrees.get(entree,set())|{espace}

    # def fusionne_salles(self,salle1:Salle,salle2:Salle): #salle1 est probablement plus grosse que salle2
    #     salle1.carres = salle1.carres|salle2.carres # Et c'est tout ?
    #     self.remove_salle(salle2)
    #     return salle1

    # def fusionne_couloirs(self,couloir1:Couloir,couloir2:Couloir): #couloir1 est probablement plus gros que couloir2
    #     if all([case in couloir1.cases for case in couloir2.cases]):
    #         self.remove_couloir(couloir2)
    #         return couloir1
    #     if all([case in couloir2.cases for case in couloir1.cases]):
    #         self.remove_couloir(couloir1)
    #         return couloir2
    #     for dir in DIRECTIONS:
    #         if self.vue.case_from_position(couloir1.cases[0]).cibles[dir][PASSE_ESCALIER] == couloir2.cases[0] and self.vue.case_from_position(couloir2.cases[0]).cibles[dir.oppose()][PASSE_ESCALIER] == couloir1.cases[0]:
    #             couloir1.cases = list(reversed(couloir1.cases)) + couloir2.cases # Et c'est tout ?
    #             self.remove_couloir(couloir2)
    #             return couloir1
    #         if self.vue.case_from_position(couloir1.cases[-1]).cibles[dir][PASSE_ESCALIER] == couloir2.cases[0] and self.vue.case_from_position(couloir2.cases[0]).cibles[dir.oppose()][PASSE_ESCALIER] == couloir1.cases[-1]:
    #             couloir1.cases = couloir1.cases + couloir2.cases # Et c'est tout ?
    #             self.remove_couloir(couloir2)
    #             return couloir1
    #         if self.vue.case_from_position(couloir1.cases[0]).cibles[dir][PASSE_ESCALIER] == couloir2.cases[-1] and self.vue.case_from_position(couloir2.cases[-1]).cibles[dir.oppose()][PASSE_ESCALIER] == couloir1.cases[0]:
    #             couloir1.cases = couloir2.cases + couloir1.cases # Et c'est tout ?
    #             self.remove_couloir(couloir2)
    #             return couloir1
    #         if self.vue.case_from_position(couloir1.cases[-1]).cibles[dir][PASSE_ESCALIER] == couloir2.cases[-1] and self.vue.case_from_position(couloir2.cases[-1]).cibles[dir.oppose()][PASSE_ESCALIER] == couloir1.cases[-1]:
    #             couloir1.cases = couloir1.cases + list(reversed(couloir2.cases)) # Et c'est tout ?
    #             self.remove_couloir(couloir2)
    #             return couloir1
    #     print(couloir1.cases)
    #     print(couloir2.cases)
    #     raise RuntimeError("Oops! How did I get there?")

    # def fusionne_zones(self,zone1:Zone_inconnue,zone2:Zone_inconnue):
    #     zone1.fusionne(zone2)
    #     self.remove_zone(zone2)
    #     return zone1

    # def scinde_salle(self,salle:Salle,carre:crt.Position):
    #     salle.carres.remove(carre)
    #     voisins = [carre+dir for dir in DIRECTIONS if carre+dir in salle.carres]
    #     salles:Set[Salle] = set()
    #     while voisins:
    #         depart = voisins.pop(0)
    #         queue = [depart]
    #         salle.carres.remove(depart)
    #         new_salle = Salle(depart)
    #         while len(queue):
    #             position = queue.pop(0)
    #             for dir in DIRECTIONS:
    #                 voisin = position+dir
    #                 if voisin in salle.carres:
    #                     salle.carres.remove(voisin)
    #                     queue.append(voisin)
    #                     new_salle.carres.add(voisin)
    #                     if voisin in voisins:
    #                         voisins.remove(voisin)
    #         salles.add(new_salle)
    #     self.remove_salle(salle)
    #     self.salles |= salles
    #     return salles

    # def scinde_couloir(self,couloir:Couloir,case:crt.Position):
    #     i = couloir.cases.index(case)
    #     cases1,cases2 = couloir.cases[:i],couloir.cases[i+1:]
    #     couloirs = set()
    #     if cases1:
    #         couloir1 = Couloir()
    #         couloir1.cases = cases1
    #         self.couloirs.add(couloir1)
    #         couloirs.add(couloir1)
    #     if cases2:
    #         couloir2 = Couloir()
    #         couloir2.cases = cases2
    #         self.couloirs.add(couloir2)
    #         couloirs.add(couloir2)
    #     self.remove_couloir(couloir)
    #     return couloirs

    # def scinde_zone(self,zone:Zone_inconnue,case:crt.Position) -> Set[Zone_inconnue]:
    #     zone.cases.remove(case)
    #     voisins = {case+dir for dir in DIRECTIONS if case+dir in zone.cases}
    #     zones = set()
    #     while voisins:
    #         depart = voisins.pop()
    #         queue = [depart]
    #         zone.cases.remove(depart)
    #         new_zone = Zone_inconnue(depart,zone)
    #         while len(queue):
    #             position = queue.pop(0)
    #             for dir in DIRECTIONS:
    #                 voisin = position+dir
    #                 if voisin in zone.cases and self.vue.case_from_position(position).cibles[dir][PASSE_ESCALIER]:
    #                     zone.cases.remove(voisin)
    #                     queue.append(voisin)
    #                     new_zone.cases.add(voisin)
    #                     if voisin in voisins:
    #                         voisins.remove(voisin)
    #         zones.add(new_zone)
    #     self.remove_zone(zone)
    #     self.zones_inconnues |= zones
    #     return zones

    # def remove_salle(self,salle:Salle):
    #     self.salles.remove(salle)
    #     for entree in salle.entrees:
    #         if entree in self.entrees and salle in self.entrees[entree]:
    #             self.entrees[entree].remove(salle)
    #             if self.entrees[entree] == []: #Si la salle était la seule à avoir cette entrée
    #                 self.entrees.pop(entree) #On la supprime

    # def remove_couloir(self,couloir:Couloir):
    #     self.couloirs.remove(couloir)
    #     for entree in couloir.entrees:
    #         if entree in self.entrees and couloir in self.entrees[entree]:
    #             self.entrees[entree].remove(couloir)
    #             if self.entrees[entree] == []: #Si le couloir était le seul à avoir cette entrée
    #                 self.entrees.pop(entree) #On le supprime

    # def remove_zone(self,zone:Zone_inconnue):
    #     self.zones_inconnues.remove(zone)
    #     # print(len(self.zones_inconnues))
    #     for entree in zone.entrees:
    #         if entree in self.entrees and zone in self.entrees[entree]:
    #             self.entrees[entree].remove(zone)
    #             if self.entrees[entree] == []: #Si la zone était la seule à avoir cette entrée
    #                 self.entrees.pop(entree) #On la supprime
    #         # /!\ Regarder avec attention ce qui se passe pour les entrées

    def get_offenses(self):
        for corp in self.corps: #On vérifie si quelqu'un nous a offensé
            offenses,etat = corp.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                self.antagonise_attaquant(offense)
                self.antagonise_supports(offense)
        
    def antagonise_attaquant(self,offense:Tuple[Agissant,float,float]):
        ID_offenseur = offense[0]
        gravite = offense[1]
        degats = offense[2]
        if ID_offenseur in self.ennemis:
            self.ennemis[ID_offenseur]["importance"] += gravite
            if self.ennemis[ID_offenseur]["dangerosite"] < degats:
                self.ennemis[ID_offenseur]["dangerosite"] = degats
        else:
            self.ennemis[ID_offenseur] = {"importance":gravite,"dangerosite":degats}

    def antagonise_supports(self,offense:Tuple[Agissant,float,float]):
        pass

    def get_pos_vues(self):
        positions = []
        for corp in self.corps:
            if self.corps[corp] != "incapacite":
                positions.append(corp.position)
        return positions

    def trouve_strateges(self):
        # Plus exactement lié aux stratèges, renommer à l'occasion
        self.resolution = 0
        self.oubli = 0
        for corp in self.corps:
            self.resolution = max(self.resolution,corp.resolution)
            self.oubli = max(self.oubli,corp.oubli)

    # def unset_skip(self):
    #     for espace in self.salles|self.couloirs:
    #         espace.skip = False

    # def set_skip(self,sources:Set[Position],recepteurs:Set[Position]):
    #     for espace in self.salles|self.couloirs:
    #         espace.skip = True
    #         for source in sources:
    #             if source in espace.get_cases():
    #                 espace.skip = False
    #         for recepteur in recepteurs:
    #             if recepteur in espace.get_all_cases():
    #                 espace.skip = False

    # def calcule_trajets(self):
    #     # On détermine la dangerosité de chaque case en fonction des dégats qui vont y avoir lieu
    #     pos_corps:Set[Position] = {corp.get_position() for corp in self.corps if self.corps[corp] != "incapacite"}
    #     coef=7 #/!\ Expérimenter avec ce coef à l'occasion
    #     for case in self.vue:
    #         for effet in case.effets:
    #             dangerosite = coef*effet[2]/(effet[1]+coef)
    #             case["dangerosite",0] -= dangerosite
    #     add_constantes_temps("attaques délayées")

    #     # On modifie légèrement pour pouvoir sortir des zones concernées
    #     coef_croissant = 1.1
    #     # On commence par trouver les seuils, vers lesquels on va vouloir aller
    #     self.unset_skip()
    #     seuils = self.trouve_seuils(self.get_pos_vues()) # On part des différents endroit d'où l'on voit, qui devraient théoriquement nous donner accès à toute notre vision
    #     self.set_skip(seuils,pos_corps)
    #     self.propage(seuils,coef_croissant,"dangerosite") # On propage de façon croissante à partir des seuils (vers l'intérieur)
    #     add_constantes_temps("propagation des seuils")

    #     # On rajoute les ennemis
    #     coef_importance = 0.9
    #     coef_dangerosite = 0.9
    #     dangerosites = seuils
    #     importances:Set[Position] = set()
    #     for ennemi in self.ennemis:
    #         if ennemi.etat == "vivant":
    #             position = ennemi.get_position()
    #             if position.lab in self.vue:
    #                 importance = self.ennemis[ennemi]["importance"]
    #                 dangerosite = -self.ennemis[ennemi]["dangerosite"]
    #                 if importance > self.vue.case_from_position(position)["importance",0]:
    #                     self.vue.case_from_position(position)["importance",0]=importance
    #                     importances.add(position)
    #                 if dangerosite < self.vue.case_from_position(position)["dangerosite",0]:
    #                     self.vue.case_from_position(position)["dangerosite",0]=dangerosite
    #                 if not position in dangerosites: # On peut avoir des doublons (ennemis sur les seuils par exemple)
    #                     dangerosites.add(position)
    #     add_constantes_temps("importance et dangerosité des ennemis")
    #     # On propage l'importance de façon décroissante à partir des ennemis
    #     self.set_skip(importances,pos_corps)
    #     self.propage(importances,coef_importance,"importance")
    #     add_constantes_temps("propagation de l'importance des ennemis")
    #     # On propage la dangerosité de façon décroissante à partir des ennemis et des seuils
    #     self.set_skip(dangerosites,pos_corps)
    #     self.propage(dangerosites,coef_dangerosite,"dangerosite",comparateur=-1)
    #     add_constantes_temps("propagation de la dangerosité des ennemis")

    #     # /!\ Prendre aussi en compte les alliés, et les cases inconnues (mais on va déjà tester ça)

    # def resoud(self,position:crt.Position,valeur:int,trajet:str):
    #     """'Résoud' un labyrinthe à partir d'une case donnée."""

    #     if position in self.vue:

    #         self.vue.case_from_position(position)[trajet,0] = valeur
    #         self.propage({position},self.dispersion_spatiale,trajet,stop_on_obstacles=True,clear=True)

    # def propage(self,positions:Set[Position],coef:float,trajet:str,stop_on_obstacles=False,comparateur=1,clear=False):
    #     """'Résoud' un labyrinthe à partir de plusieurs points"""

    #     i = 0
            
    #     # On commence par 'nettoyer' les cases
    #     if clear:
    #         for case in self.vue:
    #             if case.case.position not in positions:
    #                 case.trajets[trajet] = []

    #     while positions:

    #         queue = [{"position":position,"valeur":self.vue.case_from_position(position)[trajet,i]} for position in positions]

    #         obstacles:Set[Position] = set()

    #         # On trie par valeur (décroissant par défaut)
    #         queue.sort(key=lambda x:x["valeur"],reverse=comparateur==1)

    #         while len(queue) :
    #             position = queue.pop(0)

    #             pos_explorables, pos_obstacle = self.positions_utilisables(position["position"])

    #             for pos in pos_explorables:
    #                 valeur = position["valeur"]*coef**pos_explorables[pos]
    #                 if valeur*comparateur > self.vue.case_from_position(pos)[trajet,i]*comparateur:
    #                     self.vue.case_from_position(pos)[trajet,i] = valeur

    #                     #on ajoute les directions explorables (en gardant l'ordre)
    #                     for i in range(-1,len(queue)-1,-1): # On parcourt la liste à l'envers parce qu'on va probablement insérer vers la fin
    #                         if queue[i]["valeur"]*comparateur >= valeur*comparateur:
    #                             queue.insert(i+1,{"position":pos,"valeur":valeur})
    #                             break
    #                     else:
    #                         queue.insert(0,{"position":pos,"valeur":valeur})

    #             for pos in pos_obstacle:
    #                 valeur = position["valeur"]*coef**pos_obstacle[pos]
    #                 if all([valeur*comparateur > val*comparateur for val in self.vue.case_from_position(pos).trajets[trajet]]):
    #                     self.vue.case_from_position(pos)[trajet,i+1] = valeur
    #                     obstacles.add(pos)

    #         if stop_on_obstacles:
    #             break
    #         else:
    #             positions = obstacles
    #             i += 1

    # def trouve_seuils(self,positions:List[Position],trajet="dangerosite") -> Set[Position]:
    #     """Fonction qui trouve les 'seuils', c'est à  dire les cases qui ont une valeur plus grande que leurs voisines"""

    #     for case in self.vue:
    #         case.visitee = False

    #     seuils:Set[Position] = set()

    #     #la queue est une liste de positions
    #     queue = [position for position in positions]

    #     while len(queue) :

    #         position = queue.pop(0)            

    #         #trouver les positions explorables

    #         pos_utilisables, pos_obstacles = self.positions_utilisables(position)

    #         pos_explorables = pos_utilisables | pos_obstacles

    #         for pos in pos_explorables:
    #             if self.vue.case_from_position(position)[trajet,0] > self.vue.case_from_position(pos)[trajet,0]:
    #                 seuils.add(position)
    #             elif self.vue.case_from_position(position)[trajet,0] < self.vue.case_from_position(pos)[trajet,0]:
    #                 seuils.add(pos)
    #             if not self.vue.case_from_position(pos).visitee:
    #                 #on marque la case comme visitée
    #                 self.vue.case_from_position(pos).visitee = True
                        
    #                 #on ajoute toutes les directions explorables
    #                 queue.append(pos)
    #     return seuils

    # def print_vue(self):
    #     for etage in self.vue:
    #         matrice = self.vue.case_from_position(etage)
    #         print("Vue de l'esprit :")
    #         print(self.nom)
    #         for i in range(len(matrice)):
    #             haut = ""
    #             centre = ""
    #             bas = ""
    #             for j in range(len(matrice[0])):
    #                 case:Representation_case = matrice[i][j]
    #                 if case.clarte == 0:
    #                     haut += " ~~~ "
    #                     centre += ": ? :"
    #                     bas += " ~~~ "
    #                 else:
    #                     haut+= " "
    #                     if case.cibles[0]:
    #                         haut += "   "
    #                     else:
    #                         haut += "---"
    #                     haut += " "
    #                     if case.cibles[3]:
    #                         centre += " "
    #                     else:
    #                         centre += "|"
    #                     if case.cibles > 0:
    #                         centre += "x"
    #                     else:
    #                         centre += " "
    #                     if case.entitees:
    #                         occ = " "
    #                         for occupant in case.entitees:
    #                             if occupant in self.corps:
    #                                 occ = "O"
    #                             elif occupant in self.ennemis:
    #                                 occ = "X"
    #                         centre += occ
    #                     else:
    #                         centre += " "
    #                     if case[3][1] > 0:
    #                         centre += "x"
    #                     else:
    #                         centre += " "
    #                     if case.cibles[1]:
    #                         centre += " "
    #                     else:
    #                         centre += "|"
    #                     bas += " "
    #                     if case.cibles[2]:
    #                         bas += "   "
    #                     else:
    #                         bas += "---"
    #                     bas += " "
    #             print(haut)
    #             print(centre)
    #             print(bas)

    # def print_zones(self):
    #     print(f"Vue de l'esprit {self.nom} :")
    #     zones_visibles = self.salles + self.couloirs
    #     zones_inconnues = self.zones_inconnues
    #     for etage in self.vue:
    #         vue = self.vue.case_from_position(etage)
    #         print(f"Zones de l'étage {etage} :")
    #         for zones in [zones_visibles,zones_inconnues]:
    #             for j in range(vue.decalage.y):
    #                 haut = ""
    #                 milieu = ""
    #                 bas = ""
    #                 for i in range(vue.decalage.x):
    #                     case = vue[i,j]
    #                     # Le haut
    #                     haut+= " "
    #                     if case.cibles[0][PASSE_ESCALIER]:
    #                         haut += "   "
    #                     else:
    #                         haut += "---"
    #                     haut += " "
    #                     # La gauche
    #                     if case.cibles[3][PASSE_ESCALIER]:
    #                         gauche = " "
    #                     else:
    #                         gauche = "|"
    #                     # La droite
    #                     if case.cibles[1][PASSE_ESCALIER]:
    #                         droite = " "
    #                     else:
    #                         droite = "|"
    #                     # Le bas
    #                     bas += " "
    #                     if case.cibles[2][PASSE_ESCALIER]:
    #                         bas += "   "
    #                     else:
    #                         bas += "---"
    #                     bas += " "
    #                     # Le centre
    #                     for i in range(len(zones)):
    #                         if case[0] in zones[i].cases or case[0] in zones[i].entrees:
    #                             centre = f"{i:^{3}}"
    #                             break
    #                     else:
    #                         if case.clarte > 0:
    #                             centre = "   "
    #                         else:
    #                             centre = " ? "
    #                     milieu += gauche + centre + droite
    #                 print(haut)
    #                 print(milieu)
    #                 print(bas)
    #             print("")

    # def positions_utilisables(self,position:crt.Position)->Tuple[Dict[Position,int],Dict[Position,int]]:
    #     pos_utilisables:Dict[Position,int]={}
    #     pos_obstacles:Dict[Position,int]={}

    #     case = self.vue.case_from_position(position)
    #     case:Representation_case
    #     if position in self.entrees:
    #         for direction in DIRECTIONS:
    #             acces = case.cibles[direction][PASSE_ESCALIER]
    #             if acces: # Si la case est accessible
    #                 if not any(acces in espace.cases and espace.skip for espace in self.entrees[position]): # Si la case n'est pas skippée
    #                     if acces in self.vue: # Si la case est visible
    #                         if case.agissant: # Si la case est occupée
    #                             pos_obstacles[acces]=1
    #                         else:
    #                             pos_utilisables[acces]=1
    #         for espace in self.entrees[position]:
    #             if espace.skip: # Si l'espace est skippé
    #                 for entree in espace.entrees: # On ajoute toutes les entrées de l'espace
    #                     if entree in self.vue: # Si elles sont visibles
    #                         pos_utilisables[entree] = espace.dist(position,entree)
    #     else:
    #         for direction in DIRECTIONS:
    #             acces = case.cibles[direction][PASSE_ESCALIER]
    #             if acces: # Si la case est accessible
    #                 if acces in self.vue: # Si la case est visible
    #                     if case.agissant:
    #                         pos_obstacles[acces]=1
    #                     else:
    #                         pos_utilisables[acces]=1

    #     return pos_utilisables, pos_obstacles

    def merge(self,esprit:Esprit):
        if esprit != self:
            self.merge_corps(esprit)
            self.merge_enemies(esprit)
            self.merge_vision(esprit)

    def merge_corps(self,esprit:Self):
        for corps in esprit.corps:
            if corps not in self.corps:
                if corps in self.ennemis:
                    self.ennemis.pop(corps)
                self.corps[corps] = esprit.corps[corps]
                corps.rejoint(self)

    def merge_enemies(self,esprit:Self):
        for ennemi in esprit.ennemis:
            if ennemi not in self.corps:
                if ennemi not in self.ennemis:
                    self.ennemis[ennemi] = esprit.ennemis[ennemi]
                else:
                    for cle in ["importance","dangerosite"]:
                        self.ennemis[ennemi][cle] = max(esprit.ennemis[ennemi][cle],self.ennemis[ennemi][cle])

    def merge_vision(self,esprit:Self):
        cases_self:Set[Representation_case] = set()
        cases_other:Set[Representation_case] = set()
        for etage in esprit.vue.keys():
            if etage not in self.vue:
                self.vue[etage]= esprit.vue[etage]
            else:
                selfs, others = self.merge_vue(esprit.vue[etage])
                cases_self |= selfs
                cases_other |= others                
        self.merge_representation(esprit,cases_self,cases_other)
        self.merge_zones(esprit,cases_self,cases_other)

    def antagonise(self,esprit:Esprit):
        for corp in esprit.get_corps():
            if not corp in self.ennemis:
                self.ennemis[corp] = {"importance":0.1,"dangerosite":0}

    def decide(self):
        for corp in self.corps:
            if self.corps[corp] in ["attaque","fuite","soin","soutien"]:
                self.deplace(corp)
            elif self.corps[corp] == "PNJ" and isinstance(corp,PNJ):
                self.deplace_pnj(corp)

    def fuite_utile(self,fuyard:Agissant): #TODO inclure l'accessibilité
        for corp in self.corps:
            if corp != fuyard and self.corps[corp] not in ["fuite","incapacite","mort"]:
                return True
        return False

    def deplace(self,corp:Agissant):
        position = corp.position
        case = self.vision.get_case(position)
        repoussante = case.repoussante
        cases:List[Dict[str,Position|Direction|List[float]]] = [{"position":position,"direction":None}|case.trajets]
        dirs = []
        importance = 0
        fuite = corp.veut_fuir(case["dangerosite",0])
        attaque = corp.veut_attaquer(case["dangerosite",0])
        res = "attente"
        for i in DIRECTIONS: #On commence par se renseigner sur les possibilités :
            mur:crt.Position|Literal[False] = case.cibles[i][self.resolution]
            if mur:
                if mur in position and corp.vue.case_from_position(mur).clarte>0:
                    case_pot = self.vue.case_from_position(mur)
                    if case_pot.agissant:
                        if case_pot.agissant in self.ennemis: #Et c'est un ennemi !
                            if corp.peut_voir(i) and (attaque or (fuite and not self.fuite_utile(corp))) : #On veut attaquer lorsqu'on croise un ennemi au corps à corps (et on a assez de mana pour, si on utilise la magie)
                                if self.ennemis[case_pot.agissant]["importance"] > importance:
                                    importance = self.ennemis[case_pot.agissant]["importance"]
                                    corp.attaque(i)
                                    res = "attaque"
                            elif fuite and self.fuite_utile(corp): #On veut fuire lorsqu'on croise un ennemi au corps à corps
                                res = "fuite"
                    elif not case_pot.decors: # Ni agissant, ni décor
                        cases.append({"position":mur,"direction":i}|case_pot.trajets)
                        dirs.append(i)
        if res == "attente": #Quelques comportements possibles :
            comportement = corp.comporte_distance(case["dangerosite",0])
            if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                res = "deplacement"
            elif comportement == 1 or (comportement > 1 and not self.fuite_utile(corp)): #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                res = corp.agit_en_vue("deplacement")
                if repoussante:
                    res = "deplacement"
            elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                res = corp.agit_en_vue("fuite")
                if repoussante:
                    res = "fuite"
            elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                res = "fuite"
        if res in ["deplacement","fuite"] and (corp.action is None or corp.action.latence <= 0):
            if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                res = "bloqué"
                importance = 0
                for i in DIRECTIONS:
                    mur:crt.Position|Literal[False] = case.cibles[i][self.resolution]
                    if mur:
                        if mur.lab in self.vue:
                            case_pot = self.vue.case_from_position(mur)
                            if case_pot.agissant:
                                if corp.peut_voir(i) and case_pot.agissant in self.ennemis: #Et c'est un ennemi !
                                    if self.ennemis[case_pot.agissant]["importance"] > importance:
                                        importance = self.ennemis[case_pot.agissant]["importance"]
                                        corp.attaque(i)
                                        res = "attaque"
            elif (not any(case.trajets["dangerosite"])) and (not any(case.trajets["importance"])): #Il n'y a pas une seule dangerosité ou importance dans la case
                res = "paix"
                if not isinstance(corp,Sentinelle) or isinstance(corp,Humain) or repoussante:
                    res = "exploration"
                    if len(dirs)>1: #On peut se permettre de choisir
                        if corp.dir_regard is not None: #L'agissant regarde quelque part
                            dir_back = corp.dir_regard.oppose
                            if dir_back in dirs: #On ne veut pas y retourner
                                dirs.remove(dir_back)
                    corp.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                    # if corp.ID == 4: # /!\ Ne pas nettoyer, c'est très utile par moment
                    #     constantes_deplacements.append([self.controleur.nb_tours,"cherche",corp.dir_regard,cases])
            else:
                if repoussante: #On ne veut pas rester en place
                    cases.pop(0)
                if res == "deplacement":
                    new_cases = sorted(cases,key=operator.itemgetter("importance","dangerosite")) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    res = "approche"
                    if new_cases[-1]["direction"]: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                        direction = new_cases[-1]["direction"]
                        assert isinstance(direction,crt.Direction)
                        corp.va(direction)
                        # if corp.ID == 4:
                        #     constantes_deplacements.append([self.controleur.nb_tours,"deplacement",corp.dir_regard,new_cases])
                    else:
                        res = corp.agit_en_vue()
                elif res == "fuite":
                    new_cases = sorted(cases,key=operator.itemgetter("dangerosite","importance")) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                    if new_cases[-1]["direction"]: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                        direction = new_cases[-1]["direction"]
                        assert isinstance(direction,crt.Direction)
                        corp.va(direction)
                        # if corp.ID == 4:
                        #     constantes_deplacements.append([self.controleur.nb_tours,"fuite",corp.dir_regard,new_cases])
                    else:
                        res = corp.agit_en_vue()
        corp.set_statut(res)

    def deplace_pnj(self,pnj:PNJ):
        pnj.statut_pnj = "proximite"
        cible = pnj.position
        if pnj.mouvement == 0: #0 pour aller vers, 1 pour chercher et 2 pour aller au contact
            if isinstance(pnj.cible_deplacement,Agissant):
                if pnj.cible_deplacement.etat == "vivant":
                    cible = pnj.cible_deplacement.get_position()
                    portee = 7
                else:
                    cible = pnj.get_position()
                    portee = 1 #C'est juste pour qu'il puisse aller où il veut
            elif isinstance(pnj.cible_deplacement,Position):
                cible = pnj.cible_deplacement
                portee = 5
            else:
                raise ValueError("Cible de déplacement inconnue")
        elif pnj.mouvement == 1:
            cible = pnj.get_position()
            portee = 1 #C'est juste pour qu'il puisse aller où il veut
            pnj.statut_pnj = "exploration"
        elif pnj.mouvement == 2:
            if isinstance(pnj.cible_deplacement,Agissant):
                if pnj.cible_deplacement.etat == "vivant":
                    cible = pnj.cible_deplacement.get_position()
                    portee = 0
                else:
                    cible = pnj.get_position()
                    portee = 1 #C'est juste pour qu'il puisse aller où il veut
            elif isinstance(pnj.cible_deplacement,Position):
                cible = pnj.cible_deplacement
                portee = 0
            else:
                raise ValueError("Cible de déplacement inconnue")
        elif pnj.mouvement == 3:
            pnj.statut_pnj = "attente"
            return
        else:
            raise ValueError("Mouvement inconnu")
        pos_cibles = self.controleur.get_pos_touches(cible,portee)
        if pnj.position in pos_cibles: #Tout va bien, on y est ! On peut combattre, par exemple.
            Esprit.deplace(self,pnj)
        else:
            res = "recherche"
            position = pnj.get_position()
            self.set_skip({cible},{position})
            self.resoud(cible,1,"recherche")
            case:Representation_case = self.vue.case_from_position(position)
            repoussante = case.repoussante
            cases = [{"position":position,"direction":None}|case.trajets]
            dirs = []
            importance = 0
            fuite = pnj.veut_fuir(case["dangerosite",0])
            attaque = pnj.veut_attaquer(case["dangerosite",0])
            pnj.statut_pnj = "en chemin"
            if case.trajets["recherche"] == 0:
                pnj.statut_pnj = "perdu"
                if pnj == 4: # /!\ Remplacer par une propriété du PNJ
                    pnj.statut_pnj = "paume"
            for i in DIRECTIONS:
                mur:crt.Position|Literal[False] = case.cibles[i][self.resolution]
                if mur:
                    if mur in position and pnj.vue.case_from_position(mur).clarte>0:
                        case_pot = self.vue.case_from_position(mur)
                        if case_pot.agissant:
                            if case_pot.agissant in self.ennemis: #Et c'est un ennemi !
                                if pnj.peut_voir(i) and (attaque or (fuite and not self.fuite_utile(pnj))) : #On veut attaquer lorsqu'on croise un ennemi au corps à corps (et on a assez de mana pour, si on utilise la magie)
                                    if self.ennemis[case_pot.agissant]["importance"] > importance:
                                        importance = self.ennemis[case_pot.agissant]["importance"]
                                        pnj.attaque(i)
                                        res = "attaque"
                                elif fuite and self.fuite_utile(pnj): #On veut fuire lorsqu'on croise un ennemi au corps à corps
                                    res = "fuite"
                                elif pnj.mouvement == 2 and (case_pot.agissant == pnj.cible_deplacement or case_pot.agissant.ID == pnj.cible_deplacement):
                                    if isinstance(case_pot.agissant,PJ) and case_pot.agissant is self.controleur.joueur and pnj.peut_voir(i): #Le PNJ peut enfin parler au joueur
                                        case_pot.agissant.interlocuteur = pnj
                                        self.controleur.set_phase(DIALOGUE)
                                        pnj.start_dialogue()
                                        pnj.regarde(i)
                                        case_pot.agissant.regarde(i.oppose())
                                        pnj.mouvement = 0
                                    elif isinstance(case_pot.agissant, PNJ) and isinstance(pnj, PJ) and pnj is self.controleur.joueur and pnj.peut_voir(i): #Le joueur peut enfin parler au PNJ
                                        pnj.interlocuteur = case_pot.agissant
                                        self.controleur.set_phase(DIALOGUE)
                                        pnj.interlocuteur.start_dialogue()
                                        pnj.regarde(i)
                                        pnj.interlocuteur.regarde(i.oppose())
                                        pnj.mouvement = 0
                        elif not case_pot.decors:
                            cases.append({"position":mur,"direction":i}|case_pot.trajets)
                            dirs.append(i)
            if res == "recherche": #On n'a pas d'ennemi à portée directe (ou on ne souhaite pas attaquer ni fuir)
                comportement = pnj.comporte_distance(case["dangerosite",0])
                if comportement == 0 : #Foncer tête baissée ! Pour les combattants au corps à corps
                    res = "deplacement"
                elif comportement == 1: #Tenter une action, puis approcher. Pour les effets à distance qui ont besoin de ne pas être trop loin.
                    res = pnj.agit_en_vue("deplacement")
                    if repoussante:
                        res = "deplacement"
                elif comportement == 2: #Tenter une action, puis fuir. Pour les effets à distance qui peuvent se permettre d'être loin.
                    res = pnj.agit_en_vue("fuite")
                    if repoussante:
                        res = "fuite"
                elif comportement == 3 : #La fuite ! Quand les pvs sont bas
                    res = "fuite"
                if len(cases) == 1: #Pas de cases libres à proximité, on va essayer d'attaquer pour s'en sortir
                    res = "bloqué"
                    importance = 0
                    for dir in crt.Direction:
                        mur:crt.Position|Literal[False] = case.cibles[i][self.resolution]
                        if mur:
                            if mur.lab in self.vue:
                                case_pot = self.vue.case_from_position(mur)
                                if case_pot.agissant:
                                    if pnj.peut_voir(i) and case_pot.agissant in self.ennemis: #Et c'est un ennemi !
                                        if self.ennemis[case_pot.agissant]["importance"] > importance:
                                            importance = self.ennemis[case_pot.agissant]["importance"]
                                            pnj.attaque(i)
                                            res = "attaque"
                elif  (not any(case.trajets["dangerosite"])) and (not any(case.trajets["importance"])) and pnj.statut_pnj == "perdu":
                    res = "paix"
                    if not isinstance(pnj,Sentinelle) or repoussante:
                        res = "exploration"
                        if len(dirs)>1: #On peut se permettre de choisir
                            if pnj.dir_regard is not None: #L'agissant regarde quelque part
                                dir_back = pnj.dir_regard.oppose
                                if dir_back in dirs: #On ne veut pas y retourner
                                    dirs.remove(dir_back)
                        pnj.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                elif pnj.statut_pnj == "paume":
                    res = "paix"
                    if repoussante:
                        res = "exploration"
                        if len(dirs)>1: #On peut se permettre de choisir
                            if pnj.dir_regard is not None: #L'agissant regarde quelque part
                                dir_back = pnj.dir_regard.oppose
                                if dir_back in dirs: #On ne veut pas y retourner
                                    dirs.remove(dir_back)
                        pnj.va(dirs[random.randint(0,len(dirs)-1)]) #/!\ Ne pas retourner sur ses pas, c'est bien ! Aller vers les endroits inconnus, ce serait mieux. /!\
                else:
                    if repoussante:
                        cases.pop(0)
                    if res == "deplacement":
                        new_cases = sorted(cases,key=operator.itemgetter("importance","dangerosite"))
                        res = "approche"
                        if new_cases[-1]["direction"]: #La dernière case (i.e. les valeurs les plus élevées) n'est pas celle où l'on est
                            direction = new_cases[-1]["direction"]
                            assert isinstance(direction,crt.Direction)
                            pnj.va(direction)
                            # if pnj.ID == 4:
                            #     constantes_deplacements.append([self.controleur.nb_tours,"deplacement loin",pnj.dir_regard,new_cases])
                        else:
                            res = pnj.agit_en_vue()
                    elif res == "fuite":
                        new_cases = sorted(cases,key=operator.itemgetter("dangerosite","importance")) #2 pour le chemin d'accès indirect, 3 pour le chemin d'accès direct
                        if new_cases[-1]["direction"]: #La première case (i.e. les valeurs les moins élevées) n'est pas celle où l'on est
                            direction = new_cases[-1]["direction"]
                            assert isinstance(direction,crt.Direction)
                            pnj.va(direction)
                            # if pnj.ID == 4:
                            #     constantes_deplacements.append([self.controleur.nb_tours,"fuite loin",pnj.dir_regard,new_cases])
                        else:
                            res = pnj.agit_en_vue()
            pnj.set_statut(res)

    def oublie(self):
        anciennes_cases = []
        for case in self.vue:
            if case.oublie(self.oubli):
                anciennes_cases.append(case.case.position)

        self.downdate_zones(anciennes_cases)
        self.downdate_representation(anciennes_cases)

    #Découvront le déroulé d'un tour avec esprit-sensei :
    def debut_tour(self):
        #On va faire plein de choses pendant ce tour (est-ce vraiment nécessaire de prendre des décisions si aucun des corps ne va jouer à ce tour ?
        self.get_offenses() #On s'insurge à grands cris (s'il y a lieu)
        self.trouve_strateges()


        # La suite est très lente, comment faire pour l'accélérer ?
        self.refait_vue() #On prend connaissance de son environnement
        #Il faudra éventuellement définir une stratégie
        self.calcule_trajets() #On dresse les plans de bataille (s'il y a lieu)

    def pseudo_debut_tour(self):
        pass

    #Tout le monde agit, nos bon-à-rien d'agissants se font massacrer à cause de leurs capacités médiocres ou remportent la victoire grâce à nos ordres brillants

    def fin_tour(self):
        #Le tour est fini, on réfléchira pendant le prochain. Comment ça, c'est mauvais pour la mémoire ?
        self.oublie()

class Mindless(Esprit):
    def __init__(self):
        pass

NOBODY = Mindless()

# Imports utilisés dans le code
# from ..Esprit.Representation_spatiale import Salle, Couloir, Zone_inconnue
from .Vision.Vision import Vision
from ..Entitee.Agissant.Agissant import Agissant
from ..Entitee.Agissant.PNJ.PNJs import PNJ, PJ
from ..Entitee.Agissant.Role.Sentinelle import Sentinelle
import random
import operator