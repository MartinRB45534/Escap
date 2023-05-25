from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List

# Imports utilisés uniquement dans les annotations
if TYPE_CHECKING:
    from Jeu.Entitee.Entitee import Entitee
    from Jeu.Entitee.Agissant.Agissant import Agissant
    from Entitee.Item.Projectile.Projectile import Projectile
    from Jeu.Effet.Effet import Effet
    from Jeu.Effet.Effet import Enchantement
    from Jeu.Labyrinthe.Structure_spatiale.Position import Position
    from Jeu.Labyrinthe.Structure_spatiale.Direction import Direction
    from Jeu.Systeme.Classe import Skill_intrasec

# Imports des classes parentes
from Jeu.Action.Caste import Caste
from Jeu.Action.Action_skill import Action_skill

class Magie(Caste,Action_skill):
    """La classe des magies. Précédemment un effet."""
    nom = "magie" # Vraiment utile ?
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float): #Toutes ces caractéristiques sont déterminées par la sous-classe au moment de l'instanciation, en fonction de la magie utilisée et du niveau.
        super().__init__(agissant, latence)
        self.skill = skill
        self.gain_xp = gain_xp
        self.cout = cout_pm

    def get_titre(self,observation=0):
        return f"Magie ({type(self)})"

    def get_skin(self):
        return SKIN_MAGIE

    def get_description(self,observation=0):
        return ["Oopsie... Cette magie n'a pas de description.",f"Peut-être que son nom, {self.nom}, pourra aider."]

class Magies_offensives(Magie):
    """Les magies qui produisent un effet d'attaque"""

class Magie_dirigee(Magie) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,temps:float):
        self.temps_dir = temps
        self.direction:Optional[Direction] = None

class Magie_cout(Magie):
    """La classe des magies dont le coût peut varier."""
    def __init__(self,temps:float):
        self.temps_cout = temps

class Magie_cible(Magie) :
    """La classe des magies qui nécessitent une (ou plusieurs) cible(s)."""
    def __init__(self,temps:float):
        self.temps = temps
        self.cible:Optional[Agissant|Direction|Position|List] = None

class Multi_cible(Magie_cible) :
    """La classe des magies qui nécessitent plusieurs cibles."""
    def __init__(self,temps:float):
        self.temps = temps
        self.cible:List[int|Direction|Position] = []

class Magie_cible_dirigee(Magie_cible,Magie_dirigee):
    def __init__(self,temps_dir:float,temps:float):
        self.temps_dir = temps_dir
        self.temps = temps
        self.cible:Optional[int|Direction|Position] = None
        self.direction:Optional[Direction] = None

class Portee_limitee(Magie_cible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,portee_limite:float):
        self.portee_limite = portee_limite

class Cible_agissant(Magie_cible):
    """La classe des magies qui ciblent d'autres agissants."""
    def __init__(self):
        print("Cible_agissant ne doit pas être instanciée.")

class Cible_item(Magie_cible):
    """La classe des magies qui ciblent des items."""
    def __init__(self):
        print("Cible_item ne doit pas être instanciée.")

class Cible_item_inventaire(Magie_cible):
    """La classe des magies qui ciblent des items dans l'inventaire d'un agissant."""
    def __init__(self):
        print("Cible_item_inventaire ne doit pas être instanciée.")

class Cible_case(Magie_cible):
    """La classe des magies qui ciblent une case. (Si si, une case. Pour une explosion par exemple, vous n'avez pas envie d'être au centre ! Vraiment !)"""
    def __init__(self):
        print("Cible_case ne doit pas être instanciée.")

# Normalement on en a fini avec les magies ciblées

class Invocation(Magie):
    """La classe des magies qui créent une entitée (un agissant pour se battre à vos côtés, un projectile magique pour attaquer les ennemis, un item à utiliser plus tard..."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,entitee:Entitee):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Invocation_projectile(Invocation,Magie_dirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,temps:float,entitee:Projectile):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        Magie_dirigee.__init__(self,temps)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Creation_effet(Magie):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,effet:Effet):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.effet = effet

    def get_effet(self):
        return self.effet

class Enchante(Creation_effet):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,enchantement:Enchantement):
        Magie.__init__(self,skill,agissant,gain_xp,cout_pm,latence)
        self.enchantement = enchantement

    def get_enchantement(self):
        return self.enchantement

class Enchante_item(Enchante,Cible_item):
    """La classe des magies qui enchantent un item."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,temps:float,enchantement:Enchantement):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_cases(Enchante,Cible_case,Multi_cible):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,temps:float,enchantement:Enchantement):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_agissant(Enchante,Cible_agissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,skill:Skill_intrasec,agissant:Agissant,gain_xp:float,cout_pm:float,latence:float,temps:float,enchantement:Enchantement):
        Enchante.__init__(self,skill,agissant,gain_xp,cout_pm,latence,enchantement)
        Magie_cible.__init__(self,temps)

# Imports utilisés dans le code
from Affichage.Skins.Skins import SKIN_MAGIE