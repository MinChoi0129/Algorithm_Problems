N = int(input())

users = dict()

for user_num in range(1, N + 1):
    users[user_num] = 0
    
for vote in list(map(int, input().split())):
    if vote == 0:
        continue
    else:
        users[vote] += 1
max_user = max(users.items(), key = lambda x : x[1])
max_cnt = max_user[1]
# 제일 투표 많이 받은 유저의 받은 표 수
dupl_cnt = 0
for value in users.values():
    if value == max_cnt:
        dupl_cnt += 1
    if dupl_cnt == 2:
        break

print("skipped") if dupl_cnt == 2 else print(max_user[0])