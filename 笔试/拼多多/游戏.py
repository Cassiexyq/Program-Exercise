# -*- coding: utf-8 -*-

# @Author: xyq

HP = int(input().strip())
na = int(input().strip())
ba = int(input().strip())

if ba <= 2*na:
    if HP % na == 0:
        print(HP // na)
    else:
        print(HP // na + 1)
else:
    if HP % ba == 0:
        print(2*HP//ba)
    else:
        print(2*HP//ba + 1)



