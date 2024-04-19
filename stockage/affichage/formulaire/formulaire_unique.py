"""Contient la classe FormulaireUnique."""

from __future__ import annotations
from typing import  Callable, TypeVar
from enum import StrEnum

import affichage as af

from ...stockage import Stockage, StockageUnique, StockageCategorieUnique, StockageCategorieNivelee, StockageSurCategorie
from ..menu_enum import MenuEnum
from ..menu_stockage import MenuStockage

# Le stockage hérite de StockageUnique
StockageUn = TypeVar("StockageUn", bound=StockageUnique)

class FormulaireUnique(af.WrapperNoeud):
    """Un formulaire, avec des champs à remplir pour créer un objet."""
    def __init__(self, stockage: type[StockageUn], ajouter: Callable[[StockageUn], None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage

        self.nom = ""
        self.input_nom = af.TexteInput(acceptor=lambda nom: nom == self.nom or
                                       self.stockage.global_.valide_nom(nom))

        self.textes:dict[str, af.Texte] = {
            "nom": af.Texte("Nom :"),
        }
        self.inputs:dict[str, af.TexteInput|af.BoutonOnOff|MenuEnum|
                         list[af.TexteInput|af.BoutonOnOff|MenuEnum]] = {
            "nom": self.input_nom,
        }
        self.avertissements:dict[str, af.TexteCache] = {
            "nom": af.TexteCache(""),
        }

        for key in stockage.champs:
            self.form(key)

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
        contenu:list[af.Affichable] = [
            self.textes["nom"],
            self.input_nom,
            self.avertissements["nom"],
        ]
        for key in self.stockage.champs:
            if self.conditionnel(key):
                contenu.append(self.textes[key])
                input_ = self.inputs[key]
                if self.stockage.multiple.get(key, False):
                    assert isinstance(input_, list)
                    noms_comultiples = self.stockage.comultiple.get(key, [])
                    comultiples: list[list[af.TexteInput|af.BoutonOnOff|MenuEnum]] = []
                    for nom_comultiple in noms_comultiples:
                        input_comultiple = self.inputs[nom_comultiple]
                        assert isinstance(input_comultiple, list)
                        comultiples.append(input_comultiple)
                    for i, inp in enumerate(input_[:-1]):
                        contenu.append(inp)
                        for j, comultiple in enumerate(comultiples):
                            contenu.append(self.textes[noms_comultiples[j]])
                            contenu.append(comultiple[i])
                            contenu.append(self.avertissements[noms_comultiples[j]])
                    contenu.append(input_[-1])
                elif isinstance(input_, list):
                    pass # C'est un comultiple
                else:
                    contenu.append(input_)
                contenu.append(self.avertissements[key])
        contenu.append(self.bouton_ajouter)
        self.liste.set_contenu(contenu)

    def to_dict(self) -> dict[str, str|list[str]]:
        """Retourne un dictionnaire avec les valeurs des champs."""
        dict_:dict[str, str|list[str]] = {
            "nom": self.input_nom.valeur,
        }
        for key in self.stockage.champs:
            input_ = self.inputs[key]
            if key in sum([self.stockage.comultiple[key_] for key_ in self.stockage.comultiple], []): # type: ignore # Pylance wants me to specify the type of that empty list smh
                assert isinstance(input_, list)
                dict_[key] = [inp.valeur for inp in input_]
            elif self.stockage.multiple.get(key, False):
                assert isinstance(input_, list)
                dict_[key] = [inp.valeur for inp in input_[:-1]]
            else:
                assert isinstance(input_, af.TexteInput|af.BoutonOnOff|MenuEnum)
                dict_[key] = input_.valeur
        return dict_

    def conditionnel(self, key:str) -> bool:
        """Retourne si le champ doit être affiché."""
        return key == "nom" or self.stockage.conditionnels.get(key, lambda _: True)(self.to_dict())

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
        elif issubclass(type_, Stockage):
            return MenuStockage(type_.global_.trouve_stockage(type_))
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
        elif issubclass(type_, Stockage):
            return MenuStockage(type_.global_.trouve_stockage(type_))
        else:
            raise TypeError(f"Le type {type_} n'est pas supporté.")

    def form(self, nom:str):
        """Ajoute un champ."""
        self.textes[nom] = af.Texte(nom)
        type_ = self.stockage.champs[nom]
        acceptor = self.stockage.acceptors.get(nom, lambda _: True)
        if nom in sum(self.stockage.comultiple.values(), []): # type: ignore # Pylance wants me to specify the type of that empty list smh
            self.inputs[nom] = []
        elif self.stockage.multiple.get(nom, False):
            if type_ in (int, float, bool): # Il faut que le champs puisse avoir une absence de valeur
                raise ValueError(
                    f"Input {nom} est un champ {type_}, il ne peut pas être multiple !")
            self.inputs[nom] = [self.get_multiple_input(type_, acceptor)]
        else:
            self.inputs[nom] = self.get_input(type_, acceptor)
        self.avertissements[nom] = af.TexteCache("")

    def check_avertissements(self):
        """Met à jour les avertissements"""
        for key, input_ in self.inputs.items():
            self.avertissements[key].set_texte("")
            if self.conditionnel(key):
                if isinstance(input_, list):
                    for inp in input_: # pylint: disable=not-an-iterable # I know it's an iterable, it's a list
                        if not inp.accepte:
                            self.avertissements[key].set_texte(self.stockage.avertissements.get(key, "Cet avertissement ne devrait pas apparaître."))
                            break
                elif not input_.accepte:
                    if key == "nom":
                        if input_.valeur:
                            self.avertissements[key].set_texte(
                                self.stockage.global_.warn_nom(input_.valeur))
                        else:
                            self.avertissements[key].set_texte("Le nom ne peut pas être vide.")
                    else:
                        self.avertissements[key].set_texte(self.stockage.avertissements.get(key, "Cet avertissement ne devrait pas apparaître."))

    def check_multiples(self):
        """Met à jour les inputs multiples."""
        for key, input_ in self.inputs.items():
            if key in sum(self.stockage.comultiple.values(), []): # type: ignore # Pylance wants me to specify the type of that empty list smh
                pass # C'est un comultiple
            elif isinstance(input_, list):
                noms_comultiples = self.stockage.comultiple.get(key, [])
                comultiples: list[list[af.TexteInput|af.BoutonOnOff|MenuEnum]] = []     
                for nom_comultiple in noms_comultiples:
                    input_comultiple = self.inputs[nom_comultiple]
                    assert isinstance(input_comultiple, list)
                    comultiples.append(input_comultiple)
                i = 0
                while i < len(input_)-1:
                    if input_[i].accepte: # pylint: disable=unsubscriptable-object # I know it's subscriptable, it's a list
                        i += 1
                    else:
                        input_.pop(i)
                        for comultiple in comultiples:
                            comultiple.pop(i)
                if input_[-1].accepte: # pylint: disable=unsubscriptable-object # I know it's subscriptable, it's a list
                    input_.append(self.get_multiple_input(self.stockage.champs[key],
                                                          self.stockage.acceptors.get(key, lambda _: True)))
                    for comultiple in comultiples:
                        comultiple.append(self.get_input(self.stockage.champs[key],
                                                         self.stockage.acceptors.get(key, lambda _: True)))

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
