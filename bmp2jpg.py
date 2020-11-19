#!/usr/bin/env python3
# *_* coding: UTF-8 *_*
# @File  : bmp2jpg.py
# @Author: Frank1126lin
# @Date  : 2020/11/19

import os
from PIL import Image


def bmp2jpg(path, new_path):
    if not os.path.isdir(path):
        print("@请检查是否为文件夹目录！")
        return
    for f in os.listdir(path):
        if not f.endswith(".bmp"):
            continue
        new_name = f.replace(".bmp", ".jpg")
        new_addr = os.path.join(new_path, new_name)
        img = Image.open(os.path.join(path,f))
        img.save(new_addr)
        print(f"@文件已保存至{new_addr}")



if __name__ == '__main__':
    path = "tmp"
    new_path = os.path.join(path, "jpg")
    print(new_path)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    bmp2jpg(path, new_path)