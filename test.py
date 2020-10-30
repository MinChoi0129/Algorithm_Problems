#-*-coding:utf-8-*-
from cs1graphics import *
from time import sleep


"""캔버스"""
paper = Canvas()
paper.setWidth(1000)
paper.setHeight(600)
paper.setBackgroundColor("skyblue")
paper.setTitle("Hot Summer with Mosquito")

"""배경"""
##########################(잔디)#############################
grass = Rectangle(1000, 200, Point(500, 500))
grass.setFillColor("green")

##########################(태양)#############################
sun = Circle(50, Point(450, 100))
sun.setFillColor("yellow")

##########################(나무)#############################
tree_leaf = Polygon(Point(800, 200), Point(750, 350), Point(850, 350))
tree_leaf.setFillColor("green")

tree_wood = Rectangle(15, 80, Point(800, 365))
tree_wood.setFillColor("brown")

tree_stick1 = Path(Point(800, 350), Point(770, 300))
tree_stick1.setBorderColor("brown")
tree_stick1.setBorderWidth(4)

tree_stick2 = Path(Point(800, 350), Point(785, 300))
tree_stick2.setBorderColor("brown")
tree_stick2.setBorderWidth(4)

tree_stick3 = Path(Point(800, 350), Point(800, 300))
tree_stick3.setBorderColor("brown")
tree_stick3.setBorderWidth(4)

tree_stick4 = Path(Point(800, 350), Point(815, 300))
tree_stick4.setBorderColor("brown")
tree_stick4.setBorderWidth(4)

tree_stick5 = Path(Point(800, 350), Point(830, 300))
tree_stick5.setBorderColor("brown")
tree_stick5.setBorderWidth(4)



"""모기"""
mos_body = Ellipse(10, 40, Point(50, 500))
mos_body.setFillColor("darkred")

mos_luwing = Ellipse(30, 10, Point(30, 495))
mos_luwing.setFillColor("darkgray")

mos_ruwing = Ellipse(30, 10, Point(70, 495))
mos_ruwing.setFillColor("darkgray")

mos_ldwing = Ellipse(30, 10, Point(30, 510))
mos_ldwing.setFillColor("darkgray")

mos_rdwing = Ellipse(30, 10, Point(70, 510))
mos_rdwing.setFillColor("darkgray")

mos_leye = Circle(10, Point(40, 480))
mos_leye.setFillColor("white")

mos_reye = Circle(10, Point(60, 480))
mos_reye.setFillColor("white")

mos_l_darkeye = Circle(5, Point(40, 480))
mos_l_darkeye.setFillColor("black")

mos_r_darkeye = Circle(5, Point(60, 480))
mos_r_darkeye.setFillColor("black")

mos_stink = Polygon(Point(45, 480), Point(55, 480), Point(50, 440))
mos_stink.setFillColor("red")



"""캐릭터"""
##########################(얼굴)#############################
face_blue = Circle(160, Point(200, 200))
face_blue.setFillColor("blue")
face_blue.setBorderWidth(3)

face_white = Circle(136, Point(200, 224))
face_white.setFillColor("white")
face_white.setBorderWidth(3)

##########################(눈)#############################
eye_white_left = Circle(24, Point(176, 80))
eye_white_left.setFillColor("white")
eye_white_left.setBorderWidth(3)

eye_white_right = Circle(24, Point(224, 80))
eye_white_right.setFillColor("white")
eye_white_right.setBorderWidth(3)

eye_black_left = Circle(10.4, Point(184, 80))
eye_black_left.setFillColor("black")
eye_black_left.setBorderWidth(3)

eye_black_right = Circle(10.4, Point(216, 80))
eye_black_right.setFillColor("black")
eye_black_right.setBorderWidth(3)

small_eye_white_left = Circle(4, Point(184, 80))
small_eye_white_left.setFillColor("white")
small_eye_white_left.setBorderWidth(3)

small_eye_white_right = Circle(4, Point(216, 80))
small_eye_white_right.setFillColor("white")
small_eye_white_right.setBorderWidth(3)

##########################(코)#############################
nose = Circle(12, Point(200, 108))
nose.setFillColor("red")
nose.setBorderWidth(3)

nose_white = Circle(4, Point(196, 104))#
nose_white.setFillColor("white")
nose_white.setBorderWidth(3)

nose_down = Path(Point(200, 120), Point(200, 220))
nose_down.setBorderWidth(3)

