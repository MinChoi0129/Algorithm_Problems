n = int(input())
seq = list(map(int, input().split()))
seq.sort()
x = int(input())
cnt = 0
p1, p2 = 0, n - 1

while p1 < p2:
    tmp = seq[p1] + seq[p2]
    if tmp == x:
        cnt += 1
    if tmp < x:
        p1 += 1
    else:
        p2 -= 1
print(cnt)