# -*- coding: utf-8 -*-

# @Author: xyq
from ctypes import *
def Numberofone(n):
    cnt = 0
    while c_int(n).value:
        n = (n-1) & n
        cnt += 1
    return cnt
print(Numberofone(-3))



