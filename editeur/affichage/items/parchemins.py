"""Le contenu de l'onglet de création de parchemins."""

from __future__ import annotations
from typing import Callable, Dict, List, Optional

import affichage as af
from affichage.cliquable import Cliquable
import stockage as stck

class OngletParchemins(af.Onglet):
    """L'onglet de création de parchemins."""
    def __init__(self, stockage:stck.StockageGlobal):
        self.onglets = af.Onglets(af.DirectionAff.LEFT)
        af.Onglet.__init__(self, "Parchemins", self.onglets)
        self.stockage = stockage
        ajout = OngletAjoutParchemin(stockage, self.ajouter)
        onglets = [af.Onglet("Nouveau parchemin", ajout)]
        onglets.extend(af.Onglet(nom, OngletModificationParcheminVierge(stockage, parchemin, self.supprimer) if isinstance(parchemin, stck.ParcheminVierge) else OngletModificationParcheminViergeNivele(stockage, parchemin, self.supprimer)) for nom, parchemin in stockage.items.parchemin.parchemins.items())
        self.onglets.set_onglets(onglets)

    def ajouter(self,parchemin:stck.ParcheminVierge|stck.ParcheminViergeNivele):
        """Ajoute une nouvelle espèce."""
        self.stockage.items.parchemin.parchemins[parchemin.nom] = parchemin
        self.onglets.set_onglets(self.onglets.onglets + [af.Onglet(parchemin.nom, OngletModificationParcheminVierge(self.stockage, parchemin, self.supprimer) if isinstance(parchemin, stck.ParcheminVierge) else OngletModificationParcheminViergeNivele(self.stockage, parchemin, self.supprimer))])
        self.onglets.select(self.onglets.boutons[-1])

    def supprimer(self,parchemin:stck.ParcheminVierge|stck.ParcheminViergeNivele):
        """Supprime une espèce."""
        self.stockage.items.parchemin.parchemins.pop(parchemin.nom)
        self.onglets.set_onglets([af.Onglet("Nouvelle espèce", OngletAjoutParchemin(self.stockage, self.ajouter))] + [af.Onglet(nom, OngletModificationParcheminVierge(self.stockage, parchemin, self.supprimer) if isinstance(parchemin, stck.ParcheminVierge) else OngletModificationParcheminViergeNivele(self.stockage, parchemin, self.supprimer)) for nom, parchemin in self.stockage.items.parchemin.parchemins.items()])
        self.onglets.select(self.onglets.boutons[0])

