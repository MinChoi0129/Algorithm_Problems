def nCk(n, k):
    # 다음부분을 main에 넣으세요 >>>>>  n, k = map(int, input().split())
    matrix = [[0 for a in range(k + 1)] for b in range(n + 1)]
    for i in range(n + 1):
        matrix[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - 1]

    return matrix[n][k]