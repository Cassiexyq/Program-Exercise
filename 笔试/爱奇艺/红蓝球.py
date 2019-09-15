# -*- coding: utf-8 -*-

# @Author: xyq
def caluate(a,b):
    ans1 = 1
    ans2 = 1
    while b > 0:
        ans1 *= b
        ans2 *= a
        a -= 1
        b -= 1
    return round(ans2/ans1,6)

m,n = list(map(int, input().split()))
if m == 0:
    print(round(0.0,5))
elif m == 1:
    fm = caluate(m+n,n)
    print(round(1.0/fm,5))
else:
    fm = caluate(m+n-1, m-1) + caluate(m+n-1,m)
    print(fm)
    cishu = (m+n+1)//2
    fz = 0
    for i in range(cishu):
        res = caluate(m+n-1-2*i, m-1)
        print(res)
        fz += res
    print(round(fz/fm,5))

