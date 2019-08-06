# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        product = self.fastPower(a,b, n//2)
        product = (product * product) % b
        if n&1 :
            product = (product* a) % b
        return int(product)

if __name__ == '__main__':
    s = Solution()
    print(s.fastPower(2,3,31))