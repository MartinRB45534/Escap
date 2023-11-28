"""Contient la classe FormulaireUnique."""

from __future__ import annotations
from typing import  Callable, TypeVar

import affichage as af
import modele as mdl

from ...stockage import StockageUnique
from ..menu_element import MenuElement

# Le stockage hérite de StockageUnique
StockageUn = TypeVar("StockageUn", bound=StockageUnique)

class FormulaireUnique(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: type[StockageUn], acceptor: Callable[[str], bool],
                 avertissement:str, ajouter: Callable[[StockageUn], None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage

        self.textes:dict[str, af.Texte] = {
            "nom": af.Texte("Nom :"),
        }
        self.inputs:dict[str, af.TexteInput|af.BoutonOnOff|MenuElement] = {
            "nom": af.TexteInput(acceptor=acceptor),
        }
        self.avertissements:dict[str, af.TexteCache] = {
            "nom": af.TexteCache(""),
        }
        self.textes_avertissements:dict[str, str] = {
            "nom": avertissement,
        }

        for key in stockage.champs:
            self.form(key, stockage.champs[key], stockage.acceptors[key],
                      stockage.avertissements[key])

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
            ], []) # type: ignore # Pylance wants me to specify the type if that empty list smh
            + [af.BoutonFonction(af.SKIN_SHADE, "Ajouter", self.ajouter)]
        )

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        self.courant = self.inputs["nom"]

        self.super_ajouter = ajouter

    def form(self, nom:str, type_: type[int|str|float|bool|mdl.Element],
             acceptor: Callable[[str], bool], avertissement:str):
        """Ajoute un champ."""
        self.textes[nom] = af.Texte(nom)
        if type_ is int:
            self.inputs[nom] = af.IntInput(acceptor=acceptor)
        elif type_ is str:
            self.inputs[nom] = af.TexteInput(acceptor=acceptor)
        elif type_ is float:
            self.inputs[nom] = af.NumberInput(acceptor=acceptor)
        elif type_ is bool:
            self.inputs[nom] = af.BoutonOnOff(af.SKIN_VALIDER, af.SKIN_ANNULER, "Oui", "Non")
        elif type_ is mdl.Element:
            self.inputs[nom] = MenuElement()
        else:
            raise TypeError(f"Le type {type_} n'est pas supporté.")
        self.avertissements[nom] = af.TexteCache("")
        self.textes_avertissements[nom] = avertissement

    def check(self):
        """Met à jour les avertissements"""
        for key, input_ in self.inputs.items():
            if input_.accepte:
                self.avertissements[key].set_texte("")
            else:
                self.avertissements[key].set_texte(self.textes_avertissements[key])
        self.set_tailles(self.tailles)

    def update(self):
        self.check()
        af.WrapperNoeud.update(self)

    def ajouter(self):
        """Ajoute l'objet."""
        self.check()
        if all([avertissement.get_texte() == "" for avertissement in self.avertissements.values()]):
            json = f"""{{{
", ".join([f'"{key}": "{input_.valeur}"' for key, input_ in self.inputs.items()])
}}}"""
            self.super_ajouter(self.stockage.parse(json))

    def select(self, selection: af.Cliquable, droit:bool=False):
        """Sélectionne l'élément."""
        self.update()
        af.WrapperNoeud.select(self, selection, droit)

    def set_actif(self):
        if self.courant:
            self.courant.set_actif()
        else:
            raise af.NavigationError("Les formulaires devraient toujours avoir un élément courant.")

    def unset_actif(self):
        if self.courant:
            self.courant.unset_actif()
        else:
            raise af.NavigationError("Les formulaires devraient toujours avoir un élément courant.")

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
        self.courant.unset_actif()
        self.courant = list(self.inputs.values())[-1]
        self.courant.set_actif()
        return self

    def in_down(self):
        if isinstance(self.courant, (af.TexteInput, af.BoutonOnOff, MenuElement)):
            i = list(self.inputs.values()).index(self.courant)
            if i == len(self.inputs.values())-1:
                courant = self.liste.contenu[-1]
                if isinstance(courant, af.Bouton):
                    self.courant.unset_actif()
                    self.courant = courant
                    self.courant.set_actif()
                else:
                    raise ValueError(f"Que fait {self.courant} en dernier élément de la liste ?")
            else:
                self.courant.unset_actif()
                self.courant = list(self.inputs.values())[i+1]
                self.courant.set_actif()
            return self
        return False

    def through_out(self):
        self.courant.unset_actif()
        self.unset_actif() # Just to be really sure
        return False
