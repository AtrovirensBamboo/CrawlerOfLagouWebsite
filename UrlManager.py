# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:01:30 2018

@author: 89288
"""

import pymongo

class UrlManager():
    
    def __init__(self):
        '''
        连接数据库
        got_urls:已爬取的链接
        '''
        self.client = pymongo.MongoClient('localhost',27017)
        self.database = self.client.lagou
        
    def add_got_url(self,url):
        '''
        将已爬取的链接存入数据库
        '''
        collection_got_urls = self.database.got_urls
        collection_got_urls.insert({'url':url})
        
    def judge_got_url(self,url):
        '''
        判断链接是否已爬取
        return:返回布尔值
        '''
        collection_got_urls = self.database.got_urls
        cursor = collection_got_urls.find({'url':url})
        if cursor:
            return True
        else:
            return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

