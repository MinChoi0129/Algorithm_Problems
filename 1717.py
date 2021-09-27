import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
sets = []
for i in range(n + 1):
    tmp = set()
    tmp.add(i)
    sets.append(tmp)

for _ in range(m):
    op, a, b = input().split()
    if op == '0':
        tmp = set()
        for i in range(len(sets)):
            if int(a) in sets[i]:
                tmp.update(sets[i])
                sets[i] = set()
            if int(b) in sets[i]:
                tmp.update(sets[i])
                sets[i] = set()
        sets.append(tmp)
        while True:
            if set() not in sets:
                break
            sets.remove(set())
        print(sets)
        
                
    elif op == '1':
        find = False
        for s in sets:
            if int(a) in s and int(b) in s:
                find = True
                break
        print("YES" if find else "NO")