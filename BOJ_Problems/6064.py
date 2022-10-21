for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    answer = -1
    for k in range(x, m*n+1, m):
        if (k-y) % n == 0:
            answer = k
            break
    print(answer)