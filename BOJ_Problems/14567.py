from collections import deque

n, m = map(int, input().split())
connections = {node_num: [] for node_num in range(1, n + 1)}
indegrees = {node_num: 0 for node_num in range(1, n + 1)}
answers = {}
for _ in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)
    indegrees[b] += 1

Q = deque([(node_num, 1) for node_num in indegrees if not indegrees[node_num]])

while Q:
    current_node, semester = Q.popleft()
    answers[current_node] = semester

    for adj_node in connections[current_node]:
        indegrees[adj_node] -= 1
        if not indegrees[adj_node]:
            Q.append((adj_node, semester + 1))

for node_num in range(1, n + 1):
    print(answers[node_num], end=" ")
