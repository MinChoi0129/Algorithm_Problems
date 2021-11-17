import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

files = []
pattern = []
for _ in range(N):
    files.append(input())

for i in range(len(files[0])):
    all_same = True
    for j in range(len(files) - 1):
        if files[j][i] != files[j + 1][i]:
            all_same = False
            break
    if all_same:
        pattern.append(files[0][i])
    else:
        pattern.append("?")

for i in pattern:
    print(i, end = "")