class Decalage:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other,Decalage):
            return Decalage(self.x+other.x,self.y+other.y)
        return NotImplemented

    def __radd__(self,other):
        if isinstance(other,Decalage):
            return Decalage(other.x+self.x,other.y+self.y)
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