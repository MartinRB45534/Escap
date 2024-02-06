"""Launch the editor."""

import pygame

pygame.init()
screen = pygame.display.set_mode((1600,800),pygame.RESIZABLE)

# Import must happen after pygame.init()
import editeur as edt # pylint: disable=wrong-import-position # We need to import after pygame.init()

if __name__ == "__main__":
    editor = edt.Editeur()
    editor.run(screen)
