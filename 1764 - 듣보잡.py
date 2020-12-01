import sys
input = lambda : sys.stdin.readline().rstrip()

people = dict()

N, M = map(int, input().split())

for _ in range(N):
    people[input()] = 1
    
for _ in range(M):
    tmp = input()
    if tmp in people:
        people[tmp] = 2

nhs = []

for i in people.items():
    if i[1] == 2:
        nhs.append(i[0])

nhs.sort()
print(len(nhs))
for i in nhs:
    print(i)