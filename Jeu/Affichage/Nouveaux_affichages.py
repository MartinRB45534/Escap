from operator import itemgetter
from Jeu.Affichage.Affichage import *
from Jeu.Skins.Skins import *
from math import ceil

class Affichage_principal(Wrapper):
    """L'element principal de l'affichage. Contient tout ce qui apparait à l'écran."""
    
    def __init__(self,controleur,tailles):
        self.controleur = controleur
        self.objets = []
        self.contenu = None
        self.courant = True
        self.fond = (0,0,0)
        self.tailles = tailles
        self.position = [0,0]
        self.phase = controleur.phase
        self.evenement = controleur.joueur.event
        self.inits[self.phase](self)

    def init_tour(self):
        """Crée l'affichage tel qu'il est pendant les phases de jeu normales"""
        
        contenu = Pavage_horizontal()
        diptique = Pavage_vertical()
        triptique = Pavage_horizontal()
        triptique.set_contenu([Affichage_gauche(self.controleur.joueur),Marge_verticale(),Affichage_centre(self.controleur.joueur),Marge_verticale(),Affichage_droite_tour(self.controleur)],[-1,5,-2,5,-1])
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
        triptique.set_contenu([Affichage_gauche(self.controleur.joueur),Marge_verticale(),Affichage_centre(self.controleur.joueur),Marge_verticale(),Affichage_droite_dialogue(self.controleur.joueur.interlocuteur)],[-1,5,-2,5,-1])
        diptique.set_contenu([Marge_horizontale(),Titre(self.controleur),Marge_horizontale(),triptique,Marge_horizontale()],[5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),diptique,Marge_verticale()],[5,-1,5])
        contenu.set_tailles(self.tailles)
        self.contenu = contenu
        self.fond = (0,0,0) #S'il est modifié dans un autre cas

    def init_evenement(self):
        self.evenement = self.controleur.joueur.event
        self.inits_evenements[self.evenement](self)

    def update(self):
        if self.phase != self.controleur.phase: #On a changé de phase
            self.phase = self.controleur.phase
            self.inits[self.phase](self)
            self.set_tailles(self.tailles)
        elif self.phase == EVENEMENT and self.evenement != self.controleur.joueur.event:
            self.evenement = self.controleur.joueur.event
            self.inits_evenements[self.evenement](self)
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
        else:
            self.courant = False

    def navigue(self,direction):
        pass

    inits={
        TOUR:init_tour,
        EVENEMENT:init_evenement,
    }
    inits_evenements={
        DIALOGUE:init_dialogue,
    }

class Affichage_gauche(Wrapper):
    def __init__(self,joueur):
        self.joueur = joueur
        self.objets = []
        self.contenu = []
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
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
        self.courant = Affichage_stats(self.joueur)
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),self.courant,Marge_horizontale(),Affichage_inventaire_ferme(self.joueur),Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,-1,5,0,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_inventaire(self):
        self.courant = Affichage_inventaire(self.joueur)
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        triptique.set_contenu([Marge_horizontale(),Affichage_stats_ferme(self.joueur),Marge_horizontale(),self.courant,Marge_horizontale(),Affichage_classe_ferme(self.joueur.classe_principale),Marge_horizontale()],[5,0,5,-1,5,0,5]) # /!\ Remplacer par Affichage_classe_principale_ferme
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_classe(self):
        self.courant = Affichage_classe(self.joueur.classe_principale)
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
            if isinstance(clique,Affichage_inventaire_ferme): #On veut ouvrir l'affichage des stats
                self.init_inventaire()
            if isinstance(clique,Affichage_classe_ferme): #On veut ouvrir l'affichage des stats
                self.init_classe()
            self.set_tailles(self.tailles)
        else:
            self.init_gauche()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False
    
    # def affiche(self,screen,frame,frame_par_tour):
    #     courant = pygame.time.get_ticks()
    #     Wrapper.affiche(self,screen,frame,frame_par_tour)
    #     new_courant = pygame.time.get_ticks()
    #     print("Gauche")
    #     print(new_courant-courant)

