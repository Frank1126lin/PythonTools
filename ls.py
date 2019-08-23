#! /usr/bin/env python3
# *_* coding: utf-8 *_*
#@File  : ls.py.py
#@Author: Frank1126lin
#@Date  : 6/23/19

'''此文件用来实现Linux ls功能，输入Python ls.py 即可打印所有当前目录的文件名'''
'''打印带有字体颜色的方法'''
# \ 033 [显示方式;字体色;背景色m ...... [\ 033 [0m]

import os
import time
print('\033[1;31m Name \033[0m', '\033[1;32m - \033[0m',"Change Time")
for doc in os.listdir('./'):
    print('\033[0;31m', doc, '\033[0m', '\033[1;32m - \033[0m',time.ctime(os.path.getmtime(doc)))

