# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) < 5: return False
        numbers.sort()
        zeronum = numbers.count(0)
        for i,v in enumerate(numbers[:-1]):
            if v != 0:
                if numbers[i+1] == v: return False
                zeronum = zeronum - (numbers[i+1] -v) + 1
                if zeronum < 0:
                    return False
        return True

