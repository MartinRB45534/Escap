from Jeu.Effet.Effet import *


class Magie(On_action):
    """La classe des magies. Un effet qui s'attache au lanceur le temps de remplir les paramètres, puis se lance avant la phase d'attaque."""
    def __init__(self,gain_xp,cout_mp,latence): #Toutes ces caractéristiques sont déterminées par la sous-classe au moment de l'instanciation, en fonction de la magie utilisée et du niveau.
        self.gain_xp = gain_xp
        self.cout_mp = cout_mp
        self.latence = latence
        self.phase = "démarrage"
        self.affiche = True

    def execute(self,lanceur):
        if self.phase == "démarrage":
            self.action(lanceur)
            self.termine()

    def miss_fire(self,lanceur):
        lanceur.subit(20)

    def get_titre(self,observation):
        return f"Magie ({type(self)})"

    def get_skin(self):
        return SKIN_MAGIE

    def get_description(self,observation):
        return ["Oopsie... Cette magie n'a pas de description.",f"Peut-être que son nom, {self.nom}, pourra aider."]

class Magie_dirigee(Magie) :
    """La classe des magies qui nécessitent une direction."""
    def __init__(self,temps):
        self.temps_dir = temps
        self.direction = None

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.direction != None:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Magie_cout(Magie):
    """La classe des magies dont le coût peut varier."""
    def __init__(self,temps):
        self.temps_cout = temps

class Magie_cible(Magie) :
    """La classe des magies qui nécessitent une (ou plusieurs) cible(s)."""
    def __init__(self,temps):
        self.temps = temps
        self.cible = None

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.cible != None:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Multi_cible(Magie_cible) :
    """La classe des magies qui nécessitent plusieurs cibles."""
    def __init__(self,temps):
        self.temps = temps
        self.cible = []

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.cible != []:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Magie_cible_dirigee(Magie_cible,Magie_dirigee):
    def __init__(self,temps_dir,temps):
        self.temps_dir = temps_dir
        self.temps = temps
        self.cible = None
        self.direction = None

    def execute(self,lanceur):
        if self.phase == "démarrage":
            if self.direction != None and self.cible != None:
                self.action(lanceur)
            else:
                self.miss_fire(lanceur)
            self.termine()

class Portee_limitee(Magie_cible) :
    """La classe des magies qui ciblent quelque chose dans la proximité du joueur avec une portée limitée (sinon elles peuvent viser tout ce qui est dans le champ de vision du joueur)."""
    def __init__(self,portee):
        self.portee = portee

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
    def __init__(self,gain_xp,cout_mp,latence,entitee):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Invocation_projectile(Invocation,Magie_dirigee):
    """La classe des magies qui créent une entitée avec un attribut direction."""
    def __init__(self,gain_xp,cout_mp,latence,temps,entitee):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        Magie_dirigee.__init__(self,temps)
        self.entitee = entitee

    def invoque(self):
        return self.entitee

class Creation_effet(Magie):
    """La classe des magies qui créent un effet (un effet sur le long terme, comme les enchantement, ou sur le court terme, comme un boost ou déboost passager)."""
    def __init__(self,gain_xp,cout_mp,latence,effet):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.effet = effet

    def get_effet(self):
        return self.effet

class Enchante(Creation_effet):
    """La classe des magies qui créent des enchantements (des effets sur le très, très long terme)."""
    def __init__(self,gain_xp,cout_mp,latence,enchantement):
        Magie.__init__(self,gain_xp,cout_mp,latence)
        self.enchantement = enchantement

    def get_enchantement(self):
        return self.enchantement

class Enchante_item(Enchante,Cible_item):
    """La classe des magies qui enchantent un item."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_cases(Enchante,Cible_case,Multi_cible):
    """La classe des magies qui enchantent des cases."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)

class Enchante_agissant(Enchante,Cible_agissant):
    """La classe des magies qui enchantent un agissant."""
    def __init__(self,gain_xp,cout_mp,latence,temps,enchantement):
        Enchante.__init__(self,gain_xp,cout_mp,latence,enchantement)
        Magie_cible.__init__(self,temps)