class Affichage_centre(Wrapper):
    def __init__(self,joueur):
        self.joueur = joueur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (0,0,0)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_centre()

    def init_centre(self):
        contenu = Pavage_horizontal()
        monoptique = Pavage_vertical()
        monoptique.set_contenu([Marge_horizontale(),Affichage_labyrinthe(self.joueur),Marge_horizontale()],[5,-1,5])
        contenu.set_contenu([Marge_verticale(),monoptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (0,0,0)
    
    # def affiche(self,screen,frame,frame_par_tour):
    #     courant = pygame.time.get_ticks()
    #     Wrapper.affiche(self,screen,frame,frame_par_tour)
    #     new_courant = pygame.time.get_ticks()
    #     print("Centre")
    #     print(new_courant-courant)

class Affichage_droite_tour(Wrapper):
    def __init__(self,controleur):
        self.controleur = controleur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        diptique.set_contenu([Marge_verticale(),Affichage_allies(self.controleur),Marge_verticale(),Affichage_ennemis(self.controleur),Marge_verticale()],[5,-1,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_allie(self):
        allie = self.courant.courant.agissant
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        diptique.set_contenu([Marge_verticale(),self.courant,Marge_verticale(),Affichage_ennemis(self.controleur),Marge_verticale()],[5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(allie.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def init_ennemi(self):
        ennemi = self.courant.courant.agissant
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        monoptique = Pavage_horizontal()
        diptique.set_contenu([Marge_verticale(),Affichage_allies(self.controleur),Marge_verticale(),self.courant,Marge_verticale()],[5,-1,5,-1,5])
        monoptique.set_contenu([Marge_verticale(),Paves(ennemi.get_texte_descriptif()),Marge_verticale()],[5,-1,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5,0,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Affichage_allies):
                self.courant = clique
                self.init_allie()
            if isinstance(clique,Affichage_ennemis):
                self.courant = clique
                self.init_ennemi()
            if isinstance(clique,Paves):
                self.courant = clique
                # "Utiliser" l'agissant courant
            self.set_tailles(self.tailles)
        else:
            self.courant = False
            self.init_droite()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False
    
    # def affiche(self,screen,frame,frame_par_tour):
    #     courant = pygame.time.get_ticks()
    #     Wrapper.affiche(self,screen,frame,frame_par_tour)
    #     new_courant = pygame.time.get_ticks()
    #     print("Droite")
    #     print(new_courant-courant)

class Affichage_droite_dialogue(Wrapper):
    def __init__(self,interlocuteur):
        self.interlocuteur = interlocuteur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.courant = False
        self.fond = (255,255,255)
        self.tailles = [0,0]
        self.position = [0,0]
        self.replique = interlocuteur.replique
        self.init_droite()

    def init_droite(self):
        contenu = Pavage_horizontal()
        triptique = Pavage_vertical()
        liste = Liste_verticale()
        repliques = [Affichage_replique(self.interlocuteur.get_replique(replique),replique) for replique in self.interlocuteur.repliques]
        liste.set_contenu([repliques[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(repliques)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(repliques)*2)])
        triptique.set_contenu([Marge_horizontale(),Affichage_perso(self.interlocuteur),Marge_horizontale(),Pave(self.interlocuteur.get_replique(self.interlocuteur.replique)),Marge_horizontale(),liste,Marge_horizontale()],[5,0,5,0,5,-1,5])
        contenu.set_contenu([Marge_verticale(),triptique,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (255,255,255)

    def update(self):
        if self.replique != self.interlocuteur.replique:
            self.replique = self.interlocuteur.replique
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
    
    # def affiche(self,screen,frame,frame_par_tour):
    #     courant = pygame.time.get_ticks()
    #     Wrapper.affiche(self,screen,frame,frame_par_tour)
    #     new_courant = pygame.time.get_ticks()
    #     print("Droite")
    #     print(new_courant-courant)

class Affichage_stats_ferme(Wrapper):
    def __init__(self,joueur):
        self.joueur = joueur
        self.objets = []
        self.contenu = []
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
    def __init__(self,joueur):
        self.joueur = joueur
        self.objets = []
        self.contenu = []
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

class Affichage_inventaire_ferme(Wrapper):
    def __init__(self,joueur):
        self.joueur = joueur
        self.objets = []
        self.contenu = []
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
    def __init__(self,joueur):
        self.joueur = joueur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_vertical()
        monoptique = Liste_horizontale()
        liste_v = Liste_verticale()
        vignettes = [Vignette([0,0],40,classe.get_image()) for classe in self.joueur.inventaire.items.keys()]
        liste_v.set_contenu([vignettes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(vignettes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(vignettes)*2)])
        monoptique.set_contenu([Marge_verticale(),liste_v,Marge_verticale()],[5,0,5])
        contenu.set_contenu([Marge_horizontale(),monoptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_classe(self):
        contenu = Pavage_vertical()
        diptique = Pavage_horizontal()
        liste_v = Liste_verticale()
        liste_i = Liste_verticale()
        vignettes = [Vignette([0,0],40,classe.get_image()) for classe in self.joueur.inventaire.items.keys()]
        items = [Vignette_item([0,0],self.joueur.controleur[ID],40) for ID in self.joueur.inventaire.items[[classe for classe in self.joueur.inventaire.items.keys() if classe.get_image() == self.courant.skin][0]]]
        liste_v.set_contenu([vignettes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(vignettes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(vignettes)*2)])
        liste_i.set_contenu([items[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(items)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(items)*2)])
        diptique.set_contenu([Marge_verticale(),liste_v,Marge_verticale(),liste_i,Marge_verticale()],[5,0,5,0,5])
        contenu.set_contenu([Marge_horizontale(),diptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_item(self):
        contenu = Pavage_vertical()
        triptique = Pavage_horizontal()
        liste_v = Liste_verticale()
        liste_i = Liste_verticale()
        vignettes = [Vignette([0,0],40,classe.get_image()) for classe in self.joueur.inventaire.items.keys()]
        items = [Vignette_item([0,0],self.joueur.controleur[ID],40) for ID in self.joueur.inventaire.items[[classe for classe in self.joueur.inventaire.items.keys() if issubclass(self.courant.item.get_classe(),classe)][0]]]
        liste_v.set_contenu([vignettes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(vignettes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(vignettes)*2)])
        liste_i.set_contenu([items[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(items)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(items)*2)])
        triptique.set_contenu([Marge_verticale(),liste_v,Marge_verticale(),liste_i,Marge_verticale(),Paves(self.courant.item.get_description(0)),Marge_verticale()],[5,0,5,0,5,-1,5])
        contenu.set_contenu([Marge_horizontale(),triptique,Marge_horizontale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Vignette): #On veut ouvrir l'affichage des stats
                self.courant = clique
                self.init_classe()
            if isinstance(clique,Vignette_item): #On veut ouvrir l'affichage des stats
                if clique == self.courant:
                    self.joueur.inventaire.utilise_item(self.courant.item.ID)
                else:
                    self.courant = clique
                    self.init_item()
            self.set_tailles(self.tailles)
        else:
            self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_classe_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets = []
        self.contenu = []
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

class Affichage_classe(Wrapper):
    def __init__(self,classe):
        self.classe = classe
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
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
        liste.set_contenu([Marge_horizontale(),Affichage_intrasecs(self.classe),Marge_horizontale(),Affichage_skills_ferme(self.classe),Marge_horizontale(),Affichage_classes_ferme(self.classe),Marge_horizontale()],[5,-1,5,0,5,0,5])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_skills(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(),Affichage_intrasecs_ferme(self.classe),Marge_horizontale(),Affichage_skills(self.classe),Marge_horizontale(),Affichage_classes_ferme(self.classe),Marge_horizontale()],[5,0,5,-1,5,0,5])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_classes(self):
        contenu = Pavage_horizontal()
        liste = Pavage_vertical()
        liste.set_contenu([Marge_horizontale(),Affichage_intrasecs_ferme(self.classe),Marge_horizontale(),Affichage_skills_ferme(self.classe),Marge_horizontale(),Affichage_classes(self.classe),Marge_horizontale()],[5,0,5,0,5,-1,5])
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
            self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_intrasecs_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets = []
        self.contenu = []
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
    def __init__(self,classe):
        self.classe = classe
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        skills = [Texte(skill.nom) for skill in self.classe.skills_intrasecs]
        liste.set_contenu([skills[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(skills)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(skills)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_skills_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets = []
        self.contenu = []
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
    def __init__(self,classe):
        self.classe = classe
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        skills = [Texte(skill.nom) for skill in self.classe.skills]
        liste.set_contenu([skills[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(skills)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(skills)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

class Affichage_classes_ferme(Wrapper):
    def __init__(self,classe):
        self.joueur = classe
        self.objets = []
        self.contenu = []
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
    def __init__(self,classe):
        self.classe = classe
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        self.courant = True
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        classes = [Texte(classe.nom) for classe in self.classe.sous_classes]
        liste.set_contenu([classes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(classes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(classes)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def init_sous_classe(self):
        self.courant = Affichage_classe([classe for classe in self.classe.sous_classes if classe.nom == self.courant.texte][0])
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        classes = [Texte(classe.nom) for classe in self.classe.sous_classes]
        liste.set_contenu([self.courant if self.classe.sous_classes[i//2] == self.courant.classe else classes[i//2] if i%2==0 else Marge_horizontale() for i  in range(-1,len(classes)*2)],[0 if i%2==0 else 5 for i  in range(-1,len(classes)*2)])
        contenu.set_contenu([Marge_verticale(),liste,Marge_verticale()],[5,-1,5])
        self.contenu = contenu
        self.fond = (200,200,200)

    def clique(self,position):
        clique = self.clique_wrapper(position)
        if clique is self:
            self.courant = True
        elif clique:
            if isinstance(clique,Texte):
                self.courant = clique
                self.init_sous_classe()
            self.set_tailles(self.tailles)
        else:
            self.init()
            self.set_tailles(self.tailles)
        if clique:
            return self
        return False

class Affichage_allies_ferme(Wrapper):
    def __init__(self,controleur):
        self.controleur = controleur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_allie([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).corps.keys()]
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
            self.set_tailles(self.tailles)
        else:
            self.init()
            self.set_tailles(self.tailles)
            return self
        return False

class Affichage_allies(Wrapper):
    def __init__(self,controleur):
        self.controleur = controleur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_allie([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_corps_vus()]
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
            return self
        else:
            self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_ennemis_ferme(Wrapper):
    def __init__(self,controleur):
        self.controleur = controleur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_ennemi([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).ennemis.keys()]
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
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
            self.set_tailles(self.tailles)
        else:
            self.init()
            self.set_tailles(self.tailles)
            return self
        return False

class Affichage_ennemis(Wrapper):
    def __init__(self,controleur):
        self.controleur = controleur
        self.objets = []
        self.contenu = []
        self.courant = False
        self.fond = (200,200,200)
        self.tailles = [0,0]
        self.position = [0,0]
        self.init()

    def init(self):
        contenu = Pavage_horizontal()
        liste = Liste_verticale()
        allies = [Vignette_ennemi([0,0],self.controleur[ID],self.controleur.joueur.esprit,40) for ID in self.controleur.get_esprit(self.controleur.joueur.esprit).get_ennemis_vus()]
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
            if isinstance(clique,Vignette_ennemi):
                self.courant = clique
            return self
        else:
            self.init()
            self.set_tailles(self.tailles)
        return False

class Affichage_PV(Affichable):
    def __init__(self,joueur):
        self.joueur = joueur
        self.position = [0,0]
        self.tailles = [0,10]

    def affiche(self,screen,frame,frame_par_tour):
        pygame.draw.rect(screen,(255,160,160),(self.position[0],self.position[1],self.tailles[0],10))
        pygame.draw.rect(screen,(255,0,0),(self.position[0],self.position[1],(self.tailles[0]*self.joueur.pv)//self.joueur.pv_max,10))

    def get_tailles(self,tailles):
        return [tailles[0],self.tailles[1]]

class Affichage_PM(Affichable):
    def __init__(self,joueur):
        self.joueur = joueur
        self.position = [0,0]
        self.tailles = [0,10]

    def affiche(self,screen,frame,frame_par_tour):
        pygame.draw.rect(screen,(160,255,255),(self.position[0],self.position[1],self.tailles[0],10))
        pygame.draw.rect(screen,(32,255,255),(self.position[0],self.position[1],(self.tailles[0]*self.joueur.pm)//self.joueur.pm_max,10))

    def get_tailles(self,tailles):
        return [tailles[0],self.tailles[1]]

class Titre(Affichable):
    """Un élément qui est juste un bout de texte."""
    def __init__(self,controleur):
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
                entitee = joueur.controleur.get_entitee(ID)
                if issubclass(entitee.get_classe(),Agissant):
                    for skin in entitee.get_skins_vue():
                        skin.dessine_toi(screen,(x,y),(largeur,hauteur),frame,frame_par_tour)
                    break

class Affichage_labyrinthe(Final,Affichage,Proportionnel):
    def __init__(self,joueur):
        self.objets = []
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
            vue_x = self.joueur.position.x - distance
            vue_y = self.joueur.position.y - distance
            nb_cases = distance*2 + 1
            taille_case = int(min(self.tailles) // (nb_cases-1))
            hauteur_exploitee = taille_case * nb_cases
            marge = (min(self.tailles) - hauteur_exploitee) // 2
            self.nb_cases = nb_cases
            marge_haut = self.position[1]+marge#+taille_case//2
            for j in range(self.nb_cases):
                marge_gauche = self.position[0]+marge#+taille_case//2
                for i in range(self.nb_cases):
                    pos = Decalage(vue_x+i,vue_y+j)
                    position = [marge_gauche,marge_haut]
                    if pos in self.joueur.vue:
                        vignette = Vignettes_position(position,self.joueur,self.joueur.vue[pos],taille_case)
                    else:
                        vignette  = Vignette(position,taille_case,SKIN_BROUILLARD)
                    self.objets.append(vignette)
                    marge_gauche += taille_case
                marge_haut += taille_case
        else:
            for objet in self.objets:
                objet.update()

class Vignette_item(Final,Affichage):
    def __init__(self,position,item,taille,direction=None):
        self.item = item
        if direction == None:
            direction = item.get_direction()
        self.objets = [] #La liste des objets à afficher
        self.tailles = [taille,taille]
        self.position = position
        self.objets.append(Vignette(position,taille,item.get_skin(),direction)) #Avoir éventuellement la tête dans une autre direction ?
        for effet in item.effets:
            if effet.affiche:
                self.objets.append(Vignette(position,taille,effet.get_skin(),direction))

class Vignettes_agissant(Final,Affichage):
    def __init__(self,position,agissant,taille):
        self.agissant = agissant
        self.objets = [] #La liste des objets à afficher
        direction = agissant.get_direction()
        arme = agissant.inventaire.arme
        self.tailles = [taille,taille]
        self.position = position
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
    def __init__(self,position,joueur,vue,taille):
        self.position = position
        self.tailles = [taille,taille]
        self.objets = []
        self.objets.append(Vignette_case(position,joueur,vue,taille))
        if vue[1]>0:
            entitees = vue[6]
            agissant = None
            for ID_entitee in entitees:
                entitee = joueur.controleur.get_entitee(ID_entitee)
                if issubclass(entitee.get_classe(),Item):
                    self.objets.append(Vignette_item(position,entitee,taille)) #La direction est surtout utile pour les projectiles, sinon ils devraient tous être dans le même sens.
                elif issubclass(entitee.get_classe(),Decors):
                    self.objets.append(Vignette(position,taille,entitee.get_skin()))
                else:
                    agissant = entitee
            if agissant != None: #Enfin l'agissant (s'il y en a un)
                self.objets.append(Vignettes_agissant(position,agissant,taille))
            if vue[7] != []:
                esprit = joueur.controleur.get_esprit(joueur.esprit)
                if any([effet[2] in esprit.corps.keys() for effet in vue[7]]):
                    self.objets.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE_ALLIE))
                else:
                    self.objets.append(Vignette(position,taille,SKIN_ATTAQUE_DELAYEE))

class Vignette_case(Final,Affichage):
    def __init__(self,position,joueur,vue,taille):
        self.position = position
        self.tailles = [taille,taille]
        self.objets = []
        if vue[1]==0:
            self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
        elif vue[1]==-1: #On a affaire à un case accessible mais pas vue
            self.objets.append(Vignette(position,taille,SKIN_BROUILLARD))
            for i in DIRECTIONS:
                if vue[5][i][0]:
                    pos_voisin = vue[0]+i
                    if pos_voisin in joueur.vue and joueur.vue[pos_voisin][1]>0:
                        self.objets.append(Vignette(position,taille,SKIN_MUR_BROUILLARD,i))
        else:
            if vue[4]==0: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE)) #La case en premier, donc en bas
            elif vue[4]==1: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_1)) #La case en premier, donc en bas
            elif vue[4]==2: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_2)) #La case en premier, donc en bas
            elif vue[4]==3: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_3)) #La case en premier, donc en bas
            elif vue[4]==4: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_4)) #La case en premier, donc en bas
            elif vue[4]==5: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_5)) #La case en premier, donc en bas
            elif vue[4]==6: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_6)) #La case en premier, donc en bas
            elif vue[4]==7: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette(position,taille,SKIN_CASE_7)) #La case en premier, donc en bas
            elif vue[4]==8: #On teste le code de la case pour déterminer son image
                self.objets.append(Vignette([0,0],taille,SKIN_CASE_8)) #La case en premier, donc en bas
            case = joueur.controleur.get_case(vue[0])
            for i in DIRECTIONS:
                mur = case.get_mur_dir(i)
                for effet in mur.effets:
                    if effet.affiche:
                        if isinstance(effet,Porte) :
                            self.objets.append(Vignette(position,taille,effet.get_skin(joueur.get_clees()),i))
                        elif isinstance(effet,(Mur_plein,Mur_impassable)) :
                            self.objets.append(Vignette(position,taille,effet.get_skin(vue[4]),i))
                        else :
                            self.objets.append(Vignette(position,taille,effet.get_skin(),i))
            for effet in case.effets:
                if effet.affiche:
                    self.objets.append(Vignette(position,taille,effet.get_skin()))

class Vignette_allie(Final,Affichage):
    def __init__(self,position,agissant,esprit,taille):
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.objets = []
        self.tailles = [taille,taille]
        self.position = position
        self.objets.append(Vignettes_agissant(position,agissant,taille))
        for statut in agissant.get_skins_statuts():
            self.objets.append(Vignette(position,taille,statut))

class Vignette_ennemi(Final,Affichage):
    def __init__(self,position,agissant,esprit,taille):
        self.position = position
        self.agissant = agissant
        self.esprit = esprit
        self.courant = False
        self.objets = []
        self.tailles = [taille,taille]
        self.position = position
        self.objets.append(Vignettes_agissant(position,agissant,taille))


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







    # def ajuste_tailles(self,hauteur,largeur):
    #     # On détermine les proportions des différentes parties de l'affichage
    #     self.tailles = [largeur,hauteur] # (Ou l'inverse ?)
    #     # Pour comparaison, le petit écran de mon ASUS contenait du (1350,690)
    #     # /!\ Gérer le cas où les tailles seraient trop petites
        
    #     # On va garder les calculs de l'affichage précédent pour l'instant
    #     hauteur_exploitable = ((hauteur - 30)//20)*20
    #     largeur_exploitable = ((largeur - 30)//20)*20
    #     if hauteur_exploitable * 2 > largeur_exploitable :
    #         hauteur_exploitable = largeur_exploitable / 2
    #     elif hauteur_exploitable * 2 < self.largeur_exploitable :
    #         largeur_exploitable = hauteur_exploitable * 2
    #     else :
    #         print("Dimensions parfaites !")
    #     marge_gauche = ((largeur - largeur_exploitable) // 2) - 10
    #     marge_haut = ((hauteur - hauteur_exploitable) // 2) + -10
    #     largeur_rectangles = (largeur_exploitable) / 4
    #     position_debut_x_rectangle_1 = marge_gauche
    #     position_fin_x_rectangle_1 = position_debut_x_rectangle_1 + largeur_rectangles
    #     position_debut_x_carre = position_fin_x_rectangle_1 + 10
    #     position_fin_x_carre = position_debut_x_carre + hauteur_exploitable
    #     position_debut_x_rectangle_2 = position_fin_x_carre + 10
    #     position_fin_x_rectangle_2 = position_debut_x_rectangle_2 + largeur_rectangles
    #     position_debut_y_titre = marge_haut
    #     position_debut_y_rectangles_et_carre = marge_haut + 20
    #     position_fin_y_rectangles_et_carre = position_debut_y_rectangles_et_carre + hauteur_exploitable

    #     self.contenu[0].set_position([position_debut_x_rectangle_1,position_debut_y_rectangles_et_carre])
    #     self.contenu[0].set_tailles((hauteur_exploitable,largeur_rectangles))
    #     self.contenu[1].set_position([position_debut_x_carre,position_debut_y_rectangles_et_carre])
    #     self.contenu[1].set_tailles((hauteur_exploitable,hauteur_exploitable))
    #     self.contenu[2].set_position([position_debut_x_rectangle_2,position_debut_y_rectangles_et_carre])
    #     self.contenu[2].set_tailles((hauteur_exploitable,largeur_rectangles))




from Jeu.Entitee.Decors.Decors import *
from Jeu.Entitee.Item.Item import *
from Jeu.Entitee.Agissant.Humain.Humain import Humain
from Jeu.Effet.Effets_mouvement.Blocages import *
from Jeu.Effet.Effets import *
from Jeu.Systeme.Classe import *