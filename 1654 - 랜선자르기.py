"""
이분 탐색 : start, mid, end 활용 / 조건에 따라 start 또는 end를 조정
"""
import sys
k, n = map(int, sys.stdin.readline().rstrip().split())

lan_cables = []
for _ in range(k):
    lan_cables.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(lan_cables) # 가능하면 크게 자르면서 모자라면 좀 덜 크게 잘라보기

while start <= end:
    mid = (start + end) // 2 # mid = 자를 길이
    i_have = 0 # 내가 잘라서 갖고 있는 랜선 수
    for cable in lan_cables:
        i_have += cable // mid
    if i_have < n: # 모자라니까 좀 짧게 잘라서 많이 만들기
        end = mid - 1
    else: # 많으면 혹시 랜선을 더 길게할 수 있는지 알아보기
        start = mid + 1
        
print(end)