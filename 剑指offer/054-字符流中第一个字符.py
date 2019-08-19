# -*- coding: utf-8 -*-

# @Author: xyq

class Solution:
    # 用哈希满足时间复杂度位O(n)，空间复杂度O(n)
    # 利用ASCII码一共128个字符，直接定义一个128的数组，空间复杂度O(n)，
    # 获取第一个只出现一次的元素需要一个while循环
    # 每次insert的是一个字符，进来一个字符需要判断它是否已经存在过，没有存在记录的是下标
    # 返回对应char
    def __init__(self):
        self.char_list = [-1 for _ in range(128)]
        self.index = 0
    def FirstAppearingOnce(self):
        # write code here
        min_value = 500
        min_idx = -1
        for i in range(128):
            if self.char_list[i] >= 0:
                if self.char_list[i] < min_value:
                    min_value = self.char_list[i]
                    min_idx = i

        if min_idx == -1: return "#"
        return chr(min_idx)

    def Insert(self, char):
        if self.char_list[ord(char)] == -1:  # 没有出现过
            self.char_list[ord(char)] = 1 + self.index   # 存储的下标
        elif self.char_list[ord(char)] > 0:  # 出现过一次
            self.char_list[ord(char)] = -2
        self.index += 1

s = Solution()
s.Insert("G")
s.Insert("O")
s.Insert("O")
s.Insert("l")
s.Insert("e")
print(s.FirstAppearingOnce())