from collections import deque
import sys

def calculateNodeColor(node_color):
    if node_color in [1, 2]: return node_color
    elif node_color >= 3: return node_color % 2
    else: raise ValueError("Invalid node color")

def isBipartiteGraph(connections, visited, start_node, node_color):
    Q = deque([(start_node, node_color)])
    visited[start_node] = node_color
    
    while Q:
        current_node, node_color = Q.popleft()
        for new_node in connections[current_node]:
            if not visited[new_node]:
                new_node_color = calculateNodeColor(node_color + 1)
                Q.append((new_node, new_node_color))
                visited[new_node] = new_node_color
            elif visited[new_node] == node_color:
                return False
    
    return True

for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    connections = {node: [] for node in range(1, v+1)} # node_num: [adj_nodes]
    visited = {node: None for node in range(1, v+1)} # node_num: color(default: None, else: 1 or 2)
    for _ in range(e):
        u, v = map(int, sys.stdin.readline().split())
        connections[u].append(v)
        connections[v].append(u)
    
    results = [isBipartiteGraph(connections, visited, start_node, 1) for start_node in range(1, v+1) if not visited[start_node]]
    print("YES" if False not in results else "NO")