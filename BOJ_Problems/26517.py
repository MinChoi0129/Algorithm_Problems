k, a, b, c, d = int(input()), *map(int, input().split())
left, right = a*k+b, c*k+d
print("Yes %d" % left if left == right else "No")