# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
from readUrl import ReadUrlHelp

url="http://www.zimuzu.tv/resourcelist"
help=ReadUrlHelp(url)
help.get_urlData()
num=help.get_PageNum()
urlt=help.get_urlByPageNum(1)
print(num)
crNum=1
#1 168 286 341
while crNum<num:
    try:
        read=ReadUrlHelp(help.get_urlByPageNum(crNum))
        read.get_urlData()
        print("当前页码%s"%crNum)
    except ValueError as e:
        print(e)
    finally:
        crNum=crNum+1