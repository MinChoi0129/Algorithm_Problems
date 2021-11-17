import sys
sticks = [64]
x = int(sys.stdin.readline().rstrip())
while sum(sticks) > x:
    popped = sticks.pop(-1)
    for _ in range(2):
        sticks.append(popped // 2)
    if sum(sticks[:-1]) >= x:
        sticks.pop(-2)
print(len(sticks))