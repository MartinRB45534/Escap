from Jeu.Affichage.Affichage import *

def creation_affichage(structure):
    """fonction qui crée les objets d'affichage"""
    for i in range(len(structure["arguments"])):
        if issubclass(structure["arguments"][i],dict):
            structure["arguments"][i]=creation_affichage(structure["arguments"][i])
    return structure["classe"].structure["methode"](**args structure["arguments"])