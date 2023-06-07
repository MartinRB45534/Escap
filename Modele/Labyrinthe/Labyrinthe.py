from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Optional, Set
import Carte as crt

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from .Vue import Representation_case
    from .Pattern import Pattern
    from .Case import Case
    from .Mur import Mur
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Entitee.Entitee import Mobile

class Labyrinthe(crt.Labyrinthe):
    def __init__(self):
        super().__init__()
        self.position_case: dict[crt.Position,Case] = {}
        self.add_case(CASE_ABSENTE)

    def __contains__(self, item):
        if isinstance(item,crt.Position):
            return item in self.nodes and item is not crt.POSITION_ABSENTE
        return super().__contains__(item)

    def add_case(self, case:Case, **attr):
        self.add_node(case.position, case=case, **attr)
        self.position_case[case.position] = case
        for direction in crt.Direction:
            self.add_mur(case.position, case.position+direction, direction, Mur(case.position+direction, 1))

    def add_mur(self, u:crt.Position, v:crt.Position, direction:crt.Direction, mur:Mur, **attr):
        if v not in self.position_case:
            self.add_case(Case(v))
        else:
            if v in self[u] and direction in self[u][v]:
                raise ValueError(f"Un mur existe déjà entre {u} et {v} dans la direction {direction}")
        self.add_edge(u, v, key=direction, mur=mur, **attr)

    def get_case(self, position:crt.Position) -> Case:
        return self.position_case[position]
    
    def get_mur(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Mur:
        if v is None:
            v = self.get_cible(u, direction)
        return self[u][v][direction]['mur']
    
    def get_mur_oppose(self, u:crt.Position, direction:crt.Direction, v:Optional[crt.Position]=None) -> Optional[Mur]:
        if v is None:
            v = self.get_cible(u, direction)
        # On vérifie que le mur existe, que v n'est pas POSITION_ABSENTE, et qu'il n'y a qu'un seul mur entre v et u
        if direction in self[u][v] and len(self[v][u]) == 1:
            return self[v][u]["mur"]
        
    def get_cible(self, position:crt.Position, direction:crt.Direction) -> crt.Position:
        # Il devrait exister un mur sortant de position dans la direction direction
        # Il ne mêne pas nécessairement à position+direction
        for voisin in self[position]:
            if direction in self[position][voisin]:
                return voisin
        raise ValueError(f"La position {position} n'a pas de mur dans la direction {direction}")
        
    def extrait(self, positions:Set[crt.Position]) -> crt.Extrait:
        voisins:Set[crt.Position] = {voisin for position in positions for voisin in self[position] if voisin not in positions}
        subgraph = super().subgraph(positions|voisins)
        return crt.Extrait(voisins, subgraph)

    def veut_passer(self,intrus:Mobile,direction:Direction):
        """Fonction qui tente de faire passer une entitée.
           Se réfère à la case compétente, qui gère tout."""
        position = intrus.get_position()
        if position is POSITION_ABSENTE:
            raise Exception("L'entitée n'a pas de position")
        self.get_mur(position,direction).veut_passer(intrus)

    def get_vue(self,agissant:Agissant):
        position = agissant.get_position()
        if position is None:
            raise Exception("L'agissant n'a pas de position")
        matrice = self.resoud(position,agissant.get_portee_vue())
        if matrice is None:
            raise Exception("Pas de retour ?")
        return Representation_vue(self.id,matrice,self.decalage)

    #Découvrons le déroulé d'un tour, avec Labyrinthe-ni :
    def debut_tour(self): #On commence le tour
        for position in self.nodes:
            self[position].debut_tour()

    def pseudo_debut_tour(self): #On commence le tour
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].pseudo_debut_tour()

    def post_action(self): #On agit sur les actions en suspens (les attaques en particulier)
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].post_action()

    def fin_tour(self):
        if self.controleur is None:
            raise Exception("Pas de controleur !")
        for i in range(self.decalage.x):
            for j in range(self.decalage.y):
                self.matrice_cases[i][j].fin_tour()
        if self.temps_restant >= 0:
            if self.temps_restant == 0:
                self.controleur.desactive_lab(self.id)
            self.temps_restant -= 1
    #Et c'est la fin du tour !

    def quitte(self):
        self.temps_restant = 5

    def attaque(self,position:Position,portee:float,propagation:str,direction:Optional[Direction],obstacles:Set[Position]):
        self.resoud(position,portee,"attaque",propagation,direction,obstacles)

    def resoud(self,position:Position,portee:float,action="vue",propagation="C__S_Pb",direction:Optional[Direction]=None,dead_ends:Set=set(),reset=True,clees:Set[str]=set()) -> Optional[List[List[Representation_case]]]:
        #Les possibilités de propagation sont :
        #                           Circulaire, le mode de propagation de la vision
        #                           Rectiligne, dans une unique direction
        #                           Semi-circulaire, dans trois directions fixées
        #                           Quarter-circulaire, dans deux directions fixées
        #                           Circulaire dégénéré, commence dans toutes les directions puis devient Semi-circulaire pour interdire les demi-tours
        #                           Semi-circulaire dégénéré, commence dans trois directions puis devient Quarter-circulaire pour interdire les demi-tours
        #                           Circulaire Double dégénéré, devient Semi-circulaire dégénéré
        #                           Spatial, se déplace selon les coordonées comme la vue
        #                           Teleporte, se déplace par les téléporteurs comme les attaques magiques
        #                           Passe-porte, passe au travers des portes
        #                           Passe-barrières, passe au travers de certaines portes
        #                           Passe-mur, ignore les murs
        #Exemple de syntaxe du mode de propagation : "Sd_T_Pp", "CD_S_Pm" ou "R__T___"

        if reset:
            for i in range(len(self.matrice_cases)):
                for j in range(len(self.matrice_cases[0])):
                    self.matrice_cases[i][j].clarte = 0

        dirs = [Direction(i) for i in range(NB_DIRECTIONS)]
        forme = propagation[0]
        if forme == "R" and direction is not None:
            dirs = [direction]
        elif forme == "S" and direction is not None:
            dirs.remove(dirs[direction.oppose()])
        elif forme == "Q" and direction is not None:
            dirs.remove(dirs[direction.oppose()])
            dirs.remove(dirs[direction.oppose()-1])

        queue=[(position,dirs,propagation)]

        self.case_from_position(position).clarte = portee

        retrait = 1

        while len(queue) :

            data=queue[0]
            position = data[0]
            if action == "vue":
                retrait = self.case_from_position(position).get_opacite()
            clarte = self.case_from_position(position).clarte - retrait
            #enlever position dans queue
            queue.pop(0)

            if not position in dead_ends:
                #trouver les positions explorables
                positions_voisins=self.voisins_case(data)

                datas_explorables = self.positions_utilisables(positions_voisins,data,clees)

                for data_explorable in datas_explorables:
                    pos = data_explorable[0]
                    clarte_cible = self.case_from_position(pos).clarte

                    if clarte <= 0 and clarte_cible <= 0:
                        self.case_from_position(pos).clarte = -1

                    elif clarte > clarte_cible :
                        #on marque la case comme visitée
                        self.case_from_position(pos).clarte = clarte
                        
                        #on ajoute toutes les directions explorables
                        queue.append(data_explorable)

        if action == "vue":
            matrice_cases:List[List[Representation_case]] = []
            for colonne in self.matrice_cases:
                collone = []
                for case in colonne:
                    collone.append(case.get_infos(clees))
                matrice_cases.append(collone)
            return matrice_cases

    def generation(self,proba:float,poids:List[int]):
        """
        Fonction qui génère la matrice du labyrinthe
            Entrées:
                -Les cases spéciales sous la forme suivante:[coord_case,objet]
                -L'éventuelle probabilité pour casser des murs
                -L'éventuel nombre de murs casser
                -L'éventuelle pourcentage de murs a casser
            Sorties:
                rien
        """        
        #génération en profondeur via l'objet generateur
        #print("Génération du labyrinthe")
        self.generation_en_profondeur(poids)


        for pos in self:
            for mur in self.murs_utilisables(pos,0):
                if random.random() <= proba:
                    self.mur_from_cote(mur).brise()
                    self.mur_from_cote(mur.oppose()).brise()

        for pattern in self.patterns:
            if pattern.vide:
                for pos in pattern:
                    for cote in Bord_dec(pos):
                        if not cote in self.bord:
                            self.mur_from_cote(cote).brise()
                            self.mur_from_cote(cote.oppose()).brise()

            for i in range(len(pattern.entrees)):
                if i < len(pattern.codes):
                    self.mur_from_cote(pattern.entrees[i]+pattern.position).cree_porte(pattern.codes[i])
                    self.mur_from_cote(pattern.entrees[i].oppose()+pattern.position).cree_porte(pattern.codes[i])
                else:
                    self.mur_from_cote(pattern.entrees[i]).brise()
                    self.mur_from_cote(pattern.entrees[i].oppose()).brise()

    def generation_en_profondeur(self,poids:List[int]):
        """
        Fonction qui génère la matrice avec la méthode du parcours en profondeur
        Entrées:Rien
        Sorties:une matrice de cases générée avec le parcours en profondeur
        """
        rdm=random.randrange (1,10**18,1)

        #on définit la seed de notre générateur
        #cela permet d'avoir le meme résultat
        #rdm=851353618387733257
        #print("seed ",rdm)
        random.seed(rdm)

        #print("Début de la génération")
        #position dans la matrice
        position = self.depart
        #le stack est une liste de positions
        stack:List[Position]=[position]

        while len(stack) :

            #on récupère les coords de là où l'on est cad la dernière case dans le stack
            position = stack[len(stack)-1]

            murs_generables = self.murs_utilisables(position)

            if len(murs_generables) > 0 : 

                mur=random.choices(murs_generables,[poids[mur.direction] for mur in murs_generables])[0]
                mur_opp = mur.oppose()

                self.mur_from_cote(mur).brise()
                self.mur_from_cote(mur_opp).brise()

                new_pos = mur_opp.emplacement
                if isinstance(new_pos,Decalage):
                    raise Exception("Weird, should not happen...")
                self.case_from_position(new_pos).clarte=1
                #on ajoute les nouvelles coordonnées de la case au stack
                stack.append(new_pos)
            else:
                #on revient encore en arrière
                stack.pop()

        #print("Fini")

    def murs_utilisables(self,position:Position,nb_murs=NB_DIRECTIONS) -> List[Cote_position]:
        """
        Fonction qui prend en entrées:
            les voisins de la case
        et qui renvoie les directions ou les murs sont cassables
        """
        murs_utilisables:List[Cote_position]=[]

        for cote in Bord_dec(position):
            opp = cote.oppose()
            if not cote in self.bord :
                if self.case_from_position(opp.emplacement).nb_murs_pleins() >= nb_murs:
                    murs_utilisables.append(cote)
        return murs_utilisables

    def voisins_case(self,data:Tuple):
        """
        Fonction qui prend en entrée:
            les coordonnées de la case
        et qui renvoie les voisins de la case
        ainsi que leurs coordonnées
        """
        position:Position = data[0]
        propagation:str = data[2]
        deplacement = propagation[3]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        for i in DIRECTIONS:
            if deplacement == "S":
                cible = position+i
            elif deplacement == "T":
                cible = self.case_from_position(position)[i].get_cible()
            else:
                raise ValueError("Propagation inconnue")
            if cible not in self:
                cible = None
            positions_voisins.append(cible)

        return positions_voisins

    def positions_utilisables(self,positions_voisins:List[Position],data:Tuple,clees:Set[str]):
        """
        Fonction qui prend en entrées:
            les voisins de la case
            les positions des voisins
            la position de la case
            le chemin deja exploré
        et qui renvoie les directions ou l'on peut passer
        """
        position:Position = data[0]
        directions:List[Direction] = data[1]
        propagation:str = data[2]
        forme = propagation[0]
        degenerescence = propagation[1]
        deplacement = propagation[3]
        passage = propagation[6]
        datas_utilisables=[]

        for direction in directions:
            if positions_voisins[direction] is not None:
                voisin = positions_voisins[direction]

                #on vérifie si on peut passer
                blocage = self.case_from_position(position).get_mur_dir(direction).get_blocage(clees)
                if blocage != "Imp" and (passage=="m" or (blocage!="Ple" and ((passage=="p" and (blocage == "Por" or blocage == "P_b")) or (passage=="b" and (blocage == "Bar" or blocage == "P_b")) or (blocage == "Esc" and deplacement == "T") or (blocage == "Tel" and deplacement == "T") or blocage is None))):
                    #On détermine éventuellement la nouvelle forme de propagation
                    if degenerescence == "d":
                        if forme == "C":
                            nouv_prop = "S_"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Q_"+propagation[2:]
                        elif forme == "Q":
                            nouv_prop = "R_"+propagation[2:]
                        else:
                            raise ValueError("Forme inconnue")
                    elif degenerescence == "D":
                        if forme == "C":
                            nouv_prop = "Sd"+propagation[2:]
                        elif forme == "S":
                            nouv_prop = "Qd"+propagation[2:]
                        else:
                            raise ValueError("Forme inconnue")
                    else:
                        nouv_prop = propagation

                    if forme=="R":
                        nouv_dir=[direction]
                    elif forme!="C":
                        #On détermine la direction d'où l'on vient
                        if deplacement=="S":
                            dir_back = direction+2
                        elif deplacement=="T":
                            dir_back = 0
                            for i in DIRECTIONS:
                                if self[voisin,i].get_cible()==position:
                                    dir_back = i
                        else:
                            raise ValueError("Deplacement inconnue")
                        #On n'y retournera pas !
                        nouv_dir=[]
                        for i in directions:
                            if i!=dir_back:
                                nouv_dir.append(i)
                    else:
                        nouv_dir=[dire for dire in DIRECTIONS]

                    nouv_data=(voisin,nouv_dir,nouv_prop)

                    datas_utilisables.append(nouv_data)

        return datas_utilisables

# Imports utilisés dans le code
from .Absent import CASE_ABSENTE
import random