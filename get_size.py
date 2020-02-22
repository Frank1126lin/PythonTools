#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : get_size.py
# @Author: Frank1126lin
# @Date  : 2020/2/22

import os


def get_file_size(filepath):
    if not os.path.isfile(filepath):
        return {'Msg':'不是文件，请检查！'}
    return os.path.getsize(filepath)

def get_dir_size(dirpath):
    size = 0
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    print(size)
    if 0 <= size < 1024:
        return {'size': [size, 'B']}
    if 1024 <= size < 1024 ** 2:
        ksize = round(size / 1024, 2)
        return {'size': [ksize, 'KB']}
    if 1024 ** 2 <= size < 1024 ** 3:
        msize = round(size / 1024 ** 2, 2)
        return {'size': [msize, 'MB']}
    if 1024 ** 3 <= size < 1024 ** 4:
        gsize = round(size / 1024 ** 3, 2)
        return {'size': [gsize, 'GB']}
    if 1024 ** 4 <= size < 1024 ** 5:
        tsize = round(size / 1024 ** 4, 2)
        return {'size': [tsize, 'TB']}
    if 1024 ** 5 <= size < 1024 ** 6:
        psize = round(size / 1024 ** 4, 2)
        return {'size': [psize, 'PB']}


print(get_dir_size(os.getcwd()))
