import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1350, 690))

from Jeu import *
from Jeu.Général import *
from Jeu.Constantes import *
#print("Importation : check")

global controleur

run = True

def quitte(): #À améliorer !
    run = False

def main():
    global controleur
    controleur = Controleur() #Un objet qui permet d'accéder à tout et n'importe quoi. Il possède les dictionnaires des labyrinthes et des entitées.
    #print("Controleur : check")
    controleur.jeu(screen)
    joueur = controleur.entitees[2]
    while run == True :
        #Pour l'instant c'est un jeu rudimentaire, le joueur est le seul agissant et teste ses différents skills.
        agissants,items,labs,esprits = controleur.get_agissants_items_labs_esprits()
        
        #Découvrons le déroulé d'un tour avec main-sama :
##        print("debut")
##        clock.tick()
##        print(clock.get_time())
        #On débute le tour
        for agissant in agissants :
            controleur.make_vue(agissant)
            agissant.debut_tour()
##        print("debut agissant")
##        clock.tick()
##        print(clock.get_time())
        for item in items :
            item.debut_tour()
##        print("debut items")
##        clock.tick()
##        print(clock.get_time())
        for lab in labs:
            lab.debut_tour()
##        print("debut labs")
##        clock.tick()
##        print(clock.get_time())
        for esprit in esprits:
            esprit.debut_tour()
##        print("debut esprit")
##        clock.tick()
##        print(clock.get_time())

        #Le main gère les inputs

        events = pygame.event.get() #Les événements qui ont eu lieu depuis le dernier tour.
        for event in events :
            if event.type == pygame.QUIT :
                quitte()
            elif event.type == pygame.VIDEORESIZE :
                joueur.affichage.recalcule_zones()
            elif event.type == pygame.KEYDOWN:
                joueur.controle_zones(event.key)

        keys = pygame.key.get_pressed()
        joueur.controle(keys)

        #On a quelques effets supplémentaires...
        for agissant in agissants :
            agissant.post_decision()

        #Les agissants méritent leur nom :
        for agissant in agissants :
            while agissant.latence <= 0 and agissant.skill_courant != None : #Certains peuvent jouer plusieurs fois par tour !
                controleur.fait_agir(agissant)
                agissant.on_action()

        for item in items :
            while item.hauteur > 0 and item.latence <= 0:
                controleur.fait_voler(item)

        #On agit sur les actions (principalement des boosts sur les attaques, puis les attaques elles-mêmes sont lancées)
        for agissant in agissants :
            agissant.post_action()
##        print("autres")
##        clock.tick()
##        print(clock.get_time())

        #Le lab agit sur les actions (principalement sur les attaques, pour protéger les occupants de certaines cases)
        for lab in labs:
            lab.post_action()
##        print("post action lab")
##        clock.tick()
##        print(clock.get_time())

        #Les agissants agissent sur les attaques (s'en protègent, puis les subissent)
        for agissant in agissants :
            agissant.pre_attack()

        #On termine le tour
        for agissant in agissants :
            agissant.fin_tour()
        for item in items :
            item.fin_tour()
        for lab in labs:
            lab.fin_tour()
        for esprit in esprits:
            esprit.fin_tour()
##        print("autres")
##        clock.tick()
##        print(clock.get_time())

        # Actualisation de l'affichage
        pygame.display.flip()
##        print("affichage")
##        clock.tick()
##        print(clock.get_time())
        # 20 fps
        clock.tick(20)

    pygame.quit()

def init_duel(esprit1,esprit2,niveau_1=1,niveau_2=1,tailles_lab=(20,20),vide=True,vue=False):
    global controleur
    controleur = Controleur() #Un objet qui permet d'accéder à tout et n'importe quoi. Il possède les dictionnaires des labyrinthes et des entitées.
    #print("Controleur : check")
    controleur.duel(esprit1,esprit2,niveau_1,niveau_2,tailles_lab,vide,vue,screen)
    return reprend_duel()

def reprend_duel():
    global controleur
    res = None
    run = True
    while run :
        agissants,items,labs,esprits = controleur.get_agissants_items_labs_esprits()
        
        #Découvrons le déroulé d'un tour avec main-sama :
        #On débute le tour
        for agissant in agissants :
            controleur.make_vue(agissant)
            agissant.debut_tour()
        for item in items :
            item.debut_tour()
        for lab in labs:
            lab.debut_tour()
        for esprit in esprits:
            esprit.debut_tour()

        #On a quelques effets supplémentaires...
        for agissant in agissants :
            agissant.post_decision()

        #Les agissants méritent leur nom :
        for agissant in agissants :
            while agissant.latence <= 0 and agissant.skill_courant != None : #Certains peuvent jouer plusieurs fois par tour !
                controleur.fait_agir(agissant)
                agissant.on_action()

        #Il faudra aussi déplacer les items !

        #On agit sur les actions (principalement des boosts sur les attaques, puis les attaques elles-mêmes sont lancées)
        for agissant in agissants :
            agissant.post_action()

        #Le lab agit sur les actions (principalement sur les attaques, pour protéger les occupants de certaines cases)
        for lab in labs:
            lab.post_action()

        #Les agissants agissent sur les attaques (s'en protègent, puis les subissent)
        for agissant in agissants :
            agissant.pre_attack()

        #On termine le tour
        for agissant in agissants :
            agissant.fin_tour()
        for item in items :
            item.fin_tour()
        for lab in labs:
            lab.fin_tour()
        for esprit in esprits:
            esprit.fin_tour()

        
        pygame.display.flip()

        if len(esprits) == 1 :
            res = esprits[0].nom
            survivants = agissants
            run = False
        elif controleur.nb_tours >= 2000:
            res = "match nul"
            survivants = agissants
            run = False

        #Pas d'affichage

    print(res,controleur.nb_tours)
    del controleur
    return res,survivants

def multiduel(esprit1,esprit2,niveau_1=1,niveau_2=1,tailles_lab=(20,20),vide=True):

    score1 = 0
    score2 = 0
    nul = 0
    while True:
        res, survivants = init_duel(esprit1,esprit2,niveau_1,niveau_2,tailles_lab,vide)
        if res == "1":
            score1 += 1
        elif res == "2":
            score2 += 1
        elif res == "match nul":
            nul += 1
        print((score1,nul,score2))
        print(survivants)

#print("On run !")
main()
#multiduel(Esprit_type,Esprit_defensif,2,2,(10,5),False)
    
