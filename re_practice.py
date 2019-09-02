#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : re_practice.py
# @Author: Frank1126lin
# @Date  : 2019/8/29


import re
'''正则速记'''
"""
正则表达式
作用：指定一个规则，根据队则对字符串进行筛选
A. 原子：组成正则的基本单位就是原子
    1. 所有可见字符都是原子:abc123#$%^&
    2. 所有不可见字符也都是原子: \n \t \r
    3. 表示所有数字的原子：\d [表示0-9任意一个字符]
    4. 表示所有非数字的原子： \D 【表示除了0-9任意一个字符】
    5. 表示能够当作变量使用的原子： \w 【表示0-9a-zA-Z_任意一个字符】
    6. 表示不能够当作变量使用的原子： \W 【表示除了0-9a-zA-Z_任意一个字符】
    7. 表示不可见字符都是原子： \s 【表示任意一个不可见字符】
    8. 表示可见字符都是原子： \S 【表示任意一个可见字符】
    
B. 原则：正则表达式至少包含一个原子
C. 元字符： 用于修饰原子的符号
    1. [] :原子列表：自定义原子范围 【表示列表中任意一个字符】 [0123456789]=\d
    2. [^] :排除列表：自定义原子范围 【表示列表外任意一个字符】 [^0123456789]
    3. + :1个或以上的指定原子
    4. * :0个或以上的指定原子
    5. ? :0个或1个指定原子
    6. {m,n} :指定原子数量最少m个，最多n个
    7. {m,}或{,n} :指定原子数量最少m个或最多n个
    8. {m} :指定原子数量必须m个
    9. ^ :限制内容必须在整个字符串的开头位置
    10. $ :限制内容必须在整个字符串的结束位置
    11. . :表示任意一个字符 除了换行符\n
    12. | :唯一一个逻辑运算符或（万能钥匙）
    13. ? :表示非贪婪模式匹配（正则默认是贪婪模式匹配）
    14. \ :转义字符，用于转义字符串
    15. () :元字符，作用有三
            A:将多个原子作为一个原子处理，方便使用元字符
            B:将（）中的内容暂存于内存，方便后期调用
            C:改变优先级，主要跟|配合
    
    
"""
# 1.[]: 原子列表：自定义原子范围 【表示列表中任意一个字符】 [0123456789] =\d
# txt = '135750+++'
# result = re.findall('[01357]', txt)
# print(result)
# 2. [^] :排除列表：自定义原子范围 【表示列表外任意一个字符】 [^0123456789]
# txt = '13575024680+++'
# result = re.findall('[^01357]', txt)
# print(result)
# 3. + :1个或以上的指定原子
# txt = '135750000246800+++'
# result = re.findall('0+', txt)
# print(result)
# * :0个或以上的指定原子
# txt = '10000200+++'
# result = re.findall('0*', txt)
# print(result)
# 5. ? :0个或1个指定原子
# txt = '10000200+++'
# result = re.findall('0?', txt)
# print(result)
# 6. {m,n} :指定原子数量最少m个，最多n个
# txt = '10000200+++'
# result = re.findall('0{2,5}', txt)
# print(result)
# 7. {m,}或{,n} :指定原子数量最少m个或最多n个
# txt = '10000200+++'
# result = re.findall('0{,3}', txt)
# print(result)
# 8. {m} :指定原子数量必须m个
# txt = '10000200+++'
# result = re.search('0{2}', txt)
# print(result.group())
# 9. ^ :限制内容必须在整个字符串的开头位置
# txt = '0000200+++'
# result = re.findall('^0{2,5}', txt)
# print(result)
# 10. $ :限制内容必须在整个字符串的结束位置
# txt = '1000000'
# result = re.findall('0{2,5}$', txt)
# print(result)
# 11. . :表示任意一个字符 除了换行符\n
# txt = '10000200+++'
# result = re.findall('.+', txt)
# print(result)
# 12. | :唯一一个逻辑运算符或（万能钥匙）
# txt = '200'
# result = re.match('^0$|^[1-9]\d?$|^100$', txt)
# if result:
#     print(result.group())
# else:
#     print("NONE")
# 13. ? :表示非贪婪模式匹配（正则默认是贪婪模式匹配）

# str = "<h1>title</h1>"
# pattern = re.compile('<.+?>')
# result = re.findall(pattern=pattern,string=str)
# print(result)

# 14. \ :转义字符，用于转义字符串
# txt = 'Apple Mac is $3999'
# result = re.search('\$\d+', txt)
# print(result.group())

# 15. () :元字符，作用有三
#             A：将多个原子作为一个原子处理，方便使用元字符
# txt = 'Apple mamamamac is $3999'
# result = re.search('(ma){3}', txt)
# print(result.group())
# B: 将（）中的内容暂存于内存，方便后期调用
# txt = 'Apple mamamamac is $3999'
# result = re.search('(ma){3}', txt)
# print(result.groups())
# C: 改变优先级，主要跟 | 配合
# txt = 'Apple'
txt = 'Abble'
result = re.search('A(pp|bb)le', txt)
print(result.group())

'''
函数
'''
# 1. complie函数：
# txt = 'The num is 30.04'
# txt_comp = re.compile(r'''
#     \d+  # 小数点前面的数字
#     \.?  # 小数点本身
#     \d*  # 小数点后面的数字
#     ''', re.VERBOSE)
# result = re.search(txt_comp, txt)
# print(result.group())

