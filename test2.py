#-*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import sys
tree = ET.ElementTree(file='./data.xml')
root = tree.getroot()
#root[0][0].set('foo','bar')   # 修改
owner = 'niclas'
for branch in root:
  print branch.tag, branch.attrib

#a = ET.SubElement(root[0],'name')
#a.text = 'chelsea'
#a.attrib={'email':'missingurchin@gmail.com', 'number':'13914496739'}
#
#tree.write(sys.stdout)
