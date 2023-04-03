from collections import deque

def keyLogger(left: deque, right: deque, password: list[str]) -> str:
    for cmd in password:
        try:
            if cmd == '<': right.appendleft(left.pop())
            elif cmd == '>': left.append(right.popleft())
            elif cmd == '-': left.pop()
            else: left.append(cmd)
        except: pass

    return ''.join(left + right)

for _ in range(int(input())):
    left, right, password = deque(), deque(), list(input())
    print(keyLogger(left, right, password))

