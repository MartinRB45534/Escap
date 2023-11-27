"""Module définissant la classe de la case absente."""

import carte as crt

from .case import Case
# from ..effet.case.aura.auras import AuraPermanente

# class AuraAbsente(AuraPermanente):
#     """Classe représentant l'aura de la position absente."""

class CaseAbsent(Case, crt.CaseAbsent):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        # super().__init__(crt.POSITION_ABSENTE, AuraAbsente())
        self.position = crt.POSITION_ABSENTE

CASE_ABSENTE = CaseAbsent()
