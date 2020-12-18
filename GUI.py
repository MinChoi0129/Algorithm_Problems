from tkinter import *


count = 0

def countminus():
    global count
    count -= 1
    label1.config(text = str(count))
    
def countplus():
    global count
    count += 1
    label1.config(text = str(count))

def calculator(event):
    label2.config(text = "계산값 : " + str(eval(entry.get())))

r = Tk()
r.title("에브리타임")
r.geometry("300x200")
r.resizable(0, 0)


label1 = Label(r, text = "0", fg = "blue", relief = "solid")
label2 = Label(r, text = "", fg = "red")

bt1 = Button(r, width = 4, text = "+", command = countplus)
bt2 = Button(r, width = 4, text = "-", command = countminus)

entry = Entry(r, width = 30)






label1.pack()
label2.pack()
bt1.pack()
bt2.pack()
entry.bind("<Return>", calculator)
entry.pack()

r.mainloop()