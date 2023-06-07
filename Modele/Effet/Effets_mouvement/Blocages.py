from __future__ import annotations
from typing import TYPE_CHECKING, Set

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from ..Entitee.Entitee import Entitee
    from ..Entitee.Agissant.Agissant import Agissant
    from ..Labyrinthe.Mur import Mur

# Imports des classes parentes
from ..Effet.Effet import *

class Mur_plein(On_try_through):
    """L'effet qui correspond à la présence d'un mur plein sur le passage de l'entitee."""
    def __init__(self,durete):
        self.affiche = True
        self.durete = durete #La priorite qu'il faut avoir pour briser ce mur.
        self.casse = False

    def action(self,mur:Mur,entitee:Entitee):
        if not(isinstance(entitee,Fantome)): #Deux moyens de traverser un mur plein : être un fantome ;
            ecrasement = None
            if isinstance(entitee,Agissant):
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)   # ou l'écraser.
            if ecrasement is not None :
                passage = ecrasement.utilise(self.durete,entitee.get_priorite())
                if passage :
                    self.casse = True
                    mur_oppose = mur.get_mur_oppose()
                    if mur_oppose is not None:
                        for effet in mur_oppose.effets :
                            if isinstance(effet,Mur_plein):
                                effet.casse = True
                else :
                    mur.peut_passer = False
            else :
                mur.peut_passer = False

    def execute(self,mur:Mur,entitee:Entitee):
        if not(self.casse) :
            self.action(mur,entitee)

    def get_skin(self,code):
        if not(self.casse) :
            return SKINS_MURS[code]
        else:
            return SKIN_MUR_CASSE

class Mur_impassable(On_try_through):
    """L'effet qui correspond à un mur absolument infranchissable."""
    def __init__(self):
        self.affiche = True

    def action(self,mur:Mur,entitee:Entitee):
        mur.peut_passer = False

    def get_skin(self,code):
        return SKINS_MURS[code]

class Porte(On_try_through):
    """L'effet qui correspond à la présence d'une porte sur le passage de l'entitée (une porte et un mur plein peuvent se cumuler, mais ce n'est pas conseillé)."""
    def __init__(self,durete,code,automatique = False):
        self.affiche = True
        self.durete = durete #La priorite qu'il faut avoir pour briser ce mur.
        self.code = code #Le code qui permet d'ouvrir la porte
        self.casse = False
        self.ferme = True
        self.auto = automatique

    def action(self,mur:Mur,entitee:Entitee):
        if not(isinstance(entitee,Fantome)):          #Trois moyens de traverser une porte : être un fantome ;
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()): # avoir la clée ;
                ecrasement = None
                if isinstance(entitee,Agissant):
                    ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement)  # ou tout détruire !
                if ecrasement is not None :
                    passage = ecrasement.utilise(self.durete,entitee.get_priorite())
                    if passage :
                        self.casse = True
                        self.affiche = False
                        self.ferme = False #Si on détruit la porte, elle n'est plus fermée...
                        mur_oppose = mur.get_mur_oppose()
                        if mur_oppose is not None:
                            for effet in mur_oppose.effets :
                                if isinstance(effet,Porte):
                                    effet.casse = True
                                    effet.affiche = False
                                    effet.ferme = False #On voudrait aussi ouvrir l'autre côté de la porte.
                    else :
                        mur.peut_passer = False
                else :
                    mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False
                mur_oppose = mur.get_mur_oppose()
                if mur_oppose is not None:
                    for effet in mur_oppose.effets :
                        if isinstance(effet,Porte):
                            effet.ferme = False #On voudrait aussi ouvrir l'autre côté de la porte.

    def execute(self,mur:Mur,entitee:Entitee):
        if not(self.casse) and self.ferme :
            self.action(mur,entitee)

    def get_skin(self,clees:Set[str] = set()):
        if self.ferme and self.code in clees:
            return SKIN_PORTE_OUVRABLE
        elif self.ferme:
            return SKIN_PORTE
        else:
            return SKIN_PORTE_OUVERTE

