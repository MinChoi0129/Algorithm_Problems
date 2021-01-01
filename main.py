import pygame, time, sys, os
from datetime import datetime

pygame.init()
window = pygame.display.set_mode((800, 600)) # window == 화면 이름
pygame.display.set_caption("오목게임")

# 이미지 로딩
main_bg_img = pygame.image.load("./images/background/5mok.png")
back_img = pygame.image.load("./images/background/HTP_bg.png")
back_play_img = pygame.image.load("./images/background/play_back.png")
start_btn_img = pygame.image.load("./images/background/start.png")
rule_btn_img = pygame.image.load("./images/background/rule.png")
record_btn_img = pygame.image.load("./images/background/record.png")
exit_btn_img = pygame.image.load("./images/background/exit.png")
back_btn_img = pygame.image.load("./images/background/back.png")
back2_btn_img = pygame.image.load("./images/background/back2.png")
see_btn_img = pygame.image.load("./images/background/see.png")
table_img = pygame.image.load("./images/play/table.png")
output_img = pygame.image.load("./images/background/output.png")
s_black_img = pygame.image.load("./images/play/s_black.png")
s_white_img = pygame.image.load("./images/play/s_white.png")
stateBox_img = pygame.image.load("./images/state/stateBox.png")
winner_img = pygame.image.load("./images/state/winner.png")
#기권_img = pygame.image.load("./images/background/기권.png")

# 전역변수
count = 0 # 수
username1 = "" # 유저1
username2 = "" # 유저2
turn = "BLACK" # 차례(시작 : 흑)
board = [['·' for i in range(19)] for j in range(19)] # 오목 판 상황 이중 리스트
clear_cmd = "cls" if os.name == "nt" else "clear"

class 버튼:
    def __init__(self, 윈도우, 버튼이미지, 좌표 = (0, 0), 실행할함수 = None, 일회성 = -1):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 좌표[0] + 버튼이미지.get_width() > mouse[0] > 좌표[0] and 좌표[1] + 버튼이미지.get_height() > mouse[1] > 좌표[1]:
            윈도우.blit(버튼이미지, (좌표[0], 좌표[1]))
            if click[0]:
                if 실행할함수 != None:
                    time.sleep(0.5)
                    if 실행할함수 == show_daeguk:
                        print("이 버튼의 대국번호 : 최신 - ", 일회성 - 1) # debug
                        show_daeguk(일회성)
                    else:
                        실행할함수()
        else:
            윈도우.blit(버튼이미지, (좌표[0], 좌표[1]))

def mainmenu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        window.blit(main_bg_img, (0, 0))
        버튼(window, start_btn_img, (410, 480), game_start)
        버튼(window, rule_btn_img, (515, 410), how_to_play)
        버튼(window, record_btn_img, (615, 430), all_daeguks)
        버튼(window, exit_btn_img, (510, 500), quitcmd)
        pygame.display.update()

def initialize():  # 전역변수 매 게임마다 초기화
    #game_start와 병합하는건 어떻슴까
    global count, username1, username2, turn, board
    count = 0
    username1 = ""
    username2 = ""
    turn = "BLACK"
    board = [['·' for i in range(19)] for j in range(19)]

def game_start(): #GUI화 필요
    global count, username1, username2, turn, board
    count = 0
    username1 = ""
    username2 = ""
    turn = "BLACK"
    board = [['·' for i in range(19)] for j in range(19)]
    evaluationResult = -1
    #############################################################################################################
    #시작 화면

    #사용자 이름 입력
    username1 = input("사용자1 이름: ")
    username1 = input("사용자2 이름: ")

    print("게임을 시작합니다.")
    #############################################################################################################
    
    while True:
        #############################################################################################################
        #현재 차례 안내
        if turn == "BLACK":
          print("흑의 차례입니다.")
        else:
          print("백의 차례입니다.")

        #좌표 입력
        '''
        [[--*]                  board의 내용이
        [---]                   일 때 *의 좌표가
        [---]]                  (0,2)가 되도록 해주십쇼..
        '''
        placingAxis = input("착수할 좌표 입력(x, y):").split(',')
        placingAxis[0] = int(placingAxis[0]) #x좌표
        placingAxis[1] = int(placingAxis[1]) #y좌표
        #############################################################################################################

        if turn == "BLACK": board[placingAxis[0]][placingAxis[1]] = '●'
        else: board[placingAxis[0]][placingAxis[1]] = '○'

        evaluationResult = __evaluate(placingAxis)

        #착수 후 상황 출력############################################################################################
        print(board)
        #############################################################################################################

        if evaluationResult == 1 or evaluationResult == 2: #승자가 가려졌을 경우
            game_over(evaluationResult)
            break
        else:
            turn = "WHITE" if turn == "BLACK" else "BLACK"
            continue
           
