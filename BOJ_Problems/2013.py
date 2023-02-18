import sys
sys.setrecursionlimit(10**5)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __le__(self, other):
        if self.x < other.x: return True
        elif self.x > other.x: return False
        elif self.y <= other.y: return True
        else: return False

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = [p1, p2] if p1 <= p2 else [p2, p1]
    def projectionIntersection(self, other):
        p1, p2, p3, p4 = Line.getFourPointsFromLines(self, other)
        return p3 <= p2
    def getFourPointsFromLines(l1, l2):
        return [l1.p1, l1.p2, l2.p1, l2.p2] if l1.p1 <= l2.p1 else [l2.p1, l2.p2, l1.p1, l1.p2]

class Vector:
    def __init__(self, p1: Point, p2: Point):
        self.x, self.y = p2.x - p1.x, p2.y - p1.y
    def crossProduct(self, other):
        return self.x * other.y - self.y * other.x

class UnionFind:
    def __init__(self, N: int):
        self.parent = [i for i in range(N)]
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)

class Geometry:
    def CCW(p1, p2, p3):
        return Vector(p1, p2).crossProduct(Vector(p2, p3))
    def isOnSameLineAndHasIntersection(l1, l2):
        p1, p2, p3, p4 = Line.getFourPointsFromLines(l1, l2)
        return Geometry.CCW(p1, p2, p3) == 0 and Geometry.CCW(p1, p2, p4) == 0 and Line.projectionIntersection(l1, l2)

def getAllLinesFromInputs(N):
    lines = []
    for _ in range(N):
        x1, y1, x2, y2 = map(lambda x: int(round(float(x)*100)), input().split())
        lines.append(Line(Point(x1, y1), Point(x2, y2)))
    return lines

def getMinimumNumberOfLines(N, lines, uf):
    for i in range(N-1):
        for j in range(i+1, N):
            if Geometry.isOnSameLineAndHasIntersection(lines[i], lines[j]):
                uf.union(i, j)
    return len(set(uf.find(i) for i in range(N)))

N = int(input())
lines = getAllLinesFromInputs(N)
uf = UnionFind(N)

print(getMinimumNumberOfLines(N, lines, uf))