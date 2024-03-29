"""Passage"""


class Passage:
    """Classe qui contient les informations sur le passage d'une case à une autre"""
    def __init__(self,mur:bool,teleporteur:bool,escalier:bool,barriere:bool,porte:bool,codes:list[str]=[]): # Constructeur
        self.mur = mur # True si on passe au travers des murs
        self.teleporteur = teleporteur # True si on passe par les teleporteurs
        self.escalier = escalier # True si on passe par les escaliers
        self.barriere = barriere # True si on passe au travers des barrières
        self.porte = porte # True si on passe au travers des portes
        if porte and codes:
            raise ValueError("Si on traverse les portes, pas besoin de codes")
        self.codes = codes # Liste des codes des portes
