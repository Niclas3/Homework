#-*- coding:utf-8 -*-
import xml.etree.cElementTree as ET

user = 'nicals'
path = 'owner[@name=\"'+user+'\"]/name'

def getDateFromxml(user='niclas'):
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

slist = getDateFromxml()
lens = len(getDateFromxml())
for i in range(1,lens):
  print slist[i]
#tree = ET.ElementTree(file='./data.xml')
#for elem in tree.iterfind('owner[@name="niclas"]/name'):
#  print elem.text