class Premiere_porte(Porte):
    def execute(self,mur:Mur,entitee:Entitee):
        if isinstance(entitee,Heros):
            entitee.first_door()
            Premiere_porte.execute = Porte.execute
        Porte.execute(self,mur,entitee)

class Barriere(On_try_through):
    """L'effet qui correspond à la présence d'une barrière magique, qui bloque certaines entitées selon certains critères."""

    def execute(self,mur:Mur,entitee:Entitee):
        self.action(mur,entitee)

    def get_skin(self):
        return SKIN_BARRIERE

class Barriere_classe(Barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions de classe."""
    def __init__(self,classe):
        self.affiche = True
        self.classe = classe

    def action(self,mur:Mur,entitee:Entitee): #Pour interdire certains coins aux fantômes
        if isinstance(entitee,self.classe):
            mur.peut_passer = False

class Barriere_espece(Barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions d'espèce."""
    def __init__(self,espece):
        self.affiche = True
        self.espece = espece

    def action(self,mur:Mur,entitee:Entitee):
        if isinstance(entitee,Agissant) and self.espece in entitee.get_especes():
            mur.peut_passer = False

class Barriere_tribale(Barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'appartenance à un esprit."""
    def __init__(self,esprit):
        self.affiche = True
        self.esprit = esprit

    def action(self,mur:Mur,entitee:Entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if isinstance(entitee,Agissant) and entitee.get_esprit() != self.esprit:
            mur.peut_passer = False

class Barriere_altitude(Barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'altitude de l'item."""
    def __init__(self,altitude):
        self.affiche = True
        self.altitude = altitude

    def action(self,mur:Mur,entitee:Entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if not(isinstance(entitee,Item)) or not(entitee.hauteur >= self.altitude):
            mur.peut_passer = False

class Porte_barriere(Barriere,Porte):
    """Lorsqu'une barrière peut être franchie avec une clée."""
    pass

class Porte_classe(Porte_barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions de classe, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,classe,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.classe = classe

    def action(self,mur:Mur,entitee:Mur): #Pour interdire certains coins aux fantômes
        if isinstance(entitee,self.classe):
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_espece(Porte_barriere):
    """L'effet qui correspond à la présence d'une barrière qui bloque selon des conditions d'espèce, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,espece,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.espece = espece

    def action(self,mur:Mur,entitee:Entitee):
        if isinstance(entitee,Agissant) and self.espece in entitee.get_especes():
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_tribale(Porte_barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'appartenance à un esprit, sauf si on a la clé de la porte."""
    def __init__(self,durete,code,esprit,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.esprit = esprit

    def action(self,mur:Mur,entitee:Entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if isinstance(entitee,Agissant) and entitee.get_esprit() != self.esprit:
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

class Porte_altitude(Porte_barriere):
    """L'effet qui correspond à la présence d'un barrière qui bloque selon l'altitude de l'item."""
    def __init__(self,durete,code,altitude,automatique = False):
        Porte.__init__(self,durete,code,automatique)
        self.altitude = altitude

    def action(self,mur:Mur,entitee:Entitee): #Pour les zones protégées où seul le joueur et son groupe peuvent aller par exemple.
        if not(isinstance(entitee,Item)) or not(entitee.hauteur >= self.altitude):
            if not(isinstance(entitee,Agissant)) or not(self.code in entitee.get_clees()):
                mur.peut_passer = False
            elif not(self.auto): #Si on a la clé et la porte n'est pas automatique, elle reste ouverte !
                self.ferme = False

# Imports utilisés dans le code
from ..Entitee.Entitee import Entitee, Fantome
from ..Entitee.Agissant.Agissant import Agissant
from ..Entitee.Item.Item import Item
from ..Systeme.Classe.Classes import trouve_skill
from ..Systeme.Skill.Skills import Skill_ecrasement
from ..Entitee.Agissant.Humain.Heros import Heros
from Old_Affichage.Skins.Skins import SKIN_MUR_CASSE, SKINS_MURS, SKIN_PORTE, SKIN_PORTE_OUVRABLE, SKIN_PORTE_OUVERTE, SKIN_BARRIERE