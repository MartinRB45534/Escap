from Jeu.Effet.Effet import *
from Jeu.Entitee.Agissant.Humain.Heros import Heros
from Jeu.Entitee.Item.Item import *
from Jeu.Systeme.Classe import *
from Jeu.Constantes import *

class Teleport(On_through):
    """L'effet de téléportation, qui modifie la position de l'agissant (il peut aussi s'agir d'un déplacement normal)."""
    def __init__(self,position: Position,surnaturel: bool = False):
        self.affiche = surnaturel
        self.position = position

    def action(self,entitee: Entitee):
        assert entitee.controleur is not None
        assert entitee.position is not None
        # On va chercher un éventuel occupant de la case cible
        occupants = entitee.controleur.trouve_non_superposables(self.position)
        if issubclass(entitee.get_classe(),Item) and isinstance(entitee,Item):
            if entitee.position.lab!=self.position.lab: #Un item passe quoi qu'il arrive
                entitee.controleur.move(self.position,entitee)
            else:
                entitee.set_position(self.position)
            for ID in occupants:
                occupant = entitee.controleur.entitees[ID]
                assert isinstance(occupant,Non_superposable)
                entitee.heurte_non_superposable(occupant) #Mais il heurte les occupants
        elif issubclass(entitee.get_classe(),Agissant) and isinstance(entitee,Agissant):
            passe = True
            if occupants != []:
                ecrasement = trouve_skill(entitee.classe_principale,Skill_ecrasement) #On peut peut-être écraser l'occupant de l'autre case
                if ecrasement is not None:
                    for occupant in occupants:
                        agissant = entitee.controleur.entitees[occupant]
                        if not ecrasement.utilise(agissant.get_priorite(),entitee.get_priorite()):
                            passe = False
                else:
                    passe = False
            if passe:
                if entitee.position.lab!=self.position.lab:
                    entitee.controleur.move(self.position,entitee)
                else:
                    entitee.set_position(self.position)
                if self.affiche: #On a affaire à un téléporteur spécial, il faut peut-être changer la direction de l'entitee
                    dir_oppose = self.get_dir_oppose(entitee.controleur)
                    if dir_oppose is not None:
                        entitee.regarde(dir_oppose.oppose())

    def get_dir_oppose(self,controleur):
        dir_oppose = None
        for i in DIRECTIONS:
            mur_potentiel = controleur[self.position,i]
            cible_potentielle = mur_potentiel.get_cible()
            if cible_potentielle is not None :
                for mur in controleur[cible_potentielle].murs:
                    if self in mur.effets:
                        dir_oppose = i
        return dir_oppose

    def get_skin(self):
        return SKIN_PORTAIL

class Premier_portail(Teleport):
    def execute(self,*args):
        entitee = args[0]
        assert isinstance(entitee,Agissant)
        if entitee.ID == 2:
            assert isinstance(entitee,Heros)
            entitee.first_teleport()
            Premier_portail.execute = Teleport.execute
        Teleport.execute(self,entitee)

class Escalier(Teleport):
    def __init__(self,position:Position,sens):
        self.affiche = True
        self.sens = sens
        self.position = position

    def get_skin(self):
        if self.sens == HAUT:
            return SKIN_ESCALIER_HAUT
        elif self.sens == BAS:
            return SKIN_ESCALIER_BAS

class Premiere_marche(Escalier):
    def execute(self,*args):
        entitee = args[0]
        assert isinstance(entitee,Agissant)
        if entitee.ID == 2:
            assert isinstance(entitee,Heros)
            entitee.first_step()
            Premiere_marche.execute = Escalier.execute
        Escalier.execute(self,entitee)
