from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)-1):
        graph[temp[j]].append(temp[j+1])
        indegree[temp[j+1]] += 1

result = []
q = deque([i for i in range(1, n+1) if not indegree[i]])

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)
