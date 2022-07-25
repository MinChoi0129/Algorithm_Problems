from collections import deque as D

total_score, gears = 0, [D(list(input())) for _ in range(4)]

for _ in range(int(input())):
    number, direction = map(int, input().split())
    if number == 1:
        if direction == 1: # 시계방향
            if gears[0][2] == gears[1][-2]: # NN??
                gears[0].appendleft(gears[0].pop())
            elif gears[1][2] == gears[2][-2]: # NSS?
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
            elif gears[2][2] == gears[3][-2]: # NSNN
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
            else: # NSNS
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
                gears[3].append(gears[3].popleft())
        else: # 반시계방향
            if gears[0][2] == gears[1][-2]: # NN??
                gears[0].append(gears[0].popleft())
            elif gears[1][2] == gears[2][-2]: # NSS?
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
            elif gears[2][2] == gears[3][-2]: # NSNN
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
            else: # NSNS
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
                gears[3].appendleft(gears[3].pop())
    elif number == 2:
        if direction == 1: # 시계방향
            if gears[0][2] == gears[1][-2]: # NN??
                if gears[1][2] == gears[2][-2]: # NNN?
                    gears[1].appendleft(gears[1].pop())
                elif gears[2][2] == gears[3][-2]: # NNSS
                    gears[1].appendleft(gears[1].pop())
                    gears[2].append(gears[2].popleft())
                else: # NNSN
                    gears[1].appendleft(gears[1].pop())
                    gears[2].append(gears[2].popleft())
                    gears[3].appendleft(gears[3].pop())
            elif gears[1][2] == gears[2][-2]: # NSS?
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
            elif gears[2][2] == gears[3][-2]: # NSNN
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
            else: # NSNS
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
                gears[3].appendleft(gears[3].pop())
        else: # 반시계방향
            if gears[0][2] == gears[1][-2]: # NN??
                if gears[1][2] == gears[2][-2]: # NNN?
                    gears[1].append(gears[1].popleft())
                elif gears[2][2] == gears[3][-2]: # NNSS
                    gears[1].append(gears[1].popleft())
                    gears[2].appendleft(gears[2].pop())
                else: # NNSN
                    gears[1].append(gears[1].popleft())
                    gears[2].appendleft(gears[2].pop())
                    gears[3].append(gears[3].popleft())
            elif gears[1][2] == gears[2][-2]: # NSS?
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
            elif gears[2][2] == gears[3][-2]: # NSNN
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
            else: # NSNS
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
                gears[3].append(gears[3].popleft())
    elif number == 3:
        if direction == 1: # 시계방향
            if gears[2][2] == gears[3][-2]: # ??NN
                if gears[1][2] == gears[2][-2]: # ?NNN
                    if gears[0][2] == gears[1][-2]: # NNNN
                        gears[2].appendleft(gears[2].pop())
                    else: # SNNN
                        gears[2].appendleft(gears[2].pop())
                elif gears[0][2] == gears[1][-2]: # SSNN
                    gears[1].append(gears[1].popleft())
                    gears[2].appendleft(gears[2].pop())
                else: # NSNN
                    gears[0].appendleft(gears[0].pop())
                    gears[1].append(gears[1].popleft())
                    gears[2].appendleft(gears[2].pop())
            elif gears[1][2] == gears[2][-2]: # ?NNS
                if gears[0][2] == gears[1][-2]: # NNNS
                    gears[2].appendleft(gears[2].pop())
                    gears[3].append(gears[3].popleft())
                else: # SNNS
                    gears[2].appendleft(gears[2].pop())
                    gears[3].append(gears[3].popleft())
            elif gears[0][2] == gears[1][-2]: # SSNS
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
                gears[3].append(gears[3].popleft())
            else: # NSNS
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
                gears[3].append(gears[3].popleft())
        else: # 반시계방향
            if gears[2][2] == gears[3][-2]: # ??NN
                if gears[1][2] == gears[2][-2]: # ?NNN
                    if gears[0][2] == gears[1][-2]: # NNNN
                        gears[2].append(gears[2].popleft())
                    else: # SNNN
                        gears[2].append(gears[2].popleft())
                elif gears[0][2] == gears[1][-2]: # SSNN
                    gears[1].appendleft(gears[1].pop())
                    gears[2].append(gears[2].popleft())
                else: # NSNN
                    gears[0].append(gears[0].popleft())
                    gears[1].appendleft(gears[1].pop())
                    gears[2].append(gears[2].popleft())
            elif gears[1][2] == gears[2][-2]: # ?NNS
                if gears[0][2] == gears[1][-2]: # NNNS
                    gears[2].append(gears[2].popleft())
                    gears[3].appendleft(gears[3].pop())
                else: # SNNS
                    gears[2].append(gears[2].popleft())
                    gears[3].appendleft(gears[3].pop())
            elif gears[0][2] == gears[1][-2]: # SSNS
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
                gears[3].appendleft(gears[3].pop())
            else: # NSNS
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
                gears[3].appendleft(gears[3].pop())
    else: # number == 4
        if direction == 1: # 시계방향
            if gears[2][2] == gears[3][-2]: # ??NN
                if gears[1][2] == gears[2][-2]: # ?NNN
                    if gears[0][2] == gears[1][-2]: # NNNN
                        gears[3].appendleft(gears[3].pop())
                    else: # SNNN
                        gears[3].appendleft(gears[3].pop())
                elif gears[0][2] == gears[1][-2]: # SSNN
                    gears[3].appendleft(gears[3].pop())
                else: # NSNN
                    gears[3].appendleft(gears[3].pop())
            elif gears[1][2] == gears[2][-2]: # ?SSN
                if gears[0][2] == gears[1][-2]: # SSSN
                    gears[2].append(gears[2].popleft())
                    gears[3].appendleft(gears[3].pop())
                else: # NSSN
                    gears[2].append(gears[2].popleft())
                    gears[3].appendleft(gears[3].pop())
            elif gears[0][2] == gears[1][-2]: # NNSN
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
                gears[3].appendleft(gears[3].pop())
            else: # SNSN
                gears[0].append(gears[0].popleft())
                gears[1].appendleft(gears[1].pop())
                gears[2].append(gears[2].popleft())
                gears[3].appendleft(gears[3].pop())
        else: # 반시계방향
            if gears[2][2] == gears[3][-2]: # ??NN
                if gears[1][2] == gears[2][-2]: # ?NNN
                    if gears[0][2] == gears[1][-2]: # NNNN
                        gears[3].append(gears[3].popleft())
                    else: # SNNN
                        gears[3].append(gears[3].popleft())
                elif gears[0][2] == gears[1][-2]: # SSNN
                    gears[3].append(gears[3].popleft())
                else: # NSNN
                    gears[3].append(gears[3].popleft())
            elif gears[1][2] == gears[2][-2]: # ?SSN
                if gears[0][2] == gears[1][-2]: # SSSN
                    gears[2].appendleft(gears[2].pop())
                    gears[3].append(gears[3].popleft())
                else: # NSSN
                    gears[2].appendleft(gears[2].pop())
                    gears[3].append(gears[3].popleft())
            elif gears[0][2] == gears[1][-2]: # NNSN
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
                gears[3].append(gears[3].popleft())
            else: # SNSN
                gears[0].appendleft(gears[0].pop())
                gears[1].append(gears[1].popleft())
                gears[2].appendleft(gears[2].pop())
                gears[3].append(gears[3].popleft())

for i in range(4): total_score += (int(gears[i][0]) * (2 ** i))
print(total_score)