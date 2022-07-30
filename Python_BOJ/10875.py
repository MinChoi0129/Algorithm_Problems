def ccw(p1, p2, p3):
    s = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])
    return 1 if s > 0 else (0 if s == 0 else -1)
    
class Line:
    def __init__(self, p1, p2, size, vector):
        # 반드시 왼쪽아래점이 p1, 오른쪽윗점이 p2
        # 선분길이: size
        # vector: 증가하게 선분이 그려진다면(p1->p2) +, 감소하게 선분이 그려진다면(p2->p1) -
        self.left_down, self.right_up, self.size, self.vector = p1, p2, size, vector
        
    def isOutOfBoundary(self, L): # 선분 양 끝점에 대한 영역 판단 함수
        # 양 끝점 모두 영역 내부면, [False, None]
        # 한 점이라도 영역을 벗어난다면, [True, 벗어날때까지 걸리는 시간] 
        if   not (-L <= self.left_down[0] <= L): return [True, L + 1 +  self.right_up[0] ]
        elif not (-L <= self.left_down[1] <= L): return [True, L + 1 +  self.right_up[1] ]
        elif not (-L <=  self.right_up[0]  <= L): return [True, L + 1 - self.left_down[0]]
        elif not (-L <=  self.right_up[1]  <= L): return [True, L + 1 - self.left_down[1]]   
        return [False, None]
    
    def isCrossingOtherLine(self, other_line): # 두 선분의 충돌 여부
        
        # 반드시 현재 생각하고 있는 선분이 self(p1, p2), 기존에 있던 선분은 other_line(p3, p4)
        p1, p2, p3, p4 = self.left_down, self.right_up, other_line.left_down, other_line.right_up
        
        if p1 in [p3, p4]: # 직각으로 만남. 'ㄴ' 'ㄱ' 모양
            if self.vector == '+': return [True, 0]  # 현재 그리려고 하는 선분을 우측이나 위로 방향성을 갖게 그린다면,
            else: return [True, p2[1] - p1[1]]  # 현재 그리려고 하는 선분을 좌측이나 아래로 방향성을 갖게 그린다면,
        elif p2 in [p3, p4]:
            if self.vector == '+': return [True, p2[1] - p1[1]]
            else: return [True, 0]
        
        # ccw 활용한 판단.
        p1p2 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
        p3p4 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
        
        if p1p2 == 0 and p3p4 == 0: # 네 점이 일직선 위에 있는 경우
            result = (p3 <= p2 and p1 <= p4) # 두 선분이 겹치는지.
            if result: # 겹치는 경우
                option = 0 if p1[1] == p2[1] else 1 # option : 세로(1)로 겹치는지, 가로(0)로 겹치는지
                
                # 현재 그리려고 하는 선분을 우측이나 위로 방향성을 갖게 그린다면,
                if self.vector == '+': 
                    if p1[option] < p4[option] < p2[option]:
                        if p1[option] < p3[option]: return [True, p3[option] - p1[option]] # 선분 속 선분(p1 p3 p4 p2)
                        else: return [True, 0] # 일부만 겹침 (p3 p1 p4 p2)
                    else:  
                        if p3[option] < p1[option]: return [True, 0] # 선분 속 선분 (p3 p1 p2 p4)
                        else: return [True, p3[option] - p1[option]] # 일부만 겹침 (p1 p3 p2 p4)
                        
                # 현재 그리려고 하는 선분을 좌측이나 아래로 방향성을 갖게 그린다면,
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
        
    def isCrossingOrOutOfBoundary(self, other_line, L): # return [BooleanOfAppendability, timeUntilFalse]
        # 충돌판단 먼저하고, 나중에 영역판단. 
        result = self.isCrossingOtherLine(other_line)
        return result if result[0] else self.isOutOfBoundary(L)

