#-*- coding:utf-8 -*-
from Tkinter import *
import xml.etree.cElementTree as ET
from login import whosLog,win

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

mainWin = Tk()
lstBox = Listbox(mainWin)
# 这里是ListBox的填充内容
listcont = getDateFromxml(whosLog)  # 这里传入从login里面获得的用户名
lenFriend = len(getDateFromxml(whosLog)) +1

for i in range(1,lenFriend):
  lstBox.insert(i,listcont[i-1][0]+"\t"+listcont[i-1][1])
lstBox.pack()

ed = EditButtons(mainWin)
print "whosLog: "+ whosLog + '\n'

mainWin.title('Main')
mainWin.geometry('200x300')

mainWin.mainloop()
