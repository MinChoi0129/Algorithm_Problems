def rotated(array_2d) -> list: # 시계방향 90도 회전
    return [list(elem) for elem in zip(*array_2d[::-1])]

def flipped(array_2d) -> list: # 윗면 아랫면 뒤집기
    return [line[::-1] for line in array_2d]
    
def cleanFigureFromInput() -> list: # 불필요한 000...000 라인을 제거
    
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
    
    for i in range(11):# 11개에 대해 뒤집은 것 추가
        figures.append(flipped(figures[i]))

    for i in range(22): # 22개에 대해서 90도씩 회전한 것 추가
        arr90 = rotated(figures[i])
        arr180 = rotated(arr90)
        arr270 = rotated(arr180)
        figures.append(arr90)
        figures.append(arr180)
        figures.append(arr270)

    return figures

figures = getAllFigures()
my_figure = cleanFigureFromInput()

'''
my_figure의 자연수 부분들을 모두 '1'로 바꾼 전개도 복사본(tmp_figure)이
정육면체 전개도가 되긴 될 수 있는지 부터 파악
'''
tmp_figure = [['1' if my_figure[i][j] != '0' else '0' for j in range(len(my_figure[0]))] for i in range(len(my_figure))]
is_exist = True if tmp_figure in figures else False # 정육면체가 될 수 있는지 여부.

if not is_exist: print(0) # 정육면체 아님.
else: # 마주보는 면 찾기
    for x in range(len(my_figure)):
        for y in range(len(my_figure[0])):
            if my_figure[x][y] == '1': number_one_position = x, y # '1'의 좌표
    
    print(my_figure[마주보는면x][마주보는면y])