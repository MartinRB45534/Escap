"""
Ce fichier contient les classes des projectiles et des items qui peuvent être lancés.
"""

from __future__ import annotations

# Imports des classes parentes
from .equippement import Equippement
from .anneau import Anneau
from .armure import Armure
from .heaume import Heaume
from .role import DefensifPlafond, DefensifProportion, DefensifSeuil, DefensifValeur, PompeAPV, RenforceRegenPV, PompeAPM, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal

class EquippementGenerique(Equippement):
    """Un équippement générique, avec les arguments utilisés par tous les équippements."""

class AnneauGenerique(Anneau, EquippementGenerique):
    """Un anneau générique, avec les arguments utilisés par tous les anneaux."""

class AnneauDefensifPlafond(AnneauGenerique, DefensifPlafond):
    """Un anneau défensif plafonnant les dégats."""

class AnneauDefensifProportion(AnneauGenerique, DefensifProportion):
    """Un anneau défensif proportionnel aux dégats."""

class AnneauDefensifSeuil(AnneauGenerique, DefensifSeuil):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil."""

class AnneauDefensifValeur(AnneauGenerique, DefensifValeur):
    """Un anneau défensif bloquant une valeur fixe de dégats."""

class AnneauPompeAPV(AnneauGenerique, PompeAPV):
    """Un anneau pompant les PV."""

class AnneauRenforceRegenPV(AnneauGenerique, RenforceRegenPV):
    """Un anneau renforçant la régénération des PV."""

class AnneauPompeAPM(AnneauGenerique, PompeAPM):
    """Un anneau pompant les PM."""

class AnneauRenforceRegenPM(AnneauGenerique, RenforceRegenPM):
    """Un anneau renforçant la régénération des PM."""

class AnneauAccelerateur(AnneauGenerique, Accelerateur):
    """Un anneau qui augmente la vitesse."""

class AnneauAnoblisseur(AnneauGenerique, Anoblisseur):
    """Un anneau qui augmente la priorité."""

class AnneauElementaire(AnneauGenerique, Elementaire):
    """Un anneau qui renforce l'affinité à un élément."""

class AnneauTribal(AnneauGenerique, EquippementTribal):
    """Un anneau qui est dédié à une espèce."""

class AnneauDefensifPlafondPompeAPV(AnneauGenerique, DefensifPlafond, PompeAPV):
    """Un anneau défensif plafonnant les dégats et pompant les PV."""

class AnneauDefensifPlafondRenforceRegenPV(AnneauGenerique, DefensifPlafond, RenforceRegenPV):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV."""

class AnneauDefensifProportionPompeAPV(AnneauGenerique, DefensifProportion, PompeAPV):
    """Un anneau défensif proportionnel aux dégats et pompant les PV."""

class AnneauDefensifProportionRenforceRegenPV(AnneauGenerique, DefensifProportion, RenforceRegenPV):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV."""

class AnneauDefensifSeuilPompeAPV(AnneauGenerique, DefensifSeuil, PompeAPV):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV."""

class AnneauDefensifSeuilRenforceRegenPV(AnneauGenerique, DefensifSeuil, RenforceRegenPV):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV."""

class AnneauDefensifValeurPompeAPV(AnneauGenerique, DefensifValeur, PompeAPV):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV."""

class AnneauDefensifValeurRenforceRegenPV(AnneauGenerique, DefensifValeur, RenforceRegenPV):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV."""

class AnneauDefensifPlafondPompeAPM(AnneauGenerique, DefensifPlafond, PompeAPM):
    """Un anneau défensif plafonnant les dégats et pompant les PM."""

class AnneauDefensifPlafondRenforceRegenPM(AnneauGenerique, DefensifPlafond, RenforceRegenPM):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM."""

class AnneauDefensifProportionPompeAPM(AnneauGenerique, DefensifProportion, PompeAPM):
    """Un anneau défensif proportionnel aux dégats et pompant les PM."""

class AnneauDefensifProportionRenforceRegenPM(AnneauGenerique, DefensifProportion, RenforceRegenPM):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM."""

class AnneauDefensifSeuilPompeAPM(AnneauGenerique, DefensifSeuil, PompeAPM):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM."""

class AnneauDefensifSeuilRenforceRegenPM(AnneauGenerique, DefensifSeuil, RenforceRegenPM):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM."""

class AnneauDefensifValeurPompeAPM(AnneauGenerique, DefensifValeur, PompeAPM):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM."""

class AnneauDefensifValeurRenforceRegenPM(AnneauGenerique, DefensifValeur, RenforceRegenPM):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM."""

class AnneauPompeAPVPompeAPM(AnneauGenerique, PompeAPV, PompeAPM):
    """Un anneau pompant les PV et les PM."""

class AnneauPompeAPVRenforceRegenPM(AnneauGenerique, PompeAPV, RenforceRegenPM):
    """Un anneau pompant les PV et renforçant la régénération des PM."""

class AnneauRenforceRegenPVPompeAPM(AnneauGenerique, RenforceRegenPV, PompeAPM):
    """Un anneau renforçant la régénération des PV et pompant les PM."""

class AnneauRenforceRegenPVRenforceRegenPM(AnneauGenerique, RenforceRegenPV, RenforceRegenPM):
    """Un anneau renforçant la régénération des PV et des PM."""

class AnneauDefensifPlafondAccelerateur(AnneauGenerique, DefensifPlafond, Accelerateur):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse."""

class AnneauDefensifProportionAccelerateur(AnneauGenerique, DefensifProportion, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse."""

