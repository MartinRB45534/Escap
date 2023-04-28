import pygame

class Illustration:
    def __init__(self,nom_fichier):
        try:
            self.image = pygame.image.load("Jeu/Skins/"+nom_fichier).convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load("Jeu/Skins/vide.png").convert_alpha()
            print(f"N'a pas pu charger {nom_fichier}, remplacé par vide.png")

    def dessine_toi(self,screen,position,frame=1,frame_par_tour=1):
        screen.blit(self.image,position)

class Image(Illustration):
    def dessine_toi(self,screen,position,tailles=(40,40),frame=1,frame_par_tour=1,direction=0):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,int(direction)*-90),tailles),position)

class Skin(Illustration):
    def dessine_toi(self,screen,position,taille=40,frame=1,frame_par_tour=1,direction=0):
        screen.blit(pygame.transform.scale(pygame.transform.rotate(self.image,int(direction)*-90),(taille,taille)),position)

PROFONDEUR_DE_CHAMP = 13
SKINS_CASES_NOIRES_VUES = [[Image(f"Vue/Case/Noir/skin_case_{distance}_{ecart}.png") for ecart in range(distance//2+2)]+[Image(f"Vue/Case/Noir/skin_case_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]
SKINS_CASES_VUES = [[Image(f"Vue/Case/Code_0/skin_case_{distance}_{ecart}.png") for ecart in range(distance//2+2)]+[Image(f"Vue/Case/Code_0/skin_case_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]
SKINS_MURS_FACE_VUS = [[Image(f"Vue/Case/Code_0/skin_mur_face_{distance}_{ecart}.png") for ecart in range(distance//2+2)]+[Image(f"Vue/Case/Code_0/skin_mur_face_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]
SKINS_MURS_VUS = [[[Image(f"Vue/Case/Code_0/skin_mur_gauche_{distance}_0.png"),Image(f"Vue/Case/Code_0/skin_mur_droite_{distance}_0.png")]]+[Image(f"Vue/Case/Code_0/skin_mur_{distance}_{ecart}.png") for ecart in range(1,distance//2+2)]+[Image(f"Vue/Case/Code_0/skin_mur_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]

SKINS_ESCALIERS_BAS_FACE_VUS = [[Image(f"Vue/Case/Escalier_bas/skin_mur_face_{distance}_{ecart}.png") for ecart in range(distance//2+2)]+[Image(f"Vue/Case/Escalier_bas/skin_mur_face_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]
SKINS_ESCALIERS_BAS_VUS = [[[Image(f"Vue/Case/Escalier_bas/skin_mur_gauche_{distance}_0.png"),Image(f"Vue/Case/Escalier_bas/skin_mur_droite_{distance}_0.png")]]+[Image(f"Vue/Case/Escalier_bas/skin_mur_{distance}_{ecart}.png") for ecart in range(1,distance//2+2)]+[Image(f"Vue/Case/Escalier_bas/skin_mur_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]

SKINS_ESCALIERS_HAUT_FACE_VUS = [[Image(f"Vue/Case/Escalier_haut/skin_mur_face_{distance}_{ecart}.png") for ecart in range(distance//2+2)]+[Image(f"Vue/Case/Escalier_haut/skin_mur_face_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]
SKINS_ESCALIERS_HAUT_VUS = [[[Image(f"Vue/Case/Escalier_haut/skin_mur_gauche_{distance}_0.png"),Image(f"Vue/Case/Escalier_haut/skin_mur_droite_{distance}_0.png")]]+[Image(f"Vue/Case/Escalier_haut/skin_mur_{distance}_{ecart}.png") for ecart in range(1,distance//2+2)]+[Image(f"Vue/Case/Escalier_haut/skin_mur_{distance}_{ecart}.png") for ecart in range(-(distance//2+1),0)] for distance in range(PROFONDEUR_DE_CHAMP)]


FORMES_CORPS = ["indefini","homme","femme","gros"] #Rajouter "gobelin", "orc", "slime", "ombriul", etc.
FORMES_TETES = ["sans_tete","heros","receptionniste","paume","peureuse","encombrant","alchimiste","peste","bombe_atomique","marchand"] #Rajouter "gobelin", "orc"
FORMES_ITEMS = ["item","armure_dor","armure_dor_cassee","lance_dor","lance_dor_cassee","epee","epee_epeiste","armure_epeiste","tunique_enchantee","robe_magique","tunique_alchimiste","soutane","robe_sorciere","chapeau_sorciere","epee_marchand","armure_marchand"] #Rajouter tous les items existants

SKINS_CORPS_VUS = {forme:Image(f"Vue/Agissant/ebauche_corps_{forme}.png") for forme in FORMES_CORPS}
SKINS_TETES_VUES = {forme:Image(f"Vue/Agissant/ebauche_tete_{forme}.png") for forme in FORMES_TETES}
SKINS_ITEMS_VUS = {forme:{item:Image(f"Vue/Item/{item}_{forme}_vue.png") for item in FORMES_ITEMS} for forme in FORMES_CORPS}

SKIN_CODEUR_VUE = Image("Vue/Agissant/ebauche_codeur.png")
