#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : get_type.py
# @Author: Frank1126lin
# @Date  : 2/23/20


import os

def get_type(path):
    '''
    给定文件地址path,返回文件类型
    :param path: 文件地址
    :return: 文件类型
    '''
    if os.path.isdir(path):
        return 'Dir'
    else:
        return os.path.splitext(path)[-1][1:]

if __name__ == '__main__':
    print(get_type('./get_size.py'))
    print(type(get_type('./get_size.py')))