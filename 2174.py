import sys
input = lambda : sys.stdin.readline().rstrip()

def getAllRobotsPos(my_robots):
    return [(my_robots[i].x, my_robots[i].y) for i in range(len(my_robots))]

class Robot:
    def __init__(self, x, y, direction) -> None:
        self.x = x - 1
        self.y = y - 1
        self.direction = direction
    
    def moveORturn(self, mode, times):
        if mode == "F":
            for _ in range(times):
                if self.direction == 'N':
                    for idx, pos in getAllRobotsPos(my_robots):
                        if (self.x, self.y + 1) == pos:
                            return idx
                    self.y += 1
                    if not (0 <= self.x < A and 0 <= self.y < B):
                        return False
                elif self.direction == 'S':
                    for idx, pos in getAllRobotsPos(my_robots):
                        if (self.x, self.y - 1) == pos:
                            return idx
                    self.y -= 1
                    if not (0 <= self.x < A and 0 <= self.y < B):
                        return False    
                elif self.direction == 'W':
                    for idx, pos in getAllRobotsPos(my_robots):
                        if (self.x - 1, self.y) == pos:
                            return idx
                    self.x -= 1
                    if not (0 <= self.x < A and 0 <= self.y < B):
                        return False
                elif self.direction == 'E':
                    for idx, pos in getAllRobotsPos(my_robots):
                        if (self.x + 1, self.y) == pos:
                            return idx
                    self.x += 1
                    if not (0 <= self.x < A and 0 <= self.y < B):
                        return False
        else:
            if mode == 'L':
                for _ in range(times):
                    if self.direction == 'E':
                        self.direction = 'N'
                    elif self.direction == 'W':
                        self.direction = 'S'
                    elif self.direction == 'S':
                        self.direction = 'E'
                    elif self.direction == 'N':
                        self.direction = 'W'
            elif mode == 'R':
                for _ in range(times):
                    if self.direction == 'E':
                        self.direction = 'S'
                    elif self.direction == 'W':
                        self.direction = 'N'
                    elif self.direction == 'S':
                        self.direction = 'W'
                    elif self.direction == 'N':
                        self.direction = 'E'
            return True
                
A, B = map(int, input().split())
N, M = map(int, input().split())
my_robots = [Robot(-2, -2, "N")]

for _ in range(N):
    tmp = input().split()
    my_robots.append(Robot(int(tmp[0]), int(tmp[1]), tmp[2]))

commands = [input().split() for _ in range(M)]
for cmd in commands:
    result = my_robots[int(cmd[0])].moveORturn(cmd[1], int(cmd[2]))
    if not result:
        print("Robot", cmd[0], "crashes into the wall")
        sys.exit()
    elif type(result) == int:
        print("Robot", cmd[0], "crashes into robot", result)
        sys.exit()
print("OK")