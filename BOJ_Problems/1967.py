import sys, random
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10000000)

def dfs(node, distance):
    for new_node, new_distance in connections[node]:
        if visited[new_node] == -1:
            visited[new_node] = distance + new_distance
            dfs(new_node, distance + new_distance)

n = int(input())
connections = {i+1: [] for i in range(n)}
for _ in range(n-1):
    node1, node2, distance = map(int, input().split())
    connections[node1].append((node2, distance))
    connections[node2].append((node1, distance))

# Trial 1
start_node = random.randint(1, n)
visited = [-1] * (n + 1)
visited[start_node] = 0
dfs(start_node, 0)

# Trial 2
start_node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[start_node] = 0
dfs(start_node, 0)

print(max(visited))