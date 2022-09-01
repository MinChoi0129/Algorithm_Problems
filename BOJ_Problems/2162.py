class Point:
    def __init__(self, x, y): self.x = x; self.y = y
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

def unify(x, y):
    parent_x, parent_y = findParent(x), findParent(y)
    if parent_x < parent_y: parent[parent_y] = parent_x
    elif parent_y < parent_x: parent[parent_x] = parent_y

def findParent(x):
    if parent[x] == x: return x
    else: parent[x] = findParent(parent[x]); return parent[x]

n = int(input())
lines, parent = [], [i for i in range(n)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(Line(Point(x1, y1), Point(x2, y2)))

for i in range(n):
    for j in range(i+1, n):
        if lines[i].hasCrossingPoint(lines[j]): unify(i, j)
for i in range(n): parent[i] = findParent(parent[i]) # refresh

group = {}
for num in parent:
    if num not in group: group[num] = 1
    else: group[num] += 1

print(len(group), max(group.values()), sep = "\n")