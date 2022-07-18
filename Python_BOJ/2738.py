n, m = map(int, input().split())
matrix_A = [list(map(int, input().split())) for _ in range(n)]
matrix_B = [list(map(int, input().split())) for _ in range(n)]

for line in range(n):
    line_a, line_b = matrix_A[line], matrix_B[line]
    for element in range(m):
        print(line_a[element] + line_b[element], end = " ")
    print()