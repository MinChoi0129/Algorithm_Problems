#############################
#   함수는 여기서 정의합니다  #
#############################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from TEXT_processing import time_table, test, getItemsBySubTheme # 테스트용

def search_subjects():
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
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong != "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 통합교양에서 선택

				for lecture_obj in getItemsBySubTheme(tong, lecture_objs):
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae != "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None": # 개척교양에서 선택

				for lecture_obj in getItemsBySubTheme(gae, lecture_objs):
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho != "None" and gyojik == "None" and ilban == "None" and cs == "None": # 기초과정에서 선택

				for lecture_obj in getItemsBySubTheme(gicho, lecture_objs):
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik != "None" and ilban == "None" and cs == "None": # 교직에서 선택

				for lecture_obj in getItemsBySubTheme(gyojik, lecture_objs):
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban != "None" and cs == "None": # 일반선택에서 선택

				for lecture_obj in getItemsBySubTheme(ilban, lecture_objs):
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			elif yeok == "None" and tong == "None" and gae == "None" and \
				gicho == "None" and gyojik == "None" and ilban == "None" and cs != "None": # CS전공에서 선택

				for lecture_obj in getItemsBySubTheme(cs, lecture_objs):
					if name in lecture_obj.name:
						searched_objs.append(lecture_obj)

			else : # 다중선택
				messagebox.showinfo("Multiple Option Selected", "Please choose only one option")

	else: # 검색어 없는 경우
		if yeok == "None" and tong == "None" and gae == "None" and gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":
			messagebox.showinfo("No Option Selected", "Please choose option more than one") # 아무것도 안고른경우

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
				messagebox.showinfo("Multiple Option Selected", "Please choose only one option")

	##### List box

	scrollbar = Scrollbar(ttk.Frame(window))
	scrollbar.grid(row=1, column=2)

	subject_list = Listbox(tab1, width=35, height = 18, yscrollcommand=scrollbar.set)
	for i in range(len(searched_objs)):
		subject_list.insert(i, (searched_objs[i].name + "\n"))
	subject_list.grid(row=1, rowspan = 15, column=1)

	scrollbar['command']= subject_list.yview





window = Tk()

window.title("TimeTable")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Choice')
tab_control.add(tab2, text='Groups')
tab_control.add(tab3, text='Timetable')
tab_control.add(tab4, text ='save')

tab_control.pack(expand=1, fill='both')

sub_title=Label(tab1, text="Search subject",font = ("", 13), width=25, bg="dark grey")
sub_title_1=Label(tab1,text="Lecture", font = ("", 13), width=25, bg="grey")
#search=Entry(tab1,bg = "pink",width=25)

#검색과 강의
sub_title.grid(row=0,column=0)
sub_title_1.grid(row=0,column=1)
#sub_title_2.grid(row=0, column = 2)
#search.grid(row=2,column=0)

search_by_name_or_prof = Entry(tab1, width = 35)
search_by_name_or_prof.grid(row = 1, column = 0)

역교 = ["None", "필수역량교양", "선택역량교양"]
통교 = ["None", "문학과문화", "역사와철학", "인간과사회", "과학과기술", "예술과체육", "융복합영역"]
개교 = ["None", "진로·취업", "창업·산학협력", "기타"]
기초 = ["None", "외국어계열", "인문사회계열", "자연계열"]
교직 = ["None", "교직"]
일반 = ["None", "일반선택"]
전공 = ["None", "전공필수", "전공선택"]

Label(tab1,text="Yeoklyang_G",width=35,bg="pink").grid(row = 2, column = 0)
cb1 = ttk.Combobox(tab1, width=34, height=10, values=역교)
cb1.grid(row = 3, column = 0)
cb1.set("None")


Label(tab1,text="Tonghab_G",width=35,bg="pink").grid(row = 4, column = 0)
cb2 = ttk.Combobox(tab1, width=34, height=10, values=통교)
cb2.grid(row = 5, column = 0)
cb2.set("None")


Label(tab1,text="Gaechuck_G",width=35,bg="pink").grid(row = 6, column = 0)
cb3 = ttk.Combobox(tab1, width=34, height=10, values=개교)
cb3.grid(row = 7, column = 0)
cb3.set("None")


Label(tab1,text="Gicho_G",width=35,bg="pink").grid(row = 8, column = 0)
cb4 = ttk.Combobox(tab1, width=34, height=10, values=기초)
cb4.grid(row = 9, column = 0)
cb4.set("None")

