from tkinter import Tk, Entry, Button
import math

pi = str(round(math.pi, 2)) # 3.141... -> 3.14
e = str(round(math.e, 2)) # 2.718... -> 2.72

def click(key):

  if key == "C": # Delete all
    display.delete(0, 'end')

  elif key == "=": # Evaluation
    expression = display.get()
    display.delete(0, 'end')
    display.insert(0, eval(expression))

  elif key == "sin" or key == "cos": # Trigonometric Function
    rad = math.radians(float(display.get()))
    display.delete(0, 'end')

    if key == "sin":
      display.insert(0, str(math.sin(rad)))
    else:
      display.insert(0, str(math.cos(rad)))

  elif key == "del": # Delete last one character
    display.delete(len(display.get()) - 1, 'end')

  elif key == "pi" or key == "e": # CONSTANTS

    if key == "pi":
      display.insert('end', pi)
    else:
      display.insert('end', e)
      
  elif key == "sqrt" or key == "log": # Square Root, Logarithm
    R = float(display.get())
    display.delete(0, 'end')

    if key == "sqrt":
      display.insert(0, str(math.sqrt(R)))
    else:
      display.insert(0, str(math.log(R)))

  else: # 7, 8, 9, /, 4, 5, 6, *, 1, 2, 3, -, 0, ., +
    display.insert('end', key)

window = Tk()
window.title("My Calculator")
display = Entry(window, width=36, bg="yellow")
display.grid(row=0, column=0, columnspan=6)

button_list = \
[
'7', '8', '9', '/', 'C', 'sin',\
'4', '5', '6', '*', 'del', 'cos',\
'1', '2', '3', '-', 'pi', 'sqrt',\
'0', '.', '=', '+', 'e', 'log'\
]

row_index = 1
col_index = 0

for button_text in button_list:
  def process(t = button_text):
    click(t)
  Button(window, text = button_text, width = 5, command = process).grid(row = row_index, column = col_index)
  col_index += 1
  if col_index > 5:
    row_index += 1
    col_index = 0


window.mainloop()
