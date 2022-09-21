import sys
input = lambda : sys.stdin.readline().rstrip()

def getDistanceBetweenTwoNodes(start, end, visited):
    if start == end: return [True, 0, end]
    visited[start] = True
    for node, distance in connections[start]:
        if not visited[node]:
            visited[node] = True
            result = getDistanceBetweenTwoNodes(node, end, visited)
            if result[0]:
                return [True, distance + result[1], end]

    return [False, None, end]
n = int(input())
connections = {i+1: [] for i in range(n)}
for _ in range(n-1):
    node1, node2, distance = map(int, input().split())
    connections[node1].append((node2, distance))
    connections[node2].append((node1, distance))

diameter, target_node = 0, None
for node_num in range(2, n + 1):
    visited = [False] * (n + 1); visited[0] = None
    result = getDistanceBetweenTwoNodes(1, node_num, visited)
    if result[1] > diameter:
        diameter = result[1]
        target_node = result[2]

for node_num in range(1, n + 1):
    visited = [False] * (n + 1); visited[0] = None
    result = getDistanceBetweenTwoNodes(target_node, node_num, visited)
    if result[1] > diameter:
        diameter = result[1]

print(diameter)