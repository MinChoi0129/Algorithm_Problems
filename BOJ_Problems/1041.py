n, a, b, c, d, e, f = int(input()), *map(int, input().split())
three_sides, two_sides, one_side = [], [], [a, b, c, d, e, f]
if n == 1: print(sum(one_side) - max(one_side))
else:
    three_sides.append(f + b + c); three_sides.append(f + b + d)
    three_sides.append(f + e + d); three_sides.append(f + e + c)
    three_sides.append(a + b + c); three_sides.append(a + b + d)
    three_sides.append(a + e + d); three_sides.append(a + e + c)
    
    two_sides.append(f + c); two_sides.append(c + a)
    two_sides.append(a + d); two_sides.append(d + f)
    two_sides.append(c + b); two_sides.append(b + d)
    two_sides.append(d + e); two_sides.append(e + c)
    two_sides.append(f + b); two_sides.append(b + a)
    two_sides.append(a + e); two_sides.append(e + f)

    cal3 = 4 * min(three_sides)
    cal2 = (8*n - 12) * min(two_sides)
    cal1 = (5*n*n - 16*n + 12) * min(one_side)

    print(cal3 + cal2 + cal1)