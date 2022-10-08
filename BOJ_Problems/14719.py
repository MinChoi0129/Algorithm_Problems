h, w = map(int, input().split())
heights = [*map(int, input().split())]
world = [['0'] * w for _ in range(h)]

for y in range(w):
    height = heights[y]
    for x in range(h-1, h-1-height, -1):
        world[x][y] = '1'

for x in range(h):
    for y in range(w):
        if world[x][y] == '0':
            world[x][y] = 'w'


for x in range(h-1, -1, -1):
    for y in range(w):
        if world[x][y] == 'w':
            if y in [0, w-1]:
                world[x][y] = '0'
            elif world[x][y-1] == '0' or world[x][y+1] == '0':
                world[x][y] = '0'
    for y in range(w-1, -1, -1):
        if world[x][y] == 'w':
            if y in [0, w-1]:
                world[x][y] = '0'
            elif world[x][y-1] == '0' or world[x][y+1] == '0':
                world[x][y] = '0'

print(sum([line.count('w') for line in world]))