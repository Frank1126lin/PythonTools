#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : file_rename_by_num.py
# @Author: Frank1126lin
# @Date  : 2020/8/24


import os

path = "../data/EL-XUHAN"

i = 0
for f in os.listdir(path):
    print(f)
    f_type = os.path.splitext(f)[-1]
    print(f_type)
    i += 1
    new_name = ''.join(["0" for _ in range(6-len(str(i)))]) + str(i) + f_type
    os.rename(os.path.join(path, f), os.path.join(path, new_name))