"""Le contenu de l'onglet de création d'espèces."""

from __future__ import annotations

import affichage as af
import stockage as stck

class OngletEspeces(af.Onglet):
    """L'onglet de création d'espèces."""
    def __init__(self, stockage:stck.StockageGlobal):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, "Espèces", self.onglets)
        self.stockage = stockage
        self.make_onglets()

    def make_onglets(self):
        """Crée les onglets."""
        ajout = stck.FormulaireCategorie(
                    stck.StockageGlobal.global_.especes,
                    "Créer une espèce. Chaque espèce a un nom et un nombre de doigts possiblement nul (nombre d'anneaux qu'elle peut porter). Chaque agissant a une ou plusieurs espèces (seule la première est prise en compte pour les doigts). Certains éléments du jeu interagissent avec les espèces.",
                    lambda nom: not nom in stck.StockageGlobal.global_.especes.especes,
                    "Il existe déjà une espèce avec ce nom !",
                    self.ajouter # type: ignore # Pylint can see it but Pylance can't
                )
        onglets = [af.Onglet("Nouvelle espèce", ajout)]
        onglets.extend(af.Onglet(nom, stck.FormulaireModificationUnique(
            stck.Espece,
            lambda nom_: not nom_ in stck.StockageGlobal.global_.especes.especes,
            "Il existe déjà une espèce avec ce nom !",
            self.ajouter,
            espece,
            self.supprimer
        )) for nom, espece in self.stockage.especes.especes.items())
        self.onglets.set_onglets(onglets)
        self.onglets.set_actif()
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

    def ajouter(self,espece:stck.Espece) -> None:
        """Ajoute une nouvelle espèce."""
        self.stockage.especes.especes[espece.nom] = espece
        self.make_onglets()
        self.onglets.select(self.onglets.boutons[-1])

    def supprimer(self,espece:stck.Espece) -> None:
        """Supprime une espèce."""
        self.stockage.especes.especes.pop(espece.nom)
        self.make_onglets()
        self.onglets.select(self.onglets.boutons[0])
