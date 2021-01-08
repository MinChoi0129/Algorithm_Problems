from tkinter import *
from tkinter import ttk, messagebox, PhotoImage
from PIL import ImageGrab, ImageTk
from TEXT_processing import time_table, getItemsBySubTheme, setClassInfo
from itertools import product
import datetime, random, sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

################################################################
##########       global variables 정의 및 초기화       ##########
################################################################

window = Tk()
subject_list = Listbox()
window.title("TimeTable")
window.attributes('-fullscreen', True)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='과목선택')
tab_control.add(tab2, text='그룹')
tab_control.add(tab3, text='결과보기')
tab_control.add(tab4, text='캡쳐모음')
tab_control.pack(expand=1, fill='both')
tab3_frame1, tab2_frame2, tab3_frame3, tab4_frame1 = ttk.Frame(), ttk.Frame(), ttk.Frame(), ttk.Frame()

lecture_objs = time_table(resource_path("timetable.txt"))
for obj in lecture_objs:
    setClassInfo(obj)

searched_objs = []
selected_groups = [[], [], [], [], [], [], [], [], [], []]
day_name = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
time_list = ["9", "10", "11", "12", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
com_num_list = []
test_lists = []

역교 = ["None", "필수역량교양", "선택역량교양"]
통교 = ["None", "문학과문화", "역사와철학", "인간과사회", "과학과기술", "예술과체육", "융복합영역"]
개교 = ["None", "진로·취업", "창업·산학협력", "기타"]
기초 = ["None", "외국어계열", "인문사회계열", "자연계열"]
교직 = ["None", "교직"]
일반 = ["None", "일반선택"]
전공 = ["None", "전공필수", "전공선택"]


##############################################################
###################        함수 정의        ###################
##############################################################


def In_Lecture():    # In버튼 누르면 group에 추가
    global selected_groups, subject_list, searched_objs, variety1, tab2_list_boxes
    chosen_group = int(variety1.get())    # 선택한 그룹번호
    idx = -1
    try:
        idx = subject_list.curselection()[0]    # 리스트박스에서 선택된 과목의 인덱스
    except:
        messagebox.showinfo("오류", "과목을 선택하세요")
        return

    dupl = False
    for k in range(10):
        if searched_objs[idx] in selected_groups[k]:
            messagebox.showinfo("중복 담기", "이미 담은 과목입니다.")
            dupl = True
            break

    if not dupl:
        selected_groups[chosen_group].append(searched_objs[idx])
        messagebox.showinfo("성공", "과목을 담았습니다.")
        tab2_list_boxes[chosen_group].insert("end", selected_groups[chosen_group][-1].get_brief_info())


def exit_window():    # 프로그램 종료
    global window
    window.destroy()


def search_subjects():    # Search버튼 누르면 조건에 맞는 강의들을 보여줌
    global searched_objs, search_by_name_or_prof
    searched_objs = []    # 부를때마다 초기화
    name = search_by_name_or_prof.get()
    yeok = cb1.get()
    tong = cb2.get()
    gae = cb3.get()
    gicho = cb4.get()
    gyojik = cb5.get()
    ilban = cb6.get()
    cs = cb7.get()

    if name != "강의명 또는 교수명을 입력하세요":    # 검색어에 무언가라도 적혀있는 경우

        if yeok == "None" and tong == "None" and gae == "None" and \
                gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 검색어만 적은 경우
            for lecture_obj in lecture_objs:
                if name in lecture_obj.name or name in lecture_obj.prof:    # 강의명 또는 교수명에서 찾는다.
                    searched_objs.append(lecture_obj)

        else:    # 검색어와 옵션을 함께 고른 경우
            if yeok != "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 역량교양에서 선택

                for lecture_obj in getItemsBySubTheme(yeok, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            elif yeok == "None" and tong != "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 통합교양에서 선택

                for lecture_obj in getItemsBySubTheme(tong, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            elif yeok == "None" and tong == "None" and gae != "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 개척교양에서 선택

                for lecture_obj in getItemsBySubTheme(gae, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho != "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 기초과정에서 선택

                for lecture_obj in getItemsBySubTheme(gicho, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik != "None" and ilban == "None" and cs == "None":    # 교직에서 선택

                for lecture_obj in getItemsBySubTheme(gyojik, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban != "None" and cs == "None":    # 일반선택에서 선택

                for lecture_obj in getItemsBySubTheme(ilban, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs != "None":    # CS전공에서 선택

                for lecture_obj in getItemsBySubTheme(cs, lecture_objs):
                    if name in lecture_obj.name or name in lecture_obj.prof:
                        searched_objs.append(lecture_obj)

            else:    # 다중선택
                messagebox.showinfo("옵션 다중 선택", "옵션을 하나만 골라주세요.")

    elif name == "강의명 또는 교수명을 입력하세요" or name == "":    # 검색어 없는 경우
        if yeok == "None" and tong == "None" and gae == "None" and \
                gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":
            messagebox.showinfo("필터없음", "강의명/교수명으로 검색하거나 옵션 한 개를 골라주세요.")    # 아무것도 안고른경우

        else:    # 옵션을 고르긴 고른 경우
            if yeok != "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 역량교양에서 선택
                searched_objs = getItemsBySubTheme(yeok, lecture_objs)

            elif yeok == "None" and tong != "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 통합교양에서 선택
                searched_objs = getItemsBySubTheme(tong, lecture_objs)

            elif yeok == "None" and tong == "None" and gae != "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 개척교양에서 선택
                searched_objs = getItemsBySubTheme(gae, lecture_objs)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho != "None" and gyojik == "None" and ilban == "None" and cs == "None":    # 기초과정에서 선택
                searched_objs = getItemsBySubTheme(gicho, lecture_objs)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik != "None" and ilban == "None" and cs == "None":    # 교직에서 선택
                searched_objs = getItemsBySubTheme(gyojik, lecture_objs)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban != "None" and cs == "None":    # 일반선택에서 선택
                searched_objs = getItemsBySubTheme(ilban, lecture_objs)

            elif yeok == "None" and tong == "None" and gae == "None" and \
                    gicho == "None" and gyojik == "None" and ilban == "None" and cs != "None":    # CS전공에서 선택
                searched_objs = getItemsBySubTheme(cs, lecture_objs)

            else:    # 다중선택
                messagebox.showinfo("옵션 다중 선택", "옵션을 하나만 골라주세요.")

    # List box
    global tab1, subject_list

    winf = ttk.Frame(tab1)
    winf.grid(row=1, column=2, rowspan=15)

    subject_list = Listbox(winf, width=70, height=20)
    subject_list.pack(side="left")
    for i in range(len(searched_objs)):
        subject_list.insert(i, searched_objs[i].get_brief_info() + searched_objs[i].get_day_info())

    scrollbar = Scrollbar(winf, command=subject_list.yview)
    scrollbar.pack(side="right", fill="y")
    subject_list.config(yscrollcommand=scrollbar.set)

    search_by_name_or_prof.delete(0, 'end')
    search_by_name_or_prof.insert(0, "강의명 또는 교수명을 입력하세요")


def shot():
    global tab4_frame1, captured, ldr, scb2
    img = ImageGrab.grab((2, 25, 533, 700))
    nowdate = datetime.datetime.now()
    re_now = nowdate.strftime("%Y-%m-%d %H%M%S")
    img.save(resource_path('MyTables_/' + re_now + '.png'))
    
    tab4_frame1 = ttk.Frame(tab4)
    tab4_frame1.grid(row=0, column=1)
    captured = Listbox(tab4_frame1, width=20, height=10)
    ldr = os.listdir(resource_path("MyTables_"))
    for i in range(len(ldr) - 1):
        captured.insert(i, ldr[i + 1])
    captured.pack(side="left")
    scb2 = Scrollbar(tab4_frame1, command=captured.yview)
    scb2.pack(side = "right", fill = "y")
    captured.config(yscrollcommand=scb2.set)

def combinating():
    global tab3_frame2, test_lists
    test_lists = []
    real_groups = []
    all_possible_case = []
    msg = ""
    for group in selected_groups:
        if len(group) != 0:
            real_groups.append(group)
    all_case = list(product(*real_groups))
    for i in all_case:
        if is_possible_combination(i):
            all_possible_case.append(i)

    if len(all_possible_case) >= 60:
        test_lists = random.sample(all_possible_case, 60)
        msg = str(len(all_possible_case)) + "가지의 시간표 중 60개를 생성하였습니다.\n결과보기 탭에서 확인하세요."
    else:
        random.shuffle(all_possible_case)
        test_lists = all_possible_case
        msg = str(len(test_lists)) + "가지의 시간표가 생성되었습니다.\n결과보기 탭에서 확인하세요."

    messagebox.showinfo("조합성공", msg)


    #####################################
    #######   tab 3-2 (결과보기)   #######
    #####################################
    frame_in_frame = ttk.Frame(tab3_frame2)
    frame_in_frame.grid(row=4, column=7)
    combi = Listbox(frame_in_frame, width=5, height=5)
    for i in range(len(test_lists)):
        combi.insert(i, i + 1)
    combi.pack(side="left")
    scb = Scrollbar(frame_in_frame, command=first_list.yview)
    scb.pack(side = "right", fill = "y")
    combi.config(yscrollcommand=scb.set)
    
    
    def see_combi2():  # 선택된 조합 적용
        global tab3_frame1, tab3_frame3, test_lists
        com_num = -1
        tab3_frame3 = ttk.Frame(tab3)
        tab3_frame3.grid(row=0, column=0)
        for i in range(0, 7):  # 시간표 틀(흰)
            Label(tab3_frame3, text=day_name[i], width=10, bg="RoyalBlue", fg="white").grid(row=1, column=i)
            for k in range(len(time_list)):
                if i == 0:
                    Label(tab3_frame3, text=time_list[k], width=10, height=3, bg="white", anchor="n").grid(row=k + 2, column=i)
                else:
                    Label(tab3_frame3, width=10, height=3, bg="white",relief='solid', bd=0.1).grid(row=k + 2, column=i)
                    
        time_color_list = ['#181A2C', '#152747', '#1F3767', '#496B91', '#025373', '#012E40','#186884', '#63B6BF', '#67B8DE', '#91C9E8', '#3399CC', '#5F7ED9']  # 14가지 색상(청색계열)
        random.shuffle(time_color_list)
            
        try:
            com_num = combi.curselection()[0]
            com_num_list.append(com_num)
            
            for lectures in range(len(test_lists[com_num])):  # 과목 수
                for lecture_day in range(len(test_lists[com_num][lectures].day)):# 과목 쪼개진 요일
                    for classtime in range(len((test_lists[com_num][lectures].day)[lecture_day]) - 1):# 차시
                        c_time = (test_lists[com_num][lectures].day)[lecture_day][1:]  # 차시 리스트
                        c_time_row = c_time[classtime]
                        num_label = Label(tab3_frame3, text=test_lists[com_num][lectures].name, width=10, height=3, bg=time_color_list[lectures], bd=1, fg='white', highlightbackground='darkgrey', wraplength = 60)
                        num_label.grid(row=c_time_row + 1, column=(test_lists[com_num][lectures].day)[lecture_day][0] + 1)
                        
        except:
            return
    
    def see_combi():  # 이전 시간표 삭제 및 선택된 시간표 표시
        global tab3_frame1, tab3_frame3, test_lists
        
        if len(com_num_list) == 0:
            tab3_frame1.destroy()
        else:
            tab3_frame3.destroy()
        see_combi2()

    Button(tab3_frame2, text="See", width=10, bg="skyblue", command=see_combi).grid(row=7, column=7)
    Label(tab3_frame2, text = "\n스크린샷은 1920x1080 해상도에\n최적화되어 있습니다.").grid(row=8, column=7)

    # 조합 콤보박스 위에 뭔지 설명하는 말
    combo_label = Label(tab3_frame2, text="당신이 원하는 조합을 골라보세요!!\n    ↓    ")
    combo_label.grid(row=3, column=7)

    Button(tab3_frame2, text="Screenshot", width=10, bg="skyblue", command=shot).grid(row=9, column=7)

def is_possible_combination(time_table):
    check = [[0] * 13 for _ in range(6)]
    for lecture_obj in time_table:
        if lecture_obj.day == "null":
            continue
        for detail_day in lecture_obj.day:
            for specific_time in detail_day[1:]:
                check[detail_day[0]][specific_time - 1] += 1

    for d in check:
        for c in d:
            if c >= 2:
                return False

    return True

def entry_delete(event):
    search_by_name_or_prof.delete(0, 'end')

def OUT1():
    try:
        first_idx = first_list.curselection()[0]
        first_list.delete(first_idx)
        selected_groups[0].pop(first_idx)
    except:
        pass

def OUT2():
    try:
        second_idx = second_list.curselection()[0]
        second_list.delete(second_idx)
        selected_groups[1].pop(second_idx)
    except:
        pass

def OUT3():
    try:
        third_idx = third_list.curselection()[0]
        third_list.delete(third_idx)
        selected_groups[2].pop(third_idx)
    except:
        pass

def OUT4():
    try:
        fourth_idx = fourth_list.curselection()[0]
        fourth_list.delete(fourth_idx)
        selected_groups[3].pop(fourth_idx)
    except:
        pass

def OUT5():
    try:
        fifth_idx = fifth_list.curselection()[0]
        fifth_list.delete(fifth_idx)
        selected_groups[4].pop(fifth_idx)
    except:
        pass

def OUT6():
    try:
        sixth_idx = sixth_list.curselection()[0]
        sixth_list.delete(sixth_idx)
        selected_groups[5].pop(sixth_idx)
    except:
        pass

def OUT7():
    try:
        seventh_idx = seventh_list.curselection()[0]
        seventh_list.delete(seventh_idx)
        selected_groups[6].pop(seventh_idx)
    except:
        pass

def OUT8():
    try:
        eighth_idx = eighth_list.curselection()[0]
        eighth_list.delete(eighth_idx)
        selected_groups[7].pop(eighth_idx)
    except:
        pass

def OUT9():
    try:
        nineth_idx = nineth_list.curselection()[0]
        nineth_list.delete(nineth_idx)
        selected_groups[8].pop(nineth_idx)
    except:
        pass

def OUT10():
    try:
        tenth_idx = tenth_list.curselection()[0]
        tenth_list.delete(tenth_idx)
        selected_groups[9].pop(tenth_idx)
    except:
        pass


################################################################
###########       tab마다 기능구현(tab1 ~ tab4)       ###########
################################################################


#####################################
########   tab 1 (과목선택)   ########
#####################################
Label(tab1, text="과목검색", font=("", 13), width=21, bg="SteelBlue1", fg="white").grid(row=0, column=0)
Label(tab1, text="그룹선택", font=("", 13), width=10, bg="SteelBlue2", fg="white").grid(row=0, column=1)
Label(tab1, text="강의목록", font=("", 13), width=56, bg="SteelBlue3", fg="white").grid(row=0, column=2)

search_by_name_or_prof = Entry(tab1, width=27, highlightbackground='white', highlightcolor='sky blue')
search_by_name_or_prof.grid(row=1, column=0)
search_by_name_or_prof.insert(0, '강의명 또는 교수명을 입력하세요')
search_by_name_or_prof.bind('<Button-1>', entry_delete)

Label(tab1, text="역량교양", width=27, bg="RoyalBlue", fg="white").grid(row=2, column=0)
cb1 = ttk.Combobox(tab1, width=24, height=10, values=역교, state="readonly")
cb1.grid(row=3, column=0)
cb1.set("None")

Label(tab1, text="통합교양", width=27, bg="RoyalBlue", fg="white").grid(row=4, column=0)
cb2 = ttk.Combobox(tab1, width=24, height=10, values=통교, state="readonly")
cb2.grid(row=5, column=0)
cb2.set("None")

Label(tab1, text="개척교양", width=27, bg="RoyalBlue", fg="white").grid(row=6, column=0)
cb3 = ttk.Combobox(tab1, width=24, height=10, values=개교, state="readonly")
cb3.grid(row=7, column=0)
cb3.set("None")

Label(tab1, text="기초과정", width=27, bg="RoyalBlue", fg="white").grid(row=8, column=0)
cb4 = ttk.Combobox(tab1, width=24, height=10, values=기초, state="readonly")
cb4.grid(row=9, column=0)
cb4.set("None")

Label(tab1, text="교직", width=27, bg="RoyalBlue", fg="white").grid(row=10, column=0)
cb5 = ttk.Combobox(tab1, width=24, height=10, values=교직, state="readonly")
cb5.grid(row=11, column=0)
cb5.set("None")

Label(tab1, text="일반선택", width=27, bg="RoyalBlue", fg="white").grid(row=12, column=0)
cb6 = ttk.Combobox(tab1, width=24, height=10, values=일반, state="readonly")
cb6.grid(row=13, column=0)
cb6.set("None")

Label(tab1, text="CS전공", width=27, bg="RoyalBlue", fg="white").grid(row=14, column=0)
cb7 = ttk.Combobox(tab1, width=24, height=10, values=전공, state="readonly")
cb7.grid(row=15, column=0)
cb7.set("None")

Button(tab1, text="검색", width=10, bg='skyblue', command=search_subjects).grid(row=16, column=0)


groups_frame = ttk.Frame(tab1)
groups_frame.grid(row=1, column=1, rowspan=15)
variety1 = IntVar(value=0)
Radiobutton(groups_frame, text="Group1", value=0, variable=variety1).pack()
Radiobutton(groups_frame, text="Group2", value=1, variable=variety1).pack()
Radiobutton(groups_frame, text="Group3", value=2, variable=variety1).pack()
Radiobutton(groups_frame, text="Group4", value=3, variable=variety1).pack()
Radiobutton(groups_frame, text="Group5", value=4, variable=variety1).pack()
Radiobutton(groups_frame, text="Group6", value=5, variable=variety1).pack()
Radiobutton(groups_frame, text="Group7", value=6, variable=variety1).pack()
Radiobutton(groups_frame, text="Group8", value=7, variable=variety1).pack()
Radiobutton(groups_frame, text="Group9", value=8, variable=variety1).pack()
Radiobutton(groups_frame, text="Group10", value=9, variable=variety1).pack()


Button(tab1, text="추가", width=8, bg='sky blue', command=In_Lecture).grid(row=16, column=2)


#####################################
########   tab 2 (그룹보기)   ########
#####################################
group_list = ["Group1", "Group2", "Group3", "Group4", "Group5", "Group6", "Group7", "Group8", "Group9", "Group10"]


# 1
Label(tab2, text=group_list[0], width=37, bg="RoyalBlue", fg="white").grid(row=0, column=0)
win1 = ttk.Frame(tab2)
win1.grid(row=1, column=0, rowspan=1)

first_list = Listbox(win1, width=35, height=5)
first_list.pack(side="left")

scrollbar1 = Scrollbar(win1, command=first_list.yview)
scrollbar1.pack(side="right", fill="y")
first_list.config(yscrollcommand=scrollbar1.set)

# 2
Label(tab2, text=group_list[1], width=37, bg="RoyalBlue", fg="white").grid(row=0, column=1)
win2 = ttk.Frame(tab2)
win2.grid(row=1, column=1, rowspan=1)

second_list = Listbox(win2, width=35, height=5)
second_list.pack(side="left")

scrollbar2 = Scrollbar(win2, command=second_list.yview)
scrollbar2.pack(side="right", fill="y")
second_list.config(yscrollcommand=scrollbar2.set)


# 3
Label(tab2, text=group_list[2], width=37, bg="RoyalBlue", fg="white").grid(row=2, column=0)
win3 = ttk.Frame(tab2)
win3.grid(row=3, column=0, rowspan=1)

third_list = Listbox(win3, width=35, height=5)
third_list.pack(side="left")

scrollbar3 = Scrollbar(win3, command=third_list.yview)
scrollbar3.pack(side="right", fill="y")
third_list.config(yscrollcommand=scrollbar3.set)

# 4
Label(tab2, text=group_list[3], width=37, bg="RoyalBlue", fg="white").grid(row=2, column=1)
win4 = ttk.Frame(tab2)
win4.grid(row=3, column=1, rowspan=1)

fourth_list = Listbox(win4, width=35, height=5)
fourth_list.pack(side="left")

scrollbar4 = Scrollbar(win4, command=fourth_list.yview)
scrollbar4.pack(side="right", fill="y")
fourth_list.config(yscrollcommand=scrollbar4.set)

# 5
Label(tab2, text=group_list[4], width=37, bg="RoyalBlue", fg="white").grid(row=4, column=0)
win5 = ttk.Frame(tab2)
win5.grid(row=5, column=0, rowspan=1)

fifth_list = Listbox(win5, width=35, height=5)
fifth_list.pack(side="left")

scrollbar5 = Scrollbar(win5, command=fifth_list.yview)
scrollbar5.pack(side="right", fill="y")
fifth_list.config(yscrollcommand=scrollbar5.set)

# 6
Label(tab2, text=group_list[5], width=37, bg="RoyalBlue", fg="white").grid(row=4, column=1)
win6 = ttk.Frame(tab2)
win6.grid(row=5, column=1, rowspan=1)

sixth_list = Listbox(win6, width=35, height=5)
sixth_list.pack(side="left")

scrollbar6 = Scrollbar(win6, command=sixth_list.yview)
scrollbar6.pack(side="right", fill="y")
sixth_list.config(yscrollcommand=scrollbar6.set)

# 7
Label(tab2, text=group_list[6], width=37, bg="RoyalBlue", fg="white").grid(row=6, column=0)
win7 = ttk.Frame(tab2)
win7.grid(row=7, column=0, rowspan=1)

seventh_list = Listbox(win7, width=35, height=5)
seventh_list.pack(side="left")

scrollbar7 = Scrollbar(win7, command=seventh_list.yview)
scrollbar7.pack(side="right", fill="y")
seventh_list.config(yscrollcommand=scrollbar7.set)

# 8
Label(tab2, text=group_list[7], width=37, bg="RoyalBlue", fg="white").grid(row=6, column=1)
win8 = ttk.Frame(tab2)
win8.grid(row=7, column=1, rowspan=1)

eighth_list = Listbox(win8, width=35, height=5)
eighth_list.pack(side="left")

scrollbar8 = Scrollbar(win8, command=eighth_list.yview)
scrollbar8.pack(side="right", fill="y")
eighth_list.config(yscrollcommand=scrollbar8.set)

# 9
Label(tab2, text=group_list[8], width=37, bg="RoyalBlue", fg="white").grid(row=8, column=0)
win9 = ttk.Frame(tab2)
win9.grid(row=9, column=0, rowspan=1)

nineth_list = Listbox(win9, width=35, height=5)
nineth_list.pack(side="left")

scrollbar9 = Scrollbar(win9, command=nineth_list.yview)
scrollbar9.pack(side="right", fill="y")
nineth_list.config(yscrollcommand=scrollbar3.set)

# 10
Label(tab2, text=group_list[9], width=37, bg="RoyalBlue", fg="white").grid(row=8, column=1)
win10 = ttk.Frame(tab2)
win10.grid(row=9, column=1, rowspan=1)

tenth_list = Listbox(win10, width=35, height=5)
tenth_list.pack(side="left")

scrollbar10 = Scrollbar(win10, command=tenth_list.yview)
scrollbar10.pack(side="right", fill="y")
tenth_list.config(yscrollcommand=scrollbar10.set)

# 그룹에서 과목 삭제하는 버튼 및 merge
Button(tab2, text="OUT 1", width=10, bg='skyblue', command=OUT1).grid(row=0, column=2, rowspan=1)
Button(tab2, text="OUT 2", width=10, bg='skyblue', command=OUT2).grid(row=1, column=2, rowspan=1)
Button(tab2, text="OUT 3", width=10, bg='skyblue', command=OUT3).grid(row=2, column=2, rowspan=1)
Button(tab2, text="OUT 4", width=10, bg='skyblue', command=OUT4).grid(row=3, column=2, rowspan=1)
Button(tab2, text="OUT 5", width=10, bg='skyblue', command=OUT5).grid(row=4, column=2, rowspan=1)
Button(tab2, text="OUT 6", width=10, bg='skyblue', command=OUT6,).grid(row=5, column=2, rowspan=1)
Button(tab2, text="OUT 7", width=10, bg='skyblue', command=OUT7).grid(row=6, column=2, rowspan=1)
Button(tab2, text="OUT 8", width=10, bg='skyblue', command=OUT8).grid(row=7, column=2, rowspan=1)
Button(tab2, text="OUT 9", width=10, bg='skyblue', command=OUT9).grid(row=8, column=2, rowspan=1)
Button(tab2, text="OUT 10", width=10, bg='skyblue', command=OUT10).grid(row=9, column=2)
Button(tab2, text="Merge", width=10, bg='skyblue1', command=combinating).grid(row=10, column=2)


tab2_list_boxes = [
    first_list, second_list, third_list, fourth_list, fifth_list, sixth_list, seventh_list, eighth_list, nineth_list, tenth_list
]


#####################################
#######   tab 3-1 (결과보기)   #######
#####################################
tab3_frame1 = ttk.Frame(tab3, relief='flat')
tab3_frame1.grid(row=0, column=0)

tab3_frame2 = ttk.Frame(tab3, relief='flat')
tab3_frame2.grid(row=0, column=1)

for i in range(0, 7):  # 시간표 틀
    Label(tab3_frame1, text=day_name[i], width=10, bg="RoyalBlue", fg="white").grid(row=1, column=i)
    for k in range(len(time_list)):
        if i == 0:
            Label(tab3_frame1, text=time_list[k], width=10, height=3, bg="white", anchor="n").grid( row=k+2, column=i)
        else:
            Label(tab3_frame1, width=10, height=3, bg="white", relief='solid', bd=0.1).grid(row=k+2, column=i)

#####################################
#######   tab 4 (캡쳐모음)   #######
#####################################

def show_shot_img():
    global captured, ldr, shot_img
    idx = -1
    try:
        idx = captured.curselection()[0]    # 리스트박스에서 선택된 과목의 인덱스
    except:
        messagebox.showinfo("오류", "사진을 선택하세요")
        return

    img2 = PhotoImage(file = (resource_path("MyTables_/" + ldr[idx + 1])))
    shot_img.configure(image=img2)
    shot_img.image = img2
    

    
    
    
Button(tab4, text = "보기", width=10, bg="skyblue", command=show_shot_img).grid(row=1, column=1)
asd = PhotoImage(file = resource_path("MyTables_/0basic.png"))
shot_img = Label(tab4, image=asd)
shot_img.grid(row=0, column=0, rowspan = 15)
tab4_frame1 = ttk.Frame(tab4)
tab4_frame1.grid(row=0, column=1)
captured = Listbox(tab4_frame1, width=20, height=10)
ldr = os.listdir(resource_path("MyTables_"))
for i in range(len(ldr) - 1):
    captured.insert(i, ldr[i + 1])
captured.pack(side="left")
scb2 = Scrollbar(tab4_frame1, command=captured.yview)
scb2.pack(side = "right", fill = "y")
captured.config(yscrollcommand=scb2.set)

def file_delete():
    global captured, ldr
    idx = -1
    try:
        idx = captured.curselection()[0]    # 리스트박스에서 선택된 과목의 인덱스
    except:
        messagebox.showinfo("오류", "파일을 선택하세요")
        return
    
    file_dir = resource_path("MyTables_/" + ldr[idx + 1])
    if os.path.isfile(file_dir):
        os.remove(file_dir)
    else:
        messagebox.showinfo("오류", "파일을 선택하세요")
    
    tab4_frame1 = ttk.Frame(tab4)
    tab4_frame1.grid(row=0, column=1)
    captured = Listbox(tab4_frame1, width=20, height=10)
    ldr = os.listdir(resource_path("MyTables_"))
    for i in range(len(ldr) - 1):
        captured.insert(i, ldr[i + 1])
    captured.pack(side="left")
    scb2 = Scrollbar(tab4_frame1, command=captured.yview)
    scb2.pack(side = "right", fill = "y")
    captured.config(yscrollcommand=scb2.set)

# 기타 나머지
Button(tab1, text="EXIT", width=10, bg="slateblue2", fg="white", command=exit_window).grid(row=17, column=0)
Label(tab2).grid(row=11, column=2) # 공백
Button(tab2, text="EXIT", width=10, bg="slateblue2", fg="white", command=exit_window).grid(row=12, column=2)
Button(tab3, text="EXIT", width=10, bg="slateblue2", fg="white", command=exit_window).grid(row=2, column=0, sticky='w')
Button(tab4, text="삭제", width=10, bg="red", fg="white", command=file_delete).grid(row=2, column=1)
Button(tab4, text="EXIT", width=10, bg="slateblue2", fg="white", command=exit_window).grid(row=3, column=1)
window.mainloop()