class OngletAjoutParchemin(af.WrapperNoeud):
    """L'onglet d'ajout d'une nouvelle parchemin."""
    def __init__(self, stockage:stck.StockageGlobal, ajouter:Callable[[stck.ParcheminVierge|stck.ParcheminViergeNivele],None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage
        self.contenu = af.ListeMargeVerticale()

        self.nom = af.TexteInput("Parchemin à remplir")
        self.avertissement_parchemin = af.TexteCache("")

        self.type = af.MenuDeroulant()
        self.type.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.type,"Parchemin vierge"),
            ]
        )
        self.type.set_contenu(af.Texte("------"))
        self.avertissement_type = af.TexteCache("")

        self.a_niveau = af.MenuDeroulant()
        self.a_niveau.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.a_niveau,"Pas de niveau"),
                af.TexteMenuDeroulant(self.a_niveau,"10 niveaux"),
            ]
        )
        self.a_niveau.set_contenu(af.Texte("------"))
        self.avertissement_a_niveau = af.TexteCache("")

        self.niveau = af.MenuDeroulant()
        self.niveau.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.niveau,f"Niveau {i}") for i in range(1,11)
            ]
        )
        self.niveau.set_contenu(af.Texte("------"))
        self.avertissement_niveau = af.TexteCache("")

        self.latence_impregne = af.NumberInput()
        self.avertissement_latence_impregne = af.TexteCache("")

        self.taux_cout_caste = af.NumberInput()
        self.avertissement_taux_cout_caste = af.TexteCache("")

        self.taux_cout_impregne = af.NumberInput()
        self.avertissement_taux_cout_impregne = af.TexteCache("")

        self.taux_latence_caste = af.NumberInput()
        self.avertissement_taux_latence_caste = af.TexteCache("")

        self.taux_latence_impregne = af.NumberInput()
        self.avertissement_taux_latence_impregne = af.TexteCache("")

        self.contenu.set_contenu([
            af.Texte("Nom du parchemin (cliquez pour éditer)"),
            self.nom,
            self.avertissement_parchemin,
            af.Texte("Type de parchemin (cliquez pour éditer)"),
            self.type,
            self.avertissement_type,
            af.Texte("Nombre de niveaux (cliquez pour éditer)"),
            self.a_niveau,
            self.avertissement_a_niveau,
            af.Texte("Niveau (cliquez pour éditer)"),
            self.niveau,
            self.avertissement_niveau,
        ])

        self.saisie_type:Optional[str] = None
        self.saisie_niveau:Optional[int] = None
        self.parametres:Dict[str,List[str]] = {
            "Parchemin vierge": [
                "latence_impregne",
                "taux_cout_caste",
                "taux_cout_impregne",
                "taux_latence_caste",
                "taux_latence_impregne",
            ]
        }
        self.saisies:Dict[str,Dict[str,List[Optional[float]]]] = {
            "Parchemin vierge": {
                "latence_impregne": [None]*11,
                "taux_cout_caste": [None]*11,
                "taux_cout_impregne": [None]*11,
                "taux_latence_caste": [None]*11,
                "taux_latence_impregne": [None]*11,
            }
        }
            
        self.super_ajouter = ajouter

    def set_courant(self, element: Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
            element.set_courant(element.courant)
            if element is self.type:
                self.change_type()
            elif element is self.a_niveau:
                self.change_a_niveau()
            elif element is self.niveau:
                self.change_niveau()
        else:
            element.set_actif()

    def change_contenu(self):
        """Change le contenu de l'onglet en fonction de ce qui est sélectionné."""
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        contenu:List[af.Affichable] = [
            af.Texte("Nom du parchemin (cliquez pour éditer)"),
            self.nom,
            self.avertissement_parchemin,
            af.Texte("Type de parchemin (cliquez pour éditer)"),
            self.type,
            self.avertissement_type,
            af.Texte("Nombre de niveaux (cliquez pour éditer)"),
            self.a_niveau,
            self.avertissement_a_niveau,
        ]
        if self.saisie_niveau: # Si saisie_niveau n'est pas None ou 0
            contenu.extend([
                af.Texte("Niveau (cliquez pour éditer)"),
                self.niveau,
                self.avertissement_niveau,
            ])
        if self.saisie_type == "Parchemin vierge" and self.saisie_niveau is not None:
            contenu.extend([
                af.Texte("Latence imprégnation (cliquez pour éditer)"),
                self.latence_impregne,
                self.avertissement_latence_impregne,
                af.Texte("Taux de coût du caste (cliquez pour éditer)"),
                self.taux_cout_caste,
                self.avertissement_taux_cout_caste,
                af.Texte("Taux de coût de l'imprégnation (cliquez pour éditer)"),
                self.taux_cout_impregne,
                self.avertissement_taux_cout_impregne,
                af.Texte("Taux de latence du caste (cliquez pour éditer)"),
                self.taux_latence_caste,
                self.avertissement_taux_latence_caste,
                af.Texte("Taux de latence de l'imprégnation (cliquez pour éditer)"),
                self.taux_latence_impregne,
                self.avertissement_taux_latence_impregne,
                af.BoutonFonction(af.SKIN_SHADE,"Ajouter",self.ajouter),
            ])
        self.contenu.set_contenu(contenu)
        self.set_tailles(self.tailles)

    def change_type(self):
        """Change le type du parchemin que l'on veut ajouter."""
        assert isinstance(self.type.contenu, af.Texte)
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        new_type = self.type.contenu.get_texte()
        if self.saisie_niveau is not None:
            # Sauvegarder le type actuel
            if self.saisie_type == "Parchemin vierge":
                
                self.saisies["Parchemin vierge"]["latence_impregne"][self.saisie_niveau] = float(self.latence_impregne.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_cout_caste"][self.saisie_niveau] = float(self.taux_cout_caste.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_cout_impregne"][self.saisie_niveau] = float(self.taux_cout_impregne.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_latence_caste"][self.saisie_niveau] = float(self.taux_latence_caste.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_latence_impregne"][self.saisie_niveau] = float(self.taux_latence_impregne.textinput.value) # type: ignore
            # Vérifier qu'on n'a pas de champs remplis
            if any([self.saisies[self.saisie_type][param][i] for param in self.parametres[self.saisie_type] for i in range(11)]): # type: ignore
                self.avertissement_type.set_texte(f"Il y a des informations saisies dans le type {self.saisie_type} !")
            else:
                self.avertissement_type.set_texte("")
        # Changer le type
        self.saisie_type = new_type
        # Changer le contenu
        self.change_contenu()

    def change_a_niveau(self):
        """Change le fait que le parchemin que l'on veut ajouter ait des niveaux."""
        assert isinstance(self.a_niveau.contenu, af.Texte)
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        new_a_niveau = self.a_niveau.contenu.get_texte()
        if self.saisie_niveau is not None:
            # Sauvegarder le niveau actuel
            if self.saisie_type == "Parchemin vierge":
                self.saisies["Parchemin vierge"]["latence_impregne"][self.saisie_niveau] = float(self.latence_impregne.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_cout_caste"][self.saisie_niveau] = float(self.taux_cout_caste.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_cout_impregne"][self.saisie_niveau] = float(self.taux_cout_impregne.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_latence_caste"][self.saisie_niveau] = float(self.taux_latence_caste.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_latence_impregne"][self.saisie_niveau] = float(self.taux_latence_impregne.textinput.value) # type: ignore
            # Vérifier qu'on n'a pas de champs remplis
            if any([self.saisies[self.saisie_type][param][self.saisie_niveau] for param in self.parametres[self.saisie_type]]): # type: ignore
                self.avertissement_a_niveau.set_texte(f"Il y a des informations saisies dans le niveau {self.saisie_niveau} !" if self.saisie_niveau else "Il y a des informations saisies !")
            else:
                self.avertissement_a_niveau.set_texte("")

        # Changer le fait que le parchemin ait des niveaux
        if new_a_niveau == "Pas de niveau":
            self.saisie_niveau = 0
        elif new_a_niveau == "10 niveaux":
            self.saisie_niveau = 1
        # Changer le contenu
        self.change_contenu()

    def change_niveau(self):
        """Change le niveau du parchemin que l'on veut ajouter dont on édite les propriétés."""
        assert isinstance(self.niveau.contenu, af.Texte)
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        new_niveau = int(self.niveau.contenu.get_texte().split(" ")[1])
        if self.saisie_niveau == 0:
            raise ValueError("On ne devrait pas avoir accès au menu de changement de niveau si on n'a pas de niveaux !")
        if self.saisie_niveau is not None:
            # Sauvegarder le niveau actuel
            if self.saisie_type == "Parchemin vierge":
                self.saisies["Parchemin vierge"]["latence_impregne"][self.saisie_niveau] = float(self.latence_impregne.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_cout_caste"][self.saisie_niveau] = float(self.taux_cout_caste.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_cout_impregne"][self.saisie_niveau] = float(self.taux_cout_impregne.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_latence_caste"][self.saisie_niveau] = float(self.taux_latence_caste.textinput.value) # type: ignore
                self.saisies["Parchemin vierge"]["taux_latence_impregne"][self.saisie_niveau] = float(self.taux_latence_impregne.textinput.value) # type: ignore
            
        # Changer le niveau
        if not 0 < new_niveau <= 10:
            self.avertissement_niveau.set_texte("Le niveau doit être compris entre 1 et 10 !")
        else:
            self.avertissement_niveau.set_texte("")
            self.saisie_niveau = new_niveau
        # Changer le contenu
        self.change_contenu()

    def ajouter(self):
        """Ajoute un nouveau parchemin."""
        nom = self.nom.textinput.value # type: ignore # Partially known type

        if nom == "":
            self.avertissement_parchemin.set_texte("Le nom ne peut pas être vide !")
        elif nom in self.stockage.items.all_noms():
            self.avertissement_parchemin.set_texte("Il y a déjà un item avec ce nom !")

        if self.saisie_niveau is None:
            self.avertissement_a_niveau.set_texte("Il faut choisir si le parchemin a des niveaux !")
        if self.saisie_type is None:
            self.avertissement_type.set_texte("Il faut choisir le type de parchemin !")

        if self.avertissement_a_niveau.get_texte() != "" or self.avertissement_type.get_texte() != "":
            self.set_tailles(self.tailles)

        else:
            assert isinstance(self.saisie_niveau, int)
            if self.saisie_type == "Parchemin vierge":
                if self.saisie_niveau == 0:
                    # Le parchemin n'a pas de niveaux
                    latence_impregne = self.latence_impregne.textinput.value # type: ignore # Partially known type
                    assert isinstance(latence_impregne, str)
                    if latence_impregne == "":
                        self.avertissement_latence_impregne.set_texte("La latence ne peut pas être vide !")
                    else:
                        latence_impregne = float(latence_impregne)
                        if latence_impregne < 0:
                            self.avertissement_latence_impregne.set_texte("La latence doit être positive !")
                        else:
                            self.avertissement_latence_impregne.set_texte("")
                    taux_cout_caste = self.taux_cout_caste.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_cout_caste, str)
                    if taux_cout_caste == "":
                        self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste ne peut pas être vide !")
                    else:
                        taux_cout_caste = float(taux_cout_caste)
                        if taux_cout_caste < 0:
                            self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste doit être positif !")
                        else:
                            self.avertissement_taux_cout_caste.set_texte("")
                    taux_cout_impregne = self.taux_cout_impregne.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_cout_impregne, str)
                    if taux_cout_impregne == "":
                        self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation ne peut pas être vide !")
                    else:
                        taux_cout_impregne = float(taux_cout_impregne)
                        if taux_cout_impregne < 0:
                            self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation doit être positif !")
                        else:
                            self.avertissement_taux_cout_impregne.set_texte("")
                    taux_latence_caste = self.taux_latence_caste.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_latence_caste, str)
                    if taux_latence_caste == "":
                        self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste ne peut pas être vide !")
                    else:
                        taux_latence_caste = float(taux_latence_caste)
                        if taux_latence_caste < 0:
                            self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste doit être positif !")
                        else:
                            self.avertissement_taux_latence_caste.set_texte("")
                    taux_latence_impregne = self.taux_latence_impregne.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_latence_impregne, str)
                    if taux_latence_impregne == "":
                        self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation ne peut pas être vide !")
                    else:
                        taux_latence_impregne = float(taux_latence_impregne)
                        if taux_latence_impregne < 0:
                            self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation doit être positif !")
                        else:
                            self.avertissement_taux_latence_impregne.set_texte("")
                    if self.avertissement_latence_impregne.get_texte() != "" or self.avertissement_taux_cout_caste.get_texte() != "" or self.avertissement_taux_cout_impregne.get_texte() != "" or self.avertissement_taux_latence_caste.get_texte() != "" or self.avertissement_taux_latence_impregne.get_texte() != "":
                        self.set_tailles(self.tailles)
                    else:
                        assert isinstance(nom, str)
                        assert isinstance(latence_impregne, int)
                        assert isinstance(taux_cout_caste, int)
                        assert isinstance(taux_cout_impregne, int)
                        assert isinstance(taux_latence_caste, int)
                        assert isinstance(taux_latence_impregne, int)
                        parchemin = stck.ParcheminVierge(nom, latence_impregne, taux_cout_caste, taux_cout_impregne, taux_latence_caste, taux_latence_impregne)
                        self.nom.textinput.value = "Parchemin à remplir"
                        self.a_niveau.set_contenu(af.Texte("------"))
                        self.niveau.set_contenu(af.Texte("------"))
                        self.latence_impregne.textinput.value = "0"
                        self.taux_cout_caste.textinput.value = "0"
                        self.taux_cout_impregne.textinput.value = "0"
                        self.taux_latence_caste.textinput.value = "0"
                        self.taux_latence_impregne.textinput.value = "0"
                        self.avertissement_parchemin.set_texte("")
                        self.avertissement_a_niveau.set_texte("")
                        self.avertissement_niveau.set_texte("")
                        self.avertissement_latence_impregne.set_texte("")
                        self.avertissement_taux_cout_caste.set_texte("")
                        self.avertissement_taux_cout_impregne.set_texte("")
                        self.avertissement_taux_latence_caste.set_texte("")
                        self.avertissement_taux_latence_impregne.set_texte("")
                        self.set_tailles(self.tailles)
                        self.super_ajouter(parchemin)
                else:
                    # Le parchemin a des niveaux
                    latence_impregne = self.latence_impregne.textinput.value # type: ignore # Partially known type
                    assert isinstance(latence_impregne, str)
                    if latence_impregne == "":
                        self.avertissement_latence_impregne.set_texte("La latence ne peut pas être vide !")
                    else:
                        latence_impregne = float(latence_impregne)
                        if latence_impregne < 0:
                            self.avertissement_latence_impregne.set_texte("La latence doit être positive !")
                        else:
                            self.avertissement_latence_impregne.set_texte("")
                            self.saisies["Parchemin vierge"]["latence_impregne"][self.saisie_niveau] = latence_impregne
                    taux_cout_caste = self.taux_cout_caste.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_cout_caste, str)
                    if taux_cout_caste == "":
                        self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste ne peut pas être vide !")
                    else:
                        taux_cout_caste = float(taux_cout_caste)
                        if taux_cout_caste < 0:
                            self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste doit être positif !")
                        else:
                            self.avertissement_taux_cout_caste.set_texte("")
                            self.saisies["Parchemin vierge"]["taux_cout_caste"][self.saisie_niveau] = taux_cout_caste
                    taux_cout_impregne = self.taux_cout_impregne.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_cout_impregne, str)
                    if taux_cout_impregne == "":
                        self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation ne peut pas être vide !")
                    else:
                        taux_cout_impregne = float(taux_cout_impregne)
                        if taux_cout_impregne < 0:
                            self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation doit être positif !")
                        else:
                            self.avertissement_taux_cout_impregne.set_texte("")
                            self.saisies["Parchemin vierge"]["taux_cout_impregne"][self.saisie_niveau] = taux_cout_impregne
                    taux_latence_caste = self.taux_latence_caste.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_latence_caste, str)
                    if taux_latence_caste == "":
                        self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste ne peut pas être vide !")
                    else:
                        taux_latence_caste = float(taux_latence_caste)
                        if taux_latence_caste < 0:
                            self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste doit être positif !")
                        else:
                            self.avertissement_taux_latence_caste.set_texte("")
                            self.saisies["Parchemin vierge"]["taux_latence_caste"][self.saisie_niveau] = taux_latence_caste
                    taux_latence_impregne = self.taux_latence_impregne.textinput.value # type: ignore # Partially known type
                    assert isinstance(taux_latence_impregne, str)
                    if taux_latence_impregne == "":
                        self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation ne peut pas être vide !")
                    else:
                        taux_latence_impregne = float(taux_latence_impregne)
                        if taux_latence_impregne < 0:
                            self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation doit être positif !")
                        else:
                            self.avertissement_taux_latence_impregne.set_texte("")
                            self.saisies["Parchemin vierge"]["taux_latence_impregne"][self.saisie_niveau] = taux_latence_impregne
                    
                    # On vérifie qu'on a bien rempli tous les champs sur tous les niveaux
                    self.avertissement_niveau.set_texte("")
                    for i in range(1,11):
                        if any([self.saisies[self.saisie_type][param][i] is None for param in self.parametres[self.saisie_type]]): # type: ignore
                            self.avertissement_niveau.set_texte(self.avertissement_niveau.get_texte() + f"Il manque des informations au niveau {i} !")

                    if self.avertissement_latence_impregne.get_texte() != "" or self.avertissement_taux_cout_caste.get_texte() != "" or self.avertissement_taux_cout_impregne.get_texte() != "" or self.avertissement_taux_latence_caste.get_texte() != "" or self.avertissement_taux_latence_impregne.get_texte() != "" or self.avertissement_niveau.get_texte() != "":
                        self.set_tailles(self.tailles)
                    else:
                        assert isinstance(nom, str)
                        _latences_impregne:List[float] = self.saisies["Parchemin vierge"]["latence_impregne"][1:] # type: ignore
                        _taux_cout_caste:List[float] = self.saisies["Parchemin vierge"]["taux_cout_caste"][1:] # type: ignore
                        _taux_cout_impregne:List[float] = self.saisies["Parchemin vierge"]["taux_cout_impregne"][1:] # type: ignore
                        _taux_latence_caste:List[float] = self.saisies["Parchemin vierge"]["taux_latence_caste"][1:] # type: ignore
                        _taux_latence_impregne:List[float] = self.saisies["Parchemin vierge"]["taux_latence_impregne"][1:] # type: ignore
                        parchemin = stck.ParcheminViergeNivele(nom, _latences_impregne, _taux_cout_caste, _taux_cout_impregne, _taux_latence_caste, _taux_latence_impregne)
                        self.nom.textinput.value = "Parchemin à remplir"
                        self.a_niveau.set_contenu(af.Texte("------"))
                        self.niveau.set_contenu(af.Texte("------"))
                        self.latence_impregne.textinput.value = "0.0"
                        self.taux_cout_caste.textinput.value = "0.0"
                        self.taux_cout_impregne.textinput.value = "0.0"
                        self.taux_latence_caste.textinput.value = "0.0"
                        self.taux_latence_impregne.textinput.value = "0.0"