def __evaluate(placingAxis):
    #현재 게임을 평가하는 메서드
    #game_start 내부에서 사용
    #리턴 값: 0: 계속 진행 / 1: 흑 승 / 2: 백 승
    #placingAxis: (list) [x좌표, x좌표] - 착수한 돌의 좌표
    #내부 변수 x, y는 pygame에서의 그것과 같음
    #호출 시(placingAxis의 x, y값) game_records에서의 좌표로 호출하면 됨

    if type(placingAxis) is not list:
      print("__evaluate: 입력값이 유효하지 않음 - 매개 변수는 반드시 list여야 함")
      raise Exception

    try:
        #game_record의 좌표를 pygame의 좌표로 바꾸어서 진행
        x = int(placingAxis[1])
        y = int(placingAxis[0])
    except:
        print("__evaluate: 입력값이 유효하지 않음 - 좌표값은 반드시 숫자여야 함")
        raise Exception

    global board
    eachLine = "" #각 탐색이 끝날 때 마다 빈 문자열로 초기화
    boardSize = len(board)

    #방금 착수한 돌이 속한 줄만 탐색하면 됨 => 착수한 돌의 좌표값을 필요로 하는 이유
    #모든 탐색은 각 줄을 문자열로 바꾼 후 패턴을 비교하는 방법을 사용함

    #가로 탐색
    for i in board[x]: eachLine += i
    if eachLine.find("●●●●●") != -1: return 1
    elif eachLine.find("○○○○○") != -1: return 2
    
    #세로 탐색
    eachLine = ""
    for i in range(boardSize): eachLine += board[i][y]
    if eachLine.find("●●●●●") != -1: return 1
    elif eachLine.find("○○○○○") != -1: return 2

    eachLine = ""

    #대각선 탐색 - '\' 방향
    while x > 0 and y > 0: #대각선의 한 쪽 끝까지 이동
        x -= 1
        y -= 1

    for i in range(boardSize):
        if x >= boardSize or y >= boardSize: break
        eachLine += board[x][y]
        x += 1
        y += 1

    if eachLine.find("●●●●●") != -1: return 1
    elif eachLine.find("○○○○○") != -1: return 2

    eachLine = ""
    x = placingAxis[0]
    y = placingAxis[1]

    #대각선 탐색 - '/' 방향
    while x < boardSize and y > 0: #대각선의 한 쪽 끝까지 이동
        x += 1
        y -= 1

    for i in range(boardSize):
        if x < 0 or y >= boardSize: break
        eachLine += board[x][y]
        x -= 1
        y += 1
    
    if eachLine.find("●●●●●") != -1: return 1
    elif eachLine.find("○○○○○") != -1: return 2

    #여기까지 왔다 == 게임 계속 진행
    return 0
def game_over(result): #GUI화 필요
    #게임이 끝났을 경우 호출되는 메서드
    #result가 1이면 흑 승 / 2이면 백 승
    print("게임이 끝났습니다.\n결과를 기록하고 있습니다..")

    #현재 대국 기록 후
    record_daeguk()

    #메인으로 이동
    mainmenu()

def how_to_play():
    print("게임방법입니다.")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.blit(back_img, (0, 0))
        font = pygame.font.Font('paybooc Bold.ttf', 20)
        title = font.render("<오목 게임>", True, (255, 212, 0))
        texts = []
        texts.append(font.render("1. 2명에서 하는 게임으로, 검은색 알을 가진 사람이 먼저 시작한다.",  True, (255, 212, 0)))
        texts.append(font.render("2. 알은 선의 교차점에 놓고, 첫 점은 한 가운데에 두는 것이 일반적이다.", True, (255, 212, 0)))
        texts.append(font.render("3. 자기의 알이 양쪽으로 3개 or 4개가 연이어 놓이면 상대방에게 알려준다", True, (255, 212, 0)))
        texts.append(font.render("4. 한 알이 놓이면서 쌍삼(3-3)이 되는 수는 두지 못한다.", True, (255, 212, 0)))
        texts.append(font.render("5. 먼저 자기 알 5개를 가로나 세로, 대각선 중 한 방향으로 연이어 놓는 사람이 승!", True, (255, 212, 0)))

        axis = 80
        for text in texts:
            center = text.get_rect()
            center.center = (400, axis)
            window.blit(text, center)
            axis += 80

        버튼(window, back_btn_img, (700, 30), mainmenu)
        pygame.display.update()

