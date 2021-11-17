import sys

Conferences = []

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    Conferences.append((start, end))
    
Conferences.sort(key = lambda x : (x[1], x[0]))
# 끝나는 시간으로 우선 정렬, 끝나는 시간이 같으면 시작시간으로 정렬


possible_conference_combination = []

end_min = 0
for conference in Conferences:
    if conference[0] >= end_min:
        possible_conference_combination.append(conference)
        end_min = conference[1]
        
print(len(possible_conference_combination))