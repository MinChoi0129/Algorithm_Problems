on_off = [0 for _ in range(20000001)]

input()
for num in map(int, input().split()): on_off[num + 10000000] = 1
input()
for num in map(int, input().split()): print(on_off[num + 10000000], end = " ")