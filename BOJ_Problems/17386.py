class Point:
    def __init__(self, x, y): self.x = x; self.y = y

def ccw(p1, p2, p3): return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)

cal1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
cal2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if cal1 <= 0 and cal2 <= 0:
    if cal1 == 0 and cal2 == 0:
        if min(p1.x, p2.x) <= max(p3.x, p4.x) and max(p1.x, p2.x) >= min(p3.x, p4.x) and min(p1.y, p2.y) <= max(p3.y, p4.y) and min(p3.y, p4.y) <= max(p1.y, p2.y): print(1)
        else: print(0)
    else: print(1)
else: print(0)