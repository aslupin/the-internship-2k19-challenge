# https://stackoverflow.com/questions/25950635/check-if-xml-element-has-children-or-not-in-elementtree
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/47291973/python-create-text-file-write-to-it-replace-string
# http://www.jsondiff.com/

import json
import xml.etree.ElementTree as ET
tree = ET.parse('./weather.xml')
root = tree.getroot()
# print(len(root), list(root))

strJson = '{'

if(len(root)):
    for child in root:
        strJson += '"' + str(child.tag) + '":'
        if(str(child.attrib) != '{}'):
            strJson += str(child.attrib).replace("'", '"')
        if(len(child)):
            if(str(child.attrib) != '{}'):
                strJson = strJson[:len(strJson) - 1] + ','  # del }
                for child_ii in child:
                    strJson += '"' + str(child_ii.tag) + '":'
                    if(str(child_ii.attrib) != '{}'):
                        strJson += str(child_ii.attrib).replace("'", '"')
                        print(child_ii.tag, child_ii.attrib)
                    if(child_ii.text != None):
                        strJson += '"' + str(child_ii.text) + '"'
                        print(child_ii.text)
                    strJson += ','
            else:
                strJson += '{'
                for child_ii in child:
                    strJson += '"' + str(child_ii.tag) + '":'
                    if(str(child_ii.attrib) != '{}'):
                        strJson += str(child_ii.attrib).replace("'", '"')
                        print(child_ii.tag, child_ii.attrib)
                    if(child_ii.text != None):
                        strJson += '"' + str(child_ii.text)
                        print(child_ii.text)
                    strJson += ','

        else:
            if(child.text != None):
                print(child.text)
        strJson = strJson[:len(strJson) - 1]
        strJson += '}, '

else:
    if(root.text != None):
        print(root.text)
strJson = strJson[:len(strJson) - 2] + '}'


# Writter JSON File
file = open('weather.json', "w+")
file.write(strJson)
