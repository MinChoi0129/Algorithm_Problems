import math

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def getDistance(self, otherPoint):
        return math.sqrt((self.x - otherPoint.x) ** 2 + (self.y - otherPoint.y) ** 2)

class Vector:
    def __init__(self, startPoint, endPoint):
        self.size = math.sqrt((startPoint.x - endPoint.x) ** 2 + (startPoint.y - endPoint.y) ** 2)
        self.x, self.y = (endPoint.x - startPoint.x), (endPoint.y - startPoint.y)
        
    def __add__(self, otherVector):
        return Vector(Point(0, 0), Point(otherVector.x - self.x, otherVector.y - self.y))
    
    def __mul__(self, k):
        return Vector(Point(0, 0), Point(self.x * k, self.y * k))

def getSquareRound(P1: Point, P2: Point, P3: Point, P4: Point):
    a, b, c, d = \
        P1.getDistance(P2)
        

Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())
Pa, Pb, Pc = Point(Xa, Ya), Point(Xb, Yb), Point(Xc, Yc)

vecAB, vecAC, vecBC = Vector(Pa, Pb), Vector(Pa, Pc), Vector(Pb, Pc)
    
if vecAC.x / vecAB.x == vecAC.y / vecAB.y:
    print(-1)
else:
    # A가 기준
    vecAD = vecAB + vecAC
    Pd_1 = Point(vecAD.x, vecAD.y)
    
    # B가 기준
    vecBD = (-1) * vecAB + vecBC
    Pd_2 = Point(vecBD.x, vecBD.y)
    
    # C가 기준
    vecCD = (-1) * vecAC + (-1) * vecBC
    Pd_3 = Point(vecCD.x, vecCD.y)
    
    parallelogram_rounds = []
    parallelogram_rounds.append()