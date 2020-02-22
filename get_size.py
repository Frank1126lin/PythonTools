#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : get_size.py
# @Author: Frank1126lin
# @Date  : 2020/2/22

import os


def get_size(path):
    if os.path.isfile(path):
        return get_file_size(path)
    if os.path.isdir(path):
        return get_dir_size(path)


def get_file_size(filepath):
    size = os.path.getsize(filepath)
    return {'file path':filepath, 'file size':size_handle(size)}

def get_dir_size(dirpath):
    size = 0
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return {'dir path': dirpath, 'dir size': size_handle(size)}


def size_handle(size):
    if 0 <= size < 1024:
        return [size, 'B']
    if 1024 <= size < 1024 ** 2:
        ksize = round(size / 1024, 2)
        return [ksize, 'KB']
    if 1024 ** 2 <= size < 1024 ** 3:
        msize = round(size / 1024 ** 2, 2)
        return [msize, 'MB']
    if 1024 ** 3 <= size < 1024 ** 4:
        gsize = round(size / 1024 ** 3, 2)
        return [gsize, 'GB']
    if 1024 ** 4 <= size < 1024 ** 5:
        tsize = round(size / 1024 ** 4, 2)
        return [tsize, 'TB']
    if 1024 ** 5 <= size < 1024 ** 6:
        psize = round(size / 1024 ** 4, 2)
        return [psize, 'PB']

print(get_size(os.getcwd()))
