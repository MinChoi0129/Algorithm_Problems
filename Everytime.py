a, b, c, d, e, f = [], [], [], [], [], [] # 왼쪽부터 순서대로 <역량교양>, <통합교양>, <개척교양>, <기초과정>, <교직>, <일반선택>

class Lecture:
  def __init__(self, main_theme, sub_theme, name, number, class_num, credit, theory, practice, prof, day, classroom_num, etc):
    self.main_theme = main_theme # 큰 영역구분(ex. 역량교양, 통합교양, 기초교양, 전공 등)
    self.sub_theme = sub_theme # 작은 영역구분(ex. 필수역량, 문학과문화, 생명과환경, 진로취업, 창업산학협력, 자연계열, 전공필수, 전공선택 등)
    self.name = name # 교과목명(ex. 글쓰기기초)
    self.number = number # 학수번호(ex. ZTA10003)
    self.class_num = class_num # 수강반 번호(ex. 24반)
    self.credit = credit # 학점(ex. 3학점)
    self.theory = theory # 이론
    self.practice = practice # 실습
    self.prof = prof # 교수명
    self.day = day # 강의시간(ex. 화6, 7)
    self.classroom_num = classroom_num # 강의실(ex. 024-0141)
    self.etc = etc # 비고(수강가능학과, 블렌디드, 인원제한 등)

  def get_credit_info(self):
    return self.credit + "학점, " + self.theory + "이론, " + self.practice + "실습"
  
  def get_day_info(self):
    if len(self.day) > 16:
      return self.day

    elif len(self.day) == 0:
      return "None"
    else:
      return self.day[0] + " / " + self.day[1:] + " 교시"

def time_table(raw):
  global a, b, c, d, e, f
  data = open(raw, "r", encoding = "UTF8")
  data.readline()
  while True:
    line = data.readline()
    if not line:
      break

    while True:
      line = data.readline()
      if line == "***\n":
        data.readline()
        break
      tmp = line.split("\t")
      try:
        day = tmp[8][1 : tmp[8].find("[") - 1]
        classroom_num = tmp[8][tmp[8].find("[") : 0]
      except:
        day = "None"
        classroom_num = "None"
      a.append(Lecture("역량교양", tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], day, classroom_num, tmp[9]))
    
    while True:
      line = data.readline()
      if line == "***\n":
        data.readline()
        break
      tmp = line.split("\t")
      try:
        day = tmp[8][1 : tmp[8].find("[") - 1]
        classroom_num = tmp[8][tmp[8].find("[") : 0]
      except:
        day = "None"
        classroom_num = "None"
      b.append(Lecture("통합교양", tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], day, classroom_num, tmp[9]))

    while True:
      line = data.readline()
      if line == "***\n":
        data.readline()
        break
      tmp = line.split("\t")
      try:
        day = tmp[8][1 : tmp[8].find("[") - 1]
        classroom_num = tmp[8][tmp[8].find("[") : 0]
      except:
        day = "None"
        classroom_num = "None"
      c.append(Lecture("개척교양", tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], day, classroom_num, tmp[9]))

    while True:
      line = data.readline()
      if line == "***\n":
        data.readline()
        break
      tmp = line.split("\t")
      try:
        day = tmp[8][1 : tmp[8].find("[") - 1]
        classroom_num = tmp[8][tmp[8].find("[") : 0]
      except:
        day = "None"
        classroom_num = "None"
      d.append(Lecture("기초과정", tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], day, classroom_num, tmp[9]))

    while True:
      line = data.readline()
      if line == "***\n":
        data.readline()
        break
      tmp = line.split("\t")
      try:
        day = tmp[8][1 : tmp[8].find("[") - 1]
        classroom_num = tmp[8][tmp[8].find("[") : 0]
      except:
        day = "None"
        classroom_num = "None"
      e.append(Lecture("교직",tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], day, classroom_num, tmp[9]))

    while True:
      line = data.readline()
      if not line:
        break
      tmp = line.split("\t")
      try:
        day = tmp[8][1 : tmp[8].find("[") - 1]
        classroom_num = tmp[8][tmp[8].find("[") : 0]
      except:
        day = "None"
        classroom_num = "None"
      f.append(Lecture("일반선택", tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], day, classroom_num, tmp[9]))

  data.close()

time_table("timetable.txt")

for i in f:
  print(i.name, ";", i.get_day_info(), ";", i.get_credit_info())
  