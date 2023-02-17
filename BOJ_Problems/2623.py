
def dfs(node_num, visited, order):
    visited[node_num] = True
    for node in connections[node_num]:
        if not visited[node]:
            dfs(node, visited, order)
    order.append(node_num)

def existCycle(node, history: set):
    history.add(node)
    for new_node in connections[node]:
        if new_node in history:
            return True
        return existCycle(new_node, history)
    history.remove(node)
    return False


# 입력
n, m = map(int, input().split())
connections = {i: set() for i in range(1, n+1)}
indegree = [None] + [0] * n
for _ in range(m):
    req_order = [*map(int, input().split())]
    for a in range(1, len(req_order) - 1):
        connections[req_order[a]].add(req_order[a+1])
        indegree[req_order[a+1]] += 1

# 사이클 검사
cycle = False
for key in connections.keys():
    history = set()
    if existCycle(key, history):
        cycle = True
        break

# 사이클 여부에 따른 로직 수행
if cycle:
    print(0)
else:
    visited = [None] + [False] * n
    order = []
    for i in range(1, n+1):
        if not (indegree[i] or visited[i]):
            dfs(i, visited, order)

    for element in reversed(order):
        print(element)