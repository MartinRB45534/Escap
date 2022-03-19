import pygame

class Menu:
    #Une classe inutile
    #Les menus prennent en paramètre une liste d'options, avec texte explicatif et objets/classes pour la description et les images

    def termine(self):
        self.methode(self.choix)

class Menu_timed(Menu):
    """Un menu avec une limite de temps"""
    def __init__(self,temps):
        self.start_time = pygame.time.get_ticks()
        self.temps = temps

    def tick(self):
        return (pygame.time.get_ticks() - self.start_time)/self.temps #Si la proportion est supérieure à 1, le joueur arrète le menu

class Menu_direction(Menu):
    """Un menu destiné à choisir une direction"""
    def __init__(self,methode,position,magie,origine = "skill"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = None
        self.fin = False
        self.methode = methode

    def controle(self,touche):
        if touche == pygame.K_UP:
            self.choix = 0
        elif touche == pygame.K_RIGHT:
            self.choix = 1
        elif touche == pygame.K_DOWN:
            self.choix = 2
        elif touche == pygame.K_LEFT:
            self.choix = 3
        elif touche == pygame.K_RETURN and self.choix != None:
            self.fin = True

class Menu_direction_timed(Menu_direction,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_direction.__init__(self,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)

class Menu_case(Menu):
    """Un menu destiné à choisir une case"""
    def __init__(self,cases,methode,position,magie = None,origine = "dialogue"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = None
        self.fin = False
        self.methode = methode
        self.cases = cases
        self.element_courant = [position[0],position[1],position[2]]

    def controle(self,touche):
        if touche == pygame.K_UP:
            self.element_courant[2]-=1
        elif touche == pygame.K_RIGHT:
            self.element_courant[1]+=1
        elif touche == pygame.K_DOWN:
            self.element_courant[2]+=1
        elif touche == pygame.K_LEFT:
            self.element_courant[1]-=1
        elif touche == pygame.K_SPACE:
            self.choix = (self.element_courant[0],self.element_courant[1],self.element_courant[2])
        elif touche == pygame.K_RETURN:
            if self.choix == None:
                self.choix = (self.element_courant[0],self.element_courant[1],self.element_courant[2])
            self.fin = True

class Menu_multi_case(Menu):
    """Un menu destiné à choisir plusieurs case"""
    def __init__(self,cases,methode,position,magie,origine = "skill"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = []
        self.fin = False
        self.methode = methode
        self.cases = cases
        self.element_courant = [position[0],position[1],position[2]]

    def controle(self,touche):
        if touche == pygame.K_UP:
            self.element_courant[2]-=1
        elif touche == pygame.K_RIGHT:
            self.element_courant[1]+=1
        elif touche == pygame.K_DOWN:
            self.element_courant[2]+=1
        elif touche == pygame.K_LEFT:
            self.element_courant[1]-=1
        elif touche == pygame.K_SPACE:
            choix = (self.element_courant[0],self.element_courant[1],self.element_courant[2])
            if choix in self.choix:
                self.choix.remove(choix)
            else:
                self.choix.append(choix)
        elif touche == pygame.K_RETURN:
            if self.choix == []:
                self.choix = [(self.element_courant[0],self.element_courant[1],self.element_courant[2])]
            self.fin = True

class Menu_case_timed(Menu_case,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,cases,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_case.__init__(self,cases,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)

class Menu_multi_case_timed(Menu_multi_case,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,cases,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_multi_case.__init__(self,cases,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)

class Menu_agissant(Menu):
    """Un menu destiné à choisir un agissant"""
    def __init__(self,agissants,methode,position,magie = None,origine = "dialogue"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = None
        self.fin = False
        self.methode = methode
        self.agissants = agissants
        self.element_courant = 0

    def controle(self,touche):
        if touche == pygame.K_UP:
            if self.element_courant == 0:
                self.element_courant = len(self.agissants)
            self.element_courant-=1
        elif touche == pygame.K_DOWN:
            self.element_courant+=1
            if self.element_courant == len(self.agissants):
                self.element_courant = 0
        elif touche == pygame.K_SPACE:
            self.choix = self.agissants[self.element_courant]
        elif touche == pygame.K_RETURN:
            if self.choix == None:
                self.choix = self.agissants[self.element_courant]
            self.fin = True

class Menu_multi_agissant(Menu):
    """Un menu destiné à choisir plusieurs agissants"""
    def __init__(self,agissants,methode,position,magie,origine = "skill"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = None
        self.fin = False
        self.methode = methode
        self.agissants = agissants
        self.element_courant = 0

    def controle(self,touche):
        if touche == pygame.K_UP:
            if self.element_courant == 0:
                self.element_courant = len(self.agissants)
            self.element_courant-=1
        elif touche == pygame.K_DOWN:
            self.element_courant+=1
            if self.element_courant == len(self.agissants):
                self.element_courant = 0
        elif touche == pygame.K_SPACE:
            choix = self.agissants[self.element_courant]
            if choix in self.choix:
                self.choix.remove(choix)
            else:
                self.choix.append(choix)
        elif touche == pygame.K_RETURN:
            if self.choix == None:
                self.choix = [self.agissants[self.element_courant]]
            self.fin = True

class Menu_agissant_timed(Menu_agissant,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,agissants,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_agissant.__init__(self,agissants,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)

class Menu_multi_agissant_timed(Menu_multi_agissant,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,agissants,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_multi_agissant.__init__(self,agissants,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)

class Menu_item(Menu):
    """Un menu destiné à choisir un item"""
    def __init__(self,items,methode,position,magie = None,origine = "dialogue"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = None
        self.fin = False
        self.methode = methode
        self.items = items
        self.element_courant = 0

    def controle(self,touche):
        if touche == pygame.K_UP:
            if self.element_courant == 0:
                self.element_courant = len(self.agissants)
            self.element_courant-=1
        elif touche == pygame.K_DOWN:
            self.element_courant+=1
            if self.element_courant == len(self.agissants):
                self.element_courant = 0
        elif touche == pygame.K_SPACE:
            self.choix = self.items[self.element_courant]
        elif touche == pygame.K_RETURN:
            if self.choix == None:
                self.choix = self.items[self.element_courant]
            self.fin = True

class Menu_multi_item(Menu):
    """Un menu destiné à choisir plusieurs items"""
    def __init__(self,items,methode,position,magie,origine = "skill"): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        self.magie = magie #Est-ce qu'on a un objet ou sa classe ?
        self.origine = origine
        self.position = position
        self.choix = None
        self.fin = False
        self.methode = methode
        self.items = items
        self.element_courant = 0

    def controle(self,touche):
        if touche == pygame.K_UP:
            if self.element_courant == 0:
                self.element_courant = len(self.agissants)
            self.element_courant-=1
        elif touche == pygame.K_DOWN:
            self.element_courant+=1
            if self.element_courant == len(self.agissants):
                self.element_courant = 0
        elif touche == pygame.K_SPACE:
            choix = self.items[self.element_courant]
            if choix in self.choix:
                self.choix.remove(choix)
            else:
                self.choix.append(choix)
        elif touche == pygame.K_RETURN:
            if self.choix == None:
                self.choix = [self.items[self.element_courant]]
            self.fin = True

class Menu_item_timed(Menu_item,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,items,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_item.__init__(self,items,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)

class Menu_multi_item_timed(Menu_multi_item,Menu_timed):
    """Un menu destiné à choisir une direction"""
    def __init__(self,items,methode,position,magie,origine,temps): #/!\ Remplacer la position par la vue, une fois que les vues contiendront plus d'information
        """magie, la magie qu'on cherche à lancer
           origine, selon que la magie est castée par le skill ou depuis un parchemin
           position, l'endroit du labyrinthe à afficher"""
        Menu_multi_item.__init__(self,items,methode,position,magie,origine)
        Menu_timed.__init__(self,temps)
