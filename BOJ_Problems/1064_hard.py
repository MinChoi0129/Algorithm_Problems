class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def getDistanceTo(self, other): return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

if (Xa*Yb + Xb*Yc +Xc*Ya - Xb*Ya - Xc*Yb - Xa*Yc) == 0:
    print(-1)
else:
    Pa, Pb, Pc = Point(Xa, Ya), Point(Xb, Yb), Point(Xc, Yc)

    AB = Pa.getDistanceTo(Pb)
    BC = Pb.getDistanceTo(Pc)
    CA = Pc.getDistanceTo(Pa)

    sq1, sq2, sq3 = 2*(AB + BC), 2*(BC + CA), 2*(CA + AB)
    print(max(sq1, sq2, sq3) - min(sq1, sq2, sq3))