import sys, random, collections
input = lambda : sys.stdin.readline().rstrip()

def bfs(start_node, v):
    # distances : None이면 방문한 적 없음.
    # 0을 포함한 자연수이면 방문한 것임.
    # 그 값은 시작노드에서 해당 노드까지의 거리를 의미함.
    distances = [None] * (v+1); distances[start_node] = 0

    # 시작노드에서 최장거리가 되는 노드까지의 거리 및 그 노드의 번호.
    max_distance, node_for_max_distance = 0, None

    Q = collections.deque([start_node])
    while Q:
        current_node = Q.popleft()
        for new_node, new_distance in connections[current_node]:
            if distances[new_node] == None:
                distances[new_node] = distances[current_node] + new_distance
                if max_distance < distances[new_node]:
                    max_distance = distances[new_node]
                    node_for_max_distance = new_node
                Q.append(new_node)

    return max_distance, node_for_max_distance

v = int(input())
connections = {i: [] for i in range(1, v+1)}
for _ in range(v):
    data = [*map(int, input().split())]
    from_node, pairs = data[0], data[1:-1]
    for i in range(0, len(pairs), 2):connections[from_node].append([pairs[i], pairs[i+1]])

print(bfs(bfs(random.randint(1, v), v)[1], v)[0])