class Point:
    def __init__(self, x, y): self.x = x; self.y = y
    def __eq__(self, other): return self.x == other.x and self.y == other.y

def ccw(p1, p2, p3): return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def getCrossingPoint(p1, p2, p3, p4):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y
    x4, y4 = p4.x, p4.y

    denominator = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if denominator == 0: return False

    x = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / denominator
    y = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / denominator

    return x, y
    
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)

cal1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
cal2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

