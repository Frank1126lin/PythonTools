#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : xml2yolo.py
# @Author: Frank1126lin
# @Date  : 2020/8/14


"""
xml label 2 yolo
"""
import os
import xml.etree.ElementTree as ET



def Parse_file(dir:str, file:str, result:str = "."):
    '''
    file:file path
    result: output path
    '''
    file_path = os.path.join(dir, file)
    if not os.path.exists(dir):
        return "dir doesn't exists!"
    if os.path.isfile(file_path):
        typ = file.split(".")[-1]
        if typ == "xml":
            print(f"now dealing xml file: '{file}'...")
            filename = "".join(file.split(".")[:-1])
            inp = open(file_path)
            res = open(f"{result}/{filename}.txt", 'w')
            t = ET.parse(inp)
            root = t.getroot()
            size = root.find("size")
            imgw = int(size.find('width').text)
            imgh = int(size.find('height').text)


            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                if int(difficult) == 1:
                    continue
                if cls not in clss :
                    clss.append(cls)
                cls_id = clss.index(cls)
                bbox = obj.find('bndbox')
                xyxy = (float(bbox.find('xmin').text), float(bbox.find('ymin').text), float(bbox.find('xmax').text), float(bbox.find('ymax').text))
                x = (xyxy[0]+xyxy[2])/2
                y = (xyxy[1]+xyxy[3])/2
                w = xyxy[2] - xyxy[0]
                h = xyxy[3] - xyxy[1]
                x = x/imgw
                y = y/imgh
                w = w/imgw
                h = h/imgh
                res.write(str(cls_id) + " " + " ".join(str(a) for a in [x,y,w,h]) + "\n")
        else:
            print(f"'{file}' is not a xml file, pass...")
    else:
        print(f"'{file_path}' is not a file, pls chaeck...")


def Parse_dir(input_dir:str, output_dir:str):
    if os.path.isdir(input_dir):
        i = 0
        for f in os.listdir(input_dir):
            print(f)
            i += 1
            Parse_file(input_dir, f, output_dir)

        print(f"all {i} file done.")
    else:
        print(input_dir , "is not a dir...")

if __name__ == '__main__':
    input_dir = "."
    output_dir = "."
    clss = []
    Parse_dir(input_dir, output_dir)


