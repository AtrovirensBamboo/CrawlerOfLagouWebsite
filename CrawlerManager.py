# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:52:14 2018

@author: 89288
"""

import sys
import UrlManager
import HtmlParser
import DataArranger
from selenium import webdriver
import time

sys.path.append(r'C:\Program Files (x86)\Google\Chrome\Application')

class CrawlerManager():
    
    def __init__(self):
        '''
        初始化各类
        '''
        self.UM = UrlManager.UrlManager()
        self.HP = HtmlParser.HtmlParser()
        self.DA = DataArranger.DataArrange()
        self.driver = webdriver.Chrome()
    
    def judge_address(self):
        '''
        选择工作地址
        '''
        ele_address = self.driver.find_element_by_xpath('//a[@class="tab focus"]')
        if ele_address.text == u'深圳站':
            ele_address.click()
        else:
            ele_address = self.driver.find_element_by_xpath('//div[@id="changeCityBox"]/ul/li[6]/a')
            ele_address.click()
    
    def go_search_page(self):
        '''
        进入搜索页面
        '''
        #进入网站
        self.driver.get('https://www.lagou.com/')
        #最大化浏览器
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #选择工作地址
        self.judge_address()
        self.driver.implicitly_wait(5)
        #输入搜索内容
        ele_searchinput = self.driver.find_element_by_id('search_input')
        ele_searchinput.send_keys(u'python爬虫')
        ele_searchbutton = self.driver.find_element_by_id('search_button')
        ele_searchbutton.click()
        self.driver.implicitly_wait(10)

    
    
    def html_crawl(self):
        '''
        爬虫调度器
        '''
        self.go_search_page()
        i = 1
        while i<6:
            self.driver.implicitly_wait(5)
            #将网页拉至底部
            js = 'window.scrollTo(0,document.body.scrollHeight);'
            self.driver.execute_script(js)
            #解析网页内容
            html_text = self.driver.page_source   
            contents_tuple = self.HP.parser(html_text)
            #存储数据
            for content_tuple in contents_tuple:
                self.DA.save_job_content(content_tuple[0])
                self.DA.save_got_url({'url':content_tuple[1]})
        
            button = self.driver.find_element_by_class_name('pager_next')
            button.click()
            
            i+=1
            time.sleep(6)
    
if __name__ == '__main__':
    
    start_crawler = CrawlerManager()
    start_crawler.html_crawl()
    
    

