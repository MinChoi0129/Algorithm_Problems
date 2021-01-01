import pygame, time, sys
from datetime import datetime

pygame.init()
window = pygame.display.set_mode((800, 600)) # window == 화면 이름
pygame.display.set_caption("오목게임")

# 이미지 로딩
main_bg_img = pygame.image.load("./images/background/5mok.png")
back_img = pygame.image.load("./images/background/HTP_bg.png")
start_btn_img = pygame.image.load("./images/background/start.png")
rule_btn_img = pygame.image.load("./images/background/rule.png")
record_btn_img = pygame.image.load("./images/background/record.png")
exit_btn_img = pygame.image.load("./images/background/exit.png")
back_btn_img = pygame.image.load("./images/background/back.png")
see_btn_img = pygame.image.load("./images/background/see.png")

# 전역변수
count = 0 # 수
username1 = "" # 유저1
username2 = "" # 유저2
turn = "BLACK" # 차례(시작 : 흑)
board = [['·' for i in range(19)] for j in range(19)] # 오목 판 상황 이중 리스트

class 버튼:
    def __init__(self, 윈도우, 버튼이미지, 좌표 = (0, 0), 실행할함수 = None, 일회성 = -1):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 좌표[0] + 버튼이미지.get_width() > mouse[0] > 좌표[0] and 좌표[1] + 버튼이미지.get_height() > mouse[1] > 좌표[1]:
            윈도우.blit(버튼이미지, (좌표[0], 좌표[1]))
            if click[0]:
                if 실행할함수 != None:
                    time.sleep(0.3)
                    if 실행할함수 == show_daeguk:
                        print("이 버튼의 대국번호 : 최신 - ", 일회성 - 1)
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

def initialize():  # 전역변수 초기화
    global count, username1, username2, turn, board
    count = 0
    username1 = ""
    username2 = ""
    turn = "BLACK"
    board = [['·' for i in range(19)] for j in range(19)]

def game_start():
    initialize()
    
    print("시작을 눌렀습니다.")
    
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
        FirstTxt = font.render("1. 2명에서 하는 게임으로, 검은색 알을 가진 사람이 먼저 시작한다.",  True, (255, 212, 0))
        SecondTxt = font.render("2. 알은 선의 교차점에 놓고, 첫 점은 한 가운데에 두는 것이 일반적이다.", True, (255, 212, 0))
        ThirdTxt = font.render("3. 자기의 알이 양쪽으로 3개 or 4개가 연이어 놓이면 상대방에게 알려준다", True, (255, 212, 0))
        FourthTxt = font.render("4. 한 알이 놓이면서 쌍삼(3-3)이 되는 수는 두지 못한다.", True, (255, 212, 0))
        FifthTxt = font.render("5. 먼저 자기 알 5개를 가로나 세로, 대각선 중 한 방향으로 연이어 놓는 사람이 승!", True, (255, 212, 0))

        Title_center = title.get_rect()
        Title_center.center = (400, 80)
        window.blit(title, Title_center)

        FirstTxt_center = FirstTxt.get_rect()
        FirstTxt_center.center = (400, 160)
        window.blit(FirstTxt, FirstTxt_center)

        SecondTxt_center = SecondTxt.get_rect()
        SecondTxt_center.center = (400, 240)
        window.blit(SecondTxt, SecondTxt_center)

        ThirdTxt_center = ThirdTxt.get_rect()
        ThirdTxt_center.center = (400, 320)
        window.blit(ThirdTxt, ThirdTxt_center)

        FourthTxt_center = FourthTxt.get_rect()
        FourthTxt_center.center = (400, 400)
        window.blit(FourthTxt, FourthTxt_center)

        FifthTxt_center = FifthTxt.get_rect()
        FifthTxt_center.center = (400, 480)
        window.blit(FifthTxt, FifthTxt_center)

        버튼(window, back_btn_img, (700, 30), mainmenu)
        
        pygame.display.update()

def all_daeguks():
    print("게임 결과 요약입니다.")
    f = open("game_records.txt", 'r', encoding='utf-8')
    num_of_daeguks = 0
    for i in f:
        num_of_daeguks += 1
    f.close()
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            
        window.blit(back_img, (0, 0))
        if num_of_daeguks // 21 > 10:
            pass # 방법 1, 2 선택
        else:
            for i in range(num_of_daeguks // 21):
                버튼(window, see_btn_img, (500, 100 + 60 * i), show_daeguk, i + 1)
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
    
    f = open("game_records.txt", 'r', encoding='utf-8')
    num_of_daeguks = 0
    for i in f:
        num_of_daeguks += 1
    f.close()
    
    daeguk_number = num_of_daeguks // 21 - (getin - 1)
    
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
    
    # debug
    for i in game_result:
        print(i)

def quitcmd():
    print("종료합니다.")
    pygame.quit()
    sys.exit()

mainmenu()