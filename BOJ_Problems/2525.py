a, b = map(int, input().split())
c = int(input())
a += (b + c) // 60 # 시간 더하기
b = (b + c) % 60 # 시간 더하고 남은 분 더하기
a %= 24 # 25시 26시 등 00시 초과한 시간 처리
print(a, b)