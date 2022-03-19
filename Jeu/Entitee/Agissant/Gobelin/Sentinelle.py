from Jeu.Entitee.Agissant.Gobelin.Gobelin import *

class Sentinelle_gobelin(Tank,Gobelin,Sentinelle):
    """Un gobelin qui reste sur place tant qu'il ne voit pas d'ennemi. Créé spécifiquement pour les premiers étages et le tutoriel.
       Il a une meilleure défense que les gobelins de base."""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"sentinelle_gobelin",niveau)

    def get_offenses(self):
        offenses = self.offenses
        self.offenses = []
        if self.etat != "vivant" or self.controleur == None:
            etat = "incapacite"
        elif self.pv <= self.pv_max//9:
            etat = "fuite"
        else:
            etat = "attaque"
        return offenses, etat

    def get_texte_descriptif(self):
        return [f"Une sentinelle gobelin (niveau {self.niveau})",f"ID : {self.ID}","Stats :",f"{self.pv}/{self.pv_max} PV",f"{self.pm}/{self.pm_max} PM",self.statut,"Équippée d'une lourde armure et d'une lance, la sentinelle gobelin ne bouge qu'en présence d'ennemis et meurt difficilement. On la trouve souvent aux alentours d'un camp de gobelins."]


# Deux sentinelles un peu spéciales
class Premier_monstre(Sentinelle_gobelin):
    """La première sentinelle gobelin. Réduire ses stats pour en faire un 1/2 shot ?"""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"premier_monstre",niveau)

    def meurt(self):
        self.controleur.get_entitee(2).first_kill(self.position)
        Agissant.meurt(self)

class Troisieme_monstre(Sentinelle_gobelin):
    """La deuxième sentinelle gobelin. Réduire ses stats pour en faire un 3/4 shot ?"""
    def __init__(self,controleur,position,niveau):
        Agissant.__init__(self,controleur,position,"troisieme_monstre",niveau)

    def meurt(self):
        self.controleur.get_entitee(2).third_kill()
        Agissant.meurt(self)
