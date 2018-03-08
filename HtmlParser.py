# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:51:47 2018

@author: 89288
"""

from lxml import etree

class HtmlParser():
    
    def parser(self,response):
        '''
        解析网页内容
        yield:返回包括工作信息字典和链接的元组
        '''
        html = etree.HTML(response)
        tags = html.xpath('//ul[@class="item_con_list"]/li')
        
        for tag in tags:
            url = tag.xpath('./div[1]/div[1]/div[1]/a/@href')[0]
            job_name = tag.xpath('./div[1]/div[1]/div[1]/a/h3/text()')[0]     
            wages = tag.xpath('./div[1]/div[1]/div[2]/div[1]/span/text()')[0]
            requirements = tag.xpath('./div[1]/div[1]/div[2]/div[1]/text()')[2].strip()
            list_requirements = requirements.split('/')
            experience = list_requirements[0]
            degree = list_requirements[1]
            company_name = tag.xpath('./div[1]/div[2]/div[1]/a/text()')[0]
            dic_job = {'job_name':job_name,'wages':wages,
                       'experience':experience,'degree':degree,
                       'company_name':company_name}
            
            yield dic_job,url
        

