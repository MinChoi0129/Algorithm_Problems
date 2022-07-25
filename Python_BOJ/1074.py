def calculateZ(x, y, size):
    global answer
    
    # (r, c)가 관찰범위 내에 없는 경우(한쪽 등호 빠져야 사분면 구분됨.)
    # 관찰범위: 출발점에서 오른쪽 및 아래쪽 방향으로 변의 길이가 size 만큼 뻗은 정사각형
    if not (x <= r < x + size and y <= c < y + size):
        answer += size ** 2
    
    elif size >= 4: # 관찰범위 내에 있고, 최소사이즈 2 by 2 보다 큼
        new_size = size // 2
        calculateZ(x,               y,             new_size) # 2사분면
        calculateZ(x,               y + new_size,  new_size) # 1사분면
        calculateZ(x + new_size,    y,             new_size) # 3사분면
        calculateZ(x + new_size,    y + new_size,  new_size) # 4사분면

    elif (x+0, y+0) == (r, c): print(answer+0) # 최소 사이즈 2 by 2 인 상태, 절대적 출발점 (x, y)로부터
    elif (x+0, y+1) == (r, c): print(answer+1) # Z자
    elif (x+1, y+0) == (r, c): print(answer+2) # 모양으로
    elif (x+1, y+1) == (r, c): print(answer+3) # 탐색.

n, r, c = map(int, input().split())
answer = 0

# 탐색 순서 2-1-3-4 사분면(Z자), 절대적 시작 기준점 (0, 0) == 왼쪽 위.
calculateZ(0, 0, 2**n)