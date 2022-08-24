mabangzin = []

def horizon(idx):
    return mabangzin[idx]

def vertical(idx):
    rtn = ""
    for i in mabangzin:
        rtn += i[idx]
    return rtn

ALL_SAME = True
N = int(input())

for _ in range(N):
    mabangzin.append(input())

for i in range(N):
    if horizon(i) != vertical(i):
        ALL_SAME = False
        break

print("YES") if ALL_SAME else print("NO")