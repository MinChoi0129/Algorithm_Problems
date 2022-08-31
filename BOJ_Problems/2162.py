import sys
input = lambda : sys.stdin.readline().rstrip()
class Point:
    def __init__(self, x, y): self.x = x; self.y = y
    def __eq__(self, other): return [self.x, self.y] == [other.x, other.y]
    def __le__(self, other): return [self.x, self.y] <= [other.x, other.y]
    def __ge__(self, other): return [self.x, self.y] >= [other.x, other.y]

class Line:
    def __init__(self, p1: Point, p2: Point):
        p1, p2 = (p1, p2) if p1 <= p2 else (p2, p1)
        self.left_down = p1; self.right_up = p2
    def hasCrossingPoint(self, other):
        p1, p2, p3, p4 = self.left_down, self.right_up, other.left_down, other.right_up
        return ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0 and p1 <= p4 and p3 <= p2
        
def ccw(p1: Point, p2: Point, p3: Point):
    value = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    return 0 if not value else (1 if value > 0 else -1)

n = int(input())
lines = [] # list of Line objects
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(Line(Point(x1, y1), Point(x2, y2)))

groups = []
for i in range(n):
    for j in range(i + 1, n):
        l1, l2 = lines[i], lines[j]
        has_appended = False
        if l1.hasCrossingPoint(l2):
            for group in groups:
                if l1 in group: group.add(l2); has_appended = True
                elif l2 in group: group.add(l1); has_appended = True
        if not has_appended:
            is_l1_exist = False
            is_l2_exist = False
            
            for group in groups:
                if l1 in group:
                    is_l1_exist = True
                elif l2 in group:
                    is_l2_exist = True
            if is_l1_exist and not is_l2_exist:
                groups.append({l2})
            elif is_l2_exist and not is_l1_exist:
                groups.append({l1})
            elif not is_l1_exist and not is_l2_exist:
                groups.append({l1, l2})

print(len(groups))
print(max([len(group) for group in groups]))