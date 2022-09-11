from Jeu.Affichage.Affichage import *
from Jeu.Controleur import *
from Jeu.Skins.Skins import *

from operator import itemgetter
from math import ceil

class Affichage_principal(Wrapper):
    """L'element principal de l'affichage. Contient tout ce qui apparait à l'écran."""
    
    def __init__(self,controleur:Controleur,tailles):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = True
        self.fond = (0,0,0)
        self.tailles = tailles
        self.position = [0,0]
        self.phase = controleur.phase
        
        self.gauche = Affichage_gauche(self.controleur.joueur)
        self.centre = Affichage_centre(self.controleur.joueur)
        self.droite = Affichage_droite(self.controleur)
        # Le reste peut être régénéré à chaque fois ?

        self.inits[self.phase](self)

    def init_tour(self):
        """Crée l'affichage tel qu'il est pendant les phases de jeu normales"""
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),self.centre,Marge_verticale(),self.droite],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas
        
    def init_dialogue(self):
        """Crée l'affichage tel qu'il est pendant les phases de dialogues"""
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),self.centre,Marge_verticale(),Affichage_droite_dialogue(self.controleur.joueur.interlocuteur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_case_dialogue(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),Affichage_centre_case_dialogue(self.controleur.joueur),Marge_verticale(),Affichage_droite_dialogue(self.controleur.joueur.interlocuteur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_case_magie(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),Affichage_centre_case_magie(self.controleur.joueur),Marge_verticale(),Affichage_droite(self.controleur.joueur.interlocuteur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_case_parchemin(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),Affichage_centre_case_parchemin(self.controleur.joueur),Marge_verticale(),Affichage_droite(self.controleur.joueur.interlocuteur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_agissant_dialogue(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_droite_dialogue(self.controleur.joueur.interlocuteur),Marge_verticale(),self.centre,Marge_verticale(),Affichage_droite_agissant_dialogue(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_agissant_magie(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),self.centre,Marge_verticale(),Affichage_droite_agissant_magie(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_agissant_parchemin(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),self.centre,Marge_verticale(),Affichage_droite_agissant_parchemin(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_direction_magie(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),Affichage_centre_direction_magie(self.controleur.joueur),Marge_verticale(),self.droite],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_direction_parchemin(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([self.gauche,Marge_verticale(),Affichage_centre_direction_parchemin(self.controleur.joueur),Marge_verticale(),self.droite],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_cout_magie(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_cout_magie(self.controleur.joueur),Marge_verticale(),self.centre,Marge_verticale(),self.droite],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_cout_parchemin(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_cout_parchemin(self.controleur.joueur),Marge_verticale(),self.centre,Marge_verticale(),self.droite],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_recettes(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),Affichage_centre_recettes(self.controleur.joueur),Marge_verticale(),Affichage_droite_recettes(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_recette(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),self.courant,Marge_verticale(),Affichage_droite_recette(self.controleur,self.courant.courant.recettes)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_ventes(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        menu = Pavage_vertical()
        boutons = Pavage_horizontal()
        onglets = Liste_horizontale()
        onglets.set_contenu([Bouton(SKIN_ACHAT,"Achat"),Marge_verticale(),Bouton(SKIN_VENTE,"Vente")])
        boutons.set_contenu([Marge_verticale(),onglets,Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Quitter"),Marge_verticale()],[5,-1,5,0,5])
        menu.set_contenu([Marge_horizontale(),boutons,Marge_horizontale(),Affichage_centre_ventes(self.controleur.joueur.interlocuteur),Marge_horizontale()],[5,0,5,-1,5])
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),menu,Marge_verticale(),Affichage_droite_ventes(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_vente(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        menu = Pavage_vertical()
        boutons = Pavage_horizontal()
        onglets = Liste_horizontale()
        onglets.set_contenu([Bouton(SKIN_ACHAT,"Achat"),Marge_verticale(),Bouton(SKIN_VENTE,"Vente")])
        boutons.set_contenu([Marge_verticale(),onglets,Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Quitter"),Marge_verticale()],[5,-1,5,0,5])
        menu.set_contenu([Marge_horizontale(),boutons,Marge_horizontale(),self.courant,Marge_horizontale()],[5,0,5,-1,5])
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),menu,Marge_verticale(),Affichage_droite_vente(self.controleur,self.courant.courant)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_achats(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        menu = Pavage_vertical()
        boutons = Pavage_horizontal()
        onglets = Liste_horizontale()
        onglets.set_contenu([Bouton(SKIN_ACHAT,"Achat"),Marge_verticale(),Bouton(SKIN_VENTE,"Vente")])
        boutons.set_contenu([Marge_verticale(),onglets,Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Quitter"),Marge_verticale()],[5,-1,5,0,5])
        menu.set_contenu([Marge_horizontale(),boutons,Marge_horizontale(),Affichage_centre_achats(self.controleur.joueur.interlocuteur),Marge_horizontale()],[5,0,5,-1,5])
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),menu,Marge_verticale(),Affichage_droite_achats(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_achat(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        menu = Pavage_vertical()
        boutons = Pavage_horizontal()
        onglets = Liste_horizontale()
        onglets.set_contenu([Bouton(SKIN_ACHAT,"Achat"),Marge_verticale(),Bouton(SKIN_VENTE,"Vente")])
        boutons.set_contenu([Marge_verticale(),onglets,Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Quitter"),Marge_verticale()],[5,-1,5,0,5])
        menu.set_contenu([Marge_horizontale(),boutons,Marge_horizontale(),self.courant,Marge_horizontale()],[5,0,5,-1,5])
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),menu,Marge_verticale(),Affichage_droite_achat(self.controleur,self.courant.courant)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_impregnations(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),Affichage_centre_impregnations,Marge_verticale(),Affichage_droite_impregnations(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_impregnation(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),self.courant,Marge_verticale(),Affichage_droite_impregnation(self.controleur,self.courant.courant)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_auto_impregnations(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),Affichage_centre_auto_impregnations,Marge_verticale(),Affichage_droite_auto_impregnations(self.controleur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_auto_impregnation(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche_inventaire(self.controleur.joueur),Marge_verticale(),self.courant,Marge_verticale(),Affichage_droite_auto_impregnation(self.controleur,self.courant.courant)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def update(self):
        if self.phase != self.controleur.phase: #On a changé de phase
            self.phase = self.controleur.phase
            self.inits[self.phase](self)
            self.set_tailles(self.tailles)
        else: #Les autres changements sont gérés au plus proche
            self.contenu.update()
            for objet in self.objets:
                objet.update()

    def bouge_souris(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #On a cliqué sur quelque chose. Vérifions quoi :
            self.clique(event.pos)
        elif event.type == pygame.MOUSEWHEEL:
            self.scroll(pygame.mouse.get_pos(),10*event.x,10*event.y)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            self.courant = clique
            if isinstance(clique,Affichage_centre_recettes):
                self.init_recette()
            if isinstance(clique,Affichage_centre_ventes):
                self.init_vente()
            if isinstance(clique,Affichage_centre_achats):
                self.init_achat()
            if isinstance(clique,Bouton) and clique.texte == "Quitter":
                self.controleur.unset_phase(MARCHAND)
            if isinstance(clique,Affichage_centre_impregnations):
                self.init_impregnation()
            if isinstance(clique,Affichage_centre_auto_impregnations):
                self.init_auto_impregnation()
        else:
            self.courant = False

    def navigue(self,direction):
        pass

    inits={
        TOUR:init_tour,
        DIALOGUE:init_dialogue,
        TOUCHE:None,
        LEVEL_UP:None,
        RECETTE:init_recettes,
        MARCHAND:init_achats,
        IMPREGNATION:init_impregnations,
        AUTO_IMPREGNATION:init_auto_impregnations,
        AGISSANT_DIALOGUE:init_agissant_dialogue,
        CASE_DIALOGUE:init_case_dialogue,
        AGISSANT_MAGIE:init_agissant_magie,
        CASE_MAGIE:init_case_magie,
        DIRECTION_MAGIE:init_direction_magie,
        COUT_MAGIE:init_cout_magie,
        AGISSANT_PARCHEMIN:init_agissant_parchemin,
        CASE_PARCHEMIN:init_case_parchemin,
        DIRECTION_PARCHEMIN:init_direction_parchemin,
        COUT_PARCHEMIN:init_cout_parchemin,
        CINEMATIQUE:None,
    }

class Affichage_gauche(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]

        self.stats = Affichage_stats(self.joueur)
        self.inventaire = Affichage_inventaire(self.joueur)
        self.classe = Affichage_sous_classe(self.joueur.classe_principale)

        self.init_gauche()

    def init_gauche(self):
        self.courant = False
        contenu = Pavage_horizontal()
        triptique = Liste_verticale()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_ferme(self.joueur),Marge_horizontale(),Affichage_inventaire_ferme(self.joueur),Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,0,5,0,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_stats(self):
        self.courant = self.stats
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),self.courant,Marge_horizontale(),Affichage_inventaire_ferme(self.joueur),Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,-1,5,0,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_inventaire(self):
        self.courant = self.inventaire
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_ferme(self.joueur),Marge_horizontale(),self.courant,Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,0,5,-1,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_classe(self):
        self.courant = self.classe
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_ferme(self.joueur),Marge_horizontale(),Affichage_inventaire_ferme(self.joueur),Marge_horizontale(),self.courant,Marge_horizontale()],[5,0,5,0,5,-1,5]) # /!\ Remplacer par Affichage_classe_principale
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_stats_ferme): #On veut ouvrir l'affichage des stats
                self.init_stats()
                self.set_tailles(self.tailles)
            if isinstance(clique,Affichage_inventaire_ferme): #On veut ouvrir l'affichage des stats
                self.init_inventaire()
                self.set_tailles(self.tailles)
            if isinstance(clique,Affichage_classe_ferme): #On veut ouvrir l'affichage des stats
                self.init_classe()
                self.set_tailles(self.tailles)
        else:
            self.init_gauche()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]

        self.labyrinthe = Affichage_labyrinthe(self.joueur)

        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(),self.labyrinthe,Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

class Affichage_droite(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]

        self.allies = Affichage_allies(self.controleur)
        self.ennemis = Affichage_ennemis(self.controleur)
        self.neutres = Affichage_neutres(self.controleur)
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),self.allies,Marge_verticale(),self.ennemis,Marge_verticale(),self.neutres,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_allie(self):
        allie = self.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),self.allies,Marge_verticale(),self.ennemis,Marge_verticale(),self.neutres,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(allie.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_ennemi(self):
        ennemi = self.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),self.allies,Marge_verticale(),self.ennemis,Marge_verticale(),self.neutres,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(ennemi.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_neutre(self):
        neutre = self.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),self.allies,Marge_verticale(),self.ennemis,Marge_verticale(),self.neutres,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(neutre.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignette_allie):
                self.courant = clique
                self.init_allie() #Donner des informations spécifiques pour les alliés ?
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
                self.init_ennemi() #Donner des informations spécifiques pour les ennemis ?
            if isinstance(clique,Vignette_neutre):
                self.courant = clique
                self.init_neutre() #Donner des informations spécifiques pour les neutres ?
            if isinstance(clique,Paves):
                self.controleur.get_esprit(self.controleur.joueur.esprit).utilise(self.courant.agissant)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

    def update(self):
        if not self.courant in self.allies.allies + self.ennemis.ennemis + self.neutres.neutres :
            self.init_droite()
        else:
            if isinstance(self.courant,Vignette_allie):
                self.init_allie() #Donner des informations spécifiques pour les alliés ?
            if isinstance(self.courant,Vignette_ennemi):
                self.init_ennemi() #Donner des informations spécifiques pour les ennemis ?
            if isinstance(self.courant,Vignette_neutre):
                self.init_neutre() #Donner des informations spécifiques pour les neutres ?
        self.set_tailles(self.tailles)
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_gauche_cout_magie(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_gauche()

    def init_gauche(self):
        self.courant = False
        contenu = Pavage_horizontal()
        triptique = Liste_verticale()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_cout_magie(self.joueur),Marge_horizontale(),Affichage_inventaire_ferme(self.joueur),Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,0,5,0,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

class Affichage_gauche_cout_parchemin(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_gauche()

    def init_gauche(self):
        self.courant = False
        contenu = Pavage_horizontal()
        triptique = Liste_verticale()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_cout_parchemin(self.joueur),Marge_horizontale(),Affichage_inventaire_ferme(self.joueur),Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,0,5,0,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

class Affichage_gauche_inventaire(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_gauche()

    def init_gauche(self):
        self.courant = Affichage_inventaire(self.joueur)
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_ferme(self.joueur),Marge_horizontale(),self.courant,Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,0,5,-1,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            self.courant = clique
        else:
            self.init_gauche()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre_case_dialogue(Wrapper):
    def __init__(self,joueur:Joueur):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cible = None
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        diptique.set_contenu([Marge_horizontale(),Affichage_labyrinthe_case_dialogue(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_labyrinthe_case_dialogue):
                self.courant = clique
                self.cible = self.courant.cible
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.joueur.interlocuteur.set_cible(self.cible)
                self.joueur.controleur.unset_phase(CASE_DIALOGUE)
                print(self.joueur.controleur.phases)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_centre()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre_case_magie(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        diptique.set_contenu([Marge_horizontale(),Affichage_labyrinthe_case_magie(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_labyrinthe_case_magie):
                self.courant = clique
                self.cible = self.courant.cible
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.joueur.cible_magie = self.cible
                self.joueur.controleur.unset_phase(CASE_MAGIE)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_centre()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre_case_parchemin(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        diptique.set_contenu([Marge_horizontale(),Affichage_labyrinthe_case_parchemin(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_labyrinthe_case_parchemin):
                self.courant = clique
                self.cible = self.courant.cible
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.joueur.cible_magie_parchemin = self.cible
                self.joueur.controleur.unset_phase(CASE_PARCHEMIN)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_centre()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre_direction_magie(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        diptique.set_contenu([Marge_horizontale(),Affichage_labyrinthe_direction_magie(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_labyrinthe_direction_magie):
                self.courant = clique
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.joueur.dir_magie = self.courant.direction
                self.joueur.controleur.unset_phase(DIRECTION_MAGIE)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_centre()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre_direction_parchemin(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        diptique.set_contenu([Marge_horizontale(),Affichage_labyrinthe_direction_parchemin(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_labyrinthe_direction_parchemin):
                self.courant = clique
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.joueur.dir_magie_parchemin = self.courant.direction
                self.joueur.controleur.unset_phase(DIRECTION_PARCHEMIN)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_centre()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_centre_recettes(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        recettes = self.joueur.interlocuteur.get_recettes()
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        menu = Liste_menu()
        menu.set_contenu([Vignette_recette(recette,40,isinstance(self.courant,Vignette_recette) and recette != self.courant.recette,not self.joueur.inventaire.peut_fournir({eval(ingredient):recette["ingredients"][ingredient] for ingredient in recette["ingredients"]})) for recette in recettes])
        monoptique.set_contenu([Marge_horizontale(),menu,Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_recette):
                self.courant = clique
                self.init_centre()
            print(clique)
            return self
        else:
            self.init_centre()
            self.set_tailles(self.tailles)
        return False

class Affichage_centre_ventes(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        items = self.joueur.inventaire.get_items()
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        menu = Liste_menu()
        menu.set_contenu([Vignette_vente(item,40,self.joueur.interlocuteur.get_prix_vente(item),self.joueur.interlocuteur.get_description(item),isinstance(self.courant,Vignette_vente) and item != self.courant.item,item in self.joueur.inventaire.get_equippement()) for item in items])
        monoptique.set_contenu([Marge_horizontale(),menu,Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_vente):
                self.courant = clique
                self.init_centre()
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_centre_achats(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        items = self.joueur.interlocuteur.get_marchandise()
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        menu = Liste_menu()
        menu.set_contenu([Vignette_achat(eval(item["item"])(None),40,item["prix"],item["description"],isinstance(self.courant,Vignette_achat) and item != self.courant.item,item["prix"]>self.joueur.argent) for item in items])
        monoptique.set_contenu([Marge_horizontale(),menu,Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_achat):
                self.courant = clique
                self.init_centre()
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_centre_impregnations(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        magies = self.joueur.interlocuteur.get_magies()
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        menu = Liste_menu()
        menu.set_contenu([Vignette_magie(magie,40,isinstance(self.courant,Vignette_magie) and magie != self.courant.magie,magie.cout_mp>self.joueur.interlocuteur.pm) for magie in magies])
        monoptique.set_contenu([Marge_horizontale(),menu,Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_magie):
                self.courant = clique
                self.init_centre()
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_centre_auto_impregnations(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        magies = self.joueur.get_magies()
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        menu = Liste_menu()
        menu.set_contenu([Vignette_magie(magie,40,isinstance(self.courant,Vignette_magie) and magie != self.courant.magie,magie.cout_mp>self.joueur.pm) for magie in magies])
        monoptique.set_contenu([Marge_horizontale(),menu,Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_magie):
                self.courant = clique
                self.init_centre()
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_droite_dialogue(Wrapper):
    def __init__(self,interlocuteur:Humain):
        self.interlocuteur = interlocuteur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.replique = interlocuteur.replique

        self.repliques = Liste_verticale()
        self.phrase = Pave(self.interlocuteur.get_replique(self.interlocuteur.replique))
        repliques = [Affichage_replique(self.interlocuteur.get_replique(replique),replique) for replique in self.interlocuteur.repliques]
        self.repliques.set_contenu([repliques[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(repliques)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(repliques)*2)])

        self.init_droite()

    def init_droite(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),Affichage_perso(self.interlocuteur),Marge_horizontale(),self.phrase,Marge_horizontale(),self.repliques,Marge_horizontale()],[5,0,5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def update(self):
        if self.replique != self.interlocuteur.replique:
            self.replique = self.interlocuteur.replique
            self.phrase = Pave(self.interlocuteur.get_replique(self.interlocuteur.replique))
            repliques = [Affichage_replique(self.interlocuteur.get_replique(replique),replique) for replique in self.interlocuteur.repliques]
            self.repliques.set_contenu([repliques[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(repliques)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(repliques)*2)])
            self.init_droite()
            self.set_tailles(self.tailles)
        else:
            self.contenu.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_replique):
                if clique != self.courant:
                    self.courant = clique
                else:
                    self.interlocuteur.interprete(self.courant.replique)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_droite_agissant_dialogue(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cible = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_dialogue(self.controleur),Marge_verticale(),Affichage_ennemis_agissant_dialogue(self.controleur),Marge_verticale(),Affichage_neutres_agissant_dialogue(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_allie(self):
        allie = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),self.courant,Marge_verticale(),Affichage_ennemis_agissant_dialogue(self.controleur),Marge_verticale(),Affichage_neutres_agissant_dialogue(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(allie.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_ennemi(self):
        ennemi = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_dialogue(self.controleur),Marge_verticale(),self.courant,Marge_verticale(),Affichage_neutres_agissant_dialogue(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(ennemi.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_neutre(self):
        neutre = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_dialogue(self.controleur),Marge_verticale(),Affichage_ennemis_agissant_dialogue(self.controleur),Marge_verticale(),self.courant,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(neutre.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_allies_agissant_dialogue):
                if self.courant != clique and isinstance(self.courant,Affichable):
                    self.courant.cible = None
                self.courant = clique
                self.cible = self.courant.cible
                self.init_allie() #Donner des informations spécifiques pour ce choix ?
            if isinstance(clique,Affichage_ennemis_agissant_dialogue):
                if self.courant != clique and isinstance(self.courant,Affichable):
                    self.courant.cible = None
                self.courant = clique
                self.cible = self.courant.cible
                self.init_ennemi()
            if isinstance(clique,Affichage_neutres_agissant_dialogue):
                if self.courant != clique and isinstance(self.courant,Affichable):
                    self.courant.cible = None
                self.courant = clique
                self.cible = self.courant.cible
                self.init_neutre()
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.controleur.joueur.interlocuteur.set_cible(self.cible)
                self.controleur.unset_phase(AGISSANT_DIALOGUE)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_droite_agissant_magie(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie,Multi_cible):
            self.cible = {"alliés":[],"ennemis":[],"neutres":[]}
        else:
            self.cible = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_magie(self.controleur),Marge_verticale(),Affichage_ennemis_agissant_magie(self.controleur),Marge_verticale(),Affichage_neutres_agissant_magie(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_allie(self):
        allie = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),self.courant,Marge_verticale(),Affichage_ennemis_agissant_magie(self.controleur),Marge_verticale(),Affichage_neutres_agissant_magie(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(allie.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_ennemi(self):
        ennemi = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_magie(self.controleur),Marge_verticale(),self.courant,Marge_verticale(),Affichage_neutres_agissant_magie(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(ennemi.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_neutre(self):
        neutre = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_magie(self.controleur),Marge_verticale(),Affichage_ennemis_agissant_magie(self.controleur),Marge_verticale(),self.courant,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(neutre.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_allies_agissant_magie):
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    self.courant = clique
                    self.cible["alliés"] = self.courant.cible
                else:
                    if self.courant != clique:
                        self.courant.cible = None
                    self.courant = clique
                    self.cible = self.courant.cible
                    self.init_allie() #Donner des informations spécifiques pour ce choix ?
            if isinstance(clique,Affichage_ennemis_agissant_magie):
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    self.courant = clique
                    self.cible["ennemis"] = self.courant.cible
                else:
                    if self.courant != clique:
                        self.courant.cible = None
                    self.courant = clique
                    self.cible = self.courant.cible
                    self.init_ennemi()
            if isinstance(clique,Affichage_neutres_agissant_magie):
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    self.courant = clique
                    self.cible["neutres"] = self.courant.cible
                else:
                    if self.courant != clique:
                        self.courant.cible = None
                    self.courant = clique
                    self.cible = self.courant.cible
                    self.init_neutre()
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    self.cible = self.cible["alliés"]+self.cible["ennemis"]+self.cible["neutres"]
                self.controleur.joueur.cible_magie = self.cible
                self.controleur.unset_phase(AGISSANT_MAGIE)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_droite_agissant_parchemin(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
            self.cible = {"alliés":[],"ennemis":[],"neutres":[]}
        else:
            self.cible = None
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_parchemin(self.controleur),Marge_verticale(),Affichage_ennemis_agissant_parchemin(self.controleur),Marge_verticale(),Affichage_neutres_agissant_parchemin(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_allie(self):
        allie = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),self.courant,Marge_verticale(),Affichage_ennemis_agissant_parchemin(self.controleur),Marge_verticale(),Affichage_neutres_agissant_parchemin(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(allie.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_ennemi(self):
        ennemi = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_parchemin(self.controleur),Marge_verticale(),self.courant,Marge_verticale(),Affichage_neutres_agissant_parchemin(self.controleur),Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(ennemi.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_neutre(self):
        neutre = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_verticale(),Affichage_allies_agissant_parchemin(self.controleur),Marge_verticale(),Affichage_ennemis_agissant_parchemin(self.controleur),Marge_verticale(),self.courant,Marge_verticale()],[5,-1,5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(neutre.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale(),monoptique,Marge_horizontale(),boutons,Marge_horizontale()],[5,-1,5,0,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_allies_agissant_parchemin):
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    self.courant = clique
                    self.cible["alliés"] = self.courant.cible
                else:
                    if self.courant != clique:
                        self.courant.cible = None
                    self.courant = clique
                    self.cible = self.courant.cible
                    self.init_allie() #Donner des informations spécifiques pour ce choix ?
            if isinstance(clique,Affichage_ennemis_agissant_parchemin):
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    self.courant = clique
                    self.cible["ennemis"] = self.courant.cible
                else:
                    if self.courant != clique:
                        self.courant.cible = None
                    self.courant = clique
                    self.cible = self.courant.cible
                    self.init_ennemi()
            if isinstance(clique,Affichage_neutres_agissant_parchemin):
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    self.courant = clique
                    self.cible["neutres"] = self.courant.cible
                else:
                    if self.courant != clique:
                        self.courant.cible = None
                    self.courant = clique
                    self.cible = self.courant.cible
                    self.init_neutre()
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    self.cible = self.cible["alliés"]+self.cible["ennemis"]+self.cible["neutres"]
                self.controleur.joueur.cible_magie_parchemin = self.cible
                self.controleur.unset_phase(AGISSANT_PARCHEMIN)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_droite_recettes(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(),Texte("Choisit un item à synthétiser."),Marge_verticale()],[-1,0,-1])
        contenu.set_contenu([Marge_horizontale(),monotique,Marge_horizontale()],[-1,0,-1])
        self.contenu = contenu
        self.fond = (255,255,255)

class Affichage_droite_recette(Wrapper):
    def __init__(self,controleur:Controleur,recette):
        self.controleur = controleur
        self.recette = recette
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite_produit()

    def init_droite_produit(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        liste = Liste_horizontale()
        boutons = Pavage_horizontal()
        if self.controleur.joueur.inventaire.peut_fournir({eval(ingredient):self.recette["ingredients"][ingredient] for ingredient in self.recette["ingredients"]}):
            boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,0,-1,0,5])
        else:
            boutons.set_contenu([Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,-1,0,5])
        ingredients = [Vignette_ingredient(eval(ingredient)(None),self.recette["ingredients"][ingredient],self.controleur.joueur.inventaire.quantite(eval(ingredient)),40) for ingredient in self.recette["ingredients"]]
        liste.set_contenu([ingredients[i//2] if i%2 == 0 else Marge_verticale() for i in range(len(ingredients)*2-1)],[0 if i%2 == 0 else 5 for i in range(len(ingredients)*2-1)])
        diptique.set_contenu([Marge_verticale(),Vignette_recette(self.recette,40,False,not self.controleur.joueur.inventaire.peut_fournir({eval(ingredient):self.recette["ingredients"][ingredient] for ingredient in self.recette["ingredients"]})),Marge_verticale(),liste,Marge_verticale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale(),Paves(eval(self.recette["produit"])(None).get_description()),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_droite_ingredient(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        liste = Liste_horizontale()
        boutons = Pavage_horizontal()
        if self.controleur.joueur.inventaire.peut_fournir({eval(ingredient):self.recette["ingredients"][ingredient] for ingredient in self.recette["ingredients"]}):
            boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,0,-1,0,5])
        else:
            boutons.set_contenu([Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,-1,0,5])
        ingredients = [Vignette_ingredient(eval(ingredient)(None),self.recette["ingredients"][ingredient],self.controleur.joueur.inventaire.quantite(eval(ingredient)),40) for ingredient in self.recette["ingredients"]]
        liste.set_contenu([ingredients[i//2] if i%2 == 0 else Marge_verticale() for i in range(len(ingredients)*2-1)],[0 if i%2 == 0 else 5 for i in range(len(ingredients)*2-1)])
        diptique.set_contenu([Marge_verticale(),Vignette_recette(self.recette,40,False,not self.controleur.joueur.inventaire.peut_fournir({eval(ingredient):self.recette["ingredients"][ingredient] for ingredient in self.recette["ingredients"]})),Marge_verticale(),liste,Marge_verticale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale(),Paves(self.courant.ingredient.get_description()),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignette_recette):
                self.courant = clique
                self.init_droite_produit() #Donner des informations spécifiques pour les alliés ?
            if isinstance(clique,Vignette_ingredient):
                self.courant = clique
                self.init_droite_ingredient() #Donner des informations spécifiques pour les ennemis ?
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                item = self.controleur.joueur.interlocuteur.cuisine(self.recette)
                self.controleur.ajoute_entitee(item)
                for ingredient in self.recette["ingredients"]:
                    for _ in range(self.recette["ingredients"][ingredient]):
                        self.controleur.joueur.inventaire.consomme(eval(ingredient))
                self.controleur.joueur.inventaire.ajoute(item)
                self.controleur.unset_phase(RECETTE)
            if isinstance(clique,Bouton) and clique.texte == "Annuler":
                self.controleur.unset_phase(RECETTE)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite_produit()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_droite_ventes(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(),Texte("Quel item veux-tu vendre ?"),Marge_verticale()],[-1,0,-1])
        contenu.set_contenu([Marge_horizontale(),monotique,Marge_horizontale()],[-1,0,-1])
        self.contenu = contenu
        self.fond = (255,255,255)

class Affichage_droite_vente(Wrapper):
    def __init__(self,controleur:Controleur,vignette):
        self.controleur = controleur
        self.item = vignette.item
        self.prix = vignette.prix
        self.description = vignette.description
        self.invalide = vignette.invalide
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite_vente()

    def init_droite_vente(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        textes = self.item.get_description()
        textes.append(self.description)
        textes.append(f"Je veux bien t'en donner {self.prix} €.")
        if self.invalide:
            textes.append("(Cet item est actuellement équippé, veux-tu vraiment le vendre ?)")
        boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Vendre"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_horizontale(),Vignette_item([0,0],self.item,40,0,False,self.invalide),Marge_horizontale(),Paves(textes),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Bouton) and clique.texte == "Vendre":
                self.controleur.joueur.inventaire.drop(None,self.item.ID)
                self.controleur.joueur.argent += self.prix
            self.set_tailles(self.tailles)
            return self
        else:
            self.courant = False
            self.init_droite_vente()
            self.set_tailles(self.tailles)
        return False

class Affichage_droite_achats(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        monotique = Pavage_horizontal()
        monotique.set_contenu([Marge_verticale(),Texte("Quel item veux-tu acheter ?"),Marge_verticale()],[-1,0,-1])
        contenu.set_contenu([Marge_horizontale(),monotique,Marge_horizontale()],[-1,0,-1])
        self.contenu = contenu
        self.fond = (255,255,255)

class Affichage_droite_achat(Wrapper):
    def __init__(self,controleur:Controleur,vignette):
        self.controleur = controleur
        self.item = vignette.item
        self.prix = vignette.prix
        self.description = vignette.description
        self.invalide = vignette.invalide
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite_achat()

    def init_droite_achat(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        textes = self.item.get_description()
        textes.append(self.description)
        textes.append(f"Je te le vends pour {self.prix} €.")
        if self.invalide:
            textes.append("(Tu n'as pas assez d'argent pour acheter cet item. Tu peux me vendre ce dont tu ne sers pas si tu tiens vraiment à l'obtenir.)")
            boutons.set_contenu([Marge_verticale(),Marge_verticale(),Marge_verticale()],[5,-1,5]) #J'envisage de rajouter d'autres boutons un jour
        else:
            boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Acheter"),Marge_verticale(),Marge_verticale()],[5,0,-1,5])
        triptique.set_contenu([Marge_horizontale(),Vignette_item([0,0],self.item,40,0,False,self.invalide),Marge_horizontale(),Paves(textes),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Bouton) and clique.texte == "Acheter":
                self.controleur.joueur.inventaire.ajoute(self.item)
                self.controleur.joueur.argent -= self.prix
            self.set_tailles(self.tailles)
            return self
        else:
            self.courant = False
            self.init_droite_achat()
            self.set_tailles(self.tailles)
        return False

class Affichage_droite_impregnations(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,-1,0,5])
        diptique.set_contenu([Marge_verticale(),Texte("De quelle magie veux-tu que j'imprègne ce parchemin ?"),Marge_verticale(),Marge_verticale(),boutons,Marge_verticale()],[-1,0,-1,5,0,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale()],[-1,0,-1])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Bouton) and clique.texte == "Annuler":
                self.controleur.unset_phase(IMPREGNATION)
            self.set_tailles(self.tailles)
            return self
        else:
            self.courant = False
            self.init_droite_achat()
            self.set_tailles(self.tailles)
        return False

class Affichage_droite_impregnation(Wrapper):
    def __init__(self,controleur:Controleur,vignette):
        self.controleur = controleur
        self.magie = vignette.magie
        self.invalide = vignette.invalide
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite_achat()

    def init_droite_achat(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        textes = self.magie.get_description(0)
        textes.append(self.description)
        if self.invalide:
            textes.append("(Je n'ai pas assez de mana pour impregner ce parchemin. Reviens me voir plus tard.)")
            boutons.set_contenu([Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,-1,0,5])
        else:
            boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Impregner"),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,0,-1,0,5])
        triptique.set_contenu([Marge_horizontale(),Vignette_magie(self.magie,40,False,self.invalide),Marge_horizontale(),Paves(textes),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Bouton) and clique.texte == "Impregner":
                self.controleur.joueur.interlocuteur.impregne(self.magie.nom)
                self.controleur.unset_phase(IMPREGNATION)
            if isinstance(clique,Bouton) and clique.texte == "Annuler":
                self.controleur.unset_phase(IMPREGNATION)
            self.set_tailles(self.tailles)
            return self
        else:
            self.courant = False
            self.init_droite_achat()
            self.set_tailles(self.tailles)
        return False

class Affichage_droite_auto_impregnations(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,-1,0,5])
        diptique.set_contenu([Marge_verticale(),Texte("De quelle magie veux-tu impregner ce parchemin ?"),Marge_verticale(),Marge_verticale(),boutons,Marge_verticale()],[-1,0,-1,5,0,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale()],[-1,0,-1])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Bouton) and clique.texte == "Annuler":
                self.controleur.unset_phase(IMPREGNATION)
            self.set_tailles(self.tailles)
            return self
        else:
            self.courant = False
            self.init_droite_achat()
            self.set_tailles(self.tailles)
        return False

class Affichage_droite_auto_impregnation(Wrapper):
    def __init__(self,controleur:Controleur,vignette):
        self.controleur = controleur
        self.magie = vignette.magie
        self.invalide = vignette.invalide
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite_achat()

    def init_droite_achat(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        textes = self.magie.get_description(0)
        textes.append(self.description)
        if self.invalide:
            textes.append("(Tu n'as pas assez de mana pour impregner ce parchemin. Réessaye plus tard.)")
            boutons.set_contenu([Marge_verticale(),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,-1,0,5])
        else:
            boutons.set_contenu([Marge_verticale(),Bouton(SKIN_VALIDER,"Impregner"),Marge_verticale(),Bouton(SKIN_QUITTER,"Annuler"),Marge_verticale()],[5,0,-1,0,5])
        triptique.set_contenu([Marge_horizontale(),Vignette_magie(self.magie,40,False,self.invalide),Marge_horizontale(),Paves(textes),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Bouton) and clique.texte == "Impregner":
                self.controleur.joueur.auto_impregne(self.magie.nom)
                self.controleur.unset_phase(AUTO_IMPREGNATION)
            if isinstance(clique,Bouton) and clique.texte == "Annuler":
                self.controleur.unset_phase(AUTO_IMPREGNATION)
            self.set_tailles(self.tailles)
            return self
        else:
            self.courant = False
            self.init_droite_achat()
            self.set_tailles(self.tailles)
        return False

class Affichage_stats_ferme(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        diptique_gauche = Pavage_vertical()
        diptique_droite = Pavage_vertical()
        diptique_gauche.set_contenu([Marge_horizontale(),Texte("PV"),Marge_horizontale(),Affichage_PV(self.joueur),Marge_horizontale()],[5,0,5,0,5])
        diptique_droite.set_contenu([Marge_horizontale(),Texte("PM"),Marge_horizontale(),Affichage_PM(self.joueur),Marge_horizontale()],[5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),diptique_gauche,Marge_verticale(),diptique_droite,Marge_verticale()],[5,-1,5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_stats(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        tetraptique = Pavage_vertical()
        tetraptique.set_contenu([Marge_horizontale(),Texte("PV"),Marge_horizontale(),Affichage_PV(self.joueur),Marge_horizontale(),Texte("PM"),Marge_horizontale(),Affichage_PM(self.joueur),Marge_horizontale()],[5,0,5,0,5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),tetraptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_stats_cout_magie(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cout = 0
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        pentaptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        pentaptique.set_contenu([Marge_horizontale(),Texte("PV"),Marge_horizontale(),Affichage_PV(self.joueur),Marge_horizontale(),Texte("PM"),Marge_horizontale(),Affichage_PM_cout(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,0,5,0,5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),pentaptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_PM_cout):
                self.courant = clique
                self.cout = clique.cout
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.controleur.joueur.cout_magie = self.cout
                self.controleur.unset_phase(COUT_MAGIE)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_stats_cout_parchemin(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cout = 0
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        pentaptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Bouton(SKIN_VALIDER,"Confirmer"),Marge_verticale()],[0,-1])
        pentaptique.set_contenu([Marge_horizontale(),Texte("PV"),Marge_horizontale(),Affichage_PV(self.joueur),Marge_horizontale(),Texte("PM"),Marge_horizontale(),Affichage_PM_cout(self.joueur),Marge_horizontale(),boutons,Marge_horizontale()],[5,0,5,0,5,0,5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),pentaptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_PM_cout):
                self.courant = clique
                self.cout = clique.cout
            if isinstance(clique,Bouton) and clique.texte == "Confirmer":
                self.controleur.joueur.cout_magie_parchemin = self.cout
                self.controleur.unset_phase(COUT_PARCHEMIN)
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_inventaire_ferme(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        liste = Liste_horizontale()
        vignettes = [Vignette([0,0],20,classe.get_image()) for classe in self.joueur.inventaire.items.keys()]
        liste.set_contenu([vignettes[i//2] if i%2==0 else Marge_verticale() for i  in range(-1,len(vignettes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(vignettes)*2)])
        monoptique.set_contenu([Marge_horizontale(),liste,Marge_horizontale()],[5,0,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_inventaire(Wrapper):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]

        classes = self.joueur.inventaire.items.keys()

        self.liste_v = Liste_verticale()
        #pas joli : vignettes = [Vignette_categorie(classe,40,False,not self.joueur.inventaire.items[classe]) for classe in self.joueur.inventaire.items.keys()]
        vignettes = [Vignette_categorie(classe,40) for classe in classes]
        self.liste_v.set_contenu([vignettes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(vignettes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(vignettes)*2)])
        self.categories = {classe:Affichage_categorie(self.joueur,classe) for classe in classes}

        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monoptique = Liste_horizontale()
        monoptique.set_contenu([Marge_verticale(),self.liste_v,Marge_verticale()],[5,0,5])
        contenu.set_contenu([Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_classe(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        diptique.set_contenu([Marge_verticale(),self.liste_v,Marge_verticale(),self.categories[self.courant.categorie],Marge_verticale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignette_categorie): #On veut ouvrir une catégorie
                self.courant = clique
                self.init_classe()
                self.set_tailles(self.tailles)
        else:
            # self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_categorie(Wrapper):
    def __init__(self,joueur:Agissant,categorie:Union[Type[Potion],Type[Parchemin],Type[Cle],Type[Arme],Type[Bouclier],Type[Armure],Type[Haume],Type[Anneau],Type[Projectile],Type[Ingredient],Type[Cadavre],Type[Oeuf]]):
        self.joueur = joueur
        self.categorie = categorie
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]

        self.liste_i = Liste_verticale()
        self.items = [Vignette_item([0,0],self.joueur.controleur[ID],40) for ID in self.joueur.inventaire.items[self.categorie]]
        self.liste_i.set_contenu([self.items[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.items)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.items)*2)])

        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monoptique = Liste_horizontale()
        monoptique.set_contenu([Marge_verticale(),self.liste_i,Marge_verticale()],[5,0,5])
        contenu.set_contenu([Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_item(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(),self.liste_i,Marge_verticale(),Paves(self.courant.item.get_description(0)),Marge_verticale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignette_item): #On veut afficher un item
                if clique == self.courant:
                    self.joueur.inventaire.utilise_item(clique.item.ID)
                else:
                    self.courant = clique
                    self.init_item()
                self.set_tailles(self.tailles)
        else:
            # self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

    def update(self):
        i=0
        items = self.joueur.inventaire.items[self.categorie]
        while i < len(items) or i < len(self.items):
            if i == len(items) or i == len(self.items) or items[i] != self.items[i].item.ID: #Les deux ne correspondent pas
                if i == len(self.items) or self.items[i].item.ID in items: #Donc l'item n'a pas été retiré, mais d'autres ont été ajoutés avant
                    item = Vignette_item([0,0],self.joueur.controleur[items[i]],40)
                    self.items.insert(i,item)
                    self.liste_i.insert(2*i,item,0)
                    self.liste_i.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #l'item qui était à l'emplacement i a été retiré
                    self.items.pop(i)
                    self.liste_i.pop(2*i) # La marge avant l'item
                    self.liste_i.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres items à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_classe_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(),Pave("Classes & compétences"),Marge_horizontale()],[5,0,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_sous_classe(Wrapper):
    def __init__(self,classe):
        self.classe = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]

        self.intrasecs = Affichage_intrasecs(self.classe)
        self.skills = Affichage_skills(self.classe)
        self.classes = Affichage_classes(self.classe)

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        liste.set_contenu([Marge_horizontale(),Affichage_intrasecs_ferme(self.classe),Marge_horizontale(),Affichage_skills_ferme(self.classe),Marge_horizontale(),Affichage_classes_ferme(self.classe),Marge_horizontale()],[5,0,5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_intrasecs(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(),self.intrasecs,Marge_horizontale(),Affichage_skills_ferme(self.classe),Marge_horizontale(),Affichage_classes_ferme(self.classe),Marge_horizontale()],[5,-1,5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_skills(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(),Affichage_intrasecs_ferme(self.classe),Marge_horizontale(),self.skills,Marge_horizontale(),Affichage_classes_ferme(self.classe),Marge_horizontale()],[5,0,5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_classes(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(),Affichage_intrasecs_ferme(self.classe),Marge_horizontale(),Affichage_skills_ferme(self.classe),Marge_horizontale(),self.classes,Marge_horizontale()],[5,0,5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_intrasecs_ferme): #On veut ouvrir l'affichage des stats
                self.init_intrasecs()
            if isinstance(clique,Affichage_skills_ferme): #On veut ouvrir l'affichage des stats
                self.init_skills()
            if isinstance(clique,Affichage_classes_ferme): #On veut ouvrir l'affichage des stats
                self.init_classes()
            self.set_tailles(self.tailles)
        else:
            # self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_intrasecs_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(),Texte("Compétences intrasèques"),Marge_horizontale()],[5,0,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_intrasecs(Wrapper):
    def __init__(self,classe:Classe):
        self.classe = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        
        self.liste_skills = Liste_verticale()
        self.skills = [Affichage_skill(skill) for skill in self.classe.skills_intrasecs]
        self.liste_skills.set_contenu([self.skills[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.skills)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.skills)*2)])

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_skills,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        i=0
        skills = self.classe.skills_intrasecs
        while i < len(skills) or i < len(self.skills):
            if i == len(skills) or i == len(self.skills) or skills[i] != self.skills[i].skill: #Les deux ne correspondent pas
                if i == len(self.skills) or self.skills[i].skill in skills: #Donc le skill n'a pas été retiré, mais d'autres ont été ajoutés avant
                    skill = Affichage_skill(skills[i])
                    self.skills.insert(i,skill)
                    self.liste_skills.insert(2*i,skill,0)
                    self.liste_skills.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #le skill qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.skills.pop(i)
                    self.liste_skills.pop(2*i) # La marge avant l'item
                    self.liste_skills.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres skills à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_skills_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(),Pave("Compétences propres"),Marge_horizontale()],[5,0,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_skills(Wrapper):
    def __init__(self,classe:Classe):
        self.classe = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        
        self.liste_skills = Liste_verticale()
        self.skills = [Affichage_skill(skill) for skill in self.classe.skills]
        self.liste_skills.set_contenu([self.skills[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.skills)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.skills)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_skills,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        i=0
        skills = self.classe.skills
        while i < len(skills) or i < len(self.skills):
            if i == len(skills) or i == len(self.skills) or skills[i] != self.skills[i].skill: #Les deux ne correspondent pas
                if i == len(self.skills) or self.skills[i].skill in skills: #Donc le skill n'a pas été retiré, mais d'autres ont été ajoutés avant
                    skill = Affichage_skill(skills[i])
                    self.skills.insert(i,skill)
                    self.liste_skills.insert(2*i,skill,0)
                    self.liste_skills.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #le skill qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.skills.pop(i)
                    self.liste_skills.pop(2*i) # La marge avant l'item
                    self.liste_skills.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres skills à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_classes_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(),Pave("Sous-classes"),Marge_horizontale()],[5,0,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_classes(Wrapper):
    def __init__(self,classe:Classe):
        self.classe = classe
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        
        self.liste_classes = Liste_verticale()
        self.classes = [Affichage_classe(classe) for classe in self.classe.sous_classes]
        self.liste_classes.set_contenu([self.classes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.classes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.classes)*2)])
        
        self.init()

    def init(self):
        self.courant = True
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_classes,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_sous_classe(self):
        for i in range(len(self.classes)):
            if self.classes[i] != self.courant:
                if isinstance(self.classes[i],Affichage_sous_classe):
                    self.classe[i] = Affichage_classe(self.classes[i].classe)
                    self.liste_classes.replace(2*i+1,self.classes[i],0)
            else:
                self.classe[i] = Affichage_sous_classe(self.classes[i].classe)
                self.liste_classes.replace(2*i+1,self.classes[i],0)
                self.courant = self.classe[i]

        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_classes,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_classe):
                self.courant = clique
                self.init_sous_classe()
            self.set_tailles(self.tailles)
        else:
            # self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

    def update(self):
        i=0
        classes = self.classe.sous_classes
        while i < len(classes) or i < len(self.classes):
            if i == len(classes) or i == len(self.classes) or classes[i] != self.classes[i].classe: #Les deux ne correspondent pas
                if i == len(self.classes) or self.classes[i].classe in classes: #Donc la classe n'a pas été retiré, mais d'autres ont été ajoutés avant
                    classe = Affichage_classe(classes[i])
                    self.classes.insert(i,classe)
                    self.liste_classes.insert(2*i,classe,0)
                    self.liste_classes.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #la classe qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.classes.pop(i)
                    self.liste_classes.pop(2*i) # La marge avant l'item
                    self.liste_classes.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres classes à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_allies(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        
        self.liste_allies = Liste_verticale()
        self.allies = [Vignette_allie([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus()]
        self.liste_allies.set_contenu([self.allies[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.allies)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.allies)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_allies,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        i=0
        allies = self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus()
        while i < len(allies) or i < len(self.allies):
            if i == len(allies) or i == len(self.allies) or allies[i] != self.allies[i].agissant.ID: #Les deux ne correspondent pas
                if i == len(self.allies) or self.allies[i].agissant.ID in allies: #Donc l'allie n'a pas été retiré, mais d'autres ont été ajoutés avant
                    allie = Vignette_allie([0,0],self.controleur[allies[i]],self.controleur.joueur.esprit,40)
                    self.allies.insert(i,allie)
                    self.liste_allies.insert(2*i,allie,0)
                    self.liste_allies.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #l'allie qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.allies.pop(i)
                    self.liste_allies.pop(2*i) # La marge avant l'item
                    self.liste_allies.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres allies à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_allie):
                self.courant = clique
                return clique
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_ennemis(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        
        self.liste_ennemis = Liste_verticale()
        self.ennemis = [Vignette_ennemi([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus()]
        self.liste_ennemis.set_contenu([self.ennemis[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.ennemis)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.ennemis)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_ennemis,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        i=0
        ennemis = self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus()
        while i < len(ennemis) or i < len(self.ennemis):
            if i == len(ennemis) or i == len(self.ennemis) or ennemis[i] != self.ennemis[i].agissant.ID: #Les deux ne correspondent pas
                if i == len(self.ennemis) or self.ennemis[i].agissant.ID in ennemis: #Donc l'ennemi n'a pas été retiré, mais d'autres ont été ajoutés avant
                    ennemi = Vignette_ennemi([0,0],self.controleur[ennemis[i]],self.controleur.joueur.esprit,40)
                    self.ennemis.insert(i,ennemi)
                    self.liste_ennemis.insert(2*i,ennemi,0)
                    self.liste_ennemis.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #l'ennemi qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.ennemis.pop(i)
                    self.liste_ennemis.pop(2*i) # La marge avant l'item
                    self.liste_ennemis.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres ennemis à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
                return clique
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_neutres(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        
        self.liste_neutres = Liste_verticale()
        self.neutres = [Vignette_neutre([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus()]
        self.liste_neutres.set_contenu([self.neutres[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(self.neutres)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(self.neutres)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(),self.liste_neutres,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        i=0
        neutres = self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus()
        while i < len(neutres) or i < len(self.neutres):
            if i == len(neutres) or i == len(self.neutres) or neutres[i] != self.neutres[i].agissant.ID: #Les deux ne correspondent pas
                if i == len(self.neutres) or self.neutres[i].agissant.ID in neutres: #Donc l'neutre n'a pas été retiré, mais d'autres ont été ajoutés avant
                    neutre = Vignette_neutre([0,0],self.controleur[neutres[i]],self.controleur.joueur.esprit,40)
                    self.neutres.insert(i,neutre)
                    self.liste_neutres.insert(2*i,neutre,0)
                    self.liste_neutres.insert(2*i,Marge_horizontale(),5)
                    i+=1
                else: #l'neutre qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.neutres.pop(i)
                    self.liste_neutres.pop(2*i) # La marge avant l'item
                    self.liste_neutres.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres neutres à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_neutre):
                self.courant = clique
                return clique
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_allies_agissant_dialogue(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_allie([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus()]
        liste.set_contenu([allies[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(allies)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(allies)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_allie):
                self.courant = clique
                self.cible = clique.agissant.ID
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_ennemis_agissant_dialogue(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        ennemis = [Vignette_ennemi([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus()]
        liste.set_contenu([ennemis[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(ennemis)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(ennemis)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
                self.cible = clique.agissant.ID
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_neutres_agissant_dialogue(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        neutres = [Vignette_neutre([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus()]
        liste.set_contenu([neutres[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(neutres)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(neutres)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_neutre):
                self.courant = clique
                self.cible = clique.agissant.ID
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_allies_agissant_magie(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie,Multi_cible):
            self.cible = []
        else:
            self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_allie([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible and not(isinstance(self.joueur.magie,Multi_cible) and ID in self.cible)) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus()]
        liste.set_contenu([allies[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(allies)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(allies)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_allie):
                self.courant = clique
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    if clique.agissant.ID in self.cible:
                        self.cible.remove(clique.agissant.ID)
                    else:
                        self.cible.append(clique.agissant.ID)
                else:
                    if clique.agissant.ID != self.cible:
                        self.cible = clique.agissant.ID
                    else:
                        self.cible = None
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_ennemis_agissant_magie(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie,Multi_cible):
            self.cible = []
        else:
            self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        ennemis = [Vignette_ennemi([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible and not(isinstance(self.joueur.magie,Multi_cible) and ID in self.cible)) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus()]
        liste.set_contenu([ennemis[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(ennemis)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(ennemis)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    if clique.agissant.ID in self.cible:
                        self.cible.remove(clique.agissant.ID)
                    else:
                        self.cible.append(clique.agissant.ID)
                else:
                    if clique.agissant.ID != self.cible:
                        self.cible = clique.agissant.ID
                    else:
                        self.cible = None
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_neutres_agissant_magie(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie,Multi_cible):
            self.cible = []
        else:
            self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        neutres = [Vignette_neutre([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible and not(isinstance(self.joueur.magie,Multi_cible) and ID in self.cible)) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus()]
        liste.set_contenu([neutres[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(neutres)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(neutres)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_neutre):
                self.courant = clique
                if isinstance(self.controleur.joueur.magie,Multi_cible):
                    if clique.agissant.ID in self.cible:
                        self.cible.remove(clique.agissant.ID)
                    else:
                        self.cible.append(clique.agissant.ID)
                else:
                    if clique.agissant.ID != self.cible:
                        self.cible = clique.agissant.ID
                    else:
                        self.cible = None
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_allies_agissant_parchemin(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
            self.cible = []
        else:
            self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_allie([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible and not(isinstance(self.joueur.magie_parchemin,Multi_cible) and ID in self.cible)) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus()]
        liste.set_contenu([allies[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(allies)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(allies)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_allie):
                self.courant = clique
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    if clique.agissant.ID in self.cible:
                        self.cible.remove(clique.agissant.ID)
                    else:
                        self.cible.append(clique.agissant.ID)
                else:
                    if clique.agissant.ID != self.cible:
                        self.cible = clique.agissant.ID
                    else:
                        self.cible = None
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_ennemis_agissant_parchemin(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
            self.cible = []
        else:
            self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        ennemis = [Vignette_ennemi([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible and not(isinstance(self.joueur.magie_parchemin,Multi_cible) and ID in self.cible)) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus()]
        liste.set_contenu([ennemis[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(ennemis)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(ennemis)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    if clique.agissant.ID in self.cible:
                        self.cible.remove(clique.agissant.ID)
                    else:
                        self.cible.append(clique.agissant.ID)
                else:
                    if clique.agissant.ID != self.cible:
                        self.cible = clique.agissant.ID
                    else:
                        self.cible = None
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_neutres_agissant_parchemin(Wrapper):
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.objets:List[Affichable] = []
        self.contenu:Affichable = None
        self.courant = False
        if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
            self.cible = []
        else:
            self.cible = None
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        neutres = [Vignette_neutre([0,0],self.controleur[ID],self.controleur.joueur.esprit,40,self.cible and ID != self.cible and not(isinstance(self.joueur.magie_parchemin,Multi_cible) and ID in self.cible)) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus()]
        liste.set_contenu([neutres[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(neutres)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(neutres)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            pass
        elif clique:
            if isinstance(clique,Vignette_neutre):
                self.courant = clique
                if isinstance(self.controleur.joueur.magie_parchemin,Multi_cible):
                    if clique.agissant.ID in self.cible:
                        self.cible.remove(clique.agissant.ID)
                    else:
                        self.cible.append(clique.agissant.ID)
                else:
                    if clique.agissant.ID != self.cible:
                        self.cible = clique.agissant.ID
                    else:
                        self.cible = None
            return self
        else:
            # self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_PV(Affichable):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.position = [0,0]
        self.tailles = [0,10]

    def affiche(self,screen,frame,frame_par_tour):
        pygame.draw.rect(screen,(255,160,160),(self.position[0],self.position[1],self.tailles[0],10))
        pygame.draw.rect(screen,(255,0,0),(self.position[0],self.position[1],(self.tailles[0]*self.joueur.pv)//self.joueur.pv_max,10))

    def get_tailles(self,tailles):
        return [tailles[0],self.tailles[1]]

class Affichage_PM(Affichable):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.position = [0,0]
        self.tailles = [0,10]

    def affiche(self,screen,frame,frame_par_tour):
        pygame.draw.rect(screen,(160,255,255),(self.position[0],self.position[1],self.tailles[0],10))
        pygame.draw.rect(screen,(32,255,255),(self.position[0],self.position[1],(self.tailles[0]*self.joueur.pm)//self.joueur.pm_max,10))

    def get_tailles(self,tailles):
        return [tailles[0],self.tailles[1]]

class Affichage_PM_cout(Affichable):
    def __init__(self,joueur:Agissant):
        self.joueur = joueur
        self.position = [0,0]
        self.tailles = [0,10]
        self.cout = 0

    def affiche(self,screen,frame,frame_par_tour):
        pygame.draw.rect(screen,(160,255,255),(self.position[0],self.position[1],self.tailles[0],10))
        pygame.draw.rect(screen,(32,255,255),(self.position[0],self.position[1],(self.tailles[0]*self.joueur.pm)//self.joueur.pm_max,10))
        pygame.draw.rect(screen,(32,255,255),(self.position[0],self.position[1],(self.tailles[0]*(self.joueur.pm-self.cout))//self.joueur.pm_max,10))

    def get_tailles(self,tailles):
        return [tailles[0],self.tailles[1]]

    def clique(self,position):
        if self.touche(position):
            proportion = (position[0]-self.position[0])/self.tailles[0]
            pm = int(self.joueur.pm_max*proportion)
            cout = self.joueur.pm - pm
            if cout > 0:
                self.cout = cout
            return self
        return False

class Titre(Affichable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self,controleur:Controleur):
        self.controleur = controleur
        self.tailles = [0,40]
        self.position = [0,0]

    def affiche(self,screen,frame=1,frame_par_tour=1):
        texte = self.controleur.joueur.position.lab
        if self.controleur.phase == TOUR and self.controleur.pause:
            texte+=" - (en pause)"
        elif self.controleur.phase == DIALOGUE:
            texte+=" - dialogue"
        elif self.controleur.phase == TOUCHE:
            texte="Modification des touches"
        texte=POLICE40.render(texte,True,(255,255,255))
        screen.blit(texte,self.position)

class Affichage_perso(Proportionnel):
    def __init__(self,perso):
        self.perso = perso
        self.tailles = [0,0]
        self.position = [0,0]
        self.proportions = [3,4]

    def affiche(self,screen,frame,frame_par_tour):
        position = self.perso.position #/!\ Peut poser problème
        x = self.position[0]
        y = self.position[1]
        largeur = self.tailles[0]
        hauteur = self.tailles[1]
        direction = self.perso.dir_regard-2
        joueur = self.perso.controleur.joueur

        # Version plus jolie :
        skins = []
        for distance in range(PROFONDEUR_DE_CHAMP): #On ne va pas plus loin que ça pour l'instant
            pos_case_centre = position + direction*distance
            if pos_case_centre in joueur.vue:
                case = joueur.vue[pos_case_centre]
                if case[1] == -1:
                    skins.append(SKINS_CASES_NOIRES_VUES[distance][0])
                elif case[1] > 0:
                    skins.append(SKINS_CASES_VUES[distance][0])
                    if not case[5][direction][4]:
                        skins.append(SKINS_MURS_FACE_VUS[distance][0])
                    else:
                        traj = joueur.controleur.get_trajet(case[0],direction)
                        if traj == "escalier bas":
                            skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][0])
                        elif traj == "escalier haut":
                            skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][0])
                    if not case[5][direction-1][4]:
                        skins.append(SKINS_MURS_VUS[distance][0][0])
                    else:
                        traj = joueur.controleur.get_trajet(case[0],direction-1)
                        if traj == "escalier bas":
                            skins.append(SKINS_ESCALIERS_BAS_VUS[distance][0][0])
                        elif traj == "escalier haut":
                            skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][0][0])
                    if not case[5][direction-3][4]:
                        skins.append(SKINS_MURS_VUS[distance][0][1])
                    else:
                        traj = joueur.controleur.get_trajet(case[0],direction-3)
                        if traj == "escalier bas":
                            skins.append(SKINS_ESCALIERS_BAS_VUS[distance][0][1])
                        elif traj == "escalier haut":
                            skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][0][1])
            for ecart_ in range(distance//2+1):
                ecart = ecart_+1
                pos_case_droite = pos_case_centre + (direction+1)*ecart #À droite du point de vue du joueur
                if pos_case_droite in joueur.vue:
                    case = joueur.vue[pos_case_droite]
                    if case[1] == -1:
                        skins.append(SKINS_CASES_NOIRES_VUES[distance][ecart])
                    elif case[1] > 0:
                        skins.append(SKINS_CASES_VUES[distance][ecart])#Rajouter les affinités etc. plus tard
                        if not case[5][direction][4]:
                            skins.append(SKINS_MURS_FACE_VUS[distance][ecart])#Rajouter aussi les distinctions des téléportations
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][ecart])
                        if not case[5][direction-3][4]:
                            skins.append(SKINS_MURS_VUS[distance][ecart])#Pareil
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction-3)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][ecart])
                pos_case_droite = pos_case_centre + (direction-1)*ecart #À droite du point de vue du joueur
                if pos_case_droite in joueur.vue:
                    case = joueur.vue[pos_case_droite]
                    ecart = -ecart
                    if case[1] == -1:
                        skins.append(SKINS_CASES_NOIRES_VUES[distance][ecart])
                    elif case[1] > 0:
                        skins.append(SKINS_CASES_VUES[distance][ecart])
                        if not case[5][direction][4]:
                            skins.append(SKINS_MURS_FACE_VUS[distance][ecart])
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][ecart])
                        if not case[5][direction-1][4]:
                            skins.append(SKINS_MURS_VUS[distance][ecart])
                        else:
                            traj = joueur.controleur.get_trajet(case[0],direction-1)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][ecart])
        skins.reverse()
        for skin in skins:
            skin.dessine_toi(screen,(x,y),(largeur,hauteur),frame,frame_par_tour)

        for ID in joueur.vue[position][6]:
            if ID < 11:
                entitee = joueur.controleur[ID]
                if issubclass(entitee.get_classe(),Agissant):
                    for skin in entitee.get_skins_vue():
                        skin.dessine_toi(screen,(x,y),(largeur,hauteur),frame,frame_par_tour)
                    break

class Affichage_labyrinthe(Final,Affichage,Proportionnel):
    def __init__(self,joueur:Agissant):
        self.objets:List[Affichable] = []
        self.position=[0,0]
        self.tailles=[0,0]
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1,1]

    def set_tailles(self,tailles):
        self.tailles = tailles
        self.update()

    def update(self):
        if self.joueur.vue != None:
            self.objets = []
            decs = [[dec.x,dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs,key=itemgetter(0))[0],max(decs,key=itemgetter(0))[0],min(decs,key=itemgetter(1))[1],max(decs,key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0],visible[1]-self.joueur.position.x,self.joueur.position.y-visible[2],visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
            debut_vue = self.joueur.position + distance * (HAUT + GAUCHE)
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut_vue + Decalage(i,j)
                    position = [marge_gauche,marge_haut]
                    self.objets.append(Vignettes_position(position,self.joueur,self.joueur.vue,pos,taille_case))
                    marge_gauche += taille_case
                marge_haut += taille_case
        else:
            for objet in self.objets:
                objet.update()

class Affichage_labyrinthe_case_dialogue(Affichage,Proportionnel):
    def __init__(self,joueur:Agissant):
        self.objets:List[Affichable] = []
        self.position=[0,0]
        self.tailles=[0,0]
        self.cible = None
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1,1]
        self.courant = False

    def set_tailles(self,tailles):
        self.tailles = tailles
        if self.joueur.vue != None:
            self.objets:List[Affichable] = []
            decs = [[dec.x,dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs,key=itemgetter(0))[0],max(decs,key=itemgetter(0))[0],min(decs,key=itemgetter(1))[1],max(decs,key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0],visible[1]-self.joueur.position.x,self.joueur.position.y-visible[2],visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
            debut_vue = self.joueur.position + distance * (HAUT + GAUCHE)
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut_vue + Decalage(i,j)
                    position = [marge_gauche,marge_haut]
                    self.objets.append(Vignettes_position(position,self.joueur,self.joueur.vue,pos,taille_case,self.cible != None and self.cible != pos))
                    marge_gauche += taille_case
                marge_haut += taille_case

    def update(self):
        for objet in self.objets:
            objet.update()

    def clique_wrapper(self,position): #Pas techniquement un wrapper
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        for objet in self.objets:
            res_objet = objet.clique(position)
            if res_objet:
                res = res_objet
        return res

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignettes_position):
                if clique.pos != self.cible:
                    self.cible = clique.pos
                else:
                    self.cible = None
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_labyrinthe_case_magie(Affichage,Proportionnel):
    def __init__(self,joueur:Agissant):
        self.objets:List[Affichable] = []
        self.position=[0,0]
        self.tailles=[0,0]
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1,1]
        self.courant = False
        if isinstance(self.joueur.magie,Multi_cible):
            self.cible = []
        else:
            self.cible = None

    def set_tailles(self,tailles):
        self.tailles = tailles
        if self.joueur.vue != None:
            cibles = self.controleur.get_cibles_potentielles_cases(self.joueur.magie,self.joueur)
            self.objets:List[Affichable] = []
            decs = [[dec.x,dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs,key=itemgetter(0))[0],max(decs,key=itemgetter(0))[0],min(decs,key=itemgetter(1))[1],max(decs,key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0],visible[1]-self.joueur.position.x,self.joueur.position.y-visible[2],visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
            debut_vue = self.joueur.position + distance * (HAUT + GAUCHE)
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut_vue + Decalage(i,j)
                    position = [marge_gauche,marge_haut]
                    self.objets.append(Vignettes_position(position,self.joueur,self.joueur.vue,pos,taille_case),self.cible and pos != self.cible and not(isinstance(self.joueur.magie,Multi_cible) and pos in self.cible), pos not in cibles)
                    marge_gauche += taille_case
                marge_haut += taille_case

    def update(self):
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignettes_position) and not clique.invalide:
                if isinstance(self.joueur.magie,Multi_cible):
                    if clique.pos in self.cible:
                        self.cible.remove(clique.pos)
                    else:
                        self.cible.append(clique.pos)
                else:
                    if clique.pos != self.cible:
                        self.cible = clique.pos
                    else:
                        self.cible = None
                self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_labyrinthe_case_parchemin(Affichage,Proportionnel):
    def __init__(self,joueur:Agissant):
        self.objets:List[Affichable] = []
        self.position=[0,0]
        self.tailles=[0,0]
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1,1]
        self.courant = False
        if isinstance(self.joueur.magie_parchemin,Multi_cible):
            self.cible = []
        else:
            self.cible = None

    def set_tailles(self,tailles):
        self.tailles = tailles
        if self.joueur.vue != None:
            cibles = self.controleur.get_cibles_potentielles_cases(self.joueur.magie,self.joueur)
            self.objets:List[Affichable] = []
            decs = [[dec.x,dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs,key=itemgetter(0))[0],max(decs,key=itemgetter(0))[0],min(decs,key=itemgetter(1))[1],max(decs,key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0],visible[1]-self.joueur.position.x,self.joueur.position.y-visible[2],visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
            debut_vue = self.joueur.position + distance * (HAUT + GAUCHE)
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut_vue + Decalage(i,j)
                    position = [marge_gauche,marge_haut]
                    self.objets.append(Vignettes_position(position,self.joueur,self.joueur.vue,pos,taille_case),self.cible and pos != self.cible and not(isinstance(self.joueur.magie_parchemin,Multi_cible) and pos in self.cible), pos not in cibles)
                    marge_gauche += taille_case
                marge_haut += taille_case

    def update(self):
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignettes_position) and not clique.invalide:
                if isinstance(self.joueur.magie_parchemin,Multi_cible):
                    if clique.pos in self.cible:
                        self.cible.remove(clique.pos)
                    else:
                        self.cible.append(clique.pos)
                else:
                    if clique.pos != self.cible:
                        self.cible = clique.pos
                    else:
                        self.cible = None
                self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_labyrinthe_direction_magie(Affichage,Proportionnel):
    def __init__(self,joueur:Agissant):
        self.objets:List[Affichable] = []
        self.position=[0,0]
        self.tailles=[0,0]
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1,1]
        self.courant = False
        self.direction = HAUT

    def set_tailles(self,tailles):
        self.tailles = tailles
        if self.joueur.vue != None:
            position_magie = [self.position[0]+tailles[0]//2,self.position[1]+tailles[1]//2]
            if isinstance(self.joueur.magie,Magie_cible_dirigee):
                pos_magie = self.joueur.cible_magie
            else:
                pos_magie = self.joueur.position
            self.objets:List[Affichable] = []
            decs = [[dec.x,dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs,key=itemgetter(0))[0],max(decs,key=itemgetter(0))[0],min(decs,key=itemgetter(1))[1],max(decs,key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0],visible[1]-self.joueur.position.x,self.joueur.position.y-visible[2],visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
            debut_vue = self.joueur.position + distance * (HAUT + GAUCHE)
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut_vue + Decalage(i,j)
                    position = [marge_gauche,marge_haut]
                    self.objets.append(Vignettes_position(position,self.joueur,self.joueur.vue,pos,taille_case))
                    if pos == pos_magie:
                        position_magie = position
                    marge_gauche += taille_case
                marge_haut += taille_case
            self.objets.append(Vignette(position_magie,taille_case,SKIN_DIRECTION,self.direction))

    def update(self):
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignettes_position):
                if isinstance(self.joueur.magie,Magie_cible_dirigee):
                    pos_magie = self.joueur.cible_magie
                else:
                    pos_magie = self.joueur.position
                decalage = pos_magie-clique.pos
                if abs(decalage.x) > abs(decalage.y):
                    if decalage.x<0:
                        self.direction = HAUT
                    else:
                        self.direction = BAS
                elif abs(decalage.x) < abs(decalage.y):
                    if decalage.y<0:
                        self.direction = GAUCHE
                    else:
                        self.direction = DROITE
                self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_labyrinthe_direction_parchemin(Affichage,Proportionnel):
    def __init__(self,joueur:Agissant):
        self.objets:List[Affichable] = []
        self.position=[0,0]
        self.tailles=[0,0]
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1,1]
        self.courant = False
        self.direction = HAUT

    def set_tailles(self,tailles):
        self.tailles = tailles
        if self.joueur.vue != None:
            position_magie = [self.position[0]+tailles[0]//2,self.position[1]+tailles[1]//2]
            if isinstance(self.joueur.magie_parchemin,Magie_cible_dirigee):
                pos_magie = self.joueur.cible_magie_parchemin
            else:
                pos_magie = self.joueur.position
            self.objets:List[Affichable] = []
            decs = [[dec.x,dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs,key=itemgetter(0))[0],max(decs,key=itemgetter(0))[0],min(decs,key=itemgetter(1))[1],max(decs,key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0],visible[1]-self.joueur.position.x,self.joueur.position.y-visible[2],visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
            debut_vue = self.joueur.position + distance * (HAUT + GAUCHE)
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = debut_vue + Decalage(i,j)
                    position = [marge_gauche,marge_haut]
                    self.objets.append(Vignettes_position(position,self.joueur,self.joueur.vue,pos,taille_case))
                    if pos == pos_magie:
                        position_magie = position
                    marge_gauche += taille_case
                marge_haut += taille_case
            self.objets.append(Vignette(position_magie,taille_case,SKIN_DIRECTION,self.direction))

    def update(self):
        for objet in self.objets:
            objet.update()

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignettes_position):
                if isinstance(self.joueur.magie_parchemin,Magie_cible_dirigee):
                    pos_magie = self.joueur.cible_magie_parchemin
                else:
                    pos_magie = self.joueur.position
                decalage = pos_magie-clique.pos
                if abs(decalage.x) > abs(decalage.y):
                    if decalage.x<0:
                        self.direction = HAUT
                    else:
                        self.direction = BAS
                elif abs(decalage.x) < abs(decalage.y):
                    if decalage.y<0:
                        self.direction = GAUCHE
                    else:
                        self.direction = DROITE
                self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Vignette_categorie(Final,Affichage):
    def __init__(self,categorie,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.categorie = categorie
        self.objets.append(Vignette([0,0],taille,categorie.get_image()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))

class Vignette_recette(Final,Affichage):
    def __init__(self,recette,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.recette = recette
        self.objets.append(Vignette([0,0],taille,eval(recette["produit"])(None).get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))

class Vignette_ingredient(Final,Affichage):
    def __init__(self,ingredient:Item,quantite_necessaire,quantite_disponible,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.ingredient = ingredient
        self.objets.append(Vignette([0,0],taille,ingredient.get_skin()))
        if shade or invalide or quantite_disponible < quantite_necessaire:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide or quantite_disponible < quantite_necessaire:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        texte = Texte(f"{quantite_disponible}/{quantite_necessaire}")
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.position[0]+self.tailles[0]-tailles_texte[0],self.position[1]+self.tailles[1]-tailles_texte[1]])

class Vignette_vente(Final,Affichage):
    def __init__(self,item:Item,taille,prix,description,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.item = item
        self.prix = prix
        self.description = description
        self.objets.append(Vignette([0,0],taille,item.get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        texte = Texte(f"{prix} €")
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.position[0]+self.tailles[0]-tailles_texte[0],self.position[1]+self.tailles[1]-tailles_texte[1]])

class Vignette_achat(Final,Affichage):
    def __init__(self,item:Item,taille,prix,description,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.item = item
        self.prix = prix
        self.description = description
        self.objets.append(Vignette([0,0],taille,item.get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        texte = Texte(f"{prix} €")
        self.objets.append(texte)
        tailles_texte = texte.get_tailles(self.tailles)
        texte.set_position([self.position[0]+self.tailles[0]-tailles_texte[0],self.position[1]+self.tailles[1]-tailles_texte[1]])

class Vignette_magie(Final,Affichage):
    def __init__(self,magie:Magie,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = [0,0]
        self.magie = magie
        self.objets.append(Vignette([0,0],taille,magie.get_skin()))
        if shade or invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette([0,0],taille,SKIN_SHADE))

class Vignette_item(Final,Affichage):
    def __init__(self,position,item:Item,taille,direction=None,shade=False,invalide=False):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = position
        self.item = item
        if direction == None:
            direction = item.get_direction()
        self.objets.append(Vignette(position,taille,item.get_skin(),direction)) #Avoir éventuellement la tête dans une autre direction ?
        for effet in item.effets:
            if effet.affiche:
                self.objets.append(Vignette(position,taille,effet.get_skin(),direction))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Vignettes_agissant(Final,Affichage):
    def __init__(self,position,agissant:Agissant,taille):
        self.objets:List[Affichable] = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        direction = agissant.get_direction()
        arme = agissant.inventaire.arme
        if arme != None:
            self.objets.append(Vignette_item(position,agissant.controleur[arme],taille,direction))
        self.objets.append(Vignette(position,taille,agissant.get_skin(),direction))
        armure = agissant.inventaire.armure
        if armure != None:
            self.objets.append(Vignette_item(position,agissant.controleur[armure],taille,direction))
        bouclier = agissant.inventaire.bouclier
        if bouclier != None:
            self.objets.append(Vignette_item(position,agissant.controleur[bouclier],taille,direction))
        haume = agissant.inventaire.haume
        self.objets.append(Vignette(position,taille,agissant.get_skin_tete(),direction)) #Avoir éventuellement la tête dans une autre direction ?
        if haume != None:
            self.objets.append(Vignette_item(position,agissant.controleur[haume],taille,direction))
        for effet in agissant.effets:
            if effet.affiche:
                self.objets.append(Vignette(position,taille,effet.get_skin(),direction))
        esprit = agissant.controleur.get_esprit(agissant.controleur.joueur.esprit)
        position_pv = [position[0]+ceil(taille*(2/19)),position[1]+ceil(taille*(2/19))]
        tailles_pv = [ceil(taille*((15*agissant.pv)/(19*agissant.pv_max))),ceil(taille*(15/19))]
        if agissant.ID in esprit.ennemis.keys():
            image = IMAGE_PV_ENNEMI
        elif agissant.ID in esprit.corps.keys():
            image = IMAGE_PV_ALLIE
        else:
            image = IMAGE_PV_NEUTRE
        self.objets.append(Vignette_image(position_pv,tailles_pv,image))
        if isinstance(agissant,Humain) and agissant.dialogue > 0: #Est-ce qu'on veut vraiment avoir cet indicatif au-dessus des effets ?
            self.objets.append(Vignette(position,taille,SKIN_DIALOGUE))

class Vignettes_position(Final,Affichage):
    def __init__(self,position,joueur,vue,pos,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.pos = pos
        self.invalide = invalide
        if pos in vue:
            self.objets.append(Vignette_case(position,joueur,vue,pos,taille))
            if vue[pos][1]>0:
                entitees = vue[pos][6]
                agissant = None
                for ID_entitee in entitees:
                    entitee = joueur.controleur[ID_entitee]
                    if issubclass(entitee.get_classe(),Item):
                        self.objets.append(Vignette_item(position,entitee,taille)) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                    elif issubclass(entitee.get_classe(),Decors):
                        self.objets.append(Vignette(position,taille,entitee.get_skin()))
                    else:
                        agissant = entitee
                if agissant != None: #Enfin l'agissant (s'il y en a un)
                    self.objets.append(Vignettes_agissant(position,agissant,taille))
                if vue[pos][7] != []:
                    esprit = joueur.controleur.get_esprit(joueur.esprit)
                    if any([effet[2] in esprit.corps.keys() for effet in vue[pos][7]]):
                        self.objets.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE_ALLIE))
                    else:
                        self.objets.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE))
        else:
            self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Vignette_case(Final,Affichage):
    def __init__(self,position,joueur,vue,pos,taille):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        if pos in vue:
            vue_case = vue[pos]
            if vue_case[1]==0:
                self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
            elif vue_case[1]==-1: #On a affaire à une case accessible mais pas vue
                self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
                for i in DIRECTIONS:
                    if vue_case[5][i][0]:
                        pos_voisin = vue_case[0]+i
                        if pos_voisin in vue and vue[pos_voisin][1]>0:
                            self.objets.append(Vignette(position,taille,SKIN_MUR_BROUILLARD,i))
            else:
                if vue_case[4]==0: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE)) #La case en premier, donc en bas
                elif vue_case[4]==1: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_1)) #La case en premier, donc en bas
                elif vue_case[4]==2: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_2)) #La case en premier, donc en bas
                elif vue_case[4]==3: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_3)) #La case en premier, donc en bas
                elif vue_case[4]==4: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_4)) #La case en premier, donc en bas
                elif vue_case[4]==5: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_5)) #La case en premier, donc en bas
                elif vue_case[4]==6: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_6)) #La case en premier, donc en bas
                elif vue_case[4]==7: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette(position,taille,SKIN_CASE_7)) #La case en premier, donc en bas
                elif vue_case[4]==8: #On teste le code de la case pour déterminer son image
                    self.objets.append(Vignette([0,0],taille,SKIN_CASE_8)) #La case en premier, donc en bas
                case = joueur.controleur[vue_case[0]]
                for i in DIRECTIONS:
                    mur = case.get_mur_dir(i)
                    for effet in mur.effets:
                        if effet.affiche:
                            if isinstance(effet,Porte) :
                                self.objets.append(Vignette(position,taille,effet.get_skin(joueur.get_clees()),i))
                            elif isinstance(effet,(Mur_plein,Mur_impassable)) :
                                self.objets.append(Vignette(position,taille,effet.get_skin(vue_case[4]),i))
                            else :
                                self.objets.append(Vignette(position,taille,effet.get_skin(),i))
                for effet in case.effets:
                    if effet.affiche:
                        self.objets.append(Vignette(position,taille,effet.get_skin()))
        else:
            self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))

class Vignette_allie(Final,Affichage):
    def __init__(self,position,agissant,esprit,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.objets.append(Vignettes_agissant(position,agissant,taille))
        for statut in agissant.get_skins_statuts():
            self.objets.append(Vignette(position,taille,statut))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Vignette_ennemi(Final,Affichage):
    def __init__(self,position,agissant,esprit,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.objets.append(Vignettes_agissant(position,agissant,taille))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Vignette_neutre(Final,Affichage):
    def __init__(self,position,agissant,esprit,taille,shade=False,invalide=False):
        self.objets:List[Affichable] = []
        self.tailles = [taille,taille]
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.objets.append(Vignettes_agissant(position,agissant,taille))
        if shade or invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))
        if invalide:
            self.objets.append(Vignette(position,taille,SKIN_SHADE))

class Affichage_replique(Pave):
    """Un élément avec beaucoup de texte. S'adapte sur plusieurs lignes si besoin"""
    def __init__(self,texte,replique):
        self.tailles = [0,0]
        self.position = [0,0]
        self.texte = texte
        self.replique = replique
        self.couleur = (0,0,0)
        self.courant = False

    def get_tailles(self,tailles):
        mots = self.texte.split() #On explose sur les espaces
        if self.courant:
            mots.insert(0,"--> ")
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            hauteur += 1
        return [tailles[0],20*hauteur]

    def set_tailles(self,tailles):
        mots = self.texte.split() #On explose sur les espaces
        if self.courant:
            mots.insert(0,"--> ")
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            hauteur += 1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
        self.tailles = [tailles[0],20*hauteur]

    def affiche(self,screen,frame,frame_par_tour):
        """Fonction qui prend en entrée une chaine de caractère et renvoie les surfaces des lignes successives du texte."""
        mots = self.texte.split() #On explose sur les espaces
        if self.courant:
            mots.insert(0,"--> ")
        i = 0
        hauteur = 0
        while i < len(mots):
            ligne = mots[i]
            i+=1
            while i < len(mots) and POLICE20.size(ligne+" "+mots[i])[0] <= self.tailles[0]:
                ligne = ligne + " " + mots[i]
                i+=1
            screen.blit(POLICE20.render(ligne,True,self.couleur),[self.position[0],self.position[1]+hauteur*20])
            hauteur += 1

    def clique(self,position):
        #Trouve l'élément survolé par la souris et le renvoie
        res = False
        if self.touche(position):
            res = self
            self.courant = True
        else:
            self.courant = False
        return res

class Affichage_skill(Final,Pavage_horizontal):
    def __init__(self,skill:Skill_intrasec,fond=(0,0,0)):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
        self.fond = (0,0,0,0)
        self.contenu:List[Affichable] = [None] #Les objets qu'il 'contient'
        self.skill = skill
        self.init()

    def init(self):
        self.set_contenu([Vignette([0,0],20,self.skill.get_skin()),Marge_verticale(),Texte(self.skill.nom)],[0,5,0])

class Affichage_classe(Final,Pavage_horizontal):
    def __init__(self,classe:Classe,fond=(0,0,0)):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.tailles = [0,0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0,0]
        self.fond = (0,0,0,0)
        self.contenu:List[Affichable] = [None] #Les objets qu'il 'contient'
        self.classe = classe
        self.init()

    def init(self):
        self.set_contenu([Vignette([0,0],20,self.classe.get_skin()),Marge_verticale(),Texte(self.classe.nom)],[0,5,0])




from Jeu.Entitee.Decors.Decors import *
from Jeu.Entitee.Item.Item import *
from Jeu.Entitee.Agissant.Humain.Humain import Humain
from Jeu.Effet.Effets_mouvement.Blocages import *
from Jeu.Effet.Effets import *
from Jeu.Systeme.Classe import *