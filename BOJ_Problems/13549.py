import heapq

INF, MAX_SIZE = int(1e9), int(1e5)
n, k = map(int, input().split())

distances = {num: INF for num in range(MAX_SIZE+1)}
distances[n] = 0

Q = [(0, n)]
while Q:
    current_distance, current_node = heapq.heappop(Q) # 현재까지의 거리, 현재 노드번호
    for additional_distance, adj_node in [(0, 2 * current_node), (1, current_node + 1), (1, current_node - 1)]: # 2배, 앞으로 한 칸, 뒤로 한 칸
        if 0 <= adj_node <= MAX_SIZE and distances[adj_node] == INF: # 범위 내에 있고, 처음 보는 노드일때만
            new_distance = current_distance + additional_distance
            distances[adj_node] = new_distance # 업데이트
            heapq.heappush(Q, (new_distance, adj_node)) # (새 거리, 새 노드번호)

print(distances[k])
    