# -*- coding: utf-8 -*-

# @Author: xyq

import sys
for line in sys.stdin:
    a,b = [int(x) for x in line.split()]
    print(a+b)

