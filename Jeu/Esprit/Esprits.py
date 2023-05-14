from __future__ import annotations
from typing import TYPE_CHECKING, List, Set

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Controleur import Controleur
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Jeu.Entitee.Agissant.Humain.Humain import Humain
    from Jeu.Entitee.Agissant.Slime.Slime import Slime
    from Jeu.Systeme.Classe import Classe_principale

# Imports des classes parentes
from Jeu.Esprit.Esprit import Esprit

# class Esprit_type(Esprit):
#     """Un esprit caricatural, pour les besoins de mes expériences."""
#     def __init__(self,nom:str,niveau:int,controleur:Controleur,position:Position):
#         self.nom = nom
#         self.controleur = controleur
#         self.oubli = niveau
#         self.ennemis = {}
#         self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
#         self.prejuges = []
#         self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
#         self.resolution = 0
#         self.vue = Vues()
#         self.corps = {}
#         corps:List[Agissant] = []
#         if niveau == 1:
#             corps = [Tank(position,1),Dps(position,1),Dps(position,1)]
#         if niveau == 2:
#             corps = [Tank(position,2),Tank(position,1),Dps(position,2),Dps(position,2),Soigneur(position,1)]
#         controleur.ajoute_entitees(corps)
#         IDs = [corp for corp in corps]
#         self.ajoute_corps(IDs)
#         i = 0
#         random.shuffle(corps)
#         for corp in corps:
#             corp.position = position+i*BAS
#             i+=1

# class Esprit_sans_scrupule(Esprit_type):
#     """Un esprit qui s'en prend principalement aux soigneurs et aux soutiens."""

#     def antagonise_supports(self,offense:tuple[int,float]):
#         offenseur = self.controleur[offense[0]]
#         for effet in offenseur.effets:
#             if isinstance(effet,Dopage):
#                 ID = effet.responsable
#                 if ID != offense[0] and effet.phase == "affiche":
#                     responsabilite = (effet.taux_degats-1)*offense[1]
#                     if ID in self.ennemis:
#                         self.ennemis[ID]["importance"] += responsabilite
#                     else:
#                         self.ennemis[ID] = {"importance":responsabilite,"dangerosite":0}
#             elif isinstance(effet,Soin):
#                 ID = effet.responsable
#                 if ID != offense[0] and effet.phase == "affiche":
#                     responsabilite = (effet.gain_pv/offenseur.pv)*offense[1]
#                     if ID in self.ennemis:
#                         self.ennemis[ID]["importance"] += responsabilite
#                     else:
#                         self.ennemis[ID] = {"importance":responsabilite,"dangerosite":0}

# class Esprit_bourrin(Esprit_type): #À supprimer, plus nécessaire
#     """Un esprit sans soigneurs ni soutiens."""
#     def __init__(self,nom:str,niveau:int,controleur:Controleur,position:Position):
#         # Tout le monde spawn au même endroit, changer ça !
#         self.nom = nom
#         self.controleur = controleur
#         self.oubli = niveau
#         self.ennemis = {}
#         self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
#         self.prejuges = []
#         self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
#         self.resolution = 0
#         self.vue = Vues()
#         self.corps = {}
#         corps:List[Agissant] = []
#         if niveau == 1:
#             corps = [Dps(position,1),Dps(position,1),Dps(position,1)]
#         if niveau == 2:
#             corps = [Dps(position,2),Dps(position,2),Dps(position,2),Dps(position,1),Dps(position,1)]
#         controleur.ajoute_entitees(corps)
#         IDs = [corp.ID for corp in corps]
#         self.ajoute_corps(IDs)
#         i = 0
#         random.shuffle(corps)
#         for corp in corps:
#             corp.position = position+i*BAS
#             i+=1

