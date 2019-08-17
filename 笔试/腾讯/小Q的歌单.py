# -*- coding: utf-8 -*-

# @Author: xyq


# 直接得到所有的可能，每个里面取多少的可能
# 动态规划


def match(k,a,x,b,y):
    res = []
    for i in range(x+1):
        for j in range(y+1):
            if i * a + j * b == k:
                res.append([i,j])
    return res

# 10个里面选2个的做法
def selectfrom(i,sum_all):
    a,b = 1,1 # 分子分母的值
    tmp_i,tmp_j = i,sum_all  # 循环次数就是i
    while tmp_i >= 1:
        a = a*tmp_j
        b = b*tmp_i
        tmp_i = tmp_i-1
        tmp_j = tmp_j-1
    return a // b

def FromNself(k,n):
    if n < k: return 0
    z = 1
    for i in range(n,n-k,-1):
        z *= i
    M = 1
    for i in range(k,0,-1):
        M *= i
    return z//M


k = int(input())
a,x,b,y = [int(i) for i in input().strip().split()]
res = match(k,a,x,b,y)
if not res: print(0)
else:
    result = 0
    for i in res:
        result = result + selectfrom(i[0],x)* selectfrom(i[1],y)
    print(result % 1000000007)