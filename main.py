#-*- coding:utf-8 -*-
from Tkinter import *
class EditButtons():
  def __init__(self, master):
    fream = Frame(master)
    fream.pack()

    self.AddBut = Button(fream, text='add', width=2)
    self.AddBut.pack(side = LEFT)
    self.delBut = Button(fream, text='del', width=2)
    self.delBut.pack(side = LEFT)
    self.modBut = Button(fream, text='mod', width=3)
    self.modBut.pack(side = LEFT)
    self.seaBut = Button(fream, text='sea', width=2)
    self.seaBut.pack(side = LEFT)

class AddGui():
  def __init__(self, master, name):
    fream = Frame(master)
    fream.pack()

    self.namelab = Label(fream, text = name)
    self.namelab.pack(side = LEFT)
    self.nameEntry = Entry(fream)
    self.nameEntry.pack(side = RIGHT)

mainWin = Tk()

lstBox = Listbox(mainWin)
# 这里是ListBox的填充内容
for i in range(1,9):
  lstBox.insert(i,i*"h")
lstBox.pack()

ed     = EditButtons(mainWin)

#add    = AddGui(mainWin, 'name')
#dele   = AddGui(mainWin, 'delete')
#mod    = AddGui(mainWin, 'mod')
#search = AddGui(mainWin, 'search')

mainWin.title('Main')
mainWin.geometry('200x300')

mainWin.mainloop()
