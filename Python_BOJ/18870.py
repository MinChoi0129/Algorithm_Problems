n = int(input())
a = list(map(int, input().split()))
b = list(sorted(set(a)))

dictionary = dict()

for i in range(len(b)):
    dictionary[b[i]] = i

for i in a:
    print(dictionary[i], end = " ")
print()