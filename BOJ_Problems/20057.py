class Storm:
    def __init__(self, x, y, direction):
        """현위치x, 현위치y, 현재방향, 필요직진거리, 직진횟수, 버린모래 를 initializing 합니다."""
        self.x, self.y, self.direction, self.length, self.history, self.garbage = x, y, direction, 1, 0, []
    def move(self, n):
        """Storm 객체를 전진시킨 후, 모래를 주워 뿌립니다. 멤버변수 history는 뿌린 횟수를 기록합니다."""
        dx, dy = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}[self.direction]
        self.x, self.y = self.x + dx, self.y + dy
        self.putSand(self.pickSand(), n)
        self.history += 1
        if self.isBreakStatus(): raise Exception('Arrived to Destination')
    def turnLeft(self):
        """Storm 객체를 좌회전합니다."""
        directions = "NWSE"
        self.direction = directions[(directions.index(self.direction) + 1) % 4]
    def pickSand(self):
        """Storm 객체의 현위치에 있는 모래를 모두 줍습니다."""
        sand_amount, board[self.x][self.y] = board[self.x][self.y], 0
        return sand_amount
    def putSand(self, sand_amount, n):
        """주운 모래를 비율에 맞게 뿌립니다. 범위를 벗어난 경우 멤버변수 garbage에 담습니다."""
        # 모래 분할
        sand_division = [int(sand_amount * division / 100) for division in [5, 7, 2, 7, 2, 10, 10, 1, 1]]
        sand_division.append(sand_amount - sum(sand_division))
        # 위치 선정
        x, y = self.x, self.y
        if self.direction == 'N': new_locations = [(x-2, y), (x, y-1), (x, y-2), (x, y+1), (x, y+2), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1), (x-1, y)]
        elif self.direction == 'S': new_locations = [(x+2, y), (x, y+1), (x, y+2), (x, y-1), (x, y-2), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1), (x+1, y)]
        elif self.direction == 'W': new_locations = [(x, y-2), (x+1, y), (x+2, y), (x-1, y), (x-2, y), (x+1, y-1), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x, y-1)]
        else: new_locations = [(x, y+2), (x-1, y), (x-2, y), (x+1, y), (x+2, y), (x-1, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x, y+1)]
        # 모래 (쌓기 or 버리기) 조건 분기
        for i in range(10):
            new_x, new_y = new_locations[i]
            if 0 <= new_x < n and 0 <= new_y < n: board[new_x][new_y] += sand_division[i]
            else: self.garbage.append(sand_division[i])
    def isBreakStatus(self):
        """종료 조건을 확인합니다."""
        return self.x == 0 and self.y == 0

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
storm = Storm(n//2, n//2, 'W')

try:
    while True:
        if storm.history < 2: storm.move(n); storm.turnLeft()
        else:
            storm.length += 1
            for _ in range(2):
                for _ in range(storm.length): storm.move(n)
                storm.turnLeft()
except: print(sum(storm.garbage))