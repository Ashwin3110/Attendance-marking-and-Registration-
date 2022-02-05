# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 12:58:51 2022

@author: Ashwin D
"""


choice = int(input("1.New Resgistry 2.Attendance :"))
if(choice == 1):
    exec(open('register.py').read())
else:
    exec(open('attendance.py').read())
    
