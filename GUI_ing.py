from tkinter import *
from tkinter import ttk

window = Tk()

window.title("TimeTable")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Choice')
tab_control.add(tab2, text='Groups')
tab_control.add(tab3, text='Timetable')

tab_control.pack(expand=1, fill='both')

sub_title=Label(tab1, text="Search subject",font = ("", 13), width=25, bg="dark grey")
sub_title_1=Label(tab1,text="Lecture", font = ("", 13), width=25, bg="grey")
#search=Entry(tab1,bg = "pink",width=25)

#검색과 강의
sub_title.grid(row=0,column=0)
sub_title_1.grid(row=0,column=1)
#sub_title_2.grid(row=0, column = 2)
#search.grid(row=2,column=0)

역교 = ["None", "Essential", "Choose"]
통교 = ["None", "Moonhak", "History_cheolhak", "Human_society", "science_kisool", "Art and Sports", "Fusion"]
개교 = ["None", "jinro_job", "changupsanhakcooper", "etc"]
기초 = ["None", "waoguka", "InmoonSahui ", "nature"]
교직 = ["None", "Gyogick"]
일반 = ["None", "Ilban_seontack"]
전공 = ["None", "Cs_pilsoo", "Cs_seontack"]

Label(tab1,text="Yeoklyang_G",width=35,bg="pink").grid(row = 2, column = 0)
cb1 = ttk.Combobox(tab1, width=34, height=10, values=역교)
cb1.grid(row = 3, column = 0)
cb1.set("Choose Option")


Label(tab1,text="Tonghab_G",width=35,bg="pink").grid(row = 4, column = 0)
cb2 = ttk.Combobox(tab1, width=34, height=10, values=통교)
cb2.grid(row = 5, column = 0)
cb2.set("Choose Option")


Label(tab1,text="Gaechuck_G",width=35,bg="pink").grid(row = 6, column = 0)
cb3 = ttk.Combobox(tab1, width=34, height=10, values=개교)
cb3.grid(row = 7, column = 0)
cb3.set("Choose Option")


Label(tab1,text="Gicho_G",width=35,bg="pink").grid(row = 8, column = 0)
cb4 = ttk.Combobox(tab1, width=34, height=10, values=기초)
cb4.grid(row = 9, column = 0)
cb4.set("Choose Option")

Label(tab1,text="Gyogick",width=35,bg="pink").grid(row = 10, column = 0)
cb5 = ttk.Combobox(tab1, width=34, height=10, values=교직)
cb5.grid(row = 11, column = 0)
cb5.set("Choose Option")


Label(tab1,text="Ilban_seontack",width=35,bg="pink").grid(row = 12, column = 0)
cb6 = ttk.Combobox(tab1, width=34, height=10, values=일반)
cb6.grid(row = 13, column = 0)
cb6.set("Choose Option")

Label(tab1,text="CS Jeongong",width=35,bg="pink").grid(row = 14, column = 0)
cb7 = ttk.Combobox(tab1, width=34, height=10, values=전공)
cb7.grid(row = 15, column = 0)
cb7.set("Choose Option")

Button(tab1, text = "Search", width =33, bg='white').grid(row = 16, column = 0)


#tab 2 (Groups)
group_list=["Group1","Group2","Group3","Group4","Group5","Group6","Group7","Group8","Group9","Group10"]
row_num=1
col_num=0

for i in range(0,10):
    if i%2==0:
        col_num=2
        Label(tab2,text=group_list[i],width=35,bg="pink").grid(row=row_num,column=col_num)
        for j in range(0,2):
            Label(tab2, text="", width=35, height=2, bg="white").grid(row=row_num+1,column=col_num)
            row_num+=1 
    else:
        col_num=3
        Label(tab2, text=group_list[i],width=35,bg="pink").grid(row=row_num-2,column=col_num)
        for j in range(0,2):
            Label(tab2, text="", width=35, height=2, bg="white").grid(row=row_num-1,column=col_num)
            row_num+=1

Button(tab2, text = "Merge", width =15, bg='grey').grid(row = 20, column = 10)

day_name = ["","Mon","Tue","Wed","Thu","Fri"]
time_list = ["9","10","11","12","1","2","3","4"]

for i in range(0,6):
  Label(tab3,text = day_name[i], width=10, bg="pink").grid(row=1,column=i)
  for k in range(0,8):
    Label(tab3, width = 10, height = 3, bg = "white").grid(row = k+2, column = i)

window.mainloop()