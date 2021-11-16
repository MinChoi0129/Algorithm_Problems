from copy import deepcopy
from itertools import combinations as C

def isCompatible(arr):
    only_operator = []
    for char in arr:
        if char == '*':
            if only_operator and only_operator[-1] == '*': return False
            else: only_operator.append(char)            
        elif char == '+': only_operator.append(char)
    return True

n = int(input())

if n == 1:
    print(input())
else:
    full_arr = ["+" for _ in range(2*n - 1)]
    num_arr = [str(i) for i in sorted([int(input()) for _ in range(n)])]

    for i in range(0, 2*n - 1, 2):
        num = num_arr[i // 2]
        if num[0] == '-': full_arr[i] = '(' + num + ')'
        else: full_arr[i] = num

    max_result = int(-1e9)
    for i in range(n - 1):
        for case in C(range(1, 2*n - 1, 2), i):
            copied_arr = deepcopy(full_arr)
            for idx in case: copied_arr[idx] = '*'       
            if isCompatible(copied_arr): max_result = max(max_result, eval(''.join(copied_arr)))

    print(max_result)