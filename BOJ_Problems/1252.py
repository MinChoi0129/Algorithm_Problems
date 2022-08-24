a, b = input().split()

# y = int(x, num) : x를 num진수로 인식하여 10진수로 바꾼 후 y에 대입하여라.

a = int(a, 2)
b = int(b, 2)

print(bin(a + b)[2:])