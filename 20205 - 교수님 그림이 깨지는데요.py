n, k = map(int, input().split())

pic = []

for i in range(n):
    pic.append(input().split())

for line in pic:
    for j in range(k):
        for element in line:
            for i in range(k):
                print(element, end = " ")
        print()