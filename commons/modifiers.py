"""Détermine les modificateurs de touches."""

from typing import Set
import pygame

def get_modifiers(mod:int) -> Set[int]:
    """Détermine les modificateurs de touches."""
    if mod == pygame.KMOD_NONE:
        return set()
    else:
        modifiers: Set[int] = set()
        for modifier in [pygame.KMOD_LSHIFT,pygame.KMOD_RSHIFT,pygame.KMOD_LCTRL,pygame.KMOD_RCTRL,pygame.KMOD_LALT,pygame.KMOD_RALT,pygame.KMOD_LMETA,pygame.KMOD_RMETA]:
            if mod & modifier :
                modifiers.add(modifier)
    return modifiers
