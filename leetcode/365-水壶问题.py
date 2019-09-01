# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z: return False
        if x == 0 or y == 0 or z == 0:
            if (x == 0 and y != 0 and y == z) or (x != 0 and y == 0 and x == z) or (z == 0):
                return True
            else:
                return False


        gcd = self.gcd(x,y)
        if z%gcd == 0:
            return True
        else:
            return False

    def gcd(self,x,y):
        while y:
            x,y = y, x % y
        return x

s = Solution()
res = s.canMeasureWater(0,0,0)
print(res)