##########################(수염)#############################
hair_left_top = Path(Point(120, 140), Point(184, 148))
hair_left_mid = Path(Point(120, 156), Point(184, 156))
hair_left_bot = Path(Point(120, 172), Point(184, 164))

hair_right_top = Path(Point(216, 148), Point(280, 140))
hair_right_mid = Path(Point(216, 156), Point(280, 156))
hair_right_bot = Path(Point(216, 164), Point(280, 172))

hair_left_top.setBorderWidth(3)
hair_left_mid.setBorderWidth(3)
hair_left_bot.setBorderWidth(3)

hair_right_top.setBorderWidth(3)
hair_right_mid.setBorderWidth(3)
hair_right_bot.setBorderWidth(3)

##########################(목도리)#############################
neck = ClosedSpline(Point(120, 350), Point(200, 340), Point(280, 350), Point(200, 370))
neck.setFillColor("red")
neck.setBorderWidth(3)

##########################(방울)#############################
bell_bg = Circle(15, Point(200, 365))
bell_bg.setFillColor("yellow")
bell_bg.setBorderWidth(3)

bell_line = Rectangle(28, 5, Point(200, 360))
bell_line.setBorderWidth(3)

bell_small_gray = Circle(7, Point(200, 370))
bell_small_gray.setBorderWidth(2)
bell_small_gray.setFillColor("dark gray")

##########################(입)#############################
mouth_curve = ClosedSpline(Point(100, 180), Point(200, 180), Point(300, 180), Point(280, 230), Point(200, 300), Point(120, 230))
mouth_curve.setBorderWidth(3)
mouth_curve.setFillColor("red")

##########################(몸)#############################
body = ClosedSpline(Point(200, 360), Point(280, 360), Point(290, 450), Point(280, 490), Point(200, 500), Point(120, 490), Point(110, 450), Point(120, 360))
body.setBorderWidth(3)
body.setFillColor("blue")

body_circle = Circle(50, Point(200, 415))
body_circle.setBorderWidth(3)
body_circle.setFillColor("white")

pocket = ClosedSpline(Point(175, 400), Point(200, 400), Point(225, 400), Point(225, 425), Point(200, 445), Point(175, 425))
pocket.setBorderWidth(3)
pocket.setFillColor("white")

##########################(손, 발, 팔, 다리)#############################
foot_left = Ellipse(80, 50, Point(160, 490))
foot_left.setBorderWidth(3)
foot_left.setFillColor("white")

foot_right = Ellipse(80, 50, Point(240, 490))
foot_right.setBorderWidth(3)
foot_right.setFillColor("white")

arm_left = Ellipse(140, 40, Point(100, 400))
arm_left.setBorderWidth(3)
arm_left.setFillColor("blue")
arm_left.rotate(-45)

arm_right = Ellipse(140, 40, Point(300, 400))
arm_right.setBorderWidth(3)
arm_right.setFillColor("blue")
arm_right.rotate(45)

hand_left = Circle(25, Point(50, 450))
hand_left.setFillColor("white")
hand_left.setBorderWidth(3)

hand_right = Circle(25, Point(350, 450))
hand_right.setFillColor("white")
hand_right.setBorderWidth(3)



"""레이어 만들고 쌓기"""
background = Layer()
character = Layer()
mosquito = Layer()

def set_background_layer():
    background.add(sun)
    background.add(grass)
    background.add(tree_wood)
    background.add(tree_stick1)
    background.add(tree_stick2)
    background.add(tree_stick3)
    background.add(tree_stick4)
    background.add(tree_stick5)
    background.add(tree_leaf)

def set_character_layer():
    character.add(arm_left)
    character.add(arm_right)
    character.add(hand_left)
    character.add(hand_right)
    character.add(body)
    character.add(foot_left)
    character.add(foot_right)
    character.add(body_circle)
    character.add(pocket)
    character.add(face_blue)
    character.add(face_white)
    character.add(eye_white_left)
    character.add(eye_white_right)
    character.add(nose)
    character.add(eye_black_right)
    character.add(eye_black_left)
    character.add(small_eye_white_right)
    character.add(small_eye_white_left)
    character.add(nose_white)
    character.add(nose_down)
    character.add(hair_left_mid)
    character.add(hair_right_mid)
    character.add(hair_left_top)
    character.add(hair_right_top)
    character.add(hair_left_bot)
    character.add(hair_right_bot)
    character.add(neck)
    character.add(bell_bg)
    character.add(bell_line)
    character.add(bell_small_gray)
    character.add(mouth_curve)

