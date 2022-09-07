import sys
input = lambda : sys.stdin.readline().rstrip()

def getDistance(from_node, to_node):
    if distance_table[from_node][to_node] != None: return distance_table[from_node][to_node]

    dist = 0
    for connection in connections[from_node]:
        if connection[0] == to_node: 
            return connection[1]
        else: dist += getDistance(connection[0], to_node)

    distance_table[from_node][to_node] = dist
    distance_table[to_node][from_node] = dist

    return dist

v = int(input())
connections = {i: [] for i in range(1, v + 1)}
distance_table = [[None] * (v+1) for _ in range(v+1)]
for i in range(v): distance_table[i][i] = 0

for _ in range(v):
    data = [*map(int, input().split())]
    from_node, connection_pairs = data[0], data[1:-1]

    tmp_connection = []
    for i in range(len(connection_pairs)):
        if i % 2 == 0: tmp_connection.append(connection_pairs[i])
        else:
            tmp_connection.append(connection_pairs[i])
            distance_table[from_node][tmp_connection[0]] = tmp_connection[1]
            distance_table[tmp_connection[0]][from_node] = tmp_connection[1]
            connections[from_node].append(tmp_connection)
            tmp_connection = []

for from_node in range(1, v):
    for to_node in range(from_node + 1, v + 1):
        distance = getDistance(from_node, to_node)
        distance_table[from_node][to_node] = distance
        distance_table[to_node][from_node] = distance