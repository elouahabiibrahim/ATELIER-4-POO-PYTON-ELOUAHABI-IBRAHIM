class Vecteur2D():
    """defintion du class"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    """method d'affichage"""
    def printVector(self):
        print('coordinates of this vector: ({0},{1})'.format(self.x,self.y))

    """surcharger d'addition de deux vecteurs"""
    def __add__(self,other):
        result = Vecteur2D(self.x+other.x,self.y+other.y)
        return result


# instanciation de Vecteur2d
v1 = Vecteur2D(23,44)
v2 = Vecteur2D(13,-2)

# affichage des deux vecteurs
v1.printVector()
v2.printVector()

# la somme
res = v1 + v2
print('the sum of v1 and v2 is:')
res.printVector()