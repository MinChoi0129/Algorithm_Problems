t = int(input())

for _ in range(t):
    n = int(input())

    padovan = [0, 1, 1, 1]

    if n <= 3:
        print(padovan[n])
    else:
        for i in range(n - 3):
            padovan.append(padovan[-2] + padovan[-3])
        print(padovan[-1])