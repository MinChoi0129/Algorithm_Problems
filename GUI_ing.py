from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from TEXT_processing import time_table, test, getItemsBySubTheme
from PIL import Image, ImageGrab
import datetime

################################################################
##########       global variables 정의 및 초기화       ##########
################################################################

window = Tk()
window.title("TimeTable")
window.attributes('-fullscreen',True)


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='과목선택')
tab_control.add(tab2, text='그룹')
tab_control.add(tab3, text='결과보기')
tab_control.pack(expand=1, fill='both')

tab3_frame1 = Frame()
tab3_frame3 = Frame()


역교 = ["None", "필수역량교양", "선택역량교양"]
통교 = ["None", "문학과문화", "역사와철학", "인간과사회", "과학과기술", "예술과체육", "융복합영역"]
개교 = ["None", "진로·취업", "창업·산학협력", "기타"]
기초 = ["None", "외국어계열", "인문사회계열", "자연계열"]
교직 = ["None", "교직"]
일반 = ["None", "일반선택"]
전공 = ["None", "전공필수", "전공선택"]
lecture_objs = time_table("timetable.txt")
searched_objs = []
subject_list = Listbox()
selected_groups = [[], [], [], [], [], [], [], [], [], []]

##############################################################
###################        함수 정의        ###################
##############################################################

def In_Lecture(): #In버튼 누르면 group에 추가
	global selected_groups, subject_list, searched_objs, variety1
	chosen_group = int(variety1.get()) # 선택한 그룹번호
	idx = subject_list.curselection()[0] # 리스트박스에서 선택된 과목의 인덱스
	dupl = False
	for k in range(10):
		if searched_objs[idx] in selected_groups[k]:
			messagebox.showinfo("중복 담기", "이미 담은 과목입니다.")
			dupl = True
			break
	if not dupl:
		selected_groups[chosen_group].append(searched_objs[idx])
		messagebox.showinfo("성공", "과목을 담았습니다.")
		if chosen_group == 0:
			first_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 1:
			second_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 2:
			third_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 3:
			fourth_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 4:
			fifth_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 5:
			sixth_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 6:
			seventh_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 7:
			eighth_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 8:
			nineth_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())
		elif chosen_group == 9:
			tenth_list.insert(0, selected_groups[chosen_group][-1].get_brief_info())

def exit_window(): # 프로그램 종료
    global window
    window.destroy()


def see_b2(): #선택된 조합 적용
	global tab3_frame1,tab3_frame3
	com_num = combi.current()
	com_num_list.append(com_num)
	tab3_frame3 = Frame(tab3)
	tab3_frame3.grid(row=0, column=0)

	for i in range(0, 7): #시간표 틀(흰)
		Label(tab3_frame3, text=day_name[i], width=10, bg="pink").grid(row=1, column=i)
		for k in range(len(time_list)):
			if i == 0:
				Label(tab3_frame3, text=time_list[k], width=10, height=3, bg="white", anchor="n").grid(row=k + 2,column=i)
			else:
				Label(tab3_frame3, width=10, height=3, bg="white", relief='solid', bd=0.1).grid(row=k + 2, column=i)

	for day in range(len(test_lists[com_num])):#시간표 - 색상/과목/교수 관련 수정 예정
		CTime = test_lists[com_num][day][1:]
		for classtime in range(len(test_lists[com_num][day])-1):
			C = CTime[classtime]
			num_label = Label(tab3_frame3, text="", width=10, height=3, bg="dark grey", relief='solid', bd=1)
			num_label.grid(row = C+1, column = test_lists[com_num][day][0] + 1)

def see_b():
	global tab3_frame1, tab3_frame3
	if len(com_num_list) == 0:
		tab3_frame1.destroy()
	else:
		tab3_frame3.destroy()
	see_b2()

