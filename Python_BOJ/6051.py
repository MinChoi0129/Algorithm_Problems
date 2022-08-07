import sys, copy
input = lambda : sys.stdin.readline().rstrip()
DC = lambda : copy.deepcopy()
logs, now = [[]], []
for _ in range(int(input())):
    query = input().split()
    if len(query) == 1: now.pop()
    elif query[0] == 'a': now.append(int(query[1]))
    else: now = DC(logs[int(query[1])-1])
    try: print(now[-1])
    except: print(-1)
    finally: logs.append(DC(now))