def isProperCoordinate(x, y): return 0 <= x < h and 0 <= y < w and ocean_map[x][y] == 1 and not visited[x][y]

def dfs(x, y):
    visited[x][y] = True
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        new_x, new_y = x+dx, y+dy
        if isProperCoordinate(new_x, new_y): dfs(new_x, new_y)

while True:
    w, h = map(int, input().split())
    if not w*h: break
    ocean_map, visited, count = [[*map(int, input().split())] for _ in range(h)], [[False] * w for _ in range(h)], 0
    for x in range(h):
        for y in range(w):
            if isProperCoordinate(x, y):
                dfs(x, y); count += 1
    print(count)