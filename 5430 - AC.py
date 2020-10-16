import sys
from collections import deque

def show(command, n, deq):
    left = True
    for cmd in command:
        if cmd == 'R':
            if n == 0:
                pass
            else:
                left = not left
        elif cmd == 'D':
            if n == 0:
                print("error")
                return -1
            else:
                try:
                    if left:
                        deq.popleft()
                    else:
                        deq.pop()
                except:
                    print("error")
                    return -1
    if len(deq) == 0:
        print("[]")
    else:
        print("[", end = "")
        
        if left:
            for i in range(len(deq) - 1):
                print(deq[i], end = ",")
            print(deq[-1], end = "")
        else:
            for i in range(len(deq) - 1, 0, -1):
                print(deq[i], end = ",")
            print(deq[0], end = "")
        
        
        print("]")


t = int(input())
for _ in range(t):
    deq = deque()
    command = sys.stdin.readline().rstrip().replace("RR", "")
    n = int(input())
    temp = sys.stdin.readline().rstrip("\n").rstrip("]").lstrip("[").split(",")
    for i in temp:
        deq.append(i)
    show(command, n, deq)