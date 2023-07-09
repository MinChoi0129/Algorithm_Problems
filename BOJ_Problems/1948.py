from collections import deque

n, m = int(input()), int(input())
connections = {node_num: [] for node_num in range(1, n + 1)}
reverse_connections = {node_num: [] for node_num in range(1, n + 1)}
indegree_and_time = {
    node_num: {"indegree": 0, "time": 0} for node_num in range(1, n + 1)
}


for _ in range(m):
    a, b, time = map(int, input().split())
    connections[a].append((b, time))
    reverse_connections[b].append((a, time))
    indegree_and_time[b]["indegree"] += 1

start, end = map(int, input().split())


# 초기의 indegree가 0이면 Q에 넣음
Q = deque(
    [
        node_num
        for node_num in indegree_and_time
        if not indegree_and_time[node_num]["indegree"]
    ]
)

# 정방향 위상정렬
while Q:
    current_node = Q.popleft()
    for adj_node, time in connections[current_node]:
        # indegree 감소시키고 0되면 추가
        indegree_and_time[adj_node]["indegree"] -= 1
        if not indegree_and_time[adj_node]["indegree"]:
            Q.append(adj_node)

        # 인접 노드까지의 최대 시간 계산
        new_time = indegree_and_time[current_node]["time"] + time
        indegree_and_time[adj_node]["time"] = max(
            indegree_and_time[adj_node]["time"], new_time
        )

# 역방향 탐색
Q = deque([end])
used_edges = set()
number_of_roads = 0

while Q:
    current_node = Q.popleft()
    current_time = indegree_and_time[current_node]["time"]
    for adj_node, time in reverse_connections[current_node]:
        adj_time = indegree_and_time[adj_node]["time"]
        edge = str(current_node) + "-" + str(adj_node)
        if current_time - time == adj_time and edge not in used_edges:
            Q.append(adj_node)
            number_of_roads += 1
            used_edges.add(edge)


print(indegree_and_time[end]["time"], number_of_roads, sep="\n")
