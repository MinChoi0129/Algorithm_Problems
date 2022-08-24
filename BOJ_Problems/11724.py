import sys
sys.setrecursionlimit(1000000)
input = lambda : sys.stdin.readline().rstrip()

def DFSFrom(node):
    visited[node] = True
    for num in connections[node]:
        if not visited[num]: DFSFrom(num)

n, m = map(int, input().split())
connections = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

connections_counter = 0
for i in range(1, n + 1):
    if not visited[i]:
        DFSFrom(i)
        connections_counter += 1
print(connections_counter)