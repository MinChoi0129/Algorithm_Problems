for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    xs = []
    for x in range(-1000000, 1000001):
        if a*(x**3)+b*(x**2)+c*x+d == 0:
            xs.append(x); break
    N = xs[0]
    A, B, C = a, a*N+b, a*(N**2)+b*N+c
    D = B**2 - 4*A*C
    if D == 0:
        x = (-B) / (2*A)
        if x != N: xs.append(x)
    elif D > 0:
        x1, x2 = ((-B) + D ** 0.5) / (2*A), ((-B) - D ** 0.5) / (2*A)
        if x1 != N: xs.append(x1)
        if x2 != N: xs.append(x2)

    for x in sorted(xs): print("%.4f" % x, end = " ")
    print()