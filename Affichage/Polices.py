import pygame
from warnings import warn

try:
    POLICE20 = pygame.font.SysFont("Arial",20)
except pygame.error as message:
    warn("N'oubliez pas d'initialiser pygame avant d'importer l'affichage !")
    raise message