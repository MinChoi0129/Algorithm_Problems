from collections import deque

def bfs(graph, start, visited):
    Q = deque([start])
    visited[start] = True
    
    while Q:
        computerNum = Q.popleft()
        for computer in graph[computerNum]:
            if not visited[computer]:
                Q.append(computer)
                visited[computer] = True
 
    infectCount = 0
    for bool in visited:
        if bool:
            infectCount += 1
    return infectCount - 1

n = int(input())
visited = [False] * (n + 1) # 0번 무시
connectivity = [set() for _ in range(n + 1)] # 0번 무시

for _ in range(int(input())):
    a, b = map(int, input().split())
    connectivity[a].add(b)
    connectivity[b].add(a)

print(bfs(connectivity, 1, visited))