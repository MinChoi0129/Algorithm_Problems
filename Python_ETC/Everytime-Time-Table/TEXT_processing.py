######################################
# timetable.txt 파일을 프로세싱합니다. #
######################################

class Lecture:
    def __init__(self, dataList):
        self.main_theme = dataList[11]  # 큰 영역구분(ex. 역량교양, 통합교양, 기초교양, 전공 등)
        # 작은 영역구분(ex. 필수역량, 문학과문화, 생명과환경, 진로취업, 창업산학협력, 자연계열, 전공필수, 전공선택 등)
        self.sub_theme = dataList[0]
        self.name = dataList[1]  # 교과목명(ex. 글쓰기기초)
        self.number = dataList[2]  # 학수번호(ex. ZTA10003)
        self.class_num = dataList[3]  # 수강반 번호(ex. 24반)
        self.credit = dataList[4]  # 학점(ex. 3학점)
        self.theory = dataList[5]  # 이론
        self.practice = dataList[6]  # 실습
        self.prof = dataList[7]  # 교수명
        self.day = dataList[8]  # 강의시간(ex. 월2, 3, 수1 == [[0, 2, 3], [2, 1]])
        self.day_str = dataList[8]
        self.classroom_num = dataList[9]  # 강의실(ex. 024-0141)
        self.etc = dataList[10]  # 비고(수강가능학과, 블렌디드, 인원제한 등)

    def get_credit_info(self):
        return self.credit + "학점, " + self.theory + "이론, " + self.practice + "실습"

    def get_day_info(self):
        return " / " + self.day_str

    def get_brief_info(self):
        return self.name + " / " + self.prof

def time_table(file_name):
    lines = []  # stores contents of file
    main_theme = ""
    obj_list = []

    with open(file_name, 'r', encoding="UTF8") as f:
        lines = f.readlines()[1:]  # 헤더는 건너뛰고 불러오기

    for line in lines:
        word = line.replace('\n', "").split('\t')  # 한 line을 tab 단위로 split한 리스트
        if len(word) == 1: main_theme = word[0][1:-1] # 단어 수가 1 => 대분류임

        else:  # 아니라면 과목 정보를 담은 줄임
            infoList = []
      #따옴표는 제외하고 저장
            for content in word: infoList.append(content[1:-1] if content[0] == '"' else content)
            infoList.append(main_theme) #마지막 요소는 아까 불러왔던 대분류임

            obj_list.append(Lecture(infoList))
    return obj_list

def getItemsBySubTheme(string, obj_list):
    rtn_list = []
    for obj in obj_list:
        if obj.sub_theme == string: rtn_list.append(obj)

    return rtn_list

def test(obj_list):
    for obj in obj_list:
        # print("%-5s : %s" % ("대분류    ", obj.main_theme))
        # print("%-5s : %s" % ("소분류    ", obj.sub_theme))
        print("%-5s : %s" % ("강의명    ", obj.name))
        # print("%-5s : %s" % ("학수번호  ", obj.number))
        # print("%-5s : %s" % ("수강반번호", obj.class_num))
        # print("%-5s : %s" % ("학점      ", obj.credit))
        # print("%-5s : %s" % ("이론      ", obj.theory))
        # print("%-5s : %s" % ("실습      ", obj.practice))
        print("%-5s : %s" % ("교수명    ", obj.prof))  
        print("%-5s : %s" % ("요일및교시", obj.day_str))
        # print("%-5s : %s" % ("강의실    ", obj.classroom_num))
        # print("%-5s : %s" % ("기타      ", obj.etc))
        print()

def setClassInfo(lecture):
    #Leature.day의 문자열을 파싱하여 리스트 형태로 변환하여 다시 저장하는 메서드
    #생성자나 time_table 메서드와 통합 예정

    dayList = [[] for k in range(6)] #월, 화, ..., 금, 토
    #대응 관계를 담은 딕셔너리
    currentDayDic = {'월': 0, '화': 1, '수': 2, '목': 3, '금': 4, '토': 5}
    #현재 요일의 숫자 인덱스 변수
    currentDayIdx = 0

    if lecture.day == 'null':
        lecture.day = [] #널 값은 무시함
        return

    classTime = lecture.day.split(' ') #parsing을 위해 공백 문자 기준 split

    for word in classTime:
        if word[0].isdigit():  # 교시 정보인 경우
            # rtnList의 해당 요일 번째 리스트에 ',' 제거 후 append
            dayList[currentDayIdx].append(int(word[:-1] if word[-1] == ',' else word))

        elif word[0] in currentDayDic.keys():  # 요일 정보가 함께 들어 있는 경우
            currentDayIdx = currentDayDic[word[0]]  # 요일-번호 대응으로부터 인덱스를 구함
            dayList[currentDayIdx].append(currentDayIdx) # 구한 인덱스를 새 요일 정보 리스트에 append
            dayList[currentDayIdx].append(int(word[1:-1] if word[-1] == ',' else word[1:])) # 교시 정보도 append

    while True: #비어있는 리스트는 제거
        try: dayList.remove([])
        except: break

    lecture.day = dayList
    # print(lecture.day)
    return