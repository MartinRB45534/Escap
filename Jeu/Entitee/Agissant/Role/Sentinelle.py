from __future__ import annotations

# Pas d'imports pour les annotations

# Imports des classes parentes
from Jeu.Entitee.Agissant.Agissant import Agissant

class Sentinelle(Agissant):
    """Une classe factice. Pour les agissants qui ne se déplace qu'en présence d'ennemis. Ne fonctionne pas lorsqu'un humain est aux commandes."""
    pass