#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : OOP_ex1.py
# @Author: Frank
# @Date  : 4/25/2019

class HouseItem:
    """
    双驼峰命名法
    """


    def __init__(self, name, area):
        """
        define init function
        :param name: name
        :param area: area
        """
        self.name = name
        self.area = area

    def __str__(self):
        """
        define str function
        :return: str
        """
        return "%s 占地面积 %d 平方" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        #剩余面积
        self.free_area = area

        #家具名称列表
        self.item_list = []

    def __str__(self):

        # Python 能自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f 平米[剩余面积：%.2f平米]\n家具：%s”"
                 % (self.house_type, self.area, self.free_area, self.item_list))

bed = HouseItem("床垫", 4)
closet = HouseItem("衣橱", 2)
table = HouseItem("餐桌", 3)
New_House = House("三室两厅", 110)
print(bed)
print(closet)
print(table)
print(New_House)
