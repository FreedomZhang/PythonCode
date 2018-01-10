# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
class ReadUrlHelp(object):
    webheaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'
    }#访问头信息
    pageUrl="http://www.zimuzu.tv"

    def __init__(self,url):
        self.url=url
    #获取链接内容
    def get_urlData(self):
        req=urllib.request.Request(url=self.url,headers=ReadUrlHelp.webheaders)
        respone=urllib.request.urlopen(req)
        #直接读取url respone=urllib.request.urlopen(url)
        html=respone.read().decode("utf-8")
        content=etree.HTML(html)
        clist=content.xpath("//h3[@class='f14']")#获取列表信息
        if clist==None:
            return
        for element in clist:
            cont=etree.tostring(element,pretty_print=True)
            content=etree.HTML(cont)
            name=content.xpath("//a/text()")#获取名称
            tit=content.xpath("//font[@class='f4']/text()")#获取说明
            url=content.xpath("//a/@href")#获取连接
            if tit!=None and url!=None and len(tit)>0 and len(url)>0:
                print("%s-%s 地址 %s" % (name,tit[0], ("http://www.zimuzu.tv%s"%(url[0]))))
    
    #获取最后一页链接
    def get_PageNum(self):
        req=urllib.request.Request(url=self.url,headers=ReadUrlHelp.webheaders)
        respone=urllib.request.urlopen(req)
        html=respone.read().decode("utf-8")
        content=etree.HTML(html)
        lastUrl=content.xpath("//div[@class='pages']/div/a[last()]/@href")#最后一页链接
        lurl=("http://www.zimuzu.tv%s"%(lastUrl[0]))
        num=lurl[(lurl.find('=')+1):lurl.find('&')]#最后一页页码
        return int(num)
        
    def get_urlByPageNum(self,num):
        return("http://www.zimuzu.tv/resourcelist/?page=%s&channel=&area=&category=&year=&tvstation=&sort="%(num))
       
