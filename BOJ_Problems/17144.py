class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class AirPurifier:
    def __init__(self, x1, y1, x2, y2):
        self.head = Point(x1, y1)
        self.body = Point(x2, y2)

    def run(self, board, r, c):
        head_circulations, body_circulations = [], []
        for y in range(1, c):
            head_circulations.append([self.head.x, y])
        for x in range(self.head.x - 1, -1, -1):
            head_circulations.append([x, c-1])
        for y in range(c-2, -1, -1):
            head_circulations.append([0, y])
        for x in range(1, self.head.x + 1):
            head_circulations.append([x, 0])

        for y in range(1, c):
            body_circulations.append([self.body.x, y])
        for x in range(self.body.x + 1, r):
            body_circulations.append([x, c-1])
        for y in range(c-2, -1, -1):
            body_circulations.append([r-1, y])
        for x in range(r-2, self.body.x - 1, -1):
            body_circulations.append([x, 0])
        
        holding_head_value = board[head_circulations[-1][0]][head_circulations[-1][1]]
        holding_body_value = board[body_circulations[-1][0]][body_circulations[-1][1]]
        for i in range(len(head_circulations)):
            head_x, head_y = head_circulations[i]
            body_x, body_y = body_circulations[i]

            # head
            if board[head_x][head_y] != -1:
                copied_holding_head_value = board[head_x][head_y]
                if holding_head_value != -1:
                    board[head_x][head_y] = holding_head_value
                else:
                    board[head_x][head_y] = 0
                holding_head_value = copied_holding_head_value
            else:
                holding_head_value = 0

            # body
            if board[body_x][body_y] != -1:
                copied_holding_body_value = board[body_x][body_y]
                if holding_body_value != -1:
                    board[body_x][body_y] = holding_body_value
                else:
                    board[body_x][body_y] = 0
                holding_body_value = copied_holding_body_value
            else:
                holding_body_value = 0
    
        return board


r, c, t = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(r)]
is_head_set, head_x, head_y, body_x, body_y = False, None, None, None, None
for x in range(r):
    if board[x][0] == -1:
        if is_head_set: body_x, body_y = x, 0
        else: head_x, head_y = x, 0; is_head_set = True

air_purifier = AirPurifier(head_x, head_y, body_x, body_y)

for _ in range(t):
    # 확산
    new_board = [[0] * c for _ in range(r)]
    new_board[head_x][head_y] = -1
    new_board[body_x][body_y] = -1


    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                dust_locations = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < r and 0 <= new_y < c and board[new_x][new_y] != -1:
                        dust_locations.append((new_x, new_y))
                distributing_dust_amount = board[x][y] // len(dust_locations)
                for dust_x, dust_y in dust_locations:
                    new_board[dust_x][dust_y] += distributing_dust_amount
                new_board[x][y] += (board[x][y] - (len(dust_locations) * distributing_dust_amount))
    # 공기청정기 작동
    board = air_purifier.run(new_board, r, c)

dust = 0
for line in board:
    for element in line:
        if element > 0: dust += element

print(dust)