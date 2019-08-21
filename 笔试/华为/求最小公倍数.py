# -*- coding: utf-8 -*-

# @Author: xyq

# 最小公倍数 = 两数之积除以最大公约数

def gcd(a,b):
    while b:
        a,b = b, a % b
    return a
while True:
    try:
        a,b = map(int, input().split())
        print(a*b // gcd(a,b))
    except:
        break


