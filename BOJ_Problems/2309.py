from itertools import combinations as C

kids = [int(input()) for _ in range(9)]
kids.sort()
for case in C(kids, 7):
    if sum(case) == 100:
        for i in case:
            print(i)
        break