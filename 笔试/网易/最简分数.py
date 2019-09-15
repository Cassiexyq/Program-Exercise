# -*- coding: utf-8 -*-

# @Author: xyq
def getYZ(a):
    if a == 1:
        return 1
    res = []
    for i in range(1, a):
        x,y = a,i
        while y:
            x,y = y, x%y
        if x == 1:
            res.append(i)
    # print(res)
    return len(res)


n = int(input())
res = [0]*n
for i in range(1,n+1):
    res[i-1] = round(getYZ(i)*1.0/i,6)

print('%.6f' % min(res))


