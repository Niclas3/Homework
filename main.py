#-*- coding:utf-8 -*-
import tkMessageBox

from Tkinter import *
import xml.etree.cElementTree as ET
from login import whosLog

class EditButtons():
  def __init__(self, master):
    fream = Frame(master)
    fream.pack()

    self.AddBut = Button(fream, text='add', width=2, command=Add2xml)
    self.AddBut.pack(side = LEFT)
    self.delBut = Button(fream, text='del', width=2, command=deldata)
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

def getDateFromxml(user):
     tree = ET.ElementTree(file='./data.xml')
     root = tree.getroot()
     owers = list()    #这里存放总的用户姓名
     numbList = list()

     for owerName in tree.iter(tag='owner'):
       nameW = owerName.attrib['name']
       owers.append(nameW)

     if user in owers:
       xpath = 'owner[@name=\"'+user+'\"]/name' #这里是用XPath写的
       for elem in tree.iterfind(xpath):
         #print elem.text,elem.attrib['number']
         numbList.append((elem.text,elem.attrib['number']))
     return numbList

def Add2xml():    #增加操作
    from addGui import AddGui
    def setFriends():   #在这个函数里面写xml
      friendname  = nameEntry.entry.get()
      friendnumb  = numbEntry.entry.get()
      friendemail = emailEntry.entry.get()
    
      tree = ET.ElementTree(file='./data.xml')
      root = tree.getroot()
      owner = whosLog#'niclas'    #这里需要在main.py里面获得
      print owner
      for branch in root:
        if branch.attrib['name'] == owner:
          adder = ET.SubElement(branch,'name')
          adder.text = friendname
          if friendemail!=None and friendnumb!=None: #确保存入的数据不是空数据
            adder.attrib={'email':friendemail,'number':friendnumb}
            tree.write('./data.xml')
            #addNumber2list(lenFriend)
      main.destroy()   #在这里表示确定写入文件之后关闭窗口

    main = Tk()
    main.title('Add friend')
    nameEntry  = AddGui(main, 'name')
    numbEntry  = AddGui(main, 'numb')
    emailEntry = AddGui(main, 'e-mail')
    
    subBut = Button(main, text='Sub', width=12, command = setFriends)
    subBut.pack()

def deldata():    #删除操作
    #tkMessageBox.showinfo("show delete", lstBox.get(lstBox.curselection()))
    print lstBox.get(lstBox.curselection()[0]).split('\t')[1] # 得到电话到xml匹配
    
    #lstBox.delete(lstBox.curselection())  # 这是在列表上显示的时候删除

if whosLog != ' ':  # 判断有无用户登录
  mainWin = Tk()
  # 这里是ListBox的填充内容
  listcont = getDateFromxml(whosLog)  # 这里传入从login里面获得的用户名
  lenFriend = len(getDateFromxml(whosLog)) +1
  
  lstBox = Listbox(mainWin)#, selectmode = MULTIPLE)
  
  for i in range(1,lenFriend):
    lstBox.insert(i,str(listcont[i-1][0])+"\t"+str(listcont[i-1][1]))
  lstBox.pack()
  
  ed = EditButtons(mainWin)
  
  print "whosLog: "+ whosLog + '\n'
  
  mainWin.title('Main')
  mainWin.geometry('200x300')
  
  mainWin.mainloop()
