# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
from readUrl import ReadUrlHelp
import modelhelp
import sqliteHelp

sqlite=sqliteHelp.sqliteHelp()
sqlite.creatTable()

url="http://www.zimuzu.tv/resourcelist"
help=ReadUrlHelp(url)
introductions=help.get_urlData()
num=help.get_PageNum()
urlt=help.get_urlByPageNum(1)
print(num)
crNum=1
#解析到17页
'''
for introduction in introductions:
    print(introduction.url)
    print(introduction.name)
    print(introduction.countries)
    print(introduction.Iid)
    print(introduction.resources)
    sql="insert into Introduction values ('%s','%s','%s','%s','%s','%s')"%(introduction.name,introduction.countries,introduction.season,introduction.url,introduction.Iid,introduction.resources)
    sqlite.sqliteExecute(sql)
'''



while crNum<num:
    try:
        read=ReadUrlHelp(help.get_urlByPageNum(crNum))
        data=read.get_urlData()
        for item in data:
            print(item.name)
            sql="insert into Introduction values ('%s','%s','%s','%s','%s','%s')"%(item.name.replace("'",""),item.countries,item.season,item.url,item.Iid,item.resources)
            sqlite.sqliteExecute(sql)
        print("当前页码%s"%crNum)
    except ValueError as e:
        print(e)
    finally:
        crNum=crNum+1
