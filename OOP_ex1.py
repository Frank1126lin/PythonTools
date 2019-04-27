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

bed = HouseItem("床垫", 4)
closet = HouseItem("衣橱", 2)
table = HouseItem("餐桌", 3)
print(bed)
print(closet)
print(table)