def set_mosquito_layer():
    mosquito.add(mos_body)
    mosquito.add(mos_stink)
    mosquito.add(mos_luwing)
    mosquito.add(mos_ruwing)
    mosquito.add(mos_ldwing)
    mosquito.add(mos_rdwing)
    mosquito.add(mos_leye)
    mosquito.add(mos_reye)
    mosquito.add(mos_l_darkeye)
    mosquito.add(mos_r_darkeye)

set_background_layer()
set_character_layer()
set_mosquito_layer()



"""설명 시작"""
##############################(검정 배경)##############################
start = Rectangle(1000, 600, Point(500, 300))
start.setFillColor("black")

##############################(자막)##############################
description1 = Text("2050년 지구온난화가 심각해졌다...")
description2 = Text("어느 한 여름, 도라에몽은 쉬고 있었고 태양은 미친듯이 뜨거워졌다...")
description3 = Text("지구온난화에도 불구하고 지독한 녀석인 모기는 살아있었는데...")
description4 = Text("모기가 더운 날씨에 화난 도라에몽을 괴롭히기 시작하는데...")

description1.setFontColor("white")
description2.setFontColor("white")
description3.setFontColor("white")
description4.setFontColor("white")

description1.scale(2)
description1.moveTo(500, 100)
description2.scale(2)
description2.moveTo(500, 200)
description3.scale(2)
description3.moveTo(500, 300)
description4.scale(2)
description4.moveTo(500, 400)

##############################(순차적 등장)##############################
paper.add(start)

paper.add(description1)
sleep(2)
paper.add(description2)
sleep(2)
paper.add(description3)
sleep(2)
paper.add(description4)
sleep(4)

##############################(순차적 삭제)##############################
paper.remove(description1)
paper.remove(description2)
paper.remove(description3)
paper.remove(description4)
paper.remove(start)

##############################(본 애니메이션 시작)##############################
paper.add(background)
paper.add(character)



"""애니메이션"""

# 미친 태양
for i in range(6):
    sun.scale(1.2)
    sun.setFillColor((255, 255 - i * 40, 0))
    sleep(0.3)

# 아주 더운 날씨에 도라에몽이 땀을 흘림
sweat1 = ClosedSpline(Point(300, 130), Point(290, 140), Point(300, 160), Point(310, 140))
sweat2 = ClosedSpline(Point(320, 120), Point(310, 130), Point(320, 150), Point(330, 130))
sweat1.setFillColor("skyblue")
sweat2.setFillColor("skyblue")

paper.add(sweat1)
sleep(0.7)
paper.add(sweat2)

for i in range(15):
  sweat1.move(0, 10)
  sweat2.move(0, 10)
  sleep(0.15)
sweat1.move(0, -150)
sweat2.move(0, -150)

# 모기 왔다갔다 + 날개짓 + 계속 땀흘리는 도라에몽
paper.add(mosquito)

for i in range(10):
    sweat1.move(0, 15)
    sweat2.move(0, 15)
    mosquito.move(30, 0)
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    sleep(0.1)
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    sleep(0.1)
sweat1.move(0, -150)
sweat2.move(0, -150)

for i in range(10):
    sweat1.move(0, 15)
    sweat2.move(0, 15)
    mosquito.move(-30, -15)
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    sleep(0.1)
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    sleep(0.1)
sweat1.move(0, -150)
sweat2.move(0, -150)

for i in range(10):
    sweat1.move(0, 15)
    sweat2.move(0, 15)
    mosquito.move(30, -15)
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    sleep(0.1)
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    sleep(0.1)
sweat1.move(0, -150)
sweat2.move(0, -150)

for i in range(10):
    sweat1.move(0, 15)
    sweat2.move(0, 15)
    mosquito.move(30, 0)
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    sleep(0.1)
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    sleep(0.1)

# 모기에 짜증난 도라에몽
mention = Text("모기 너무 싫어!!!")
mention.scale(1.7)
mention.moveTo(200, 300)
paper.add(mention)

# 도라에몽이 화나서 각성하며 얼굴이 붉어짐 + 모기는 계속 날고 있음
for i in range(30):
    face_white.setFillColor((255, 255 - i * 8, 255 - i * 8))
    eye_white_left.setFillColor((255, 255 - i * 8, 255 - i * 8))
    eye_white_right.setFillColor((255, 255 - i * 8, 255 - i * 8))
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    sleep(0.1)
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    sleep(0.1)

