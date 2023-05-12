from typing import Tuple
import pygame

def get_modifiers(mod) -> Tuple|Tuple[int]:
    if mod == pygame.KMOD_NONE:
        return ()
    else:
        modifiers = []
        for modifier in [pygame.KMOD_LSHIFT,pygame.KMOD_RSHIFT,pygame.KMOD_LCTRL,pygame.KMOD_RCTRL,pygame.KMOD_LALT,pygame.KMOD_RALT,pygame.KMOD_LMETA,pygame.KMOD_RMETA]:
            if mod & modifier :
                modifiers.append(modifier)
    return tuple(modifiers)