import sys
n = int(sys.stdin.readline())

mem = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    mem.append([age, name, i])

mem = sorted(mem, key = lambda x : int(x[0]))

for i in range(n):
    print(mem[i][0], mem[i][1])