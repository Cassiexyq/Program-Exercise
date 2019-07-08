# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array: return []
        tmp = 0
        for i in array: tmp ^= i
        tmp &= - tmp # 得到最后一个为1的位
        a = b = 0
        for i in array:
            if (i & tmp) == 0: a^= i
            else: b^=i
        return [a,b]



acc = Solution().FindNumsAppearOnce([1,2,2,4,3,1])
print(acc)