# class Esprit_defensif(Esprit_type): #À supprimer, plus nécessaire
#     """Un esprit sans soigneurs ni soutiens."""
#     def __init__(self,nom:str,niveau:int,controleur:Controleur,position,Position):
#         # Tout le monde spawn au même endroit, changer ça !
#         self.nom = nom
#         self.controleur = controleur
#         self.oubli = niveau
#         self.ennemis = {}
#         self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
#         self.prejuges = []
#         self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
#         self.resolution = 0
#         self.vue = Vues()
#         self.corps = {}
#         corps:List[Agissant] = []
#         if niveau == 1:
#             corps = [Tank(position,1),Tank(position,1),Dps(position,1)]
#         if niveau == 2:
#             corps = [Tank(position,2),Tank(position,2),Dps(position,2),Tank(position,1),Dps(position,1)]
#         controleur.ajoute_entitees(corps)
#         IDs = [corp.ID for corp in corps]
#         self.ajoute_corps(IDs)
#         i = 0
#         random.shuffle(corps)
#         for corp in corps:
#             corp.position = position+i*BAS
#             i+=1

# class Esprit_solitaire(Esprit_type):
#     """Un esprit avec un unique corp."""
#     def __init__(self,nom:str,corp:int,controleur:Controleur):
#         self.nom = nom
#         self.controleur = controleur
#         self.oubli = 5
#         self.ennemis = {}
#         self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
#         self.prejuges = []
#         self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
#         self.resolution = 0
#         self.vue = Vues()
#         self.corps = {}
#         self.ajoute_corp(corp)

class Esprit_simple(Esprit):
    """Un esprit avec les corps qu'on lui donne."""
    def __init__(self,nom:str,corps:List[Agissant],prejuges:List[str],controleur:Controleur):
        Esprit.__init__(self,controleur,nom)
        self.oubli = 5
        self.prejuges = prejuges
        self.ajoute_corps(corps)

class Esprit_humain(Esprit_simple):
    """Un esprit qui dirige un ou plusieurs humains. Peut interragir avec d'autres esprits humains."""
    def __init__(self,corp:Humain,controleur:Controleur): #Les humains commencent tous séparément, donc ils ont leur propre esprit au début
        Esprit.__init__(self,controleur,corp.identite)
        self.controleur = controleur
        self.ajoute_corp(corp)
        self.chef = corp #Les humains ne peuvent pas s'empêcher d'avoir des chefs

    def get_offenses(self):
        for corp in self.corps: #On vérifie si quelqu'un nous a offensé
            offenses,etat = corp.get_offenses()
            self.corps[corp] = etat
            for offense in offenses:
                self.antagonise_attaquant(offense)
                self.antagonise_supports(offense)
                if True:# self.peureuse():
                    for coennemi in offense[0].esprit.corps:
                        if not coennemi in self.ennemis:
                            self.ennemis[coennemi] = {"importance":0.01,"dangerosite":0}

    def merge(self,esprit:Esprit_humain): #Regroupe deux esprits, lorsque des humains forment un groupe
        Esprit.merge(self,esprit)
        self.elit()

    def elit(self):
        if self.controleur.joueur in self.corps:
            self.chef = self.controleur.joueur #Le joueur est le chef par défaut ! Ah mais non mais !
        else:
            candidats:Set[Humain] = set()
            for corp in self.corps:
                if "humain" in corp.get_especes() and isinstance(corp,Humain):
                    candidats.add(corp) #Les humains sont les seuls à pouvoir diriger un esprit d'humain. Et les seuls à voter, aussi.
            votes_max = 0
            for candidat in candidats:
                votes = 0
                place = candidat.ID
                for votant in candidats:
                    votes += votant.appreciations[place]
                if votes > votes_max:
                    self.chef = candidat #/!\ Éviter les chefs morts, à l'occasion /!\
                    votes_max = votes

    def exclus(self,corp:Agissant): #C'est super sympa, les relations humaines !
        #Il va falloir créer un nouvel esprit pour l'humain exclus
        #Et il va falloir donner un nom à ce nouvel esprit
        #Les esprits humains sont nommés d'après leur porteur originel
        if corp.identite != self.nom: #Tout va bien
            if isinstance(corp,Humain):
                self.controleur.esprits[corp.identite]=Esprit_humain(corp,self.controleur)
            else:
                self.controleur.esprits[corp.identite]=Esprit(self.controleur,corp.identite)
                self.controleur.esprits[corp.identite].ajoute_corp(corp)
        else:
            assert isinstance(corp,Humain)
            self.controleur.esprits[corp.identite]=Esprit_humain(corp,self.controleur)
            self.elit() #Autant changer tous les rapports de force d'un coup
            self.nom = self.chef.identite
            self.controleur.esprits[self.nom] = self

