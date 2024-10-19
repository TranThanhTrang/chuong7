# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:54:23 2024

@author: Administrator
"""

#viết hàm tính căn bậc n từ 1 số thực
def canbac_n(x,n):
    return x**(1/n)

#hàm tính giá trị bình phương của 1 số dương
def binhphuong(n):
    if n>0 :
        return n**2
    return "so khong hop le, nhap lai"

#hàm kiểm tra số chẳn âm
def sochanam(n):
    return n < 0 and n % 2 == 0

#hàm lẻ âm thì trả về -1, chẳn dương trả về 1 ,còn lại trả về 0
def kiemtraso(n):
    if n < 0 and n % 2 == 1:
        return -1
    elif n > 0 and n % 2 == 0:
        return 1
    return 0

#hàm kiểm tra giá trị nhập vào thuộc đoạn [-89,90], sai thì nhập lại
def kiemtragiatri():
    n=input('nhap n:')
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n)
    #if n.lstrip('-').isdigit():
        # n = int(n)
    #if n.strip('-').isdigit():
        # n = int(n)
    if -89 <= n <= 90:
        return n
    print('gia tri khong hop le, nhap lai')
    return kiemtragiatri()
    
    
if __name__=="__main__" :
    print(canbac_n(8,3))
    print(binhphuong(3))
    print(sochanam(-4))
    print(kiemtraso(4))
    print(kiemtragiatri())