Label(tab1,text="Gyogick",width=35,bg="pink").grid(row = 10, column = 0)
cb5 = ttk.Combobox(tab1, width=34, height=10, values=교직)
cb5.grid(row = 11, column = 0)
cb5.set("None")


Label(tab1,text="Ilban_seontack",width=35,bg="pink").grid(row = 12, column = 0)
cb6 = ttk.Combobox(tab1, width=34, height=10, values=일반)
cb6.grid(row = 13, column = 0)
cb6.set("None")

Label(tab1,text="CS Jeongong",width=35,bg="pink").grid(row = 14, column = 0)
cb7 = ttk.Combobox(tab1, width=34, height=10, values=전공)
cb7.grid(row = 15, column = 0)
cb7.set("None")


searched_objs = [] # search 버튼을 눌러서 검색하여 나온 최근 결과

lecture_objs = time_table("timetable.txt")


			
Button(tab1, text = "Search", width = 15, bg='white', command = search_subjects).grid(row = 16, column = 0)

def In_Lecture(): #In버튼 누르면 group에 추가하는거 적용
  row_num=1
  choose_lecture=[]
  choose_lecture.append(In_button)
  for i in range(len(choose_lecture)):
    if i%2==0:
      Label(tab2, text="", width=35, height=2, bg="white").grid(row=row_num+1,column=col_num)
      row_num+=1 
    else:
      Label(tab2, text="", width=35, height=2, bg="white").grid(row=row_num-1,column=col_num)
      row_num+=1
  return

##### 과목 담는 버튼 만들기

groups = []
for i in range(10):
  groups.append('Group'+str(i+1))

group_comb = ttk.Combobox(tab1, width=8, height=10, values=groups)
group_comb.grid(row = 13, column = 2, rowspan=1)
group_comb.set("None")
In_button=Button(tab1, text = "IN", width =8, bg='light grey',command=In_Lecture)
In_button.grid(row = 15, column = 2, rowspan=1)

#tab 2 (Groups)
group_list=["Group1","Group2","Group3","Group4","Group5","Group6","Group7","Group8","Group9","Group10"]
row_num=0
col_num=0

for i in range(0,10):
    if i%2==0:
        col_num=0
        Label(tab2,text=group_list[i],width=35,bg="pink").grid(row=row_num,column=col_num)
        for j in range(0,2):
            Label(tab2, text="", width=35, height=2, bg="white").grid(row=row_num+1,column=col_num)
            row_num+=1 
    else:
        col_num=1
        Label(tab2, text=group_list[i],width=35,bg="pink").grid(row=row_num-2,column=col_num)
        for j in range(0,2):
            Label(tab2, text="", width=35, height=2, bg="white").grid(row=row_num-1,column=col_num)
            row_num+=1

##### 그룹에서 과목 삭제하는 버튼 및 merge

Button(tab2, text = "OUT", width =10, bg='light grey').grid(row = 18, column = 10, rowspan=1)
Button(tab2, text = "Merge", width =10, bg='grey').grid(row = 19, column = 10, rowspan=1)

day_name = ["","Mon","Tue","Wed","Thu","Fri","Sat"]
time_list = ["9","10","11","12","1","2","3","4"]

for i in range(0,7):
  Label(tab3,text = day_name[i], width=10, bg="pink").grid(row=1,column=i)
  for k in range(0,8):
    if i==0:
      Label(tab3, text=time_list[k],  width = 10, height = 3, bg = "white", anchor = "n").grid(row = k+2, column = i)
    else:
      Label(tab3, width = 10, height = 3, bg = "white").grid(row = k+2, column = i)



#test 조합 (combobox 간격체크용)
test_lists = []
for i in range(60):
  test_lists.append('com'+str(i))


#만드는중

    
    


def see_b(): #선택된 조합 적용
  
  
  return

def save_b(): #시간표 저장
  return


combi = ttk.Combobox(tab3, width=10, height=10, values=test_lists)
combi.grid(row = 4, column = 7)
combi.set("None")

Button(tab3, text = "See", width = 10, bg = "pink", command =see_b).grid(row = 8, column = 7) 

Button(tab3, text = "Save", width = 10, bg = "pink").grid(row = 9, column = 7) 


window.mainloop()
