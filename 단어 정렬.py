n = int(input())

a = {}
for i in range(n):
    word = input()
    a[word] = len(word)

a = sorted(a.items(), key = lambda x : x[1])

for i in range(50):
    temp = []
    for j in range(len(a)):
        if a[j][1] == i + 1:
            temp.append(a[j][0])
    temp.sort()
    for k in range(len(temp)):
        print(temp[k])