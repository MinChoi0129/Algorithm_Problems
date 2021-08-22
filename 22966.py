easiestName, easiestLevel = "", 5
for _ in range(int(input())):
    tmp = input().split()
    name, level = tmp[0], int(tmp[1])
    if level < easiestLevel:
        easiestName = name
        easiestLevel = level
print(easiestName)