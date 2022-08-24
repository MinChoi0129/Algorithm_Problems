n, m = map(int, input().split())

how_many_know, their_numbers = 0, []
how_many_know, *their_numbers = map(int, input().split())

knows = set()
all_parties = [] # 파티 기록

for number in their_numbers: # 초기 확진자
    knows.add(number)

for _ in range(m):
    party = list(map(int, input().split()))[1:] # 개별 파티
    all_parties.append(party)

for _ in range(m):
    for party in all_parties:
        for human in list(knows):
            if human in party:
                for smallhuman in party:
                    knows.add(smallhuman)
                

count = 0
for party in all_parties:
    canGo = True
    for human in party:
        if human in list(knows):
            canGo = False
            break
    if canGo:
        count += 1

print(count)