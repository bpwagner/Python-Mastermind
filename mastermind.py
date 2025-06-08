from tkinter import *
import random



currRow = []
Rows = []
Solution = []

Colors = ['magenta2', 'cyan', 'purple2','teal','yellow','dark green']


def DrawRow(ThisRow, row):
  col = 0
  offset = 20
  spacing = 20
  size = 20

  for pegColor in ThisRow:
    canvas1.create_oval(spacing * col + offset, spacing  * row + offest, spacing * col+ size + offset,spacing   * row +size + offset, fill=pegColor)
    col += 1
  pass

def DrawBoard():
  #canvas1.create_rectangle(30, 30, 70, 70, fill='dark green')
  row = 0
  col = 0

  #draw the rows

  #for pegColor in currRow:
  #  canvas1.create_oval(80 * col, 30  * row, 80 * col+50,30  # row +50, fill=pegColor)
  #  col += 1

  DrawRow(currRow, row)

  pass


def Color(c):
  global currRow
  global Rows
  if len(currRow) < 4:
    currRow.append(c)
  print(currRow)
  DrawBoard()
  pass

def Delete():
    pass

def Check():
    global currRow
    global Rows
    if len(currRow == 4):
      Rows.append(currRow)
      currRow = []

    print (rows)
    pass

root = Tk()
root.title("MasterMind")
root.configure(background = 'white')

frame1 = Frame(root, bg='sky blue', bd= 10)
frame1.pack(side=TOP)

canvas1 = Canvas(frame1, width = 400, height=400)
canvas1.pack()

frame2 = Frame(root)

c1 = Button(frame2, text=" ", bg=Colors[0], command=lambda: Color(Colors[0]))
c1.pack(side=LEFT)

c2 = Button(frame2, text=" ", bg=Colors[1], command=lambda: Color(Colors[1]))
c2.pack(side=LEFT)

c3 = Button(frame2, text=" ", bg=Colors[2], command=lambda: Color(Colors[2]))
c3.pack(side=LEFT)

c4 = Button(frame2, text=" ", bg=Colors[3], command=lambda: Color(Colors[3]))
c4.pack(side=LEFT)

c5 = Button(frame2, text=" ", bg=Colors[4], command=lambda: Color(Colors[4]))
c5.pack(side=LEFT)


c6 = Button(frame2, text=" ", bg=Colors[5], command=lambda: Color(Colors[5]))
c6.pack(side=LEFT)

b1 = Button(frame2, text="Delete", command=Delete)
b1.pack(side=RIGHT)

b2 = Button(frame2, text="Check", command=Check)
b2.pack(side=RIGHT)


frame2.pack(side=BOTTOM)


for i in range(4):
  Solution.append(Colors[random.randint(0,5)])
print(Solution)

mainloop()
