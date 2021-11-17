from collections import deque
n = int(input())
adventurer = deque(sorted(map(int, input().split()), reverse = True))
groups = deque()

while adventurer:
    tmp_group = deque()
    for _ in range(adventurer[0]):
        try: tmp_group.append(adventurer.popleft())
        except: break
    groups.append(tmp_group)
print(len(groups))