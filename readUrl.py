# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
import modelhelp
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


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
        introductions=set()
        if clist==None:
            return
        for element in clist:
            cont=etree.tostring(element,pretty_print=True)
            content=etree.HTML(cont)
            name=content.xpath("//a/text()")#获取名称
            tit=content.xpath("//font[@class='f4']/text()")#获取说明
            url=content.xpath("//a/@href")#获取连接
            if tit!=None and url!=None and len(tit)>0 and len(url)>0:
                #print("%s-%s 地址 %s" % (name,tit[0], ("http://www.zimuzu.tv%s"%(url[0]))))
                detailsUrl=("http://www.zimuzu.tv%s"%(url[0]))
                #reUrl=self.get_resourcesUrl(detailsUrl)
                #print(detailsUrl)
                reUrl=self.get_cont(detailsUrl)
                introduction=modelhelp.Introduction(name=name[0],season=tit[0],url=detailsUrl,resources=reUrl)
                introductions.add(introduction)
        return introductions

    
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
    
    def get_resourcesUrl(self,detailsUrl):
        req=urllib.request.Request(url=detailsUrl,headers=ReadUrlHelp.webheaders)
        respone=urllib.request.urlopen(req)
        html=respone.read().decode("utf-8")
        content=etree.HTML(html)
        resUrl=content.xpath("//h3/a/strong/text()")
        #//*[@id="resource-box"]/div/div/h3/a
        print(detailsUrl)
        print(resUrl)
        return resUrl

    def get_cont(self,url):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
            )
        driver = webdriver.PhantomJS(executable_path=r'phantomjs.exe',desired_capabilities=dcap)
        driver.get(url)
        #html=driver.find_element_by_xpath("//h3/a")
        #html=driver.find_element_by_id("resource-box")
        #stt=str(driver.page_source)
        #urlt=html.get_attribute("hreff")
        #print(stt)
        #print(driver.find_element_by_xpath("//h3/a/strong/text()"))
        #cont=etree.tostring(stt,pretty_print=True)
        driver.save_screenshot("test.html")
        #lxml_html=etree.HTML(stt)
        #url=lxml_html.xpath("//h3/a/strong")
        driver.quit()
        driver.close()
        print(url)
        return ""
    
    def parse_from_unicode(unicode_str):
        utf8_parser = lxml.etree.HTMLParser(encoding='utf-8')
        s = unicode_str.encode('utf-8')
        return lxml.etree.fromstring(s, parser=utf8_parser)
