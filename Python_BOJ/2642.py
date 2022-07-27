def rotated(array_2d): # 시계방향 90도 회전
    return [list(elem) for elem in zip(*array_2d[::-1])]

def flipped(array_2d): # 윗면 아랫면 뒤집기
    return [line[::-1] for line in array_2d]
    
def cleanFigureFromInput(): # 불필요한 000...000 라인을 제거
    
    # 가로 부분 제거
    figure = []
    for _ in range(6):
        line = input().split()
        if line != ['0'] * 6:
            figure.append(line)

    # 세로부분 제거
    rotated_figure = [line for line in rotated(figure) if line != ['0'] * len(line)] 
    
    return rotated_figure

def getAllFigures():
    figures = [\
        [list('1000'), list('1111'), list('1000')], [list('0100'), list('1111'), list('1000')], [list('0010'), list('1111'), list('1000')], \
        [list('0001'), list('1111'), list('1000')], [list('0100'), list('1111'), list('0100')], [list('0010'), list('1111'), list('0100')], \
        [list('0011'), list('0110'), list('1100')], [list('0011'), list('1110'), list('1000')], [list('1100'), list('0111'), list('0100')], \
        [list('0100'), list('1110'), list('0011')], [list('00111'), list('11100')]
    ] # 기본 전개도 11종류.
    
    for i in range(11): figures.append(flipped(figures[i]))

    for i in range(22):
        arr90 = rotated(figures[i])
        arr180 = rotated(arr90)
        arr270 = rotated(arr180)
        figures.append(arr90)
        figures.append(arr180)
        figures.append(arr270)

    return figures

figures = getAllFigures()
my_figure = cleanFigureFromInput()

if not (True if [['1' if my_figure[i][j] != '0' else '0' for j in range(len(my_figure[0]))] for i in range(len(my_figure))] in figures else False):
    print(0)
else:
    for x in range(len(my_figure)):
        for y in range(len(my_figure[0])):
            if my_figure[x][y] == '1': number_one_position = x, y

    dxys = [
        [[0, 2]], [[0, -2]], # 0, 2

        [[-1, 0], [0, -1], [-1, 0]], [[0, 1], [1, 0], [0, 1]], # 1, 2
        [[-1, 0], [0, 1], [-1, 0]], [[0, 1], [-1, 0], [0, 1]],

        [[-1, 0], [0, 1], [0, 1], [-1, 0]], [[1, 0], [0, -1], [0, -1], [1, 0]], # 2, 2
        [[1, 0], [0, 1], [0, 1], [1, 0]], [[-1, 0], [0, -1], [0, -1], [-1, 0]],

        [[-1, 0], [0, 1], [0, 1], [0, 1], [-1, 0]], [[1, 0], [0, -1], [0, -1],[0, -1], [1, 0]], # 2, 3
        [[1, 0], [0, 1], [0, 1], [0, 1], [1, 0]], [[-1, 0], [0, -1], [0, -1],[0, -1], [-1, 0]],  
    ]
    
    for i in range(len(dxys)): dxys.append(flipped(dxys[i]))
    
    for dxy in dxys:
        is_good_dxy = True
        new_x, new_y = number_one_position[0], number_one_position[1]
        for dx, dy in dxy:
            if not is_good_dxy: break
            
            try:
                new_x, new_y = new_x + dx, new_y + dy
                if new_x < 0 or new_y < 0: is_good_dxy = False
                if my_figure[new_x][new_y] == '0': is_good_dxy = False
            except: is_good_dxy = False

        if is_good_dxy:
            print(my_figure[new_x][new_y])
            break