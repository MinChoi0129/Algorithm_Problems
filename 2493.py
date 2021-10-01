n = int(input())
towers = [*map(int, input().split())]

for i in range(n):
    approach = 0
    tmp = towers[:i][::-1]
    for j in range(len(tmp)):
        if tmp[j] > towers[i]:
            approach = i - j
            break
    print(approach, end = " ")