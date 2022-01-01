class Point:
    """defintion du class"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Segment:
    """defintion du class"""
    def __init__(self, originX, originY, extremeX, extremeY):
        self.origin = Point(originX,originY)
        self.extreme = Point(extremeX,extremeY)

    def printSegment(self):
        print("segment origin: ({0},{1})".format(self.origin.x,self.origin.y))
        print("segment extreme: ({0},{1})".format(self.extreme.x,self.extreme.y))

# creation d'un instance,,

mySegment = Segment(1,2,3,4)
mySegment.printSegment()