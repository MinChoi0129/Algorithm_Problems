#-*- encoding: utf-8 -*-
from cs1graphics import Canvas, Layer, Rectangle, Image, Text, Circle, Point
import os
import sys
import random as rd
from time import sleep

paper = Canvas()
paper.setWidth(1000) # 가로
paper.setHeight(600) # 세로
paper.setBackgroundColor("skyblue")

console_clear = "cls" if os.name == "nt" else "clear"

def execute():
    global paper
    paper.clear()
    os.system(console_clear)
    #####################################################
    Main = Layer()  
    start = Rectangle(200, 100, Point(275, 450))
    start.setFillColor('yellow')
    Main.add(start)
    way = Rectangle(200, 100, Point(525, 450))
    way.setFillColor('yellow')
    Main.add(way)
    paper.add(Main)

    Man = Layer()
    man = Image("python/man.png")
    Man.setDepth(80)
    Man.add(man)
    Man.moveTo(390,350)
    paper.add(Man)

    Txt = Layer()
    startTxt = Text("START", 30)
    startTxt.moveTo(275, 450) 
    Txt.add(startTxt)
    howplayTxt = Text("HOW PLAY", 30)
    howplayTxt.moveTo(525, 450)
    Txt.add(howplayTxt)
    numberTxt = Text("NUMBER", 45)
    numberTxt.moveTo(140, 320)
    Txt.add(numberTxt)
    baseballTxt = Text("BASEBALL", 45)
    baseballTxt.moveTo(660, 350)
    Txt.add(baseballTxt)

    # 구름
    Cloud = Layer()
    flcloud = Circle(30, Point(80, 70))
    slcloud = Circle(30, Point(130, 70))
    thlcloud = Circle(30, Point(180, 70))
    flcloud.setFillColor('white')
    slcloud.setFillColor('white')
    thlcloud.setFillColor('white')
    flcloud.setBorderColor('white')
    slcloud.setBorderColor('white')
    thlcloud.setBorderColor('white')
    Cloud.add(flcloud)
    Cloud.add(slcloud)
    Cloud.add(thlcloud)
    Cloud.scale(5)
    Cloud.moveTo(-250, 0)
    Cloud.setDepth(100)
    paper.add(Cloud)

    # 대화상자
    Input_a = Layer()
    input_bar = Rectangle(1000, 50, Point(500, 575))
    input_bar.setFillColor('black')
    input_bar.setBorderWidth(0)
    Input_a.add(input_bar)
    paper.add(Input_a)

    #명령 입력
    welcome = Text("☆☆☆ Welcome to Number Baseball Game!! ☆☆☆",20)
    welcome.moveTo(390,575)
    welcome.setFontColor("white")

    introduction1 = Text("게임을 시작하려면 '1'을 입력하세요",20)
    introduction1.moveTo(390,575)
    introduction1.setFontColor("white")

    introduction2 = Text("게임방법을 알고싶다면 '2'를 입력하세요",20)
    introduction2.moveTo(390,575)
    introduction2.setFontColor("white")

    introduction3 = Text("게임순위를 보고싶다면 '3'을 입력하세요",20)
    introduction3.moveTo(390,575)
    introduction3.setFontColor("white")

    introduction4 = Text("게임을 종료하려면 '4'를 입력하세요",20)
    introduction4.moveTo(390,575)
    introduction4.setFontColor("white")

    for _ in range(3):
        paper.add(Txt)
        sleep(0.5)
        paper.remove(Txt)
        sleep(0.5)

    paper.add(Txt)

    paper.add(welcome)
    sleep(2)
    paper.remove(welcome)
    paper.add(introduction1)
    sleep(2)
    paper.remove(introduction1)
    paper.add(introduction2)
    sleep(2)
    paper.remove(introduction2)
    paper.add(introduction3)
    sleep(2)
    paper.remove(introduction3)
    paper.add(introduction4)
    sleep(2)
    paper.remove(introduction4)

    #############################################################

    while True:
        try:
            choose_option = input("\n옵션을 선택해주세요 : ")
        except:
            os.system(console_clear)
            continue
        
        if choose_option == '1':
            while True:
                gs = game_start()
                if gs == -1:
                    execute()
                    return
        elif choose_option == '2':
            how_to_play()
            execute()
            return
        elif choose_option == '3':
            view_scores()
            execute()
            return
        elif choose_option == '4':
            os.system(console_clear)
            return

def game_start():
    user_name = ""
    while True:
        try:
            os.system(console_clear)
            user_name = input("플레이어의 이름을 입력해주세요 : ")
            ask = ""
        except:
            continue
        
        while True:
            try:
                os.system(console_clear)
                print("'" + user_name + "'" + " 이(가) 맞습니까? (Y / N) : ", end = "")
                ask = input()
            except:
                continue
            
            if ask in ["y", "Y"] or ask in ["n", "N"]:
                break
        if ask in ["y", "Y"]:
            break

    tries = playGame()

    f = open("best_user_score.txt", 'a', encoding='utf8')
    f.write("%s %d\n" % (user_name, tries))
    f.close()

    while True:
        try:
            retry = input("다시 시도 하시겠습니까? (Y / N) : ") # Canvas에 그림으로 표시할 예정
        except:
            os.system(console_clear)
            continue

        if retry in ["y", "Y"]:
            return 1
        elif retry in ["n", "N"]:
            return -1
        else:
            os.system(console_clear)
            print("올바른 입력이 아닙니다.")
            sleep(1)

