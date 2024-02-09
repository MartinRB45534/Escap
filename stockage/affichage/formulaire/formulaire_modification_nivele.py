"""Contient la classe FormulaireModificationNivele."""

from __future__ import annotations
from typing import  Callable

import affichage as af
from ..menu_enum import MenuEnum

from .formulaire_nivele import FormulaireNivele, StockageNi

class FormulaireModificationNivele(FormulaireNivele, af.NoeudVertical):
    """Un formulaire, avec des champs à remplir pour modifier un objet."""
    def __init__(self, stockage: type[StockageNi],  modifier: Callable[[StockageNi], None],
                 objet:StockageNi, supprimer: Callable[[StockageNi], None]):
        af.NoeudVertical.__init__(self)

        self.bouton_modifier = af.BoutonFonction(af.SKIN_SHADE, "Modifier", self.ajouter)
        self.bouton_supprimer = af.BoutonFonction(af.SKIN_SHADE, "Supprimer", lambda: supprimer(objet))

        FormulaireNivele.__init__(self, stockage, modifier)

        self.objet = objet
        input_nom = self.inputs["nom"]
        assert isinstance(input_nom, af.TexteInput)
        input_nom.valeur = objet.nom
        self.nom = objet.nom

        for key in stockage.champs:
            # Est-ce que getattr est pire que d'utiliser la jsonification ?
            input_ = self.inputs[key]
            if key in self.valeurs:
                assert isinstance(input_, af.TexteInput)
                input_.valeur = str(getattr(objet, key)[0])
                self.valeurs[key] = [str(attr) for attr in getattr(objet, key)]
            elif stockage.multiple[key]:
                assert isinstance(input_, list)
                for attr in list(getattr(objet, key)[0]):
                    input_[-1].valeur = str(attr)
                    input_.append(self.get_multiple_input(stockage.champs[key], stockage.acceptors[key]))
            else:
                assert not isinstance(input_, list)
                input_.valeur = str(getattr(objet, key))

        self.make_contenu()
        self.check_avertissements()

    def make_contenu(self):
        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
                if key == "nom" or key == "niveau" or self.stockage.conditionnels[key](self.to_dict())
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
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuEnum)):
            if self.courant in self.inputs.values():
                i = list(self.inputs.values()).index(self.courant)
            else:
                for i, input_ in enumerate(self.inputs.values()):
                    if isinstance(input_, list) and self.courant in input_:
                        j = input_.index(self.courant)
                        if j > 0:
                            self.courant = input_[j-1]
                            self.courant.set_actif()
                            return self
                        break
                else:
                    raise ValueError(f"On ne trouve pas {self.courant} dans les inputs !")
        else:
            i = len(self.inputs.values())
        while i > 0:
            i -= 1
            key = list(self.inputs.keys())[i]
            if key == "nom" or key == "niveau" or self.stockage.conditionnels[key](self.to_dict()):
                input_ = self.inputs[key]
                self.courant = input_ if not isinstance(input_, list) else input_[-1]
                self.courant.set_actif()
                return self
        return False

    def in_down(self): # type: ignore # Pylance somehow can't figure out that this inherits from its parent smh...
        self.courant.unset_actif()
        if self.courant is self.bouton_modifier:
            self.courant = self.bouton_supprimer
            self.courant.set_actif()
            return self
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuEnum)):
            if self.courant in self.inputs.values():
                i = list(self.inputs.values()).index(self.courant)
            else:
                for i, input_ in enumerate(self.inputs.values()):
                    if isinstance(input_, list) and self.courant in input_:
                        j = input_.index(self.courant)
                        if j < len(input_)-1:
                            self.courant = input_[j+1]
                            self.courant.set_actif()
                            return self
                        break
                else:
                    raise ValueError(f"On ne trouve pas {self.courant} dans les inputs !")
        else:
            return False
        while i < len(self.inputs.values())-1:
            i += 1
            key = list(self.inputs.keys())[i]
            if key == "nom" or key == "niveau" or self.stockage.conditionnels[key](self.to_dict()):
                input_ = self.inputs[key]
                self.courant = input_ if not isinstance(input_, list) else input_[0]
                self.courant.set_actif()
                return self
        self.courant = self.bouton_modifier
        self.courant.set_actif()
        return self

    def through_up(self):
        return self.in_up()

    def through_down(self):
        return self.in_down()
