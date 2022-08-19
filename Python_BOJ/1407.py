import sys; sys.setrecursionlimit(int(1e9))
def S(n):
    if not n: return 0
    elif n == 1: return 1
    elif n % 2 == 0: return n//2 + 2*S(n//2)
    else: return (n//2 + 1) + 2*S((n-1)//2)
a, b = map(int, input().split())
print(S(b)-S(a-1))