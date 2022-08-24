def rotated(array_2d):
    return [list(elem) for elem in zip(*array_2d[::-1])]

def flipped(array_2d):
    return [line[::-1] for line in array_2d]
    
def setBoards() -> list:
    tmp_boards = []
    tmp_board = []
    for i in range(18):
        line = input().split()
        if line != list('000000'):
            tmp_board.append(line)
        if (i + 1) % 6 == 0:
            tmp_boards.append(tmp_board)
            tmp_board = []

    for i in range(len(tmp_boards)):
        rotated_board = []  
        for line in rotated(tmp_boards[i]):
            if line != ['0'] * len(line):
                rotated_board.append(line)        
        tmp_boards[i] = rotated_board
             
    return tmp_boards

answers = [\
    [list('1000'), list('1111'), list('1000')], [list('0100'), list('1111'), list('1000')], [list('0010'), list('1111'), list('1000')], \
    [list('0001'), list('1111'), list('1000')], [list('0100'), list('1111'), list('0100')], [list('0010'), list('1111'), list('0100')], \
    [list('0011'), list('0110'), list('1100')], [list('0011'), list('1110'), list('1000')], [list('1100'), list('0111'), list('0100')], \
    [list('0100'), list('1110'), list('0011')], [list('00111'), list('11100')]
]
my_cubes = setBoards()

for i in range(11):
    answers.append(flipped(answers[i]))

for i in range(22):
    arr90 = rotated(answers[i])
    arr180 = rotated(arr90)
    arr270 = rotated(arr180)
    answers.append(arr90)
    answers.append(arr180)
    answers.append(arr270)
    
for cube in my_cubes:
    print("yes" if cube in answers else "no")
