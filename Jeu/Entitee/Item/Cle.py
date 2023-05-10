from Jeu.Entitee.Item.Item import *

class Cle(Item):
    """La classe des items qui ouvrent les portes (et les coffres ?)."""
    def __init__(self,position:Optional[Position]=None,codes:List[str]):
        Item.__init__(self,position)
        self.codes = codes

    def get_codes(self):
        return self.codes

    def get_classe(self):
        return Cle

    def get_titre(self,observation=0):
        return "Clé"

    def get_description(self,observation=0):
        return ["Une clé","Je suppose qu'elle ouvre une porte."]

    def get_skin(self):
        return SKIN_CLE

    def get_image():
        return SKIN_CLE
