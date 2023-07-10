# def dfs(node_num):
#     if not visited[node_num]:
#         visited[node_num] = True
#         for node in connections[node_num]:
#             dfs(node)
#         order.append(node_num)


# n, m = map(int, input().split())
# connections = {i: [] for i in range(1, n + 1)}
# visited = [None] + [False] * n
# order = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     connections[a].append(b)
# for i in range(1, n + 1):
#     dfs(i)
# print(*reversed(order))


from collections import deque

n, m = map(int, input().split())
connections = {student_num: [] for student_num in range(1, n + 1)}
indegrees = {student_num: 0 for student_num in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)  # connection 정보 추가
    indegrees[b] += 1

Q = deque()

for student_num in range(1, n + 1):
    if not indegrees[student_num]:
        Q.append(student_num)

while Q:
    student_num = Q.popleft()
    print(student_num, end=" ")
    for adj_student_num in connections[student_num]:
        indegrees[adj_student_num] -= 1
        if not indegrees[adj_student_num]:
            Q.append(adj_student_num)
