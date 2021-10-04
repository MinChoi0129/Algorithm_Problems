from copy import deepcopy

def keyCheck(keys, board, m):
    for newKey in keys:
        newBoard = deepcopy(board)
        for x in range(m):
            for y in range(m):
                newBoard[x][y] += newKey[x][y]
        allIn = True
        for line in newBoard:
            for num in line:
                if not (0 < num < 2):
                    allIn = False
                    break
            if not allIn:
                break
        if allIn:
            return True
    return False
    

def getFourKeys(key):    
    keys =  [key]
    N = len(key)
    for _ in range(3): keys.append(deepcopy(key))
    
    # 90'
    for r in range(N):
        for c in range(N):
            keys[1][c][N-1-r] = key[r][c]
            
    # 180'
    for r in range(N):
        for c in range(N):
            keys[2][N-1-r][N-1-c] = key[r][c]
    
    # 270'
    for r in range(N):
        for c in range(N):
            keys[3][N-1-c][r] = key[r][c]
    
    return keys

    
def solution(key, lock):
    lockZeroCount = 0
    for line in lock:
        for num in line:
            if num == 0: lockZeroCount += 1
    n, m = len(lock), len(key)
    paddedLock = [[0.5] * (n * 3) for _ in range(n * 3)]
    keys = getFourKeys(key)
    # Updating paddedLock
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            paddedLock[i][j] = lock[i - n][j - n]

    # getTinyBoard
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            tmpBoard = []
            for x in range(i, i + m):
                tmp = []
                for y in range(j, j + m):
                    tmp.append(paddedLock[x][y])
                tmpBoard.append(tmp)

            # zeroCount
            count = 0
            for line in tmpBoard:
                for num in line:
                    if num == 0: count += 1

            if count == lockZeroCount and keyCheck(keys, tmpBoard, m):
                return True
    return False