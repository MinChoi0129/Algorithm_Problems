#import Functions
from TEXT_processing import time_table, test, getItemsBySubTheme
#import GUI_by_tkinter
#import GUI_ing
#############################################
#    오류 없이 작동하는 코드만 넣어주세요   #
#############################################

lecture_objs = time_table("timetable.txt")
test(getItemsBySubTheme("전공선택", lecture_objs))