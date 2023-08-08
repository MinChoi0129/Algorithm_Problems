class Planet:
    def __init__(self, x, y, z, id):
        self.x, self.y, self.z = x, y, z
        self.id = id


def find(num):
    if parents[num] == num:
        return num
    parents[num] = find(parents[num])
    return parents[num]


def union(num1, num2):
    parent_of_num1, parent_of_num2 = find(num1), find(num2)
    if parent_of_num1 < parent_of_num2:
        parents[parent_of_num2] = parent_of_num1
    elif parent_of_num1 > parent_of_num2:
        parents[parent_of_num1] = parent_of_num2
    else:
        raise Exception("Union 조건 위배")


n = int(input())

planets = []
for id in range(n):
    x, y, z = map(int, input().split())
    planet = Planet(x, y, z, id)
    planets.append(planet)


planets_by_x = sorted(planets, key=lambda planet: planet.x)
planets_by_y = sorted(planets, key=lambda planet: planet.y)
planets_by_z = sorted(planets, key=lambda planet: planet.z)


edges = []

for i in range(n - 1):
    me, other = planets_by_x[i], planets_by_x[i + 1]
    edge = [abs(other.x - me.x), me.id, other.id]
    edges.append(edge)

for i in range(n - 1):
    me, other = planets_by_y[i], planets_by_y[i + 1]
    edge = [abs(other.y - me.y), me.id, other.id]
    edges.append(edge)

for i in range(n - 1):
    me, other = planets_by_z[i], planets_by_z[i + 1]
    edge = [abs(other.z - me.z), me.id, other.id]
    edges.append(edge)

edges.sort()

parents = [planet_number for planet_number in range(n)]

total_distance = 0
for distance, me, other in edges:
    if find(me) == find(other):
        continue
    union(me, other)
    total_distance += distance

print(total_distance)
