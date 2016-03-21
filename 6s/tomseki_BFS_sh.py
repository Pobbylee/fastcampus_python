# coding=utf-8

import os
import re


def getall(momaddress, searchword):

    os.chdir(momaddress)
    thequeue = [os.getcwd()]
    while True:
        if len(thequeue) == 0:
            print ("!!!search complete!!!")
            break
        else:
            frontaddress = thequeue.pop(0)
            if os.path.isdir(frontaddress):
                sons = os.listdir(frontaddress)
                for i in sons:
                    sonsaddress = os.path.join(frontaddress, i)
                    thequeue.append(sonsaddress)
            else:
                iffiledothis(frontaddress, searchword)

def iffiledothis(address, searchword):
    theRegex = re.compile(searchword)
    f1 = theRegex.search(address)
    if f1 is not None:
        print(address)

# Command starts here
print """\
Target the address
Ex) Windows-> C:\\Users\\SH\\Desktop , Mac-> /home/SH"""
target = raw_input("Target : ")

print "What do you want to search?"
keyword = raw_input("Type in the keyword : ")

getall(target, keyword)
