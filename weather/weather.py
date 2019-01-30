# https://stackoverflow.com/questions/25950635/check-if-xml-element-has-children-or-not-in-elementtree
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/47291973/python-create-text-file-write-to-it-replace-string
# http://www.jsondiff.com/
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys
import json
import xml.etree.ElementTree as ET


def main(argv):  # !.py  => (0) -i (1) -o
    input_file_name, output_file_name = argv[0], argv[1]
    root = readXmlFromInputFile(input_file_name)
    strJson = getJsonByPrompt(root)
    createJsonByStr(strJson, output_file_name)


def createJsonByStr(strJson, output_file_name):
    file = open(output_file_name, "w+")
    file.write(strJson)


def readXmlFromInputFile(input_file_name):
    tree = ET.parse(input_file_name)
    root = tree.getroot()
    return root


def getJsonByPrompt(root):
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
                        if(child_ii.text != None):
                            strJson += '"' + str(child_ii.text) + '"'
                        strJson += ','
                else:
                    strJson += '{'
                    for child_ii in child:
                        strJson += '"' + str(child_ii.tag) + '":'
                        if(str(child_ii.attrib) != '{}'):
                            strJson += str(child_ii.attrib).replace("'", '"')
                        if(child_ii.text != None):
                            strJson += '"' + str(child_ii.text)
                        strJson += ','
            strJson = strJson[:len(strJson) - 1]
            strJson += '}, '

    return strJson[:len(strJson) - 2] + '}'


# ignore program (weather.py) and pass to parameter start at index 0
main(sys.argv[1:])
