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

        self.bouton_modifier = af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter)
        self.bouton_supprimer = af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))

        FormulaireUnique.__init__(self, stockage, modifier)

        self.objet = objet
        self.inputs["nom"].valeur = objet.nom
        self.nom = objet.nom

        for key in stockage.champs:
            # Est-ce que c'est pire que d'utiliser la jsonification ?
            self.inputs[key].valeur = str(getattr(objet, key))

        self.make_contenu()
        self.check()

    def make_contenu(self):
        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
                if key == "nom" or self.stockage.conditionnels[key](
                    {ke: input_.valeur for ke, input_ in self.inputs.items()}
                )
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [self.bouton_modifier, self.bouton_supprimer]
        )

    def in_right(self):
        # On continue vers l'intérieur (pour coller avec le reste)
        return self.in_in()

    def in_up(self): # type: ignore # Pylance somehow can't figure out that this inherits from its parent smh...
        self.courant.unset_actif()
        if self.courant is self.bouton_supprimer:
            self.courant = self.bouton_modifier
            self.courant.set_actif()
            return self
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuElement)):
            i = list(self.inputs.values()).index(self.courant)
        else:
            i = len(self.inputs.values())
        while i > 0:
            i -= 1
            key = list(self.inputs.keys())[i]
            if key == "nom" or self.stockage.conditionnels[key](
                {ke: input_.valeur for ke, input_ in self.inputs.items()}
            ):
                self.courant = list(self.inputs.values())[i]
                self.courant.set_actif()
                return self
        return False

    def in_down(self): # type: ignore # Pylance somehow can't figure out that this inherits from its parent smh...
        self.courant.unset_actif()
        if self.courant is self.bouton_modifier:
            self.courant = self.bouton_supprimer
            self.courant.set_actif()
            return self
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuElement)):
            i = list(self.inputs.values()).index(self.courant)
        else:
            return False
        while i < len(self.inputs.values())-1:
            i += 1
            key = list(self.inputs.keys())[i]
            if key == "nom" or self.stockage.conditionnels[key](
                {ke: input_.valeur for ke, input_ in self.inputs.items()}
            ):
                self.courant = list(self.inputs.values())[i]
                self.courant.set_actif()
                return self
        self.courant = self.bouton_modifier
        self.courant.set_actif()
        return self

    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()
