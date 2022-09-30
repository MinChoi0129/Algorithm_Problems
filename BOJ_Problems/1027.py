class Line:
    def __init__(self, x1, y1, x2, y2): self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
    def y(self, x): return (((self.y2 - self.y1) * (x - self.x1)) / (self.x2 - self.x1)) + self.y1

class Building:
    def __init__(self, x, y): self.x = x; self.y = y
    def numberOfFacableBuildings(self): return [self.facable(building) for building in buildings if building != None].count(True)
    def facable(self, other):
        if self == other: return False
        left, right = (self, other) if self.x < other.x else (other, self)
        line = Line(left.x, left.y, right.x, right.y)
        for x in range(left.x + 1, right.x):
            if line.y(x) <= buildings[x].y:
                return False
        return True

n, heights = int(input()), [*map(int, input().split())]
buildings = [None] + [Building(i+1, heights[i]) for i in range(n)]
print(max([building.numberOfFacableBuildings() for building in buildings if building != None]))