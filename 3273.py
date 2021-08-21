n = int(input())
seq = list(map(int, input().split()))
x = int(input())
cnt = 0

p1, p2 = 0, n - 1

while True:
    if seq[p1] + seq[p2] == x:
        cnt += 1
    p1 += 1

    if p1 == p2:
        p1 = 0
        p2 -= 1
        if p2 == 0:
            break
print(cnt)