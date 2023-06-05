import pygame

try:
    POLICE20 = pygame.font.SysFont("Arial",20)
except pygame.error as message:
    print("N'oubliez pas d'initialiser pygame avant d'importer l'affichage !")
    raise message