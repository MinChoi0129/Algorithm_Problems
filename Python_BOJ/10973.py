import sys
sys.setrecursionlimit(987654321)
def P(xs) :
    if xs == [] :
        yield []
    for x in xs :
        ys = [y for y in xs if not y==x]
        for p in P(ys) :
            yield ([x] + p)
        
n = int(input())
get = list(map(int, input().split()))
before = list(range(1, n + 1))
if get == before:
    print(-1)
else:
    for i in P(range(1, n + 1)):
        if i == get:
            for j in before:
                print(j, end = " ")
            print()
            break
        before = i