n, k = map(int, input().split())
visited = [False] * (n + 1)

count = 0 
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if not visited[j]:
            visited[j] = True
            count += 1
            
            if count == k:
                print(j)
                exit()