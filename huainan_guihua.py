#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : huainan_guihua.py
# @Author: Frank1126lin
# @Date  : 2019/8/27

import re
import json
import requests
# 1/定义baseurl 及headers
baseurl = "http://ghgs.huainan.gov.cn/"
# print(baseurl+"site/tpl/15866800?t=1")

headers ={
    "Referer": "http://ghgs.huainan.gov.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}
# 2/返回主页html字符串
response = requests.get(url=baseurl+"site/tpl/15866800?t=1", headers=headers)
html = response.content.decode("utf-8")

# 3/使用正则表达式获取所有url
def url_list(html):
    '''

    :param html: html字符串
    :return: 所有需要的url列表
    '''
    pattern = re.compile(' <p class="p1"><a href="(.*?)" target="_blank">', re.S)
    items = re.findall(pattern, html)
    url_list = []
    for item in items:
        url_list.append(baseurl+item)
    return url_list

# 4/针对每一个url，获取页面对应的string:url 字典
def parse_one(url):
    '''
    :param url:每一页的url
    :return: 字符串
    '''
    url_rep = requests.get(url=url, headers=headers)
    url_html = url_rep.content.decode("utf-8")
    url_pat = re.compile('.*<a href="(.*?)" target="_blank">(.*?)</a>', re.S)
    items = re.findall(url_pat, url_html)
    for item in items:
        yield {
            item[1]:item[0],
        }

def write_to_json(content, file_name):
    '''
    写为json格式文件
    :param content: 写入的内容
    :param file_name: 文件名，str, 如result.txt
    :return:
    '''
    with open(file_name,'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False,)+'\n')


if __name__ == '__main__':
    urlLi = url_list(html)
    for i in urlLi:
        for j in parse_one(i):
            write_to_json(j,'huainan.txt')
