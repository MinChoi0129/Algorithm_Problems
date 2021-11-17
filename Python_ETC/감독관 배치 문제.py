import sys

def total_counting(n, l, b, c):
    tot = 0
    for i in range(n):
        tot += temp_counting(l[i], b, c)
    return tot

def temp_counting(num, b, c):
    count = 0
    b_used = 0
    while num > 0:
        if b >= c:
            if num >= b and b_used == 0:
                몫 = num // b
                나머지 = num % b
                num = 나머지
                count += 몫
                b_used += 1
            else:
                몫 = num // c
                나머지 = num % c
                num = c
                count += 몫

        else:
            if num >= c:
                몫 = num // c
                나머지 = num % c
                num = c
                count += 몫
    return count



n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

print(total_counting(n, l, b, c))