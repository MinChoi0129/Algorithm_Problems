import sys

ropes = []
ans = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
        
ropes.sort(reverse = True)

for i in range(n):
    ans.append(ropes[i] * (i + 1))
print(max(ans))

'''
ex_list : [24, 50, 13, 80, 100]
sorted_list : [100, 80, 50, 24, 13]
1개 쓰면 : 100 * 1 = 100
2개 쓰면 : min(100, 80) * 2 = 160 [정답]
3개 쓰면 : min(100, 80, 50) * 3 = 150
4개 쓰면 : min(100, 80, 50, 24) * 4 = 96
5개 쓰면 : min(100, 80, 50, 24, 13) * 5 = 65

일반화
n개 쓰면 : min(sorted_list[0 : n - 1]) * n
'''