# -*- coding: utf-8 -*-

# @Author: xyq
# 异或运算，把array的所有都逐个做异或运算，那么所有相同的出现过两次的数字都会抵消，
# 最后只剩下那两个不一样数字的异或结果，既然两个是不一样的数字，
# 异或结果的1个数必然大于1，先找到最左边那个1的位置，然后遍历array，分两个数组，把index为1的分一起，
# 为0的放一起，这样就把这两个不一样的分开了，然后再对每个数组做异或，异或结果就是不一样的那个数字。
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