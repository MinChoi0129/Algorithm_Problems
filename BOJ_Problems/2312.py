import sys
n = int(sys.stdin.readline().rstrip())

def show(num):
    count = [0 for _ in range(num + 1)]
    temp = num
    for i in range(2, num + 1):
        while temp % i == 0:
            count[i] += 1
            temp /= i
    for i in range(2, num + 1):
        if count[i] > 0:
            print(i, count[i])

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    show(num)