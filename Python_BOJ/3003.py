my_chess = [*map(int, input().split())]; full_chess = [1, 1, 2, 2, 2, 8]
for i in range(6): print(full_chess[i] - my_chess[i], end = " ")