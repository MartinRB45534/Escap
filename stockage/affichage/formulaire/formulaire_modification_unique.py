"""Contient la classe FormulaireModificationUnique."""

from __future__ import annotations
from typing import  Callable

import affichage as af
from ..menu_element import MenuElement

from .formulaire_unique import FormulaireUnique, StockageUn

class FormulaireModificationUnique(FormulaireUnique, af.NoeudVertical):
    """Un formulaire, avec des champs à remplir pour modifier un objet."""
    def __init__(self, stockage: type[StockageUn], modifier: Callable[[StockageUn], None],
                 objet:StockageUn, supprimer: Callable[[StockageUn], None]):
        af.NoeudVertical.__init__(self)
        FormulaireUnique.__init__(self, stockage, modifier)

        self.objet = objet
        self.inputs["nom"].valeur = objet.nom
        self.nom = objet.nom

        for key in stockage.champs:
            # Est-ce que c'est pire que d'utiliset la jsonification ?
            self.inputs[key].valeur = str(getattr(objet, key))

        self.bouton_modifier = af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter)
        self.bouton_supprimer = af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))

        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [self.bouton_modifier, self.bouton_supprimer]
        )

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self):
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuElement)):
            i = list(self.inputs.values()).index(self.courant)
            if i == 0:
                self.courant.unset_actif()
                return False
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[i-1]
            self.courant.set_actif()
            return self
        if self.courant is self.bouton_modifier:
            self.courant.unset_actif()
            self.courant = list(self.inputs.values())[-1]
            self.courant.set_actif()
            return self
        self.courant.unset_actif()
        self.courant = self.bouton_modifier
        self.courant.set_actif()
        return self

    def in_down(self):
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuElement)):
            i = list(self.inputs.values()).index(self.courant)
            if i == len(self.inputs.values())-1:
                courant = self.bouton_modifier
                self.courant.unset_actif()
                self.courant = courant
                self.courant.set_actif()
            else:
                self.courant.unset_actif()
                self.courant = list(self.inputs.values())[i+1]
                self.courant.set_actif()
            return self
        if self.courant is self.bouton_modifier:
            self.courant.unset_actif()
            self.courant = self.bouton_supprimer
            self.courant.set_actif()
            return self
        return False

    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()