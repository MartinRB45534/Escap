"""Le contenu de l'onglet de création d'un ou plusieurs quelque chose."""

from __future__ import annotations

import affichage as af
import stockage as stck

class OngletCategorie(af.Onglet):
    """L'onglet de création d'éléments."""
    def __init__(self, stockage:stck.StockageCategorie):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, stockage.nom, self.onglets)
        self.stockage = stockage
        self.make_onglets()

    def make_onglets(self):
        """Crée les onglets."""
        ajout = stck.FormulaireCategorie(
                    self.stockage,
                    self.ajouter
                ) if len(self.stockage.elements) > 1 else stck.FormulaireCategorieNivele(
                    self.stockage,
                    self.ajouter
                ) if isinstance(list(self.stockage.elements.values())[0],
                tuple) else stck.FormulaireCategorieUnique(
                    self.stockage,
                    self.ajouter
                )
        onglets = [af.Onglet(self.stockage.titre_nouveau, ajout)]
        onglets.extend(af.Onglet(nom, stck.FormulaireModificationUnique(
            type(element),
            self.ajouter,
            element,
            self.supprimer
        ) if isinstance(element, stck.StockageUnique) else stck.FormulaireModificationNivele(
            type(element),
            self.ajouter,
            element,
            self.supprimer
        )) for nom, element in self.stockage.contenu.items())
        self.onglets.set_onglets(onglets)
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

    def ajouter(self,element:stck.StockageUnique|stck.StockageNivele):
        """Ajoute une nouvelle espèce."""
        self.stockage.contenu[element.nom] = element
        self.make_onglets()
        self.set_actif()
        self.onglets.select(self.onglets.boutons[-1])

    def supprimer(self,element:stck.StockageUnique|stck.StockageNivele):
        """Supprime une espèce."""
        self.stockage.contenu.pop(element.nom)
        self.make_onglets()
        self.onglets.select(self.onglets.boutons[0])
