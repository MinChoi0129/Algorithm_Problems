from functools import cmp_to_key as CTK
int(input())
arr = sorted(input().split(), key = CTK(lambda x, y : 1 if int(x + y) < int(y + x) else -1))
if arr.count('0') == len(arr) : print(0)
else: print(''.join(arr))