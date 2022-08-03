from math import factorial
from itertools import combinations as C
n = int(input())
table = [[*map(int, input().split())] for _ in range(n)]

all_cases = set()
cut = (factorial(n) / (factorial(n//2)**2)) // 2
a = set(range(n))
count = 0
for case in C(range(n), n // 2):
    if count == cut: break
    b = set(case)
    count += 1
    c, d = list(b), list(a-b)
    for i in range(n // 2):
        i %= n//2
        print("TEAM-A")
        print(c[i], c[i-1], end = " ")
        print()
    for i in range(n // 2):
        i %= n//2
        print("TEAM-B")
        print(d[i], d[i-1], end = " ")
        print()
    
    
    