# -*- coding: utf-8 -*-
# @Time : 2022/7/3 22:22
# @Author : ZZZZZHHHHH
# @FileName: 2-6.py
# @Software: PyCharm
colors = ['black','white']
sizes = ['S','M','L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)