# 토르 망치 + 모기는 계속 날고 있음
hammer = Layer()

iron = Rectangle(100, 60, Point(0,0))
iron.setFillColor("darkgray")
handle = Rectangle(10, 50, Point(0,55))
handle.setFillColor("brown")

hammer.add(iron)
hammer.add(handle)

hammer.rotate(45)
hammer.moveTo(400, 400)
hammer.scale(0.1)

paper.add(hammer)

for i in range(10):
    hammer.scale(1.3)
    
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    sleep(0.1)
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    sleep(0.1)

# 각성한 도라에몽이 망치에 전기가 흐르게 하며 세상을 어둡게 만듦 + 모기는 계속 날고 있음

thunder_hammer = Path(Point(650, 180), Point(680, 135), Point(630, 90), Point(650, 1))
thunder_hammer.moveTo(400, 400)
thunder_hammer.setBorderColor("yellow")
thunder_hammer.setBorderWidth(4)

thunder_hammer2 = thunder_hammer.clone()
thunder_hammer2.rotate(30)
thunder_hammer2.moveTo(390, 410)

thunder_hammer3 = thunder_hammer.clone()
thunder_hammer3.rotate(40)
thunder_hammer3.moveTo(390, 390)

thunder_hammer4 = thunder_hammer.clone()
thunder_hammer4.rotate(-40)
thunder_hammer4.moveTo(410, 410)

thunder_hammer5 = thunder_hammer.clone()
thunder_hammer5.rotate(-30)
thunder_hammer5.moveTo(410, 390)

for i in range(10):
    paper.setBackgroundColor((135 - i * 13, 206 - i * 20, 235 - i * 23))
    grass.setFillColor((255 - i * 25, 255 - i * 25, 0))
    sun.setFillColor((255 - i * 25, 55 - 5, 0))
    
    paper.add(thunder_hammer)
    sleep(0.08)
    
    """날개짓"""
    mos_luwing.rotate(45)
    mos_ldwing.rotate(45)
    mos_ruwing.rotate(-45)
    mos_rdwing.rotate(-45)
    
    paper.add(thunder_hammer3)
    sleep(0.08)
    paper.add(thunder_hammer5)
    sleep(0.08)
    paper.remove(thunder_hammer)
    sleep(0.08)
    paper.add(thunder_hammer2)
    sleep(0.08)
    
    """날개짓"""
    mos_luwing.rotate(-45)
    mos_ldwing.rotate(-45)
    mos_ruwing.rotate(45)
    mos_rdwing.rotate(45)
    
    paper.remove(thunder_hammer5)
    sleep(0.08)
    paper.add(thunder_hammer4)
    sleep(0.08)
    
    paper.remove(thunder_hammer3)
    paper.remove(thunder_hammer2)
    paper.remove(thunder_hammer4)
    

# 하늘도 태양도 새까맣게 타버림
paper.setBackgroundColor("black")
sun.setFillColor("black")

# 번개를 모기와 나무에 강타함
thunder = Path(Point(650, 180), Point(680, 135), Point(630, 90), Point(650, 1))
thunder.setBorderColor("yellow")
thunder.setBorderWidth(4)

thunder_tree = thunder.clone()
thunder_tree.move(150, 0)

paper.add(thunder)
paper.add(thunder_tree)

sleep(1)

# 번개가 사라지고 모기는 땅으로 떨어져 사망함
paper.remove(thunder)
paper.remove(thunder_tree)

mosquito.rotate(80)
mosquito.move(550, 600)

# 죽은 모기의 눈을 표현
dead_left_eye = Circle(10.5, Point(685, 422))
dead_left_eye.setFillColor("white")
dead_right_eye = Circle(10.5, Point(687, 443))
dead_right_eye.setFillColor("white")

dead_left_x = Circle(2, Point(685, 422))
dead_left_x.setFillColor("red")
dead_right_x = Circle(2, Point(687, 443))
dead_right_x.setFillColor("red")

paper.add(dead_left_eye)
paper.add(dead_right_eye)
paper.add(dead_left_x)
paper.add(dead_right_x)

# 나무가 번개를 맞고 가지만 남음
for i in range(3):
    tree_leaf.setFillColor("yellow")
    sleep(0.2)
    tree_leaf.setFillColor("black")
    sleep(0.2)

tree_leaf.setFillColor("black")
tree_leaf.setDepth(99)