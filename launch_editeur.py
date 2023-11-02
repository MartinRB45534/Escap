"""Launch the editor."""

import pygame

pygame.init()
screen = pygame.display.set_mode((800,800),pygame.RESIZABLE)

# Import must happen after pygame.init()
import editeur as edt

if __name__ == "__main__":
    editor = edt.Editeur()
    editor.run(screen)
