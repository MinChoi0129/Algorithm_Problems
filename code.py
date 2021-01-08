#-*- encoding: utf-8 -*-
from cs1graphics import Canvas, Layer, Rectangle, Image, Text, Circle, Point
import os, sys
import random as rd
from time import sleep

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

################################## Initializing Variables ##################################

paper = Canvas()
userName = givenNumber = predictedNumber = ""
balls = strikes = tries = 0
console_clear = "cls" if os.name == "nt" else "clear"

##################################### Display Functions #####################################

def image_set(name_image):   # 이미지 기본 셋팅
  global paper
  name_image.moveTo(400,300)  
  name_image.setDepth(50)   
  paper.add(name_image)

def displayFix(name_image):  #고정멘트 이미지 추가
  global fix
  fix = Image(resource_path("images/fix/"+name_image+".png"))
  image_set(fix)
  return

def displayCheck(name_image): #비고정멘트 이미지 추가
  global check
  check = Image(resource_path("images/check/"+name_image+".png"))
  image_set(check)
  return

def displayInit(): #그래픽 초기 설정 메소드
  global paper
  paper.setWidth(800)  # 가로
  paper.setHeight(600)  # 세로
  paper.setBackgroundColor("skyblue")

def displayingame():   # 인게임 바탕화면
  global paper
  background_image = Image(resource_path("images/image/background.png"))
  image_set(background_image)

def displayMainScreen():  # 게임 메인 화면(메뉴)
  global paper

  paper.clear()
  Main = Layer()

  start = Rectangle(150, 100, Point(115, 450))
  start.setFillColor('yellow')
  Main.add(start)
  way = Rectangle(150, 100, Point(305, 450))
  way.setFillColor('yellow')
  Main.add(way)
  score = Rectangle(150, 100, Point(495, 450))
  score.setFillColor('yellow')
  Main.add(score)
  exit = Rectangle(150, 100, Point(685, 450))
  exit.setFillColor('yellow')
  Main.add(exit)
  paper.add(Main)

  Man = Layer()
  man = Image(resource_path("images/man.png"))
  Man.setDepth(80)
  Man.add(man)
  Man.moveTo(390,350)
  paper.add(Man)

  Txt = Layer()
  startTxt = Text("1. START", 25)
  startTxt.moveTo(115, 450) 
  Txt.add(startTxt)
  howplayTxt = Text("2. HOW", 25)
  howplayTxt.moveTo(305, 450)
  Txt.add(howplayTxt)
  numberTxt = Text("NUMBER", 45)
  numberTxt.moveTo(140, 320)
  Txt.add(numberTxt)
  baseballTxt = Text("BASEBALL", 45)
  baseballTxt.moveTo(660, 350)
  Txt.add(baseballTxt)
  scoreTxt = Text("3. SCORE", 25)
  scoreTxt.moveTo(495, 450)
  Txt.add(scoreTxt)
  exitTxt = Text("4. EXIT", 25)
  exitTxt.moveTo(685, 450)
  Txt.add(exitTxt)

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

  introduction5 = Text("옵션을 선택해주세요!",20)
  introduction5.moveTo(390,575)
  introduction5.setFontColor("white")

  for _ in range(3):
    paper.add(Txt)
    sleep(0.5)
    paper.remove(Txt)
    sleep(0.5)

  paper.add(Txt)

  paper.add(welcome)
  sleep(1.5)
  paper.remove(welcome)
  paper.add(introduction1)
  sleep(1.5)
  paper.remove(introduction1)
  paper.add(introduction2)
  sleep(1.5)
  paper.remove(introduction2)
  paper.add(introduction3)
  sleep(1.5)
  paper.remove(introduction3)
  paper.add(introduction4)
  sleep(1.5)
  paper.remove(introduction4)
  sleep(1.5)
  paper.add(introduction5)
  return

def displayHowToPlay():  # 게임 방법을 알려주는 화면
  global paper

  paper.clear()
  HowToPlay = Layer()
  HowToPlay_background = Image(resource_path("images/how_to_back.png"))
  HowToPlay_background.setDepth(100)
  HowToPlay_background.moveTo(400, 300)
  what_is = Text("숫자 야구란?", 20)
  FirstTxt = Text("감춰진 3개의 숫자가 무엇인지 맞추는 게임입니다.", 20)
  wayTxt = Text("게임 방법", 20)
  SecondTxt = Text("1. 숫자는 0~9까지 구성되어 있으며, 각 숫자는 한번씩만 사용 가능합니다", 20)
  ThirdTxt = Text("2. 숫자와 자리의 위치가 맞으면 스트라이크(S), 숫자만 맞으면 볼(B) 입니다.", 20)
  FourthTxt = Text("3. 숫자가 하나도 맞지 않을 경우 아웃(OUT)으로 표시됩니다.", 20)

  HowToPlay.add(what_is)
  HowToPlay.add(FirstTxt)
  HowToPlay.add(wayTxt)
  HowToPlay.add(SecondTxt)
  HowToPlay.add(ThirdTxt)
  HowToPlay.add(FourthTxt)
  HowToPlay.add(HowToPlay_background)

  what_is.moveTo(400, 80)
  FirstTxt.moveTo(400, 160)
  wayTxt.moveTo(400, 240)
  SecondTxt.moveTo(400, 320)
  ThirdTxt.moveTo(400, 390)
  FourthTxt.moveTo(400, 460)
  paper.add(HowToPlay)
  return

