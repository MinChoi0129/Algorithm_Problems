from collections import deque

# stack = deque() # 이번 코드에는 재귀함수로 구현
queue = deque()

n, m, v = map(int, input().split())

graph = [ [] for _ in range(n + 1)] # Ignore Node0
for _ in range(m):
    tmp = list(map(int, input().split()))
    if tmp[1] not in graph[tmp[0]]:
        graph[tmp[0]].append(tmp[1])
    if tmp[0] not in graph[tmp[1]]:
        graph[tmp[1]].append(tmp[0])
    
    
for connectionsForNode in graph:
    connectionsForNode.sort()
    
'''========================================'''
visitedDFS = [False] * (n+1)
def dfs(graphIdx):
    global graph, visitedDFS
    visitedDFS[graphIdx] = True
    print(graphIdx, end = " ")
    
    for node in graph[graphIdx]:
        if node == []:
            continue
        if not visitedDFS[node]:
            dfs(node)
            
'''========================================'''
visitedBFS = [False] * (n+1)
def bfs(graphIdx):
    global graph, visitedBFS, queue
    queue.append(graphIdx)
    visitedBFS[graphIdx] = True
    
    while queue:
        nodeNum = queue.popleft()
        print(nodeNum, end = " ")
        
        for node in graph[nodeNum]:
            if node == []:
                continue
            if not visitedBFS[node]:
                queue.append(node)
                visitedBFS[node] = True
                
dfs(v)
print()
bfs(v)
print()