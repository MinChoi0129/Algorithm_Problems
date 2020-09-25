import math

def 약수(x):
    div_list = [x]
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i) 
    div_list.sort()
    for i in div_list:
        print(i, end=" ")


n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

arr_diff = []

for i in range(n - 1):
    arr_diff.append(arr[i + 1] - arr[i])

if len(arr_diff) == 1:
    give = arr_diff[0]
elif len(arr_diff) == 2:
    give = math.gcd(arr_diff[0], arr_diff[1])
else:
    give = arr_diff[0]
    for i in range(1, len(arr_diff)):
        give = math.gcd(give, arr_diff[i])

약수(give)