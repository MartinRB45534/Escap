"""Module définissant la classe de la case absente."""

import carte as crt

from .case import Case
from ..effet.auras import AuraPermanente

class AuraAbsente(AuraPermanente):
    """Classe représentant l'aura de la position absente."""

class CaseAbsent(Case, crt.caseAbsent):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        super().__init__(crt.POSITION_ABSENTE,AuraAbsente)

CASE_ABSENTE = CaseAbsent()
