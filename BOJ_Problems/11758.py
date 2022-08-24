x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3= map(float, input().split())

def 행렬(a, b, c, d):
    return a * d - b * c

pns = x1 * 행렬(y2, 1, y3, 1) - y1 * 행렬(x2, 1, x3, 1) + 1 * 행렬(x2, y2, x3, y3)

if pns > 0:
    print(1)
elif pns == 0:
    print(0)
else:
    print(-1)