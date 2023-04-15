from typing import Callable
from warnings import warn
from Affichage.Affichage import *

from operator import itemgetter

class Affichage_principal(Wrapper_knot, Knot_horizontal):
    """L'element principal de l'affichage. Contient tout ce qui apparait à l'écran."""
    
    def __init__(self, controleur:Controleur, tailles):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.fond = (0, 0, 0)
        self.tailles = tailles
        self.phase = controleur.phase
        
        self.affichage_gauche = Affichage_gauche(self.controleur.joueur)
        self.affichage_centre = Affichage_centre(self.controleur.joueur)
        self.affichage_droite = Affichage_droite(self.controleur)
        self.gauche = self.affichage_gauche
        self.centre = self.affichage_centre
        self.droite = self.affichage_droite
        self.courant_ = self.affichage_gauche
        self.actif_ = True
        # Le reste peut être généré à chaque fois ?

        self.inits[self.phase](self)

    def init_triptique(self, gauche, centre, droite, courant):
        """Créer l'affichage séparé en trois parties"""
        self.gauche = gauche
        self.centre = centre
        self.droite = droite
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([gauche, Marge_verticale(), centre, Marge_verticale(), droite], [-1, 5, -2, 5, -1])
        diptique.set_contenu([Marge_horizontale(), Titre(self.controleur), Marge_horizontale(), triptique, Marge_horizontale()], [5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_verticale(), diptique, Marge_verticale()], [5, -1, 5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.set_courant(courant)
        self.fond = (0, 0, 0)

    def init_tour(self):
        """Crée l'affichage tel qu'il est pendant les phases de jeu normales"""
        self.init_triptique(self.affichage_gauche, self.affichage_centre, self.affichage_droite, self.courant_)
        self.actif = self.actif_
        
    def init_dialogue(self):
        """Crée l'affichage tel qu'il est pendant les phases de dialogues"""
        droite = Affichage_droite_dialogue(self.controleur.joueur.interlocuteur)
        self.init_triptique(self.affichage_gauche, self.affichage_centre, droite, droite)

    def init_case_dialogue(self):
        centre = Affichage_centre_case_dialogue(self.controleur.joueur)
        droite = Affichage_droite_dialogue(self.controleur.joueur.interlocuteur)
        self.init_triptique(self.affichage_gauche, centre, droite, centre)

    def init_case_magie(self):
        centre = Affichage_centre_case_magie(self.controleur.joueur)
        droite = Affichage_droite(self.controleur.joueur.interlocuteur)
        self.init_triptique(self.affichage_gauche, centre, droite, centre)

    def init_case_parchemin(self):
        centre = Affichage_centre_case_parchemin(self.controleur.joueur)
        droite = Affichage_droite(self.controleur.joueur.interlocuteur)
        self.init_triptique(self.affichage_gauche, centre, droite, centre)

    def init_agissant_dialogue(self):
        gauche = Affichage_droite_dialogue(self.controleur.joueur.interlocuteur)
        droite = Affichage_droite_agissant_cible(self.controleur, False, AGISSANT_DIALOGUE)
        self.init_triptique(gauche, self.affichage_centre, droite, droite)

    def init_agissant_magie(self):
        droite = Affichage_droite_agissant_cible(self.controleur, isinstance(self.controleur.joueur.magie_courante, Multi_cible), AGISSANT_MAGIE)
        self.init_triptique(self.affichage_gauche, self.affichage_centre, droite, droite)

    def init_agissant_parchemin(self):
        droite = Affichage_droite_agissant_cible(self.controleur, isinstance(self.controleur.joueur.magie_parchemin, Multi_cible), AGISSANT_PARCHEMIN)
        self.init_triptique(self.affichage_gauche, self.affichage_centre, droite, droite)

    def init_direction_magie(self):
        centre = Affichage_centre_direction_magie(self.controleur.joueur)
        self.init_triptique(self.affichage_gauche, centre, self.affichage_droite, centre)

    def init_direction_parchemin(self):
        centre = Affichage_centre_direction_parchemin(self.controleur.joueur)
        self.init_triptique(self.affichage_gauche, centre, self.affichage_droite, centre)

    def init_cout_magie(self):
        gauche = Affichage_gauche_cout_magie(self.controleur)
        self.init_triptique(gauche, self.affichage_centre, self.affichage_droite, gauche)

    def init_cout_parchemin(self):
        gauche = Affichage_gauche_cout_parchemin(self.controleur)
        self.init_triptique(gauche, self.affichage_centre, self.affichage_droite, gauche)

    def init_recettes(self):
        gauche = Affichage_gauche_inventaire(self.controleur.joueur)
        centre = Affichage_centre_recettes(self.controleur.joueur)
        droite = Center_texte("Choisis un item à synthétiser.")
        self.init_triptique(gauche, centre, droite, centre)

    def init_recette(self):
        new_droite = Affichage_droite_recette(self.controleur, self.courant.courant)
        contenu: Pavage_horizontal = self.contenu
        diptique: Pavage_vertical = contenu.contenu[1]
        triptique: Pavage_horizontal = diptique.contenu[3]
        triptique.contenu[4] = new_droite
        self.set_courant(new_droite)

    def init_ventes(self):
        menu = Pavage_vertical()
        boutons = Pavage_horizontal()
        onglets = Liste_horizontale()
        onglets.set_contenu([Bouton(SKIN_ACHAT, "Achat"), Marge_verticale(), Bouton(SKIN_VENTE, "Vente")])
        boutons.set_contenu([Marge_verticale(), onglets, Marge_verticale(), Marge_verticale(), Bouton(SKIN_QUITTER, "Quitter"), Marge_verticale()], [5, -1, 5, 0, 5])
        menu.set_contenu([Marge_horizontale(), boutons, Marge_horizontale(), Affichage_centre_ventes(self.controleur.joueur.interlocuteur), Marge_horizontale()], [5, 0, 5, -1, 5])

        gauche = Affichage_gauche_inventaire(self.controleur.joueur)
        centre = menu
        droite = Center_texte("Quel item veux-tu vendre ?")
        self.init_triptique(gauche, centre, droite, centre)

    def init_vente(self):
        new_droite = Affichage_droite_vente(self.controleur, self.courant.courant)
        contenu: Pavage_horizontal = self.contenu
        diptique: Pavage_vertical = contenu.contenu[1]
        triptique: Pavage_horizontal = diptique.contenu[3]
        triptique.contenu[4] = new_droite
        self.set_courant(new_droite)

    def init_achats(self):
        menu = Pavage_vertical()
        boutons = Pavage_horizontal()
        onglets = Liste_horizontale()
        onglets.set_contenu([Bouton(SKIN_ACHAT, "Achat"), Marge_verticale(), Bouton(SKIN_VENTE, "Vente")])
        boutons.set_contenu([Marge_verticale(), onglets, Marge_verticale(), Marge_verticale(), Bouton(SKIN_QUITTER, "Quitter"), Marge_verticale()], [5, -1, 5, 0, 5])
        menu.set_contenu([Marge_horizontale(), boutons, Marge_horizontale(), Affichage_centre_achats(self.controleur.joueur.interlocuteur), Marge_horizontale()], [5, 0, 5, -1, 5])
        
        gauche = Affichage_gauche_inventaire(self.controleur.joueur)
        centre = menu
        droite = Center_texte("Quel item veux-tu acheter ?")
        self.init_triptique(gauche, centre, droite, centre)

    def init_achat(self):
        new_droite = Affichage_droite_achat(self.controleur, self.courant.courant)
        contenu: Pavage_horizontal = self.contenu
        diptique: Pavage_vertical = contenu.contenu[1]
        triptique: Pavage_horizontal = diptique.contenu[3]
        triptique.contenu[4] = new_droite
        self.set_courant(new_droite)

    def init_impregnations(self):
        gauche = Affichage_gauche_inventaire(self.controleur.joueur)
        centre = Affichage_centre_impregnations(self.controleur.joueur)
        droite = Affichage_droite_impregnations(self.controleur, "De quelle magie veux-tu imprégner ce parchemin ?", IMPREGNATION)
        self.init_triptique(gauche, centre, droite, centre)

    def init_impregnation(self):
        new_droite = Affichage_droite_impregnation(self.controleur, self.courant.courant)
        contenu: Pavage_horizontal = self.contenu
        diptique: Pavage_vertical = contenu.contenu[1]
        triptique: Pavage_horizontal = diptique.contenu[3]
        triptique.contenu[4] = new_droite
        self.set_courant(new_droite)

    def init_auto_impregnations(self):
        gauche = Affichage_gauche_inventaire(self.controleur.joueur)
        centre = Affichage_centre_auto_impregnations(self.controleur.joueur)
        droite = Affichage_droite_impregnations(self.controleur, "De quelle magie est-ce que je veux imprégner ce parchemin ?", AUTO_IMPREGNATION)
        self.init_triptique(gauche, centre, droite, centre)
        
    def init_auto_impregnation(self):
        new_droite = Affichage_droite_impregnation(self.controleur, self.courant.courant, auto=True)
        contenu: Pavage_horizontal = self.contenu
        diptique: Pavage_vertical = contenu.contenu[1]
        triptique: Pavage_horizontal = diptique.contenu[3]
        triptique.contenu[4] = new_droite
        self.set_courant(new_droite)

    def update(self):
        if self.phase != self.controleur.phase: #On a changé de phase
            if self.phase == TOUR: # On quitte la phase de jeu "normale"
                self.courant_ = self.courant # On sauvegarde l'objet courant
                self.actif_ = self.actif
            self.phase = self.controleur.phase
            self.inits[self.phase](self)
            self.set_tailles(self.tailles)
        else: #Les autres changements sont gérés au plus proche
            self.contenu.update()
            for objet in self.objets:
                objet.update()

    def bouge_souris(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #On a cliqué sur quelque chose. Vérifions quoi :
            if not self.clique(event.pos):
                # Now that's weird...
                print("Clic sur rien")
        elif event.type == pygame.MOUSEWHEEL: #On a scrollé
            self.scroll(pygame.mouse.get_pos(), 10*event.x, 10*event.y)
        elif event.type == pygame.MOUSEMOTION: #On a bougé la souris
            # On vérifie que la souris est dans la fenêtre
            if event.pos[0] >= 0 and event.pos[0] <= self.tailles[0] and event.pos[1] >= 0 and event.pos[1] <= self.tailles[1]:
                # print("survol")
                self.survol(event.pos)

    def select(self, selection):
        self.set_courant(selection)
        if isinstance(selection, Affichage_centre_recettes):
            self.init_recette()
        if isinstance(selection, Affichage_centre_ventes):
            self.init_vente()
        if isinstance(selection, Affichage_centre_achats):
            self.init_achat()
        if isinstance(selection, Bouton) and selection.texte == "Quitter":
            self.controleur.unset_phase(MARCHAND)
        if isinstance(selection, Affichage_centre_impregnations):
            self.init_impregnation()
        if isinstance(selection, Affichage_centre_auto_impregnations):
            self.init_auto_impregnation()

    def set_default_courant(self):
        self.set_courant(self.centre)

    def in_out(self):
        return self
    
    def in_left(self):
        if self.courant == self.centre:
            self.set_courant(self.gauche)
        elif self.courant == self.droite:
            self.set_courant(self.centre)
        return self

    def in_right(self):
        if self.courant == self.gauche:
            self.set_courant(self.centre)
        elif self.courant == self.centre:
            self.set_courant(self.droite)
        return self

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

class Affichage_gauche(Wrapper_knot, Knot_vertical):
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (255, 255, 255)

        self.stats = Affichage_stats(self.joueur)
        self.inventaire = Affichage_inventaire(self.joueur)
        self.classe = Affichage_sous_classe(self.joueur.classe_principale)
        self.stats_ferme = Affichage_stats_ferme(self.joueur)
        self.inventaire_ferme = Affichage_inventaire_ferme(self.joueur)
        self.classe_ferme = Margin_texte("Classes & compétences")
        self.courant = self.inventaire_ferme

        self.init_gauche()

    def init_gauche(self):
        contenu = Pavage_horizontal()
        triptique = Liste_verticale()
        triptique.set_contenu([Marge_horizontale(), self.stats_ferme, Marge_horizontale(), self.inventaire_ferme, Marge_horizontale(), self.classe_ferme, Marge_horizontale()], [5, 0, 5, 0, 5, 0, 5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu

    def init_stats(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(), self.stats, Marge_horizontale(), self.inventaire_ferme, Marge_horizontale(), self.classe_ferme, Marge_horizontale()], [5, -1, 5, 0, 5, 0, 5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.set_courant(self.stats)

    def init_inventaire(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(), self.stats_ferme, Marge_horizontale(), self.inventaire, Marge_horizontale(), self.classe_ferme, Marge_horizontale()], [5, 0, 5, -1, 5, 0, 5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.set_courant(self.inventaire)

    def init_classe(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(), self.stats_ferme, Marge_horizontale(), self.inventaire_ferme, Marge_horizontale(), self.classe, Marge_horizontale()], [5, 0, 5, 0, 5, -1, 5]) # /!\ Remplacer par Affichage_classe_principale
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.set_courant(self.classe)

    def select(self, selection:bool|Affichable):
        if isinstance(selection, Affichage_stats_ferme): #On veut ouvrir l'affichage des stats
            self.init_stats()
            self.set_tailles(self.tailles)
        if isinstance(selection, Affichage_inventaire_ferme): #On veut ouvrir l'affichage des stats
            self.init_inventaire()
            self.set_tailles(self.tailles)
        if isinstance(selection, Margin_texte) and selection.texte.texte == "Classes & compétences": #On veut ouvrir l'affichage des stats
            self.init_classe()
            self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.inventaire)
        self.init_inventaire()
        self.set_tailles(self.tailles)

    def in_down(self):
        if self.courant is self.stats or self.courant is self.stats_ferme:
            self.init_inventaire()
            self.set_tailles(self.tailles)
        elif self.courant is self.inventaire or self.courant is self.inventaire_ferme:
            self.init_classe()
            self.set_tailles(self.tailles)
        return self

    def in_up(self):
        if self.courant is self.classe or self.courant is self.classe_ferme:
            self.init_inventaire()
            self.set_tailles(self.tailles)
        elif self.courant is self.inventaire or self.courant is self.inventaire_ferme:
            self.init_stats()
            self.set_tailles(self.tailles)
        return self

class Affichage_centre(Wrapper_knot_bloque):
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (0, 0, 0)

        self.labyrinthe = Affichage_labyrinthe_jeu(self.joueur)
        self.courant = self.labyrinthe

        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(), self.labyrinthe, Marge_horizontale()], [5, -1, 5])
        contenu.set_contenu([Marge_verticale(), monoptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (0, 0, 0)

class Affichage_droite(Wrapper_knot, Knot_horizontal):
    def __init__(self, controleur:Controleur):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.fond = (255, 255, 255)

        self.allies = Affichage_agissants(self.controleur, Vignette_allie, self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus)
        self.neutres = Affichage_agissants(self.controleur, Vignette_neutre, self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus)
        self.ennemis = Affichage_agissants(self.controleur, Vignette_ennemi, self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus)
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(), self.allies, Marge_verticale(), self.neutres, Marge_verticale(), self.ennemis, Marge_verticale()], [5, -1, 5, -1, 5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), triptique, Marge_horizontale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def init_agissant(self):
        agissant = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(), self.allies, Marge_verticale(), self.neutres, Marge_verticale(), self.ennemis, Marge_verticale()], [5, -1, 5, -1, 5, -1, 5])
        monoptique.set_contenu([Marge_verticale(), Paves(agissant.get_texte_descriptif()), Marge_verticale()], [5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), triptique, Marge_horizontale(), monoptique, Marge_horizontale()], [5, -1, 5, 0, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Affichage_agissants):
            self.set_courant(selection)
            if self.courant.courant is None:
                self.courant.set_default_courant()
            if self.courant.courant is not None:
                self.init_agissant()
            else:
                self.init_droite()
        if isinstance(selection, Paves):
            self.controleur.get_esprit(self.controleur.joueur.esprit).utilise(self.courant.agissant)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.allies)
        self.init_droite()
        self.set_tailles(self.tailles)

    def in_left(self):
        if self.courant is self.neutres:
            self.select(self.allies)
        elif self.courant is self.ennemis:
            self.select(self.neutres)
        return self

    def in_right(self):
        if self.courant is self.allies:
            self.select(self.neutres)
        elif self.courant is self.neutres:
            self.select(self.ennemis)
        return self

    def update(self):
        if isinstance(self.courant, Affichage_agissants) and not self.courant.courant in self.allies.agissants + self.ennemis.agissants + self.neutres.agissants :
            self.init_droite()
        else:
            if isinstance(self.courant, Vignette_allie):
                self.init_agissant() #Donner des informations spécifiques pour les alliés ?
            if isinstance(self.courant, Vignette_ennemi):
                self.init_agissant() #Donner des informations spécifiques pour les ennemis ?
            if isinstance(self.courant, Vignette_neutre):
                self.init_agissant() #Donner des informations spécifiques pour les neutres ?
        self.set_tailles(self.tailles)
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_gauche_cout_magie(Wrapper_knot_bloque):
    def __init__(self, controleur:Controleur):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.fond = (255, 255, 255)
        self.courant = Affichage_stats_cout_magie(self.controleur)
        self.init_gauche()

    def init_gauche(self):
        contenu = Pavage_horizontal()
        triptique = Liste_verticale()
        triptique.set_contenu([Marge_horizontale(), self.courant, Marge_horizontale(), Affichage_inventaire_ferme(self.controleur.joueur), Marge_horizontale(), Margin_texte("Classes & compétences"), Marge_horizontale()], [5, 0, 5, 0, 5, 0, 5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

class Affichage_gauche_cout_parchemin(Wrapper_knot_bloque):
    def __init__(self, controleur:Controleur):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.fond = (255, 255, 255)
        self.courant = Affichage_stats_cout_magie(self.controleur, cout_parchemin=True)
        self.init_gauche()

    def init_gauche(self):
        contenu = Pavage_horizontal()
        triptique = Liste_verticale()
        triptique.set_contenu([Marge_horizontale(), self.courant, Marge_horizontale(), Affichage_inventaire_ferme(self.controleur.joueur), Marge_horizontale(), Margin_texte("Classes & compétences"), Marge_horizontale()], [5, 0, 5, 0, 5, 0, 5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

class Affichage_gauche_inventaire(Wrapper_knot_bloque):
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (255, 255, 255)
        self.courant = Affichage_inventaire(self.joueur)
        self.init_gauche()

    def init_gauche(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(), Affichage_stats_ferme(self.joueur), Marge_horizontale(), self.courant, Marge_horizontale(), Margin_texte("Classes & compétences"), Marge_horizontale()], [5, 0, 5, -1, 5, 0, 5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

class Affichage_centre_selection_lab(Wrapper_knot, Knot_vertical):
    def __init__(self, joueur: PJ, type_affichage_labyrinthe:type):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.type_affichage_labyrinthe:Type[Affichage_labyrinthe_case_dialogue|Affichage_labyrinthe_case_magie|Affichage_labyrinthe_case_parchemin|Affichage_labyrinthe_direction_magie|Affichage_labyrinthe_direction_parchemin] = type_affichage_labyrinthe
        self.affichage_labyrinthe:Affichable = None
        self.boutons:List[Bouton] = []
        self.cible = None
        self.fond = (0, 0, 0)
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        self.affichage_labyrinthe = self.type_affichage_labyrinthe(self.joueur)
        boutons = Pavage_horizontal()
        self.boutons = [Bouton(SKIN_VALIDER, "Confirmer")]
        boutons.set_contenu([self.boutons[i//2] if i%2==0 else Marge_verticale() for i in range(len(self.boutons)*2)], [0 if i%2==0 else 5 for i in range(len(self.boutons)*2-1)]+[-1])
        diptique.set_contenu([Marge_horizontale(), self.affichage_labyrinthe, Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), diptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (0, 0, 0)

    def select(self, selection):
        if isinstance(selection, self.type_affichage_labyrinthe):
            self.set_courant(selection)
            self.courant.actif = True
            self.cible = self.courant.cible
        if isinstance(selection, Bouton) and selection.texte == "Confirmer":
            if isinstance(self.courant, self.type_affichage_labyrinthe):
                self.joueur.interlocuteur.set_cible(self.cible)
                self.joueur.controleur.unset_phase(CASE_DIALOGUE)
                print(self.joueur.controleur.phases)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.affichage_labyrinthe)

    def in_up(self):
        if isinstance(self.courant, Bouton):
            self.set_courant(self.affichage_labyrinthe)
        return self
    
    def in_down(self):
        if isinstance(self.courant, Affichage_labyrinthe_case_dialogue):
            self.set_courant(self.boutons[0])
        return self
    
    def through_left(self):
        if isinstance(self.courant, Bouton):
            index = self.boutons.index(self.courant)
            if index > 0:
                self.courant.actif = False
                self.set_courant(self.boutons[index-1])
                self.courant.actif = True
        return self

    def through_right(self):
        if isinstance(self.courant, Bouton):
            index = self.boutons.index(self.courant)
            if index < len(self.boutons)-1:
                self.courant.actif = False
                self.set_courant(self.boutons[index+1])
                self.courant.actif = True
        return self

class Affichage_centre_case_dialogue(Affichage_centre_selection_lab):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_lab.__init__(self, joueur, Affichage_labyrinthe_case_dialogue)

class Affichage_centre_case_magie(Affichage_centre_selection_lab):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_lab.__init__(self, joueur, Affichage_labyrinthe_case_magie)
    
class Affichage_centre_case_parchemin(Affichage_centre_selection_lab):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_lab.__init__(self, joueur, Affichage_labyrinthe_case_parchemin)

class Affichage_centre_direction_magie(Affichage_centre_selection_lab):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_lab.__init__(self, joueur, Affichage_labyrinthe_direction_magie)

class Affichage_centre_direction_parchemin(Affichage_centre_selection_lab):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_lab.__init__(self, joueur, Affichage_labyrinthe_direction_parchemin)

class Affichage_centre_selection_liste_menu(Wrapper_knot_bloque):
    def __init__(self, joueur: PJ, type_liste_menu: type):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.type_liste_menu:Affichage_liste_menu_recettes|Affichage_liste_menu_ventes|Affichage_liste_menu_achats|Affichage_liste_menu_impregnations|Affichage_liste_menu_auto_impregnations = type_liste_menu
        self.liste_menu:Liste_menu = None
        self.fond = (0, 0, 0)
        self.courant = self.type_liste_menu(self.joueur)
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(), self.courant, Marge_horizontale()], [5, -1, 5])
        contenu.set_contenu([Marge_verticale(), monoptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (0, 0, 0)

class Affichage_centre_recettes(Affichage_centre_selection_liste_menu):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_liste_menu.__init__(self, joueur, Affichage_liste_menu_recettes)

class Affichage_centre_ventes(Affichage_centre_selection_liste_menu):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_liste_menu.__init__(self, joueur, Affichage_liste_menu_ventes)

class Affichage_centre_achats(Affichage_centre_selection_liste_menu):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_liste_menu.__init__(self, joueur, Affichage_liste_menu_achats)

class Affichage_centre_impregnations(Affichage_centre_selection_liste_menu):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_liste_menu.__init__(self, joueur, Affichage_liste_menu_impregnations)

class Affichage_centre_auto_impregnations(Affichage_centre_selection_liste_menu):
    def __init__(self, joueur: PJ):
        Affichage_centre_selection_liste_menu.__init__(self, joueur, Affichage_liste_menu_auto_impregnations)

class Affichage_droite_dialogue(Wrapper_knot, Knot_vertical):
    def __init__(self, interlocuteur:Humain):
        Wrapper_knot.__init__(self)

        self.interlocuteur = interlocuteur
        self.fond = (255, 255, 255)
        self.replique = interlocuteur.replique

        self.phrase = Pave(self.interlocuteur.get_replique(self.interlocuteur.replique))
        self.repliques = [Affichage_replique(self.interlocuteur.get_replique(replique), replique) for replique in self.interlocuteur.repliques]

        self.set_default_courant()

    def init_droite(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        liste_repliques = Liste_verticale()
        liste_repliques.set_contenu([self.repliques[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.repliques)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.repliques)*2)])
        triptique.set_contenu([Marge_horizontale(), Affichage_perso(self.interlocuteur), Marge_horizontale(), self.phrase, Marge_horizontale(), liste_repliques, Marge_horizontale()], [5, 0, 5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def update(self):
        if self.replique != self.interlocuteur.replique:
            self.replique = self.interlocuteur.replique
            self.phrase = Pave(self.interlocuteur.get_replique(self.interlocuteur.replique))
            self.repliques = [Affichage_replique(self.interlocuteur.get_replique(replique), replique) for replique in self.interlocuteur.repliques]
            self.init_droite()
            self.set_tailles(self.tailles)
            if self.courant.actif:
                self.actif = True
            self.set_courant(self.repliques[0])
        else:
            self.contenu.update()

    def select(self, selection):
        if isinstance(selection, Affichage_replique):
            if selection != self.courant:
                self.set_courant(selection)
            else:
                self.interlocuteur.interprete(self.courant.replique)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.repliques[0])
        self.init_droite()
        self.set_tailles(self.tailles)

    def in_up(self):
        if self.courant != self.repliques[0]:
            self.set_courant(self.repliques[self.repliques.index(self.courant)-1])
        return self
    
    def in_down(self):
        if self.courant != self.repliques[-1]:
            self.set_courant(self.repliques[self.repliques.index(self.courant)+1])
        return self

    def survol(self, position):
        survol = Wrapper.survol(self, position)
        if survol is self:
            pass
        elif survol:
            if isinstance(survol, Affichage_replique):
                if survol != self.courant:
                    if self.courant and self.courant.actif:
                        self.courant.actif = False
                        survol.actif = True
                    self.set_courant(survol) # Une exception pour les dialogues ? Pourquoi ? Pourquoi pas ?
            self.set_tailles(self.tailles)
        else:
            self.set_tailles(self.tailles)
        if survol:
            return self
        return False

class Affichage_droite_agissant_cible(Wrapper_knot, Knot_horizontal):
    def __init__(self, controleur:Controleur, multi:bool, phase:int):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        if multi:
            self.cible = {"alliés":[], "ennemis":[], "neutres":[]}
        else:
            self.cible = None
        self.phase = phase
        self.fond = (255, 255, 255)

        self.allies = Affichage_agissants_cible(self.controleur, multi, Vignette_allie, self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus)
        self.ennemis = Affichage_agissants_cible(self.controleur, multi, Vignette_ennemi, self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus)
        self.neutres = Affichage_agissants_cible(self.controleur, multi, Vignette_neutre, self.controleur.get_esprit(self.controleur.joueur.esprit).get_neutres_vus)
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(), self.allies, Marge_verticale(), self.ennemis, Marge_verticale(), self.neutres, Marge_verticale()], [5, -1, 5, -1, 5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), triptique, Marge_horizontale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def init_agissant(self):
        agissant = self.courant.courant.agissant
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(), Bouton(SKIN_VALIDER, "Confirmer"), Marge_verticale(), Marge_verticale()], [5, 0, -1, 5])
        triptique.set_contenu([Marge_verticale(), self.allies, Marge_verticale(), self.ennemis, Marge_verticale(), self.neutres, Marge_verticale()], [5, -1, 5, -1, 5, -1, 5])
        monoptique.set_contenu([Marge_verticale(), Paves(agissant.get_texte_descriptif()), Marge_verticale()], [5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), triptique, Marge_horizontale(), monoptique, Marge_horizontale(), boutons, Marge_horizontale()], [5, -1, 5, 0, 5, 0, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Affichage_agissants_cible):
            if isinstance(self.controleur.joueur.magie_courante, Multi_cible):
                self.set_courant(selection)
                if isinstance(selection.type_vignette, Vignette_allie):
                    self.cible["alliés"] = self.courant.cible
                elif isinstance(selection.type_vignette, Vignette_ennemi):
                    self.cible["ennemis"] = self.courant.cible
                elif isinstance(selection.type_vignette, Vignette_neutre):
                    self.cible["neutres"] = self.courant.cible
            else:
                self.set_courant(selection)
                self.cible = self.courant.cible
                self.init_agissant()
        if isinstance(selection, Bouton) and selection.texte == "Confirmer":
            if isinstance(self.controleur.joueur.magie_courante, Multi_cible):
                self.cible = self.cible["alliés"]+self.cible["ennemis"]+self.cible["neutres"]
            self.controleur.joueur.cible_magie = self.cible
            self.controleur.unset_phase(self.phase)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.allies)
        self.init_agissant()
        self.set_tailles(self.tailles)
        
    def in_left(self):
        if self.courant is self.neutres:
            self.set_courant(self.allies)
            if self.courant.agissants: # Si on a des alliés (on a forcément nous-mêmes) il vaut mieux sélectionner le premier plutôt que de demander au joueur de faire un IN supplémentaire
                self.init_agissant()
            else:
                self.init_droite()
            self.set_tailles(self.tailles)
        elif self.courant is self.ennemis:
            self.set_courant(self.neutres)
            if self.courant.agissants:
                self.init_agissant()
            else:
                self.init_droite()
            self.set_tailles(self.tailles)
        return self

    def in_right(self):
        if self.courant is self.allies:
            self.set_courant(self.neutres)
            if self.courant.agissants:
                self.init_agissant()
            else:
                self.init_droite()
            self.set_tailles(self.tailles)
        elif self.courant is self.neutres:
            self.set_courant(self.ennemis)
            if self.courant.agissants:
                self.init_agissant()
            else:
                self.init_droite()
            self.set_tailles(self.tailles)
        return self

class Affichage_droite_recette(Wrapper_knot, Knot_vertical):
    def __init__(self, controleur:Controleur, recette):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.recette = recette
        self.fond = (255, 255, 255)
        self.ingredients = [Vignette_ingredient(eval(ingredient)(None), self.recette["ingredients"][ingredient], self.controleur.joueur.inventaire.quantite(eval(ingredient)), 40) for ingredient in self.recette["ingredients"]]
        self.vignette_recette = Vignette_recette(self.recette, 40, False, not self.controleur.joueur.inventaire.peut_fournir({eval(ingredient):self.recette["ingredients"][ingredient] for ingredient in self.recette["ingredients"]}))
        if self.controleur.joueur.inventaire.peut_fournir({eval(ingredient):self.recette["ingredients"][ingredient] for ingredient in self.recette["ingredients"]}):
            self.boutons = [Bouton(SKIN_VALIDER, "Confirmer"), Bouton(SKIN_QUITTER, "Annuler")]
        else:
            self.boutons = [Bouton(SKIN_QUITTER, "Annuler")]
        self.init_droite_produit()

    def init_droite_produit(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        liste = Liste_horizontale()
        boutons = Pavage_horizontal()
        boutons.set_contenu([self.boutons[i//2] if i%2 == 1 else Marge_horizontale() for i in range(len(self.boutons)*2+1)], [0 if i%2 == 1 else 5 for i in range(len(self.boutons)*2+1)])
        liste.set_contenu([self.ingredients[i//2] if i%2 == 0 else Marge_verticale() for i in range(len(self.ingredients)*2-1)], [0 if i%2 == 0 else 5 for i in range(len(self.ingredients)*2-1)])
        diptique.set_contenu([Marge_verticale(), self.vignette_recette, Marge_verticale(), liste, Marge_verticale()], [5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), diptique, Marge_horizontale(), Paves(eval(self.recette["produit"])(None).get_description()), Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def init_droite_ingredient(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        liste = Liste_horizontale()
        boutons = Pavage_horizontal()
        boutons.set_contenu([self.boutons[i//2] if i%2 == 1 else Marge_horizontale() for i in range(len(self.boutons)*2+1)], [0 if i%2 == 1 else 5 for i in range(len(self.boutons)*2+1)])
        liste.set_contenu([self.ingredients[i//2] if i%2 == 0 else Marge_verticale() for i in range(len(self.ingredients)*2-1)], [0 if i%2 == 0 else 5 for i in range(len(self.ingredients)*2-1)])
        diptique.set_contenu([Marge_verticale(), self.vignette_recette, Marge_verticale(), liste, Marge_verticale()], [5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), diptique, Marge_horizontale(), Paves(self.courant.ingredient.get_description()), Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Vignette_recette):
            self.set_courant(selection)
            self.init_droite_produit()
        if isinstance(selection, Vignette_ingredient):
            self.set_courant(selection)
            self.init_droite_ingredient()
        if isinstance(selection, Bouton) and selection.texte == "Confirmer":
            item = self.controleur.joueur.interlocuteur.cuisine(self.recette)
            self.controleur.ajoute_entitee(item)
            for ingredient in self.recette["ingredients"]:
                for _ in range(self.recette["ingredients"][ingredient]):
                    self.controleur.joueur.inventaire.consomme(eval(ingredient))
            self.controleur.joueur.inventaire.ajoute(item)
            self.controleur.unset_phase(RECETTE)
        if isinstance(selection, Bouton) and selection.texte == "Annuler":
            self.controleur.unset_phase(RECETTE)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.vignette_recette)
        self.init_droite_produit()
        self.set_tailles(self.tailles)

    def in_up(self):
        if isinstance(self.courant, Bouton):
            self.set_courant(self.vignette_recette)
            self.init_droite_produit()
            self.set_tailles(self.tailles)
        elif isinstance(self.courant, (Vignette_recette, Vignette_ingredient)):
            self.set_courant(self.boutons[0])
            self.init_droite_produit()
            self.set_tailles(self.tailles)
        return self

    def in_down(self):
        if isinstance(self.courant, (Vignette_recette, Vignette_ingredient)):
            self.set_courant(self.boutons[0])
            self.init_droite_produit()
            self.set_tailles(self.tailles)
        elif isinstance(self.courant, Bouton): # /!\ On veut vraiment wrapper ?
            self.set_courant(self.vignette_recette)
            self.init_droite_produit()
            self.set_tailles(self.tailles)
        return self
    
    def in_left(self):
        if isinstance(self.courant, Vignette_ingredient):
            if self.courant != self.ingredients[0]:
                self.set_courant(self.ingredients[self.ingredients.index(self.courant)-1])
                self.init_droite_ingredient()
                self.set_tailles(self.tailles)
            else:
                self.set_courant(self.vignette_recette)
                self.init_droite_produit()
                self.set_tailles(self.tailles)
        elif isinstance(self.courant, Bouton):
            if self.courant != self.boutons[0]:
                self.set_courant(self.boutons[self.boutons.index(self.courant)-1])
                self.init_droite_produit()
                self.set_tailles(self.tailles)
        return self
    
    def in_right(self):
        if isinstance(self.courant, Vignette_recette):
            self.set_courant(self.ingredients[0])
            self.init_droite_ingredient()
            self.set_tailles(self.tailles)
        elif isinstance(self.courant, Vignette_ingredient):
            if self.courant != self.ingredients[-1]:
                self.set_courant(self.ingredients[self.ingredients.index(self.courant)+1])
                self.init_droite_ingredient()
                self.set_tailles(self.tailles)
        elif isinstance(self.courant, Bouton):
            if self.courant != self.boutons[-1]:
                self.set_courant(self.boutons[self.boutons.index(self.courant)+1])
                self.init_droite_produit()
                self.set_tailles(self.tailles)
        return self

class Affichage_droite_vente(Wrapper_knot_bloque):
    def __init__(self, controleur:Controleur, vignette:Vignette_vente):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.item = vignette.item
        self.prix = vignette.prix
        self.invalide = vignette.item in self.controleur.joueur.equipement
        self.fond = (255, 255, 255)

        self.textes:List[str] = vignette.item.get_description() + [
            vignette.description, 
            f"Je veux bien t'en donner {vignette.prix} €.", 
        ]
        if self.invalide:
            self.textes.append("(Cet item est actuellement équippé, veux-tu vraiment le vendre ?)")
        self.bouton = Bouton(SKIN_VALIDER, "Vendre")
        self.courant = self.bouton
        self.init_droite_vente()

    def init_droite_vente(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(), self.bouton, Marge_verticale(), Marge_verticale()], [5, 0, -1, 5])
        triptique.set_contenu([Marge_horizontale(), Vignette_item([0, 0], self.item, 40, 0, False, self.invalide), Marge_horizontale(), Paves(self.textes), Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, -1, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Bouton) and selection.texte == "Vendre":
            self.controleur.joueur.inventaire.drop(None, self.item.ID)
            self.controleur.joueur.argent += self.prix
        self.set_tailles(self.tailles)

class Affichage_droite_achat(Wrapper_knot_bloque):
    def __init__(self, controleur:Controleur, vignette:Vignette_achat):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.item = vignette.item
        self.prix = vignette.prix
        self.invalide = vignette.prix > self.controleur.joueur.argent
        self.fond = (255, 255, 255)

        self.textes:List[str] = vignette.item.get_description() + [
            vignette.description, 
            f"Je veux bien t'en donner {vignette.prix} €.", 
        ]
        if self.invalide:
            self.textes.append("(Tu n'as pas assez d'argent pour acheter cet item. Tu peux me vendre ce dont tu ne sers pas si tu tiens vraiment à l'obtenir.)")
        self.bouton = Bouton(SKIN_VALIDER, "Acheter")
        self.courant = self.bouton
        self.init_droite_achat()

    def init_droite_achat(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(), self.bouton, Marge_verticale(), Marge_verticale()], [5, 0, -1, 5])
        triptique.set_contenu([Marge_horizontale(), Vignette_item([0, 0], self.item, 40, 0, False, self.invalide), Marge_horizontale(), Paves(self.textes), Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, -1, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Bouton) and selection.texte == "Acheter" and not self.invalide:
            self.controleur.joueur.inventaire.ajoute(self.item)
            self.controleur.joueur.argent -= self.prix
        self.set_tailles(self.tailles)

class Affichage_droite_impregnations(Wrapper_knot_bloque):
    def __init__(self, controleur:Controleur, texte:str, phase:int):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.fond = (255, 255, 255)
        self.texte = Texte(texte)
        self.phase = phase
        self.bouton = Bouton(SKIN_QUITTER, "Annuler")
        self.courant = self.bouton
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        boutons = Pavage_horizontal()
        boutons.set_contenu([Marge_verticale(), Marge_verticale(), self.courant, Marge_verticale()], [5, -1, 0, 5])
        diptique.set_contenu([Marge_verticale(), self.texte, Marge_verticale(), Marge_verticale(), boutons, Marge_verticale()], [-1, 0, -1, 5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), diptique, Marge_horizontale()], [-1, 0, -1])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Bouton) and selection.texte == "Annuler":
            self.controleur.unset_phase(self.phase)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.bouton)
        self.init_droite()
        self.set_tailles(self.tailles)

class Affichage_droite_impregnation(Wrapper_knot, Knot_horizontal):
    def __init__(self, controleur:Controleur, vignette:Vignette_magie, auto:bool=False):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.magie = vignette.magie
        self.invalide = vignette.magie.cout_pm>(controleur.joueur.pm if auto else controleur.joueur.interlocuteur.pm)
        self.auto = auto
        self.fond = (255, 255, 255)

        self.textes = self.magie.get_description() + [
            "Je peux imprégner ce parchemin de la magie de " + self.magie.nom + ".", 
        ]
        if self.invalide:
            self.textes.append("(Je n'ai pas assez de mana pour impregner ce parchemin. "+("Je devrais me reposer un peu.)" if auto else "Reviens me voir plus tard.)"))
            self.boutons = [Bouton(SKIN_QUITTER, "Annuler")]
        else:
            self.boutons = [Bouton(SKIN_VALIDER, "Impregner"), Bouton(SKIN_QUITTER, "Annuler")]
        self.init_droite_impregnation()

    def init_droite_impregnation(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        if self.invalide:
            boutons.set_contenu([Marge_verticale(), Marge_verticale(), self.boutons[0], Marge_verticale()], [5, -1, 0, 5])
        else:
            boutons.set_contenu([Marge_verticale(), self.boutons[0], Marge_verticale(), self.boutons[1], Marge_verticale()], [5, 0, -1, 0, 5])
        triptique.set_contenu([Marge_horizontale(), Vignette_magie(self.magie, 40, False, self.invalide), Marge_horizontale(), Paves(self.textes), Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, -1, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), triptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (255, 255, 255)

    def select(self, selection):
        if isinstance(selection, Bouton) and selection.texte == "Impregner":
            self.controleur.joueur.auto_impregne(self.magie.nom) if self.auto else self.controleur.joueur.interlocuteur.impregne(self.magie.nom)
            self.controleur.unset_phase(AUTO_IMPREGNATION if self.auto else IMPREGNATION)
        if isinstance(selection, Bouton) and selection.texte == "Annuler":
            self.controleur.unset_phase(AUTO_IMPREGNATION if self.auto else IMPREGNATION)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.boutons[0])
        self.init_droite_impregnation()
        self.set_tailles(self.tailles)

    def in_left(self):
        if self.courant != self.boutons[0]:
            self.set_courant(self.boutons[0])
            self.init_droite_impregnation()
            self.set_tailles(self.tailles)
        return self
    
    def in_right(self):
        if self.courant != self.boutons[-1]:
            self.set_courant(self.boutons[-1])
            self.init_droite_impregnation()
            self.set_tailles(self.tailles)
        return self

class Affichage_stats_ferme(Wrapper_cliquable):
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (200, 200, 200)
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        diptique_gauche = Pavage_vertical()
        diptique_droite = Pavage_vertical()
        diptique_gauche.set_contenu([Marge_horizontale(), Texte("PV"), Marge_horizontale(), Affichage_PV(self.joueur), Marge_horizontale()], [5, 0, 5, 0, 5])
        diptique_droite.set_contenu([Marge_horizontale(), Texte("PM"), Marge_horizontale(), Affichage_PM(self.joueur), Marge_horizontale()], [5, 0, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), diptique_gauche, Marge_verticale(), diptique_droite, Marge_verticale()], [5, -1, 5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

class Affichage_stats(Wrapper_cliquable): # Modifier en donnant la possibilité d'afficher le détail des stats
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (200, 200, 200)
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        tetraptique = Pavage_vertical()
        tetraptique.set_contenu([Marge_horizontale(), Texte("PV"), Marge_horizontale(), Affichage_PV(self.joueur), Marge_horizontale(), Texte("PM"), Marge_horizontale(), Affichage_PM(self.joueur), Marge_horizontale()], [5, 0, 5, 0, 5, 0, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), tetraptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

class Affichage_stats_cout_magie(Wrapper_knot, Knot_vertical):
    def __init__(self, controleur:Controleur, parchemin:bool=False):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.parchemin = parchemin
        self.cout = 0
        self.fond = (200, 200, 200)
        self.affichage_cout = Affichage_PM_cout(self.controleur.joueur)
        self.bouton = Bouton(SKIN_VALIDER, "Confirmer")
        self.courant = self.bouton
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        pentaptique = Pavage_vertical()
        boutons = Pavage_horizontal()
        boutons.set_contenu([self.bouton, Marge_verticale()], [0, -1])
        pentaptique.set_contenu([Marge_horizontale(), Texte("PV"), Marge_horizontale(), Affichage_PV(self.controleur.joueur), Marge_horizontale(), Texte("PM"), Marge_horizontale(), self.affichage_cout, Marge_horizontale(), boutons, Marge_horizontale()], [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), pentaptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def select(self, selection):
        if isinstance(selection, Affichage_PM_cout):
            self.set_courant(selection)
            self.cout = selection.cout
        if isinstance(selection, Bouton) and selection.texte == "Confirmer":
            if self.parchemin:
                self.controleur.joueur.cout_magie_parchemin = self.cout
            else:
                self.controleur.joueur.cout_magie = self.cout
            self.controleur.unset_phase(COUT_MAGIE if self.parchemin else COUT_PARCHEMIN)
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.bouton)
        self.init()
        self.set_tailles(self.tailles)

    def in_up(self):
        if self.courant != self.affichage_cout:
            self.set_courant(self.affichage_cout)
            self.init()
            self.set_tailles(self.tailles)
        return self

    def in_down(self):
        if self.courant != self.bouton:
            self.set_courant(self.bouton)
            self.init()
            self.set_tailles(self.tailles)
        return self

class Affichage_inventaire_ferme(Wrapper_cliquable):
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (200, 200, 200)
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        liste = Liste_horizontale()
        vignettes = [Vignette([0, 0], 20, classe.get_image()) for classe in self.joueur.inventaire.items.keys()]
        liste.set_contenu([vignettes[i//2] if i%2==0 else Marge_verticale() for i  in range(-1, len(vignettes)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(vignettes)*2)])
        monoptique.set_contenu([Marge_horizontale(), liste, Marge_horizontale()], [5, 0, 5])
        contenu.set_contenu([Marge_verticale(), monoptique, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

class Affichage_inventaire(Wrapper_knot, Knot_vertical, Knot_hierarchique_sinistre_sommet):
    def __init__(self, joueur: PJ):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.fond = (200, 200, 200)

        classes = self.joueur.inventaire.items.keys()

        self.liste_v = Liste_verticale()
        #pas joli : vignettes = [Vignette_categorie(classe, 40, False, not self.joueur.inventaire.items[classe]) for classe in self.joueur.inventaire.items.keys()]
        self.vignettes = [Vignette_categorie(classe, 40) for classe in classes]
        self.liste_v.set_contenu([self.vignettes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.vignettes)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.vignettes)*2)])
        self.categories = {classe:Affichage_categorie(self.joueur, classe) for classe in classes}

        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monoptique = Liste_horizontale()
        monoptique.set_contenu([Marge_verticale(), self.liste_v, Marge_verticale()], [5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), monoptique, Marge_horizontale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_classe(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        diptique.set_contenu([Marge_verticale(), self.liste_v, Marge_verticale(), self.categories[self.courant.categorie], Marge_verticale()], [5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), diptique, Marge_horizontale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def select(self, selection):
        if isinstance(selection, Vignette_categorie):
            self.set_courant(selection)
            self.init_classe()
            self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.categories[Cle]) # Est-ce qu'on veut vraiment cette catégorie par défaut ? (Ça pourrait être dans les paramètres du joueur...)
        self.init_classe()
        self.set_tailles(self.tailles)

    def in_down(self):
        if self.courant in self.vignettes:
            self.set_courant(self.vignettes[(self.vignettes.index(self.courant)+1)%len(self.vignettes)]) # On veut vraiment wrapper ?
            self.init_classe()
            self.set_tailles(self.tailles)
        return self
    
    def in_up(self):
        if self.courant in self.vignettes:
            self.set_courant(self.vignettes[(self.vignettes.index(self.courant)-1)%len(self.vignettes)])
            self.init_classe()
            self.set_tailles(self.tailles)
        return self
    
    def in_in(self):
        if self.courant in self.vignettes:
            self.actif = False
            self.set_courant(self.categories[self.courant.categorie])
            self.courant.actif = True
        return self
    
    def in_out(self):
        if self.courant in self.categories.values():
            self.courant.actif = False
            self.set_courant([vignette for vignette in self.vignettes if vignette.categorie == self.courant.categorie][0])
            self.actif = True
        return self

class Affichage_categorie(Wrapper_knot, Knot_vertical, Knot_hierarchique_sinistre_base):
    def __init__(self, joueur: PJ, categorie:Type[Potion|Parchemin|Cle|Arme|Bouclier|Armure|Haume|Anneau|Projectile|Ingredient|Cadavre|Oeuf]):
        Wrapper_knot.__init__(self)

        self.joueur = joueur
        self.categorie = categorie
        self.fond = (200, 200, 200)

        self.liste_i = Liste_verticale()
        self.items = [Vignette_item([0, 0], self.joueur.controleur[ID], 40) for ID in self.joueur.inventaire.items[self.categorie]]
        self.liste_i.set_contenu([self.items[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.items)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.items)*2)])

        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monoptique = Liste_horizontale()
        monoptique.set_contenu([Marge_verticale(), self.liste_i, Marge_verticale()], [5, 0, 5])
        contenu.set_contenu([Marge_horizontale(), monoptique, Marge_horizontale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_item(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Marge_verticale(), self.liste_i, Marge_verticale(), Paves(self.courant.item.get_description(0)), Marge_verticale()], [5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_horizontale(), triptique, Marge_horizontale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def select(self, selection):
        if isinstance(selection, Vignette_item): #On veut afficher un item
            if selection == self.courant:
                self.joueur.inventaire.utilise_item(selection.item.ID)
            else:
                self.set_courant(selection)
                self.init_item()
            self.set_tailles(self.tailles)

    def set_default_courant(self):
        if self.items != []:
            self.set_courant(self.items[0])
            self.init_item()
            self.set_tailles(self.tailles)

    def in_down(self):
        if self.courant != self.items[-1]:
            self.set_courant(self.items[self.items.index(self.courant)+1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def in_up(self):
        if self.courant != self.items[0]:
            self.set_courant(self.items[self.items.index(self.courant)-1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def update(self):
        i=0
        items = self.joueur.inventaire.items[self.categorie]
        while i < len(items) or i < len(self.items):
            if i == len(items) or i == len(self.items) or items[i] != self.items[i].item.ID: #Les deux ne correspondent pas
                if i == len(self.items) or self.items[i].item.ID in items: #Donc l'item n'a pas été retiré, mais d'autres ont été ajoutés avant
                    item = Vignette_item([0, 0], self.joueur.controleur[items[i]], 40)
                    self.items.insert(i, item)
                    self.liste_i.insert(2*i, item, 0)
                    self.liste_i.insert(2*i, Marge_horizontale(), 5)
                    i+=1
                else: #l'item qui était à l'emplacement i a été retiré
                    if self.courant == self.items[i]:
                        if self.courant == self.items[0]:
                            if len(self.items) == 1:
                                self.set_courant(None)
                            else:
                                self.set_courant(self.items[1])
                        else:
                            self.set_courant(self.items[i-1])
                    self.items.pop(i)
                    self.liste_i.pop(2*i) # La marge avant l'item
                    self.liste_i.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres items à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_sous_classe(Wrapper_knot, Knot_vertical):
    def __init__(self, classe):
        Wrapper_knot.__init__(self)

        self.classe = classe
        self.fond = (200, 200, 200)

        self.intrasecs = Affichage_intrasecs(self.classe)
        self.skills = Affichage_skills(self.classe)
        self.classes = Affichage_classes(self.classe)

        self.intrasecs_ferme = Margin_texte("Compétences intrasèques")
        self.skills_ferme = Margin_texte("Compétences propres")
        self.classes_ferme = Margin_texte("Sous-classes")

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        liste.set_contenu([Marge_horizontale(), self.intrasecs_ferme, Marge_horizontale(), self.skills_ferme, Marge_horizontale(), self.classes_ferme, Marge_horizontale()], [5, 0, 5, 0, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), liste, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_intrasecs(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(), self.intrasecs, Marge_horizontale(), self.skills_ferme, Marge_horizontale(), self.classes_ferme, Marge_horizontale()], [5, -1, 5, 0, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), liste, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_skills(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(), self.intrasecs_ferme, Marge_horizontale(), self.skills, Marge_horizontale(), self.classes_ferme, Marge_horizontale()], [5, 0, 5, -1, 5, 0, 5])
        contenu.set_contenu([Marge_verticale(), liste, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_classes(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(), self.intrasecs_ferme, Marge_horizontale(), self.skills_ferme, Marge_horizontale(), self.classes, Marge_horizontale()], [5, 0, 5, 0, 5, -1, 5])
        contenu.set_contenu([Marge_verticale(), liste, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_sous(self):
        if self.courant is self.intrasecs_ferme or self.courant is self.intrasecs:
            self.init_intrasecs()
            self.set_courant(self.intrasecs)
        elif self.courant is self.skills_ferme or self.courant is self.skills:
            self.init_skills()
            self.set_courant(self.skills)
        elif self.courant is self.classes_ferme or self.courant is self.classes:
            self.init_classes()
            self.set_courant(self.classes)
        else:
            self.init()

    def select(self, selection):
        if selection in [self.intrasecs_ferme, self.skills_ferme, self.classes_ferme, self.intrasecs, self.skills, self.classes]:
            self.set_courant(selection)
            self.init_sous()
        self.set_tailles(self.tailles)

    def set_default_courant(self):
        self.set_courant(self.intrasecs)

    def in_up(self):
        if self.courant is self.classes:
            self.set_courant(self.skills_ferme)
            self.init_sous()
            self.set_tailles(self.tailles)
        elif self.courant is self.skills:
            self.set_courant(self.intrasecs_ferme)
            self.init_sous()
            self.set_tailles(self.tailles)
        return self

    def in_down(self):
        if self.courant is self.intrasecs:
            self.set_courant(self.skills_ferme)
            self.init_sous()
            self.set_tailles(self.tailles)
        elif self.courant is self.skills:
            self.set_courant(self.classes_ferme)
            self.init_sous()
            self.set_tailles(self.tailles)
        return self

class Affichage_intrasecs(Wrapper_knot, Knot_vertical):
    def __init__(self, classe:Classe):
        Wrapper_knot.__init__(self)

        self.classe = classe
        self.fond = (200, 200, 200)
        
        self.liste_skills = Liste_verticale()
        self.skills = [Affichage_skill(skill) for skill in self.classe.skills_intrasecs]
        self.liste_skills.set_contenu([self.skills[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.skills)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.skills)*2)])

        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(), self.liste_skills, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def select(self, selection):
        if isinstance(selection, Affichage_skill): #On veut afficher un item
            if selection == self.courant:
                pass #TODO: utiliser le skill
            self.set_tailles(self.tailles)

    def set_default_courant(self):
        if self.skills != []:
            self.set_courant(self.skills[0])
            self.init()
            self.set_tailles(self.tailles)
        else:
            self.set_courant(None)

    def in_up(self):
        if self.courant not in self.skills:
            self.set_default_courant()
        elif self.courant != self.skills[0]:
            self.set_courant(self.skills[self.skills.index(self.courant)-1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def in_down(self):
        if self.courant not in self.skills:
            self.set_default_courant()
        elif self.courant != self.skills[-1]:
            self.set_courant(self.skills[self.skills.index(self.courant)+1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def update(self):
        i=0
        skills = self.classe.skills_intrasecs
        while i < len(skills) or i < len(self.skills):
            if i >= len(skills) or i >= len(self.skills) or skills[i] != self.skills[i].skill: #Les deux ne correspondent pas
                if i == len(self.skills) or self.skills[i].skill in skills: #Donc le skill n'a pas été retiré, mais d'autres ont été ajoutés avant
                    skill = Affichage_skill(skills[i])
                    self.skills.insert(i, skill)
                    self.liste_skills.insert(2*i, skill, 0)
                    self.liste_skills.insert(2*i, Marge_horizontale(), 5)
                    i+=1
                else: #le skill qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    if self.courant == self.skills[i]:
                        if self.courant == self.skills[0]:
                            if len(self.skills) == 1:
                                self.set_courant(None)
                            else:
                                self.set_courant(self.skills[1])
                        else:
                            self.set_courant(self.skills[i-1])
                    self.skills.pop(i)
                    self.liste_skills.pop(2*i) # La marge avant l'item
                    self.liste_skills.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres skills à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_skills(Wrapper_knot, Knot_vertical):
    def __init__(self, classe:Classe):
        Wrapper_knot.__init__(self)

        self.classe = classe
        self.fond = (200, 200, 200)
        
        self.liste_skills = Liste_verticale()
        self.skills = [Affichage_skill(skill) for skill in self.classe.skills]
        self.liste_skills.set_contenu([self.skills[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.skills)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.skills)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(), self.liste_skills, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(), self.liste_skills, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def select(self, selection):
        if isinstance(selection, Affichage_skill): #On veut afficher un item
            if selection == self.courant:
                pass #TODO: utiliser le skill
            self.set_tailles(self.tailles)

    def set_default_courant(self):
        if self.skills != []:
            self.set_courant(self.skills[0])
            self.init()
            self.set_tailles(self.tailles)
        else:
            self.set_courant(None)

    def in_up(self):
        if self.courant not in self.skills:
            self.set_default_courant()
        elif self.courant != self.skills[0]:
            self.set_courant(self.skills[self.skills.index(self.courant)-1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def in_down(self):
        if self.courant not in self.skills:
            self.set_default_courant()
        elif self.courant != self.skills[-1]:
            self.set_courant(self.skills[self.skills.index(self.courant)+1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def update(self):
        i=0
        skills = self.classe.skills
        while i < len(skills) or i < len(self.skills):
            if i >= len(skills) or i >= len(self.skills) or skills[i] != self.skills[i].skill: #Les deux ne correspondent pas
                if i == len(self.skills) or self.skills[i].skill in skills: #Donc le skill n'a pas été retiré, mais d'autres ont été ajoutés avant
                    skill = Affichage_skill(skills[i])
                    self.skills.insert(i, skill)
                    self.liste_skills.insert(2*i, skill, 0)
                    self.liste_skills.insert(2*i, Marge_horizontale(), 5)
                    i+=1
                else: #le skill qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    if self.courant == self.skills[i]:
                        if self.courant == self.skills[0]:
                            if len(self.skills) == 1:
                                self.set_courant(None)
                            else:
                                self.set_courant(self.skills[1])
                        else:
                            self.set_courant(self.skills[i-1])
                    self.skills.pop(i)
                    self.liste_skills.pop(2*i) # La marge avant l'item
                    self.liste_skills.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres skills à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_classes(Wrapper_knot, Knot_vertical):
    def __init__(self, classe:Classe):
        Wrapper_knot.__init__(self)

        self.classe = classe
        self.fond = (200, 200, 200)
        
        self.liste_classes = Liste_verticale()
        self.classes = [Affichage_classe(classe) for classe in self.classe.sous_classes]
        self.liste_classes.set_contenu([self.classes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.classes)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.classes)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(), self.liste_classes, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def init_sous_classe(self):
        for i in range(len(self.classes)):
            if self.classes[i] != self.courant:
                if isinstance(self.classes[i], Affichage_sous_classe):
                    self.classe[i] = Affichage_classe(self.classes[i].classe)
                    self.liste_classes.replace(i*2+1, self.classes[i], 0)
            else:
                self.classe[i] = Affichage_sous_classe(self.classes[i].classe)
                self.liste_classes.replace(i*2+1, self.classes[i], 0)
                self.set_courant(self.classe[i])

        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(), self.liste_classes, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def select(self, selection):
        if isinstance(selection, Affichage_sous_classe): #On veut afficher un item
            if selection == self.courant:
                self.init_sous_classe()
            else:
                self.courant.actif = False
                self.set_courant(selection)
                self.courant.actif = True
            self.set_tailles(self.tailles)

    def set_default_courant(self):
        if self.classes != []:
            self.set_courant(self.classes[0])
            self.init()
            self.set_tailles(self.tailles)
        else:
            self.set_courant(None)

    def in_up(self):
        if self.courant not in self.classes:
            self.set_default_courant()
        elif self.courant != self.classes[0]:
            self.set_courant(self.classes[self.classes.index(self.courant)-1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def in_down(self):
        if self.courant not in self.classes:
            self.set_default_courant()
        elif self.courant != self.classes[-1]:
            self.set_courant(self.classes[self.classes.index(self.courant)+1])
            self.init()
            self.set_tailles(self.tailles)
        return self

    def update(self):
        i=0
        classes = self.classe.sous_classes
        while i < len(classes) or i < len(self.classes):
            if i == len(classes) or i == len(self.classes) or classes[i] != self.classes[i].classe: #Les deux ne correspondent pas
                if i == len(self.classes) or self.classes[i].classe in classes: #Donc la classe n'a pas été retiré, mais d'autres ont été ajoutés avant
                    classe = Affichage_classe(classes[i])
                    self.classes.insert(i, classe)
                    self.liste_classes.insert(2*i, classe, 0)
                    self.liste_classes.insert(2*i, Marge_horizontale(), 5)
                    i+=1
                else: #la classe qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    if self.courant == self.classes[i]:
                        if self.courant == self.classes[0]:
                            if len(self.classes) == 1:
                                self.set_courant(None)
                            else:
                                self.set_courant(self.classes[1])
                        else:
                            self.set_courant(self.classes[i-1])
                    self.classes.pop(i)
                    self.liste_classes.pop(2*i) # La marge avant l'item
                    self.liste_classes.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres classes à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

class Affichage_agissants(Wrapper_knot, Knot_vertical):
    def __init__(self, controleur:Controleur, type_vignette:Type[Vignette_allie|Vignette_ennemi|Vignette_neutre], methode:Callable[[], List[int]]):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.type_vignette = type_vignette
        self.methode = methode
        self.fond = (200, 200, 200)
        
        self.liste_agissants = Liste_verticale()
        self.agissants = [self.type_vignette(self.controleur[ID], self.controleur.joueur.esprit, 40) for ID in self.methode()]
        self.liste_agissants.set_contenu([self.agissants[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.agissants)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.agissants)*2)])
        
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        contenu.set_contenu([Marge_verticale(), self.liste_agissants, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def update(self):
        i=0
        agissants = self.methode()
        while i < len(agissants) or i < len(self.agissants):
            if i == len(agissants) or i == len(self.agissants) or agissants[i] != self.agissants[i].agissant.ID: #Les deux ne correspondent pas
                if i == len(self.agissants) or self.agissants[i].agissant.ID in agissants: #Donc l'agissant n'a pas été retiré, mais d'autres ont été ajoutés avant
                    allie = self.type_vignette(self.controleur[agissants[i]], self.controleur.joueur.esprit, 40)
                    self.agissants.insert(i, allie)
                    self.liste_agissants.insert(2*i, allie, 0)
                    self.liste_agissants.insert(2*i, Marge_horizontale(), 5)
                    i+=1
                else: #l'agissant qui était à l'emplacement i a été retiré (rare mais je suppose que ça peut arriver)
                    self.agissants.pop(i)
                    self.liste_agissants.pop(2*i) # La marge avant l'item
                    self.liste_agissants.pop(2*i) # L'item
                    # On n'incrémente pas i puisqu'il peut y avoir d'autres agissants à retirer/ajouter
            else:
                i+=1
        self.contenu.update()
        for objet in self.objets:
            objet.update()

    def set_default_courant(self):
        if len(self.agissants) > 0:
            self.set_courant(self.agissants[0])
        else:
            self.set_courant(None)

    def select(self, selection):
        if isinstance(selection, self.type_vignette):
            if self.courant == selection:
                pass
            else:
                self.set_courant(selection)

    def in_up(self):
        if self.courant is None:
            self.set_default_courant()
        if self.courant is not None:
            self.set_courant(self.agissants[(self.agissants.index(self.courant) - 1) % len(self.agissants)])
        return self

    def in_down(self):
        if self.courant is None:
            self.set_default_courant()
        if self.courant is not None:
            self.set_courant(self.agissants[(self.agissants.index(self.courant) + 1) % len(self.agissants)])
        return self

class Affichage_agissants_cible(Wrapper_knot, Knot_vertical):
    def __init__(self, controleur:Controleur, multi:bool, type_vignette:Type[Vignette_allie|Vignette_ennemi|Vignette_neutre], methode:Callable[[], List[int]]):
        Wrapper_knot.__init__(self)

        self.controleur = controleur
        self.type_vignette = type_vignette
        self.methode = methode
        if multi :
            self.cible = []
        else:
            self.cible = None
        self.multi = multi
        self.fond = (200, 200, 200)

        self.agissants = [self.type_vignette(self.controleur[ID], self.controleur.joueur.esprit, 40) for ID in self.methode()]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        liste.set_contenu([self.agissants[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1, len(self.agissants)*2)], [0 if i%2==0 else 5 for i  in range(-1, len(self.agissants)*2)])
        contenu.set_contenu([Marge_verticale(), liste, Marge_verticale()], [5, -1, 5])
        self.contenu = contenu
        self.fond = (200, 200, 200)

    def update(self):
        self.init()
        for objet in self.objets:
            objet.update()
        self.set_tailles(self.tailles)

    def select(self, selection):
        if isinstance(selection, self.type_vignette):
            if self.courant == selection:
                if self.multi and selection.agissant.ID in self.cible:
                    self.cible.remove(selection.agissant.ID)
                    self.set_courant(self.type_vignette([0, 0], self.controleur[selection.agissant.ID], self.controleur.joueur.esprit, 40, True))
                    self.agissants[self.agissants.index(selection)] = self.courant
                elif self.multi:
                    self.set_courant(self.type_vignette([0, 0], self.controleur[selection.agissant.ID], self.controleur.joueur.esprit, 40, True, True))
                    self.agissants[self.agissants.index(selection)] = self.courant
                    self.cible.append(selection.agissant.ID)
                elif selection.agissant.ID == self.cible:
                    self.set_courant(self.type_vignette([0, 0], self.controleur[selection.agissant.ID], self.controleur.joueur.esprit, 40, True))
                    self.agissants[self.agissants.index(selection)] = self.courant
                    self.cible = None
                else:
                    self.set_courant(self.type_vignette([0, 0], self.controleur[selection.agissant.ID], self.controleur.joueur.esprit, 40, True, True))
                    self.agissants[self.agissants.index(selection)] = self.courant
                    self.cible = selection.agissant.ID
            else:
                if self.courant.agissant.ID is self.cible or self.multi and self.courant.agissant.ID in self.cible:
                    self.agissants[self.agissants.index(self.courant)] = self.type_vignette([0, 0], self.controleur[self.courant.agissant.ID], self.controleur.joueur.esprit, 40, True, True)
                else:
                    self.agissants[self.agissants.index(self.courant)] = self.type_vignette([0, 0], self.controleur[self.courant.agissant.ID], self.controleur.joueur.esprit, 40)
                self.set_courant(selection)
                self.agissants[self.agissants.index(self.courant)] = self.type_vignette([0, 0], self.controleur[self.courant.agissant.ID], self.controleur.joueur.esprit, 40, True)

    def in_up(self):
        self.set_courant(self.agissants[(self.agissants.index(self.courant) - 1) % len(self.agissants)])
        return self

    def in_down(self):
        self.set_courant(self.agissants[(self.agissants.index(self.courant) + 1) % len(self.agissants)])
        return self

class Affichage_PV(Affichable):
    def __init__(self, joueur: PJ):
        self.joueur = joueur
        self.position = [0, 0]
        self.tailles = [0, 10]

    def affiche(self, screen, frame, frame_par_tour):
        pygame.draw.rect(screen, (255, 160, 160), (self.position[0], self.position[1], self.tailles[0], 10))
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], (self.tailles[0]*self.joueur.pv)//self.joueur.pv_max, 10))

    def get_tailles(self, tailles):
        return [tailles[0], self.tailles[1]]

class Affichage_PM(Affichable):
    def __init__(self, joueur: PJ):
        self.joueur = joueur
        self.position = [0, 0]
        self.tailles = [0, 10]

    def affiche(self, screen, frame, frame_par_tour):
        pygame.draw.rect(screen, (160, 255, 255), (self.position[0], self.position[1], self.tailles[0], 10))
        pygame.draw.rect(screen, (32, 255, 255), (self.position[0], self.position[1], (self.tailles[0]*self.joueur.pm)//self.joueur.pm_max, 10))

    def get_tailles(self, tailles):
        return [tailles[0], self.tailles[1]]

class Affichage_PM_cout(Cliquable):
    def __init__(self, joueur: PJ):
        self.joueur = joueur
        self.position = [0, 0]
        self.tailles = [0, 10]
        self.cout = 0

    def affiche(self, screen, frame, frame_par_tour):
        pygame.draw.rect(screen, (160, 255, 255), (self.position[0], self.position[1], self.tailles[0], 10))
        pygame.draw.rect(screen, (32, 255, 255), (self.position[0], self.position[1], (self.tailles[0]*self.joueur.pm)//self.joueur.pm_max, 10))
        pygame.draw.rect(screen, (32, 255, 255), (self.position[0], self.position[1], (self.tailles[0]*(self.joueur.pm-self.cout))//self.joueur.pm_max, 10))

    def get_tailles(self, tailles):
        return [tailles[0], self.tailles[1]]

    def clique(self, position):
        if self.touche(position):
            proportion = (position[0]-self.position[0])/self.tailles[0]
            if proportion < 0:
                proportion = 0
            elif proportion > 1:
                proportion = 1
            pm = int(self.joueur.pm_max*proportion)
            if pm < self.joueur.pm:
                self.cout = pm
            return self
        return 
        
    def in_left(self):
        self.cout -= 5
        if self.cout < 0:
            self.cout = 0
        return self
    
    def in_right(self):
        self.cout += 5
        if self.cout > self.joueur.pm:
            self.cout = self.joueur.pm
        return self

class Titre(Cliquable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self, controleur:Controleur):
        self.controleur = controleur
        self.tailles = [0, 40]
        self.position = [0, 0]

    def affiche(self, screen, frame=1, frame_par_tour=1):
        texte = self.controleur.joueur.position.lab
        if self.controleur.phase == TOUR and self.controleur.pause:
            texte+=" - (en pause)"
        elif self.controleur.phase == DIALOGUE:
            texte+=" - dialogue"
        elif self.controleur.phase == TOUCHE:
            texte="Modification des touches"
        texte=POLICE40.render(texte, True, (255, 255, 255))
        screen.blit(texte, self.position)

class Affichage_perso(Proportionnel):
    def __init__(self, perso):
        self.perso = perso
        self.tailles = [0, 0]
        self.position = [0, 0]
        self.proportions = [3, 4]

    def affiche(self, screen, frame, frame_par_tour):
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
                        traj = joueur.controleur.get_trajet(case[0], direction)
                        if traj == "escalier bas":
                            skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][0])
                        elif traj == "escalier haut":
                            skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][0])
                    if not case[5][direction-1][4]:
                        skins.append(SKINS_MURS_VUS[distance][0][0])
                    else:
                        traj = joueur.controleur.get_trajet(case[0], direction-1)
                        if traj == "escalier bas":
                            skins.append(SKINS_ESCALIERS_BAS_VUS[distance][0][0])
                        elif traj == "escalier haut":
                            skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][0][0])
                    if not case[5][direction-3][4]:
                        skins.append(SKINS_MURS_VUS[distance][0][1])
                    else:
                        traj = joueur.controleur.get_trajet(case[0], direction-3)
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
                            traj = joueur.controleur.get_trajet(case[0], direction)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][ecart])
                        if not case[5][direction-3][4]:
                            skins.append(SKINS_MURS_VUS[distance][ecart])#Pareil
                        else:
                            traj = joueur.controleur.get_trajet(case[0], direction-3)
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
                            traj = joueur.controleur.get_trajet(case[0], direction)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_FACE_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_FACE_VUS[distance][ecart])
                        if not case[5][direction-1][4]:
                            skins.append(SKINS_MURS_VUS[distance][ecart])
                        else:
                            traj = joueur.controleur.get_trajet(case[0], direction-1)
                            if traj == "escalier bas":
                                skins.append(SKINS_ESCALIERS_BAS_VUS[distance][ecart])
                            elif traj == "escalier haut":
                                skins.append(SKINS_ESCALIERS_HAUT_VUS[distance][ecart])
        skins.reverse()
        for skin in skins:
            skin.dessine_toi(screen, (x, y), (largeur, hauteur), frame, frame_par_tour)

        for ID in joueur.vue[position][6]:
            if ID < 11:
                entitee = joueur.controleur[ID]
                if issubclass(entitee.get_classe(), Agissant):
                    for skin in entitee.get_skins_vue():
                        skin.dessine_toi(screen, (x, y), (largeur, hauteur), frame, frame_par_tour)
                    break

class Affichage_labyrinthe(Affichage_knot, Proportionnel):
    def __init__(self, joueur: PJ):
        Affichage_knot.__init__(self)
        
        self.joueur = joueur
        self.taille_case = 0
        self.nb_cases = 0
        self.proportions = [1, 1]

    def set_tailles(self, tailles):
        Proportionnel.set_tailles(self, tailles)
        self.update()

    def update(self):
        courant = None
        if self.joueur.vue != None:
            self.objets:List[Affichable] = []
            decs = [[dec.x, dec.y] for dec in self.joueur.vue.decalage if self.joueur.vue[dec][1] > 0]
            visible = [min(decs, key=itemgetter(0))[0], max(decs, key=itemgetter(0))[0], min(decs, key=itemgetter(1))[1], max(decs, key=itemgetter(1))[1]]
            distance = max(self.joueur.position.x-visible[0], visible[1]-self.joueur.position.x, self.joueur.position.y-visible[2], visible[3]-self.joueur.position.y) + 1 #On cherche à déterminer le carré qui comprend toutes les cases utiles de la vue
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
                    pos = debut_vue + Decalage(i, j)
                    position = [marge_gauche, marge_haut]
                    vignette = self.make_vignette(position, self.joueur, self.joueur.vue, pos, taille_case)
                    if self.courant and vignette.pos == self.courant.pos:
                        courant = vignette
                        if self.courant.actif:
                            vignette.actif = True
                    self.objets.append(vignette)
                    marge_gauche += taille_case
                marge_haut += taille_case
        else:
            for objet in self.objets:
                objet.update()
        self.courant = courant

    def make_vignette(self, position:List[int], joueur: PJ, vue:Vue, position_vue:Position, taille:int):
        return Vignettes_position(position, joueur, vue, position_vue, taille)
    
    def select(self, selection):
        if isinstance(selection, Vignettes_position):
            self.set_courant(selection)

    def set_default_courant(self):
        vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignettes_position) and vignette.pos == self.joueur.position]
        if vignettes:
            self.set_courant(vignettes[0])
        else:
            self.set_courant(None)

    def in_up(self):
        if isinstance(self.courant, Vignettes_position):
            up = self.courant.pos + HAUT
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignettes_position) and vignette.pos == up]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
    
    def in_down(self):
        if isinstance(self.courant, Vignettes_position):
            down = self.courant.pos + BAS
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignettes_position) and vignette.pos == down]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
    
    def in_left(self):
        if isinstance(self.courant, Vignettes_position):
            left = self.courant.pos + GAUCHE
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignettes_position) and vignette.pos == left]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self
    
    def in_right(self):
        if isinstance(self.courant, Vignettes_position):
            right = self.courant.pos + DROITE
            vignettes = [vignette for vignette in self.objets if isinstance(vignette, Vignettes_position) and vignette.pos == right]
            if vignettes:
                self.set_courant(vignettes[0])
            else:
                self.set_courant(None)
        return self

class Affichage_labyrinthe_jeu(Affichage_labyrinthe):
    def select(self, selection):
        if isinstance(selection, Vignettes_position):
            self.set_courant(selection)
            pos_joueur = self.joueur.position
            if selection.pos not in pos_joueur:
                print("Le joueur et l'affichage du labyrinthe ne sont pas au même étage")
                return
            decalage = pos_joueur-selection.pos
            if abs(decalage.x) > abs(decalage.y):
                if decalage.x<0:
                    direction = DROITE
                else:
                    direction = GAUCHE
            elif abs(decalage.x) < abs(decalage.y):
                if decalage.y<0:
                    direction = BAS
                else:
                    direction = HAUT
            else:
                return
            self.joueur.va(direction)
            self.set_tailles(self.tailles)

class Affichage_labyrinthe_case_dialogue(Affichage_labyrinthe):
    def __init__(self, joueur: PJ):
        Affichage_labyrinthe.__init__(self, joueur)

        self.cible = None

    def make_vignette(self, position: List[int], joueur: PJ, vue: Vue, position_vue: Position, taille: int):
        return Vignettes_position(position, joueur, vue, position_vue, taille, self.cible != None and self.cible != position_vue)

    def select(self, selection):
        if isinstance(selection, Vignettes_position):
            self.set_courant(selection)
            if selection.pos != self.cible:
                self.cible = selection.pos
            else:
                self.cible = None

class Affichage_labyrinthe_case_magie(Affichage_labyrinthe):
    def __init__(self, controleur:Controleur):
        Affichage_labyrinthe.__init__(self, controleur.joueur)

        self.cibles = controleur.get_cibles_potentielles_cases(self.joueur.magie_courante, self.joueur)
        if isinstance(self.joueur.magie_courante, Multi_cible):
            self.cible = []
        else:
            self.cible = None

    def make_vignette(self, position: List[int], joueur: PJ, vue: Vue, position_vue: Position, taille: int):
        return Vignettes_position(position, joueur, vue, position_vue, taille, self.cible != None and self.cible != position_vue, position_vue not in self.cibles)

    def select(self, selection):
        if isinstance(selection, Vignettes_position) and selection.pos in self.cibles:
            self.set_courant(selection)
            if isinstance(self.joueur.magie_courante, Multi_cible):
                if selection.pos in self.cible:
                    self.cible.remove(selection.pos)
                else:
                    self.cible.append(selection.pos)
            else:
                if selection.pos != self.cible:
                    self.cible = selection.pos
                else:
                    self.cible = None
            self.set_tailles(self.tailles)

class Affichage_labyrinthe_case_parchemin(Affichage_labyrinthe):
    def __init__(self, controleur:Controleur):
        Affichage_labyrinthe.__init__(self, controleur.joueur)

        self.cibles = controleur.get_cibles_potentielles_cases(self.joueur.magie_parchemin, self.joueur)
        if isinstance(self.joueur.magie_parchemin, Multi_cible):
            self.cible = []
        else:
            self.cible = None

    def make_vignette(self, position: List[int], joueur: PJ, vue: Vue, position_vue: Position, taille: int):
        return Vignettes_position(position, joueur, vue, position_vue, taille, self.cible != None and self.cible != position_vue, position_vue not in self.cibles)
    
    def select(self, selection):
        if isinstance(selection, Vignettes_position) and selection.pos in self.cibles:
            self.set_courant(selection)
            if isinstance(self.joueur.magie_parchemin, Multi_cible):
                if selection.pos in self.cible:
                    self.cible.remove(selection.pos)
                else:
                    self.cible.append(selection.pos)
            else:
                if selection.pos != self.cible:
                    self.cible = selection.pos
                else:
                    self.cible = None
            self.set_tailles(self.tailles)

class Affichage_labyrinthe_direction_magie(Affichage_labyrinthe):
    def __init__(self, joueur: PJ):
        Affichage_labyrinthe.__init__(self, joueur)

        self.direction = HAUT

    def make_vignette(self, position: List[int], joueur: PJ, vue: Vue, position_vue: Position, taille: int):
        vignette = Vignettes_position(position, joueur, vue, position_vue, taille)
        if isinstance(self.joueur.magie_courante, Magie_cible_dirigee):
            if position_vue == self.joueur.cible_magie:
                vignette.objets.append(Vignette(position, taille, SKIN_DIRECTION, self.direction))
        else:
            if position_vue == self.joueur.position:
                vignette.objets.append(Vignette(position, taille, SKIN_DIRECTION, self.direction))
        return vignette

    def select(self, selection):
        if isinstance(selection, Vignettes_position):
            self.set_courant(selection)
            if isinstance(self.joueur.magie_courante, Magie_cible_dirigee):
                pos_magie = self.joueur.cible_magie
            else:
                pos_magie = self.joueur.position
            decalage = pos_magie-selection.pos
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

class Affichage_labyrinthe_direction_parchemin(Affichage_labyrinthe):
    def __init__(self, joueur: PJ):
        Affichage_labyrinthe.__init__(self, joueur)

        self.direction = HAUT

    def make_vignette(self, position: List[int], joueur: PJ, vue: Vue, position_vue: Position, taille: int):
        vignette = Vignettes_position(position, joueur, vue, position_vue, taille)
        if isinstance(self.joueur.magie_parchemin, Magie_cible_dirigee):
            if position_vue == self.joueur.cible_magie_parchemin:
                vignette.objets.append(Vignette(position, taille, SKIN_DIRECTION, self.direction))
        else:
            if position_vue == self.joueur.position:
                vignette.objets.append(Vignette(position, taille, SKIN_DIRECTION, self.direction))
        return vignette
    
    def select(self, selection):
        if isinstance(selection, Vignettes_position):
            self.set_courant(selection)
            if isinstance(self.joueur.magie_parchemin, Magie_cible_dirigee):
                pos_magie = self.joueur.cible_magie_parchemin
            else:
                pos_magie = self.joueur.position
            decalage = pos_magie-selection.pos
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

class Affichage_liste_menu_recettes(Liste_menu):
    vignette = Vignette_recette
    def __init__(self, joueur: PJ):
        self.joueur = joueur
        recettes = self.joueur.interlocuteur.get_recettes()
        Liste_menu.__init__(self)
        self.set_contenu([Vignette_recette(recette, 40, isinstance(self.courant, Vignette_recette) and recette != self.courant.recette, not self.joueur.inventaire.peut_fournir({eval(ingredient):recette["ingredients"][ingredient] for ingredient in recette["ingredients"]})) for recette in recettes])

class Affichage_liste_menu_ventes(Liste_menu):
    vignette = Vignette_vente
    def __init__(self, joueur: PJ):
        self.joueur = joueur
        items = self.joueur.inventaire.get_items()
        Liste_menu.__init__(self)
        self.set_contenu([Vignette_vente(item, 40, self.joueur.interlocuteur.get_prix_vente(item), self.joueur.interlocuteur.get_description(item), isinstance(self.courant, Vignette_vente) and item != self.courant.item, item in self.joueur.inventaire.get_equippement()) for item in items])

class Affichage_liste_menu_achats(Liste_menu):
    vignette = Vignette_achat
    def __init__(self, joueur: PJ):
        items = self.joueur.interlocuteur.get_marchandise()
        Liste_menu.__init__(self)
        self.set_contenu([Vignette_achat(eval(item["item"])(None), 40, item["prix"], item["description"], isinstance(self.courant, Vignette_achat) and item != self.courant.item, item["prix"]>self.joueur.argent) for item in items])

class Affichage_liste_menu_impregnations(Liste_menu):
    vignette = Vignette_magie
    def __init__(self, joueur: PJ):
        magies = self.joueur.interlocuteur.get_magies()
        Liste_menu.__init__(self)
        self.set_contenu([Vignette_magie(magie, 40, isinstance(self.courant, Vignette_magie) and magie != self.courant.magie, magie.cout_pm>self.joueur.interlocuteur.pm) for magie in magies])

class Affichage_liste_menu_auto_impregnations(Liste_menu):
    vignette = Vignette_magie
    def __init__(self, joueur: PJ):
        magies = self.joueur.get_magies()
        Liste_menu.__init__(self)
        self.set_contenu([Vignette_magie(magie, 40, isinstance(self.courant, Vignette_magie) and magie != self.courant.magie, magie.cout_pm>self.joueur.pm) for magie in magies])

class Affichage_replique(Pave):
    """Un élément avec beaucoup de texte. S'adapte sur plusieurs lignes si besoin"""
    def __init__(self, texte, replique):
        Pave.__init__(self, texte, "--> "+texte)
        self.replique = replique

class Affichage_skill(Cliquable, Pavage_horizontal):
    def __init__(self, skill:Skill_intrasec, fond=(0, 0, 0)):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.tailles = [0, 0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0, 0]
        self.fond = (0, 0, 0, 0)
        self.contenu:List[Affichable] = [None] #Les objets qu'il 'contient'
        self.skill = skill
        self.init()

    def init(self):
        self.set_contenu([Vignette([0, 0], 20, self.skill.get_skin()), Marge_verticale(), Texte(self.skill.nom)], [0, 5, 0])

class Affichage_classe(Cliquable, Pavage_horizontal):
    def __init__(self, classe:Classe, fond=(0, 0, 0)):
        self.objets:List[Affichable] = [] #Il peut quand même avoir des objets 'normaux'
        self.tailles = [0, 0] #La largeur et la hauteur (ou l'inverse ?)
        self.position = [0, 0]
        self.fond = (0, 0, 0, 0)
        self.contenu:List[Affichable] = [None] #Les objets qu'il 'contient'
        self.classe = classe
        self.init()

    def init(self):
        self.set_contenu([Vignette([0, 0], 20, self.classe.get_skin()), Marge_verticale(), Texte(self.classe.nom)], [0, 5, 0])




from Jeu.Entitee.Decors.Decors import *
from Jeu.Entitee.Item.Item import *
from Jeu.Entitee.Agissant.Humain.Humain import Humain
from Jeu.Effet.Effets_mouvement.Blocages import *
from Jeu.Effet.Effets import *
from Jeu.Systeme.Classe import *