# -*- coding: utf-8 -*-

# @Author: xyq
# 一个长度为n的所有数字都在0-n-1范围内，某些数字有重复，找出重复的数字
# 把每个数字放入对应下标的位置，是的num[i] = i,如果已经有满足这个条件，但仍然想放进去的元素必然是重复的
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # 时间复杂度O（N） 空间复杂度O（1）
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                j = numbers[i]
                numbers[i], numbers[j] = numbers[j], numbers[i]
        return False

dup = [1]
print(Solution().duplicate([2,3,1,0,2,5,3],dup))
print(dup)