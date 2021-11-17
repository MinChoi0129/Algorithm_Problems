import sys

cnt = 1
for i in sys.stdin.readline().rstrip():
    print(i, end = "")
    if cnt == 10:
        cnt = 0
        print()
    cnt += 1