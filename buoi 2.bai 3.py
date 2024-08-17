# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:36:23 2024

@author: ADMIN
"""

# Giải phương trình bậc hai
a = float(input("Nhập số thực a:"))
b = float(input("Nhập số thưc b:"))
c = float(input("Nhập số thực c:"))
delta = float(b**2-4*a*c)

if delta == 0:
        print("Phương trình có nghiệm kép là:", -b/(2*a))
elif delta > 0:
        print("Phương trình có 2 nghiệm phân biệt là:", (-b + delta**0.5)/(2*a), "và", (-b-delta**0.5)/(2*a))
else:
        print("Phương trình vô nghiệm")
        
              

