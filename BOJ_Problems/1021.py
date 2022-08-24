import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
find = list(map(int, sys.stdin.readline().rstrip().split()))

d = deque()

for i in range(1, n + 1):
    d.append(i)
    
def pop_first():
    d.popleft()

def move_left():
    d.append(d.popleft())

def move_right():
    d.insert(0, d.pop())

left_count = 0
right_count = 0

for i in find: # 숫자를 리스트 화
    while d[0] != i:
        length = len(d)
        if d.index(i) <= length // 2:
            move_left()
            left_count += 1
        else:
            move_right()
            right_count += 1
    pop_first()

print(left_count + right_count)