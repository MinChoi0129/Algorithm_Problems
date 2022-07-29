def ccw(p1, p2, p3):
    s = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])
    return 1 if s > 0 else (0 if s == 0 else -1)
    
class Line:
    def __init__(self, p1, p2, size, vector):
        self.start, self.end, self.size, self.vector = p1, p2, size, vector
        
    def isOutOfBoundary(self):
        global L
        if   not (-L <= self.start[0] <= L): return [True, L + 1 +  self.end[0] ]
        elif not (-L <= self.start[1] <= L): return [True, L + 1 +  self.end[1] ]
        elif not (-L <=  self.end[0]  <= L): return [True, L + 1 - self.start[0]]
        elif not (-L <=  self.end[1]  <= L): return [True, L + 1 - self.start[1]]   
        return [False, None]
    
    def isCrossingOtherLine(self, other_line):
        p1, p2, p3, p4 = self.start, self.end, other_line.start, other_line.end
        p1p2 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
        p3p4 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
        
        if p1p2 == 0 and p3p4 == 0: # 일직선 위에
            result = (p3 <= p2 and p1 <= p4) # 겹침여부
            if result:
                option = 0 if p1[1] == p2[1] else 1
                if self.vector == '+':
                    if p1[option] < p4[option] < p2[option]:
                        if p1[option] < p3[option]: return [True, p3[option] - p1[option]] # 선분 속 선분
                        else: return [True, 0]
                    else:
                        if p3[option] < p1[option]: return [True, 0] # 선분 속 선분
                        else: return [True, p3[option] - p1[option]]
                else: return [True, p2[option] - p4[option]] if p1[option] < p4[option] < p2[option] else [True, 0]
                    
        else: # 수직으로 교차
            result = p1p2 <= 0 and p3p4 <= 0
            if result:
                if p1[1] == p2[1]:
                    if self.vector == '+': return [True, p3[0] - p1[0]]
                    else: return [True, p2[0] - p3[0]]
                else:
                    if self.vector == '+': return [True, p3[1] - p1[1]]
                    else: return [True, p2[1] - p3[1]]
        
        return [False, None] # 완벽한 선분.
        
    def isCrossingOrOutOfBoundary(self, other_line): # return [Boolean, timeUntilFalse]
        # 선 충돌판단, 후 영역판단
        result = self.isCrossingOtherLine(other_line)
        return result if result[0] else self.isOutOfBoundary()

direction, lines, isSnakeDead, L, location, N = 'R', [], False, int(input()), [0, 0], int(input())
for dt, next_direction in [input().split() for _ in range(N)]:
    if isSnakeDead: break

    if direction == 'R' or direction == 'U':
        p2 = [location[0] + int(dt), location[1]] if direction == 'R' else [location[0], location[1] + int(dt)]
        p1, location = location, p2
        vector = '+'
    elif direction == 'L' or direction == 'D':
        p1 = [location[0] - int(dt), location[1]] if direction == 'L' else [location[0], location[1] - int(dt)]
        p2, location = location, p1
        vector = '-'

    all_directions = ['U', 'L', 'D', 'R']
    direction = all_directions[(all_directions.index(direction) + (1 if next_direction == 'L' else -1)) % 4]
    new_line = Line(p1, p2, int(dt), vector) # 오브젝트 생성.
    
    if len(lines) >= 3:
        closest_line_distance = L * L # 적절히 큰 숫자
        for old_line in lines[:-1]: # 최근 두개의 선분은 충돌가능성 없음.
            result = new_line.isCrossingOrOutOfBoundary(old_line) # result = [가능여부, 불가능까지의 시간]
            if result[0]:
                isSnakeDead = True
                if result[1] < closest_line_distance: closest_line_distance = result[1]
        if closest_line_distance < L * L: new_line.size = closest_line_distance # 첫 충돌 판정시, 선분충돌까지의 길이를 업데이트.
        lines.append(new_line)
    else:
        is_out_of_boundary = new_line.isOutOfBoundary()
        if is_out_of_boundary[0]:
            new_line.size = is_out_of_boundary[1]
            lines.append(new_line)
            isSnakeDead = True
            break
        else:
            lines.append(new_line)

if N == 0: isSnakeDead = True
if not isSnakeDead:
    
    if direction == 'R' or direction == 'U':
        p2 = [L + 1, location[1]] if direction == 'R' else [location[0], L + 1]
        p1, location = location, p2
        vector = '+'
    elif direction == 'L' or direction == 'D':
        p1 = [-(L + 1), location[1]] if direction == 'L' else [location[0], -(L + 1)]
        p2, location = location, p1
        vector = '-'
    
    new_line = Line(p1, p2, int(dt), vector)
    
    if len(lines) >= 3:
        closest_line_distance = L * L
        for old_line in lines[:-1]: # 최근 두개는 충돌가능성 없음.
            result = new_line.isCrossingOrOutOfBoundary(old_line)
            if result[0]:
                isSnakeDead = True
                if result[1] < closest_line_distance: closest_line_distance = result[1]
        if closest_line_distance < L * L: new_line.size = closest_line_distance
        lines.append(new_line)
    else:
        is_out_of_boundary = new_line.isOutOfBoundary()
        if is_out_of_boundary[0]:
            new_line.size = is_out_of_boundary[1]
            lines.append(new_line)
            isSnakeDead = True
        else:
            lines.append(new_line)

answer = 0
for line in lines: answer += line.size
print(answer if N != 0 else L + 1)