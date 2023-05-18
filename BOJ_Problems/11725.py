import sys

sys.setrecursionlimit(10000000)


def dfs(now):
    visited[now] = True
    for node in connections[now]:
        if not visited[node]:
            answer[node] = now
            dfs(node)


n = int(input())

connections = {i: [] for i in range(1, n + 1)}
answer = {i: None for i in range(1, n + 1)}
visited = {i: False for i in range(1, n + 1)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

dfs(1)

for i in range(2, n + 1):
    print(answer[i])