class AnneauDefensifSeuilAccelerateur(AnneauGenerique, DefensifSeuil, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse."""

class AnneauDefensifValeurAccelerateur(AnneauGenerique, DefensifValeur, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse."""

class AnneauPompeAPVAccelerateur(AnneauGenerique, PompeAPV, Accelerateur):
    """Un anneau pompant les PV et augmentant la vitesse."""

class AnneauRenforceRegenPVAccelerateur(AnneauGenerique, RenforceRegenPV, Accelerateur):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse."""

class AnneauPompeAPMAccelerateur(AnneauGenerique, PompeAPM, Accelerateur):
    """Un anneau pompant les PM et augmentant la vitesse."""

class AnneauRenforceRegenPMAccelerateur(AnneauGenerique, RenforceRegenPM, Accelerateur):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifPlafondAnoblisseur(AnneauGenerique, DefensifPlafond, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et augmentant la priorité."""

class AnneauDefensifProportionAnoblisseur(AnneauGenerique, DefensifProportion, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et augmentant la priorité."""

class AnneauDefensifSeuilAnoblisseur(AnneauGenerique, DefensifSeuil, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité."""

class AnneauDefensifValeurAnoblisseur(AnneauGenerique, DefensifValeur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la priorité."""

class AnneauPompeAPVAnoblisseur(AnneauGenerique, PompeAPV, Anoblisseur):
    """Un anneau pompant les PV et augmentant la priorité."""

class AnneauRenforceRegenPVAnoblisseur(AnneauGenerique, RenforceRegenPV, Anoblisseur):
    """Un anneau renforçant la régénération des PV et augmentant la priorité."""

class AnneauPompeAPMAnoblisseur(AnneauGenerique, PompeAPM, Anoblisseur):
    """Un anneau pompant les PM et augmentant la priorité."""

class AnneauRenforceRegenPMAnoblisseur(AnneauGenerique, RenforceRegenPM, Anoblisseur):
    """Un anneau renforçant la régénération des PM et augmentant la priorité."""

class AnneauAccelerateurAnoblisseur(AnneauGenerique, Accelerateur, Anoblisseur):
    """Un anneau augmentant la vitesse et la priorité."""

class AnneauDefensifPlafondElementaire(AnneauGenerique, DefensifPlafond, Elementaire):
    """Un anneau défensif plafonnant les dégats et augmentant l'affinité à un élément."""

class AnneauDefensifProportionElementaire(AnneauGenerique, DefensifProportion, Elementaire):
    """Un anneau défensif proportionnel aux dégats et augmentant l'affinité à un élément."""

class AnneauDefensifSeuilElementaire(AnneauGenerique, DefensifSeuil, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité à un élément."""

class AnneauDefensifValeurElementaire(AnneauGenerique, DefensifValeur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant l'affinité à un élément."""

class AnneauPompeAPVElementaire(AnneauGenerique, PompeAPV, Elementaire):
    """Un anneau pompant les PV et augmentant l'affinité à un élément."""

class AnneauRenforceRegenPVElementaire(AnneauGenerique, RenforceRegenPV, Elementaire):
    """Un anneau renforçant la régénération des PV et augmentant l'affinité à un élément."""

class AnneauPompeAPMElementaire(AnneauGenerique, PompeAPM, Elementaire):
    """Un anneau pompant les PM et augmentant l'affinité à un élément."""

class AnneauRenforceRegenPMElementaire(AnneauGenerique, RenforceRegenPM, Elementaire):
    """Un anneau renforçant la régénération des PM et augmentant l'affinité à un élément."""

class AnneauAccelerateurElementaire(AnneauGenerique, Accelerateur, Elementaire):
    """Un anneau augmentant la vitesse et l'affinité à un élément."""

class AnneauAnoblisseurElementaire(AnneauGenerique, Anoblisseur, Elementaire):
    """Un anneau augmentant la priorité et l'affinité à un élément."""

class AnneauDefensifPlafondTribal(AnneauGenerique, DefensifPlafond, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant l'affinité."""

class AnneauDefensifProportionTribal(AnneauGenerique, DefensifProportion, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant l'affinité."""

class AnneauDefensifSeuilTribal(AnneauGenerique, DefensifSeuil, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité."""

class AnneauDefensifValeurTribal(AnneauGenerique, DefensifValeur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant l'affinité."""

class AnneauPompeAPVTribal(AnneauGenerique, PompeAPV, EquippementTribal):
    """Un anneau pompant les PV et augmentant l'affinité."""

class AnneauRenforceRegenPVTribal(AnneauGenerique, RenforceRegenPV, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant l'affinité."""

class AnneauPompeAPMTribal(AnneauGenerique, PompeAPM, EquippementTribal):
    """Un anneau pompant les PM et augmentant l'affinité."""

class AnneauRenforceRegenPMTribal(AnneauGenerique, RenforceRegenPM, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant l'affinité."""

class AnneauAccelerateurTribal(AnneauGenerique, Accelerateur, EquippementTribal):
    """Un anneau augmentant la vitesse et l'affinité."""

class AnneauAnoblisseurTribal(AnneauGenerique, Anoblisseur, EquippementTribal):
    """Un anneau augmentant la priorité et l'affinité."""

class AnneauElementaireTribal(AnneauGenerique, Elementaire, EquippementTribal):
    """Un anneau augmentant l'affinité à un élément et l'affinité à une espèce."""

class AnneauDefensifPlafondPompeAPVPompeAPM(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM."""

class AnneauDefensifProportionPompeAPVPompeAPM(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM."""

class AnneauDefensifSeuilPompeAPVPompeAPM(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM."""

class AnneauDefensifValeurPompeAPVPompeAPM(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPM(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM."""

class AnneauDefensifProportionRenforceRegenPVPompeAPM(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPM(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM."""

class AnneauDefensifValeurRenforceRegenPVPompeAPM(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPM(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM."""

class AnneauDefensifProportionPompeAPVRenforceRegenPM(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPM(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM."""

class AnneauDefensifValeurPompeAPVRenforceRegenPM(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPM(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPM(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPM(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPM(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM."""

class AnneauDefensifPlafondPompeAPVAccelerateur(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse."""

class AnneauDefensifProportionPompeAPVAccelerateur(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse."""

class AnneauDefensifSeuilPompeAPVAccelerateur(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse."""

class AnneauDefensifValeurPompeAPVAccelerateur(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse."""

class AnneauDefensifProportionRenforceRegenPVAccelerateur(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse."""

class AnneauDefensifValeurRenforceRegenPVAccelerateur(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse."""

class AnneauDefensifPlafondPompeAPMAccelerateur(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse."""

class AnneauDefensifProportionPompeAPMAccelerateur(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse."""

class AnneauDefensifSeuilPompeAPMAccelerateur(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse."""

class AnneauDefensifValeurPompeAPMAccelerateur(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateur(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifProportionRenforceRegenPMAccelerateur(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateur(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifValeurRenforceRegenPMAccelerateur(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauPompeAPVPompeAPMAccelerateur(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur):
    """Un anneau pompant les PV et les PM et augmentant la vitesse."""

class AnneauRenforceRegenPVPompeAPMAccelerateur(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class AnneauPompeAPVRenforceRegenPMAccelerateur(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateur(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse."""

class AnneauDefensifPlafondPompeAPVAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPV, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la priorité."""

class AnneauDefensifProportionPompeAPVAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPV, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPVAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPV, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité."""

class AnneauDefensifValeurPompeAPVAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPV, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPVAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPVAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPVAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPVAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPMAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPM, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la priorité."""

class AnneauDefensifProportionPompeAPMAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPM, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPMAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPM, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité."""

class AnneauDefensifValeurPompeAPMAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPM, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité."""

class AnneauPompeAPVPompeAPMAnoblisseur(AnneauGenerique, PompeAPV, PompeAPM, Anoblisseur):
    """Un anneau pompant les PV et les PM et augmentant la priorité."""

class AnneauRenforceRegenPVPompeAPMAnoblisseur(AnneauGenerique, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class AnneauPompeAPVRenforceRegenPMAnoblisseur(AnneauGenerique, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class AnneauRenforceRegenPVRenforceRegenPMAnoblisseur(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la priorité."""

class AnneauDefensifPlafondAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et la priorité."""

class AnneauDefensifProportionAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et la priorité."""

class AnneauDefensifSeuilAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et la priorité."""

class AnneauDefensifValeurAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et la priorité."""

class AnneauPompeAPVAccelerateurAnoblisseur(AnneauGenerique, PompeAPV, Accelerateur, Anoblisseur):
    """Un anneau pompant les PV et augmentant la vitesse et la priorité."""

class AnneauRenforceRegenPVAccelerateurAnoblisseur(AnneauGenerique, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et la priorité."""

class AnneauPompeAPMAccelerateurAnoblisseur(AnneauGenerique, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau pompant les PM et augmentant la vitesse et la priorité."""

class AnneauRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et la priorité."""

class AnneauDefensifPlafondPompeAPVElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVElementaire(AnneauGenerique, DefensifProportion, PompeAPV, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVElementaire(AnneauGenerique, DefensifValeur, PompeAPV, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMElementaire(AnneauGenerique, DefensifPlafond, PompeAPM, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMElementaire(AnneauGenerique, DefensifProportion, PompeAPM, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMElementaire(AnneauGenerique, DefensifSeuil, PompeAPM, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMElementaire(AnneauGenerique, DefensifValeur, PompeAPM, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPM, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPM, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMElementaire(AnneauGenerique, PompeAPV, PompeAPM, Elementaire):
    """Un anneau pompant les PV et les PM et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMElementaire(AnneauGenerique, RenforceRegenPV, PompeAPM, Elementaire):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMElementaire(AnneauGenerique, PompeAPV, RenforceRegenPM, Elementaire):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMElementaire(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un anneau renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondAccelerateurElementaire(AnneauGenerique, DefensifPlafond, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et l'affinité élémentaire."""

class AnneauDefensifProportionAccelerateurElementaire(AnneauGenerique, DefensifProportion, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et l'affinité élémentaire."""

class AnneauDefensifSeuilAccelerateurElementaire(AnneauGenerique, DefensifSeuil, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et l'affinité élémentaire."""

class AnneauDefensifValeurAccelerateurElementaire(AnneauGenerique, DefensifValeur, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et l'affinité élémentaire."""

class AnneauPompeAPVAccelerateurElementaire(AnneauGenerique, PompeAPV, Accelerateur, Elementaire):
    """Un anneau pompant les PV et augmentant la vitesse et l'affinité élémentaire."""

class AnneauRenforceRegenPVAccelerateurElementaire(AnneauGenerique, RenforceRegenPV, Accelerateur, Elementaire):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et l'affinité élémentaire."""

class AnneauPompeAPMAccelerateurElementaire(AnneauGenerique, PompeAPM, Accelerateur, Elementaire):
    """Un anneau pompant les PM et augmentant la vitesse et l'affinité élémentaire."""

class AnneauRenforceRegenPMAccelerateurElementaire(AnneauGenerique, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et l'affinité élémentaire."""

class AnneauDefensifPlafondAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et augmentant la priorité et l'affinité élémentaire."""

class AnneauDefensifProportionAnoblisseurElementaire(AnneauGenerique, DefensifProportion, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et augmentant la priorité et l'affinité élémentaire."""

class AnneauDefensifSeuilAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et l'affinité élémentaire."""

class AnneauDefensifValeurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la priorité et l'affinité élémentaire."""

class AnneauPompeAPVAnoblisseurElementaire(AnneauGenerique, PompeAPV, Anoblisseur, Elementaire):
    """Un anneau pompant les PV et augmentant la priorité et l'affinité élémentaire."""

class AnneauRenforceRegenPVAnoblisseurElementaire(AnneauGenerique, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PV et augmentant la priorité et l'affinité élémentaire."""

class AnneauPompeAPMAnoblisseurElementaire(AnneauGenerique, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau pompant les PM et augmentant la priorité et l'affinité élémentaire."""

class AnneauRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PM et augmentant la priorité et l'affinité élémentaire."""

class AnneauAccelerateurAnoblisseurElementaire(AnneauGenerique, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau augmentant la vitesse et la priorité et l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVTribal(AnneauGenerique, DefensifPlafond, PompeAPV, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant l'affinité tribale."""

class AnneauDefensifProportionPompeAPVTribal(AnneauGenerique, DefensifProportion, PompeAPV, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité tribale."""

class AnneauDefensifSeuilPompeAPVTribal(AnneauGenerique, DefensifSeuil, PompeAPV, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité tribale."""

class AnneauDefensifValeurPompeAPVTribal(AnneauGenerique, DefensifValeur, PompeAPV, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité tribale."""

class AnneauDefensifPlafondRenforceRegenPVTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class AnneauDefensifProportionRenforceRegenPVTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class AnneauDefensifSeuilRenforceRegenPVTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité tribale."""

class AnneauDefensifValeurRenforceRegenPVTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class AnneauDefensifPlafondPompeAPMTribal(AnneauGenerique, DefensifPlafond, PompeAPM, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant l'affinité tribale."""

class AnneauDefensifProportionPompeAPMTribal(AnneauGenerique, DefensifProportion, PompeAPM, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité tribale."""

class AnneauDefensifSeuilPompeAPMTribal(AnneauGenerique, DefensifSeuil, PompeAPM, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité tribale."""

class AnneauDefensifValeurPompeAPMTribal(AnneauGenerique, DefensifValeur, PompeAPM, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité tribale."""

class AnneauDefensifPlafondRenforceRegenPMTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class AnneauDefensifProportionRenforceRegenPMTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class AnneauDefensifSeuilRenforceRegenPMTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité tribale."""

class AnneauDefensifValeurRenforceRegenPMTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class AnneauPompeAPVPompeAPMTribal(AnneauGenerique, PompeAPV, PompeAPM, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant l'affinité tribale."""

class AnneauRenforceRegenPVPompeAPMTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant l'affinité tribale."""

class AnneauPompeAPVRenforceRegenPMTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant l'affinité tribale."""

class AnneauRenforceRegenPVRenforceRegenPMTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un anneau renforçant la régénération des PV et des PM et augmentant l'affinité tribale."""

class AnneauDefensifPlafondAccelerateurTribal(AnneauGenerique, DefensifPlafond, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et l'affinité tribale."""

class AnneauDefensifProportionAccelerateurTribal(AnneauGenerique, DefensifProportion, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et l'affinité tribale."""

class AnneauDefensifSeuilAccelerateurTribal(AnneauGenerique, DefensifSeuil, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et l'affinité tribale."""

class AnneauDefensifValeurAccelerateurTribal(AnneauGenerique, DefensifValeur, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et l'affinité tribale."""

class AnneauPompeAPVAccelerateurTribal(AnneauGenerique, PompeAPV, Accelerateur, EquippementTribal):
    """Un anneau pompant les PV et augmentant la vitesse et l'affinité tribale."""

class AnneauRenforceRegenPVAccelerateurTribal(AnneauGenerique, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et l'affinité tribale."""

class AnneauPompeAPMAccelerateurTribal(AnneauGenerique, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau pompant les PM et augmentant la vitesse et l'affinité tribale."""

class AnneauRenforceRegenPMAccelerateurTribal(AnneauGenerique, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et l'affinité tribale."""

class AnneauDefensifPlafondAnoblisseurTribal(AnneauGenerique, DefensifPlafond, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant la priorité et l'affinité tribale."""

class AnneauDefensifProportionAnoblisseurTribal(AnneauGenerique, DefensifProportion, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant la priorité et l'affinité tribale."""

class AnneauDefensifSeuilAnoblisseurTribal(AnneauGenerique, DefensifSeuil, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et l'affinité tribale."""

class AnneauDefensifValeurAnoblisseurTribal(AnneauGenerique, DefensifValeur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la priorité et l'affinité tribale."""

class AnneauPompeAPVAnoblisseurTribal(AnneauGenerique, PompeAPV, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PV et augmentant la priorité et l'affinité tribale."""

class AnneauRenforceRegenPVAnoblisseurTribal(AnneauGenerique, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant la priorité et l'affinité tribale."""

class AnneauPompeAPMAnoblisseurTribal(AnneauGenerique, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PM et augmentant la priorité et l'affinité tribale."""

class AnneauRenforceRegenPMAnoblisseurTribal(AnneauGenerique, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant la priorité et l'affinité tribale."""

class AnneauAccelerateurAnoblisseurTribal(AnneauGenerique, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau augmentant la vitesse et la priorité et l'affinité tribale."""

class AnneauDefensifPlafondElementaireTribal(AnneauGenerique, DefensifPlafond, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant l'affinité élémentaire et tribale."""

class AnneauDefensifProportionElementaireTribal(AnneauGenerique, DefensifProportion, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant l'affinité élémentaire et tribale."""

class AnneauDefensifSeuilElementaireTribal(AnneauGenerique, DefensifSeuil, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité élémentaire et tribale."""

class AnneauDefensifValeurElementaireTribal(AnneauGenerique, DefensifValeur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant l'affinité élémentaire et tribale."""

class AnneauPompeAPVElementaireTribal(AnneauGenerique, PompeAPV, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et augmentant l'affinité élémentaire et tribale."""

class AnneauRenforceRegenPVElementaireTribal(AnneauGenerique, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant l'affinité élémentaire et tribale."""

class AnneauPompeAPMElementaireTribal(AnneauGenerique, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau pompant les PM et augmentant l'affinité élémentaire et tribale."""

class AnneauRenforceRegenPMElementaireTribal(AnneauGenerique, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant l'affinité élémentaire et tribale."""

class AnneauAccelerateurElementaireTribal(AnneauGenerique, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau augmentant la vitesse et l'affinité élémentaire et tribale."""

class AnneauAnoblisseurElementaireTribal(AnneauGenerique, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau augmentant la priorité et l'affinité élémentaire et tribale."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateur(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateur(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateur(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateur(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateur(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateur(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateur(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité."""

class AnneauDefensifProportionPompeAPVPompeAPMAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité."""

class AnneauDefensifValeurPompeAPVPompeAPMAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionPompeAPVAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurPompeAPVAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauPompeAPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPVPompeAPMElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMElementaire(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMElementaire(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMElementaire(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMElementaire(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVAccelerateurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVAccelerateurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVAccelerateurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVAccelerateurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMAccelerateurElementaire(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMAccelerateurElementaire(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMAnoblisseurElementaire(AnneauGenerique, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMAnoblisseurElementaire(AnneauGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVAccelerateurAnoblisseurElementaire(AnneauGenerique, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVAccelerateurAnoblisseurElementaire(AnneauGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVPompeAPMTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVAccelerateurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVAccelerateurTribal(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVAccelerateurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVAccelerateurTribal(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMAccelerateurTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMAccelerateurTribal(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMAccelerateurTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMAccelerateurTribal(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMAccelerateurTribal(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMAccelerateurTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMAnoblisseurTribal(AnneauGenerique, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMAnoblisseurTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVAccelerateurAnoblisseurTribal(AnneauGenerique, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVAccelerateurAnoblisseurTribal(AnneauGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMElementaireTribal(AnneauGenerique, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMElementaireTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMElementaireTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMElementaireTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauPompeAPVAccelerateurElementaireTribal(AnneauGenerique, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVAccelerateurElementaireTribal(AnneauGenerique, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauPompeAPMAccelerateurElementaireTribal(AnneauGenerique, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVAnoblisseurElementaireTribal(AnneauGenerique, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVPompeAPMElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVPompeAPMElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVPompeAPMElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVPompeAPMElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(AnneauGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un anneau défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureGenerique(Armure, EquippementGenerique):
    """Une armure générique, avec les arguments utilisés par toutes les armures."""

class ArmureDefensifPlafond(ArmureGenerique, DefensifPlafond):
    """Une armure défensif plafonnant les dégats."""

class ArmureDefensifProportion(ArmureGenerique, DefensifProportion):
    """Une armure défensif proportionnel aux dégats."""

class ArmureDefensifSeuil(ArmureGenerique, DefensifSeuil):
    """Une armure défensif bloquant les dégats en dessous d'un seuil."""

class ArmureDefensifValeur(ArmureGenerique, DefensifValeur):
    """Une armure défensif bloquant une valeur fixe de dégats."""

class ArmurePompeAPV(ArmureGenerique, PompeAPV):
    """Une armure pompant les PV."""

class ArmureRenforceRegenPV(ArmureGenerique, RenforceRegenPV):
    """Une armure renforçant la régénération des PV."""

class ArmurePompeAPM(ArmureGenerique, PompeAPM):
    """Une armure pompant les PM."""

class ArmureRenforceRegenPM(ArmureGenerique, RenforceRegenPM):
    """Une armure renforçant la régénération des PM."""

class ArmureAccelerateur(ArmureGenerique, Accelerateur):
    """Une armure qui augmente la vitesse."""

class ArmureAnoblisseur(ArmureGenerique, Anoblisseur):
    """Une armure qui augmente la priorité."""

class ArmureElementaire(ArmureGenerique, Elementaire):
    """Une armure qui renforce l'affinité à un élément."""

class ArmureTribal(ArmureGenerique, EquippementTribal):
    """Une armure qui est dédié à une espèce."""

class ArmureDefensifPlafondPompeAPV(ArmureGenerique, DefensifPlafond, PompeAPV):
    """Une armure défensif plafonnant les dégats et pompant les PV."""

class ArmureDefensifPlafondRenforceRegenPV(ArmureGenerique, DefensifPlafond, RenforceRegenPV):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV."""

class ArmureDefensifProportionPompeAPV(ArmureGenerique, DefensifProportion, PompeAPV):
    """Une armure défensif proportionnel aux dégats et pompant les PV."""

class ArmureDefensifProportionRenforceRegenPV(ArmureGenerique, DefensifProportion, RenforceRegenPV):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV."""

class ArmureDefensifSeuilPompeAPV(ArmureGenerique, DefensifSeuil, PompeAPV):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV."""

class ArmureDefensifSeuilRenforceRegenPV(ArmureGenerique, DefensifSeuil, RenforceRegenPV):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV."""

class ArmureDefensifValeurPompeAPV(ArmureGenerique, DefensifValeur, PompeAPV):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV."""

class ArmureDefensifValeurRenforceRegenPV(ArmureGenerique, DefensifValeur, RenforceRegenPV):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV."""

class ArmureDefensifPlafondPompeAPM(ArmureGenerique, DefensifPlafond, PompeAPM):
    """Une armure défensif plafonnant les dégats et pompant les PM."""

class ArmureDefensifPlafondRenforceRegenPM(ArmureGenerique, DefensifPlafond, RenforceRegenPM):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM."""

class ArmureDefensifProportionPompeAPM(ArmureGenerique, DefensifProportion, PompeAPM):
    """Une armure défensif proportionnel aux dégats et pompant les PM."""

class ArmureDefensifProportionRenforceRegenPM(ArmureGenerique, DefensifProportion, RenforceRegenPM):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM."""

class ArmureDefensifSeuilPompeAPM(ArmureGenerique, DefensifSeuil, PompeAPM):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM."""

class ArmureDefensifSeuilRenforceRegenPM(ArmureGenerique, DefensifSeuil, RenforceRegenPM):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM."""

class ArmureDefensifValeurPompeAPM(ArmureGenerique, DefensifValeur, PompeAPM):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM."""

class ArmureDefensifValeurRenforceRegenPM(ArmureGenerique, DefensifValeur, RenforceRegenPM):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM."""

class ArmurePompeAPVPompeAPM(ArmureGenerique, PompeAPV, PompeAPM):
    """Une armure pompant les PV et les PM."""

class ArmurePompeAPVRenforceRegenPM(ArmureGenerique, PompeAPV, RenforceRegenPM):
    """Une armure pompant les PV et renforçant la régénération des PM."""

class ArmureRenforceRegenPVPompeAPM(ArmureGenerique, RenforceRegenPV, PompeAPM):
    """Une armure renforçant la régénération des PV et pompant les PM."""

class ArmureRenforceRegenPVRenforceRegenPM(ArmureGenerique, RenforceRegenPV, RenforceRegenPM):
    """Une armure renforçant la régénération des PV et des PM."""

class ArmureDefensifPlafondAccelerateur(ArmureGenerique, DefensifPlafond, Accelerateur):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse."""

class ArmureDefensifProportionAccelerateur(ArmureGenerique, DefensifProportion, Accelerateur):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse."""

class ArmureDefensifSeuilAccelerateur(ArmureGenerique, DefensifSeuil, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse."""

class ArmureDefensifValeurAccelerateur(ArmureGenerique, DefensifValeur, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse."""

class ArmurePompeAPVAccelerateur(ArmureGenerique, PompeAPV, Accelerateur):
    """Une armure pompant les PV et augmentant la vitesse."""

class ArmureRenforceRegenPVAccelerateur(ArmureGenerique, RenforceRegenPV, Accelerateur):
    """Une armure renforçant la régénération des PV et augmentant la vitesse."""

class ArmurePompeAPMAccelerateur(ArmureGenerique, PompeAPM, Accelerateur):
    """Une armure pompant les PM et augmentant la vitesse."""

class ArmureRenforceRegenPMAccelerateur(ArmureGenerique, RenforceRegenPM, Accelerateur):
    """Une armure renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifPlafondAnoblisseur(ArmureGenerique, DefensifPlafond, Anoblisseur):
    """Une armure défensif plafonnant les dégats et augmentant la priorité."""

class ArmureDefensifProportionAnoblisseur(ArmureGenerique, DefensifProportion, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et augmentant la priorité."""

class ArmureDefensifSeuilAnoblisseur(ArmureGenerique, DefensifSeuil, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité."""

class ArmureDefensifValeurAnoblisseur(ArmureGenerique, DefensifValeur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la priorité."""

class ArmurePompeAPVAnoblisseur(ArmureGenerique, PompeAPV, Anoblisseur):
    """Une armure pompant les PV et augmentant la priorité."""

class ArmureRenforceRegenPVAnoblisseur(ArmureGenerique, RenforceRegenPV, Anoblisseur):
    """Une armure renforçant la régénération des PV et augmentant la priorité."""

class ArmurePompeAPMAnoblisseur(ArmureGenerique, PompeAPM, Anoblisseur):
    """Une armure pompant les PM et augmentant la priorité."""

class ArmureRenforceRegenPMAnoblisseur(ArmureGenerique, RenforceRegenPM, Anoblisseur):
    """Une armure renforçant la régénération des PM et augmentant la priorité."""

class ArmureAccelerateurAnoblisseur(ArmureGenerique, Accelerateur, Anoblisseur):
    """Une armure augmentant la vitesse et la priorité."""

class ArmureDefensifPlafondElementaire(ArmureGenerique, DefensifPlafond, Elementaire):
    """Une armure défensif plafonnant les dégats et augmentant l'affinité à un élément."""

class ArmureDefensifProportionElementaire(ArmureGenerique, DefensifProportion, Elementaire):
    """Une armure défensif proportionnel aux dégats et augmentant l'affinité à un élément."""

class ArmureDefensifSeuilElementaire(ArmureGenerique, DefensifSeuil, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité à un élément."""

class ArmureDefensifValeurElementaire(ArmureGenerique, DefensifValeur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant l'affinité à un élément."""

class ArmurePompeAPVElementaire(ArmureGenerique, PompeAPV, Elementaire):
    """Une armure pompant les PV et augmentant l'affinité à un élément."""

class ArmureRenforceRegenPVElementaire(ArmureGenerique, RenforceRegenPV, Elementaire):
    """Une armure renforçant la régénération des PV et augmentant l'affinité à un élément."""

class ArmurePompeAPMElementaire(ArmureGenerique, PompeAPM, Elementaire):
    """Une armure pompant les PM et augmentant l'affinité à un élément."""

class ArmureRenforceRegenPMElementaire(ArmureGenerique, RenforceRegenPM, Elementaire):
    """Une armure renforçant la régénération des PM et augmentant l'affinité à un élément."""

class ArmureAccelerateurElementaire(ArmureGenerique, Accelerateur, Elementaire):
    """Une armure augmentant la vitesse et l'affinité à un élément."""

class ArmureAnoblisseurElementaire(ArmureGenerique, Anoblisseur, Elementaire):
    """Une armure augmentant la priorité et l'affinité à un élément."""

class ArmureDefensifPlafondTribal(ArmureGenerique, DefensifPlafond, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant l'affinité."""

class ArmureDefensifProportionTribal(ArmureGenerique, DefensifProportion, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant l'affinité."""

class ArmureDefensifSeuilTribal(ArmureGenerique, DefensifSeuil, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité."""

class ArmureDefensifValeurTribal(ArmureGenerique, DefensifValeur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant l'affinité."""

class ArmurePompeAPVTribal(ArmureGenerique, PompeAPV, EquippementTribal):
    """Une armure pompant les PV et augmentant l'affinité."""

class ArmureRenforceRegenPVTribal(ArmureGenerique, RenforceRegenPV, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant l'affinité."""

class ArmurePompeAPMTribal(ArmureGenerique, PompeAPM, EquippementTribal):
    """Une armure pompant les PM et augmentant l'affinité."""

class ArmureRenforceRegenPMTribal(ArmureGenerique, RenforceRegenPM, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant l'affinité."""

class ArmureAccelerateurTribal(ArmureGenerique, Accelerateur, EquippementTribal):
    """Une armure augmentant la vitesse et l'affinité."""

class ArmureAnoblisseurTribal(ArmureGenerique, Anoblisseur, EquippementTribal):
    """Une armure augmentant la priorité et l'affinité."""

class ArmureElementaireTribal(ArmureGenerique, Elementaire, EquippementTribal):
    """Une armure augmentant l'affinité à un élément et l'affinité à une espèce."""

class ArmureDefensifPlafondPompeAPVPompeAPM(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM."""

class ArmureDefensifProportionPompeAPVPompeAPM(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM."""

class ArmureDefensifSeuilPompeAPVPompeAPM(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM."""

class ArmureDefensifValeurPompeAPVPompeAPM(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPM(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM."""

class ArmureDefensifProportionRenforceRegenPVPompeAPM(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPM(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM."""

class ArmureDefensifValeurRenforceRegenPVPompeAPM(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPM(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM."""

class ArmureDefensifProportionPompeAPVRenforceRegenPM(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPM(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM."""

class ArmureDefensifValeurPompeAPVRenforceRegenPM(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPM(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPM(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPM(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPM(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM."""

class ArmureDefensifPlafondPompeAPVAccelerateur(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse."""

class ArmureDefensifProportionPompeAPVAccelerateur(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse."""

class ArmureDefensifSeuilPompeAPVAccelerateur(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse."""

class ArmureDefensifValeurPompeAPVAccelerateur(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse."""

class ArmureDefensifProportionRenforceRegenPVAccelerateur(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse."""

class ArmureDefensifValeurRenforceRegenPVAccelerateur(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse."""

class ArmureDefensifPlafondPompeAPMAccelerateur(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse."""

class ArmureDefensifProportionPompeAPMAccelerateur(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse."""

class ArmureDefensifSeuilPompeAPMAccelerateur(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse."""

class ArmureDefensifValeurPompeAPMAccelerateur(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateur(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifProportionRenforceRegenPMAccelerateur(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateur(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifValeurRenforceRegenPMAccelerateur(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse."""

class ArmurePompeAPVPompeAPMAccelerateur(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur):
    """Une armure pompant les PV et les PM et augmentant la vitesse."""

class ArmureRenforceRegenPVPompeAPMAccelerateur(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class ArmurePompeAPVRenforceRegenPMAccelerateur(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateur(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse."""

class ArmureDefensifPlafondPompeAPVAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPV, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la priorité."""

class ArmureDefensifProportionPompeAPVAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPV, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPVAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPV, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité."""

class ArmureDefensifValeurPompeAPVAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPV, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPVAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPVAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPVAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPVAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPMAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPM, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la priorité."""

class ArmureDefensifProportionPompeAPMAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPM, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPMAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPM, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité."""

class ArmureDefensifValeurPompeAPMAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPM, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité."""

class ArmurePompeAPVPompeAPMAnoblisseur(ArmureGenerique, PompeAPV, PompeAPM, Anoblisseur):
    """Une armure pompant les PV et les PM et augmentant la priorité."""

class ArmureRenforceRegenPVPompeAPMAnoblisseur(ArmureGenerique, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class ArmurePompeAPVRenforceRegenPMAnoblisseur(ArmureGenerique, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class ArmureRenforceRegenPVRenforceRegenPMAnoblisseur(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Une armure renforçant la régénération des PV et des PM et augmentant la priorité."""

class ArmureDefensifPlafondAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et la priorité."""

class ArmureDefensifProportionAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et la priorité."""

class ArmureDefensifSeuilAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et la priorité."""

class ArmureDefensifValeurAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et la priorité."""

class ArmurePompeAPVAccelerateurAnoblisseur(ArmureGenerique, PompeAPV, Accelerateur, Anoblisseur):
    """Une armure pompant les PV et augmentant la vitesse et la priorité."""

class ArmureRenforceRegenPVAccelerateurAnoblisseur(ArmureGenerique, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et la priorité."""

class ArmurePompeAPMAccelerateurAnoblisseur(ArmureGenerique, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure pompant les PM et augmentant la vitesse et la priorité."""

class ArmureRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et la priorité."""

class ArmureDefensifPlafondPompeAPVElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVElementaire(ArmureGenerique, DefensifProportion, PompeAPV, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVElementaire(ArmureGenerique, DefensifValeur, PompeAPV, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMElementaire(ArmureGenerique, DefensifPlafond, PompeAPM, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMElementaire(ArmureGenerique, DefensifProportion, PompeAPM, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMElementaire(ArmureGenerique, DefensifSeuil, PompeAPM, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMElementaire(ArmureGenerique, DefensifValeur, PompeAPM, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPM, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPM, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMElementaire(ArmureGenerique, PompeAPV, PompeAPM, Elementaire):
    """Une armure pompant les PV et les PM et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMElementaire(ArmureGenerique, RenforceRegenPV, PompeAPM, Elementaire):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMElementaire(ArmureGenerique, PompeAPV, RenforceRegenPM, Elementaire):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMElementaire(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Une armure renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondAccelerateurElementaire(ArmureGenerique, DefensifPlafond, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et l'affinité élémentaire."""

class ArmureDefensifProportionAccelerateurElementaire(ArmureGenerique, DefensifProportion, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et l'affinité élémentaire."""

class ArmureDefensifSeuilAccelerateurElementaire(ArmureGenerique, DefensifSeuil, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et l'affinité élémentaire."""

class ArmureDefensifValeurAccelerateurElementaire(ArmureGenerique, DefensifValeur, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et l'affinité élémentaire."""

class ArmurePompeAPVAccelerateurElementaire(ArmureGenerique, PompeAPV, Accelerateur, Elementaire):
    """Une armure pompant les PV et augmentant la vitesse et l'affinité élémentaire."""

class ArmureRenforceRegenPVAccelerateurElementaire(ArmureGenerique, RenforceRegenPV, Accelerateur, Elementaire):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et l'affinité élémentaire."""

class ArmurePompeAPMAccelerateurElementaire(ArmureGenerique, PompeAPM, Accelerateur, Elementaire):
    """Une armure pompant les PM et augmentant la vitesse et l'affinité élémentaire."""

class ArmureRenforceRegenPMAccelerateurElementaire(ArmureGenerique, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et l'affinité élémentaire."""

class ArmureDefensifPlafondAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et augmentant la priorité et l'affinité élémentaire."""

class ArmureDefensifProportionAnoblisseurElementaire(ArmureGenerique, DefensifProportion, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et augmentant la priorité et l'affinité élémentaire."""

class ArmureDefensifSeuilAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et l'affinité élémentaire."""

class ArmureDefensifValeurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la priorité et l'affinité élémentaire."""

class ArmurePompeAPVAnoblisseurElementaire(ArmureGenerique, PompeAPV, Anoblisseur, Elementaire):
    """Une armure pompant les PV et augmentant la priorité et l'affinité élémentaire."""

class ArmureRenforceRegenPVAnoblisseurElementaire(ArmureGenerique, RenforceRegenPV, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PV et augmentant la priorité et l'affinité élémentaire."""

class ArmurePompeAPMAnoblisseurElementaire(ArmureGenerique, PompeAPM, Anoblisseur, Elementaire):
    """Une armure pompant les PM et augmentant la priorité et l'affinité élémentaire."""

class ArmureRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PM et augmentant la priorité et l'affinité élémentaire."""

class ArmureAccelerateurAnoblisseurElementaire(ArmureGenerique, Accelerateur, Anoblisseur, Elementaire):
    """Une armure augmentant la vitesse et la priorité et l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVTribal(ArmureGenerique, DefensifPlafond, PompeAPV, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant l'affinité tribale."""

class ArmureDefensifProportionPompeAPVTribal(ArmureGenerique, DefensifProportion, PompeAPV, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité tribale."""

class ArmureDefensifSeuilPompeAPVTribal(ArmureGenerique, DefensifSeuil, PompeAPV, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité tribale."""

class ArmureDefensifValeurPompeAPVTribal(ArmureGenerique, DefensifValeur, PompeAPV, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité tribale."""

class ArmureDefensifPlafondRenforceRegenPVTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class ArmureDefensifProportionRenforceRegenPVTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class ArmureDefensifSeuilRenforceRegenPVTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité tribale."""

class ArmureDefensifValeurRenforceRegenPVTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class ArmureDefensifPlafondPompeAPMTribal(ArmureGenerique, DefensifPlafond, PompeAPM, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant l'affinité tribale."""

class ArmureDefensifProportionPompeAPMTribal(ArmureGenerique, DefensifProportion, PompeAPM, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité tribale."""

class ArmureDefensifSeuilPompeAPMTribal(ArmureGenerique, DefensifSeuil, PompeAPM, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité tribale."""

class ArmureDefensifValeurPompeAPMTribal(ArmureGenerique, DefensifValeur, PompeAPM, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité tribale."""

class ArmureDefensifPlafondRenforceRegenPMTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class ArmureDefensifProportionRenforceRegenPMTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class ArmureDefensifSeuilRenforceRegenPMTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité tribale."""

class ArmureDefensifValeurRenforceRegenPMTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class ArmurePompeAPVPompeAPMTribal(ArmureGenerique, PompeAPV, PompeAPM, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant l'affinité tribale."""

class ArmureRenforceRegenPVPompeAPMTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant l'affinité tribale."""

class ArmurePompeAPVRenforceRegenPMTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant l'affinité tribale."""

class ArmureRenforceRegenPVRenforceRegenPMTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Une armure renforçant la régénération des PV et des PM et augmentant l'affinité tribale."""

class ArmureDefensifPlafondAccelerateurTribal(ArmureGenerique, DefensifPlafond, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et l'affinité tribale."""

class ArmureDefensifProportionAccelerateurTribal(ArmureGenerique, DefensifProportion, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et l'affinité tribale."""

class ArmureDefensifSeuilAccelerateurTribal(ArmureGenerique, DefensifSeuil, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et l'affinité tribale."""

class ArmureDefensifValeurAccelerateurTribal(ArmureGenerique, DefensifValeur, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et l'affinité tribale."""

class ArmurePompeAPVAccelerateurTribal(ArmureGenerique, PompeAPV, Accelerateur, EquippementTribal):
    """Une armure pompant les PV et augmentant la vitesse et l'affinité tribale."""

class ArmureRenforceRegenPVAccelerateurTribal(ArmureGenerique, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et l'affinité tribale."""

class ArmurePompeAPMAccelerateurTribal(ArmureGenerique, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure pompant les PM et augmentant la vitesse et l'affinité tribale."""

class ArmureRenforceRegenPMAccelerateurTribal(ArmureGenerique, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et l'affinité tribale."""

class ArmureDefensifPlafondAnoblisseurTribal(ArmureGenerique, DefensifPlafond, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant la priorité et l'affinité tribale."""

class ArmureDefensifProportionAnoblisseurTribal(ArmureGenerique, DefensifProportion, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant la priorité et l'affinité tribale."""

class ArmureDefensifSeuilAnoblisseurTribal(ArmureGenerique, DefensifSeuil, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et l'affinité tribale."""

class ArmureDefensifValeurAnoblisseurTribal(ArmureGenerique, DefensifValeur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la priorité et l'affinité tribale."""

class ArmurePompeAPVAnoblisseurTribal(ArmureGenerique, PompeAPV, Anoblisseur, EquippementTribal):
    """Une armure pompant les PV et augmentant la priorité et l'affinité tribale."""

class ArmureRenforceRegenPVAnoblisseurTribal(ArmureGenerique, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant la priorité et l'affinité tribale."""

class ArmurePompeAPMAnoblisseurTribal(ArmureGenerique, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure pompant les PM et augmentant la priorité et l'affinité tribale."""

class ArmureRenforceRegenPMAnoblisseurTribal(ArmureGenerique, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant la priorité et l'affinité tribale."""

class ArmureAccelerateurAnoblisseurTribal(ArmureGenerique, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure augmentant la vitesse et la priorité et l'affinité tribale."""

class ArmureDefensifPlafondElementaireTribal(ArmureGenerique, DefensifPlafond, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant l'affinité élémentaire et tribale."""

class ArmureDefensifProportionElementaireTribal(ArmureGenerique, DefensifProportion, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant l'affinité élémentaire et tribale."""

class ArmureDefensifSeuilElementaireTribal(ArmureGenerique, DefensifSeuil, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité élémentaire et tribale."""

class ArmureDefensifValeurElementaireTribal(ArmureGenerique, DefensifValeur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant l'affinité élémentaire et tribale."""

class ArmurePompeAPVElementaireTribal(ArmureGenerique, PompeAPV, Elementaire, EquippementTribal):
    """Une armure pompant les PV et augmentant l'affinité élémentaire et tribale."""

class ArmureRenforceRegenPVElementaireTribal(ArmureGenerique, RenforceRegenPV, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant l'affinité élémentaire et tribale."""

class ArmurePompeAPMElementaireTribal(ArmureGenerique, PompeAPM, Elementaire, EquippementTribal):
    """Une armure pompant les PM et augmentant l'affinité élémentaire et tribale."""

class ArmureRenforceRegenPMElementaireTribal(ArmureGenerique, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant l'affinité élémentaire et tribale."""

class ArmureAccelerateurElementaireTribal(ArmureGenerique, Accelerateur, Elementaire, EquippementTribal):
    """Une armure augmentant la vitesse et l'affinité élémentaire et tribale."""

class ArmureAnoblisseurElementaireTribal(ArmureGenerique, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure augmentant la priorité et l'affinité élémentaire et tribale."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateur(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateur(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateur(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateur(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateur(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateur(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateur(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité."""

class ArmureDefensifProportionPompeAPVPompeAPMAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité."""

class ArmureDefensifValeurPompeAPVPompeAPMAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionPompeAPVAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurPompeAPVAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmurePompeAPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPVPompeAPMElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMElementaire(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMElementaire(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMElementaire(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMElementaire(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVAccelerateurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVAccelerateurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVAccelerateurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVAccelerateurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMAccelerateurElementaire(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMAccelerateurElementaire(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMAnoblisseurElementaire(ArmureGenerique, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMAnoblisseurElementaire(ArmureGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVAccelerateurAnoblisseurElementaire(ArmureGenerique, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVAccelerateurAnoblisseurElementaire(ArmureGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVPompeAPMTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVAccelerateurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVAccelerateurTribal(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVAccelerateurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVAccelerateurTribal(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMAccelerateurTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMAccelerateurTribal(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMAccelerateurTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMAccelerateurTribal(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMAccelerateurTribal(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMAccelerateurTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPV, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPV, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMAnoblisseurTribal(ArmureGenerique, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMAnoblisseurTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVAccelerateurAnoblisseurTribal(ArmureGenerique, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVAccelerateurAnoblisseurTribal(ArmureGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMElementaireTribal(ArmureGenerique, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMElementaireTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMElementaireTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMElementaireTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmurePompeAPVAccelerateurElementaireTribal(ArmureGenerique, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVAccelerateurElementaireTribal(ArmureGenerique, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmurePompeAPMAccelerateurElementaireTribal(ArmureGenerique, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVAnoblisseurElementaireTribal(ArmureGenerique, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPMAnoblisseurElementaireTribal(ArmureGenerique, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVPompeAPMElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVPompeAPMElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVPompeAPMElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVPompeAPMElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmurePompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmurePompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(ArmureGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Une armure défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeGenerique(Heaume, EquippementGenerique):
    """Un heaume générique, avec les arguments utilisés par tous les heaumes."""

class HeaumeDefensifPlafond(HeaumeGenerique, DefensifPlafond):
    """Un heaume défensif plafonnant les dégats."""

class HeaumeDefensifProportion(HeaumeGenerique, DefensifProportion):
    """Un heaume défensif proportionnel aux dégats."""

class HeaumeDefensifSeuil(HeaumeGenerique, DefensifSeuil):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil."""

class HeaumeDefensifValeur(HeaumeGenerique, DefensifValeur):
    """Un heaume défensif bloquant une valeur fixe de dégats."""

class HeaumePompeAPV(HeaumeGenerique, PompeAPV):
    """Un heaume pompant les PV."""

class HeaumeRenforceRegenPV(HeaumeGenerique, RenforceRegenPV):
    """Un heaume renforçant la régénération des PV."""

class HeaumePompeAPM(HeaumeGenerique, PompeAPM):
    """Un heaume pompant les PM."""

class HeaumeRenforceRegenPM(HeaumeGenerique, RenforceRegenPM):
    """Un heaume renforçant la régénération des PM."""

class HeaumeAccelerateur(HeaumeGenerique, Accelerateur):
    """Un heaume qui augmente la vitesse."""

class HeaumeAnoblisseur(HeaumeGenerique, Anoblisseur):
    """Un heaume qui augmente la priorité."""

class HeaumeElementaire(HeaumeGenerique, Elementaire):
    """Un heaume qui renforce l'affinité à un élément."""

class HeaumeTribal(HeaumeGenerique, EquippementTribal):
    """Un heaume qui est dédié à une espèce."""

class HeaumeDefensifPlafondPompeAPV(HeaumeGenerique, DefensifPlafond, PompeAPV):
    """Un heaume défensif plafonnant les dégats et pompant les PV."""

class HeaumeDefensifPlafondRenforceRegenPV(HeaumeGenerique, DefensifPlafond, RenforceRegenPV):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV."""

class HeaumeDefensifProportionPompeAPV(HeaumeGenerique, DefensifProportion, PompeAPV):
    """Un heaume défensif proportionnel aux dégats et pompant les PV."""

class HeaumeDefensifProportionRenforceRegenPV(HeaumeGenerique, DefensifProportion, RenforceRegenPV):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV."""

class HeaumeDefensifSeuilPompeAPV(HeaumeGenerique, DefensifSeuil, PompeAPV):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV."""

class HeaumeDefensifSeuilRenforceRegenPV(HeaumeGenerique, DefensifSeuil, RenforceRegenPV):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV."""

class HeaumeDefensifValeurPompeAPV(HeaumeGenerique, DefensifValeur, PompeAPV):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV."""

class HeaumeDefensifValeurRenforceRegenPV(HeaumeGenerique, DefensifValeur, RenforceRegenPV):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV."""

class HeaumeDefensifPlafondPompeAPM(HeaumeGenerique, DefensifPlafond, PompeAPM):
    """Un heaume défensif plafonnant les dégats et pompant les PM."""

class HeaumeDefensifPlafondRenforceRegenPM(HeaumeGenerique, DefensifPlafond, RenforceRegenPM):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM."""

class HeaumeDefensifProportionPompeAPM(HeaumeGenerique, DefensifProportion, PompeAPM):
    """Un heaume défensif proportionnel aux dégats et pompant les PM."""

class HeaumeDefensifProportionRenforceRegenPM(HeaumeGenerique, DefensifProportion, RenforceRegenPM):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM."""

class HeaumeDefensifSeuilPompeAPM(HeaumeGenerique, DefensifSeuil, PompeAPM):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM."""

class HeaumeDefensifSeuilRenforceRegenPM(HeaumeGenerique, DefensifSeuil, RenforceRegenPM):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM."""

class HeaumeDefensifValeurPompeAPM(HeaumeGenerique, DefensifValeur, PompeAPM):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM."""

class HeaumeDefensifValeurRenforceRegenPM(HeaumeGenerique, DefensifValeur, RenforceRegenPM):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM."""

class HeaumePompeAPVPompeAPM(HeaumeGenerique, PompeAPV, PompeAPM):
    """Un heaume pompant les PV et les PM."""

class HeaumePompeAPVRenforceRegenPM(HeaumeGenerique, PompeAPV, RenforceRegenPM):
    """Un heaume pompant les PV et renforçant la régénération des PM."""

class HeaumeRenforceRegenPVPompeAPM(HeaumeGenerique, RenforceRegenPV, PompeAPM):
    """Un heaume renforçant la régénération des PV et pompant les PM."""

class HeaumeRenforceRegenPVRenforceRegenPM(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM):
    """Un heaume renforçant la régénération des PV et des PM."""

class HeaumeDefensifPlafondAccelerateur(HeaumeGenerique, DefensifPlafond, Accelerateur):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse."""

class HeaumeDefensifProportionAccelerateur(HeaumeGenerique, DefensifProportion, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse."""

class HeaumeDefensifSeuilAccelerateur(HeaumeGenerique, DefensifSeuil, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse."""

class HeaumeDefensifValeurAccelerateur(HeaumeGenerique, DefensifValeur, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse."""

class HeaumePompeAPVAccelerateur(HeaumeGenerique, PompeAPV, Accelerateur):
    """Un heaume pompant les PV et augmentant la vitesse."""

class HeaumeRenforceRegenPVAccelerateur(HeaumeGenerique, RenforceRegenPV, Accelerateur):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse."""

class HeaumePompeAPMAccelerateur(HeaumeGenerique, PompeAPM, Accelerateur):
    """Un heaume pompant les PM et augmentant la vitesse."""

class HeaumeRenforceRegenPMAccelerateur(HeaumeGenerique, RenforceRegenPM, Accelerateur):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifPlafondAnoblisseur(HeaumeGenerique, DefensifPlafond, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et augmentant la priorité."""

class HeaumeDefensifProportionAnoblisseur(HeaumeGenerique, DefensifProportion, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et augmentant la priorité."""

class HeaumeDefensifSeuilAnoblisseur(HeaumeGenerique, DefensifSeuil, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité."""

class HeaumeDefensifValeurAnoblisseur(HeaumeGenerique, DefensifValeur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la priorité."""

class HeaumePompeAPVAnoblisseur(HeaumeGenerique, PompeAPV, Anoblisseur):
    """Un heaume pompant les PV et augmentant la priorité."""

class HeaumeRenforceRegenPVAnoblisseur(HeaumeGenerique, RenforceRegenPV, Anoblisseur):
    """Un heaume renforçant la régénération des PV et augmentant la priorité."""

class HeaumePompeAPMAnoblisseur(HeaumeGenerique, PompeAPM, Anoblisseur):
    """Un heaume pompant les PM et augmentant la priorité."""

class HeaumeRenforceRegenPMAnoblisseur(HeaumeGenerique, RenforceRegenPM, Anoblisseur):
    """Un heaume renforçant la régénération des PM et augmentant la priorité."""

class HeaumeAccelerateurAnoblisseur(HeaumeGenerique, Accelerateur, Anoblisseur):
    """Un heaume augmentant la vitesse et la priorité."""

class HeaumeDefensifPlafondElementaire(HeaumeGenerique, DefensifPlafond, Elementaire):
    """Un heaume défensif plafonnant les dégats et augmentant l'affinité à un élément."""

class HeaumeDefensifProportionElementaire(HeaumeGenerique, DefensifProportion, Elementaire):
    """Un heaume défensif proportionnel aux dégats et augmentant l'affinité à un élément."""

class HeaumeDefensifSeuilElementaire(HeaumeGenerique, DefensifSeuil, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité à un élément."""

class HeaumeDefensifValeurElementaire(HeaumeGenerique, DefensifValeur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant l'affinité à un élément."""

class HeaumePompeAPVElementaire(HeaumeGenerique, PompeAPV, Elementaire):
    """Un heaume pompant les PV et augmentant l'affinité à un élément."""

class HeaumeRenforceRegenPVElementaire(HeaumeGenerique, RenforceRegenPV, Elementaire):
    """Un heaume renforçant la régénération des PV et augmentant l'affinité à un élément."""

class HeaumePompeAPMElementaire(HeaumeGenerique, PompeAPM, Elementaire):
    """Un heaume pompant les PM et augmentant l'affinité à un élément."""

class HeaumeRenforceRegenPMElementaire(HeaumeGenerique, RenforceRegenPM, Elementaire):
    """Un heaume renforçant la régénération des PM et augmentant l'affinité à un élément."""

class HeaumeAccelerateurElementaire(HeaumeGenerique, Accelerateur, Elementaire):
    """Un heaume augmentant la vitesse et l'affinité à un élément."""

class HeaumeAnoblisseurElementaire(HeaumeGenerique, Anoblisseur, Elementaire):
    """Un heaume augmentant la priorité et l'affinité à un élément."""

class HeaumeDefensifPlafondTribal(HeaumeGenerique, DefensifPlafond, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant l'affinité."""

class HeaumeDefensifProportionTribal(HeaumeGenerique, DefensifProportion, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant l'affinité."""

class HeaumeDefensifSeuilTribal(HeaumeGenerique, DefensifSeuil, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité."""

class HeaumeDefensifValeurTribal(HeaumeGenerique, DefensifValeur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant l'affinité."""

class HeaumePompeAPVTribal(HeaumeGenerique, PompeAPV, EquippementTribal):
    """Un heaume pompant les PV et augmentant l'affinité."""

class HeaumeRenforceRegenPVTribal(HeaumeGenerique, RenforceRegenPV, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant l'affinité."""

class HeaumePompeAPMTribal(HeaumeGenerique, PompeAPM, EquippementTribal):
    """Un heaume pompant les PM et augmentant l'affinité."""

class HeaumeRenforceRegenPMTribal(HeaumeGenerique, RenforceRegenPM, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant l'affinité."""

class HeaumeAccelerateurTribal(HeaumeGenerique, Accelerateur, EquippementTribal):
    """Un heaume augmentant la vitesse et l'affinité."""

class HeaumeAnoblisseurTribal(HeaumeGenerique, Anoblisseur, EquippementTribal):
    """Un heaume augmentant la priorité et l'affinité."""

class HeaumeElementaireTribal(HeaumeGenerique, Elementaire, EquippementTribal):
    """Un heaume augmentant l'affinité à un élément et l'affinité à une espèce."""

class HeaumeDefensifPlafondPompeAPVPompeAPM(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM."""

class HeaumeDefensifProportionPompeAPVPompeAPM(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM."""

class HeaumeDefensifSeuilPompeAPVPompeAPM(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM."""

class HeaumeDefensifValeurPompeAPVPompeAPM(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPM(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPM(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPM(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPM(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPM(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPM(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPM(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPM(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPM(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPM(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPM(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPM(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM."""

class HeaumeDefensifPlafondPompeAPVAccelerateur(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse."""

class HeaumeDefensifProportionPompeAPVAccelerateur(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse."""

class HeaumeDefensifSeuilPompeAPVAccelerateur(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse."""

class HeaumeDefensifValeurPompeAPVAccelerateur(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse."""

class HeaumeDefensifPlafondPompeAPMAccelerateur(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifProportionPompeAPMAccelerateur(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifSeuilPompeAPMAccelerateur(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifValeurPompeAPMAccelerateur(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumePompeAPVPompeAPMAccelerateur(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur):
    """Un heaume pompant les PV et les PM et augmentant la vitesse."""

class HeaumeRenforceRegenPVPompeAPMAccelerateur(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class HeaumePompeAPVRenforceRegenPMAccelerateur(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateur(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse."""

class HeaumeDefensifPlafondPompeAPVAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPV, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPVAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPV, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPVAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPV, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPVAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPV, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPVAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPVAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPVAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPVAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPMAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPM, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPMAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPM, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPMAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPM, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPMAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPM, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité."""

class HeaumePompeAPVPompeAPMAnoblisseur(HeaumeGenerique, PompeAPV, PompeAPM, Anoblisseur):
    """Un heaume pompant les PV et les PM et augmentant la priorité."""

class HeaumeRenforceRegenPVPompeAPMAnoblisseur(HeaumeGenerique, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class HeaumePompeAPVRenforceRegenPMAnoblisseur(HeaumeGenerique, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeRenforceRegenPVRenforceRegenPMAnoblisseur(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la priorité."""

class HeaumeDefensifPlafondAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et la priorité."""

class HeaumeDefensifProportionAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et la priorité."""

class HeaumeDefensifSeuilAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et la priorité."""

class HeaumeDefensifValeurAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et la priorité."""

class HeaumePompeAPVAccelerateurAnoblisseur(HeaumeGenerique, PompeAPV, Accelerateur, Anoblisseur):
    """Un heaume pompant les PV et augmentant la vitesse et la priorité."""

class HeaumeRenforceRegenPVAccelerateurAnoblisseur(HeaumeGenerique, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et la priorité."""

class HeaumePompeAPMAccelerateurAnoblisseur(HeaumeGenerique, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume pompant les PM et augmentant la vitesse et la priorité."""

class HeaumeRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et la priorité."""

class HeaumeDefensifPlafondPompeAPVElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMElementaire(HeaumeGenerique, DefensifPlafond, PompeAPM, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMElementaire(HeaumeGenerique, DefensifProportion, PompeAPM, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMElementaire(HeaumeGenerique, DefensifSeuil, PompeAPM, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMElementaire(HeaumeGenerique, DefensifValeur, PompeAPM, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMElementaire(HeaumeGenerique, PompeAPV, PompeAPM, Elementaire):
    """Un heaume pompant les PV et les PM et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMElementaire(HeaumeGenerique, RenforceRegenPV, PompeAPM, Elementaire):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMElementaire(HeaumeGenerique, PompeAPV, RenforceRegenPM, Elementaire):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMElementaire(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un heaume renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et l'affinité élémentaire."""

class HeaumeDefensifProportionAccelerateurElementaire(HeaumeGenerique, DefensifProportion, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et l'affinité élémentaire."""

class HeaumeDefensifSeuilAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et l'affinité élémentaire."""

class HeaumeDefensifValeurAccelerateurElementaire(HeaumeGenerique, DefensifValeur, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et l'affinité élémentaire."""

class HeaumePompeAPVAccelerateurElementaire(HeaumeGenerique, PompeAPV, Accelerateur, Elementaire):
    """Un heaume pompant les PV et augmentant la vitesse et l'affinité élémentaire."""

class HeaumeRenforceRegenPVAccelerateurElementaire(HeaumeGenerique, RenforceRegenPV, Accelerateur, Elementaire):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et l'affinité élémentaire."""

class HeaumePompeAPMAccelerateurElementaire(HeaumeGenerique, PompeAPM, Accelerateur, Elementaire):
    """Un heaume pompant les PM et augmentant la vitesse et l'affinité élémentaire."""

class HeaumeRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et l'affinité élémentaire."""

class HeaumeDefensifPlafondAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et augmentant la priorité et l'affinité élémentaire."""

class HeaumeDefensifProportionAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et augmentant la priorité et l'affinité élémentaire."""

class HeaumeDefensifSeuilAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et l'affinité élémentaire."""

class HeaumeDefensifValeurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la priorité et l'affinité élémentaire."""

class HeaumePompeAPVAnoblisseurElementaire(HeaumeGenerique, PompeAPV, Anoblisseur, Elementaire):
    """Un heaume pompant les PV et augmentant la priorité et l'affinité élémentaire."""

class HeaumeRenforceRegenPVAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PV et augmentant la priorité et l'affinité élémentaire."""

class HeaumePompeAPMAnoblisseurElementaire(HeaumeGenerique, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume pompant les PM et augmentant la priorité et l'affinité élémentaire."""

class HeaumeRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PM et augmentant la priorité et l'affinité élémentaire."""

class HeaumeAccelerateurAnoblisseurElementaire(HeaumeGenerique, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume augmentant la vitesse et la priorité et l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant l'affinité tribale."""

class HeaumeDefensifProportionPompeAPVTribal(HeaumeGenerique, DefensifProportion, PompeAPV, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité tribale."""

class HeaumeDefensifSeuilPompeAPVTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité tribale."""

class HeaumeDefensifValeurPompeAPVTribal(HeaumeGenerique, DefensifValeur, PompeAPV, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class HeaumeDefensifProportionRenforceRegenPVTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité tribale."""

class HeaumeDefensifValeurRenforceRegenPVTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité tribale."""

class HeaumeDefensifPlafondPompeAPMTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant l'affinité tribale."""

class HeaumeDefensifProportionPompeAPMTribal(HeaumeGenerique, DefensifProportion, PompeAPM, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité tribale."""

class HeaumeDefensifSeuilPompeAPMTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité tribale."""

class HeaumeDefensifValeurPompeAPMTribal(HeaumeGenerique, DefensifValeur, PompeAPM, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité tribale."""

class HeaumeDefensifPlafondRenforceRegenPMTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class HeaumeDefensifProportionRenforceRegenPMTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class HeaumeDefensifSeuilRenforceRegenPMTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité tribale."""

class HeaumeDefensifValeurRenforceRegenPMTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité tribale."""

class HeaumePompeAPVPompeAPMTribal(HeaumeGenerique, PompeAPV, PompeAPM, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant l'affinité tribale."""

class HeaumeRenforceRegenPVPompeAPMTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant l'affinité tribale."""

class HeaumePompeAPVRenforceRegenPMTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant l'affinité tribale."""

class HeaumeRenforceRegenPVRenforceRegenPMTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un heaume renforçant la régénération des PV et des PM et augmentant l'affinité tribale."""

class HeaumeDefensifPlafondAccelerateurTribal(HeaumeGenerique, DefensifPlafond, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et l'affinité tribale."""

class HeaumeDefensifProportionAccelerateurTribal(HeaumeGenerique, DefensifProportion, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et l'affinité tribale."""

class HeaumeDefensifSeuilAccelerateurTribal(HeaumeGenerique, DefensifSeuil, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et l'affinité tribale."""

class HeaumeDefensifValeurAccelerateurTribal(HeaumeGenerique, DefensifValeur, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et l'affinité tribale."""

class HeaumePompeAPVAccelerateurTribal(HeaumeGenerique, PompeAPV, Accelerateur, EquippementTribal):
    """Un heaume pompant les PV et augmentant la vitesse et l'affinité tribale."""

class HeaumeRenforceRegenPVAccelerateurTribal(HeaumeGenerique, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et l'affinité tribale."""

class HeaumePompeAPMAccelerateurTribal(HeaumeGenerique, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume pompant les PM et augmentant la vitesse et l'affinité tribale."""

class HeaumeRenforceRegenPMAccelerateurTribal(HeaumeGenerique, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et l'affinité tribale."""

class HeaumeDefensifPlafondAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant la priorité et l'affinité tribale."""

class HeaumeDefensifProportionAnoblisseurTribal(HeaumeGenerique, DefensifProportion, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant la priorité et l'affinité tribale."""

class HeaumeDefensifSeuilAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et l'affinité tribale."""

class HeaumeDefensifValeurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la priorité et l'affinité tribale."""

class HeaumePompeAPVAnoblisseurTribal(HeaumeGenerique, PompeAPV, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PV et augmentant la priorité et l'affinité tribale."""

class HeaumeRenforceRegenPVAnoblisseurTribal(HeaumeGenerique, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant la priorité et l'affinité tribale."""

class HeaumePompeAPMAnoblisseurTribal(HeaumeGenerique, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PM et augmentant la priorité et l'affinité tribale."""

class HeaumeRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant la priorité et l'affinité tribale."""

class HeaumeAccelerateurAnoblisseurTribal(HeaumeGenerique, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume augmentant la vitesse et la priorité et l'affinité tribale."""

class HeaumeDefensifPlafondElementaireTribal(HeaumeGenerique, DefensifPlafond, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant l'affinité élémentaire et tribale."""

class HeaumeDefensifProportionElementaireTribal(HeaumeGenerique, DefensifProportion, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant l'affinité élémentaire et tribale."""

class HeaumeDefensifSeuilElementaireTribal(HeaumeGenerique, DefensifSeuil, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant l'affinité élémentaire et tribale."""

class HeaumeDefensifValeurElementaireTribal(HeaumeGenerique, DefensifValeur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant l'affinité élémentaire et tribale."""

class HeaumePompeAPVElementaireTribal(HeaumeGenerique, PompeAPV, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et augmentant l'affinité élémentaire et tribale."""

class HeaumeRenforceRegenPVElementaireTribal(HeaumeGenerique, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant l'affinité élémentaire et tribale."""

class HeaumePompeAPMElementaireTribal(HeaumeGenerique, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume pompant les PM et augmentant l'affinité élémentaire et tribale."""

class HeaumeRenforceRegenPMElementaireTribal(HeaumeGenerique, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant l'affinité élémentaire et tribale."""

class HeaumeAccelerateurElementaireTribal(HeaumeGenerique, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume augmentant la vitesse et l'affinité élémentaire et tribale."""

class HeaumeAnoblisseurElementaireTribal(HeaumeGenerique, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume augmentant la priorité et l'affinité élémentaire et tribale."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateur(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateur(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateur(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateur(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumePompeAPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPVPompeAPMElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVAccelerateurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVAccelerateurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMAccelerateurElementaire(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurElementaire(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVPompeAPMTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVAccelerateurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVAccelerateurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVAccelerateurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVAccelerateurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMAccelerateurTribal(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMAnoblisseurTribal(HeaumeGenerique, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMAnoblisseurTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVAccelerateurAnoblisseurTribal(HeaumeGenerique, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVAccelerateurAnoblisseurTribal(HeaumeGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMElementaireTribal(HeaumeGenerique, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMElementaireTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMElementaireTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMElementaireTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et renforçant la régénération des PM et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumePompeAPVAccelerateurElementaireTribal(HeaumeGenerique, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVAccelerateurElementaireTribal(HeaumeGenerique, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumePompeAPMAccelerateurElementaireTribal(HeaumeGenerique, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumePompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant l'affinité élémentaire et augmentant la priorité tribale."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumePompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, PompeAPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et pompant les PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, PompeAPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et pompant les PV et renforçant la régénération des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifPlafond, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif plafonnant les dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifProportion, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif proportionnel aux dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifSeuil, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant les dégats en dessous d'un seuil et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

class HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal(HeaumeGenerique, DefensifValeur, RenforceRegenPV, RenforceRegenPM, Accelerateur, Anoblisseur, Elementaire, EquippementTribal):
    """Un heaume défensif bloquant une valeur fixe de dégats et renforçant la régénération des PV et des PM et augmentant la vitesse et augmentant la priorité tribale et augmentant l'affinité élémentaire."""

equippements: dict[tuple[str, str, str, str, bool, bool, bool, bool], type[EquippementGenerique]] = {
    ("Anneau", "non", "non", "non", False, False, False, False): AnneauGenerique,
    ("Armure", "non", "non", "non", False, False, False, False): ArmureGenerique,
    ("Heaume", "non", "non", "non", False, False, False, False): HeaumeGenerique,
    ("Anneau", "Plafond", "non", "non", False, False, False, False): AnneauDefensifPlafond,
    ("Armure", "Plafond", "non", "non", False, False, False, False): ArmureDefensifPlafond,
    ("Heaume", "Plafond", "non", "non", False, False, False, False): HeaumeDefensifPlafond,
    ("Anneau", "Proportion", "non", "non", False, False, False, False): AnneauDefensifProportion,
    ("Armure", "Proportion", "non", "non", False, False, False, False): ArmureDefensifProportion,
    ("Heaume", "Proportion", "non", "non", False, False, False, False): HeaumeDefensifProportion,
    ("Anneau", "Seuil", "non", "non", False, False, False, False): AnneauDefensifSeuil,
    ("Armure", "Seuil", "non", "non", False, False, False, False): ArmureDefensifSeuil,
    ("Heaume", "Seuil", "non", "non", False, False, False, False): HeaumeDefensifSeuil,
    ("Anneau", "Valeur", "non", "non", False, False, False, False): AnneauDefensifValeur,
    ("Armure", "Valeur", "non", "non", False, False, False, False): ArmureDefensifValeur,
    ("Heaume", "Valeur", "non", "non", False, False, False, False): HeaumeDefensifValeur,
    ("Anneau", "non", "PompeAPV", "non", False, False, False, False): AnneauPompeAPV,
    ("Armure", "non", "PompeAPV", "non", False, False, False, False): ArmurePompeAPV,
    ("Heaume", "non", "PompeAPV", "non", False, False, False, False): HeaumePompeAPV,
    ("Anneau", "Plafond", "PompeAPV", "non", False, False, False, False): AnneauDefensifPlafondPompeAPV,
    ("Armure", "Plafond", "PompeAPV", "non", False, False, False, False): ArmureDefensifPlafondPompeAPV,
    ("Heaume", "Plafond", "PompeAPV", "non", False, False, False, False): HeaumeDefensifPlafondPompeAPV,
    ("Anneau", "Proportion", "PompeAPV", "non", False, False, False, False): AnneauDefensifProportionPompeAPV,
    ("Armure", "Proportion", "PompeAPV", "non", False, False, False, False): ArmureDefensifProportionPompeAPV,
    ("Heaume", "Proportion", "PompeAPV", "non", False, False, False, False): HeaumeDefensifProportionPompeAPV,
    ("Anneau", "Seuil", "PompeAPV", "non", False, False, False, False): AnneauDefensifSeuilPompeAPV,
    ("Armure", "Seuil", "PompeAPV", "non", False, False, False, False): ArmureDefensifSeuilPompeAPV,
    ("Heaume", "Seuil", "PompeAPV", "non", False, False, False, False): HeaumeDefensifSeuilPompeAPV,
    ("Anneau", "Valeur", "PompeAPV", "non", False, False, False, False): AnneauDefensifValeurPompeAPV,
    ("Armure", "Valeur", "PompeAPV", "non", False, False, False, False): ArmureDefensifValeurPompeAPV,
    ("Heaume", "Valeur", "PompeAPV", "non", False, False, False, False): HeaumeDefensifValeurPompeAPV,
    ("Anneau", "non", "RenforceRegenPV", "non", False, False, False, False): AnneauRenforceRegenPV,
    ("Armure", "non", "RenforceRegenPV", "non", False, False, False, False): ArmureRenforceRegenPV,
    ("Heaume", "non", "RenforceRegenPV", "non", False, False, False, False): HeaumeRenforceRegenPV,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, False, False, False): AnneauDefensifPlafondRenforceRegenPV,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, False, False, False): ArmureDefensifPlafondRenforceRegenPV,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, False, False, False): HeaumeDefensifPlafondRenforceRegenPV,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, False, False, False): AnneauDefensifProportionRenforceRegenPV,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, False, False, False): ArmureDefensifProportionRenforceRegenPV,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, False, False, False): HeaumeDefensifProportionRenforceRegenPV,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, False, False, False): AnneauDefensifSeuilRenforceRegenPV,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, False, False, False): ArmureDefensifSeuilRenforceRegenPV,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, False, False, False): HeaumeDefensifSeuilRenforceRegenPV,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, False, False, False): AnneauDefensifValeurRenforceRegenPV,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, False, False, False): ArmureDefensifValeurRenforceRegenPV,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, False, False, False): HeaumeDefensifValeurRenforceRegenPV,
    ("Anneau", "non", "non", "PompeAPM", False, False, False, False): AnneauPompeAPM,
    ("Armure", "non", "non", "PompeAPM", False, False, False, False): ArmurePompeAPM,
    ("Heaume", "non", "non", "PompeAPM", False, False, False, False): HeaumePompeAPM,
    ("Anneau", "Plafond", "non", "PompeAPM", False, False, False, False): AnneauDefensifPlafondPompeAPM,
    ("Armure", "Plafond", "non", "PompeAPM", False, False, False, False): ArmureDefensifPlafondPompeAPM,
    ("Heaume", "Plafond", "non", "PompeAPM", False, False, False, False): HeaumeDefensifPlafondPompeAPM,
    ("Anneau", "Proportion", "non", "PompeAPM", False, False, False, False): AnneauDefensifProportionPompeAPM,
    ("Armure", "Proportion", "non", "PompeAPM", False, False, False, False): ArmureDefensifProportionPompeAPM,
    ("Heaume", "Proportion", "non", "PompeAPM", False, False, False, False): HeaumeDefensifProportionPompeAPM,
    ("Anneau", "Seuil", "non", "PompeAPM", False, False, False, False): AnneauDefensifSeuilPompeAPM,
    ("Armure", "Seuil", "non", "PompeAPM", False, False, False, False): ArmureDefensifSeuilPompeAPM,
    ("Heaume", "Seuil", "non", "PompeAPM", False, False, False, False): HeaumeDefensifSeuilPompeAPM,
    ("Anneau", "Valeur", "non", "PompeAPM", False, False, False, False): AnneauDefensifValeurPompeAPM,
    ("Armure", "Valeur", "non", "PompeAPM", False, False, False, False): ArmureDefensifValeurPompeAPM,
    ("Heaume", "Valeur", "non", "PompeAPM", False, False, False, False): HeaumeDefensifValeurPompeAPM,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, False, False, False): AnneauPompeAPVPompeAPM,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, False, False, False): ArmurePompeAPVPompeAPM,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, False, False, False): HeaumePompeAPVPompeAPM,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, False, False, False): AnneauDefensifPlafondPompeAPVPompeAPM,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, False, False, False): ArmureDefensifPlafondPompeAPVPompeAPM,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, False, False, False): HeaumeDefensifPlafondPompeAPVPompeAPM,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, False, False, False): AnneauDefensifProportionPompeAPVPompeAPM,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, False, False, False): ArmureDefensifProportionPompeAPVPompeAPM,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, False, False, False): HeaumeDefensifProportionPompeAPVPompeAPM,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, False, False, False): AnneauDefensifSeuilPompeAPVPompeAPM,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, False, False, False): ArmureDefensifSeuilPompeAPVPompeAPM,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, False, False, False): HeaumeDefensifSeuilPompeAPVPompeAPM,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, False, False, False): AnneauDefensifValeurPompeAPVPompeAPM,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, False, False, False): ArmureDefensifValeurPompeAPVPompeAPM,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, False, False, False): HeaumeDefensifValeurPompeAPVPompeAPM,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, False, False, False): AnneauRenforceRegenPVPompeAPM,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, False, False, False): ArmureRenforceRegenPVPompeAPM,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, False, False, False): HeaumeRenforceRegenPVPompeAPM,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, False, False): AnneauDefensifPlafondRenforceRegenPVPompeAPM,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, False, False): ArmureDefensifPlafondRenforceRegenPVPompeAPM,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, False, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPM,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, False, False): AnneauDefensifProportionRenforceRegenPVPompeAPM,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, False, False): ArmureDefensifProportionRenforceRegenPVPompeAPM,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, False, False): HeaumeDefensifProportionRenforceRegenPVPompeAPM,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, False, False): AnneauDefensifSeuilRenforceRegenPVPompeAPM,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, False, False): ArmureDefensifSeuilRenforceRegenPVPompeAPM,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, False, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPM,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, False, False): AnneauDefensifValeurRenforceRegenPVPompeAPM,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, False, False): ArmureDefensifValeurRenforceRegenPVPompeAPM,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, False, False): HeaumeDefensifValeurRenforceRegenPVPompeAPM,
    ("Anneau", "non", "non", "RenforceRegenPM", False, False, False, False): AnneauRenforceRegenPM,
    ("Armure", "non", "non", "RenforceRegenPM", False, False, False, False): ArmureRenforceRegenPM,
    ("Heaume", "non", "non", "RenforceRegenPM", False, False, False, False): HeaumeRenforceRegenPM,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, False, False, False): AnneauDefensifPlafondRenforceRegenPM,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, False, False, False): ArmureDefensifPlafondRenforceRegenPM,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, False, False, False): HeaumeDefensifPlafondRenforceRegenPM,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, False, False, False): AnneauDefensifProportionRenforceRegenPM,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, False, False, False): ArmureDefensifProportionRenforceRegenPM,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, False, False, False): HeaumeDefensifProportionRenforceRegenPM,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, False, False, False): AnneauDefensifSeuilRenforceRegenPM,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, False, False, False): ArmureDefensifSeuilRenforceRegenPM,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, False, False, False): HeaumeDefensifSeuilRenforceRegenPM,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, False, False, False): AnneauDefensifValeurRenforceRegenPM,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, False, False, False): ArmureDefensifValeurRenforceRegenPM,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, False, False, False): HeaumeDefensifValeurRenforceRegenPM,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, False, False, False): AnneauPompeAPVRenforceRegenPM,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, False, False, False): ArmurePompeAPVRenforceRegenPM,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, False, False, False): HeaumePompeAPVRenforceRegenPM,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifPlafondPompeAPVRenforceRegenPM,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifPlafondPompeAPVRenforceRegenPM,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPM,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifProportionPompeAPVRenforceRegenPM,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifProportionPompeAPVRenforceRegenPM,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifProportionPompeAPVRenforceRegenPM,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifSeuilPompeAPVRenforceRegenPM,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifSeuilPompeAPVRenforceRegenPM,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPM,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifValeurPompeAPVRenforceRegenPM,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifValeurPompeAPVRenforceRegenPM,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifValeurPompeAPVRenforceRegenPM,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): AnneauRenforceRegenPVRenforceRegenPM,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): ArmureRenforceRegenPVRenforceRegenPM,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): HeaumeRenforceRegenPVRenforceRegenPM,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPM,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPM,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPM,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPM,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPM,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPM,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPM,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPM,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPM,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPM,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPM,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, False, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPM,
    ("Anneau", "non", "non", "non", True, False, False, False): AnneauAccelerateur,
    ("Armure", "non", "non", "non", True, False, False, False): ArmureAccelerateur,
    ("Heaume", "non", "non", "non", True, False, False, False): HeaumeAccelerateur,
    ("Anneau", "Plafond", "non", "non", True, False, False, False): AnneauDefensifPlafondAccelerateur,
    ("Armure", "Plafond", "non", "non", True, False, False, False): ArmureDefensifPlafondAccelerateur,
    ("Heaume", "Plafond", "non", "non", True, False, False, False): HeaumeDefensifPlafondAccelerateur,
    ("Anneau", "Proportion", "non", "non", True, False, False, False): AnneauDefensifProportionAccelerateur,
    ("Armure", "Proportion", "non", "non", True, False, False, False): ArmureDefensifProportionAccelerateur,
    ("Heaume", "Proportion", "non", "non", True, False, False, False): HeaumeDefensifProportionAccelerateur,
    ("Anneau", "Seuil", "non", "non", True, False, False, False): AnneauDefensifSeuilAccelerateur,
    ("Armure", "Seuil", "non", "non", True, False, False, False): ArmureDefensifSeuilAccelerateur,
    ("Heaume", "Seuil", "non", "non", True, False, False, False): HeaumeDefensifSeuilAccelerateur,
    ("Anneau", "Valeur", "non", "non", True, False, False, False): AnneauDefensifValeurAccelerateur,
    ("Armure", "Valeur", "non", "non", True, False, False, False): ArmureDefensifValeurAccelerateur,
    ("Heaume", "Valeur", "non", "non", True, False, False, False): HeaumeDefensifValeurAccelerateur,
    ("Anneau", "non", "PompeAPV", "non", True, False, False, False): AnneauPompeAPVAccelerateur,
    ("Armure", "non", "PompeAPV", "non", True, False, False, False): ArmurePompeAPVAccelerateur,
    ("Heaume", "non", "PompeAPV", "non", True, False, False, False): HeaumePompeAPVAccelerateur,
    ("Anneau", "Plafond", "PompeAPV", "non", True, False, False, False): AnneauDefensifPlafondPompeAPVAccelerateur,
    ("Armure", "Plafond", "PompeAPV", "non", True, False, False, False): ArmureDefensifPlafondPompeAPVAccelerateur,
    ("Heaume", "Plafond", "PompeAPV", "non", True, False, False, False): HeaumeDefensifPlafondPompeAPVAccelerateur,
    ("Anneau", "Proportion", "PompeAPV", "non", True, False, False, False): AnneauDefensifProportionPompeAPVAccelerateur,
    ("Armure", "Proportion", "PompeAPV", "non", True, False, False, False): ArmureDefensifProportionPompeAPVAccelerateur,
    ("Heaume", "Proportion", "PompeAPV", "non", True, False, False, False): HeaumeDefensifProportionPompeAPVAccelerateur,
    ("Anneau", "Seuil", "PompeAPV", "non", True, False, False, False): AnneauDefensifSeuilPompeAPVAccelerateur,
    ("Armure", "Seuil", "PompeAPV", "non", True, False, False, False): ArmureDefensifSeuilPompeAPVAccelerateur,
    ("Heaume", "Seuil", "PompeAPV", "non", True, False, False, False): HeaumeDefensifSeuilPompeAPVAccelerateur,
    ("Anneau", "Valeur", "PompeAPV", "non", True, False, False, False): AnneauDefensifValeurPompeAPVAccelerateur,
    ("Armure", "Valeur", "PompeAPV", "non", True, False, False, False): ArmureDefensifValeurPompeAPVAccelerateur,
    ("Heaume", "Valeur", "PompeAPV", "non", True, False, False, False): HeaumeDefensifValeurPompeAPVAccelerateur,
    ("Anneau", "non", "RenforceRegenPV", "non", True, False, False, False): AnneauRenforceRegenPVAccelerateur,
    ("Armure", "non", "RenforceRegenPV", "non", True, False, False, False): ArmureRenforceRegenPVAccelerateur,
    ("Heaume", "non", "RenforceRegenPV", "non", True, False, False, False): HeaumeRenforceRegenPVAccelerateur,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, False, False, False): AnneauDefensifPlafondRenforceRegenPVAccelerateur,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, False, False, False): ArmureDefensifPlafondRenforceRegenPVAccelerateur,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, False, False, False): HeaumeDefensifPlafondRenforceRegenPVAccelerateur,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, False, False, False): AnneauDefensifProportionRenforceRegenPVAccelerateur,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, False, False, False): ArmureDefensifProportionRenforceRegenPVAccelerateur,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, False, False, False): HeaumeDefensifProportionRenforceRegenPVAccelerateur,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, False, False, False): AnneauDefensifSeuilRenforceRegenPVAccelerateur,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, False, False, False): ArmureDefensifSeuilRenforceRegenPVAccelerateur,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, False, False, False): HeaumeDefensifSeuilRenforceRegenPVAccelerateur,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, False, False, False): AnneauDefensifValeurRenforceRegenPVAccelerateur,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, False, False, False): ArmureDefensifValeurRenforceRegenPVAccelerateur,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, False, False, False): HeaumeDefensifValeurRenforceRegenPVAccelerateur,
    ("Anneau", "non", "non", "PompeAPM", True, False, False, False): AnneauPompeAPMAccelerateur,
    ("Armure", "non", "non", "PompeAPM", True, False, False, False): ArmurePompeAPMAccelerateur,
    ("Heaume", "non", "non", "PompeAPM", True, False, False, False): HeaumePompeAPMAccelerateur,
    ("Anneau", "Plafond", "non", "PompeAPM", True, False, False, False): AnneauDefensifPlafondPompeAPMAccelerateur,
    ("Armure", "Plafond", "non", "PompeAPM", True, False, False, False): ArmureDefensifPlafondPompeAPMAccelerateur,
    ("Heaume", "Plafond", "non", "PompeAPM", True, False, False, False): HeaumeDefensifPlafondPompeAPMAccelerateur,
    ("Anneau", "Proportion", "non", "PompeAPM", True, False, False, False): AnneauDefensifProportionPompeAPMAccelerateur,
    ("Armure", "Proportion", "non", "PompeAPM", True, False, False, False): ArmureDefensifProportionPompeAPMAccelerateur,
    ("Heaume", "Proportion", "non", "PompeAPM", True, False, False, False): HeaumeDefensifProportionPompeAPMAccelerateur,
    ("Anneau", "Seuil", "non", "PompeAPM", True, False, False, False): AnneauDefensifSeuilPompeAPMAccelerateur,
    ("Armure", "Seuil", "non", "PompeAPM", True, False, False, False): ArmureDefensifSeuilPompeAPMAccelerateur,
    ("Heaume", "Seuil", "non", "PompeAPM", True, False, False, False): HeaumeDefensifSeuilPompeAPMAccelerateur,
    ("Anneau", "Valeur", "non", "PompeAPM", True, False, False, False): AnneauDefensifValeurPompeAPMAccelerateur,
    ("Armure", "Valeur", "non", "PompeAPM", True, False, False, False): ArmureDefensifValeurPompeAPMAccelerateur,
    ("Heaume", "Valeur", "non", "PompeAPM", True, False, False, False): HeaumeDefensifValeurPompeAPMAccelerateur,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, False, False, False): AnneauPompeAPVPompeAPMAccelerateur,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, False, False, False): ArmurePompeAPVPompeAPMAccelerateur,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, False, False, False): HeaumePompeAPVPompeAPMAccelerateur,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, False, False, False): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateur,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, False, False, False): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateur,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, False, False, False): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateur,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, False, False, False): AnneauDefensifProportionPompeAPVPompeAPMAccelerateur,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, False, False, False): ArmureDefensifProportionPompeAPVPompeAPMAccelerateur,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, False, False, False): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateur,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, False, False, False): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateur,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, False, False, False): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateur,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, False, False, False): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateur,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, False, False, False): AnneauDefensifValeurPompeAPVPompeAPMAccelerateur,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, False, False, False): ArmureDefensifValeurPompeAPVPompeAPMAccelerateur,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, False, False, False): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateur,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, False, False, False): AnneauRenforceRegenPVPompeAPMAccelerateur,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, False, False, False): ArmureRenforceRegenPVPompeAPMAccelerateur,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, False, False, False): HeaumeRenforceRegenPVPompeAPMAccelerateur,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, False, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateur,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, False, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateur,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, False, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateur,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, False, False): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateur,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, False, False): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateur,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, False, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateur,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, False, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateur,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, False, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateur,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, False, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateur,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, False, False): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateur,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, False, False): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateur,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, False, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateur,
    ("Anneau", "non", "non", "RenforceRegenPM", True, False, False, False): AnneauRenforceRegenPMAccelerateur,
    ("Armure", "non", "non", "RenforceRegenPM", True, False, False, False): ArmureRenforceRegenPMAccelerateur,
    ("Heaume", "non", "non", "RenforceRegenPM", True, False, False, False): HeaumeRenforceRegenPMAccelerateur,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, False, False, False): AnneauDefensifPlafondRenforceRegenPMAccelerateur,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, False, False, False): ArmureDefensifPlafondRenforceRegenPMAccelerateur,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, False, False, False): HeaumeDefensifPlafondRenforceRegenPMAccelerateur,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, False, False, False): AnneauDefensifProportionRenforceRegenPMAccelerateur,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, False, False, False): ArmureDefensifProportionRenforceRegenPMAccelerateur,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, False, False, False): HeaumeDefensifProportionRenforceRegenPMAccelerateur,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, False, False, False): AnneauDefensifSeuilRenforceRegenPMAccelerateur,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, False, False, False): ArmureDefensifSeuilRenforceRegenPMAccelerateur,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, False, False, False): HeaumeDefensifSeuilRenforceRegenPMAccelerateur,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, False, False, False): AnneauDefensifValeurRenforceRegenPMAccelerateur,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, False, False, False): ArmureDefensifValeurRenforceRegenPMAccelerateur,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, False, False, False): HeaumeDefensifValeurRenforceRegenPMAccelerateur,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, False, False, False): AnneauPompeAPVRenforceRegenPMAccelerateur,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, False, False, False): ArmurePompeAPVRenforceRegenPMAccelerateur,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, False, False, False): HeaumePompeAPVRenforceRegenPMAccelerateur,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateur,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateur,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateur,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateur,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateur,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateur,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateur,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateur,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateur,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateur,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateur,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateur,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): AnneauRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): ArmureRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): HeaumeRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, False, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateur,
    ("Anneau", "non", "non", "non", False, True, False, False): AnneauAnoblisseur,
    ("Armure", "non", "non", "non", False, True, False, False): ArmureAnoblisseur,
    ("Heaume", "non", "non", "non", False, True, False, False): HeaumeAnoblisseur,
    ("Anneau", "Plafond", "non", "non", False, True, False, False): AnneauDefensifPlafondAnoblisseur,
    ("Armure", "Plafond", "non", "non", False, True, False, False): ArmureDefensifPlafondAnoblisseur,
    ("Heaume", "Plafond", "non", "non", False, True, False, False): HeaumeDefensifPlafondAnoblisseur,
    ("Anneau", "Proportion", "non", "non", False, True, False, False): AnneauDefensifProportionAnoblisseur,
    ("Armure", "Proportion", "non", "non", False, True, False, False): ArmureDefensifProportionAnoblisseur,
    ("Heaume", "Proportion", "non", "non", False, True, False, False): HeaumeDefensifProportionAnoblisseur,
    ("Anneau", "Seuil", "non", "non", False, True, False, False): AnneauDefensifSeuilAnoblisseur,
    ("Armure", "Seuil", "non", "non", False, True, False, False): ArmureDefensifSeuilAnoblisseur,
    ("Heaume", "Seuil", "non", "non", False, True, False, False): HeaumeDefensifSeuilAnoblisseur,
    ("Anneau", "Valeur", "non", "non", False, True, False, False): AnneauDefensifValeurAnoblisseur,
    ("Armure", "Valeur", "non", "non", False, True, False, False): ArmureDefensifValeurAnoblisseur,
    ("Heaume", "Valeur", "non", "non", False, True, False, False): HeaumeDefensifValeurAnoblisseur,
    ("Anneau", "non", "PompeAPV", "non", False, True, False, False): AnneauPompeAPVAnoblisseur,
    ("Armure", "non", "PompeAPV", "non", False, True, False, False): ArmurePompeAPVAnoblisseur,
    ("Heaume", "non", "PompeAPV", "non", False, True, False, False): HeaumePompeAPVAnoblisseur,
    ("Anneau", "Plafond", "PompeAPV", "non", False, True, False, False): AnneauDefensifPlafondPompeAPVAnoblisseur,
    ("Armure", "Plafond", "PompeAPV", "non", False, True, False, False): ArmureDefensifPlafondPompeAPVAnoblisseur,
    ("Heaume", "Plafond", "PompeAPV", "non", False, True, False, False): HeaumeDefensifPlafondPompeAPVAnoblisseur,
    ("Anneau", "Proportion", "PompeAPV", "non", False, True, False, False): AnneauDefensifProportionPompeAPVAnoblisseur,
    ("Armure", "Proportion", "PompeAPV", "non", False, True, False, False): ArmureDefensifProportionPompeAPVAnoblisseur,
    ("Heaume", "Proportion", "PompeAPV", "non", False, True, False, False): HeaumeDefensifProportionPompeAPVAnoblisseur,
    ("Anneau", "Seuil", "PompeAPV", "non", False, True, False, False): AnneauDefensifSeuilPompeAPVAnoblisseur,
    ("Armure", "Seuil", "PompeAPV", "non", False, True, False, False): ArmureDefensifSeuilPompeAPVAnoblisseur,
    ("Heaume", "Seuil", "PompeAPV", "non", False, True, False, False): HeaumeDefensifSeuilPompeAPVAnoblisseur,
    ("Anneau", "Valeur", "PompeAPV", "non", False, True, False, False): AnneauDefensifValeurPompeAPVAnoblisseur,
    ("Armure", "Valeur", "PompeAPV", "non", False, True, False, False): ArmureDefensifValeurPompeAPVAnoblisseur,
    ("Heaume", "Valeur", "PompeAPV", "non", False, True, False, False): HeaumeDefensifValeurPompeAPVAnoblisseur,
    ("Anneau", "non", "RenforceRegenPV", "non", False, True, False, False): AnneauRenforceRegenPVAnoblisseur,
    ("Armure", "non", "RenforceRegenPV", "non", False, True, False, False): ArmureRenforceRegenPVAnoblisseur,
    ("Heaume", "non", "RenforceRegenPV", "non", False, True, False, False): HeaumeRenforceRegenPVAnoblisseur,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, True, False, False): AnneauDefensifPlafondRenforceRegenPVAnoblisseur,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, True, False, False): ArmureDefensifPlafondRenforceRegenPVAnoblisseur,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, True, False, False): HeaumeDefensifPlafondRenforceRegenPVAnoblisseur,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, True, False, False): AnneauDefensifProportionRenforceRegenPVAnoblisseur,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, True, False, False): ArmureDefensifProportionRenforceRegenPVAnoblisseur,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, True, False, False): HeaumeDefensifProportionRenforceRegenPVAnoblisseur,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, True, False, False): AnneauDefensifSeuilRenforceRegenPVAnoblisseur,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, True, False, False): ArmureDefensifSeuilRenforceRegenPVAnoblisseur,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, True, False, False): HeaumeDefensifSeuilRenforceRegenPVAnoblisseur,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, True, False, False): AnneauDefensifValeurRenforceRegenPVAnoblisseur,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, True, False, False): ArmureDefensifValeurRenforceRegenPVAnoblisseur,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, True, False, False): HeaumeDefensifValeurRenforceRegenPVAnoblisseur,
    ("Anneau", "non", "non", "PompeAPM", False, True, False, False): AnneauPompeAPMAnoblisseur,
    ("Armure", "non", "non", "PompeAPM", False, True, False, False): ArmurePompeAPMAnoblisseur,
    ("Heaume", "non", "non", "PompeAPM", False, True, False, False): HeaumePompeAPMAnoblisseur,
    ("Anneau", "Plafond", "non", "PompeAPM", False, True, False, False): AnneauDefensifPlafondPompeAPMAnoblisseur,
    ("Armure", "Plafond", "non", "PompeAPM", False, True, False, False): ArmureDefensifPlafondPompeAPMAnoblisseur,
    ("Heaume", "Plafond", "non", "PompeAPM", False, True, False, False): HeaumeDefensifPlafondPompeAPMAnoblisseur,
    ("Anneau", "Proportion", "non", "PompeAPM", False, True, False, False): AnneauDefensifProportionPompeAPMAnoblisseur,
    ("Armure", "Proportion", "non", "PompeAPM", False, True, False, False): ArmureDefensifProportionPompeAPMAnoblisseur,
    ("Heaume", "Proportion", "non", "PompeAPM", False, True, False, False): HeaumeDefensifProportionPompeAPMAnoblisseur,
    ("Anneau", "Seuil", "non", "PompeAPM", False, True, False, False): AnneauDefensifSeuilPompeAPMAnoblisseur,
    ("Armure", "Seuil", "non", "PompeAPM", False, True, False, False): ArmureDefensifSeuilPompeAPMAnoblisseur,
    ("Heaume", "Seuil", "non", "PompeAPM", False, True, False, False): HeaumeDefensifSeuilPompeAPMAnoblisseur,
    ("Anneau", "Valeur", "non", "PompeAPM", False, True, False, False): AnneauDefensifValeurPompeAPMAnoblisseur,
    ("Armure", "Valeur", "non", "PompeAPM", False, True, False, False): ArmureDefensifValeurPompeAPMAnoblisseur,
    ("Heaume", "Valeur", "non", "PompeAPM", False, True, False, False): HeaumeDefensifValeurPompeAPMAnoblisseur,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, True, False, False): AnneauPompeAPVPompeAPMAnoblisseur,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, True, False, False): ArmurePompeAPVPompeAPMAnoblisseur,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, True, False, False): HeaumePompeAPVPompeAPMAnoblisseur,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, True, False, False): AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseur,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, True, False, False): ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseur,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, True, False, False): HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseur,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, True, False, False): AnneauDefensifProportionPompeAPVPompeAPMAnoblisseur,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, True, False, False): ArmureDefensifProportionPompeAPVPompeAPMAnoblisseur,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, True, False, False): HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseur,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, True, False, False): AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseur,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, True, False, False): ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseur,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, True, False, False): HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseur,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, True, False, False): AnneauDefensifValeurPompeAPVPompeAPMAnoblisseur,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, True, False, False): ArmureDefensifValeurPompeAPVPompeAPMAnoblisseur,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, True, False, False): HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseur,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, True, False, False): AnneauRenforceRegenPVPompeAPMAnoblisseur,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, True, False, False): ArmureRenforceRegenPVPompeAPMAnoblisseur,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, True, False, False): HeaumeRenforceRegenPVPompeAPMAnoblisseur,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, False, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseur,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, False, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseur,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, False, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseur,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, False, False): AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseur,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, False, False): ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseur,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, False, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseur,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, False, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseur,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, False, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseur,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, False, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseur,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, False, False): AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseur,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, False, False): ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseur,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, False, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseur,
    ("Anneau", "non", "non", "RenforceRegenPM", False, True, False, False): AnneauRenforceRegenPMAnoblisseur,
    ("Armure", "non", "non", "RenforceRegenPM", False, True, False, False): ArmureRenforceRegenPMAnoblisseur,
    ("Heaume", "non", "non", "RenforceRegenPM", False, True, False, False): HeaumeRenforceRegenPMAnoblisseur,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, True, False, False): AnneauDefensifPlafondRenforceRegenPMAnoblisseur,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, True, False, False): ArmureDefensifPlafondRenforceRegenPMAnoblisseur,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, True, False, False): HeaumeDefensifPlafondRenforceRegenPMAnoblisseur,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, True, False, False): AnneauDefensifProportionRenforceRegenPMAnoblisseur,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, True, False, False): ArmureDefensifProportionRenforceRegenPMAnoblisseur,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, True, False, False): HeaumeDefensifProportionRenforceRegenPMAnoblisseur,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, True, False, False): AnneauDefensifSeuilRenforceRegenPMAnoblisseur,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, True, False, False): ArmureDefensifSeuilRenforceRegenPMAnoblisseur,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, True, False, False): HeaumeDefensifSeuilRenforceRegenPMAnoblisseur,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, True, False, False): AnneauDefensifValeurRenforceRegenPMAnoblisseur,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, True, False, False): ArmureDefensifValeurRenforceRegenPMAnoblisseur,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, True, False, False): HeaumeDefensifValeurRenforceRegenPMAnoblisseur,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, True, False, False): AnneauPompeAPVRenforceRegenPMAnoblisseur,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, True, False, False): ArmurePompeAPVRenforceRegenPMAnoblisseur,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, True, False, False): HeaumePompeAPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseur,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseur,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseur,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseur,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseur,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): AnneauRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): ArmureRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): HeaumeRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, False, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseur,
    ("Anneau", "non", "non", "non", True, True, False, False): AnneauAccelerateurAnoblisseur,
    ("Armure", "non", "non", "non", True, True, False, False): ArmureAccelerateurAnoblisseur,
    ("Heaume", "non", "non", "non", True, True, False, False): HeaumeAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "non", "non", True, True, False, False): AnneauDefensifPlafondAccelerateurAnoblisseur,
    ("Armure", "Plafond", "non", "non", True, True, False, False): ArmureDefensifPlafondAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "non", "non", True, True, False, False): HeaumeDefensifPlafondAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "non", "non", True, True, False, False): AnneauDefensifProportionAccelerateurAnoblisseur,
    ("Armure", "Proportion", "non", "non", True, True, False, False): ArmureDefensifProportionAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "non", "non", True, True, False, False): HeaumeDefensifProportionAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "non", "non", True, True, False, False): AnneauDefensifSeuilAccelerateurAnoblisseur,
    ("Armure", "Seuil", "non", "non", True, True, False, False): ArmureDefensifSeuilAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "non", "non", True, True, False, False): HeaumeDefensifSeuilAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "non", "non", True, True, False, False): AnneauDefensifValeurAccelerateurAnoblisseur,
    ("Armure", "Valeur", "non", "non", True, True, False, False): ArmureDefensifValeurAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "non", "non", True, True, False, False): HeaumeDefensifValeurAccelerateurAnoblisseur,
    ("Anneau", "non", "PompeAPV", "non", True, True, False, False): AnneauPompeAPVAccelerateurAnoblisseur,
    ("Armure", "non", "PompeAPV", "non", True, True, False, False): ArmurePompeAPVAccelerateurAnoblisseur,
    ("Heaume", "non", "PompeAPV", "non", True, True, False, False): HeaumePompeAPVAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "PompeAPV", "non", True, True, False, False): AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseur,
    ("Armure", "Plafond", "PompeAPV", "non", True, True, False, False): ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "PompeAPV", "non", True, True, False, False): HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "PompeAPV", "non", True, True, False, False): AnneauDefensifProportionPompeAPVAccelerateurAnoblisseur,
    ("Armure", "Proportion", "PompeAPV", "non", True, True, False, False): ArmureDefensifProportionPompeAPVAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "PompeAPV", "non", True, True, False, False): HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "PompeAPV", "non", True, True, False, False): AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseur,
    ("Armure", "Seuil", "PompeAPV", "non", True, True, False, False): ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "PompeAPV", "non", True, True, False, False): HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "PompeAPV", "non", True, True, False, False): AnneauDefensifValeurPompeAPVAccelerateurAnoblisseur,
    ("Armure", "Valeur", "PompeAPV", "non", True, True, False, False): ArmureDefensifValeurPompeAPVAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "PompeAPV", "non", True, True, False, False): HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseur,
    ("Anneau", "non", "RenforceRegenPV", "non", True, True, False, False): AnneauRenforceRegenPVAccelerateurAnoblisseur,
    ("Armure", "non", "RenforceRegenPV", "non", True, True, False, False): ArmureRenforceRegenPVAccelerateurAnoblisseur,
    ("Heaume", "non", "RenforceRegenPV", "non", True, True, False, False): HeaumeRenforceRegenPVAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, True, False, False): AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseur,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, True, False, False): ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, True, False, False): HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, True, False, False): AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseur,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, True, False, False): ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, True, False, False): HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, True, False, False): AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseur,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, True, False, False): ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, True, False, False): HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, True, False, False): AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseur,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, True, False, False): ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, True, False, False): HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseur,
    ("Anneau", "non", "non", "PompeAPM", True, True, False, False): AnneauPompeAPMAccelerateurAnoblisseur,
    ("Armure", "non", "non", "PompeAPM", True, True, False, False): ArmurePompeAPMAccelerateurAnoblisseur,
    ("Heaume", "non", "non", "PompeAPM", True, True, False, False): HeaumePompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "non", "PompeAPM", True, True, False, False): AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Plafond", "non", "PompeAPM", True, True, False, False): ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "non", "PompeAPM", True, True, False, False): HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "non", "PompeAPM", True, True, False, False): AnneauDefensifProportionPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Proportion", "non", "PompeAPM", True, True, False, False): ArmureDefensifProportionPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "non", "PompeAPM", True, True, False, False): HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "non", "PompeAPM", True, True, False, False): AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Seuil", "non", "PompeAPM", True, True, False, False): ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "non", "PompeAPM", True, True, False, False): HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "non", "PompeAPM", True, True, False, False): AnneauDefensifValeurPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Valeur", "non", "PompeAPM", True, True, False, False): ArmureDefensifValeurPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "non", "PompeAPM", True, True, False, False): HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, True, False, False): AnneauPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, True, False, False): ArmurePompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, True, False, False): HeaumePompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, True, False, False): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, True, False, False): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, True, False, False): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, True, False, False): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, True, False, False): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, True, False, False): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, True, False, False): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, True, False, False): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, True, False, False): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, True, False, False): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, True, False, False): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, True, False, False): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, True, False, False): AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, True, False, False): ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, True, False, False): HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, False, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, False, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, False, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, False, False): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, False, False): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, False, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, False, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, False, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, False, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, False, False): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, False, False): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, False, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseur,
    ("Anneau", "non", "non", "RenforceRegenPM", True, True, False, False): AnneauRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "non", "non", "RenforceRegenPM", True, True, False, False): ArmureRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "non", "non", "RenforceRegenPM", True, True, False, False): HeaumeRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, True, False, False): AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, True, False, False): ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, True, False, False): HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, True, False, False): AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, True, False, False): ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, True, False, False): HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, True, False, False): AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, True, False, False): ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, True, False, False): HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, True, False, False): AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, True, False, False): ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, True, False, False): HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, True, False, False): AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, True, False, False): ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, True, False, False): HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, False, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseur,
    ("Anneau", "non", "non", "non", False, False, True, False): AnneauElementaire,
    ("Armure", "non", "non", "non", False, False, True, False): ArmureElementaire,
    ("Heaume", "non", "non", "non", False, False, True, False): HeaumeElementaire,
    ("Anneau", "Plafond", "non", "non", False, False, True, False): AnneauDefensifPlafondElementaire,
    ("Armure", "Plafond", "non", "non", False, False, True, False): ArmureDefensifPlafondElementaire,
    ("Heaume", "Plafond", "non", "non", False, False, True, False): HeaumeDefensifPlafondElementaire,
    ("Anneau", "Proportion", "non", "non", False, False, True, False): AnneauDefensifProportionElementaire,
    ("Armure", "Proportion", "non", "non", False, False, True, False): ArmureDefensifProportionElementaire,
    ("Heaume", "Proportion", "non", "non", False, False, True, False): HeaumeDefensifProportionElementaire,
    ("Anneau", "Seuil", "non", "non", False, False, True, False): AnneauDefensifSeuilElementaire,
    ("Armure", "Seuil", "non", "non", False, False, True, False): ArmureDefensifSeuilElementaire,
    ("Heaume", "Seuil", "non", "non", False, False, True, False): HeaumeDefensifSeuilElementaire,
    ("Anneau", "Valeur", "non", "non", False, False, True, False): AnneauDefensifValeurElementaire,
    ("Armure", "Valeur", "non", "non", False, False, True, False): ArmureDefensifValeurElementaire,
    ("Heaume", "Valeur", "non", "non", False, False, True, False): HeaumeDefensifValeurElementaire,
    ("Anneau", "non", "PompeAPV", "non", False, False, True, False): AnneauPompeAPVElementaire,
    ("Armure", "non", "PompeAPV", "non", False, False, True, False): ArmurePompeAPVElementaire,
    ("Heaume", "non", "PompeAPV", "non", False, False, True, False): HeaumePompeAPVElementaire,
    ("Anneau", "Plafond", "PompeAPV", "non", False, False, True, False): AnneauDefensifPlafondPompeAPVElementaire,
    ("Armure", "Plafond", "PompeAPV", "non", False, False, True, False): ArmureDefensifPlafondPompeAPVElementaire,
    ("Heaume", "Plafond", "PompeAPV", "non", False, False, True, False): HeaumeDefensifPlafondPompeAPVElementaire,
    ("Anneau", "Proportion", "PompeAPV", "non", False, False, True, False): AnneauDefensifProportionPompeAPVElementaire,
    ("Armure", "Proportion", "PompeAPV", "non", False, False, True, False): ArmureDefensifProportionPompeAPVElementaire,
    ("Heaume", "Proportion", "PompeAPV", "non", False, False, True, False): HeaumeDefensifProportionPompeAPVElementaire,
    ("Anneau", "Seuil", "PompeAPV", "non", False, False, True, False): AnneauDefensifSeuilPompeAPVElementaire,
    ("Armure", "Seuil", "PompeAPV", "non", False, False, True, False): ArmureDefensifSeuilPompeAPVElementaire,
    ("Heaume", "Seuil", "PompeAPV", "non", False, False, True, False): HeaumeDefensifSeuilPompeAPVElementaire,
    ("Anneau", "Valeur", "PompeAPV", "non", False, False, True, False): AnneauDefensifValeurPompeAPVElementaire,
    ("Armure", "Valeur", "PompeAPV", "non", False, False, True, False): ArmureDefensifValeurPompeAPVElementaire,
    ("Heaume", "Valeur", "PompeAPV", "non", False, False, True, False): HeaumeDefensifValeurPompeAPVElementaire,
    ("Anneau", "non", "RenforceRegenPV", "non", False, False, True, False): AnneauRenforceRegenPVElementaire,
    ("Armure", "non", "RenforceRegenPV", "non", False, False, True, False): ArmureRenforceRegenPVElementaire,
    ("Heaume", "non", "RenforceRegenPV", "non", False, False, True, False): HeaumeRenforceRegenPVElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, False, True, False): AnneauDefensifPlafondRenforceRegenPVElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, False, True, False): ArmureDefensifPlafondRenforceRegenPVElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, False, True, False): HeaumeDefensifPlafondRenforceRegenPVElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, False, True, False): AnneauDefensifProportionRenforceRegenPVElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, False, True, False): ArmureDefensifProportionRenforceRegenPVElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, False, True, False): HeaumeDefensifProportionRenforceRegenPVElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, False, True, False): AnneauDefensifSeuilRenforceRegenPVElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, False, True, False): ArmureDefensifSeuilRenforceRegenPVElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, False, True, False): HeaumeDefensifSeuilRenforceRegenPVElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, False, True, False): AnneauDefensifValeurRenforceRegenPVElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, False, True, False): ArmureDefensifValeurRenforceRegenPVElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, False, True, False): HeaumeDefensifValeurRenforceRegenPVElementaire,
    ("Anneau", "non", "non", "PompeAPM", False, False, True, False): AnneauPompeAPMElementaire,
    ("Armure", "non", "non", "PompeAPM", False, False, True, False): ArmurePompeAPMElementaire,
    ("Heaume", "non", "non", "PompeAPM", False, False, True, False): HeaumePompeAPMElementaire,
    ("Anneau", "Plafond", "non", "PompeAPM", False, False, True, False): AnneauDefensifPlafondPompeAPMElementaire,
    ("Armure", "Plafond", "non", "PompeAPM", False, False, True, False): ArmureDefensifPlafondPompeAPMElementaire,
    ("Heaume", "Plafond", "non", "PompeAPM", False, False, True, False): HeaumeDefensifPlafondPompeAPMElementaire,
    ("Anneau", "Proportion", "non", "PompeAPM", False, False, True, False): AnneauDefensifProportionPompeAPMElementaire,
    ("Armure", "Proportion", "non", "PompeAPM", False, False, True, False): ArmureDefensifProportionPompeAPMElementaire,
    ("Heaume", "Proportion", "non", "PompeAPM", False, False, True, False): HeaumeDefensifProportionPompeAPMElementaire,
    ("Anneau", "Seuil", "non", "PompeAPM", False, False, True, False): AnneauDefensifSeuilPompeAPMElementaire,
    ("Armure", "Seuil", "non", "PompeAPM", False, False, True, False): ArmureDefensifSeuilPompeAPMElementaire,
    ("Heaume", "Seuil", "non", "PompeAPM", False, False, True, False): HeaumeDefensifSeuilPompeAPMElementaire,
    ("Anneau", "Valeur", "non", "PompeAPM", False, False, True, False): AnneauDefensifValeurPompeAPMElementaire,
    ("Armure", "Valeur", "non", "PompeAPM", False, False, True, False): ArmureDefensifValeurPompeAPMElementaire,
    ("Heaume", "Valeur", "non", "PompeAPM", False, False, True, False): HeaumeDefensifValeurPompeAPMElementaire,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, False, True, False): AnneauPompeAPVPompeAPMElementaire,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, False, True, False): ArmurePompeAPVPompeAPMElementaire,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, False, True, False): HeaumePompeAPVPompeAPMElementaire,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, False, True, False): AnneauDefensifPlafondPompeAPVPompeAPMElementaire,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, False, True, False): ArmureDefensifPlafondPompeAPVPompeAPMElementaire,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, False, True, False): HeaumeDefensifPlafondPompeAPVPompeAPMElementaire,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, False, True, False): AnneauDefensifProportionPompeAPVPompeAPMElementaire,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, False, True, False): ArmureDefensifProportionPompeAPVPompeAPMElementaire,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, False, True, False): HeaumeDefensifProportionPompeAPVPompeAPMElementaire,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, False, True, False): AnneauDefensifSeuilPompeAPVPompeAPMElementaire,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, False, True, False): ArmureDefensifSeuilPompeAPVPompeAPMElementaire,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, False, True, False): HeaumeDefensifSeuilPompeAPVPompeAPMElementaire,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, False, True, False): AnneauDefensifValeurPompeAPVPompeAPMElementaire,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, False, True, False): ArmureDefensifValeurPompeAPVPompeAPMElementaire,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, False, True, False): HeaumeDefensifValeurPompeAPVPompeAPMElementaire,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, False, True, False): AnneauRenforceRegenPVPompeAPMElementaire,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, False, True, False): ArmureRenforceRegenPVPompeAPMElementaire,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, False, True, False): HeaumeRenforceRegenPVPompeAPMElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, True, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, True, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, True, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, True, False): AnneauDefensifProportionRenforceRegenPVPompeAPMElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, True, False): ArmureDefensifProportionRenforceRegenPVPompeAPMElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, True, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, True, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, True, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, True, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, True, False): AnneauDefensifValeurRenforceRegenPVPompeAPMElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, True, False): ArmureDefensifValeurRenforceRegenPVPompeAPMElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, True, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMElementaire,
    ("Anneau", "non", "non", "RenforceRegenPM", False, False, True, False): AnneauRenforceRegenPMElementaire,
    ("Armure", "non", "non", "RenforceRegenPM", False, False, True, False): ArmureRenforceRegenPMElementaire,
    ("Heaume", "non", "non", "RenforceRegenPM", False, False, True, False): HeaumeRenforceRegenPMElementaire,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, False, True, False): AnneauDefensifPlafondRenforceRegenPMElementaire,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, False, True, False): ArmureDefensifPlafondRenforceRegenPMElementaire,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, False, True, False): HeaumeDefensifPlafondRenforceRegenPMElementaire,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, False, True, False): AnneauDefensifProportionRenforceRegenPMElementaire,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, False, True, False): ArmureDefensifProportionRenforceRegenPMElementaire,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, False, True, False): HeaumeDefensifProportionRenforceRegenPMElementaire,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, False, True, False): AnneauDefensifSeuilRenforceRegenPMElementaire,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, False, True, False): ArmureDefensifSeuilRenforceRegenPMElementaire,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, False, True, False): HeaumeDefensifSeuilRenforceRegenPMElementaire,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, False, True, False): AnneauDefensifValeurRenforceRegenPMElementaire,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, False, True, False): ArmureDefensifValeurRenforceRegenPMElementaire,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, False, True, False): HeaumeDefensifValeurRenforceRegenPMElementaire,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, False, True, False): AnneauPompeAPVRenforceRegenPMElementaire,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, False, True, False): ArmurePompeAPVRenforceRegenPMElementaire,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, False, True, False): HeaumePompeAPVRenforceRegenPMElementaire,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMElementaire,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMElementaire,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMElementaire,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifProportionPompeAPVRenforceRegenPMElementaire,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifProportionPompeAPVRenforceRegenPMElementaire,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMElementaire,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMElementaire,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMElementaire,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMElementaire,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifValeurPompeAPVRenforceRegenPMElementaire,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifValeurPompeAPVRenforceRegenPMElementaire,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMElementaire,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): AnneauRenforceRegenPVRenforceRegenPMElementaire,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): ArmureRenforceRegenPVRenforceRegenPMElementaire,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): HeaumeRenforceRegenPVRenforceRegenPMElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, True, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMElementaire,
    ("Anneau", "non", "non", "non", True, False, True, False): AnneauAccelerateurElementaire,
    ("Armure", "non", "non", "non", True, False, True, False): ArmureAccelerateurElementaire,
    ("Heaume", "non", "non", "non", True, False, True, False): HeaumeAccelerateurElementaire,
    ("Anneau", "Plafond", "non", "non", True, False, True, False): AnneauDefensifPlafondAccelerateurElementaire,
    ("Armure", "Plafond", "non", "non", True, False, True, False): ArmureDefensifPlafondAccelerateurElementaire,
    ("Heaume", "Plafond", "non", "non", True, False, True, False): HeaumeDefensifPlafondAccelerateurElementaire,
    ("Anneau", "Proportion", "non", "non", True, False, True, False): AnneauDefensifProportionAccelerateurElementaire,
    ("Armure", "Proportion", "non", "non", True, False, True, False): ArmureDefensifProportionAccelerateurElementaire,
    ("Heaume", "Proportion", "non", "non", True, False, True, False): HeaumeDefensifProportionAccelerateurElementaire,
    ("Anneau", "Seuil", "non", "non", True, False, True, False): AnneauDefensifSeuilAccelerateurElementaire,
    ("Armure", "Seuil", "non", "non", True, False, True, False): ArmureDefensifSeuilAccelerateurElementaire,
    ("Heaume", "Seuil", "non", "non", True, False, True, False): HeaumeDefensifSeuilAccelerateurElementaire,
    ("Anneau", "Valeur", "non", "non", True, False, True, False): AnneauDefensifValeurAccelerateurElementaire,
    ("Armure", "Valeur", "non", "non", True, False, True, False): ArmureDefensifValeurAccelerateurElementaire,
    ("Heaume", "Valeur", "non", "non", True, False, True, False): HeaumeDefensifValeurAccelerateurElementaire,
    ("Anneau", "non", "PompeAPV", "non", True, False, True, False): AnneauPompeAPVAccelerateurElementaire,
    ("Armure", "non", "PompeAPV", "non", True, False, True, False): ArmurePompeAPVAccelerateurElementaire,
    ("Heaume", "non", "PompeAPV", "non", True, False, True, False): HeaumePompeAPVAccelerateurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "non", True, False, True, False): AnneauDefensifPlafondPompeAPVAccelerateurElementaire,
    ("Armure", "Plafond", "PompeAPV", "non", True, False, True, False): ArmureDefensifPlafondPompeAPVAccelerateurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "non", True, False, True, False): HeaumeDefensifPlafondPompeAPVAccelerateurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "non", True, False, True, False): AnneauDefensifProportionPompeAPVAccelerateurElementaire,
    ("Armure", "Proportion", "PompeAPV", "non", True, False, True, False): ArmureDefensifProportionPompeAPVAccelerateurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "non", True, False, True, False): HeaumeDefensifProportionPompeAPVAccelerateurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "non", True, False, True, False): AnneauDefensifSeuilPompeAPVAccelerateurElementaire,
    ("Armure", "Seuil", "PompeAPV", "non", True, False, True, False): ArmureDefensifSeuilPompeAPVAccelerateurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "non", True, False, True, False): HeaumeDefensifSeuilPompeAPVAccelerateurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "non", True, False, True, False): AnneauDefensifValeurPompeAPVAccelerateurElementaire,
    ("Armure", "Valeur", "PompeAPV", "non", True, False, True, False): ArmureDefensifValeurPompeAPVAccelerateurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "non", True, False, True, False): HeaumeDefensifValeurPompeAPVAccelerateurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "non", True, False, True, False): AnneauRenforceRegenPVAccelerateurElementaire,
    ("Armure", "non", "RenforceRegenPV", "non", True, False, True, False): ArmureRenforceRegenPVAccelerateurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "non", True, False, True, False): HeaumeRenforceRegenPVAccelerateurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, False, True, False): AnneauDefensifPlafondRenforceRegenPVAccelerateurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, False, True, False): ArmureDefensifPlafondRenforceRegenPVAccelerateurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, False, True, False): HeaumeDefensifPlafondRenforceRegenPVAccelerateurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, False, True, False): AnneauDefensifProportionRenforceRegenPVAccelerateurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, False, True, False): ArmureDefensifProportionRenforceRegenPVAccelerateurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, False, True, False): HeaumeDefensifProportionRenforceRegenPVAccelerateurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, False, True, False): AnneauDefensifSeuilRenforceRegenPVAccelerateurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, False, True, False): ArmureDefensifSeuilRenforceRegenPVAccelerateurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, False, True, False): HeaumeDefensifSeuilRenforceRegenPVAccelerateurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, False, True, False): AnneauDefensifValeurRenforceRegenPVAccelerateurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, False, True, False): ArmureDefensifValeurRenforceRegenPVAccelerateurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, False, True, False): HeaumeDefensifValeurRenforceRegenPVAccelerateurElementaire,
    ("Anneau", "non", "non", "PompeAPM", True, False, True, False): AnneauPompeAPMAccelerateurElementaire,
    ("Armure", "non", "non", "PompeAPM", True, False, True, False): ArmurePompeAPMAccelerateurElementaire,
    ("Heaume", "non", "non", "PompeAPM", True, False, True, False): HeaumePompeAPMAccelerateurElementaire,
    ("Anneau", "Plafond", "non", "PompeAPM", True, False, True, False): AnneauDefensifPlafondPompeAPMAccelerateurElementaire,
    ("Armure", "Plafond", "non", "PompeAPM", True, False, True, False): ArmureDefensifPlafondPompeAPMAccelerateurElementaire,
    ("Heaume", "Plafond", "non", "PompeAPM", True, False, True, False): HeaumeDefensifPlafondPompeAPMAccelerateurElementaire,
    ("Anneau", "Proportion", "non", "PompeAPM", True, False, True, False): AnneauDefensifProportionPompeAPMAccelerateurElementaire,
    ("Armure", "Proportion", "non", "PompeAPM", True, False, True, False): ArmureDefensifProportionPompeAPMAccelerateurElementaire,
    ("Heaume", "Proportion", "non", "PompeAPM", True, False, True, False): HeaumeDefensifProportionPompeAPMAccelerateurElementaire,
    ("Anneau", "Seuil", "non", "PompeAPM", True, False, True, False): AnneauDefensifSeuilPompeAPMAccelerateurElementaire,
    ("Armure", "Seuil", "non", "PompeAPM", True, False, True, False): ArmureDefensifSeuilPompeAPMAccelerateurElementaire,
    ("Heaume", "Seuil", "non", "PompeAPM", True, False, True, False): HeaumeDefensifSeuilPompeAPMAccelerateurElementaire,
    ("Anneau", "Valeur", "non", "PompeAPM", True, False, True, False): AnneauDefensifValeurPompeAPMAccelerateurElementaire,
    ("Armure", "Valeur", "non", "PompeAPM", True, False, True, False): ArmureDefensifValeurPompeAPMAccelerateurElementaire,
    ("Heaume", "Valeur", "non", "PompeAPM", True, False, True, False): HeaumeDefensifValeurPompeAPMAccelerateurElementaire,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, False, True, False): AnneauPompeAPVPompeAPMAccelerateurElementaire,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, False, True, False): ArmurePompeAPVPompeAPMAccelerateurElementaire,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, False, True, False): HeaumePompeAPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, False, True, False): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurElementaire,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, False, True, False): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, False, True, False): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, False, True, False): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurElementaire,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, False, True, False): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, False, True, False): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, False, True, False): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurElementaire,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, False, True, False): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, False, True, False): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, False, True, False): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurElementaire,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, False, True, False): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, False, True, False): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, False, True, False): AnneauRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, False, True, False): ArmureRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, False, True, False): HeaumeRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, True, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, True, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, True, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, True, False): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, True, False): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, True, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, True, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, True, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, True, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, True, False): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, True, False): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, True, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaire,
    ("Anneau", "non", "non", "RenforceRegenPM", True, False, True, False): AnneauRenforceRegenPMAccelerateurElementaire,
    ("Armure", "non", "non", "RenforceRegenPM", True, False, True, False): ArmureRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "non", "non", "RenforceRegenPM", True, False, True, False): HeaumeRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, False, True, False): AnneauDefensifPlafondRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, False, True, False): ArmureDefensifPlafondRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, False, True, False): HeaumeDefensifPlafondRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, False, True, False): AnneauDefensifProportionRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, False, True, False): ArmureDefensifProportionRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, False, True, False): HeaumeDefensifProportionRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, False, True, False): AnneauDefensifSeuilRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, False, True, False): ArmureDefensifSeuilRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, False, True, False): HeaumeDefensifSeuilRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, False, True, False): AnneauDefensifValeurRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, False, True, False): ArmureDefensifValeurRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, False, True, False): HeaumeDefensifValeurRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, False, True, False): AnneauPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, False, True, False): ArmurePompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, False, True, False): HeaumePompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): AnneauRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): ArmureRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, True, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaire,
    ("Anneau", "non", "non", "non", False, True, True, False): AnneauAnoblisseurElementaire,
    ("Armure", "non", "non", "non", False, True, True, False): ArmureAnoblisseurElementaire,
    ("Heaume", "non", "non", "non", False, True, True, False): HeaumeAnoblisseurElementaire,
    ("Anneau", "Plafond", "non", "non", False, True, True, False): AnneauDefensifPlafondAnoblisseurElementaire,
    ("Armure", "Plafond", "non", "non", False, True, True, False): ArmureDefensifPlafondAnoblisseurElementaire,
    ("Heaume", "Plafond", "non", "non", False, True, True, False): HeaumeDefensifPlafondAnoblisseurElementaire,
    ("Anneau", "Proportion", "non", "non", False, True, True, False): AnneauDefensifProportionAnoblisseurElementaire,
    ("Armure", "Proportion", "non", "non", False, True, True, False): ArmureDefensifProportionAnoblisseurElementaire,
    ("Heaume", "Proportion", "non", "non", False, True, True, False): HeaumeDefensifProportionAnoblisseurElementaire,
    ("Anneau", "Seuil", "non", "non", False, True, True, False): AnneauDefensifSeuilAnoblisseurElementaire,
    ("Armure", "Seuil", "non", "non", False, True, True, False): ArmureDefensifSeuilAnoblisseurElementaire,
    ("Heaume", "Seuil", "non", "non", False, True, True, False): HeaumeDefensifSeuilAnoblisseurElementaire,
    ("Anneau", "Valeur", "non", "non", False, True, True, False): AnneauDefensifValeurAnoblisseurElementaire,
    ("Armure", "Valeur", "non", "non", False, True, True, False): ArmureDefensifValeurAnoblisseurElementaire,
    ("Heaume", "Valeur", "non", "non", False, True, True, False): HeaumeDefensifValeurAnoblisseurElementaire,
    ("Anneau", "non", "PompeAPV", "non", False, True, True, False): AnneauPompeAPVAnoblisseurElementaire,
    ("Armure", "non", "PompeAPV", "non", False, True, True, False): ArmurePompeAPVAnoblisseurElementaire,
    ("Heaume", "non", "PompeAPV", "non", False, True, True, False): HeaumePompeAPVAnoblisseurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "non", False, True, True, False): AnneauDefensifPlafondPompeAPVAnoblisseurElementaire,
    ("Armure", "Plafond", "PompeAPV", "non", False, True, True, False): ArmureDefensifPlafondPompeAPVAnoblisseurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "non", False, True, True, False): HeaumeDefensifPlafondPompeAPVAnoblisseurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "non", False, True, True, False): AnneauDefensifProportionPompeAPVAnoblisseurElementaire,
    ("Armure", "Proportion", "PompeAPV", "non", False, True, True, False): ArmureDefensifProportionPompeAPVAnoblisseurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "non", False, True, True, False): HeaumeDefensifProportionPompeAPVAnoblisseurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "non", False, True, True, False): AnneauDefensifSeuilPompeAPVAnoblisseurElementaire,
    ("Armure", "Seuil", "PompeAPV", "non", False, True, True, False): ArmureDefensifSeuilPompeAPVAnoblisseurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "non", False, True, True, False): HeaumeDefensifSeuilPompeAPVAnoblisseurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "non", False, True, True, False): AnneauDefensifValeurPompeAPVAnoblisseurElementaire,
    ("Armure", "Valeur", "PompeAPV", "non", False, True, True, False): ArmureDefensifValeurPompeAPVAnoblisseurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "non", False, True, True, False): HeaumeDefensifValeurPompeAPVAnoblisseurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "non", False, True, True, False): AnneauRenforceRegenPVAnoblisseurElementaire,
    ("Armure", "non", "RenforceRegenPV", "non", False, True, True, False): ArmureRenforceRegenPVAnoblisseurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "non", False, True, True, False): HeaumeRenforceRegenPVAnoblisseurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, True, True, False): AnneauDefensifPlafondRenforceRegenPVAnoblisseurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, True, True, False): ArmureDefensifPlafondRenforceRegenPVAnoblisseurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, True, True, False): HeaumeDefensifPlafondRenforceRegenPVAnoblisseurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, True, True, False): AnneauDefensifProportionRenforceRegenPVAnoblisseurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, True, True, False): ArmureDefensifProportionRenforceRegenPVAnoblisseurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, True, True, False): HeaumeDefensifProportionRenforceRegenPVAnoblisseurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, True, True, False): AnneauDefensifSeuilRenforceRegenPVAnoblisseurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, True, True, False): ArmureDefensifSeuilRenforceRegenPVAnoblisseurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, True, True, False): HeaumeDefensifSeuilRenforceRegenPVAnoblisseurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, True, True, False): AnneauDefensifValeurRenforceRegenPVAnoblisseurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, True, True, False): ArmureDefensifValeurRenforceRegenPVAnoblisseurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, True, True, False): HeaumeDefensifValeurRenforceRegenPVAnoblisseurElementaire,
    ("Anneau", "non", "non", "PompeAPM", False, True, True, False): AnneauPompeAPMAnoblisseurElementaire,
    ("Armure", "non", "non", "PompeAPM", False, True, True, False): ArmurePompeAPMAnoblisseurElementaire,
    ("Heaume", "non", "non", "PompeAPM", False, True, True, False): HeaumePompeAPMAnoblisseurElementaire,
    ("Anneau", "Plafond", "non", "PompeAPM", False, True, True, False): AnneauDefensifPlafondPompeAPMAnoblisseurElementaire,
    ("Armure", "Plafond", "non", "PompeAPM", False, True, True, False): ArmureDefensifPlafondPompeAPMAnoblisseurElementaire,
    ("Heaume", "Plafond", "non", "PompeAPM", False, True, True, False): HeaumeDefensifPlafondPompeAPMAnoblisseurElementaire,
    ("Anneau", "Proportion", "non", "PompeAPM", False, True, True, False): AnneauDefensifProportionPompeAPMAnoblisseurElementaire,
    ("Armure", "Proportion", "non", "PompeAPM", False, True, True, False): ArmureDefensifProportionPompeAPMAnoblisseurElementaire,
    ("Heaume", "Proportion", "non", "PompeAPM", False, True, True, False): HeaumeDefensifProportionPompeAPMAnoblisseurElementaire,
    ("Anneau", "Seuil", "non", "PompeAPM", False, True, True, False): AnneauDefensifSeuilPompeAPMAnoblisseurElementaire,
    ("Armure", "Seuil", "non", "PompeAPM", False, True, True, False): ArmureDefensifSeuilPompeAPMAnoblisseurElementaire,
    ("Heaume", "Seuil", "non", "PompeAPM", False, True, True, False): HeaumeDefensifSeuilPompeAPMAnoblisseurElementaire,
    ("Anneau", "Valeur", "non", "PompeAPM", False, True, True, False): AnneauDefensifValeurPompeAPMAnoblisseurElementaire,
    ("Armure", "Valeur", "non", "PompeAPM", False, True, True, False): ArmureDefensifValeurPompeAPMAnoblisseurElementaire,
    ("Heaume", "Valeur", "non", "PompeAPM", False, True, True, False): HeaumeDefensifValeurPompeAPMAnoblisseurElementaire,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, True, True, False): AnneauPompeAPVPompeAPMAnoblisseurElementaire,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, True, True, False): ArmurePompeAPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, True, True, False): HeaumePompeAPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, True, True, False): AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, True, True, False): ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, True, True, False): HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, True, True, False): AnneauDefensifProportionPompeAPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, True, True, False): ArmureDefensifProportionPompeAPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, True, True, False): HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, True, True, False): AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, True, True, False): ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, True, True, False): HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, True, True, False): AnneauDefensifValeurPompeAPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, True, True, False): ArmureDefensifValeurPompeAPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, True, True, False): HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, True, True, False): AnneauRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, True, True, False): ArmureRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, True, True, False): HeaumeRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, True, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, True, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, True, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, True, False): AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, True, False): ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, True, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, True, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, True, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, True, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, True, False): AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, True, False): ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, True, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaire,
    ("Anneau", "non", "non", "RenforceRegenPM", False, True, True, False): AnneauRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "non", "non", "RenforceRegenPM", False, True, True, False): ArmureRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "non", "non", "RenforceRegenPM", False, True, True, False): HeaumeRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, True, True, False): AnneauDefensifPlafondRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, True, True, False): ArmureDefensifPlafondRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, True, True, False): HeaumeDefensifPlafondRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, True, True, False): AnneauDefensifProportionRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, True, True, False): ArmureDefensifProportionRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, True, True, False): HeaumeDefensifProportionRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, True, True, False): AnneauDefensifSeuilRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, True, True, False): ArmureDefensifSeuilRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, True, True, False): HeaumeDefensifSeuilRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, True, True, False): AnneauDefensifValeurRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, True, True, False): ArmureDefensifValeurRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, True, True, False): HeaumeDefensifValeurRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, True, True, False): AnneauPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, True, True, False): ArmurePompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, True, True, False): HeaumePompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): AnneauRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): ArmureRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): HeaumeRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, True, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaire,
    ("Anneau", "non", "non", "non", True, True, True, False): AnneauAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "non", "non", True, True, True, False): ArmureAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "non", "non", True, True, True, False): HeaumeAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "non", "non", True, True, True, False): AnneauDefensifPlafondAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "non", "non", True, True, True, False): ArmureDefensifPlafondAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "non", "non", True, True, True, False): HeaumeDefensifPlafondAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "non", "non", True, True, True, False): AnneauDefensifProportionAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "non", "non", True, True, True, False): ArmureDefensifProportionAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "non", "non", True, True, True, False): HeaumeDefensifProportionAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "non", "non", True, True, True, False): AnneauDefensifSeuilAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "non", "non", True, True, True, False): ArmureDefensifSeuilAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "non", "non", True, True, True, False): HeaumeDefensifSeuilAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "non", "non", True, True, True, False): AnneauDefensifValeurAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "non", "non", True, True, True, False): ArmureDefensifValeurAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "non", "non", True, True, True, False): HeaumeDefensifValeurAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "PompeAPV", "non", True, True, True, False): AnneauPompeAPVAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "PompeAPV", "non", True, True, True, False): ArmurePompeAPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "PompeAPV", "non", True, True, True, False): HeaumePompeAPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "non", True, True, True, False): AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "PompeAPV", "non", True, True, True, False): ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "non", True, True, True, False): HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "non", True, True, True, False): AnneauDefensifProportionPompeAPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "PompeAPV", "non", True, True, True, False): ArmureDefensifProportionPompeAPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "non", True, True, True, False): HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "non", True, True, True, False): AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "PompeAPV", "non", True, True, True, False): ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "non", True, True, True, False): HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "non", True, True, True, False): AnneauDefensifValeurPompeAPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "PompeAPV", "non", True, True, True, False): ArmureDefensifValeurPompeAPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "non", True, True, True, False): HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "non", True, True, True, False): AnneauRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "RenforceRegenPV", "non", True, True, True, False): ArmureRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "non", True, True, True, False): HeaumeRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, True, True, False): AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, True, True, False): ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, True, True, False): HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, True, True, False): AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, True, True, False): ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, True, True, False): HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, True, True, False): AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, True, True, False): ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, True, True, False): HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, True, True, False): AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, True, True, False): ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, True, True, False): HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "non", "PompeAPM", True, True, True, False): AnneauPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "non", "PompeAPM", True, True, True, False): ArmurePompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "non", "PompeAPM", True, True, True, False): HeaumePompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "non", "PompeAPM", True, True, True, False): AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "non", "PompeAPM", True, True, True, False): ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "non", "PompeAPM", True, True, True, False): HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "non", "PompeAPM", True, True, True, False): AnneauDefensifProportionPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "non", "PompeAPM", True, True, True, False): ArmureDefensifProportionPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "non", "PompeAPM", True, True, True, False): HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "non", "PompeAPM", True, True, True, False): AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "non", "PompeAPM", True, True, True, False): ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "non", "PompeAPM", True, True, True, False): HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "non", "PompeAPM", True, True, True, False): AnneauDefensifValeurPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "non", "PompeAPM", True, True, True, False): ArmureDefensifValeurPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "non", "PompeAPM", True, True, True, False): HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, True, True, False): AnneauPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, True, True, False): ArmurePompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, True, True, False): HeaumePompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, True, True, False): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, True, True, False): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, True, True, False): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, True, True, False): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, True, True, False): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, True, True, False): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, True, True, False): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, True, True, False): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, True, True, False): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, True, True, False): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, True, True, False): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, True, True, False): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, True, True, False): AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, True, True, False): ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, True, True, False): HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, True, False): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, True, False): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, True, False): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, True, False): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, True, False): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, True, False): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, True, False): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, True, False): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, True, False): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, True, False): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, True, False): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, True, False): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "non", "RenforceRegenPM", True, True, True, False): AnneauRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "non", "RenforceRegenPM", True, True, True, False): ArmureRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "non", "RenforceRegenPM", True, True, True, False): HeaumeRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, True, True, False): AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, True, True, False): ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, True, True, False): HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, True, True, False): AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, True, True, False): ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, True, True, False): HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, True, True, False): AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, True, True, False): ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, True, True, False): HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, True, True, False): AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, True, True, False): ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, True, True, False): HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, True, True, False): AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, True, True, False): ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, True, True, False): HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, True, False): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaire,
    ("Anneau", "non", "non", "non", False, False, False, True): AnneauTribal,
    ("Armure", "non", "non", "non", False, False, False, True): ArmureTribal,
    ("Heaume", "non", "non", "non", False, False, False, True): HeaumeTribal,
    ("Anneau", "Plafond", "non", "non", False, False, False, True): AnneauDefensifPlafondTribal,
    ("Armure", "Plafond", "non", "non", False, False, False, True): ArmureDefensifPlafondTribal,
    ("Heaume", "Plafond", "non", "non", False, False, False, True): HeaumeDefensifPlafondTribal,
    ("Anneau", "Proportion", "non", "non", False, False, False, True): AnneauDefensifProportionTribal,
    ("Armure", "Proportion", "non", "non", False, False, False, True): ArmureDefensifProportionTribal,
    ("Heaume", "Proportion", "non", "non", False, False, False, True): HeaumeDefensifProportionTribal,
    ("Anneau", "Seuil", "non", "non", False, False, False, True): AnneauDefensifSeuilTribal,
    ("Armure", "Seuil", "non", "non", False, False, False, True): ArmureDefensifSeuilTribal,
    ("Heaume", "Seuil", "non", "non", False, False, False, True): HeaumeDefensifSeuilTribal,
    ("Anneau", "Valeur", "non", "non", False, False, False, True): AnneauDefensifValeurTribal,
    ("Armure", "Valeur", "non", "non", False, False, False, True): ArmureDefensifValeurTribal,
    ("Heaume", "Valeur", "non", "non", False, False, False, True): HeaumeDefensifValeurTribal,
    ("Anneau", "non", "PompeAPV", "non", False, False, False, True): AnneauPompeAPVTribal,
    ("Armure", "non", "PompeAPV", "non", False, False, False, True): ArmurePompeAPVTribal,
    ("Heaume", "non", "PompeAPV", "non", False, False, False, True): HeaumePompeAPVTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", False, False, False, True): AnneauDefensifPlafondPompeAPVTribal,
    ("Armure", "Plafond", "PompeAPV", "non", False, False, False, True): ArmureDefensifPlafondPompeAPVTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", False, False, False, True): HeaumeDefensifPlafondPompeAPVTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", False, False, False, True): AnneauDefensifProportionPompeAPVTribal,
    ("Armure", "Proportion", "PompeAPV", "non", False, False, False, True): ArmureDefensifProportionPompeAPVTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", False, False, False, True): HeaumeDefensifProportionPompeAPVTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", False, False, False, True): AnneauDefensifSeuilPompeAPVTribal,
    ("Armure", "Seuil", "PompeAPV", "non", False, False, False, True): ArmureDefensifSeuilPompeAPVTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", False, False, False, True): HeaumeDefensifSeuilPompeAPVTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", False, False, False, True): AnneauDefensifValeurPompeAPVTribal,
    ("Armure", "Valeur", "PompeAPV", "non", False, False, False, True): ArmureDefensifValeurPompeAPVTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", False, False, False, True): HeaumeDefensifValeurPompeAPVTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", False, False, False, True): AnneauRenforceRegenPVTribal,
    ("Armure", "non", "RenforceRegenPV", "non", False, False, False, True): ArmureRenforceRegenPVTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", False, False, False, True): HeaumeRenforceRegenPVTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, False, False, True): AnneauDefensifPlafondRenforceRegenPVTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, False, False, True): ArmureDefensifPlafondRenforceRegenPVTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, False, False, True): HeaumeDefensifPlafondRenforceRegenPVTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, False, False, True): AnneauDefensifProportionRenforceRegenPVTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, False, False, True): ArmureDefensifProportionRenforceRegenPVTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, False, False, True): HeaumeDefensifProportionRenforceRegenPVTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, False, False, True): AnneauDefensifSeuilRenforceRegenPVTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, False, False, True): ArmureDefensifSeuilRenforceRegenPVTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, False, False, True): HeaumeDefensifSeuilRenforceRegenPVTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, False, False, True): AnneauDefensifValeurRenforceRegenPVTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, False, False, True): ArmureDefensifValeurRenforceRegenPVTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, False, False, True): HeaumeDefensifValeurRenforceRegenPVTribal,
    ("Anneau", "non", "non", "PompeAPM", False, False, False, True): AnneauPompeAPMTribal,
    ("Armure", "non", "non", "PompeAPM", False, False, False, True): ArmurePompeAPMTribal,
    ("Heaume", "non", "non", "PompeAPM", False, False, False, True): HeaumePompeAPMTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", False, False, False, True): AnneauDefensifPlafondPompeAPMTribal,
    ("Armure", "Plafond", "non", "PompeAPM", False, False, False, True): ArmureDefensifPlafondPompeAPMTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", False, False, False, True): HeaumeDefensifPlafondPompeAPMTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", False, False, False, True): AnneauDefensifProportionPompeAPMTribal,
    ("Armure", "Proportion", "non", "PompeAPM", False, False, False, True): ArmureDefensifProportionPompeAPMTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", False, False, False, True): HeaumeDefensifProportionPompeAPMTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", False, False, False, True): AnneauDefensifSeuilPompeAPMTribal,
    ("Armure", "Seuil", "non", "PompeAPM", False, False, False, True): ArmureDefensifSeuilPompeAPMTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", False, False, False, True): HeaumeDefensifSeuilPompeAPMTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", False, False, False, True): AnneauDefensifValeurPompeAPMTribal,
    ("Armure", "Valeur", "non", "PompeAPM", False, False, False, True): ArmureDefensifValeurPompeAPMTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", False, False, False, True): HeaumeDefensifValeurPompeAPMTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, False, False, True): AnneauPompeAPVPompeAPMTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, False, False, True): ArmurePompeAPVPompeAPMTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, False, False, True): HeaumePompeAPVPompeAPMTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, False, False, True): AnneauDefensifPlafondPompeAPVPompeAPMTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, False, False, True): ArmureDefensifPlafondPompeAPVPompeAPMTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, False, False, True): HeaumeDefensifPlafondPompeAPVPompeAPMTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, False, False, True): AnneauDefensifProportionPompeAPVPompeAPMTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, False, False, True): ArmureDefensifProportionPompeAPVPompeAPMTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, False, False, True): HeaumeDefensifProportionPompeAPVPompeAPMTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, False, False, True): AnneauDefensifSeuilPompeAPVPompeAPMTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, False, False, True): ArmureDefensifSeuilPompeAPVPompeAPMTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, False, False, True): HeaumeDefensifSeuilPompeAPVPompeAPMTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, False, False, True): AnneauDefensifValeurPompeAPVPompeAPMTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, False, False, True): ArmureDefensifValeurPompeAPVPompeAPMTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, False, False, True): HeaumeDefensifValeurPompeAPVPompeAPMTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, False, False, True): AnneauRenforceRegenPVPompeAPMTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, False, False, True): ArmureRenforceRegenPVPompeAPMTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, False, False, True): HeaumeRenforceRegenPVPompeAPMTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, False, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, False, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, False, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, False, True): AnneauDefensifProportionRenforceRegenPVPompeAPMTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, False, True): ArmureDefensifProportionRenforceRegenPVPompeAPMTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, False, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, False, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, False, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, False, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, False, True): AnneauDefensifValeurRenforceRegenPVPompeAPMTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, False, True): ArmureDefensifValeurRenforceRegenPVPompeAPMTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, False, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", False, False, False, True): AnneauRenforceRegenPMTribal,
    ("Armure", "non", "non", "RenforceRegenPM", False, False, False, True): ArmureRenforceRegenPMTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", False, False, False, True): HeaumeRenforceRegenPMTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, False, False, True): AnneauDefensifPlafondRenforceRegenPMTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, False, False, True): ArmureDefensifPlafondRenforceRegenPMTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, False, False, True): HeaumeDefensifPlafondRenforceRegenPMTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, False, False, True): AnneauDefensifProportionRenforceRegenPMTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, False, False, True): ArmureDefensifProportionRenforceRegenPMTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, False, False, True): HeaumeDefensifProportionRenforceRegenPMTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, False, False, True): AnneauDefensifSeuilRenforceRegenPMTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, False, False, True): ArmureDefensifSeuilRenforceRegenPMTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, False, False, True): HeaumeDefensifSeuilRenforceRegenPMTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, False, False, True): AnneauDefensifValeurRenforceRegenPMTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, False, False, True): ArmureDefensifValeurRenforceRegenPMTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, False, False, True): HeaumeDefensifValeurRenforceRegenPMTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, False, False, True): AnneauPompeAPVRenforceRegenPMTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, False, False, True): ArmurePompeAPVRenforceRegenPMTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, False, False, True): HeaumePompeAPVRenforceRegenPMTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifProportionPompeAPVRenforceRegenPMTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifProportionPompeAPVRenforceRegenPMTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifValeurPompeAPVRenforceRegenPMTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifValeurPompeAPVRenforceRegenPMTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): AnneauRenforceRegenPVRenforceRegenPMTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): ArmureRenforceRegenPVRenforceRegenPMTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): HeaumeRenforceRegenPVRenforceRegenPMTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, False, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMTribal,
    ("Anneau", "non", "non", "non", True, False, False, True): AnneauAccelerateurTribal,
    ("Armure", "non", "non", "non", True, False, False, True): ArmureAccelerateurTribal,
    ("Heaume", "non", "non", "non", True, False, False, True): HeaumeAccelerateurTribal,
    ("Anneau", "Plafond", "non", "non", True, False, False, True): AnneauDefensifPlafondAccelerateurTribal,
    ("Armure", "Plafond", "non", "non", True, False, False, True): ArmureDefensifPlafondAccelerateurTribal,
    ("Heaume", "Plafond", "non", "non", True, False, False, True): HeaumeDefensifPlafondAccelerateurTribal,
    ("Anneau", "Proportion", "non", "non", True, False, False, True): AnneauDefensifProportionAccelerateurTribal,
    ("Armure", "Proportion", "non", "non", True, False, False, True): ArmureDefensifProportionAccelerateurTribal,
    ("Heaume", "Proportion", "non", "non", True, False, False, True): HeaumeDefensifProportionAccelerateurTribal,
    ("Anneau", "Seuil", "non", "non", True, False, False, True): AnneauDefensifSeuilAccelerateurTribal,
    ("Armure", "Seuil", "non", "non", True, False, False, True): ArmureDefensifSeuilAccelerateurTribal,
    ("Heaume", "Seuil", "non", "non", True, False, False, True): HeaumeDefensifSeuilAccelerateurTribal,
    ("Anneau", "Valeur", "non", "non", True, False, False, True): AnneauDefensifValeurAccelerateurTribal,
    ("Armure", "Valeur", "non", "non", True, False, False, True): ArmureDefensifValeurAccelerateurTribal,
    ("Heaume", "Valeur", "non", "non", True, False, False, True): HeaumeDefensifValeurAccelerateurTribal,
    ("Anneau", "non", "PompeAPV", "non", True, False, False, True): AnneauPompeAPVAccelerateurTribal,
    ("Armure", "non", "PompeAPV", "non", True, False, False, True): ArmurePompeAPVAccelerateurTribal,
    ("Heaume", "non", "PompeAPV", "non", True, False, False, True): HeaumePompeAPVAccelerateurTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", True, False, False, True): AnneauDefensifPlafondPompeAPVAccelerateurTribal,
    ("Armure", "Plafond", "PompeAPV", "non", True, False, False, True): ArmureDefensifPlafondPompeAPVAccelerateurTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", True, False, False, True): HeaumeDefensifPlafondPompeAPVAccelerateurTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", True, False, False, True): AnneauDefensifProportionPompeAPVAccelerateurTribal,
    ("Armure", "Proportion", "PompeAPV", "non", True, False, False, True): ArmureDefensifProportionPompeAPVAccelerateurTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", True, False, False, True): HeaumeDefensifProportionPompeAPVAccelerateurTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", True, False, False, True): AnneauDefensifSeuilPompeAPVAccelerateurTribal,
    ("Armure", "Seuil", "PompeAPV", "non", True, False, False, True): ArmureDefensifSeuilPompeAPVAccelerateurTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", True, False, False, True): HeaumeDefensifSeuilPompeAPVAccelerateurTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", True, False, False, True): AnneauDefensifValeurPompeAPVAccelerateurTribal,
    ("Armure", "Valeur", "PompeAPV", "non", True, False, False, True): ArmureDefensifValeurPompeAPVAccelerateurTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", True, False, False, True): HeaumeDefensifValeurPompeAPVAccelerateurTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", True, False, False, True): AnneauRenforceRegenPVAccelerateurTribal,
    ("Armure", "non", "RenforceRegenPV", "non", True, False, False, True): ArmureRenforceRegenPVAccelerateurTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", True, False, False, True): HeaumeRenforceRegenPVAccelerateurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, False, False, True): AnneauDefensifPlafondRenforceRegenPVAccelerateurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, False, False, True): ArmureDefensifPlafondRenforceRegenPVAccelerateurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, False, False, True): HeaumeDefensifPlafondRenforceRegenPVAccelerateurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, False, False, True): AnneauDefensifProportionRenforceRegenPVAccelerateurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, False, False, True): ArmureDefensifProportionRenforceRegenPVAccelerateurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, False, False, True): HeaumeDefensifProportionRenforceRegenPVAccelerateurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, False, False, True): AnneauDefensifSeuilRenforceRegenPVAccelerateurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, False, False, True): ArmureDefensifSeuilRenforceRegenPVAccelerateurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, False, False, True): HeaumeDefensifSeuilRenforceRegenPVAccelerateurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, False, False, True): AnneauDefensifValeurRenforceRegenPVAccelerateurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, False, False, True): ArmureDefensifValeurRenforceRegenPVAccelerateurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, False, False, True): HeaumeDefensifValeurRenforceRegenPVAccelerateurTribal,
    ("Anneau", "non", "non", "PompeAPM", True, False, False, True): AnneauPompeAPMAccelerateurTribal,
    ("Armure", "non", "non", "PompeAPM", True, False, False, True): ArmurePompeAPMAccelerateurTribal,
    ("Heaume", "non", "non", "PompeAPM", True, False, False, True): HeaumePompeAPMAccelerateurTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", True, False, False, True): AnneauDefensifPlafondPompeAPMAccelerateurTribal,
    ("Armure", "Plafond", "non", "PompeAPM", True, False, False, True): ArmureDefensifPlafondPompeAPMAccelerateurTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", True, False, False, True): HeaumeDefensifPlafondPompeAPMAccelerateurTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", True, False, False, True): AnneauDefensifProportionPompeAPMAccelerateurTribal,
    ("Armure", "Proportion", "non", "PompeAPM", True, False, False, True): ArmureDefensifProportionPompeAPMAccelerateurTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", True, False, False, True): HeaumeDefensifProportionPompeAPMAccelerateurTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", True, False, False, True): AnneauDefensifSeuilPompeAPMAccelerateurTribal,
    ("Armure", "Seuil", "non", "PompeAPM", True, False, False, True): ArmureDefensifSeuilPompeAPMAccelerateurTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", True, False, False, True): HeaumeDefensifSeuilPompeAPMAccelerateurTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", True, False, False, True): AnneauDefensifValeurPompeAPMAccelerateurTribal,
    ("Armure", "Valeur", "non", "PompeAPM", True, False, False, True): ArmureDefensifValeurPompeAPMAccelerateurTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", True, False, False, True): HeaumeDefensifValeurPompeAPMAccelerateurTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, False, False, True): AnneauPompeAPVPompeAPMAccelerateurTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, False, False, True): ArmurePompeAPVPompeAPMAccelerateurTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, False, False, True): HeaumePompeAPVPompeAPMAccelerateurTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, False, False, True): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, False, False, True): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, False, False, True): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, False, False, True): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, False, False, True): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, False, False, True): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, False, False, True): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, False, False, True): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, False, False, True): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, False, False, True): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, False, False, True): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, False, False, True): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, False, False, True): AnneauRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, False, False, True): ArmureRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, False, False, True): HeaumeRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, False, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, False, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, False, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, False, True): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, False, True): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, False, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, False, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, False, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, False, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, False, True): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, False, True): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, False, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", True, False, False, True): AnneauRenforceRegenPMAccelerateurTribal,
    ("Armure", "non", "non", "RenforceRegenPM", True, False, False, True): ArmureRenforceRegenPMAccelerateurTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", True, False, False, True): HeaumeRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, False, False, True): AnneauDefensifPlafondRenforceRegenPMAccelerateurTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, False, False, True): ArmureDefensifPlafondRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, False, False, True): HeaumeDefensifPlafondRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, False, False, True): AnneauDefensifProportionRenforceRegenPMAccelerateurTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, False, False, True): ArmureDefensifProportionRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, False, False, True): HeaumeDefensifProportionRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, False, False, True): AnneauDefensifSeuilRenforceRegenPMAccelerateurTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, False, False, True): ArmureDefensifSeuilRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, False, False, True): HeaumeDefensifSeuilRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, False, False, True): AnneauDefensifValeurRenforceRegenPMAccelerateurTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, False, False, True): ArmureDefensifValeurRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, False, False, True): HeaumeDefensifValeurRenforceRegenPMAccelerateurTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, False, False, True): AnneauPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, False, False, True): ArmurePompeAPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, False, False, True): HeaumePompeAPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): AnneauRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): ArmureRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, False, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurTribal,
    ("Anneau", "non", "non", "non", False, True, False, True): AnneauAnoblisseurTribal,
    ("Armure", "non", "non", "non", False, True, False, True): ArmureAnoblisseurTribal,
    ("Heaume", "non", "non", "non", False, True, False, True): HeaumeAnoblisseurTribal,
    ("Anneau", "Plafond", "non", "non", False, True, False, True): AnneauDefensifPlafondAnoblisseurTribal,
    ("Armure", "Plafond", "non", "non", False, True, False, True): ArmureDefensifPlafondAnoblisseurTribal,
    ("Heaume", "Plafond", "non", "non", False, True, False, True): HeaumeDefensifPlafondAnoblisseurTribal,
    ("Anneau", "Proportion", "non", "non", False, True, False, True): AnneauDefensifProportionAnoblisseurTribal,
    ("Armure", "Proportion", "non", "non", False, True, False, True): ArmureDefensifProportionAnoblisseurTribal,
    ("Heaume", "Proportion", "non", "non", False, True, False, True): HeaumeDefensifProportionAnoblisseurTribal,
    ("Anneau", "Seuil", "non", "non", False, True, False, True): AnneauDefensifSeuilAnoblisseurTribal,
    ("Armure", "Seuil", "non", "non", False, True, False, True): ArmureDefensifSeuilAnoblisseurTribal,
    ("Heaume", "Seuil", "non", "non", False, True, False, True): HeaumeDefensifSeuilAnoblisseurTribal,
    ("Anneau", "Valeur", "non", "non", False, True, False, True): AnneauDefensifValeurAnoblisseurTribal,
    ("Armure", "Valeur", "non", "non", False, True, False, True): ArmureDefensifValeurAnoblisseurTribal,
    ("Heaume", "Valeur", "non", "non", False, True, False, True): HeaumeDefensifValeurAnoblisseurTribal,
    ("Anneau", "non", "PompeAPV", "non", False, True, False, True): AnneauPompeAPVAnoblisseurTribal,
    ("Armure", "non", "PompeAPV", "non", False, True, False, True): ArmurePompeAPVAnoblisseurTribal,
    ("Heaume", "non", "PompeAPV", "non", False, True, False, True): HeaumePompeAPVAnoblisseurTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", False, True, False, True): AnneauDefensifPlafondPompeAPVAnoblisseurTribal,
    ("Armure", "Plafond", "PompeAPV", "non", False, True, False, True): ArmureDefensifPlafondPompeAPVAnoblisseurTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", False, True, False, True): HeaumeDefensifPlafondPompeAPVAnoblisseurTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", False, True, False, True): AnneauDefensifProportionPompeAPVAnoblisseurTribal,
    ("Armure", "Proportion", "PompeAPV", "non", False, True, False, True): ArmureDefensifProportionPompeAPVAnoblisseurTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", False, True, False, True): HeaumeDefensifProportionPompeAPVAnoblisseurTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", False, True, False, True): AnneauDefensifSeuilPompeAPVAnoblisseurTribal,
    ("Armure", "Seuil", "PompeAPV", "non", False, True, False, True): ArmureDefensifSeuilPompeAPVAnoblisseurTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", False, True, False, True): HeaumeDefensifSeuilPompeAPVAnoblisseurTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", False, True, False, True): AnneauDefensifValeurPompeAPVAnoblisseurTribal,
    ("Armure", "Valeur", "PompeAPV", "non", False, True, False, True): ArmureDefensifValeurPompeAPVAnoblisseurTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", False, True, False, True): HeaumeDefensifValeurPompeAPVAnoblisseurTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", False, True, False, True): AnneauRenforceRegenPVAnoblisseurTribal,
    ("Armure", "non", "RenforceRegenPV", "non", False, True, False, True): ArmureRenforceRegenPVAnoblisseurTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", False, True, False, True): HeaumeRenforceRegenPVAnoblisseurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, True, False, True): AnneauDefensifPlafondRenforceRegenPVAnoblisseurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, True, False, True): ArmureDefensifPlafondRenforceRegenPVAnoblisseurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, True, False, True): HeaumeDefensifPlafondRenforceRegenPVAnoblisseurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, True, False, True): AnneauDefensifProportionRenforceRegenPVAnoblisseurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, True, False, True): ArmureDefensifProportionRenforceRegenPVAnoblisseurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, True, False, True): HeaumeDefensifProportionRenforceRegenPVAnoblisseurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, True, False, True): AnneauDefensifSeuilRenforceRegenPVAnoblisseurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, True, False, True): ArmureDefensifSeuilRenforceRegenPVAnoblisseurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, True, False, True): HeaumeDefensifSeuilRenforceRegenPVAnoblisseurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, True, False, True): AnneauDefensifValeurRenforceRegenPVAnoblisseurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, True, False, True): ArmureDefensifValeurRenforceRegenPVAnoblisseurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, True, False, True): HeaumeDefensifValeurRenforceRegenPVAnoblisseurTribal,
    ("Anneau", "non", "non", "PompeAPM", False, True, False, True): AnneauPompeAPMAnoblisseurTribal,
    ("Armure", "non", "non", "PompeAPM", False, True, False, True): ArmurePompeAPMAnoblisseurTribal,
    ("Heaume", "non", "non", "PompeAPM", False, True, False, True): HeaumePompeAPMAnoblisseurTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", False, True, False, True): AnneauDefensifPlafondPompeAPMAnoblisseurTribal,
    ("Armure", "Plafond", "non", "PompeAPM", False, True, False, True): ArmureDefensifPlafondPompeAPMAnoblisseurTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", False, True, False, True): HeaumeDefensifPlafondPompeAPMAnoblisseurTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", False, True, False, True): AnneauDefensifProportionPompeAPMAnoblisseurTribal,
    ("Armure", "Proportion", "non", "PompeAPM", False, True, False, True): ArmureDefensifProportionPompeAPMAnoblisseurTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", False, True, False, True): HeaumeDefensifProportionPompeAPMAnoblisseurTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", False, True, False, True): AnneauDefensifSeuilPompeAPMAnoblisseurTribal,
    ("Armure", "Seuil", "non", "PompeAPM", False, True, False, True): ArmureDefensifSeuilPompeAPMAnoblisseurTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", False, True, False, True): HeaumeDefensifSeuilPompeAPMAnoblisseurTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", False, True, False, True): AnneauDefensifValeurPompeAPMAnoblisseurTribal,
    ("Armure", "Valeur", "non", "PompeAPM", False, True, False, True): ArmureDefensifValeurPompeAPMAnoblisseurTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", False, True, False, True): HeaumeDefensifValeurPompeAPMAnoblisseurTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, True, False, True): AnneauPompeAPVPompeAPMAnoblisseurTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, True, False, True): ArmurePompeAPVPompeAPMAnoblisseurTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, True, False, True): HeaumePompeAPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, True, False, True): AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseurTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, True, False, True): ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, True, False, True): HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, True, False, True): AnneauDefensifProportionPompeAPVPompeAPMAnoblisseurTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, True, False, True): ArmureDefensifProportionPompeAPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, True, False, True): HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, True, False, True): AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseurTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, True, False, True): ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, True, False, True): HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, True, False, True): AnneauDefensifValeurPompeAPVPompeAPMAnoblisseurTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, True, False, True): ArmureDefensifValeurPompeAPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, True, False, True): HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseurTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, True, False, True): AnneauRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, True, False, True): ArmureRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, True, False, True): HeaumeRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, False, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, False, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, False, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, False, True): AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, False, True): ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, False, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, False, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, False, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, False, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, False, True): AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, False, True): ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, False, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseurTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", False, True, False, True): AnneauRenforceRegenPMAnoblisseurTribal,
    ("Armure", "non", "non", "RenforceRegenPM", False, True, False, True): ArmureRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", False, True, False, True): HeaumeRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, True, False, True): AnneauDefensifPlafondRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, True, False, True): ArmureDefensifPlafondRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, True, False, True): HeaumeDefensifPlafondRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, True, False, True): AnneauDefensifProportionRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, True, False, True): ArmureDefensifProportionRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, True, False, True): HeaumeDefensifProportionRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, True, False, True): AnneauDefensifSeuilRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, True, False, True): ArmureDefensifSeuilRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, True, False, True): HeaumeDefensifSeuilRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, True, False, True): AnneauDefensifValeurRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, True, False, True): ArmureDefensifValeurRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, True, False, True): HeaumeDefensifValeurRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, True, False, True): AnneauPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, True, False, True): ArmurePompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, True, False, True): HeaumePompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): AnneauRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): ArmureRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): HeaumeRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, False, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurTribal,
    ("Anneau", "non", "non", "non", True, True, False, True): AnneauAccelerateurAnoblisseurTribal,
    ("Armure", "non", "non", "non", True, True, False, True): ArmureAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "non", "non", True, True, False, True): HeaumeAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "non", "non", True, True, False, True): AnneauDefensifPlafondAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "non", "non", True, True, False, True): ArmureDefensifPlafondAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "non", "non", True, True, False, True): HeaumeDefensifPlafondAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "non", "non", True, True, False, True): AnneauDefensifProportionAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "non", "non", True, True, False, True): ArmureDefensifProportionAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "non", "non", True, True, False, True): HeaumeDefensifProportionAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "non", "non", True, True, False, True): AnneauDefensifSeuilAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "non", "non", True, True, False, True): ArmureDefensifSeuilAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "non", "non", True, True, False, True): HeaumeDefensifSeuilAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "non", "non", True, True, False, True): AnneauDefensifValeurAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "non", "non", True, True, False, True): ArmureDefensifValeurAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "non", "non", True, True, False, True): HeaumeDefensifValeurAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "PompeAPV", "non", True, True, False, True): AnneauPompeAPVAccelerateurAnoblisseurTribal,
    ("Armure", "non", "PompeAPV", "non", True, True, False, True): ArmurePompeAPVAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "PompeAPV", "non", True, True, False, True): HeaumePompeAPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", True, True, False, True): AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "PompeAPV", "non", True, True, False, True): ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", True, True, False, True): HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", True, True, False, True): AnneauDefensifProportionPompeAPVAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "PompeAPV", "non", True, True, False, True): ArmureDefensifProportionPompeAPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", True, True, False, True): HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", True, True, False, True): AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "PompeAPV", "non", True, True, False, True): ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", True, True, False, True): HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", True, True, False, True): AnneauDefensifValeurPompeAPVAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "PompeAPV", "non", True, True, False, True): ArmureDefensifValeurPompeAPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", True, True, False, True): HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", True, True, False, True): AnneauRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Armure", "non", "RenforceRegenPV", "non", True, True, False, True): ArmureRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", True, True, False, True): HeaumeRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, True, False, True): AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, True, False, True): ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, True, False, True): HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, True, False, True): AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, True, False, True): ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, True, False, True): HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, True, False, True): AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, True, False, True): ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, True, False, True): HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, True, False, True): AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, True, False, True): ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, True, False, True): HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "non", "PompeAPM", True, True, False, True): AnneauPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "non", "non", "PompeAPM", True, True, False, True): ArmurePompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "non", "PompeAPM", True, True, False, True): HeaumePompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", True, True, False, True): AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "non", "PompeAPM", True, True, False, True): ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", True, True, False, True): HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", True, True, False, True): AnneauDefensifProportionPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "non", "PompeAPM", True, True, False, True): ArmureDefensifProportionPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", True, True, False, True): HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", True, True, False, True): AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "non", "PompeAPM", True, True, False, True): ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", True, True, False, True): HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", True, True, False, True): AnneauDefensifValeurPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "non", "PompeAPM", True, True, False, True): ArmureDefensifValeurPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", True, True, False, True): HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, True, False, True): AnneauPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, True, False, True): ArmurePompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, True, False, True): HeaumePompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, True, False, True): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, True, False, True): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, True, False, True): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, True, False, True): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, True, False, True): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, True, False, True): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, True, False, True): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, True, False, True): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, True, False, True): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, True, False, True): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, True, False, True): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, True, False, True): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, True, False, True): AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, True, False, True): ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, True, False, True): HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, False, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, False, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, False, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, False, True): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, False, True): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, False, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, False, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, False, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, False, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, False, True): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, False, True): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, False, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", True, True, False, True): AnneauRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "non", "non", "RenforceRegenPM", True, True, False, True): ArmureRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", True, True, False, True): HeaumeRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, True, False, True): AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, True, False, True): ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, True, False, True): HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, True, False, True): AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, True, False, True): ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, True, False, True): HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, True, False, True): AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, True, False, True): ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, True, False, True): HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, True, False, True): AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, True, False, True): ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, True, False, True): HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, True, False, True): AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, True, False, True): ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, True, False, True): HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, False, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurTribal,
    ("Anneau", "non", "non", "non", False, False, True, True): AnneauElementaireTribal,
    ("Armure", "non", "non", "non", False, False, True, True): ArmureElementaireTribal,
    ("Heaume", "non", "non", "non", False, False, True, True): HeaumeElementaireTribal,
    ("Anneau", "Plafond", "non", "non", False, False, True, True): AnneauDefensifPlafondElementaireTribal,
    ("Armure", "Plafond", "non", "non", False, False, True, True): ArmureDefensifPlafondElementaireTribal,
    ("Heaume", "Plafond", "non", "non", False, False, True, True): HeaumeDefensifPlafondElementaireTribal,
    ("Anneau", "Proportion", "non", "non", False, False, True, True): AnneauDefensifProportionElementaireTribal,
    ("Armure", "Proportion", "non", "non", False, False, True, True): ArmureDefensifProportionElementaireTribal,
    ("Heaume", "Proportion", "non", "non", False, False, True, True): HeaumeDefensifProportionElementaireTribal,
    ("Anneau", "Seuil", "non", "non", False, False, True, True): AnneauDefensifSeuilElementaireTribal,
    ("Armure", "Seuil", "non", "non", False, False, True, True): ArmureDefensifSeuilElementaireTribal,
    ("Heaume", "Seuil", "non", "non", False, False, True, True): HeaumeDefensifSeuilElementaireTribal,
    ("Anneau", "Valeur", "non", "non", False, False, True, True): AnneauDefensifValeurElementaireTribal,
    ("Armure", "Valeur", "non", "non", False, False, True, True): ArmureDefensifValeurElementaireTribal,
    ("Heaume", "Valeur", "non", "non", False, False, True, True): HeaumeDefensifValeurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "non", False, False, True, True): AnneauPompeAPVElementaireTribal,
    ("Armure", "non", "PompeAPV", "non", False, False, True, True): ArmurePompeAPVElementaireTribal,
    ("Heaume", "non", "PompeAPV", "non", False, False, True, True): HeaumePompeAPVElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", False, False, True, True): AnneauDefensifPlafondPompeAPVElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "non", False, False, True, True): ArmureDefensifPlafondPompeAPVElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", False, False, True, True): HeaumeDefensifPlafondPompeAPVElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", False, False, True, True): AnneauDefensifProportionPompeAPVElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "non", False, False, True, True): ArmureDefensifProportionPompeAPVElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", False, False, True, True): HeaumeDefensifProportionPompeAPVElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", False, False, True, True): AnneauDefensifSeuilPompeAPVElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "non", False, False, True, True): ArmureDefensifSeuilPompeAPVElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", False, False, True, True): HeaumeDefensifSeuilPompeAPVElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", False, False, True, True): AnneauDefensifValeurPompeAPVElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "non", False, False, True, True): ArmureDefensifValeurPompeAPVElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", False, False, True, True): HeaumeDefensifValeurPompeAPVElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", False, False, True, True): AnneauRenforceRegenPVElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "non", False, False, True, True): ArmureRenforceRegenPVElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", False, False, True, True): HeaumeRenforceRegenPVElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, False, True, True): AnneauDefensifPlafondRenforceRegenPVElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, False, True, True): ArmureDefensifPlafondRenforceRegenPVElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, False, True, True): HeaumeDefensifPlafondRenforceRegenPVElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, False, True, True): AnneauDefensifProportionRenforceRegenPVElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, False, True, True): ArmureDefensifProportionRenforceRegenPVElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, False, True, True): HeaumeDefensifProportionRenforceRegenPVElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, False, True, True): AnneauDefensifSeuilRenforceRegenPVElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, False, True, True): ArmureDefensifSeuilRenforceRegenPVElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, False, True, True): HeaumeDefensifSeuilRenforceRegenPVElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, False, True, True): AnneauDefensifValeurRenforceRegenPVElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, False, True, True): ArmureDefensifValeurRenforceRegenPVElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, False, True, True): HeaumeDefensifValeurRenforceRegenPVElementaireTribal,
    ("Anneau", "non", "non", "PompeAPM", False, False, True, True): AnneauPompeAPMElementaireTribal,
    ("Armure", "non", "non", "PompeAPM", False, False, True, True): ArmurePompeAPMElementaireTribal,
    ("Heaume", "non", "non", "PompeAPM", False, False, True, True): HeaumePompeAPMElementaireTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", False, False, True, True): AnneauDefensifPlafondPompeAPMElementaireTribal,
    ("Armure", "Plafond", "non", "PompeAPM", False, False, True, True): ArmureDefensifPlafondPompeAPMElementaireTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", False, False, True, True): HeaumeDefensifPlafondPompeAPMElementaireTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", False, False, True, True): AnneauDefensifProportionPompeAPMElementaireTribal,
    ("Armure", "Proportion", "non", "PompeAPM", False, False, True, True): ArmureDefensifProportionPompeAPMElementaireTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", False, False, True, True): HeaumeDefensifProportionPompeAPMElementaireTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", False, False, True, True): AnneauDefensifSeuilPompeAPMElementaireTribal,
    ("Armure", "Seuil", "non", "PompeAPM", False, False, True, True): ArmureDefensifSeuilPompeAPMElementaireTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", False, False, True, True): HeaumeDefensifSeuilPompeAPMElementaireTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", False, False, True, True): AnneauDefensifValeurPompeAPMElementaireTribal,
    ("Armure", "Valeur", "non", "PompeAPM", False, False, True, True): ArmureDefensifValeurPompeAPMElementaireTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", False, False, True, True): HeaumeDefensifValeurPompeAPMElementaireTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, False, True, True): AnneauPompeAPVPompeAPMElementaireTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, False, True, True): ArmurePompeAPVPompeAPMElementaireTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, False, True, True): HeaumePompeAPVPompeAPMElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, False, True, True): AnneauDefensifPlafondPompeAPVPompeAPMElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, False, True, True): ArmureDefensifPlafondPompeAPVPompeAPMElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, False, True, True): HeaumeDefensifPlafondPompeAPVPompeAPMElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, False, True, True): AnneauDefensifProportionPompeAPVPompeAPMElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, False, True, True): ArmureDefensifProportionPompeAPVPompeAPMElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, False, True, True): HeaumeDefensifProportionPompeAPVPompeAPMElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, False, True, True): AnneauDefensifSeuilPompeAPVPompeAPMElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, False, True, True): ArmureDefensifSeuilPompeAPVPompeAPMElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, False, True, True): HeaumeDefensifSeuilPompeAPVPompeAPMElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, False, True, True): AnneauDefensifValeurPompeAPVPompeAPMElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, False, True, True): ArmureDefensifValeurPompeAPVPompeAPMElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, False, True, True): HeaumeDefensifValeurPompeAPVPompeAPMElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, False, True, True): AnneauRenforceRegenPVPompeAPMElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, False, True, True): ArmureRenforceRegenPVPompeAPMElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, False, True, True): HeaumeRenforceRegenPVPompeAPMElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, True, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, True, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, False, True, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, True, True): AnneauDefensifProportionRenforceRegenPVPompeAPMElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, True, True): ArmureDefensifProportionRenforceRegenPVPompeAPMElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, False, True, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, True, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, True, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, False, True, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, True, True): AnneauDefensifValeurRenforceRegenPVPompeAPMElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, True, True): ArmureDefensifValeurRenforceRegenPVPompeAPMElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, False, True, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMElementaireTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", False, False, True, True): AnneauRenforceRegenPMElementaireTribal,
    ("Armure", "non", "non", "RenforceRegenPM", False, False, True, True): ArmureRenforceRegenPMElementaireTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", False, False, True, True): HeaumeRenforceRegenPMElementaireTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, False, True, True): AnneauDefensifPlafondRenforceRegenPMElementaireTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, False, True, True): ArmureDefensifPlafondRenforceRegenPMElementaireTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, False, True, True): HeaumeDefensifPlafondRenforceRegenPMElementaireTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, False, True, True): AnneauDefensifProportionRenforceRegenPMElementaireTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, False, True, True): ArmureDefensifProportionRenforceRegenPMElementaireTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, False, True, True): HeaumeDefensifProportionRenforceRegenPMElementaireTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, False, True, True): AnneauDefensifSeuilRenforceRegenPMElementaireTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, False, True, True): ArmureDefensifSeuilRenforceRegenPMElementaireTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, False, True, True): HeaumeDefensifSeuilRenforceRegenPMElementaireTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, False, True, True): AnneauDefensifValeurRenforceRegenPMElementaireTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, False, True, True): ArmureDefensifValeurRenforceRegenPMElementaireTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, False, True, True): HeaumeDefensifValeurRenforceRegenPMElementaireTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, False, True, True): AnneauPompeAPVRenforceRegenPMElementaireTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, False, True, True): ArmurePompeAPVRenforceRegenPMElementaireTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, False, True, True): HeaumePompeAPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifProportionPompeAPVRenforceRegenPMElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifProportionPompeAPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifValeurPompeAPVRenforceRegenPMElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifValeurPompeAPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): AnneauRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): ArmureRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): HeaumeRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, False, True, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMElementaireTribal,
    ("Anneau", "non", "non", "non", True, False, True, True): AnneauAccelerateurElementaireTribal,
    ("Armure", "non", "non", "non", True, False, True, True): ArmureAccelerateurElementaireTribal,
    ("Heaume", "non", "non", "non", True, False, True, True): HeaumeAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "non", "non", True, False, True, True): AnneauDefensifPlafondAccelerateurElementaireTribal,
    ("Armure", "Plafond", "non", "non", True, False, True, True): ArmureDefensifPlafondAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "non", "non", True, False, True, True): HeaumeDefensifPlafondAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "non", "non", True, False, True, True): AnneauDefensifProportionAccelerateurElementaireTribal,
    ("Armure", "Proportion", "non", "non", True, False, True, True): ArmureDefensifProportionAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "non", "non", True, False, True, True): HeaumeDefensifProportionAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "non", "non", True, False, True, True): AnneauDefensifSeuilAccelerateurElementaireTribal,
    ("Armure", "Seuil", "non", "non", True, False, True, True): ArmureDefensifSeuilAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "non", "non", True, False, True, True): HeaumeDefensifSeuilAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "non", "non", True, False, True, True): AnneauDefensifValeurAccelerateurElementaireTribal,
    ("Armure", "Valeur", "non", "non", True, False, True, True): ArmureDefensifValeurAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "non", "non", True, False, True, True): HeaumeDefensifValeurAccelerateurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "non", True, False, True, True): AnneauPompeAPVAccelerateurElementaireTribal,
    ("Armure", "non", "PompeAPV", "non", True, False, True, True): ArmurePompeAPVAccelerateurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "non", True, False, True, True): HeaumePompeAPVAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", True, False, True, True): AnneauDefensifPlafondPompeAPVAccelerateurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "non", True, False, True, True): ArmureDefensifPlafondPompeAPVAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", True, False, True, True): HeaumeDefensifPlafondPompeAPVAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", True, False, True, True): AnneauDefensifProportionPompeAPVAccelerateurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "non", True, False, True, True): ArmureDefensifProportionPompeAPVAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", True, False, True, True): HeaumeDefensifProportionPompeAPVAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", True, False, True, True): AnneauDefensifSeuilPompeAPVAccelerateurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "non", True, False, True, True): ArmureDefensifSeuilPompeAPVAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", True, False, True, True): HeaumeDefensifSeuilPompeAPVAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", True, False, True, True): AnneauDefensifValeurPompeAPVAccelerateurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "non", True, False, True, True): ArmureDefensifValeurPompeAPVAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", True, False, True, True): HeaumeDefensifValeurPompeAPVAccelerateurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", True, False, True, True): AnneauRenforceRegenPVAccelerateurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "non", True, False, True, True): ArmureRenforceRegenPVAccelerateurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", True, False, True, True): HeaumeRenforceRegenPVAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, False, True, True): AnneauDefensifPlafondRenforceRegenPVAccelerateurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, False, True, True): ArmureDefensifPlafondRenforceRegenPVAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, False, True, True): HeaumeDefensifPlafondRenforceRegenPVAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, False, True, True): AnneauDefensifProportionRenforceRegenPVAccelerateurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, False, True, True): ArmureDefensifProportionRenforceRegenPVAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, False, True, True): HeaumeDefensifProportionRenforceRegenPVAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, False, True, True): AnneauDefensifSeuilRenforceRegenPVAccelerateurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, False, True, True): ArmureDefensifSeuilRenforceRegenPVAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, False, True, True): HeaumeDefensifSeuilRenforceRegenPVAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, False, True, True): AnneauDefensifValeurRenforceRegenPVAccelerateurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, False, True, True): ArmureDefensifValeurRenforceRegenPVAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, False, True, True): HeaumeDefensifValeurRenforceRegenPVAccelerateurElementaireTribal,
    ("Anneau", "non", "non", "PompeAPM", True, False, True, True): AnneauPompeAPMAccelerateurElementaireTribal,
    ("Armure", "non", "non", "PompeAPM", True, False, True, True): ArmurePompeAPMAccelerateurElementaireTribal,
    ("Heaume", "non", "non", "PompeAPM", True, False, True, True): HeaumePompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", True, False, True, True): AnneauDefensifPlafondPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Plafond", "non", "PompeAPM", True, False, True, True): ArmureDefensifPlafondPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", True, False, True, True): HeaumeDefensifPlafondPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", True, False, True, True): AnneauDefensifProportionPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Proportion", "non", "PompeAPM", True, False, True, True): ArmureDefensifProportionPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", True, False, True, True): HeaumeDefensifProportionPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", True, False, True, True): AnneauDefensifSeuilPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Seuil", "non", "PompeAPM", True, False, True, True): ArmureDefensifSeuilPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", True, False, True, True): HeaumeDefensifSeuilPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", True, False, True, True): AnneauDefensifValeurPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Valeur", "non", "PompeAPM", True, False, True, True): ArmureDefensifValeurPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", True, False, True, True): HeaumeDefensifValeurPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, False, True, True): AnneauPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, False, True, True): ArmurePompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, False, True, True): HeaumePompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, False, True, True): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, False, True, True): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, False, True, True): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, False, True, True): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, False, True, True): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, False, True, True): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, False, True, True): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, False, True, True): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, False, True, True): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, False, True, True): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, False, True, True): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, False, True, True): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, False, True, True): AnneauRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, False, True, True): ArmureRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, False, True, True): HeaumeRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, True, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, True, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, False, True, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, True, True): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, True, True): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, False, True, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, True, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, True, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, False, True, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, True, True): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, True, True): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, False, True, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurElementaireTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", True, False, True, True): AnneauRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "non", "non", "RenforceRegenPM", True, False, True, True): ArmureRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", True, False, True, True): HeaumeRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, False, True, True): AnneauDefensifPlafondRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, False, True, True): ArmureDefensifPlafondRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, False, True, True): HeaumeDefensifPlafondRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, False, True, True): AnneauDefensifProportionRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, False, True, True): ArmureDefensifProportionRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, False, True, True): HeaumeDefensifProportionRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, False, True, True): AnneauDefensifSeuilRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, False, True, True): ArmureDefensifSeuilRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, False, True, True): HeaumeDefensifSeuilRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, False, True, True): AnneauDefensifValeurRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, False, True, True): ArmureDefensifValeurRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, False, True, True): HeaumeDefensifValeurRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, False, True, True): AnneauPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, False, True, True): ArmurePompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, False, True, True): HeaumePompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): AnneauRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): ArmureRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, False, True, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurElementaireTribal,
    ("Anneau", "non", "non", "non", False, True, True, True): AnneauAnoblisseurElementaireTribal,
    ("Armure", "non", "non", "non", False, True, True, True): ArmureAnoblisseurElementaireTribal,
    ("Heaume", "non", "non", "non", False, True, True, True): HeaumeAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "non", "non", False, True, True, True): AnneauDefensifPlafondAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "non", "non", False, True, True, True): ArmureDefensifPlafondAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "non", "non", False, True, True, True): HeaumeDefensifPlafondAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "non", "non", False, True, True, True): AnneauDefensifProportionAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "non", "non", False, True, True, True): ArmureDefensifProportionAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "non", "non", False, True, True, True): HeaumeDefensifProportionAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "non", "non", False, True, True, True): AnneauDefensifSeuilAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "non", "non", False, True, True, True): ArmureDefensifSeuilAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "non", "non", False, True, True, True): HeaumeDefensifSeuilAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "non", "non", False, True, True, True): AnneauDefensifValeurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "non", "non", False, True, True, True): ArmureDefensifValeurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "non", "non", False, True, True, True): HeaumeDefensifValeurAnoblisseurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "non", False, True, True, True): AnneauPompeAPVAnoblisseurElementaireTribal,
    ("Armure", "non", "PompeAPV", "non", False, True, True, True): ArmurePompeAPVAnoblisseurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "non", False, True, True, True): HeaumePompeAPVAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", False, True, True, True): AnneauDefensifPlafondPompeAPVAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "non", False, True, True, True): ArmureDefensifPlafondPompeAPVAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", False, True, True, True): HeaumeDefensifPlafondPompeAPVAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", False, True, True, True): AnneauDefensifProportionPompeAPVAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "non", False, True, True, True): ArmureDefensifProportionPompeAPVAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", False, True, True, True): HeaumeDefensifProportionPompeAPVAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", False, True, True, True): AnneauDefensifSeuilPompeAPVAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "non", False, True, True, True): ArmureDefensifSeuilPompeAPVAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", False, True, True, True): HeaumeDefensifSeuilPompeAPVAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", False, True, True, True): AnneauDefensifValeurPompeAPVAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "non", False, True, True, True): ArmureDefensifValeurPompeAPVAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", False, True, True, True): HeaumeDefensifValeurPompeAPVAnoblisseurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", False, True, True, True): AnneauRenforceRegenPVAnoblisseurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "non", False, True, True, True): ArmureRenforceRegenPVAnoblisseurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", False, True, True, True): HeaumeRenforceRegenPVAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", False, True, True, True): AnneauDefensifPlafondRenforceRegenPVAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", False, True, True, True): ArmureDefensifPlafondRenforceRegenPVAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", False, True, True, True): HeaumeDefensifPlafondRenforceRegenPVAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", False, True, True, True): AnneauDefensifProportionRenforceRegenPVAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", False, True, True, True): ArmureDefensifProportionRenforceRegenPVAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", False, True, True, True): HeaumeDefensifProportionRenforceRegenPVAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", False, True, True, True): AnneauDefensifSeuilRenforceRegenPVAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", False, True, True, True): ArmureDefensifSeuilRenforceRegenPVAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", False, True, True, True): HeaumeDefensifSeuilRenforceRegenPVAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", False, True, True, True): AnneauDefensifValeurRenforceRegenPVAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", False, True, True, True): ArmureDefensifValeurRenforceRegenPVAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", False, True, True, True): HeaumeDefensifValeurRenforceRegenPVAnoblisseurElementaireTribal,
    ("Anneau", "non", "non", "PompeAPM", False, True, True, True): AnneauPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "non", "non", "PompeAPM", False, True, True, True): ArmurePompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "non", "non", "PompeAPM", False, True, True, True): HeaumePompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", False, True, True, True): AnneauDefensifPlafondPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "non", "PompeAPM", False, True, True, True): ArmureDefensifPlafondPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", False, True, True, True): HeaumeDefensifPlafondPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", False, True, True, True): AnneauDefensifProportionPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "non", "PompeAPM", False, True, True, True): ArmureDefensifProportionPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", False, True, True, True): HeaumeDefensifProportionPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", False, True, True, True): AnneauDefensifSeuilPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "non", "PompeAPM", False, True, True, True): ArmureDefensifSeuilPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", False, True, True, True): HeaumeDefensifSeuilPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", False, True, True, True): AnneauDefensifValeurPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "non", "PompeAPM", False, True, True, True): ArmureDefensifValeurPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", False, True, True, True): HeaumeDefensifValeurPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", False, True, True, True): AnneauPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", False, True, True, True): ArmurePompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", False, True, True, True): HeaumePompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", False, True, True, True): AnneauDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", False, True, True, True): ArmureDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", False, True, True, True): HeaumeDefensifPlafondPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", False, True, True, True): AnneauDefensifProportionPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", False, True, True, True): ArmureDefensifProportionPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", False, True, True, True): HeaumeDefensifProportionPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", False, True, True, True): AnneauDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", False, True, True, True): ArmureDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", False, True, True, True): HeaumeDefensifSeuilPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", False, True, True, True): AnneauDefensifValeurPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", False, True, True, True): ArmureDefensifValeurPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", False, True, True, True): HeaumeDefensifValeurPompeAPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", False, True, True, True): AnneauRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", False, True, True, True): ArmureRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", False, True, True, True): HeaumeRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, True, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, True, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", False, True, True, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, True, True): AnneauDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, True, True): ArmureDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", False, True, True, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, True, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, True, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", False, True, True, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, True, True): AnneauDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, True, True): ArmureDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", False, True, True, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMAnoblisseurElementaireTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", False, True, True, True): AnneauRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "non", "non", "RenforceRegenPM", False, True, True, True): ArmureRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", False, True, True, True): HeaumeRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", False, True, True, True): AnneauDefensifPlafondRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", False, True, True, True): ArmureDefensifPlafondRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", False, True, True, True): HeaumeDefensifPlafondRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", False, True, True, True): AnneauDefensifProportionRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", False, True, True, True): ArmureDefensifProportionRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", False, True, True, True): HeaumeDefensifProportionRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", False, True, True, True): AnneauDefensifSeuilRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", False, True, True, True): ArmureDefensifSeuilRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", False, True, True, True): HeaumeDefensifSeuilRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", False, True, True, True): AnneauDefensifValeurRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", False, True, True, True): ArmureDefensifValeurRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", False, True, True, True): HeaumeDefensifValeurRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", False, True, True, True): AnneauPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", False, True, True, True): ArmurePompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", False, True, True, True): HeaumePompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): AnneauRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): ArmureRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): HeaumeRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", False, True, True, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAnoblisseurElementaireTribal,
    ("Anneau", "non", "non", "non", True, True, True, True): AnneauAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "non", "non", True, True, True, True): ArmureAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "non", "non", True, True, True, True): HeaumeAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "non", "non", True, True, True, True): AnneauDefensifPlafondAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "non", "non", True, True, True, True): ArmureDefensifPlafondAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "non", "non", True, True, True, True): HeaumeDefensifPlafondAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "non", "non", True, True, True, True): AnneauDefensifProportionAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "non", "non", True, True, True, True): ArmureDefensifProportionAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "non", "non", True, True, True, True): HeaumeDefensifProportionAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "non", "non", True, True, True, True): AnneauDefensifSeuilAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "non", "non", True, True, True, True): ArmureDefensifSeuilAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "non", "non", True, True, True, True): HeaumeDefensifSeuilAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "non", "non", True, True, True, True): AnneauDefensifValeurAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "non", "non", True, True, True, True): ArmureDefensifValeurAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "non", "non", True, True, True, True): HeaumeDefensifValeurAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "non", True, True, True, True): AnneauPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "PompeAPV", "non", True, True, True, True): ArmurePompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "non", True, True, True, True): HeaumePompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "non", True, True, True, True): AnneauDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "non", True, True, True, True): ArmureDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "non", True, True, True, True): HeaumeDefensifPlafondPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "non", True, True, True, True): AnneauDefensifProportionPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "non", True, True, True, True): ArmureDefensifProportionPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "non", True, True, True, True): HeaumeDefensifProportionPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "non", True, True, True, True): AnneauDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "non", True, True, True, True): ArmureDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "non", True, True, True, True): HeaumeDefensifSeuilPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "non", True, True, True, True): AnneauDefensifValeurPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "non", True, True, True, True): ArmureDefensifValeurPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "non", True, True, True, True): HeaumeDefensifValeurPompeAPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "non", True, True, True, True): AnneauRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "non", True, True, True, True): ArmureRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "non", True, True, True, True): HeaumeRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "non", True, True, True, True): AnneauDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "non", True, True, True, True): ArmureDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "non", True, True, True, True): HeaumeDefensifPlafondRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "non", True, True, True, True): AnneauDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "non", True, True, True, True): ArmureDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "non", True, True, True, True): HeaumeDefensifProportionRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "non", True, True, True, True): AnneauDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "non", True, True, True, True): ArmureDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "non", True, True, True, True): HeaumeDefensifSeuilRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "non", True, True, True, True): AnneauDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "non", True, True, True, True): ArmureDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "non", True, True, True, True): HeaumeDefensifValeurRenforceRegenPVAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "non", "PompeAPM", True, True, True, True): AnneauPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "non", "PompeAPM", True, True, True, True): ArmurePompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "non", "PompeAPM", True, True, True, True): HeaumePompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "non", "PompeAPM", True, True, True, True): AnneauDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "non", "PompeAPM", True, True, True, True): ArmureDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "non", "PompeAPM", True, True, True, True): HeaumeDefensifPlafondPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "non", "PompeAPM", True, True, True, True): AnneauDefensifProportionPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "non", "PompeAPM", True, True, True, True): ArmureDefensifProportionPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "non", "PompeAPM", True, True, True, True): HeaumeDefensifProportionPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "non", "PompeAPM", True, True, True, True): AnneauDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "non", "PompeAPM", True, True, True, True): ArmureDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "non", "PompeAPM", True, True, True, True): HeaumeDefensifSeuilPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "non", "PompeAPM", True, True, True, True): AnneauDefensifValeurPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "non", "PompeAPM", True, True, True, True): ArmureDefensifValeurPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "non", "PompeAPM", True, True, True, True): HeaumeDefensifValeurPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "PompeAPM", True, True, True, True): AnneauPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "PompeAPV", "PompeAPM", True, True, True, True): ArmurePompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "PompeAPM", True, True, True, True): HeaumePompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "PompeAPM", True, True, True, True): AnneauDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "PompeAPM", True, True, True, True): ArmureDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "PompeAPM", True, True, True, True): HeaumeDefensifPlafondPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "PompeAPM", True, True, True, True): AnneauDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "PompeAPM", True, True, True, True): ArmureDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "PompeAPM", True, True, True, True): HeaumeDefensifProportionPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "PompeAPM", True, True, True, True): AnneauDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "PompeAPM", True, True, True, True): ArmureDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "PompeAPM", True, True, True, True): HeaumeDefensifSeuilPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "PompeAPM", True, True, True, True): AnneauDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "PompeAPM", True, True, True, True): ArmureDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "PompeAPM", True, True, True, True): HeaumeDefensifValeurPompeAPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "PompeAPM", True, True, True, True): AnneauRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "PompeAPM", True, True, True, True): ArmureRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "PompeAPM", True, True, True, True): HeaumeRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, True, True): AnneauDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, True, True): ArmureDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "PompeAPM", True, True, True, True): HeaumeDefensifPlafondRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, True, True): AnneauDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, True, True): ArmureDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "PompeAPM", True, True, True, True): HeaumeDefensifProportionRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, True, True): AnneauDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, True, True): ArmureDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "PompeAPM", True, True, True, True): HeaumeDefensifSeuilRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, True, True): AnneauDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, True, True): ArmureDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "PompeAPM", True, True, True, True): HeaumeDefensifValeurRenforceRegenPVPompeAPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "non", "RenforceRegenPM", True, True, True, True): AnneauRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "non", "RenforceRegenPM", True, True, True, True): ArmureRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "non", "RenforceRegenPM", True, True, True, True): HeaumeRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "non", "RenforceRegenPM", True, True, True, True): AnneauDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "non", "RenforceRegenPM", True, True, True, True): ArmureDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "non", "RenforceRegenPM", True, True, True, True): HeaumeDefensifPlafondRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "non", "RenforceRegenPM", True, True, True, True): AnneauDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "non", "RenforceRegenPM", True, True, True, True): ArmureDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "non", "RenforceRegenPM", True, True, True, True): HeaumeDefensifProportionRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "non", "RenforceRegenPM", True, True, True, True): AnneauDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "non", "RenforceRegenPM", True, True, True, True): ArmureDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "non", "RenforceRegenPM", True, True, True, True): HeaumeDefensifSeuilRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "non", "RenforceRegenPM", True, True, True, True): AnneauDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "non", "RenforceRegenPM", True, True, True, True): ArmureDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "non", "RenforceRegenPM", True, True, True, True): HeaumeDefensifValeurRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "PompeAPV", "RenforceRegenPM", True, True, True, True): AnneauPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "PompeAPV", "RenforceRegenPM", True, True, True, True): ArmurePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "PompeAPV", "RenforceRegenPM", True, True, True, True): HeaumePompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "PompeAPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifPlafondPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "PompeAPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifProportionPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "PompeAPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifSeuilPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "PompeAPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifValeurPompeAPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): AnneauRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): ArmureRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "non", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): HeaumeRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Plafond", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifPlafondRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Proportion", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifProportionRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Seuil", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifSeuilRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Anneau", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): AnneauDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Armure", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): ArmureDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
    ("Heaume", "Valeur", "RenforceRegenPV", "RenforceRegenPM", True, True, True, True): HeaumeDefensifValeurRenforceRegenPVRenforceRegenPMAccelerateurAnoblisseurElementaireTribal,
}
"""
(type_equippement, defensif, pv, pm, accelerateur, anoblisseur, elementaire, tribal) -> classe correspondante
"""
