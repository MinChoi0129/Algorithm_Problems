expression = input().split("+")
expression = [expression[0]] + expression[1].split("=")
a, b, c = expression[0], expression[1], expression[2]

'''
# 자리수 길이(len())
  <a + b = c>
1. a > b > c (x)
2. a > c > b (x)
3. b > a > c (x)
4. b > c > a (x)
5. c > a > b
6. c > b > a
7. a = b > c (x)
8. a = c > b
9. b = c > a
10. a = b = c
'''

# 10. len(a) == len(b) == len(c)
'''
ex)
? + ? = ?
a + b <= 9 = 10^1 - 1

?? + ?? = ??
a + b <= 99 = 10^2 - 1

??? + ??? = ???
a + b <= 999 = 10^3 -1

...
n = len(a or b or c)
a + b <= 10^n - 1
a : 10^(n-1) ~ 10^n - 1
b : 10^(n-1) ~ 10^n - 1

'''