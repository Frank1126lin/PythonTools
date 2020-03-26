#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : get_size.py
# @Author: Frank1126lin
# @Date  : 2020/2/22

import os


def get_size(path):
    if path is '':
        return [0, 'B']
    if os.path.isfile(path):
        return get_file_size(path)
    if os.path.isdir(path):
        return get_dir_size(path)


def get_file_size(filepath):
    size = os.path.getsize(filepath)
    return size_handle(size)

def get_dir_size(dirpath):
    size = 0
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size_handle(size)



def size_handle(size):
    unit_list = [
        (60, 'EB'),
        (50, 'PB'),
        (40, 'TB'),
        (30, 'GB'),
        (20, 'MB'),
        (10, 'KB'),
        (1, 'B'),
    ]
    if size == 0:
        return [0, 'B']
    for i in range(len(unit_list)):
        if size >> unit_list[i][0] > 0:
            return [round(size / 2 ** unit_list[i][0], 2), unit_list[i][1]]



if __name__ == '__main__':
    size = get_size('')
    print(size)