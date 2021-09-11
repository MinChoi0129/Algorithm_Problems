n, m = map(int, input().split())

their_numbers = map(int, input().split())[1:]

knows = [False] * (n+1) # 0번 인덱스 무시
all_parties = [] # 파티 기록

for number in their_numbers: # 초기 확진자
    knows[number] = True

for _ in range(m):
    party = list(map(int, input().split()))[1:] # 개별 파티
    all_parties.append(party)
    for i in range(len(party)):
        if knows[party[i]]: # 확진자가 그 파티에 있으면
            for j in range(len(party)): # 모든 파티 참여자는 감염
                knows[party[j]] = True
            break

count = 0
for party in all_parties:
    canGo = True
    for human in party:
        if knows[human]:
            canGo = False
            break
    if canGo:
        count += 1

print(count)