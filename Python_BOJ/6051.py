import sys, copy
input = lambda : sys.stdin.readline().rstrip()
logs, now = [[]], []
for _ in range(int(input())):
    query = input().split()
    if len(query) == 1: now.pop()
    elif query[0] == 'a': now.append(int(query[1]))
    else: now = copy.deepcopy(logs[int(query[1])-1])
    try: print(now[-1])
    except: print(-1)
    finally: logs.append(copy.deepcopy(now))