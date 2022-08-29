from collections import deque

n, l, r = map(int, input().split())
world = [[*map(int, input().split())] for _ in range(n)]

def getUnion(x, y):
    visited[x][y] = True
    
    Q = deque([(x, y)]); Q_history = [(x, y)]
    
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y] and l <= abs(world[x][y] - world[new_x][new_y]) <= r:
                visited[new_x][new_y] = True
                
                Q.append((new_x, new_y)); Q_history.append((new_x, new_y))
                
    return Q_history

days = 0
while True:
    had_union_created = False
    visited = [[False] * n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                
                unified_countries = getUnion(x, y)
                union_size = len(unified_countries)
                
                if union_size >= 2:
                    had_union_created = True
                    separated_number_of_people = sum([world[i][j] for i, j in unified_countries]) // union_size
                    
                    for i, j in unified_countries:
                        world[i][j] = separated_number_of_people
             
    if not had_union_created: break
    days += 1

print(days)