def search_subjects(): # Search버튼 누르면 조건에 맞는 강의들을 보여줌
	global searched_objs
	searched_objs = [] # 부를때마다 초기화
	name = search_by_name_or_prof.get()
	yeok = cb1.get()
	tong = cb2.get()
	gae = cb3.get()
	gicho = cb4.get()
	gyojik = cb5.get()
	ilban = cb6.get()
	cs = cb7.get()
	if name: # 검색어에 무언가라도 적혀있는 경우

		if yeok == "None" and tong == "None" and gae == "None" and \
			gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 검색어만 적은 경우
			for lecture_obj in lecture_objs:
				if name in lecture_obj.name or name in lecture_obj.prof: # 강의명 또는 교수명에서 찾는다.
					searched_objs.append(lecture_obj)

		else: # 검색어와 옵션을 함께 고른 경우
			if yeok != "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 역량교양에서 선택

				for lecture_obj in getItemsBySubTheme(yeok, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong != "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 통합교양에서 선택

				for lecture_obj in getItemsBySubTheme(tong, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae != "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 개척교양에서 선택

				for lecture_obj in getItemsBySubTheme(gae, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho != "None" and gyojik == "None" and ilban == "None" and cs == "None": # 기초과정에서 선택

				for lecture_obj in getItemsBySubTheme(gicho, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik != "None" and ilban == "None" and cs == "None": # 교직에서 선택

				for lecture_obj in getItemsBySubTheme(gyojik, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban != "None" and cs == "None": # 일반선택에서 선택

				for lecture_obj in getItemsBySubTheme(ilban, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs != "None": # CS전공에서 선택

				for lecture_obj in getItemsBySubTheme(cs, lecture_objs):
					if name in lecture_obj.name or name in lecture_obj.prof:
						searched_objs.append(lecture_obj)

			else : # 다중선택
				messagebox.showinfo("옵션 다중 선택", "옵션을 하나만 골라주세요.")

	else: # 검색어 없는 경우
		if yeok == "None" and tong == "None" and gae == "None" and gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":
			messagebox.showinfo("필터없음", "강의명/교수명으로 검색하거나 옵션 한 개를 골라주세요.") # 아무것도 안고른경우

		else: # 옵션을 고르긴 고른 경우
			if yeok != "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 역량교양에서 선택
				searched_objs = getItemsBySubTheme(yeok, lecture_objs)

			elif yeok == "None" and tong != "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 통합교양에서 선택
				searched_objs = getItemsBySubTheme(tong, lecture_objs)

			elif yeok == "None" and tong == "None" and gae != "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 개척교양에서 선택
				searched_objs = getItemsBySubTheme(gae, lecture_objs)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho != "None" and gyojik == "None" and ilban == "None" and cs == "None": # 기초과정에서 선택
				searched_objs = getItemsBySubTheme(gicho, lecture_objs)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik != "None" and ilban == "None" and cs == "None": # 교직에서 선택
				searched_objs = getItemsBySubTheme(gyojik, lecture_objs)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban != "None" and cs == "None": # 일반선택에서 선택
				searched_objs = getItemsBySubTheme(ilban, lecture_objs)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs != "None": # CS전공에서 선택
				searched_objs = getItemsBySubTheme(cs, lecture_objs)

			else : # 다중선택
				messagebox.showinfo("옵션 다중 선택", "옵션을 하나만 골라주세요.")

	##### List box
	global tab1, subject_list
	winf = ttk.Frame(tab1)
	winf.grid(row=1, column=2, rowspan = 15)

	subject_list = Listbox(winf, width=70, height = 20)
	subject_list.pack(side = "left")
	for i in range(len(searched_objs)):
		subject_list.insert(i, searched_objs[i].get_brief_info())
	
	scrollbar = Scrollbar(winf, command = subject_list.yview)
	scrollbar.pack(side = "right", fill = "y")
	subject_list.config(yscrollcommand=scrollbar.set)

def shot():
    img = ImageGrab.grab()
    img.save(re_nowdate + '.png')

def OUT1():
	try:
		first_idx = first_list.curselection()[0]
		first_list.delete(first_idx)
		selected_groups[0].pop(first_idx)
	except:
		pass

def OUT2():
  second_idx = second_list.curselection()
  second_list.delete(second_idx)
	
def OUT3():
  third_idx = third_list.curselection()
  third_list.delete(third_idx)

def OUT4():
  fourth_idx = fourth_list.curselection()
  fourth_list.delete(fourth_idx)

def OUT5():
  fifth_idx = fifth_list.curselection()
  fifth_list.delete(fifth_idx)
	
def OUT6():
  sixth_idx = sixth_list.curselection()
  sixth_list.delete(sixth_idx)

def OUT7():
  seventh_idx = seventh_list.curselection()
  seventh_list.delete(seventh_idx)

def OUT8():
  eighth_idx = eighth_list.curselection()
  eighth_list.delete(eighth_idx)
	
def OUT9():
  nineth_idx = nineth_list.curselection()
  nineth_list.delete(nineth_idx)

def OUT10():
  tenth_idx = tenth_list.curselection()
  tenth_list.delete(tenth_idx)



################################################################
###########       tab마다 기능구현(tab1 ~ tab4)       ###########
################################################################




# tab1 (과목선택)
Label(tab1, text="과목검색",font = ("", 13), width=14, bg="dark grey").grid(row=0,column=0)
Label(tab1, text="그룹선택",font = ("", 13), width=10, bg="grey").grid(row=0,column=1)
Label(tab1,text="강의목록", font = ("", 13), width=56, bg="dark grey").grid(row=0,column=2)

search_by_name_or_prof = Entry(tab1, width = 18, bg = "orange")
search_by_name_or_prof.grid(row = 1, column = 0)

Label(tab1,text="역량교양",width=18,bg="pink").grid(row = 2, column = 0)
cb1 = ttk.Combobox(tab1, width=15, height=10, values=역교, state="readonly")
cb1.grid(row = 3, column = 0)
cb1.set("None")

Label(tab1,text="통합교양",width=18,bg="pink").grid(row = 4, column = 0)
cb2 = ttk.Combobox(tab1, width=15, height=10, values=통교, state="readonly")
cb2.grid(row = 5, column = 0)
cb2.set("None")

Label(tab1,text="개척교양",width=18,bg="pink").grid(row = 6, column = 0)
cb3 = ttk.Combobox(tab1, width=15, height=10, values=개교, state="readonly")
cb3.grid(row = 7, column = 0)
cb3.set("None")

Label(tab1,text="기초과정",width=18,bg="pink").grid(row = 8, column = 0)
cb4 = ttk.Combobox(tab1, width=15, height=10, values=기초, state="readonly")
cb4.grid(row = 9, column = 0)
cb4.set("None")

Label(tab1,text="교직",width=18,bg="pink").grid(row = 10, column = 0)
cb5 = ttk.Combobox(tab1, width=15, height=10, values=교직, state="readonly")
cb5.grid(row = 11, column = 0)
cb5.set("None")

Label(tab1,text="일반선택",width=18,bg="pink").grid(row = 12, column = 0)
cb6 = ttk.Combobox(tab1, width=15, height=10, values=일반, state="readonly")
cb6.grid(row = 13, column = 0)
cb6.set("None")

Label(tab1,text="CS전공",width=18,bg="pink").grid(row = 14, column = 0)
cb7 = ttk.Combobox(tab1, width=15, height=10, values=전공, state="readonly")
cb7.grid(row = 15, column = 0)
cb7.set("None")

Button(tab1, text = "검색", width = 15, bg='white', command = search_subjects).grid(row = 16, column = 0)



groups_frame = ttk.Frame(tab1)
groups_frame.grid(row= 1, column=1, rowspan = 15)
variety1 = IntVar(value = 0)
Radiobutton(groups_frame, text="Group1", value=0, variable = variety1).pack()
Radiobutton(groups_frame, text="Group2", value=1, variable = variety1).pack()
Radiobutton(groups_frame, text="Group3", value=2, variable = variety1).pack()
Radiobutton(groups_frame, text="Group4", value=3, variable = variety1).pack()
Radiobutton(groups_frame, text="Group5", value=4, variable = variety1).pack()
Radiobutton(groups_frame, text="Group6", value=5, variable = variety1).pack()
Radiobutton(groups_frame, text="Group7", value=6, variable = variety1).pack()
Radiobutton(groups_frame, text="Group8", value=7, variable = variety1).pack()
Radiobutton(groups_frame, text="Group9", value=8, variable = variety1).pack()
Radiobutton(groups_frame, text="Group10", value=9, variable = variety1).pack()


Button(tab1, text = "추가", width =8, bg='light grey',command=In_Lecture).grid(row = 16, column = 2)




# tab 2 (그룹)
group_list=["Group1","Group2","Group3","Group4","Group5","Group6","Group7","Group8","Group9","Group10"]



# 1
Label(tab2, text=group_list[0], width=35, bg="pink").grid(row= 0, column=0)
win1 = ttk.Frame(tab2)
win1.grid(row= 1, column=0, rowspan=1)

first_list = Listbox(win1, width=35, height=4)
first_list.pack(side="left")

scrollbar1 = Scrollbar(win1, command=first_list.yview)
scrollbar1.pack(side="right", fill="y")
first_list.config(yscrollcommand=scrollbar1.set)

# 2
Label(tab2, text=group_list[1], width=35, bg="pink").grid(row= 0, column=1)
win2 = ttk.Frame(tab2)
win2.grid(row= 1, column=1, rowspan=1)

second_list = Listbox(win2, width=35, height=4)
second_list.pack(side="left")

scrollbar2 = Scrollbar(win2, command=second_list.yview)
scrollbar2.pack(side="right", fill="y")
second_list.config(yscrollcommand=scrollbar2.set)


# 3
Label(tab2, text=group_list[2], width=35, bg="pink").grid(row= 2, column=0)
win3 = ttk.Frame(tab2)
win3.grid(row= 3, column=0, rowspan=1)

third_list = Listbox(win3, width=35, height=4)
third_list.pack(side="left")

scrollbar3 = Scrollbar(win3, command=third_list.yview)
scrollbar3.pack(side="right", fill="y")
third_list.config(yscrollcommand=scrollbar3.set)

# 4
Label(tab2, text=group_list[3], width=35, bg="pink").grid(row= 2, column=1)
win4 = ttk.Frame(tab2)
win4.grid(row= 3, column=1, rowspan=1)

fourth_list = Listbox(win4, width=35, height=4)
fourth_list.pack(side="left")

scrollbar4 = Scrollbar(win4, command=fourth_list.yview)
scrollbar4.pack(side="right", fill="y")
fourth_list.config(yscrollcommand=scrollbar4.set)

# 5
Label(tab2, text=group_list[4], width=35, bg="pink").grid(row= 4, column=0)
win5 = ttk.Frame(tab2)
win5.grid(row= 5, column=0, rowspan=1)

fifth_list = Listbox(win5, width=35, height=4)
fifth_list.pack(side="left")

scrollbar5 = Scrollbar(win5, command=fifth_list.yview)
scrollbar5.pack(side="right", fill="y")
fifth_list.config(yscrollcommand=scrollbar5.set)

# 6
Label(tab2, text=group_list[5], width=35, bg="pink").grid(row= 4, column=1)
win6 = ttk.Frame(tab2)
win6.grid(row= 5, column=1, rowspan=1)

sixth_list = Listbox(win6, width=35, height=4)
sixth_list.pack(side="left")

scrollbar6 = Scrollbar(win6, command=sixth_list.yview)
scrollbar6.pack(side="right", fill="y")
sixth_list.config(yscrollcommand=scrollbar6.set)

# 7
Label(tab2, text=group_list[6], width=35, bg="pink").grid(row= 6, column=0)
win7 = ttk.Frame(tab2)
win7.grid(row= 7, column=0, rowspan=1)

seventh_list = Listbox(win7, width=35, height=4)
seventh_list.pack(side="left")

scrollbar7 = Scrollbar(win7, command=seventh_list.yview)
scrollbar7.pack(side="right", fill="y")
seventh_list.config(yscrollcommand=scrollbar7.set)

# 8
Label(tab2, text=group_list[7], width=35, bg="pink").grid(row= 6, column=1)
win8 = ttk.Frame(tab2)
win8.grid(row= 7, column=1, rowspan=1)

eighth_list = Listbox(win8, width=35, height=4)
eighth_list.pack(side="left")

scrollbar8 = Scrollbar(win8, command=eighth_list.yview)
scrollbar8.pack(side="right", fill="y")
eighth_list.config(yscrollcommand=scrollbar8.set)

# 9
Label(tab2, text=group_list[8], width=35, bg="pink").grid(row= 8, column=0)
win9 = ttk.Frame(tab2)
win9.grid(row= 9, column=0, rowspan=1)

nineth_list = Listbox(win9, width=35, height=4)
nineth_list.pack(side="left")

scrollbar9 = Scrollbar(win9, command=nineth_list.yview)
scrollbar9.pack(side="right", fill="y")
nineth_list.config(yscrollcommand=scrollbar3.set)

# 10
Label(tab2, text=group_list[9], width=35, bg="pink").grid(row= 8, column=1)
win10 = ttk.Frame(tab2)
win10.grid(row= 9, column=1, rowspan=1)

tenth_list = Listbox(win10, width=35, height=4)
tenth_list.pack(side="left")

scrollbar10 = Scrollbar(win10, command=tenth_list.yview)
scrollbar10.pack(side="right", fill="y")
tenth_list.config(yscrollcommand=scrollbar10.set)


##### 그룹에서 과목 삭제하는 버튼 및 merge
Button(tab2, text = "OUT 1", width =10, bg='pink', command=OUT1).grid(row = 0, column = 2, rowspan=1)
Button(tab2, text = "OUT 2", width =10, bg='pink', command=OUT2).grid(row = 1, column = 2, rowspan=1)
Button(tab2, text = "OUT 3", width =10, bg='pink', command=OUT3).grid(row = 2, column = 2, rowspan=1)
Button(tab2, text = "OUT 4", width =10, bg='pink', command=OUT4).grid(row = 3, column = 2, rowspan=1)
Button(tab2, text = "OUT 5", width =10, bg='pink', command=OUT5).grid(row = 4, column = 2, rowspan=1)
Button(tab2, text = "OUT 6", width =10, bg='pink', command=OUT6).grid(row = 5, column = 2, rowspan=1)
Button(tab2, text = "OUT 7", width =10, bg='pink', command=OUT7).grid(row = 6, column = 2, rowspan=1)
Button(tab2, text = "OUT 8", width =10, bg='pink', command=OUT8).grid(row = 7, column = 2, rowspan=1)
Button(tab2, text = "OUT 9", width =10, bg='pink', command=OUT9).grid(row = 8, column = 2, rowspan=1)
Button(tab2, text = "OUT 10", width =10, bg='pink', command=OUT10).grid(row = 9, column = 2, rowspan=1)
Button(tab2, text = "Merge", width =10, bg='pink').grid(row = 10, column = 2, rowspan=1)



tab2_list_boxes = [\
first_list, second_list, third_list, fourth_list, \
fifth_list, sixth_list, seventh_list, eighth_list, \
nineth_list, tenth_list]





# tab 3 (결과보기)
day_name = ["","Mon","Tue","Wed","Thu","Fri","Sat"]
time_list = ["9","10","11","12","1","2","3","4","5","6","7","8","9"]

#test 조합 -> 과목 구분 / 과목명 은 후에 공지되는대로 수정
test_lists = []
test_lists.append([[0,2,3,6,7], [1,1,2,6,7], [2,1,5,6], [3,1,2,3,4,6,7],[4,5,6]])#2학기
test_lists.append([[0,2,3,5,6,7,8,9,10],[1,3,4,6,7,8,9],[2,1,5,6],[3,5,6,7,8,9],[4,2,3]])#건축

com_num_list = [] #이전 시간표frame 삭제 시 필요함

tab3_frame1 = Frame(tab3, relief = 'flat')
tab3_frame1.grid(row = 0, column = 0)

tab3_frame2 = Frame(tab3, relief = 'flat')
tab3_frame2.grid(row = 0, column = 1)

for i in range(0,7):
  Label(tab3_frame1,text = day_name[i], width=10, bg="pink").grid(row=1,column=i)
  for k in range(len(time_list)):
    if i==0:
      Label(tab3_frame1, text=time_list[k],  width = 10, height = 3, bg = "white", anchor = "n").grid(row = k+2, column = i)
    else:
      Label(tab3_frame1, width = 10, height = 3, bg = "white", relief = 'solid', bd = 0.1).grid(row = k+2, column = i)


combi = ttk.Combobox(tab3_frame2, width=10, height=10, values=test_lists, state = 'readonly')
combi.grid(row = 4, column = 7)
combi.set("Combi")


Button(tab3_frame2, text = "See", width = 10, bg = "pink", command =see_b).grid(row = 8, column = 7)


# 조합 콤보박스 위에 뭔지 설명하는 말
combo_label = Label(tab3_frame2, text="당신이 원하는 조합을 골라보세요!!\n    ↓   " )
combo_label.grid(row = 3, column = 7)


# tab3 스샷 찍어서 저장하기

nowdate = datetime.datetime.now()
re_nowdate = nowdate.strftime("%Y-%m-%d %H%M")


Button(tab3_frame2, text="Screenshot", width=10, bg="pink", command = shot).grid(row=7, column=7)


# 프로그램 종료
Button(tab1, text = "EXIT", width = 10, bg = "Green", fg = "white", command = exit_window).grid(row = 17, column = 0)
Button(tab2, text = "EXIT", width = 10, bg = "Green", fg = "white", command = exit_window).grid(row = 10, column = 0)
Button(tab3, text = "EXIT", width = 10, bg = "Green", fg = "white", command = exit_window).grid(row = 2, column = 0, sticky = 'w')


window.mainloop()