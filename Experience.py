import pygame
pygame.init()
screen = pygame.display.set_mode((1,1))
import numpy as np
from Jeu import * #Nécessaire ?
from Jeu.Général import *
from Jeu.Constantes import *

#Expérience 1 (dispersion spatiale 0.1-0.9 milieu ouvert):
#Équipe 1 contre équipe 2, l'équipe 1 est désavantagée (shamans à l'avant, sentinelle et guerriers à l'arrière)
#Mesure la durée du combat (l'équipe 1 n'a jamais gagné), limitée à 5000 tours (victoire la plus tardive enregistrée : 3582)
#Moyennes : 585.875 (8 combats), 5000 (8), 3730 (3), 5000 (11), 5000 (6), 3688.889 (8), 1312.8 (5), 1187.25 (8), 1598.667 (6)
#Observations : Beaucoup de match nul (5000+) pour les dispersions de 0.2 à 0.6
#Remarque : la dispersion pourrait aussi influer sur l'efficacité au combat

#Expérience 2 (dispersion spatiale 0.1-0.9 milieu fermé):
#Similaire à l'expérience 1 mais dans un labyrinthe au lieu d'une salle ouverte.
#Même mesure, la limite de temps a été réduite à 3000, il y a aussi eu quelques victoires de l'équipe 1
#Moyennes (défaites/nuls/victoires) : 706.5 (6/3/1), 576 (6/3/1), 545.75 (4/1/0), 2033.333 (3/1/1), 633.25 (4/2/0), 905.6 (5/2/0), 712.25 (8/1/1), 584.3 (10/3/1), 1213 (7/3/1)
#Observations : Très peu de match nul (pourtant descendus à 3000+), quelques victoires de l'équipe 1 et globalement pas de tendance notable
#Remarque : la disposition du labyrinthe a un effet non négligeable sur l'issue du combat et sa durée, suffisament pour cacher l'effet de la dispersion mais pas celui du positionnement de départ

#Expérience 3 (dispersion spatiale 0.2-0.6):
#Similaire à l'expérience 1 et deux mais dans un labyrinthe partiellement ouvert.
#En sortie les listes de corps pour déterminer qui est mort quand, la limite de temps a été réduite à 1000, données peu utilisable car beaucoup de combats terminés avant la limite des 1000 tours et les listes de corps sont difficiles à analyser systématiquement
#Moyennes (nombre de combats) : 736.72 (36), 769.90 (41), 728 (27), 738.73 (33), 736.93 (43)
#Observations : Pas de tendance claire, peut-être prendre le temps de traiter les données correctement à l'occasion
#Remarque : rien de neuf



def exp():
    experimente5()

def experimente5():
    ranje = [0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65]
    global res
    res = {i:[] for i in ranje}
    while True:
        i = random.randint(0,len(ranje)-1)
        diffusion = ranje[i]
        global controleur
        controleur = Controleur()
        controleur.experience5()
        controleur.esprits["Equipe 1"].dispersion_spatiale = diffusion
        run = True
        while run:
            agissants_courants,items_courants,labs_courants,esprits_courants = controleur.get_agissants_items_labs_esprits()

            for agissant in agissants_courants :
                controleur.make_vue(agissant)
                agissant.debut_tour()
            for item in items_courants :
                item.debut_tour()
            for lab in labs_courants:
                lab.debut_tour()
            for esprit in esprits_courants:
                esprit.debut_tour()
            for agissant in agissants_courants :
                agissant.post_decision()
            for agissant in agissants_courants :
                while agissant.latence <= 0 and agissant.skill_courant is not None :
                    controleur.fait_agir(agissant)
                    agissant.on_action()
                agissant.on_action()
            for item in items_courants :
                while item.hauteur > 0 and item.latence <= 0:
                    controleur.fait_voler(item)
            for agissant in agissants_courants :
                agissant.post_action()
            for lab in labs_courants:
                lab.post_action()
            for agissant in agissants_courants :
                agissant.pre_attack()
            for agissant in agissants_courants :
                agissant.fin_tour()
            for item in items_courants :
                item.fin_tour()
            for lab in labs_courants:
                lab.fin_tour()
            for esprit in esprits_courants:
                esprit.fin_tour()

            if controleur.check_exp5():
                run = False
        res[diffusion].append(controleur.check_exp5())
        print(diffusion,res[diffusion][-1])

exp()
