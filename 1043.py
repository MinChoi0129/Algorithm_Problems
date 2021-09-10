n, m = map(int, input().split())

how_many_know, their_numbers = 0, []
how_many_know, *their_numbers = map(int, input().split())

knows = [False] * (n+1) # 0번 인덱스 무시

for number in their_numbers: # 초기 확진자
    print(number)
    knows[number] = True

for _ in range(m):
    input()

print(how_many_know, their_numbers)
print(knows)
