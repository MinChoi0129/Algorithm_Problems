a, b = map(int, input().split())
c = int(input())
a += (b + c) // 60
b = (b + c) % 60
a %= 24
print(a, b)