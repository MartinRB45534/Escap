import Carte as crt 

from .Case import Case
from ..Effet.Auras import Aura_permanente

class Aura_absente(Aura_permanente):
    """Classe représentant l'aura de la position absente."""
    pass

class Case_absent(Case, crt.Case_absent):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        super().__init__(crt.POSITION_ABSENTE,Aura_absente)

CASE_ABSENTE = Case_absent()