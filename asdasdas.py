def getBorder(_lock):
    flag = False
    count = 0
    for elem1 in _lock:
        for elem2 in elem1:
            if elem2 != 1:
                flag = True
                break
        if flag:
            break
        else:
            count += 1
    return count

def rotateList(_list):
    temp1, temp2 = [], []
    for i in range(0, len(_list)):
        for elem1 in _list[::-1]:
            temp1.append(elem1[i])
        temp2.append(temp1)
        temp1 = []
    return temp2

def makeNewKey(key, u, d, l, r):
    new_key = []
    for _ in range(0, u + len(key) + d):
            new_key.append([1 for i in range(0, l + len(key) + r)])

    for i in range(0, len(key)):
        for j in range(0, len(key)):
            new_key[i+u][j+l] = (key[i][j]+1)%2
    return new_key
                
def makeNewList(_list, i, j, _len):
    temp = []
    for k in range(0, _len):
        temp.append(_list[k+j][i:i+_len])
    return temp
    
def solution(key, lock):
    locks = []
    locks.append(lock)
    for i in range(0, 3):
        locks.append(rotateList(locks[i]))
           
    up_count = getBorder(locks[0])
    left_count = getBorder(locks[1])
    down_count = getBorder(locks[2])
    right_count = getBorder(locks[3])

    for k in range(0, 4):
        new_key = makeNewKey(key, up_count, down_count, left_count, right_count)
        key = rotateList(key)
        for i in range(0, len(new_key) - len(lock) + 1):
            for j in range(0, len(new_key) - len(lock) + 1):
                if makeNewList(new_key, i, j, len(lock)) == lock:
                    return True
    return False