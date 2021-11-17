from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()

def keyLoger(left : deque, right : deque, password : str):
    for cmd in password:
        if cmd == 'L':
            try:
                right.appendleft(left.pop())
            except:
                pass
        elif cmd == 'D':
            try:
                left.append(right.popleft())
            except:
                pass
        elif cmd == 'B':
            try:
                left.pop()
            except:
                pass
        else:
            left.append(cmd[2])
            
    return ''.join(left + right)


left = deque(list(input()))
right = deque()
password = []
for _ in range(int(input())):
    password.append(input())

print(keyLoger(left, right, password))