#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : get_cdate.py
# @Author: Frank1126lin
# @Date  : 2/23/20

import os
import time

def get_cdate(path):
    '''
    给定文件地址（path),返回文件修改时间date
    :param path: 文件或文件夹地址
    :return: 文件最后一次修改时间
    '''
    return time.ctime(os.path.getmtime(path))

if __name__ == '__main__':
    print(get_cdate('./get_size.py'))
    print(type(get_cdate('./get_size.py')))