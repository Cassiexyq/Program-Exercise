# -*- coding: utf-8 -*-

# @Author: xyq
# 数对问题： x,y 都小于等于n， x/y的余数大于等于k

# 余数大于k，除数一定是从k+1开始的
# 余数从0到y-1循环，对于每个y值，x包含n/y个余数循环，每个余数循环只有y-k个符合
# 剩下一个不完整的循环，判断最大余数是否大于k
if __name__ == '__main__':
    n,k = [int(x) for x in input().split()]
    if k == 0:
        print(n*n)
    else:
        res = 0
        for i in range(k+1, n+1):
            res += (int(n/i)) * (i-k)
            if (n % i) >= k:
                res += n % i -k + 1
        print(res)