def displayRetry():  # 게임 오버 후 새 게임 시작 여부를 묻는 화면
  global paper
  retry_image = Image(resource_path("images/image/retry.png"))   # Try Again? 이미지
  image_set(retry_image)

def displayStartGame(): # 게임 설정 완료 후 게임 진행 화면으로 이동
  global givenNumber
  return

def displayOutSituation():  # 예측 숫자 입력 결과가 '아웃'일 때 화면
  global paper
  out_image = Image(resource_path("images/image/out.png"))
  image_set(out_image)
  sleep(1)
  paper.remove(out_image)
  return

def displayGameOverByWinning():  # 정답을 맞추어 게임이 끝났을 때 화면
  global paper
  end_image = Image(resource_path("images/image/end.png"))
  image_set(end_image)
  sleep(3)
  paper.remove(end_image)
  return

def displayEvaluationResult(): # 스트라이크, 볼, 아웃 화면
  global strikes, balls, paper
  judge_image = Image(resource_path("images/image/judge.png"))   # 볼 스트라이크 판정 이미지
  image_set(judge_image)

  directory_s = resource_path("images/num/num" + str(strikes) + "_s.png")
  directory_b = resource_path("images/num/num" + str(balls) + "_b.png")
  strike_num_image = Image(directory_s)
  ball_num_image = Image(directory_b)

  image_set(strike_num_image)
  image_set(ball_num_image)
  
  for i in range(3, 0, -1):
    __clear()                    
    print(i, "초 뒤 사라집니다.")
    sleep(1)
  paper.remove(judge_image)
  paper.remove(strike_num_image)
  paper.remove(ball_num_image)
  return

def displayNameCheck(): #'이름 이(가) 맞습니까?' 화면
  displayCheck("namecheck")
  
  global l_nameCheck
  l_nameCheck = Layer()
  
  nameBox = Rectangle(230,50,Point(148,255))
  nameBox.setBorderWidth(3)
  nameCk = Text(str(userName),40)
  nameCk.moveTo(148,255)

  l_nameCheck.add(nameBox)
  l_nameCheck.add(nameCk)
  paper.add(l_nameCheck)
  return

def displayStartSec(): # n초후 시작합니다
  displayCheck("startsec")
  for i in range(5, 0, -1):
    __clear()
    secNum = Image(resource_path("images/numbers13pt/num"+str(i)+".png"))
    secNum.moveTo(100,300)
    secNum.setDepth(50)
    paper.add(secNum)
    sleep(1)
    paper.remove(secNum)
  paper.remove(check)
  return


##################################### Other Functions #####################################

def __clear(): # 콘솔 초기화
  os.system(console_clear)
  
def how_to_play(): # 게임 방법
  __clear()
  displayHowToPlay()
  input("메인으로 가려면 아무키나 입력하세요: ")

def view_scores(): # 점수 보기
  __clear()
  paper.clear()
  bg = Image(resource_path("images/image/background.png"))
  bg.moveTo(400, 300)
  paper.add(bg)
  Prize = Layer()
  grade = Text("     Rank             Name                Tries", 25)
  grade.moveTo(400, 100)
  firstEmpty = Text("-----------------------------------------------------", 25)
  firstEmpty.moveTo(400, 130)
  Prize.add(grade)
  Prize.add(firstEmpty)
  paper.add(Prize)
  ThirdEmpty = Text("-----------------------------------------------------", 25)
  ThirdEmpty.moveTo(400, 550)
  paper.add(ThirdEmpty)

  tempDict = dict()
  
  with open(resource_path("best_user_score.txt"), "r", encoding='utf8') as f:
    while True:
      read = list(f.readline().split())
      if not read:
        break 
      user_name, tries = read[0], int(read[1])
      if user_name not in tempDict: 
        tempDict[user_name] = tries 
      else: 
        if tempDict[user_name] > tries:
          tempDict[user_name] = tries

  sorted_list = sorted(tempDict.items(), key = lambda x : x[1])
  ranking = 1
  ran = len(sorted_list) if len(sorted_list) <= 10 else 10
  for i in range(ran):
    if sorted_list[i - 1][1] < sorted_list[i][1]:
      ranking += 1
    data = "%2sth\t%10s\t\t%2d" % (ranking, sorted_list[i][0], sorted_list[i][1])
    data_text = Text(data, 25)
    data_text.moveTo(400, 160+40*i)
    paper.add(data_text)
  
  input("메인으로 가려면 아무키나 입력하세요")

