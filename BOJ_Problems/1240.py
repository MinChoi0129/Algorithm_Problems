def calculateDistanceOfTwoNodes(home_node, target_node):
    for now_node, distance in node_connections[home_node]:
        if now_node == target_node: return distance
        
    total_distance, node_visited[home_node] = 0, True
    for now_node, distance in node_connections[home_node]:
        if not node_visited[now_node]:
            result = calculateDistanceOfTwoNodes(now_node, target_node)
            if result: total_distance += result + distance
            
    return total_distance

number_of_nodes, number_of_commands = map(int, input().split())
node_connections = dict( { node: [] for node in range(1, number_of_nodes + 1) } )

for _ in range(number_of_nodes-1):
    node1, node2, distance = map(int, input().split())
    node_connections[node1].append([node2, distance])
    node_connections[node2].append([node1, distance])

for _ in range(number_of_commands):
    node_visited = [False] * (number_of_nodes + 1)
    home_node, target_node = map(int, input().split())
    print(calculateDistanceOfTwoNodes(home_node, target_node))