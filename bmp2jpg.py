#!/usr/bin/env python3
# *_* coding: UTF-8 *_*
# @File  : bmp2jpg.py
# @Author: Frank1126lin
# @Date  : 2020/11/19

import os
from PIL import Image


def bmp2jpg(f):
    # 输入文件全路径f, 保存jpg至当前路径
    if f.endswith(".bmp"):
        basename = os.path.basename(f)
        dirname = os.path.dirname(f)
        newdir = dirname + "jpg"
        if not os.path.exists(newdir):
            os.mkdir(newdir)
        jpg_name = os.path.join(newdir, basename.replace(".bmp", ".jpg"))
        # png_name = os.path.join(newdir, basename.replace(".bmp", ".png"))
        img = Image.open(f)
        img.save(jpg_name, quality = 95) # quality范围1-95，默认75，默认效果较差。
        # img.save(png_name)
        print(f"@文件已保存至{jpg_name}\n")



def main(path):
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            main(new_path)
        elif os.path.isfile(new_path):
            print(new_path)
            bmp2jpg(new_path)

if __name__ == '__main__':
    main(".")
