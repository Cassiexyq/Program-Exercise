# -*- coding: utf-8 -*-

# @Author: xyq

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


print(Solution().duplicate([2,3,1,0,2,5,3],[1]))