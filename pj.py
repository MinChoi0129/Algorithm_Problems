import os
from time import sleep
current_stone_color = "black"
board = []

def game_init():
    global board
    global current_stone_color
    os.system("cls")
    board = [["·" for i in range(15)] for j in range(15)] # 보드 초기화
    current_stone_color = "black" # 흑 선 초기화
    
def print_board():
    global board
    global current_stone_color
    os.system("cls")
    ##########################################################################
    print("")
    print("------------------- 오 목 게 임 -------------------")
    if current_stone_color == "black":
        print("                <현재 차례 : 흑(●)>                ")
    else:
        print("                <현재 차례 : 백(○)>                ")
    print(" y")
    for i in range(15):
        print("%2d" % (15 - i), end = " ")
        for j in range(15):
            print("%2s" % (board[i][j]), end = " ")
        print("")
    print("  ", end = " ")
    for i in range(15):
        print("%2d" % (i + 1), end = " ")
    print(" x")
    ##########################################################################

def put_stone(x, y):
    global board
    global current_stone_color
    if board[(16 - y) - 1][(x) - 1] == "·":
        if current_stone_color == "black":
            board[(16 - y) - 1][(x) - 1] = "●"
            current_stone_color = "white"
        else:
            board[(16 - y) - 1][(x) - 1] = "○"
            current_stone_color = "black"
    else:
        print("이 위치에 이미 돌이 있습니다!")
        sleep(1)

def game_main():
    game_init()
    print(" ☆☆☆ 오목게임에 오신 것을 환영합니다!!! ☆☆☆ ")
    print("1 : How To Play")
    print("2 : Game Start")
    print("3 : Ranking")
    print("4 : Exit")
    
    while True:
        ask = int(input(">>> "))
        if ask == 1:
            result = how_to_play()
            if result == "main":
                game_main()
                break
        elif ask == 2:
            result = game_start()
            if result == "exit":
                return
            elif result == "main":
                game_main()
                break
        elif ask == 3:
            result = show_rank()
            if result == "main":
                game_main()
                break
        elif ask == 4:
            break
    return

def how_to_play():
    os.system("cls")
    print("이렇게 하는거에요")
    ### 내용 추가 ###
    while True:
        print("m을 누르면 메인으로 갑니다")
        ask = input(">>> ")
        if ask == "m":
            return "main"
        else:
            os.system("cls")
            
def game_start():
    global board
    global current_stone_color    
    while True:
        print_board()
        
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            os.system("cls")
            if current_stone_color == "black":
                print("흑(●)이 기권하였습니다. 백(○) 승리!!")
            else:
                print("백(○)이 기권하였습니다. 흑(●) 승리!!")
                
            while True:
                print("게임종료 : 1 / 메인화면 : 2")
                ask = int(input(">>> "))
                if ask == 1:
                    return "exit"
                elif ask == 2:
                    return "main"
                else:
                    os.system("cls")
                    
        if x > 15 or y > 15 or x < 1 or y < 1:
            continue
        else:
            put_stone(x, y)
            condition = check_condition()
            if condition[0] == "gameover":
                print_board()
                print("!!GAME OVER!!")
                print("Winner : 흑(●) / Loser : 백(○)") if condition[1] == "white" else print("Winner : 백(○) / Loser : 흑(●)")
                """
                put_stone 함수에서 돌을 놓은 후 돌 색을 바꾸기 때문에
                condition[1]에는 마지막에 둔 사람이 아닌 사람(혹은 게임이 끝난 경우, 진 사람)이 들어옴
                """

def show_rank():
    os.system("cls")
    print("순위는 이렇습니다")
    ### 내용 추가 ###
    while True:
        print("m을 누르면 메인으로 갑니다")
        ask = input(">>> ")
        if ask == "m":
            return "main"
        else:
            os.system("cls")

def check_condition():
    global board
    global current_stone_color
    status = False
    
    
    
    if status:
        return ["gameover", current_stone_color]
    else:
        return ["go_on", current_stone_color]

game_main()