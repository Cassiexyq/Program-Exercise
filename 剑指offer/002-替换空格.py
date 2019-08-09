# -*- coding: utf-8 -*-

# @Author: xyq
# 先找到多少个空格，再开辟数组填充
# 注意空格，判断空格就要空一下
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s_len = len(s)
        space_count = s.count(' ')
        s_len += 2 * space_count
        j = 0
        new_array = [''] * s_len
        for i in range(len(s)):
            if s[i] == ' ':
                new_array[j] = '%'
                new_array[j+1] = '2'
                new_array[j+2] = '0'
                j += 3
            else:
                new_array[j] = s[i]
                j += 1
        return ''.join(new_array)


s = Solution()
res = s.replaceSpace("We Are Happy")
print(res)