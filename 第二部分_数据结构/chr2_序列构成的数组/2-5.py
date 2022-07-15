# -*- coding: utf-8 -*-
# @Time : 2022/7/3 22:20
# @Author : ZZZZZHHHHH
# @FileName: 2-5.py
# @Software: PyCharm
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
import array

print(array.array('I', [ord(symbol) for symbol in symbols]))