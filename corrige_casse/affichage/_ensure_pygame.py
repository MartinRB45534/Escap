"""S'assure que pygame est bien initialisé avant d'importer l'affichage."""

from warnings import warn

import pygame

try:
    transparency_flag = pygame.SRCALPHA
except pygame.error as message:
    warn("N'oubliez pas d'initialiser pygame avant d'importer l'affichage !")
    raise message
