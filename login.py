# -*- coding: utf-8 -*-
from Tkinter import *
import xml.etree.ElementTree as ET  #使用ElementTree来遍历xml文件方面又快捷O(∩_∩)O哈哈哈~
import tkMessageBox

class Login(): # 设置一个label和Entry的组合
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.Userlabel = Label(frame, text="User")
    self.Userlabel.pack(side=LEFT)

    self.NameEntry = Entry(frame, bd=2)
    self.NameEntry.pack(side=RIGHT)

class PassWord():
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.Passlabel = Label(frame, text="pass")
    self.Passlabel.pack(side=LEFT)

    self.PassEntry= Entry(frame, bd=2, show="*")
    self.PassEntry.pack(side=RIGHT)

class OKBut():
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.butOK = Button(frame, text="OK", width=5, command=getInfo)
    self.butOK.pack(side=LEFT)
    
    self.butCancel = Button(frame, text="Cancel", width=5, command=master.quit)
    self.butCancel.pack(side=LEFT)

def getInfo():    #获得用户名和密码
    name = login.NameEntry.get()
    pwd  = password.PassEntry.get()
    
    print "name: ", name, " password: ",pwd
    findUser(name, pwd)

def printFriend():
    tkMessageBox.showinfo("Some one name...","hello world")

def findUser(name, pwd):
    count = 0    # 遍历完毕xml文件后在确定有无用户
    tree = ET.ElementTree(file='./login.xml') # 文件目录记得更改
    root = tree.getroot()

    for names in tree.iter(tag='name'):
      if names.text == name:
        count+=1
    if count == 0:
      tkMessageBox.showerror("ERROR","请输入正确的用户名")

    for elem in tree.iter(tag='name'):
      if elem.text == name:
        if elem.attrib['password'] == pwd:
          tkMessageBox.showinfo("wellcome.","O(∩_∩)O哈哈~·")
          break
        else:
          tkMessageBox.showerror("Error ","请检查您的密码")
      else:
        continue

win = Tk()
win.title('Login')
win.geometry('200x150')

login = Login(win)         # 输入姓名框
password = PassWord(win)   # 输入密码框
Butt = OKBut(win)          # 确认按钮

win.mainloop()

