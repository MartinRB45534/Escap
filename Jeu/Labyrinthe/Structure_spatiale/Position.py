from Jeu.Constantes import NB_DIRECTIONS

class Position:
    def __init__(self,lab,x,y):
        self.lab=lab #Doit être un chaine de caractères
        self.x=x
        self.y=y

    def __sub__(self,other):
        if isinstance(other,Position):
            if other in self:
                return Decalage(self.x-other.x,self.y-other.y)
            else:
                print(f"On ne peut pas soustraire {other} à {self} car les étages diffèrent.")
                return NotImplemented
        elif isinstance(other,Decalage):
            return Position(self.lab,self.x-other.x,self.y-other.y)
        return NotImplemented

    def __rsub__(self,other):
        if isinstance(other,Position): #Ne devrait pas pouvoir arriver
            if other in self:
                return Decalage(other.x-self.x,other.y-self.y)
            else:
                print(f"On ne peut pas soustraire {self} à {other} car les étages diffèrent.")
                return NotImplemented
        return NotImplemented

    def __eq__(self,other):
        if isinstance(other,Position):
            return self.lab == other.lab and self.x == other.x and self.y == other.y
        return False

    def __contains__(self,item): #Ce n'est pas exactement l'usage normal de in, mais en l'occurence pos1 in pos2 est vrai si les deux positions sont au même étage
        if isinstance(item,Position):
            return self.lab == item.lab
        return False

    def __str__(self):
        return f"Position : {self.lab}, {self.x}, {self.y}"

    def __repr__(self):
        return f"Position : {self.lab}, {self.x}, {self.y}"

    def __iter__(self):
        for i in range(self.y):
            for j in range(self.x):
                yield Position(self.lab,j,i)

class Decalage:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other,Decalage):
            return Decalage(self.x+other.x,self.y+other.y)
        elif isinstance(other,Position):
            return Position(other.lab,self.x+other.x,self.y+other.y)
        else:
            return NotImplemented

    def __radd__(self,other):
        if isinstance(other,Decalage):
            return Decalage(other.x+self.x,other.y+self.y)
        elif isinstance(other,Position):
            return Position(other.lab,other.x+self.x,other.y+self.y)
        else:
            return NotImplemented

    def __sub__(self,other): #Probablement une mauvaise idée !
        if isinstance(other,Decalage): #Il vaudrait mieux additionner -1*other...
            print("Euh, pourquoi tu soustrais un décalage à un décalage ?")
            return Decalage(self.x-other.x,self.y-other.y) #/!\ Renvoyer un warning
        else:
            return NotImplemented

    def __rsub__(self,other): #Probablement une mauvaise idée !
        if isinstance(other,Decalage): #Il vaudrait mieux additionner -1*self...
            print("Euh, pourquoi tu soustrais un décalage à un décalage ?")
            return Decalage(self.x-other.x,self.y-other.y) #/!\ Renvoyer un warning
        elif isinstance(other,Position):
            print("Euh, pourquoi tu soustrais un décalage à une position ?")
            return Position(other.lab,other.x-self.x,other.y-self.y) #Pareil !
        else:
            return NotImplemented

    def __mul__(self,other):
        if isinstance(other,int):
            return Decalage(self.x*other,self.y*other)
        else:
            return NotImplemented

    def __rmul__(self,other):
        if isinstance(other,int):
            return Decalage(other*self.x,other*self.y)
        else:
            return NotImplemented

    def __eq__(self,other):
        if isinstance(other,Decalage): #Il vaudrait mieux additionner -1*self...
            return self.x==other.x and self.y==other.y
        else:
            return NotImplemented

    def __str__(self):
        return f"Decalage : {self.x}, {self.y}"

    def __repr__(self):
        return f"Decalage : {self.x}, {self.y}"

    def __iter__(self):
        if self.y>0:
            ys=range(self.y)
        else:
            ys=range(0,self.y-1)
        for i in ys:
            if self.x>0:
                xs=range(self.x)
            else:
                xs=range(0,self.x-1)
            for j in xs:
                yield Decalage(j,i)
