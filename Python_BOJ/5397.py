from collections import deque

def keyLoger(left : deque, right : deque, password : str):
    for cmd in password:
        if cmd == '<':
            try:
                right.appendleft(left.pop())
            except:
                pass
        elif cmd == '>':
            try:
                left.append(right.popleft())
            except:
                pass
        elif cmd == '-':
            try:
                left.pop()
            except:
                pass
        else:
            left.append(cmd)
            
    return ''.join(left + right)

for _ in range(int(input())):
    left = deque()
    right = deque()
    password = list(input())
    print(keyLoger(left, right, password))