"""
from itertools import combinations

def is_possible(combi_list):
    for one_conf_idx in range(len(combi_list) - 1):
        for t in combi_list[one_conf_idx]:
            if t in combi_list[one_conf_idx + 1]:
                return False
    return True

def maxlen(twoDimentionList):
    result = 0
    for oneDimentionList in twoDimentionList:
        l = len(oneDimentionList)
        if  l > result:
            result = l
    return result

N = int(input())
Conferences = []
all_possible_combinations = []

for _ in range(N):
    conference_time = []
    start, end = map(int, input().split())
    for t in range(start, end + 1):
        conference_time.append(t)
    Conferences.append(conference_time)


for i in range(1, len(Conferences) + 1):
    for combination in list(combinations(Conferences, i)):
        if is_possible(combination):
            all_possible_combinations.append(combination)

print(maxlen(all_possible_combinations))
"""


import sys

Conferences = []

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    Conferences.append((start, end))

Conferences.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간으로 우선 정렬, 끝나는 시간이 같으면 시작시간으로 정렬


possible_conference_combination = []

end_min = 0
for conference in Conferences:
    if conference[0] >= end_min:
        possible_conference_combination.append(conference)
        end_min = conference[1]

print(len(possible_conference_combination))
