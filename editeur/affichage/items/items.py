"""Le contenu de l'onglet de création d'items."""

from __future__ import annotations
from typing import TYPE_CHECKING, Callable

import affichage as af
import modele as mdl

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ...jeu import Jeu

class OngletItems(af.Onglet):
    """L'onglet de création d'items."""
    def __init__(self, jeu:Jeu):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, "Items", self.onglets)
        self.jeu = jeu
        ajout = OngletAjout(jeu, self.ajouter)
        onglets = [af.Onglet("Nouvelle espèce", ajout)]
        onglets.extend(af.Onglet(espece.nom, OngletModification(jeu, espece, self.supprimer)) for espece in jeu.especes)
        self.onglets.set_onglets(onglets)

    def ajouter(self,espece:mdl.Espece):
        """Ajoute une nouvelle espèce."""
        self.jeu.especes.append(espece)
        self.onglets.set_onglets(self.onglets.onglets + [af.Onglet(espece.nom, OngletModification(self.jeu, espece, self.supprimer))])
        self.onglets.select(self.onglets.boutons[-1])

    def supprimer(self,espece:mdl.Espece):
        """Supprime une espèce."""
        self.jeu.especes.remove(espece)
        self.onglets.set_onglets([af.Onglet("Nouvelle espèce", OngletAjout(self.jeu, self.ajouter))] + [af.Onglet(espece.nom, OngletModification(self.jeu, espece, self.supprimer)) for espece in self.jeu.especes])
        self.onglets.select(self.onglets.boutons[0])

class OngletAjout(af.WrapperCliquable):
    """L'onglet d'ajout d'une nouvelle espece."""
    def __init__(self, jeu:Jeu, ajouter:Callable[[mdl.Espece],None]):
        af.WrapperCliquable.__init__(self)
        self.jeu = jeu
        self.contenu = af.PavageVertical()
        self.nom = af.TexteInput("Humain")
        self.doigts = af.IntInput("10")
        self.contenu.set_contenu([ # type: ignore # Pylance is stupid
            af.MargeHorizontale(),
            af.CenterHorizontalTexte("Nom de l'espèce (cliquez pour éditer)"),
            self.nom,
            af.MargeHorizontale(),
            af.CenterHorizontalTexte("Nombre de doigts (cliquez pour éditer)"),
            self.doigts,
            af.MargeHorizontale(),
            af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
            af.MargeHorizontale(),
        ],[5,0,0,5,0,0,5,0,-1])
        self.super_ajouter = ajouter

    def ajouter(self):
        """Ajoute une nouvelle espèce."""
        nom = self.nom.textinput.value # type: ignore # Partially known type
        nb_doigts = self.doigts.textinput.value # type: ignore # Partially known type

        assert isinstance(nom, str)
        assert isinstance(nb_doigts, str)
        assert isinstance(self.contenu, af.PavageVertical)

        if nom == "":
            self.contenu.set_contenu([ # type: ignore # Pylance is stupid
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nom de l'espèce (cliquez pour éditer)"),
                self.nom,
                af.CenterHorizontalTexte("Le nom ne peut pas être vide !"),
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nombre de doigts (cliquez pour éditer)"),
                self.doigts,
                af.MargeHorizontale(),
                af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
                af.MargeHorizontale(),
            ],[5,0,0,0,5,0,0,5,0,-1])
            return
        if nom in [espece.nom for espece in self.jeu.especes]:
            self.contenu.set_contenu([ # type: ignore # Pylance is stupid
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nom de l'espèce (cliquez pour éditer)"),
                self.nom,
                af.CenterHorizontalTexte("Il y a déjà une espèce avec ce nom !"),
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nombre de doigts (cliquez pour éditer)"),
                self.doigts,
                af.MargeHorizontale(),
                af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
                af.MargeHorizontale(),
            ],[5,0,0,0,5,0,0,5,0,-1])
            return
        if nb_doigts == "":
            self.contenu.set_contenu([ # type: ignore # Pylance is stupid
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nom de l'espèce (cliquez pour éditer)"),
                self.nom,
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nombre de doigts (cliquez pour éditer)"),
                self.doigts,
                af.CenterHorizontalTexte("Le nombre de doigts ne peut pas être vide !"),
                af.MargeHorizontale(),
                af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
                af.MargeHorizontale(),
            ],[5,0,0,5,0,0,0,5,0,-1])
            return
        nb_doigts = int(nb_doigts)
        if nb_doigts < 0:
            self.contenu.set_contenu([ # type: ignore # Pylance is stupid
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nom de l'espèce (cliquez pour éditer)"),
                self.nom,
                af.MargeHorizontale(),
                af.CenterHorizontalTexte("Nombre de doigts (cliquez pour éditer)"),
                self.doigts,
                af.CenterHorizontalTexte("Le nombre de doigts doit être positif !"),
                af.MargeHorizontale(),
                af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
                af.MargeHorizontale(),
            ],[5,0,0,5,0,0,0,5,0,-1])
            return

        espece = mdl.Espece(nom, nb_doigts)

        self.nom.textinput.value = "Humain"
        self.doigts.textinput.value = "10"

        self.contenu.set_contenu([ # type: ignore # Pylance is stupid
            af.MargeHorizontale(),
            af.CenterHorizontalTexte("Nom de l'espèce (cliquez pour éditer)"),
            self.nom,
            af.MargeHorizontale(),
            af.CenterHorizontalTexte("Nombre de doigts (cliquez pour éditer)"),
            self.doigts,
            af.MargeHorizontale(),
            af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
            af.MargeHorizontale(),
        ],[5,0,0,5,0,0,5,0,-1])

        self.super_ajouter(espece)
