n = int(input())
for i in range(n-1, -1, -1):
    print(" " * i, end = "")
    print("*" * (2*n-1-2*i))