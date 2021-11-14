from itertools import combinations as C
descending_numbers = []
for i in range(1, 11):
    for combi in C([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], i):
        descending_numbers.append(int(''.join(map(str, sorted(combi, reverse=True)))))
descending_numbers.sort()
try: print(descending_numbers[int(input())])
except: print(-1)