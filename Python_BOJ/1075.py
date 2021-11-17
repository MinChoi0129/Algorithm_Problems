import sys
n, f = input(), int(input())

for first in range(0, 10):
    for second in range(0, 10):
        tmp = str(first) + str(second)
        if int(n[:len(n) - 2] + tmp) % f == 0:
            print(tmp)
            sys.exit()