# def getCheaperWay(roads, stations):
#     if len(stations) == 1:
#         return 0
#     else:
#         return min(stations[0] * sum(roads), 
#                    stations[0] * roads[0] + getCheaperWay(roads[1:], stations[1:]))
        
# n = int(input())
# print(getCheaperWay(list(map(int, input().split())), list(map(int, input().split()))))

n = int(input())
roads = list(map(int, input().split()))
stations = list(map(int, input().split()))

minPrice = stations[0]
money = 0
for i in range(n - 1):
    if minPrice > stations[i]:
        minPrice = stations[i]
    money += minPrice * roads[i]
print(money)