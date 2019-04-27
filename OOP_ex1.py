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


    def add_item(self, item):

        print("Now adding: %s" % item)
        #1. check the furniture area
        if item.area > self.free_area:
            print("The %s is too big to place." % item.name)
            return

        #2. add the furniture into item list
        self.item_list.append(item.name)

        #3. calculate the free area
        self.free_area -= item.area


# 1. create new furniture
bed = HouseItem("床垫", 4)
closet = HouseItem("衣橱", 2)
table = HouseItem("餐桌", 4)
print(bed)
print(closet)
print(table)

# 2. create new house
new_house = House("三室一厅", 110)
new_house.add_item(bed)
new_house.add_item(closet)
new_house.add_item(table)
print(new_house)
