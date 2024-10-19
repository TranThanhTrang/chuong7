# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:43:01 2024

@author: Administrator
"""

# sắp xếp các phần tử trong ds tăng dần
# ds=[('tien giang',63),('long an',62),...]

ds=[('tien giang',63),('long an',62),('vinh long',59),('binh duong',60)]
print(sorted(ds, key=lambda x: x[1]))  #sorted không thì theo chữ , còn lambda chạy theo số
 
