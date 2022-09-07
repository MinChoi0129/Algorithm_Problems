class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    
class AirPurifier:
    def __init__(self, x1, y1, x2, y2, r, c):
        self.head = Point(x1, y1)
        self.body = Point(x2, y2)
        self.head_circulations, self.body_circulations = [], []
        for y in range(1, c): self.head_circulations.append([self.head.x, y])
        for x in range(self.head.x - 1, -1, -1): self.head_circulations.append([x, c-1])
        for y in range(c-2, -1, -1): self.head_circulations.append([0, y])
        for x in range(1, self.head.x + 1): self.head_circulations.append([x, 0])
        for y in range(1, c): self.body_circulations.append([self.body.x, y])
        for x in range(self.body.x + 1, r): self.body_circulations.append([x, c-1])
        for y in range(c-2, -1, -1): self.body_circulations.append([r-1, y])
        for x in range(r-2, self.body.x - 1, -1): self.body_circulations.append([x, 0])
        
    def run(self, arr):
        for part in [self.head_circulations, self.body_circulations]:
            hold = -1
            for i in range(len(part)):
                x, y = part[i]
                if arr[x][y] != -1:
                    copy = arr[x][y]
                    if hold != -1: arr[x][y] = hold
                    else: arr[x][y] = 0
                    hold = copy

def spreadDust(arr, r, c, air_purifier):
    head_x, head_y, body_x, body_y = air_purifier.head.x, air_purifier.head.y, air_purifier.body.x, air_purifier.body.y
    tmp_arr = [[0 for _ in range(c)] for _ in range(r)]
    tmp_arr[head_x][head_y], tmp_arr[body_x][body_y] = -1, -1
    
    for x, y in [(x, y) for y in range(c) for x in range(r) if arr[x][y] > 0]:
        put_locations = [(x+dx, y+dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x+dx < r and 0 <= y+dy < c and arr[x+dx][y+dy] != -1]
        for put_x, put_y in put_locations:
            tmp_arr[put_x][put_y] += arr[x][y] // 5
        tmp_arr[x][y] += (arr[x][y] - (arr[x][y] // 5 * len(put_locations)))

    return tmp_arr

def init():
    r, c, t = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(r)]
    (head_x, head_y), (body_x, body_y) = [(x, y) for y in range(c) for x in range(r) if arr[x][y] == -1]
    air_purifier = AirPurifier(head_x, head_y, body_x, body_y, r, c)
    return r, c, t, arr, air_purifier

def main():
    r, c, t, arr, air_purifier = init()
    for _ in range(t):
        arr = spreadDust(arr, r, c, air_purifier)
        air_purifier.run(arr)
    print(sum(sum(element for element in line if element > 0) for line in arr))

main()