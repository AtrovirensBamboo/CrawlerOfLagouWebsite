# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:02:17 2018

@author: 89288
"""

import pymongo

class DataArrange():
    
    def __init__(self):
        '''
        连接数据库
        client:mongodb对象
        database:数据库对象
        '''
        self.client = pymongo.MongoClient('localhost',27017)
        self.database = self.client.lagou
        
    def save_job_content(self,dic_job):
        '''
        将爬取到的职位信息存入数据库
        dic_job：职位信息的字典形式
        '''
        collection_job = self.database.job_content
        collection_job.insert(dic_job)
        
    def save_got_url(self,dic_url):
        '''
        将已爬取的url存入数据库
        url:已爬取的url
        '''
        collection_got_urls = self.database.got_urls
        collection_got_urls.insert(dic_url)
