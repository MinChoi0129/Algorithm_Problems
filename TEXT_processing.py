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
		self.day = dataList[8]  # 강의시간(ex. 화6, 7)
		self.classroom_num = dataList[9]  # 강의실(ex. 024-0141)
		self.etc = dataList[10]  # 비고(수강가능학과, 블렌디드, 인원제한 등)

	def get_credit_info(self):
		return self.credit + "학점, " + self.theory + "이론, " + self.practice + "실습"

	def get_day_info(self):
		if len(self.day) == 0: return None
		else: return self.day

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
		if len(word) == 1: main_theme = word[0][1:-1]

		else:  # 아니라면 과목 정보를 담은 줄임
			li = []
			for content in word:
				li.append(content)
			li.append(main_theme)

			obj_list.append(Lecture(li))
	return obj_list

def getItemsBySubTheme(string, obj_list):
	rtn_list = []
	for obj in obj_list:
		if obj.sub_theme == string: rtn_list.append(obj)

	return rtn_list

def test(sub_theme_list):
	for i in sub_theme_list:
		# print("%-5s : %s" % ("대분류    ", i.main_theme))
		# print("%-5s : %s" % ("소분류    ", i.sub_theme))
		print("%-5s : %s" % ("강의명    ", i.name))
		# print("%-5s : %s" % ("학수번호  ", i.number))
		# print("%-5s : %s" % ("수강반번호", i.class_num))
		# print("%-5s : %s" % ("학점      ", i.credit))
		# print("%-5s : %s" % ("이론      ", i.theory))
		# print("%-5s : %s" % ("실습      ", i.practice))
		# print("%-5s : %s" % ("교수명    ", i.prof))  
		print("%-5s : %s" % ("요일및교시", i.day))
		# print("%-5s : %s" % ("강의실    ", i.classroom_num))
		# print("%-5s : %s" % ("기타      ", i.etc))
		# print()