import collections

class ConditionalDeque(collections.deque):
    def __init__(self, direction): super().__init__(); self.direction = direction
    def conditionalAppend(self, item):
        if self.direction == 'L': super().append(item)
        else: super().appendleft(item)

def rotated(arr, mode):
    return [*map(list, zip(*arr))][::-1] if mode == 'L' else [*map(list, zip(*arr[::-1]))]

def game2048(brd, direction):    
    if direction == 'L': point = -1; rng = range(8)
    elif direction == 'R': point = 0; rng = range(7, -1, -1)
    elif direction == 'U': return rotated(game2048(rotated(brd, 'L'), 'L'), 'R')
    elif direction == 'D': return rotated(game2048(rotated(brd, 'L'), 'R'), 'R')
    
    rtn_brd = [ConditionalDeque(direction) for _ in rng]
    for x in range(8):
        recently_combined = False
        for y in rng:
            if brd[x][y] == 0: continue
            if rtn_brd[x]:
                if rtn_brd[x][point] == brd[x][y]:
                    if not recently_combined: rtn_brd[x][point] *= 2; recently_combined = True
                    else: rtn_brd[x].conditionalAppend(brd[x][y]); recently_combined = False
                else: rtn_brd[x].conditionalAppend(brd[x][y]); recently_combined = False
            else: rtn_brd[x].conditionalAppend(brd[x][y])
        for _ in range(8 - len(rtn_brd[x])): rtn_brd[x].conditionalAppend(0)
    return rtn_brd

for line in game2048([[*map(int, input().split())] for _ in range(8)], input()):
    for element in line: print(element, end = " ")
    print()