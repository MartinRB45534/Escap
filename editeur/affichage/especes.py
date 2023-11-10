"""Le contenu de l'onglet de création d'espèces."""

from __future__ import annotations
from typing import Callable

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

class OngletAjoutEspece(af.WrapperCliquable):
    """L'onglet d'ajout d'une nouvelle espece."""
    def __init__(self, stockage:stck.StockageGlobal, ajouter:Callable[[stck.Espece],None]):
        af.WrapperCliquable.__init__(self)
        self.stockage = stockage
        self.contenu = af.ListeMargeVerticale()
        self.nom = af.TexteInput("Humain")
        self.doigts = af.IntInput("10")
        self.avertissement_espece = af.TexteCache("")
        self.avertissement_doigts = af.TexteCache("")
        self.contenu.set_contenu([ # type: ignore # Pylance is stupid
            af.Texte("Nom de l'espèce (cliquez pour éditer)"),
            self.nom,
            self.avertissement_espece,
            af.Texte("Nombre de doigts (cliquez pour éditer)"),
            self.doigts,
            self.avertissement_doigts,
            af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
        ])
        self.super_ajouter = ajouter

    def ajouter(self):
        """Ajoute une nouvelle espèce."""
        nom = self.nom.textinput.value # type: ignore # Partially known type
        nb_doigts = self.doigts.textinput.value # type: ignore # Partially known type

        assert isinstance(nom, str)
        assert isinstance(nb_doigts, str)
        assert isinstance(self.contenu, af.ListeMargeVerticale)

        if nom == "":
            self.avertissement_espece.set_texte("Le nom ne peut pas être vide !")
        elif nom in self.stockage.especes.especes:
            self.avertissement_espece.set_texte("Il y a déjà une espèce avec ce nom !")

        if nb_doigts == "":
            self.avertissement_doigts.set_texte("Le nombre de doigts ne peut pas être vide !")
        else:
            nb_doigts = int(nb_doigts)
            if nb_doigts < 0:
                self.avertissement_doigts.set_texte("Le nombre de doigts doit être positif !")
        
        if self.avertissement_espece.get_texte() != "" or self.avertissement_doigts.get_texte() != "":
            self.set_tailles(self.tailles)

        else:
            assert isinstance(nb_doigts, int)
            espece = stck.Espece(nom, nb_doigts)

            self.nom.textinput.value = "Humain"
            self.doigts.textinput.value = "10"

            self.avertissement_espece.set_texte("")
            self.avertissement_doigts.set_texte("")
            self.set_tailles(self.tailles)

            self.super_ajouter(espece)

class OngletModificationEspece(af.WrapperCliquable):
    """L'onglet de modification d'une espèce."""
    def __init__(self, stockage:stck.StockageGlobal, espece:stck.Espece, supprimer:Callable[[stck.Espece],None]):
        af.WrapperCliquable.__init__(self)
        self.stockage = stockage
        self.espece = espece
        self.contenu = af.ListeMargeVerticale()
        self.nom = af.TexteInput(espece.nom)
        self.doigts = af.IntInput(str(espece.nb_doigts))
        self.texte_espece = af.Texte(f"Nom de l'espèce (cliquez pour éditer, actuellement {self.espece.nom})")
        self.texte_doigts = af.Texte(f"Nombre de doigts (cliquez pour éditer, actuellement {self.espece.nb_doigts})")
        self.avertissement_espece = af.TexteCache("")
        self.avertissement_doigts = af.TexteCache("")
        self.contenu.set_contenu([ # type: ignore # Pylance is stupid
            self.texte_espece,
            self.nom,
            self.avertissement_espece,
            self.texte_doigts,
            self.doigts,
            self.avertissement_doigts,
            af.BoutonFonction(af.SKIN_SHADE,"Modifier",self.modifier),
            af.BoutonFonction(af.SKIN_SHADE,"Supprimer",self.supprimer),
        ])
        self.super_supprimer = supprimer

    def modifier(self):
        """Modifie l'espèce."""
        nom = self.nom.textinput.value # type: ignore # Partially known type
        nb_doigts = self.doigts.textinput.value # type: ignore # Partially known type

        assert isinstance(nom, str)
        assert isinstance(nb_doigts, str)
        assert isinstance(self.contenu, af.ListeMargeVerticale)

        if nom == "":
            self.avertissement_espece.set_texte("Le nom ne peut pas être vide !")
        elif nom in self.stockage.especes.especes:
            self.avertissement_espece.set_texte("Il y a déjà une espèce avec ce nom !")

        if nb_doigts == "":
            self.avertissement_doigts.set_texte("Le nombre de doigts ne peut pas être vide !")
        else:
            nb_doigts = int(nb_doigts)
            if nb_doigts < 0:
                self.avertissement_doigts.set_texte("Le nombre de doigts doit être positif !")
        
        if self.avertissement_espece.get_texte() != "" or self.avertissement_doigts.get_texte() != "":
            self.set_tailles(self.tailles)

        else:
            self.espece.nom = self.nom.textinput.value # type: ignore # Partially known type
            self.espece.nb_doigts = int(self.doigts.textinput.value) # type: ignore # Partially known type
            self.texte_espece.set_texte(f"Nom de l'espèce (cliquez pour éditer, actuellement {self.espece.nom})")
            self.texte_doigts.set_texte(f"Nombre de doigts (cliquez pour éditer, actuellement {self.espece.nb_doigts})")
            self.set_tailles(self.tailles)

    def supprimer(self):
        """Supprime l'espèce."""
        self.super_supprimer(self.espece)
