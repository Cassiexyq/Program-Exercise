# -*- coding: utf-8 -*-

# @Author: xyq

# 排序 + 计算顺差（下一张牌和上一张牌差的值是多少）
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

