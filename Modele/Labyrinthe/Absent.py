import Carte as crt 

from .Case import Case

class Case_absent(Case, crt.Case_absent):
    """Classe représentant l'étage de la position absente."""
    def __init__(self):
        super().__init__(crt.POSITION_ABSENTE,0)

CASE_ABSENTE = Case_absent()