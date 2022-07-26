from copy import deepcopy as DC

def rotated(array_2d):
    return [list(elem) for elem in zip(*array_2d[::-1])]

def flipped(array_2d):
    return [line[::-1] for line in array_2d]
    
def getCleanCubeFromInput() -> list:
    board = []
    for i in range(6):
        line = input().split()
        if line != ['0'] * 6:
            board.append(line)

    rotated_board = []  
    for line in rotated(board):
        if line != ['0'] * len(line):
            rotated_board.append(line)        
    return rotated_board

def getAnswers():
    answers = [\
        [list('1000'), list('1111'), list('1000')], [list('0100'), list('1111'), list('1000')], [list('0010'), list('1111'), list('1000')], \
        [list('0001'), list('1111'), list('1000')], [list('0100'), list('1111'), list('0100')], [list('0010'), list('1111'), list('0100')], \
        [list('0011'), list('0110'), list('1100')], [list('0011'), list('1110'), list('1000')], [list('1100'), list('0111'), list('0100')], \
        [list('0100'), list('1110'), list('0011')], [list('00111'), list('11100')]
    ] # 기본 전개도
    
    for i in range(11): # 뒤집기
        answers.append(flipped(answers[i]))

    for i in range(22): # 돌리기
        arr90 = rotated(answers[i])
        arr180 = rotated(arr90)
        arr270 = rotated(arr180)
        answers.append(arr90)
        answers.append(arr180)
        answers.append(arr270)

    return answers


answers = getAnswers()
cube = getCleanCubeFromInput()
new_cube = DC(cube) # 임시로 사용할 cube

# 자연수를 모두 '1'로 바꿔 정육면체가 되긴 될 수 있는지 파악.
for i in range(len(new_cube)):
    for j in range(len(new_cube[0])):
        if new_cube[i][j] != '0': new_cube[i][j] = '1'

is_exist = True if new_cube in answers else False # 정육면체가 될 수 있는지 여부.

if not is_exist: print(0)
else: # 마주보는 면 찾기
    for x in range(len(cube)):
        for y in range(len(cube[0])):
            if cube[x][y] == '1': one_position = x, y

    print(one_position) # '1'의 좌표
    