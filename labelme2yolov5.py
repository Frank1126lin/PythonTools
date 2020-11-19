#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : labelme2yolov5.py
# @Author: Frank1126lin
# @Date  : 2020/8/3


import os
import json

path = "..\\03-Data\\Battery\\cemian\\label"
class_2_id = []


for file in os.listdir(path):
    if os.path.isdir(os.path.join(path, file)):
        continue
    if not file.endswith(".json"):
        continue
    file_path = os.path.join(path, file)
    file_name = os.path.splitext(file)[0]
    print(file)
    with open(file_path, 'r') as f:
        label_data = json.load(f)
    img_w = label_data["imageWidth"]
    img_h = label_data["imageHeight"]
    for shape in label_data["shapes"]:
        if shape["label"] not in class_2_id:
            class_2_id.append(shape["label"])
        class_id = class_2_id.index(shape["label"])
        x1 = shape["points"][0][0]
        y1 = shape["points"][0][1]
        x2 = shape["points"][1][0]
        y2 = shape["points"][1][1]
        x = (x1 + x2)/2
        y = (y1 + y2)/2
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        yolov5_txt = ' '.join([str(class_id), str(x/img_w), str(y/img_h), str(w/img_w), str(h/img_w), "\n"])
        print(yolov5_txt.strip())
        yolo_label_path = os.path.join(path, file_name + ".txt")
        # print(yolo_label_path)
        # with open(yolo_label_path, "a") as yolov5_file:
        #     yolov5_file.write(yolov5_txt)
        #     print( path , file_name + ".txt", "saved!")
print(class_2_id)
with open(os.path.join(path, "classes.txt"), "w", encoding="utf-8") as l:
    l.write(str(class_2_id))


