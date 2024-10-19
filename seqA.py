# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:35:28 2024

@author: Administrator
"""

#seqA/60
import random
def tao_seqA():
    n = random.randint(30,80)
    seqA = []
    for i in range (n+1) :
        if random.randint(0,1) == 0:
            seqA.append(round(random.uniform(-79,39),2))
        else:
            seqA.append(random.randint(-79,39))
    return seqA
    
    
# Viết hàm kiểm tra dữ liệu từng phần tử    
def kiemtra_dulieu(seqA):
    return [type(i).__name__ for i in seqA]

# thống kê số lượng phần tử có trong seqA
def thongke(seqA):
    return len(seqA)

#sắp xếp dãy seqA thành dãy seqB tăng dần, dãy giảm thì reverse True
def sapxep_seqB(seqA):
    return sorted(seqA)
    
#tính trung bình các phần tử trong seqA
def tinhtrungbinh(seqA):
    return sum(seqA)/len(seqA)

# viết hàm tính giá trị trung bình giữa 2 phần tử nằm trong dãy seqB khi N chẵn.
# Khi N lẻ, thì hàm tính trả về giá trị nằm giữa
def trungbinh_seqB(seqB):
    n = len(seqB)
    if n % 2 == 0 :
        return (seqB[n//2 - 1] + seqB[n//2])/2
    else:
        return seqB[n//2]

# khoảng cách max, min seqA hoặc seqB
def khoangcach(seq):
    return max(seq) - min(seq)
    
#so sánh kết quả hàm tb seqA và trung bình seqB
def sosanh(seqA, seqB):
    return  tinhtrungbinh(seqA), trungbinh_seqB(seqB),  tinhtrungbinh(seqA) == trungbinh_seqB(seqB)
    
    
    
if __name__=="__main__" :
    seqA = tao_seqA()
    print(seqA)
    print(kiemtra_dulieu(seqA))
    print(thongke(seqA))
    seqB = sapxep_seqB(seqA)
    print(seqB)
    print(tinhtrungbinh(seqA))
    print(trungbinh_seqB(seqB))
    print(khoangcach(seqA))
    print(khoangcach(seqB))
    print(sosanh(seqA,seqB))
    
    
    
    