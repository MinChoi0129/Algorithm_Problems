import sys
sys.setrecursionlimit(1000000)
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parents = dict()
for i in range(n + 1):
    parents[i] = i


def findParent(parents, x):
    if parents[x] != x: # Root Node가 아니라면
        parents[x] = findParent(parents, parents[x])
        return parents[x]
    return x

def unionParents(parents, a, b):
    a = findParent(parents, a)
    b = findParent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        unionParents(parents, a, b)
    elif op == 1:
        if findParent(parents, a) == findParent(parents, b):
            print("YES")
        else:
            print("NO")