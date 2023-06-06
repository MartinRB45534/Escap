from __future__ import annotations

# Pas d'import pour les annotations

# Imports des classes parentes
from .Case import Case

class Case_absent(Case):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        super().__init__(POSITION_ABSENTE,0)

from .Structure_spatiale.Absent import POSITION_ABSENTE

CASE_ABSENTE = Case_absent()
        