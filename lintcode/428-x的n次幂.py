# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    # 递归
    def myPow(self, x, n):
        # write your code here
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        return self.myPow(x*x, n//2) if not n & 1 else x * self.myPow(x*x, n//2)

    # 迭代  我们让i初始化为n，然后看i是否是2的倍数，是的话x乘以自己，否则res乘以x，
    # i每次循环缩小一半，直到为0停止循环。最后看n的正负，如果为负，返回其倒数
    def myPow2(self,x,n):
        res = 1.0
        tmp = x
        i = n
        while i:
            if i & 1: res *= tmp
            tmp *= tmp
            i = i//2
        return res if n > 0 else 1/res

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.1,3))
    print(s.myPow2(2.1,3))