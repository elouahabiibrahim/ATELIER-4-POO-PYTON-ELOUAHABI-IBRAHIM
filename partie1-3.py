class Rectangle:
    """defintion du class"""

    nom = "rectangle"

    def __init__(self,long=3,larg=4):
        self.long = long
        self.larg = larg

    """methode d'affichage"""
    def printShape(self):
        print('dimensions of this {2}: {0} X {1}'.format(self.long,self.larg,self.nom))
    
    """methode surface"""
    def surface(self):
        return self.larg * self.long
    
class Carre(Rectangle):
    """defintion du class"""

    nom = "carre"

    def __init__(self,size=4):
        super().__init__(size,size)
        self.size = size
        

        

# instanciation des class:

myRectangle = Rectangle(12,2)
mySquare = Carre(12)
# affichage
myRectangle.printShape()
mySquare.printShape()
# surface
print('surface 1:{0}'.format(myRectangle.surface()))
print('surface 2:{0}'.format(mySquare.surface()))