def all_daeguks():

    file_len = 0
    font = pygame.font.Font('paybooc Bold.ttf', 20)

    print("게임 결과 요약입니다.")
    with open("game_records.txt", 'r', encoding='utf-8') as f:
        num_of_daeguks = 0
        for i in f: num_of_daeguks += 1
    
    run = True
    with open("game_records.txt", 'r', encoding='utf-8') as f:
        contents = list()
        new_contents = list()

        while True:
            content = f.readline()

            if content:
                contents.append(content)
                file_len += 1
            else:
                break


    for j in range(file_len):
        if 'BLACK' in contents[j] or 'WHITE' in contents[j]:
            sep_content = contents[j].split()
            new_contents.append(sep_content)
    
    new_contents.reverse()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            
        window.blit(back_img, (0, 0))

        output_index = 0
        output_place = 10

        if num_of_daeguks // 21 > 7:
            for i in range(7):
                버튼(window, see_btn_img, (600, 100 + 60 * i), show_daeguk, i + 1)
                버튼(window, output_img, (150, 100 + 60 * i))
                title = font.render(new_contents[output_index][3] + ' ' + new_contents[output_index][0] + ' ' + 'VS' + ' ' + new_contents[output_index][1], True, (255, 212, 0))
                Title_center = title.get_rect()
                Title_center.center = (350, 115 + output_place)
                window.blit(title, Title_center)
                output_index += 1
                output_place += 60
        else:
            for i in range(num_of_daeguks // 21):
                버튼(window, see_btn_img, (600, 100 + 60 * i), show_daeguk, i + 1)
                버튼(window, output_img, (150, 100 + 60 * i))
                title = font.render(new_contents[output_index][3] + ' ' + new_contents[output_index][0] + ' ' + 'VS' + ' ' + new_contents[output_index][1], True, (255, 212, 0))
                Title_center = title.get_rect()
                Title_center.center = (350, 115 + output_place)
                window.blit(title, Title_center)
                output_index += 1
                output_place += 60

        버튼(window, back_btn_img, (700, 30), mainmenu)
        pygame.display.update()
                
def record_daeguk():  # 완성
    global count, username1, username2, turn, board

    now = datetime.now().strftime('%Y-%m-%d')  # 오늘 날짜
    winner = "BLACK" if turn == "WHITE" else "WHITE"  # 승자

    f = open("game_records.txt", "a+", encoding='utf-8')
    write_data = "%s %s %s %s %d\n" % (
        username1, username2, winner, now, count)  # 유저1 유저2 승자 날짜 n수 기록
    f.write(write_data)

    # 보드 상황 기록
    for x in range(19):
        for y in range(18):
            f.write("%c " % str(board[x][y]))
        f.write("%c\n" % str(board[x][18]))
    f.write("\n")
    f.close()

def show_daeguk(getin):  # 모든 대국 중 원하는 대국을 자세히 보기
    num_of_daeguks = 0

    with open("game_records.txt", 'r', encoding='utf-8') as f:
        contents = f.readlines()
        for i in contents:
            num_of_daeguks += 1
    
    num_of_daeguks = num_of_daeguks // 21
    print("nod :", num_of_daeguks)
    daeguk_number = num_of_daeguks - (getin - 1)
    
    game_result = []
    g = open("game_records.txt", 'r', encoding='utf-8')
    start_line = 21 * (daeguk_number - 1)
    for i in range(start_line):  # 줄 건너뛰기
        g.readline()

    t = list(g.readline().split())  # 대국 정보(유저1 유저2 승자 날짜 n수)
    game_result.append(t)
    for i in range(19):
        game_result.append(list(g.readline().split()))
    g.close()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.blit(back_play_img, (0, 0))
        window.blit(stateBox_img, (612, 0))
        window.blit(winner_img, (646, 200))
        if game_result[0][2] == "BLACK":
            window.blit(s_black_img, (695, 270))
        else:
            window.blit(s_white_img, (695, 270))
        window.blit(table_img, (22, 22))
        for x in range(1, 20):
            for y in range(19):
                print("x, y =", x, y)
                if game_result[x][y] == "●":  # 흑
                    y += 1
                    x1 = ((x // 2) * 26 + ((x // 2) - 1) * 25 +
                        69) if x % 2 == 0 else ((x // 2) * 26 + (x // 2) * 25 + 69)
                    y1 = ((y // 2) * 26 + ((y // 2) - 1) * 25 +
                        69) if y % 2 == 0 else ((y // 2) * 26 + (y // 2) * 25 + 69)
                    black_center = s_black_img.get_rect()
                    black_center.center = (y1,x1)
                    window.blit(s_black_img, black_center)
                elif game_result[x][y] == "○":  # 백
                    y += 1
                    x1 = ((x // 2) * 26 + ((x // 2) - 1) * 25 +
                        69) if x % 2 == 0 else ((x // 2) * 26 + (x // 2) * 25 + 69)
                    y1 = ((y // 2) * 26 + ((y // 2) - 1) * 25 +
                        69) if y % 2 == 0 else ((y // 2) * 26 + (y // 2) * 25 + 69)
                    white_center = s_white_img.get_rect()
                    white_center.center = (y1,x1)
                    window.blit(s_white_img, white_center)
        버튼(window, back2_btn_img, (700, 30), all_daeguks)
        pygame.display.update()
        
        pygame.display.update()
 
def quitcmd():
    print("종료합니다.")
    pygame.quit()
    sys.exit()

mainmenu()