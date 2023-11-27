"""Le contenu de l'onglet de création de parchemins."""

from __future__ import annotations

import affichage as af
import stockage as stck

class OngletParchemins(af.Onglet):
    """L'onglet de création de parchemins."""
    def __init__(self, stockage:stck.StockageGlobal):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, "Parchemins", self.onglets)
        self.stockage = stockage
        self.make_onglets()

    def make_onglets(self):
        """Crée les onglets."""
        ajout = stck.FormulaireCategorie(
                    stck.StockageGlobal.global_.items.parchemin,
                    "Ajouter un parchemin. Les parchemins sont des items consommables qui s'activent avec du mana. Les parchemins vierges n'ont pas encore d'effet placé, tandis que les parchemins préécrits ont besoin d'un effet à la création.",
                    lambda nom: not nom in stck.StockageGlobal.global_.items.all_noms(),
                    "Il existe déjà un item avec ce nom !",
                    self.ajouter # type: ignore # Pylint can see it but Pylance can't
                )
        onglets = [af.Onglet("Nouveau parchemin", ajout)]
        onglets.extend(af.Onglet(nom, stck.FormulaireModificationUnique(
            stck.ParcheminVierge,
            lambda nom_: not nom_ in stck.StockageGlobal.global_.items.all_noms(),
            "Il existe déjà un item avec ce nom !",
            self.ajouter,
            parchemin,
            self.supprimer
        ) if isinstance(parchemin, stck.ParcheminVierge) else stck.FormulaireModificationNivele(
            stck.ParcheminViergeNivele,
            lambda nom_: not nom_ in stck.StockageGlobal.global_.items.all_noms(),
            "Il existe déjà un item avec ce nom !",
            self.ajouter,
            parchemin,
            self.supprimer
        )) for nom, parchemin in self.stockage.items.parchemin.parchemins.items())
        self.onglets.set_onglets(onglets)
        if self.tailles != (0,0):
            self.set_tailles(self.tailles)

    def ajouter(self,parchemin:stck.ParcheminVierge|stck.ParcheminViergeNivele):
        """Ajoute une nouvelle espèce."""
        self.stockage.items.parchemin.parchemins[parchemin.nom] = parchemin
        self.make_onglets()
        self.onglets.select(self.onglets.boutons[-1])

    def supprimer(self,parchemin:stck.ParcheminVierge|stck.ParcheminViergeNivele):
        """Supprime une espèce."""
        self.stockage.items.parchemin.parchemins.pop(parchemin.nom)
        self.make_onglets()
        self.onglets.select(self.onglets.boutons[0])
