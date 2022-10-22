from itertools import combinations as C

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

min_gap = int(1e9)
players = set(range(n))

start_cases = C(players, n//2)
for start_case in start_cases:
    link_case = players - set(start_case)

    start_power, link_power = 0, 0
    start_case, link_case = tuple(start_case), tuple(link_case) # 인덱싱을 위한 단순한 형변환.
    for i in range(n//2 - 1):
        for j in range(i+1, n//2):
            start_1, start_2 = start_case[i], start_case[j]
            link_1, link_2 = link_case[i], link_case[j]

            start_power += board[start_1][start_2] + board[start_2][start_1]
            link_power += board[link_1][link_2] + board[link_2][link_1]

    min_gap = min(min_gap, abs(link_power - start_power))

print(min_gap)