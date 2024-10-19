# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:27:27 2024

@author: Administrator
"""

import random
class NhanVien:
    def __init__(self, ma_nv, ho_ten, loai, luongcb, songay, sosp):
        """
        Khởi tạo một đối tượng NhanVien với mã nhân viên, họ tên và lương cơ bản.
        Loại: 
            - "bh" : Nhân viên bán hàng
            - "vp" : Nhân viên văn phòng
        """
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.loai = loai
        self.luongcb = luongcb
        self.songay= songay
        self.sosp= sosp
        self.tinhluonght()
        
    def xuat_thong_tin(self):
        """
        Trả về chuỗi mô tả thông tin nhân viên.
        """
        return f"Mã NV: {self.ma_nv}, Họ tên: {self.ho_ten}, Lương cơ bản: {self.luongcb}, Hằng tháng: {self.luonght}"
    
    def tinhluonght(self):
        """
        Tính lương hàng tháng cho nhân viên.
        """
        if self.loai=="bh":
            self.luonght=self.luongcb + self.sosp*18000
        else:
            self.luonght=self.luongcb + self.songay*150000
            
class QuanLyNhanVien:
    def __init__(self):
        """
        Khởi tạo danh sách nhân viên.
        """
        self.danh_sach_nv = []
        
    def khoi_tao_ngau_nhien(self, so_nv):
        """
        Khởi tạo ngẫu nhiên các nhân viên.
        """
        self.danh_sach_nv.append(NhanVien("NV1001", "Tran Van D", "vp", 9000, 10, 0))
        for _ in range(so_nv):
            ma_nv = ''.join(["NV" , str(random.randint(1, 1000))])
            ho_ten = random.choice(['Nguyen Van E', 'Nguyen Thi F', 'Tran Van G'])
            luongcb = random.randint(1000,10000)
            loai= random.choice(["bh","vp"])
            if loai == "bh":
                sosp = random.randint(1,50)
                self.danh_sach_nv.append(NhanVien(ma_nv, ho_ten,loai, luongcb, 0, sosp))
            if loai=="vp":
                songay = random.randint(1,31)
                self.danh_sach_nv.append(NhanVien(ma_nv, ho_ten,loai, luongcb, songay, 0))
                
    def xuat_thong_tin_nv(self):
        """
        Xuất thông tin tất cả nhân viên.
        """
        for nv in self.danh_sach_nv:
            print(nv.xuat_thong_tin())
            
    def cap_nhat_luong(self):
        """
        Cập nhật lương hàng tháng cho tất cả nhân viên.
        """
        for nv in self.danh_sach_nv:
            nv.tinhluonght()
            
    def tim_nv_theo_ma(self, ma_nv):
        """
        Tìm nhân viên theo mã nhân viên.
        """
        for nv in self.danh_sach_nv:
            if nv.ma_nv == ma_nv:
                print(nv.xuat_thong_tin())
                return nv
        print("Không tìm thấy nhân viên với mã:", ma_nv)
        
    def xuat_nv_luonght_max(self):
        """
        Xuất thông tin nhân viên có lương hàng tháng cao nhất.
        """
        nv_max_luong = max(self.danh_sach_nv, key=lambda nv: nv.luonght)
        print(nv_max_luong.xuat_thong_tin())
        
    def xuat_nv_luonght_min(self):
        """
        Xuất thông tin nhân viên có lương hàng tháng thấp nhất.
        """
        nv_min_luong = min(self.danh_sach_nv, key=lambda nv: nv.luonght)
        print(nv_min_luong.xuat_thong_tin())
        
       
quan_ly_nv = QuanLyNhanVien()

quan_ly_nv.khoi_tao_ngau_nhien(10)

quan_ly_nv.xuat_thong_tin_nv()
 
quan_ly_nv.cap_nhat_luong()

print("\nNhân viên có mã NV1001:")
quan_ly_nv.tim_nv_theo_ma("NV1001")

print("\nNhân viên có lương hàng tháng cao nhất:")
quan_ly_nv.xuat_nv_luonght_max()

print("\nNhân viên có lương hàng tháng thấp nhất:")
quan_ly_nv.xuat_nv_luonght_min()






    