def how_to_play():
    os.system(console_clear)

    # 수정 필요
    ############################################
    HowToPlay = Layer()
    HowToPlay_background = Image("python/how_to_back.png")
    HowToPlay_background.setDepth(100)
    HowToPlay_background.moveTo(500,300)
    what_is = Text("숫자 야구란?", 26)
    FirstTxt = Text("감춰진 3개의 숫자가 무엇인지 맞추는 게임입니다.", 26)
    wayTxt = Text("게임 방법", 26)
    SecondTxt = Text("1. 숫자는 0~9까지 구성되어 있으며, 각 숫자는 한번씩만 사용 가능합니다", 26)
    ThirdTxt = Text("2. 숫자와 자리의 위치가 맞으면 스트라이크(S), 숫자만 맞으면 볼(B) 입니다.", 26)
    FourthTxt = Text("3. 숫자가 하나도 맞지 않을 경우 아웃(OUT)으로 표시됩니다.", 26)

    HowToPlay.add(what_is)
    HowToPlay.add(FirstTxt)
    HowToPlay.add(wayTxt)
    HowToPlay.add(SecondTxt)
    HowToPlay.add(ThirdTxt)
    HowToPlay.add(FourthTxt)
    HowToPlay.add(HowToPlay_background)

    what_is.moveTo(500, 70)
    FirstTxt.moveTo(500, 150)
    wayTxt.moveTo(500, 230)
    SecondTxt.moveTo(500, 310)
    ThirdTxt.moveTo(500, 380)
    FourthTxt.moveTo(500, 450)
    paper.add(HowToPlay)
    ############################################
    # 수정 범위 끝

    print("메인으로 가려면 아무키나 입력하세요")
    try:
        go_main = sys.stdin.readline()
    except:
        pass
    print(go_main)

def view_scores():
    os.system(console_clear)

    # 수정 필요
    ##################################################
    
    userName = ""
    tries = 0

    show_result = [[userName, tries]]

    num_result = []
    name_result = []

    for i in range(len(show_result)):
        num_result.append(show_result[i][1])
        name_result.append(show_result[i][0])

    num_result.sort(reverse = True)
    
    print("등수\t이름\t점수")
    with open("best_user_score.txt", "w", encoding='utf8') as f:
        for i in range(len(num_result)): 
            sort_show_result = [str(i+1) + "등   " + str(name_result[i])+ "    " + str(num_result[i])]
            f.write(str(sort_show_result))
            f.write("\n")

    with open("best_user_score.txt", "r", encoding='utf8') as f:
        contend = f.read()
        print(contend)
        f.close()
    
    ##################################################
    # 수정 범위 끝

    print("메인으로 가려면 아무키나 입력하세요")
    try:
        go_main = sys.stdin.readline()
    except:
        pass
    print(go_main)

def __getRandomNumber(count):
    randomList = rd.sample([i for i in range(0, 10)], count) # 0 ~ 9 랜덤하게 중복x로 count 자릿수만큼 뽑음
    returnStr = "".join([str(i) for i in randomList])
    return returnStr # return type == str ex) 8145 or 127

def checkCondition(predictedNumber, givenNumber):
    balls = strikes = outs = 0

    for i in range(len(givenNumber)):
        for j in range(len(predictedNumber)):
            if givenNumber[i] == predictedNumber[j]: #같은 숫자 발견
                if i == j: #같은 위치 && 같은 숫자(스트라이크 조건)
                    strikes += 1
                else:      #다른 위치 && 같은 숫자(볼 조건)
                    balls += 1

    if strikes == 0 and balls == 0:
        outs = 1
    else:
        outs = 0

    return [strikes, balls, outs]

def playGame():  
    balls = 0
    strikes = 0
    tries = 0
    predictedNumber = " "
    givenNumber = " "
    ask = ""
    while True:
        os.system(console_clear)
        try:
            ask = input("자릿수를 입력해주세요 (3 또는 4) : ")
        except:
            continue
        
        if ask == '3' or ask == '4':
            break

    givenNumber = __getRandomNumber(int(ask))
    for i in range(5, 0, -1):
        os.system(console_clear)
        print(str(len(givenNumber)) + "자리수 게임으로 설정하였습니다!")
        print(str(i) + "초후 게임이 시작됩니다!")
        sleep(1)

    # 숫자 맞추기 시작
    while True:
        while True:
            os.system(console_clear)
            print("정답 = " + givenNumber) #for debug, 정답
            try:
                predictedNumber = input("숫자를 추측하세요 :")
                if len(givenNumber) != len(predictedNumber):
                  print(str(len(givenNumber)) + "자리수로 입력해주세요")
                  sleep(1)
                  continue
            except:
                continue

            on_off = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in predictedNumber:
                if int(i) in [j for j in range(0, 10)]:
                    on_off[int(i)] += 1
            
            isDuplicate = False
            for i in on_off:
                if i >= 2:
                    print("중복된 입력은 불가능합니다")
                    sleep(1)
                    isDuplicate = True
                    break
            if not isDuplicate:
                tries += 1
                break            

        condition = checkCondition(predictedNumber, givenNumber)

        strikes, balls, out = condition[0], condition[1], condition[2]

        if out == 1:
            print("OUT") # Canvas에 그림으로 표시할 예정
            sleep(3)
        else:
            if strikes == len(givenNumber):
                print("정답입니다!!") # Canvas에 그림으로 표시할 예정
                print(str(tries) + "번 시도하셨습니다!!")
                return tries
            else:
                for i in range(3, 0, -1):
                    os.system(console_clear)
                    print(str(strikes) + "S " + str(balls) + "B") # Canvas에 그림으로 표시할 예정
                    print(str(i) + "초뒤 사라집니다.")
                    sleep(1)

execute()