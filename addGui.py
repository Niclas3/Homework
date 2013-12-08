# -*- coding:utf-8 -*-
from Tkinter import *
import xml.etree.ElementTree as ET

class AddGui():
  def __init__(self, master, name):
    fream = Frame(master)
    fream.pack()

    self.namelab = Label(fream, text = name,width=10)
    self.namelab.pack(side = LEFT)
    self.entry = Entry(fream, width=15)
    self.entry.pack(side = RIGHT)

def setFriends():   #在这个函数里面写xml
  friendname  = nameEntry.entry.get()
  friendnumb  = numbEntry.entry.get()
  friendemail = emailEntry.entry.get()

  tree = ET.ElementTree(file='./data.xml')
  root = tree.getroot()
  owner = 'niclas'    #这里需要在main.py里面获得
  for branch in root:
    if branch.attrib['name'] == owner:
      adder = ET.SubElement(branch,'name')
      adder.text = friendname
      adder.attrib={'email':friendemail,'number':friendnumb}
      tree.write('./data.xml')
  main.destroy()   #在这里表示确定写入文件之后关闭窗口

  print friendname, friendnumb, friendemail
if __name__ == '__main__':
  main = Tk()
  main.title('Add friend')
  nameEntry  = AddGui(main, 'name')
  numbEntry  = AddGui(main, 'numb')
  emailEntry = AddGui(main, 'e-mail')
  
  subBut = Button(main, text='Sub', width=12, command = setFriends)
  subBut.pack()
  
  main.mainloop()