def __getRandomNumber(count): # 랜덤한 count자리수 숫자 생성기
  randomList = rd.sample([i for i in range(0, 10)], count)
  returnStr = "".join([str(i) for i in randomList])
  return returnStr

def execute(): # 프로그램 시작
  __clear()
  displayInit()
  choose_option = ""
  displayMainScreen()
  while True:
    try:
      choose_option = input("옵션을 선택해주세요 : ")
    except:
      __clear()
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
      __clear()
      paper.close()
      return
      
def game_start(): # 게임 시작 -> 인게임 -> Retry
  global balls
  global strikes
  global tries
  global givenNumber
  global predictedNumber
  global userName

  balls = strikes = tries = 0
  givenNumber = predictedNumber = userName = ans = ""
  
  displayingame()
  
  while True:
    displayFix("name_input")

    while True:
      __clear()
      userName = input("플레이어의 이름을 입력하세요(6자리 최대): ")
      if len(userName) > 6 or " " in userName or len(userName) <= 0:
        continue
      else:
        break
    
    paper.remove(fix)
    displayNameCheck()
    __clear()
    ans = input("'" + userName + "' 이(가) 맞습니까? [Y / N]: ")
  
    if ans[0] == "y" or ans[0] == "Y":
      paper.remove(l_nameCheck)
      paper.remove(check)
      break

    paper.remove(l_nameCheck)
    paper.remove(check)
    continue

  __clear()
  ans = ""
  while True:
    __clear()
    displayFix("choosenum")
    ans = input("사용자가 숫자를 선택할까요? [Y / N]: ")
    if ans not in ["y", "Y", "n", "N"]:
      paper.remove(fix)
      continue
    else:
      paper.remove(fix)
      break

  ugn = True if (ans == "y" or ans == "Y") else False
  tries = playGame(ugn)
  
  score = tries
  with open(resource_path("best_user_score.txt"), "a+", encoding="utf-8") as f:
    f.write("%s %d\n" % (userName, score))
  
  displayRetry()
  while True:
    __clear()
    ans = input("다시 플레이 하시겠습니까? [Y / N]: ")
    if ans == "y" or ans == "Y":
      paper.clear()
      return 1
    elif ans == "n" or ans == "N":
      paper.clear()
      return -1
    else:
      continue

def playGame(userGivesNumber=False): # 인게임
  global strikes
  global balls
  global tries
  global givenNumber
  global predictedNumber
  
  ask = " "
  if userGivesNumber:
    displayFix("digit")
    while True:
      try:
        __clear()          
        ask = input("자릿수를 입력해주세요 (3 또는 4) : ")
      except:
        continue

      if ask == '3' or ask == '4':
        break
  
    givenNumber = __getRandomNumber(int(ask))
    paper.remove(fix)

  else:
    __clear()
    givenNumber = __getRandomNumber(rd.randint(3, 4))

  displayStartSec()
  __clear()
  displayStartGame()

  while True:
    __clear()
    balls = strikes = 0
    while True:
      __clear()
      displayFix("guess")
      t = "< " + str(len(givenNumber)) + "자리수 >"
      len_givenNumber = Text(t, 30)
      len_givenNumber.moveTo(400, 400)
      paper.add(len_givenNumber)
      predictedNumber = input("숫자를 추측하세요: ")
      paper.remove(fix)
      paper.remove(len_givenNumber)

      if not predictedNumber.isdigit():
        continue

      if len(predictedNumber) != len(givenNumber):
        continue

      isDuplicate = False
      for i in range(len(predictedNumber)):
        if not isDuplicate:
          for j in range(len(predictedNumber)):
            if i != j and predictedNumber[i] == predictedNumber[j]:
              displayFix("dupl_input")
              sleep(1)
              paper.remove(fix)
              isDuplicate = not isDuplicate
              break

      if isDuplicate == False:
        tries += 1
        break

    for i in range(len(givenNumber)):
      for j in range(len(predictedNumber)):
        if givenNumber[i] == predictedNumber[j]:
          if i == j:
            strikes += 1
          else:
            balls += 1

    if strikes == 0 and balls == 0:
      displayOutSituation()
    elif strikes == len(givenNumber):
      displayGameOverByWinning()
      return tries
    else:
      __clear()
      displayEvaluationResult()
      continue

execute()