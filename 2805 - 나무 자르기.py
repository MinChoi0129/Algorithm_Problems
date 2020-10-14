import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
cut_meter = 1
stack = 0
down = 0
trees = list(map(int, sys.stdin.readline().rstrip().split()))
h = max(trees)

while stack < m:
    for i in range(len(trees)):
        if trees[i] > h - down:
            trees[i] -= cut_meter
            stack += 1
    down += 1
print(h - (down - 1))
    
