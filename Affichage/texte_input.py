"""Les fonctions de saisie de texte."""

from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Literal, Callable, Tuple, List
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
    waiting: bool = False
    def __init__(self, texte: str = "(Cliquez ici)", validator:Callable[[str],bool] = lambda x: True, acceptor:Callable[[str],bool] = lambda x: True):
        Cliquable.__init__(self)
        manager = pygame_textinput.TextInputManager(texte, validator)
        self.acceptor = acceptor
        self.textinput = pygame_textinput.TextInputVisualizer(manager,POLICE20)

    def get_tailles(self, _tailles: Tuple[int, int]):
        return self.textinput.surface.get_size()

    def affiche(self, screen: pygame.Surface, frame: int = 1, frame_par_tour: int = 1):
        """Affiche l'élément."""
        if self.accepte:
            self.textinput.font_color = (0,0,0)
        else:
            self.textinput.font_color = (255,0,0)
        screen.blit(self.textinput.surface, self.position)

    def set_actif(self):
        """Rend l'élément actif."""
        if TexteInput.current_input:
            TexteInput.current_input.cursor_visible = False
        TexteInput.current_input = self.textinput
        TexteInput.waiting = True
        pygame.key.set_repeat(500, 50)
        Cliquable.set_actif(self)

    def unset_actif(self):
        """Rend l'élément inactif."""
        if TexteInput.current_input:
            TexteInput.current_input.cursor_visible = False
        TexteInput.current_input = None
        pygame.key.set_repeat()
        Cliquable.unset_actif(self)

    def navigue(self,direction: Direction) -> Cliquable|Literal[False]:
        """Navigue dans la direction donnée, et renvoie l'élément navigué, ou False sinon
           (récursif pour d'autres éléments).
           """
        if self.actif: #On est à ce niveau
            if direction == DirectionAff.IN:
                return self
        return False

    @classmethod
    def event(cls, events : List[pygame.event.Event]):
        """Traite les évènements."""
        if cls.waiting:
            cls.waiting = False
        else:
            cls.current_input.update(events) # type: ignore # Type partially unknown

    @property
    def valeur(self) -> str:
        """Renvoie la valeur saisie."""
        return self.textinput.value # type: ignore # Type partially unknown

    @valeur.setter
    def valeur(self, valeur: str):
        """Change la valeur saisie."""
        self.textinput.value = valeur

    @property
    def accepte(self):
        """Renvoie si la valeur saisie est acceptée."""
        return self.valeur and self.acceptor(self.valeur)

class IntInput(TexteInput):
    """Un élément qui permet de saisir un entier."""
    def __init__(self, texte: str = "0", acceptor:Callable[[str],bool] = lambda x: True): # On accepte les entiers, positifs et négatifs, et les chaines vides
        TexteInput.__init__(self, texte, lambda x: x.isdigit() or (x.startswith("-") and x[1:].isdigit()) or x == "", acceptor)

    def navigue(self, direction: Direction) -> Cliquable|Literal[False]:
        """Navigue dans la direction donnée, et renvoie l'élément navigué, ou False sinon
           (récursif pour d'autres éléments).
           """
        if self.actif:
            if direction == DirectionAff.UP:
                self.valeur = str(int(self.valeur)+1)
                return self
            elif direction == DirectionAff.DOWN:
                self.valeur = str(int(self.valeur)-1)
                return self
        return TexteInput.navigue(self, direction)

class NumberInput(TexteInput):
    """Un élément qui permet de saisir un nombre."""
    def __init__(self, texte: str = "0.0", acceptor:Callable[[str],bool] = lambda x: True): # On accepte les nombres, positifs et négatifs, et les chaines vides
        TexteInput.__init__(self, texte, lambda x: x.replace(".","",1).isdigit() or (x.startswith("-") and x[1:].replace(".","",1).isdigit()) or x == "", acceptor)
