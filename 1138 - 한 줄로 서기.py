from itertools import permutations

def check(line):
    global n, data
    
    compare = []
    for i in range(1, n + 1):
        count = 0
        for people in line[0 : line.index(i)]:
            if people > i:
                count += 1
        compare.append(count)
        if compare[i - 1] != data[i - 1]:
            return False
    return True
        
    
n = int(input())
data = list(map(int, input().split()))

for perm in permutations([i for i in range(1, n + 1)], n):
    if check(perm):
        for element in perm:
            print(element, end = " ")
        break
    
'''숏코딩'''
# result = [] 
# for i in range(n - 1, -1, -1):
#     result.insert(data[i], i + 1)
# print(result)