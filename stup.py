# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
from readUrl import ReadUrlHelp
import modelhelp

url="http://www.zimuzu.tv/resourcelist"
help=ReadUrlHelp(url)
introductions=help.get_urlData()
num=help.get_PageNum()
urlt=help.get_urlByPageNum(1)
print(num)
crNum=1
for introduction in introductions:
    print(introduction.name)
    print(introduction.countries)
    print(introduction.Iid)
'''
while crNum<num:
    try:
        read=ReadUrlHelp(help.get_urlByPageNum(crNum))
        read.get_urlData()
        print("当前页码%s"%crNum)
    except ValueError as e:
        print(e)
    finally:
        crNum=crNum+1
'''