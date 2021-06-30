from Jeu.Constantes import *
from Jeu.Skins.Skins import *

class Bouton:
    def __init__(self,texte,details=[],action=True,couleurs=[(255,255,255),(155,155,155),(0,0,0)],image=IMAGE_VIDE):
        self.texte = texte
        self.details = details
        self.action = action
        self.couleurs = couleurs
        self.image = image

def menu(parametres,screen,couleur=(255,255,255),illustration=SKIN_ESCAP,police=POLICE20):
    res = False
    clock = pygame.time.Clock()
    boutons = [Bouton(*parametre) for parametre in parametres] #J'ai appris quelque chose aujourd'hui !
    while not(res):
        largeur,hauteur = screen.get_size()
        debut_largeur = int((largeur-1350)//2)
        debut_hauteur = int((hauteur-690)//2)
        curseur = 0
        nb = len(boutons)
        taille = int(4*police.get_linesize()//3) #La taille du rectangle (aussi la taille 'officielle' de la police
        distance = 2*police.get_linesize() #La distance entre deux débuts de rectangles
        mimax = int(345//distance)-1 #Le nombre maximum de rectangles par demi-écran, avec une marge de principe
        start = debut_hauteur + int(345-distance*mimax-taille//2) #Le début du premier rectangle
        #Calcul des positions des boutons :
        if curseur <= mimax: #On n'a pas de boutons superflus en haut
            imin = 0
            imax = min(nb-1,2*mimax)
        elif curseur + mimax >= nb-1:
            imax = nb-1
            imin = max(0,nb-1-2*mimax)
        else:
            imax = curseur + mimax
            imin = curseur-mimax
        #Récupération / traitement des inputs :
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                res = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    res = boutons[curseur].action
                elif event.key == pygame.K_UP:
                    if curseur == 0:
                        curseur = len(boutons)
                    curseur -= 1
                elif event.key == pygame.K_DOWN:
                    curseur += 1
                    if curseur == len(boutons):
                        curseur = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos
                    if debut_largeur + 50 < pos[0] < debut_largeur + 350:
                        if (pos[1]-start)%distance <= taille:
                            irel = int((pos[1]-start)//distance)
                            i = irel + imin
                            if i <= imax:
                                res = boutons[i].action
                
                

        #Affichage :
        screen.fill((0,0,0))
        illustration.dessine_toi(screen,(debut_largeur,debut_hauteur))
        marge_haut = start
        marge_gauche = debut_largeur + 50
        for i in range(imin,imax+1) :
            if i == curseur:
                pygame.draw.rect(screen,boutons[i].couleurs[1],(marge_gauche-2,marge_haut-2,304,taille+4)) #/!\ Remplacer le 304 par une variable calculée en fonction de la longueur des titres
                descr = boutons[i].details
            pygame.draw.rect(screen,boutons[i].couleurs[0],(marge_gauche,marge_haut,300,taille)) #/!\ Remplacer ce 300 aussi
            boutons[i].image.dessine_toi(screen,(marge_gauche,marge_haut),(50,taille)) #/!\ Et ce 50 !
            text = police.render(boutons[i].texte,True,boutons[i].couleurs[2])
            screen.blit(text,(marge_gauche+40,marge_haut+3))
            marge_haut += distance

        
        marge_haut = start
        marge_gauche += 300 + taille
        for tex in descr :
            line = police.render(tex,True,couleur)
            screen.blit(line,(marge_gauche,marge_haut))
            marge_haut += distance

        pygame.display.flip()
        clock.tick(20)
    if res == True:
        res = False
    return res
