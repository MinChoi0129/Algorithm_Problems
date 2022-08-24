class RobotCleaner:
    direction = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
    
    def __init__(self, r: int, c: int, facing: int):
        self.r = r
        self.c = c
        self.facing = facing
        self.clean_count = 0
    
    def clean(self) -> None :
        global floor
        floor[self.r][self.c] = 2 # 청소처리
        self.clean_count += 1
    
    def move(self, fwd_or_back: str) -> None: # wall check 안함
        if fwd_or_back == 'forward':
            if self.facing == RobotCleaner.direction['N']:
                self.r -= 1
            elif self.facing == RobotCleaner.direction['E']:
                self.c += 1
            elif self.facing == RobotCleaner.direction['S']:
                self.r += 1
            elif self.facing == RobotCleaner.direction['W']:
                self.c -= 1
        else: # 'back'
            if self.facing == RobotCleaner.direction['N']:
                self.r += 1
            elif self.facing == RobotCleaner.direction['E']:
                self.c -= 1
            elif self.facing == RobotCleaner.direction['S']:
                self.r -= 1
            elif self.facing == RobotCleaner.direction['W']:
                self.c += 1

    def turnLeft(self):
        if self.facing - 1 >= 0:
            self.facing -= 1
        else:
            self.facing = RobotCleaner.direction['W']

    def check(self, where_to_check: str) -> int:
        '''
        청소했으면(2이면) return 2
        벽이있으면(1이면) return 1
        청소안했으면(0이면) return 0
        '''

        if where_to_check == 'left':
            if self.facing == RobotCleaner.direction['N']:
                if floor[self.r][self.c - 1] == 2:
                    return 2
                elif floor[self.r][self.c - 1] == 1:
                    return 1
                else:
                    return 0
            elif self.facing == RobotCleaner.direction['E']:
                if floor[self.r - 1][self.c] == 2:
                    return 2
                elif floor[self.r - 1][self.c] == 1:
                    return 1
                else:
                    return 0
            elif self.facing == RobotCleaner.direction['S']:
                if floor[self.r][self.c + 1] == 2:
                    return 2
                elif floor[self.r][self.c + 1] == 1:
                    return 1
                else:
                    return 0
            elif self.facing == RobotCleaner.direction['W']:
                if floor[self.r + 1][self.c] == 2:
                    return 2
                elif floor[self.r + 1][self.c] == 1:
                    return 1
                else:
                    return 0

        elif where_to_check == 'back':
            if self.facing == RobotCleaner.direction['N']:
                if floor[self.r + 1][self.c] == 2:
                    return 2
                elif floor[self.r + 1][self.c] == 1:
                    return 1
                else:
                    return 0
            elif self.facing == RobotCleaner.direction['E']:
                if floor[self.r][self.c - 1] == 2:
                    return 2
                elif floor[self.r][self.c - 1] == 1:
                    return 1
                else:
                    return 0
            elif self.facing == RobotCleaner.direction['S']:
                if floor[self.r - 1][self.c] == 2:
                    return 2
                elif floor[self.r - 1][self.c] == 1:
                    return 1
                else:
                    return 0
            elif self.facing == RobotCleaner.direction['W']:
                if floor[self.r][self.c + 1] == 2:
                    return 2
                elif floor[self.r][self.c + 1] == 1:
                    return 1
                else:
                    return 0
        elif where_to_check == 'all':
            p1, p2, p3, p4 = \
            floor[self.r + 1][self.c], floor[self.r - 1][self.c],\
            floor[self.r][self.c + 1], floor[self.r][self.c - 1] # 절대좌표 하, 상, 우, 좌
            zero_count = 0
            ps = [p1, p2, p3, p4]
            for p in ps:
                if p == 0:
                    zero_count += 1
            if zero_count == 0:
                return True
            else: # 청소 안한 곳 1군데 이상
                return False
    
def main():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    for _ in range(n):
        floor.append(list(map(int, input().split())))
        
    r = RobotCleaner(r, c, d)

    r.clean()
    while True:    
        if r.check('left') == 0:
            r.turnLeft()
            r.move('forward')
            r.clean()
        else:
            r.turnLeft()
        
        while r.check('all'):
            if r.check('back') == 1:
                print(r.clean_count)
                return
            else:
                r.move('back')

floor = []
main()