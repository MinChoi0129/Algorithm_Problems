from cs1robots import *

############################# define function #############################

def turn_right(rb):
  for _ in range(3):
    rb.turn_left()

def check(rb, orient):
  if orient == "right":
    if (not rb.front_is_clear()) and (not rb.right_is_clear()): # 앞과 오른쪽 모두 막힘
      return 0
    else: # 한쪽이라도 뚫림
      return 1

  elif orient == "left":
    if (not rb.front_is_clear()) and (not rb.left_is_clear()): # 앞과 왼쪽 모두 막힘
      return 0
    else: # 한쪽이라도 뚫림
      return 1

  else: # 잘못된 입력
    return -1

############################# create world and robot #############################

create_world(4, 5)
hubo = Robot(orientation = 'N')
hubo.set_trace("blue")

############################# solution #############################

"""
while문:
  앞이나 오른쪽 중 한 군데라도 뚫려있는 동안
  앞으로 직진한다
  목적지 도착인가? (앞과 오른쪽 모두 막혀야 함)
  목적지가 아니라면
  180도 돌아서 쭉 직진
  목적지 도착인가? (앞과 왼쪽 모두 막혀야 함)
  목적지가 아니라면 180도 회전(one time zigzag)

"""

while check(hubo, "right") != 0:

  while hubo.front_is_clear():
    hubo.move()

  if check(hubo, "right") == 0: 
    break

  else:
    turn_right(hubo)
    hubo.move()
    turn_right(hubo)
    while hubo.front_is_clear():
      hubo.move()
    
    if check(hubo, "left") == 0:
      break
    else:
      hubo.turn_left()
      hubo.move()
      hubo.turn_left()