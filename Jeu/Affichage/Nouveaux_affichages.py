from Jeu.Affichage.Affichage import *

class Affichage_principal(Conteneur):
    """L'element principal de l'affichage. Contient tout ce qui apparait à l'écran."""
    
    def __init__(self):
        self.objets = []
        self.contenu = [Affichage_gauche(),Affichage_centre(),Affichage_droite()]
        self.fond = (0,0,0)
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]

    def ajuste_tailles(self,hauteur,largeur):
        # On détermine les proportions des différentes parties de l'affichage
        self.tailles = [largeur,hauteur] # (Ou l'inverse ?)
        # Pour comparaison, le petit écran de mon ASUS contenait du (1350,690)
        # /!\ Gérer le cas où les tailles seraient trop petites
        
        # On va garder les calculs de l'affichage précédent pour l'instant
        hauteur_exploitable = ((hauteur - 30)//20)*20
        largeur_exploitable = ((largeur - 30)//20)*20
        if hauteur_exploitable * 2 > largeur_exploitable :
            hauteur_exploitable = largeur_exploitable / 2
        elif hauteur_exploitable * 2 < self.largeur_exploitable :
            largeur_exploitable = hauteur_exploitable * 2
        else :
            print("Dimensions parfaites !")
        marge_gauche = ((largeur - largeur_exploitable) // 2) - 10
        marge_haut = ((hauteur - hauteur_exploitable) // 2) + -10
        largeur_rectangles = (largeur_exploitable) / 4
        position_debut_x_rectangle_1 = marge_gauche
        position_fin_x_rectangle_1 = position_debut_x_rectangle_1 + largeur_rectangles
        position_debut_x_carre = position_fin_x_rectangle_1 + 10
        position_fin_x_carre = position_debut_x_carre + hauteur_exploitable
        position_debut_x_rectangle_2 = position_fin_x_carre + 10
        position_fin_x_rectangle_2 = position_debut_x_rectangle_2 + largeur_rectangles
        position_debut_y_titre = marge_haut
        position_debut_y_rectangles_et_carre = marge_haut + 20
        position_fin_y_rectangles_et_carre = position_debut_y_rectangles_et_carre + hauteur_exploitable

        self.contenu[0].set_position([position_debut_x_rectangle_1,position_debut_y_rectangles_et_carre])
        self.contenu[0].set_tailles((hauteur_exploitable,largeur_rectangles))
        self.contenu[1].set_position([position_debut_x_carre,position_debut_y_rectangles_et_carre])
        self.contenu[1].set_tailles((hauteur_exploitable,hauteur_exploitable))
        self.contenu[2].set_position([position_debut_x_rectangle_2,position_debut_y_rectangles_et_carre])
        self.contenu[2].set_tailles((hauteur_exploitable,largeur_rectangles))

class Affichage_gauche(Conteneur):
    pass

class Affichage_centre(Conteneur):
    pass

class Affichage_droite(Conteneur):
    pass