class OngletModificationParcheminVierge(af.WrapperCliquable):
    """L'onglet de modification d'une espèce."""
    def __init__(self, stockage:stck.StockageGlobal, parchemin:stck.ParcheminVierge, supprimer:Callable[[stck.ParcheminVierge],None]):
        af.WrapperCliquable.__init__(self)
        self.stockage = stockage
        self.parchemin = parchemin
        self.contenu = af.ListeMargeVerticale()
        self.nom = af.TexteInput(parchemin.nom)
        self.latence_impregne = af.NumberInput(str(parchemin.latence_impregne))
        self.taux_cout_caste = af.NumberInput(str(parchemin.taux_cout_caste))
        self.taux_cout_impregne = af.NumberInput(str(parchemin.taux_cout_impregne))
        self.taux_latence_caste = af.NumberInput(str(parchemin.taux_latence_caste))
        self.taux_latence_impregne = af.NumberInput(str(parchemin.taux_latence_impregne))
        self.texte_parchemin = af.Texte(f"Nom du parchemin (cliquez pour éditer, actuellement {self.parchemin.nom})")
        self.texte_latence_impregne = af.Texte(f"Latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.latence_impregne})")
        self.texte_taux_cout_caste = af.Texte(f"Taux de coût du caste (cliquez pour éditer, actuellement {self.parchemin.taux_cout_caste})")
        self.texte_taux_cout_impregne = af.Texte(f"Taux de coût de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_cout_impregne})")
        self.texte_taux_latence_caste = af.Texte(f"Taux de latence du caste (cliquez pour éditer, actuellement {self.parchemin.taux_latence_caste})")
        self.texte_taux_latence_impregne = af.Texte(f"Taux de latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_latence_impregne})")
        self.avertissement_parchemin = af.TexteCache("")
        self.avertissement_latence_impregne = af.TexteCache("")
        self.avertissement_taux_cout_caste = af.TexteCache("")
        self.avertissement_taux_cout_impregne = af.TexteCache("")
        self.avertissement_taux_latence_caste = af.TexteCache("")
        self.avertissement_taux_latence_impregne = af.TexteCache("")
        self.contenu.set_contenu([ # type: ignore # Pylance is stupid
            self.texte_parchemin,
            self.nom,
            self.avertissement_parchemin,
            self.texte_latence_impregne,
            self.latence_impregne,
            self.avertissement_latence_impregne,
            self.texte_taux_cout_caste,
            self.taux_cout_caste,
            self.avertissement_taux_cout_caste,
            self.texte_taux_cout_impregne,
            self.taux_cout_impregne,
            self.avertissement_taux_cout_impregne,
            self.texte_taux_latence_caste,
            self.taux_latence_caste,
            self.avertissement_taux_latence_caste,
            self.texte_taux_latence_impregne,
            self.taux_latence_impregne,
            self.avertissement_taux_latence_impregne,
            af.BoutonFonction(af.SKIN_SHADE,"Modifier",self.modifier),
            af.BoutonFonction(af.SKIN_SHADE,"Supprimer",self.supprimer),
        ])
        self.super_supprimer = supprimer

    def modifier(self):
        """Modifie le parchemin."""
        nom = self.nom.textinput.value # type: ignore # Partially known type
        latence_impregne = self.latence_impregne.textinput.value # type: ignore # Partially known type
        taux_cout_caste = self.taux_cout_caste.textinput.value # type: ignore # Partially known type
        taux_cout_impregne = self.taux_cout_impregne.textinput.value # type: ignore # Partially known type
        taux_latence_caste = self.taux_latence_caste.textinput.value # type: ignore # Partially known type
        taux_latence_impregne = self.taux_latence_impregne.textinput.value # type: ignore # Partially known type

        assert isinstance(nom, str)
        assert isinstance(latence_impregne, str)
        assert isinstance(taux_cout_caste, str)
        assert isinstance(taux_cout_impregne, str)
        assert isinstance(taux_latence_caste, str)
        assert isinstance(taux_latence_impregne, str)
        assert isinstance(self.contenu, af.ListeMargeVerticale)

        if nom == "":
            self.avertissement_parchemin.set_texte("Le nom ne peut pas être vide !")
        elif nom in self.stockage.items.all_noms():
            self.avertissement_parchemin.set_texte("Il y a déjà une espèce avec ce nom !")

        if latence_impregne == "":
            self.avertissement_latence_impregne.set_texte("La latence ne peut pas être vide !")
        else:
            latence_impregne = float(latence_impregne)
            if latence_impregne < 0:
                self.avertissement_latence_impregne.set_texte("La latence doit être positive !")
            else:
                self.avertissement_latence_impregne.set_texte("")

        if taux_cout_caste == "":
            self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste ne peut pas être vide !")
        else:
            taux_cout_caste = float(taux_cout_caste)
            if taux_cout_caste < 0:
                self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste doit être positif !")
            else:
                self.avertissement_taux_cout_caste.set_texte("")

        if taux_cout_impregne == "":
            self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation ne peut pas être vide !")
        else:
            taux_cout_impregne = float(taux_cout_impregne)
            if taux_cout_impregne < 0:
                self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation doit être positif !")
            else:
                self.avertissement_taux_cout_impregne.set_texte("")

        if taux_latence_caste == "":
            self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste ne peut pas être vide !")
        else:
            taux_latence_caste = float(taux_latence_caste)
            if taux_latence_caste < 0:
                self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste doit être positif !")
            else:
                self.avertissement_taux_latence_caste.set_texte("")

        if taux_latence_impregne == "":
            self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation ne peut pas être vide !")
        else:
            taux_latence_impregne = float(taux_latence_impregne)
            if taux_latence_impregne < 0:
                self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation doit être positif !")
            else:
                self.avertissement_taux_latence_impregne.set_texte("")
        
        if self.avertissement_parchemin.get_texte() != "" or self.avertissement_latence_impregne.get_texte() != "" or self.avertissement_taux_cout_caste.get_texte() != "" or self.avertissement_taux_cout_impregne.get_texte() != "" or self.avertissement_taux_latence_caste.get_texte() != "" or self.avertissement_taux_latence_impregne.get_texte() != "":
            self.set_tailles(self.tailles)

        else:
            self.parchemin.nom = self.nom.textinput.value # type: ignore # Partially known type
            self.parchemin.latence_impregne = float(self.latence_impregne.textinput.value) # type: ignore # Partially known type
            self.parchemin.taux_cout_caste = float(self.taux_cout_caste.textinput.value) # type: ignore # Partially known type
            self.parchemin.taux_cout_impregne = float(self.taux_cout_impregne.textinput.value) # type: ignore # Partially known type
            self.parchemin.taux_latence_caste = float(self.taux_latence_caste.textinput.value) # type: ignore # Partially known type
            self.parchemin.taux_latence_impregne = float(self.taux_latence_impregne.textinput.value) # type: ignore # Partially known type
            self.texte_parchemin.set_texte(f"Nom du parchemin (cliquez pour éditer, actuellement {self.parchemin.nom})")
            self.texte_latence_impregne.set_texte(f"Latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.latence_impregne})")
            self.texte_taux_cout_caste.set_texte(f"Taux de coût du caste (cliquez pour éditer, actuellement {self.parchemin.taux_cout_caste})")
            self.texte_taux_cout_impregne.set_texte(f"Taux de coût de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_cout_impregne})")
            self.texte_taux_latence_caste.set_texte(f"Taux de latence du caste (cliquez pour éditer, actuellement {self.parchemin.taux_latence_caste})")
            self.texte_taux_latence_impregne.set_texte(f"Taux de latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_latence_impregne})")
            self.set_tailles(self.tailles)

    def supprimer(self):
        """Supprime l'espèce."""
        self.super_supprimer(self.parchemin)

