from Jeu.Entitee.Agissant.Gobelin.Gobelin import *

class Mage_gobelin(Attaquant_magique_case,Support,Gobelin):
    """Un gobelin avec un potentiel magique.
       Il peut utiliser une attaque magique."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"mage_gobelin",niveau)

    def peut_caster(self,niveau):
        return self.peut_payer(cout_pm_petite_secousse[niveau-1])

    def caste(self):
        return "magie petite secousse"

    def attaque(self,direction):
        skill = trouve_skill(self.classe_principale,Skill_magie) #Est-ce qu'il a le même Skill_magie que le joueur ?
        self.dir_regard = direction
        if self.peut_payer(cout_pm_poing_magique[skill.niveau-1]): #Quelle est l'attaque magique des gobelins ?
            self.skill_courant = Skill_magie
            self.magie_courante = "magie poing magique"
            self.dir_magie = direction
        else:
            self.skill_courant = Skill_stomp
        self.statut = "attaque"

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//2:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_texte_descriptif(self):
        return [f"Un mage gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Un gobelin apte à l'utilisation de la magie. Il s'en sert pour donner plus de force à ses poings, mais lui-même n'est pas très solide. Tuez-le avant qu'il ne vous tue, ou laissez-le gaspiller ses PM sur une défense digne de ce nom."]

# Un mage un peu spécial
class Deuxieme_monstre(Mage_gobelin):
    """Le premier mage gobelin."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"deuxieme_monstre",niveau)

    def meurt(self):
        self.controleur.get_entitee(2).magic_kill(self.position)
        Agissant.meurt(self)
