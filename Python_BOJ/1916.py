import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

n, m, INF = int(input()), int(input()), sys.maxsize
min_distance_to_node = [INF] + [INF for _ in range(n)]
node_connections = [None] + [[] for _ in range(n)]
visited = [None] + [False for _ in range(n)]

for _ in range(m):
    node1, node2, distance = map(int, input().split())
    node_connections[node1].append([node2, distance])
    
start_node, end_node = map(int, input().split())
min_distance_to_node[start_node] = 0

while not visited[end_node]:
    heapq_list = [[value, idx] for idx, value in enumerate(min_distance_to_node) if not visited[idx]]
    heapq.heapify(heapq_list)
    present_idx = heapq_list[0][1]

    if not visited[present_idx]:
        for node, distance in node_connections[present_idx]:
            min_distance_to_node[node] = min(min_distance_to_node[node], min_distance_to_node[present_idx] + distance)
    visited[present_idx] = True

print(min_distance_to_node[end_node])