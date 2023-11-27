"""Détermine les modificateurs de touches."""

import pygame

def get_modifiers(mod:int) -> set[int]:
    """Détermine les modificateurs de touches."""
    if mod == pygame.KMOD_NONE:
        return set()
    else:
        modifiers: set[int] = set()
        for modifier in [pygame.KMOD_LSHIFT,pygame.KMOD_RSHIFT,pygame.KMOD_LCTRL,pygame.KMOD_RCTRL,pygame.KMOD_LALT,pygame.KMOD_RALT,pygame.KMOD_LMETA,pygame.KMOD_RMETA]:
            if mod & modifier :
                modifiers.add(modifier)
    return modifiers