class OngletModificationParcheminViergeNivele(af.WrapperNoeud):
    """L'onglet de modification d'une espèce."""
    def __init__(self, stockage:stck.StockageGlobal, parchemin:stck.ParcheminViergeNivele, supprimer:Callable[[stck.ParcheminViergeNivele],None]):
        af.WrapperNoeud.__init__(self)
        self.stockage = stockage
        self.parchemin = parchemin
        self.contenu = af.ListeMargeVerticale()
        self.nom = af.TexteInput(parchemin.nom)
        self.niveau = af.MenuDeroulant()
        self.niveau.set_contenu_liste(
            [
                af.TexteMenuDeroulant(self.niveau, f"Niveau {i}") for i in range(1,11)
            ]
        )
        self.niveau.set_contenu(af.Texte("Niveau 1"))
        self.latence_impregne = af.NumberInput(str(parchemin.latences_impregne[0]))
        self.taux_cout_caste = af.NumberInput(str(parchemin.taux_cout_caste[0]))
        self.taux_cout_impregne = af.NumberInput(str(parchemin.taux_cout_impregne[0]))
        self.taux_latence_caste = af.NumberInput(str(parchemin.taux_latence_caste[0]))
        self.taux_latence_impregne = af.NumberInput(str(parchemin.taux_latence_impregne[0]))
        self.texte_parchemin = af.Texte(f"Nom du parchemin (cliquez pour éditer, actuellement {self.parchemin.nom})")
        self.texte_latence_impregne = af.Texte(f"Latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.latences_impregne[0]})")
        self.texte_taux_cout_caste = af.Texte(f"Taux de coût du caste (cliquez pour éditer, actuellement {self.parchemin.taux_cout_caste[0]})")
        self.texte_taux_cout_impregne = af.Texte(f"Taux de coût de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_cout_impregne[0]})")
        self.texte_taux_latence_caste = af.Texte(f"Taux de latence du caste (cliquez pour éditer, actuellement {self.parchemin.taux_latence_caste[0]})")
        self.texte_taux_latence_impregne = af.Texte(f"Taux de latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_latence_impregne[0]})")
        self.avertissement_parchemin = af.TexteCache("")
        self.avertissement_niveau = af.TexteCache("")
        self.avertissement_latence_impregne = af.TexteCache("")
        self.avertissement_taux_cout_caste = af.TexteCache("")
        self.avertissement_taux_cout_impregne = af.TexteCache("")
        self.avertissement_taux_latence_caste = af.TexteCache("")
        self.avertissement_taux_latence_impregne = af.TexteCache("")
        self.contenu.set_contenu([ # type: ignore # Pylance is stupid
            self.texte_parchemin,
            self.nom,
            self.avertissement_parchemin,
            self.texte_latence_impregne,
            self.latence_impregne,
            self.avertissement_latence_impregne,
            self.texte_taux_cout_caste,
            self.taux_cout_caste,
            self.avertissement_taux_cout_caste,
            self.texte_taux_cout_impregne,
            self.taux_cout_impregne,
            self.avertissement_taux_cout_impregne,
            self.texte_taux_latence_caste,
            self.taux_latence_caste,
            self.avertissement_taux_latence_caste,
            self.texte_taux_latence_impregne,
            self.taux_latence_impregne,
            self.avertissement_taux_latence_impregne,
            af.BoutonFonction(af.SKIN_SHADE,"Modifier",self.modifier),
            af.BoutonFonction(af.SKIN_SHADE,"Supprimer",self.supprimer),
        ])

        self.saisie_niveau:int = 1
        self.parametres:List[str] = [
            "latence_impregne",
            "taux_cout_caste",
            "taux_cout_impregne",
            "taux_latence_caste",
            "taux_latence_impregne",
        ]
        self.saisies:Dict[str,List[float]] = {
            "latence_impregne": parchemin.latences_impregne.copy(),
            "taux_cout_caste": parchemin.taux_cout_caste.copy(),
            "taux_cout_impregne": parchemin.taux_cout_impregne.copy(),
            "taux_latence_caste": parchemin.taux_latence_caste.copy(),
            "taux_latence_impregne": parchemin.taux_latence_impregne.copy(),
        }

        self.super_supprimer = supprimer

    def set_courant(self, element: Cliquable | None):
        self.courant = element
        if element is None:
            self.set_actif()
        elif isinstance(element, af.Noeud):
            element.set_courant(element.courant)
            if element is self.niveau:
                self.change_niveau()
        else:
            element.set_actif()

    def change_niveau(self):
        """Change le niveau du parchemin que l'on veut ajouter dont on édite les propriétés."""
        assert isinstance(self.niveau.contenu, af.Texte)
        assert isinstance(self.contenu, af.ListeMargeVerticale)
        new_niveau = int(self.niveau.contenu.get_texte().split(" ")[1])
        self.saisies["latence_impregne"][self.saisie_niveau-1] = float(self.latence_impregne.textinput.value) # type: ignore
        self.saisies["taux_cout_caste"][self.saisie_niveau-1] = float(self.taux_cout_caste.textinput.value) # type: ignore
        self.saisies["taux_cout_impregne"][self.saisie_niveau-1] = float(self.taux_cout_impregne.textinput.value) # type: ignore
        self.saisies["taux_latence_caste"][self.saisie_niveau-1] = float(self.taux_latence_caste.textinput.value) # type: ignore
        self.saisies["taux_latence_impregne"][self.saisie_niveau-1] = float(self.taux_latence_impregne.textinput.value) # type: ignore
        
        # Changer le niveau
        if not 0 < new_niveau <= 10:
            self.avertissement_niveau.set_texte("Le niveau doit être compris entre 1 et 10 !")
        else:
            self.avertissement_niveau.set_texte("")
            self.saisie_niveau = new_niveau
        # Changer le contenu
        self.latence_impregne.textinput.value = str(self.saisies["latence_impregne"][self.saisie_niveau-1])
        self.texte_latence_impregne.set_texte(f"Latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.latences_impregne[self.saisie_niveau-1]})")
        self.taux_cout_caste.textinput.value = str(self.saisies["taux_cout_caste"][self.saisie_niveau-1])
        self.texte_taux_cout_caste.set_texte(f"Taux de coût du caste (cliquez pour éditer, actuellement {self.parchemin.taux_cout_caste[self.saisie_niveau-1]})")
        self.taux_cout_impregne.textinput.value = str(self.saisies["taux_cout_impregne"][self.saisie_niveau-1])
        self.texte_taux_cout_impregne.set_texte(f"Taux de coût de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_cout_impregne[self.saisie_niveau-1]})")
        self.taux_latence_caste.textinput.value = str(self.saisies["taux_latence_caste"][self.saisie_niveau-1])
        self.texte_taux_latence_caste.set_texte(f"Taux de latence du caste (cliquez pour éditer, actuellement {self.parchemin.taux_latence_caste[self.saisie_niveau-1]})")
        self.taux_latence_impregne.textinput.value = str(self.saisies["taux_latence_impregne"][self.saisie_niveau-1])
        self.texte_taux_latence_impregne.set_texte(f"Taux de latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_latence_impregne[self.saisie_niveau-1]})")
        self.set_tailles(self.tailles)

    def modifier(self):
        """Modifie le parchemin."""
        nom = self.nom.textinput.value # type: ignore # Partially known type
        latence_impregne = self.latence_impregne.textinput.value # type: ignore # Partially known type
        taux_cout_caste = self.taux_cout_caste.textinput.value # type: ignore # Partially known type
        taux_cout_impregne = self.taux_cout_impregne.textinput.value # type: ignore # Partially known type
        taux_latence_caste = self.taux_latence_caste.textinput.value # type: ignore # Partially known type
        taux_latence_impregne = self.taux_latence_impregne.textinput.value # type: ignore # Partially known type

        assert isinstance(nom, str)
        assert isinstance(latence_impregne, str)
        assert isinstance(taux_cout_caste, str)
        assert isinstance(taux_cout_impregne, str)
        assert isinstance(taux_latence_caste, str)
        assert isinstance(taux_latence_impregne, str)
        assert isinstance(self.contenu, af.ListeMargeVerticale)

        if nom == "":
            self.avertissement_parchemin.set_texte("Le nom ne peut pas être vide !")
        elif nom in self.stockage.items.all_noms():
            self.avertissement_parchemin.set_texte("Il y a déjà une espèce avec ce nom !")

        if latence_impregne == "":
            self.avertissement_latence_impregne.set_texte("La latence ne peut pas être vide !")
        else:
            latence_impregne = float(latence_impregne)
            if latence_impregne < 0:
                self.avertissement_latence_impregne.set_texte("La latence doit être positive !")
            else:
                self.avertissement_latence_impregne.set_texte("")
                self.saisies["latences_impregne"][self.saisie_niveau] = latence_impregne

        if taux_cout_caste == "":
            self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste ne peut pas être vide !")
        else:
            taux_cout_caste = float(taux_cout_caste)
            if taux_cout_caste < 0:
                self.avertissement_taux_cout_caste.set_texte("Le taux de coût du caste doit être positif !")
            else:
                self.avertissement_taux_cout_caste.set_texte("")
                self.saisies["taux_cout_caste"][self.saisie_niveau] = taux_cout_caste

        if taux_cout_impregne == "":
            self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation ne peut pas être vide !")
        else:
            taux_cout_impregne = float(taux_cout_impregne)
            if taux_cout_impregne < 0:
                self.avertissement_taux_cout_impregne.set_texte("Le taux de coût de l'imprégnation doit être positif !")
            else:
                self.avertissement_taux_cout_impregne.set_texte("")
                self.saisies["taux_cout_impregne"][self.saisie_niveau] = taux_cout_impregne

        if taux_latence_caste == "":
            self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste ne peut pas être vide !")
        else:
            taux_latence_caste = float(taux_latence_caste)
            if taux_latence_caste < 0:
                self.avertissement_taux_latence_caste.set_texte("Le taux de latence du caste doit être positif !")
            else:
                self.avertissement_taux_latence_caste.set_texte("")
                self.saisies["taux_latence_caste"][self.saisie_niveau] = taux_latence_caste

        if taux_latence_impregne == "":
            self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation ne peut pas être vide !")
        else:
            taux_latence_impregne = float(taux_latence_impregne)
            if taux_latence_impregne < 0:
                self.avertissement_taux_latence_impregne.set_texte("Le taux de latence de l'imprégnation doit être positif !")
            else:
                self.avertissement_taux_latence_impregne.set_texte("")
                self.saisies["taux_latence_impregne"][self.saisie_niveau] = taux_latence_impregne
        
        if self.avertissement_parchemin.get_texte() != "" or self.avertissement_latence_impregne.get_texte() != "" or self.avertissement_taux_cout_caste.get_texte() != "" or self.avertissement_taux_cout_impregne.get_texte() != "" or self.avertissement_taux_latence_caste.get_texte() != "" or self.avertissement_taux_latence_impregne.get_texte() != "":
            self.set_tailles(self.tailles)

        else:
            self.parchemin.nom = self.nom.textinput.value # type: ignore # Partially known type
            self.parchemin.latences_impregne = self.saisies["latence_impregne"]
            self.parchemin.taux_cout_caste = self.saisies["taux_cout_caste"]
            self.parchemin.taux_cout_impregne = self.saisies["taux_cout_impregne"]
            self.parchemin.taux_latence_caste = self.saisies["taux_latence_caste"]
            self.parchemin.taux_latence_impregne = self.saisies["taux_latence_impregne"]
            self.texte_parchemin.set_texte(f"Nom du parchemin (cliquez pour éditer, actuellement {self.parchemin.nom})")
            self.texte_latence_impregne.set_texte(f"Latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.latences_impregne[self.saisie_niveau-1]})")
            self.texte_taux_cout_caste.set_texte(f"Taux de coût du caste (cliquez pour éditer, actuellement {self.parchemin.taux_cout_caste[self.saisie_niveau-1]})")
            self.texte_taux_cout_impregne.set_texte(f"Taux de coût de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_cout_impregne[self.saisie_niveau-1]})")
            self.texte_taux_latence_caste.set_texte(f"Taux de latence du caste (cliquez pour éditer, actuellement {self.parchemin.taux_latence_caste[self.saisie_niveau-1]})")
            self.texte_taux_latence_impregne.set_texte(f"Taux de latence de l'imprégnation (cliquez pour éditer, actuellement {self.parchemin.taux_latence_impregne[self.saisie_niveau-1]})")
            self.set_tailles(self.tailles)

    def supprimer(self):
        """Supprime l'espèce."""
        self.super_supprimer(self.parchemin)
