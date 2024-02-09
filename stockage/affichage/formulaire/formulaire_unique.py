"""Contient la classe FormulaireUnique."""

from __future__ import annotations
from typing import  Callable, TypeVar
from enum import StrEnum

import affichage as af

from ...stockage import StockageUnique, StockageCategorieUnique, StockageCategorieNivelee, StockageSurCategorie
from ...stockageglobal import StockageGlobal
from ..menu_enum import MenuEnum

# Le stockage hérite de StockageUnique
StockageUn = TypeVar("StockageUn", bound=StockageUnique)

class FormulaireUnique(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: type[StockageUn], ajouter: Callable[[StockageUn], None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage

        self.nom = ""

        self.textes:dict[str, af.Texte] = {
            "nom": af.Texte("Nom :"),
        }
        self.inputs:dict[str, af.TexteInput|af.BoutonOnOff|MenuEnum|
                         list[af.TexteInput|MenuEnum]] = {
            "nom": af.TexteInput(acceptor=lambda nom: nom == self.nom or 
                                 StockageGlobal.global_.valide_nom(nom)),
        }
        self.avertissements:dict[str, af.TexteCache] = {
            "nom": af.TexteCache(""),
        }
        self.textes_avertissements:dict[str, str] = {
            "nom": "Le nom doit être unique.",
        }

        for key in stockage.champs:
            self.form(key, stockage.champs[key], stockage.acceptors[key],
                      stockage.avertissements[key], stockage.multiple[key])

        self.bouton_ajouter = af.BoutonFonction(af.SKIN_SHADE, "Ajouter", self.ajouter)

        self.liste = af.ListeMargeVerticale(shrink=True)
        self.make_contenu()

        self.contenu = af.WrapperMarge()
        self.contenu.set_contenu(self.liste)

        input_nom = self.inputs["nom"]
        assert isinstance(input_nom, af.TexteInput)
        self.courant = input_nom

        self.super_ajouter = ajouter

    def make_contenu(self):
        """Met à jour le contenu de la liste."""
        self.liste.set_contenu(
            sum([
                [texte, self.inputs[key], self.avertissements[key]]
                for key, texte in self.textes.items()
                if self.conditionnel(key)
            ], []) # type: ignore # Pylance wants me to specify the type of that empty list smh
            + [self.bouton_ajouter]
        )

    def to_dict(self) -> dict[str, str|list[str]]:
        """Retourne un dictionnaire avec les valeurs des champs."""
        return {
            key:
            [inp.valeur for inp in input_] # pylint: disable=not-an-iterable # I know it's an iterable, it's a list
            if isinstance(input_, list) # like seriously, why can't pylance just read this line?
            else input_.valeur
            for key, input_
            in self.inputs.items()
        }

    def conditionnel(self, key:str) -> bool:
        """Retourne si le champ est conditionnel."""
        return key == "nom" or self.stockage.conditionnels[key](self.to_dict())

    def get_input(self, type_: type[int|str|float|bool|StrEnum|StockageCategorieUnique|StockageCategorieNivelee|StockageSurCategorie],
                  acceptor: Callable[[str], bool]) -> af.TexteInput|af.BoutonOnOff|MenuEnum:
        """Retourne un input."""
        if type_ is int:
            return af.IntInput(acceptor=acceptor)
        elif type_ is str:
            return af.TexteInput(acceptor=acceptor)
        elif type_ is float:
            return af.NumberInput(acceptor=acceptor)
        elif type_ is bool:
            return af.BoutonOnOff(af.SKIN_VALIDER, af.SKIN_ANNULER, "Oui", "Non")
        elif issubclass(type_, StrEnum):
            return MenuEnum(type_)
        else:
            raise TypeError(f"Le type {type_} n'est pas supporté.")

    def get_multiple_input(self, type_: type[int|str|float|bool|StrEnum|StockageCategorieUnique|StockageCategorieNivelee|StockageSurCategorie],
                           acceptor: Callable[[str], bool]) -> af.TexteInput|MenuEnum:
        """Retourne un input multiple."""
        if type_ is int:
            raise ValueError("Input est un champ entier, il ne peut pas être multiple !")
        elif type_ is str:
            return af.TexteInput(acceptor=acceptor)
        elif type_ is float:
            raise ValueError("Input est un champ flottant, il ne peut pas être multiple !")
        elif type_ is bool:
            raise ValueError("Input est un champ booléen, il ne peut pas être multiple !")
        elif issubclass(type_, StrEnum):
            return MenuEnum(type_)
        else:
            raise TypeError(f"Le type {type_} n'est pas supporté.")

    def form(self, nom:str, type_: type[int|str|float|bool|StrEnum|StockageCategorieUnique|StockageCategorieNivelee|StockageSurCategorie],
             acceptor: Callable[[str], bool], avertissement:str, multiple: bool):
        """Ajoute un champ."""
        self.textes[nom] = af.Texte(nom)
        if multiple:
            if type_ in (int, float, bool):
                raise ValueError(
                    f"Input {nom} est un champ {type_}, il ne peut pas être multiple !")
            self.inputs[nom] = [self.get_multiple_input(type_, acceptor)]
        else:
            self.inputs[nom] = self.get_input(type_, acceptor)
        self.avertissements[nom] = af.TexteCache("")
        self.textes_avertissements[nom] = avertissement

    def check_avertissements(self):
        """Met à jour les avertissements"""
        for key, input_ in self.inputs.items():
            self.avertissements[key].set_texte("")
            if self.conditionnel(key):
                if isinstance(input_, list):
                    for inp in input_: # pylint: disable=not-an-iterable # I know it's an iterable, it's a list
                        if not inp.accepte:
                            self.avertissements[key].set_texte(self.textes_avertissements[key])
                            break
                elif not input_.accepte:
                    if key == "nom":
                        if input_.valeur:
                            self.avertissements[key].set_texte(
                                StockageGlobal.global_.warn_nom(input_.valeur))
                        else:
                            self.avertissements[key].set_texte("Le nom ne peut pas être vide.")
                    else:
                        self.avertissements[key].set_texte(self.textes_avertissements[key])

    def check_multiples(self):
        """Met à jour les inputs multiples."""
        for key, input_ in self.inputs.items():
            if isinstance(input_, list):
                i = 0
                while i < len(input_)-1:
                    if input_[i].accepte: # pylint: disable=unsubscriptable-object # I know it's subscriptable, it's a list
                        i += 1
                    else:
                        input_.pop(i)
                if input_[-1].accepte: # pylint: disable=unsubscriptable-object # I know it's subscriptable, it's a list
                    input_.append(self.get_multiple_input(self.stockage.champs[key],
                                                          self.stockage.acceptors[key]))

    def update(self):
        self.make_contenu()
        self.check_avertissements()
        self.check_multiples()
        af.WrapperNoeud.update(self)

    def ajouter(self):
        """Ajoute l'objet."""
        self.check_avertissements()
        if all([avertissement.get_texte() == "" for avertissement in self.avertissements.values()]):
            json = f"""{{{
        ", ".join([f'"{key}": "{(
            "["+(",".join([inp.valeur for inp in input_]))+"]" # pylint: disable=not-an-iterable # I know it's an iterable, it's a list
        ) if isinstance(input_, list) else input_.valeur}"'
    for key, input_ in self.inputs.items()])
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
        self.courant.unset_actif()
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
            if self.conditionnel(key):
                input_ = self.inputs[key]
                self.courant = input_ if not isinstance(input_, list) else input_[-1]
                self.courant.set_actif()
                return self
        return False

    def in_down(self):
        self.courant.unset_actif()
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
            if self.conditionnel(key):
                input_ = self.inputs[key]
                self.courant = input_ if not isinstance(input_, list) else input_[0]
                self.courant.set_actif()
                return self
        courant = self.liste.contenu[-1]
        if isinstance(courant, af.Bouton):
            self.courant = courant
            self.courant.set_actif()
            return self
        else:
            raise ValueError(f"Que fait {self.courant} en dernier élément de la liste ?")

    def through_out(self):
        self.courant.unset_actif()
        self.unset_actif() # Just to be really sure
        return False
