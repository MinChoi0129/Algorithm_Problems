num1, num2 = map(int, input().split())
answer = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0 :
        answer = i
print(answer)


# 문제점 : 1부터 56까지 무조건 다 나눠봐야 한다. 두 수 중, 작은 값이 9억.. 1~9억까지 다 찾아봐야돼.

# ----------------------------------------------------

num1, num2 = map(int, input().split())

for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break

    
# ----------------------------------------------------
from math import gcd
print(gcd(map(int, input().split())))