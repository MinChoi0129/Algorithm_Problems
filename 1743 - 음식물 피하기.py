import sys

sys.setrecursionlimit(100000)  # 런타임오류 해결

possible = []
count = 0

def dfs(x, y):
    global count
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if floor[x][y] == 1:
        count += 1
        floor[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

N, M, K = map(int, sys.stdin.readline().split())

floor = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    floor[r - 1][c - 1] = 1

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            possible.append(count)
        count = 0

print(max(possible))

####################################################################################

import sys
from collections import deque
sys.setrecursionlimit(100000)  # 런타임오류 해결

possible = []

def bfs(x, y):
    q = deque()
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    q.append((x, y))
    size = -1
    if floor[x][y] == 1:
        size = 1
        floor[x][y] = 0
    else:
        size = 0
    
    while q: # 큐가 빌때까지
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x <= -1 or new_x >= N or new_y <= -1 or new_y >= M:
                continue
            
            if floor[new_x][new_y] == 1:
                floor[new_x][new_y] = 0
                size += 1
                q.append((new_x, new_y))
                
    return size


N, M, K = map(int, sys.stdin.readline().split())

floor = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    floor[r - 1][c - 1] = 1
    
for i in range(N):
    for j in range(M):
        possible.append(bfs(i, j))
        
print(max(possible))