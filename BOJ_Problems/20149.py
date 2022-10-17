class Point:
    def __init__(self, x, y): self.x = x; self.y = y
    def __eq__(self, other): return self.x == other.x and self.y == other.y

def ccw(p1, p2, p3): return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def getCrossingPoint(p1, p2, p3, p4):
    x11, y11 = p1.x, p1.y
    x12, y12 = p2.x, p2.y
    x21, y21 = p3.x, p3.y
    x22, y22 = p4.x, p4.y

    m1 = (y12 - y11) / (x12 - x11)
    m2 = (y22 - y21) / (x22 - x21)
    if m1==m2: return False
    cx = (x11 * m1 - y11 - x21 * m2 + y21) / (m1 - m2)
    cy = m1 * (cx - x11) + y11
    return cx, cy

    
    return
    
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)

cal1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
cal2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if cal1 <= 0 and cal2 <= 0:
    if cal1 == 0 and cal2 == 0:
        if  min(p1.x, p2.x) <= max(p3.x, p4.x) and \
            min(p3.x, p4.x) <= max(p1.x, p2.x) and \
            min(p1.y, p2.y) <= max(p3.y, p4.y) and \
            min(p3.y, p4.y) <= max(p1.y, p2.y):
            print(1)
            if p1 == p3 or p1 == p4: print(p1.x, p1.y)
            elif p2 == p3 or p2 == p4: print(p2.x, p2.y) 
        else: print(0)
    else:
        print(1)
        # 끝 점 아닌 교점 존재
        print("%.11f %.11f" % getCrossingPoint(p1, p2, p3, p4))
else: print(0)