def main():
    direction, lines, isSnakeDead, L, location, N = 'R', [], False, int(input()), [0, 0], int(input())
    # 기본방향, Line객체모음, 뱀사망여부, L, 현위치, N

    if N == 0: # 직진만 하고 사망.
        print(L + 1)
        return

    for dt, next_direction in [input().split() for _ in range(N)]:
        if isSnakeDead: break

        if direction == 'R' or direction == 'U':
            vector = '+' # 증가하게 선분을 그림.
            p2 = [location[0] + int(dt), location[1]] if direction == 'R' else [location[0], location[1] + int(dt)]
            p1, location = location, p2 # p1, p2 위치 결정 후 현위치 업데이트
            
        elif direction == 'L' or direction == 'D':
            vector = '-' # 감소하게 선분을 그림.
            p1 = [location[0] - int(dt), location[1]] if direction == 'L' else [location[0], location[1] - int(dt)]
            p2, location = location, p1
        
        new_line = Line(p1, p2, int(dt), vector) # 객체생성, new_line: 새로 그리고싶은 선분
        
        if len(lines) >= 3: # 최근 두개의 선분(뱀의 머리 뒷 두군데 == 뱀의 목 부분 쯤) 은 충돌안하므로 3개이상 쌓였을때 새 선분과 비교가능
            closest_distance_to_first_crossing_line = L * L # 현위치에서 제일 먼저 충돌하는 선분까지의 거리(적절히 큰 숫자로 초기화)
            
            for old_line in lines[:-2]: # 최근 두개의 선분(뱀의 머리 뒷 두군데 == 뱀의 목 부분 쯤) 은 충돌안함.
                result = new_line.isCrossingOrOutOfBoundary(old_line, L) # result = [충돌여부, 충돌점까지의 거리]
                if result[0]: # 선분 충돌 발생.
                    isSnakeDead = True # 뱀 사망처리.
                    if result[1] < closest_distance_to_first_crossing_line:
                        closest_distance_to_first_crossing_line = result[1] # 제일 먼저 충돌하는 선분까지의 거리로 최솟값 탐색.
                    
            # 최댓값이 변경되었다면, 선분을 다 그리는 것이 아니라 첫 충돌하는 선분까지의 거리로 업데이트.
            if closest_distance_to_first_crossing_line < L * L:
                new_line.size = closest_distance_to_first_crossing_line 
            
        else:
            is_out_of_boundary = new_line.isOutOfBoundary(L) # 선분이 영역을 벗어나는지 여부.
            if is_out_of_boundary[0]:
                new_line.size = is_out_of_boundary[1] # 벗어나는데까지의 거리로 업데이트
                isSnakeDead = True # 사망처리.
                
        # 정보를 담고있는 new_line객체를 lines에 모아줌.
        lines.append(new_line)
        
        # 이동을 끝내고, 방향 업데이트
        all_directions = ['U', 'L', 'D', 'R']
        direction = all_directions[(all_directions.index(direction) + (1 if next_direction == 'L' else -1)) % 4]

    # 주어진 미션을 다 수행하고도 뱀이 살아있는 경우 -> 벗어날때까지 직진.
    if not isSnakeDead:
        if direction == 'R' or direction == 'U':
            vector = '+'
            p2 = [L + 1, location[1]] if direction == 'R' else [location[0], L + 1]
            p1, location = location, p2
            
        elif direction == 'L' or direction == 'D':
            vector = '-'
            p1 = [-(L + 1), location[1]] if direction == 'L' else [location[0], -(L + 1)]
            p2, location = location, p1

        size = p2[0] - p1[0] if direction in ['R', 'L'] else p2[1] - p1[1] # 선분길이: 가로선분이면 x값차이, 세로선분이면 y값차이
        new_line = Line(p1, p2, size, vector) # 한 점이 보드 바깥쪽에.
        
        if len(lines) >= 3:
            closest_distance_to_first_crossing_line = L * L
            for old_line in lines[:-2]:
                result = new_line.isCrossingOrOutOfBoundary(old_line, L)
                if result[0]:
                    isSnakeDead = True
                    if result[1] < closest_distance_to_first_crossing_line:
                        closest_distance_to_first_crossing_line = result[1]

            if closest_distance_to_first_crossing_line < L * L:
                new_line.size = closest_distance_to_first_crossing_line
        else:
            is_out_of_boundary = new_line.isOutOfBoundary(L)
            if is_out_of_boundary[0]:
                new_line.size = is_out_of_boundary[1]
                isSnakeDead = True
                
        lines.append(new_line)

    answer = 0
    for line in lines: answer += line.size
    print(answer)
    
main()