class Esprit_slime(Esprit):
    """Un esprit qui dirige un ou plusieurs slimes. Peut interragir avec d'autres esprits slimes."""
    def __init__(self,corp:Slime,controleur:Controleur): #Les slimes commencent tous séparément, donc ils ont leur propre esprit au début
        Esprit.__init__(self,controleur,"esprit_slime_"+str(corp))
        self.oubli = 5 #Faire dépendre des skills
        self.dispersion_spatiale = 0.9 #La décroissance de l'importance dans l'espace. Tester plusieurs options pour l'optimiser
        self.prejuges = ["humain"] #Vraiment ?
        self.pardon = 0.9 #La décroissance de l'importance avec le temps. Peut être supérieure à 1 pour s'en prendre en priorité aux ennemis ancestraux.
        self.resolution = 0
        self.classe:Classe_principale = corp.classe_principale
        self.ajoute_corp(corp)

    def merge(self,esprit:Esprit_slime): #Regroupe deux esprits, lorsque des slimes se regroupent
        self.merge_classe(esprit.classe)
        Esprit.merge(self,esprit)

    def merge_classe(self,classe:Classe_principale):
        #On va comparer tous les skills de chaque classe
        #Les slimes ont trois skills intrasecs : la fusion, pour unir deux groupes de slimes en un seul, la division, pour créer un nouveau slime, et l'absorption, pour ramasser un cadavre et voler ses skills
        #Ils peuvent avoir beaucoup de skills non-intrasecs, et n'utilisent souvent que les passifs
        #Ils ne peuvent pas avoir de sous-classes

        if classe.niveau > self.classe.niveau:
            self.classe.skills_intrasecs = classe.skills_intrasecs
            self.classe.niveau = classe.niveau
            self.classe.xp = classe.xp
        # for skill_intrasec in classe.skills_intrasecs:
        #     autre_skill_intrasec:Skill_intrasec = trouve_skill(self.classe,type(skill_intrasec))
        #     if autre_skill_intrasec is not None:
        #         if skill_intrasec.niveau > autre_skill_intrasec.niveau:
        #             self.classe.skills_intrasecs.remove(autre_skill_intrasec)
        #             self.classe.skills_intrasecs.append(skill_intrasec)
        #         elif skill_intrasec.xp > autre_skill_intrasec.xp:
        #             self.classe.skills_intrasecs.remove(autre_skill_intrasec)
        #             self.classe.skills_intrasecs.append(skill_intrasec)
        #     else: #Ça ne devrait pas arriver dans les intrasecs, mais sait-on jamais...
        #         print("Le slime receveur n'avait de skill intrasec correspondant à celui-ci :")
        #         print(skill_intrasec)
        #         self.classe.skills_intrasecs.append(skill_intrasec)

        for skill in classe.skills:
            autre_skill = trouve_skill(self.classe,type(skill))
            if autre_skill is not None:
                if skill.niveau > autre_skill.niveau or (skill.niveau == autre_skill.niveau and skill.xp > autre_skill.xp):
                    self.classe.skills.remove(autre_skill)
                    self.classe.skills.append(skill)
                elif skill.niveau == autre_skill.niveau and skill.xp > autre_skill.xp:
                    self.classe.skills.remove(autre_skill)
                    self.classe.skills.append(skill)
            else:
                self.classe.skills.append(skill)

    def ajoute_corp(self,corp:Slime):
        if not corp in self.corps:
            self.corps[corp] = "incapacite"
            corp.rejoint(self)
            corp.classe_principale = self.classe #C'est la plus grande force des slimes : progresser ensemble !

    #/!\ Faire un processus de décision propre aux slimes, qui prend en compte les capacités (communes heureusement) et la situation de chacun

# Imports utilisés dans le code
from Jeu.Systeme.Classe import trouve_skill