from itertools import combinations as C

n, m = map(int, input().split())
city = [[*map(int, input().split())] for _ in range(n)]
houses, chicken = [], []

def getChickenDistanceOfCity(case):
    total = 0 # 모든 집에 대하여 제일 가까운 치킨집 거리의 합
    for hx, hy in houses:
        min_distance_of_a_house = int(1e9) # 한 집에 대하여 제일 가까운 치킨집 거리
        for x, y in case:
            min_distance_of_a_house = min(min_distance_of_a_house, (abs(hx - x) + abs(hy - y)))
        total += min_distance_of_a_house
    return total

for x in range(n):
    for y in range(n):
        if city[x][y] == 1:
            houses.append((x, y))
        elif city[x][y] == 2:
            chicken.append((x, y))

minimum_chicken_distance_of_city = int(1e9)
for case in C(chicken, m):
    minimum_chicken_distance_of_city = min(minimum_chicken_distance_of_city, getChickenDistanceOfCity(case))
    
print(minimum_chicken_distance_of_city)