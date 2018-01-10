# -*- coding: utf-8 -*-
class Introduction(object):

    def __init__(self,name,season,url,resources):
        self.countries=self.get_countrie(name)
        self.name=name
        self.season=season
        self.url=url
        self.Iid=self.get_urlId(url)
        self.resources=resources

    #根据名称获取国别
    def get_countrie(self,name):
        if len(name)>0:
            st=name.find("【")
            ed=name.find("】")
            countrie=name[st+1:ed]
            return countrie
        else:
            return "暂无"
    #获取url后面的资源id
    def get_urlId(self,url):
        if len(url)>0:
            return url.split('/')[-1:][0]