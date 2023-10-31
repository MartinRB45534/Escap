"""Les fonctions de saisie de texte."""

from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Literal, Callable, Tuple
import pygame_textinput # type: ignore # Missing type stubs
import pygame

from .cliquable import Cliquable
from .direction import DirectionAff
from .polices import POLICE20

if TYPE_CHECKING:
    from .direction import Direction

class TexteInput(Cliquable):
    """Un élément qui permet de saisir du texte."""
    current_input: Optional[pygame_textinput.TextInputVisualizer] = None
    def __init__(self, texte: str = "", validator:Optional[Callable[[str],bool]] = lambda x: True):
        Cliquable.__init__(self)
        manager = pygame_textinput.TextInputManager(texte, validator)
        self.textinput = pygame_textinput.TextInputVisualizer(manager,POLICE20)

    def get_tailles(self, _tailles: Tuple[int, int]):
        return self.textinput.surface.get_size()

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        """Affiche l'élément."""
        screen.blit(self.textinput.surface, self.position)

    def set_actif(self):
        """Rend l'élément actif."""
        TexteInput.current_input = self.textinput
        pygame.key.set_repeat(500, 50)

    def navigue(self,direction: Direction) -> Optional[Cliquable]|Literal[False]:
        """Navigue dans la direction donnée, et renvoie l'élément navigué, ou False sinon
           (récursif pour d'autres éléments).
           """
        if self.actif: #On est à ce niveau
            if direction == DirectionAff.IN:
                return self
            if direction == DirectionAff.VALIDATE:
                TexteInput.current_input = None # On a validé la saisie
                pygame.key.set_repeat()
            return False

class IntInput(TexteInput):
    """Un élément qui permet de saisir un entier."""
    def __init__(self, texte: str = ""): # On accepte les entiers, positifs et négatifs, et les chaines vides
        TexteInput.__init__(self, texte, lambda x: x.isdigit() or (x.startswith("-") and x[1:].isdigit()) or x == "")

class NumberInput(TexteInput):
    """Un élément qui permet de saisir un nombre."""
    def __init__(self, texte: str = ""): # On accepte les nombres, positifs et négatifs, et les chaines vides
        TexteInput.__init__(self, texte, lambda x: x.replace(".","",1).isdigit() or (x.startswith("-") and x[1:].replace(".","",1).isdigit()) or x == "")
