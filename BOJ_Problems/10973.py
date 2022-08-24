from itertools import permutations as P
        
n, seq, answer = int(input()), [*map(int, input().split())], [-1]
for case in P(range(1, n+1), n):
    case = list(case)
    if case == seq:
        for num in answer: print(num, end = " ")
        break
    else: answer = case