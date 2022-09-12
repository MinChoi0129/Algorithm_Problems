import heapq

def getMinimumLostRupeeByDijkstra(board, losts, n):
    Q = [(board[0][0], 0, 0)]
    while Q:
        current_lost, x, y = heapq.heappop(Q)
        if losts[x][y] >= current_lost:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    updated_lost = current_lost + board[new_x][new_y]
                    if updated_lost < losts[new_x][new_y]:
                        losts[new_x][new_y] = updated_lost
                        heapq.heappush(Q, (updated_lost, new_x, new_y))
    return losts[n-1][n-1]

test_case_number = 1
while True:
    n = int(input())
    if not n: break
    board = [[*map(int, input().split())] for _ in range(n)]
    losts = [[int(1e9)] * n for _ in range(n)]
    print("Problem %d: %d" % (test_case_number, getMinimumLostRupeeByDijkstra(board, losts, n)))
    test_case_number += 1