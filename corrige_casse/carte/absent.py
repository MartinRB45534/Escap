"""Module contenant la classe Case_absent."""

from __future__ import annotations

from .case import Case
from .structure_spatiale.absent import POSITION_ABSENTE

class CaseAbsent(Case):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        super().__init__(POSITION_ABSENTE)

CASE_ABSENTE = CaseAbsent()
        