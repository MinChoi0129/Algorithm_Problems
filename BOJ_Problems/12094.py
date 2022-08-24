from itertools import product as PI
from collections import deque
from copy import deepcopy as DC
def tryMove(board, move, n):
    for direction in move:
        deques = [deque() for _ in range(n)]
        if direction == 'U':
            for y in range(n):
                tmp = []
                for x in range(n):
                    if board[x][y] != 0:
                        tmp.append(board[x][y])
                        if len(tmp) == 2:
                            if tmp[0] == tmp[1]:
                                deques[y].append(tmp)
                                tmp = []
                            else:
                                deques[y].append([tmp[0]])
                                tmp = [tmp[1]]
                if len(tmp) == 1:deques[y].append(tmp)
            for i in range(n):
                for j in range(len(deques[i])):
                    if len(deques[i][j]) == 2:
                        if deques[i][j][0] == deques[i][j][1]:deques[i][j] = [deques[i][j][0] * 2]            
            for deq in deques:
                while [0] in deq:deq.remove([0])            
            for i in range(n):
                answer = []
                for element in deques[i]:answer += element                    
                for x in range(n):board[x][i] = 0                    
                for j in range(len(answer)):board[j][i] = answer[j]                       
        elif direction == 'D':
            for y in range(n):
                tmp = []
                for x in range(n - 1, -1, -1):
                    if board[x][y] != 0:
                        tmp.append(board[x][y])
                        if len(tmp) == 2:
                            if tmp[0] == tmp[1]:
                                deques[y].append(tmp)
                                tmp = []
                            else:
                                deques[y].append([tmp[0]])
                                tmp = [tmp[1]]
                if len(tmp) == 1:deques[y].append(tmp)                 
            for i in range(n):
                for j in range(len(deques[i])):
                    if len(deques[i][j]) == 2:
                        if deques[i][j][0] == deques[i][j][1]:deques[i][j] = [deques[i][j][0] * 2]
            for deq in deques:
                while [0] in deq:deq.remove([0])
            for i in range(n):
                answer = []
                for element in deques[i]:answer += element
                for x in range(n):board[x][i] = 0
                for j in range(len(answer)):board[n - 1 - j][i] = answer[j]
        elif direction == 'L':
            for x in range(n):
                tmp = []
                for y in range(n):
                    if board[x][y] != 0:
                        tmp.append(board[x][y])
                        if len(tmp) == 2:
                            if tmp[0] == tmp[1]:
                                deques[x].append(tmp)
                                tmp = []
                            else:
                                deques[x].append([tmp[0]])
                                tmp = [tmp[1]]
                if len(tmp) == 1:deques[x].append(tmp)
            for i in range(n):
                for j in range(len(deques[i])):
                    if len(deques[i][j]) == 2:
                        if deques[i][j][0] == deques[i][j][1]:deques[i][j] = [deques[i][j][0] * 2]
            for deq in deques:
                while [0] in deq:deq.remove([0])
            for i in range(n):
                answer = []
                for element in deques[i]:answer += element
                for y in range(n):board[i][y] = 0
                for j in range(len(answer)):board[i][j] = answer[j]
        elif direction == 'R':
            for x in range(n):
                tmp = []
                for y in range(n - 1, -1, -1):
                    if board[x][y] != 0:
                        tmp.append(board[x][y])
                        if len(tmp) == 2:
                            if tmp[0] == tmp[1]:
                                deques[x].append(tmp)
                                tmp = []
                            else:
                                deques[x].append([tmp[0]])
                                tmp = [tmp[1]]
                if len(tmp) == 1:deques[x].append(tmp)
            for i in range(n):
                for j in range(len(deques[i])):
                    if len(deques[i][j]) == 2:
                        if deques[i][j][0] == deques[i][j][1]:deques[i][j] = [deques[i][j][0] * 2]
            for deq in deques:
                while [0] in deq:deq.remove([0])
            for i in range(n):
                answer = []
                for element in deques[i]:answer += element
                for y in range(n):board[i][y] = 0
                for j in range(len(answer)):board[i][n - 1 - j] = answer[j]
    return board           
n, maximum_number = int(input()), 0
board = [[*map(int, input().split())] for _ in range(n)]
for move in [*PI("UDLR", repeat = 10)]:
    result = 0
    for line in tryMove(DC(board), move, n):
        for num in line: result = max(result, num)
    maximum_number = max(maximum_number, result)
print(maximum_number)