# -*- coding: utf-8 -*-

# @Author: xyq


class Solution:
    def NumberOf1Between1AndN_Solution2(self, n):
        return ''.join(map(str,range(n+1))).count('1')

    # 对于每个位置来说，把10进制数分成两个部分，比如说
    # 当m = 100
    # 的时候， 把十进制数
    # n = 3141592
    # 分成
    # a = 31415
    # 和
    # b = 92 ，以此来分析百位数为1时所有数的个数和。m = 100
    # 时，百位数的前缀为3141，当百位数大于1时，为3142 * 100，因为当百位数大于1时，前缀可以为0，
    # 即百位数可以从100到199，共100个数；当百位数不大于1时，为3141 * 100；如何判断百位数是否大于1？假设百位数为x，若（x + 8） / 10
    # 等于1，则大于1，若（x + 8） / 10
    # 等于0，则小于1。因此前缀可用（n / m + 8） / 10 * m来计算
    # (若计算2的个数，可以改为（n / m + 7） / 10 * m, 若计算3的个数，改为（n / m + 6） / 10 * m，…以此类推)。

    def NumberOf1Between1AndN_Solution(self, n):
        m = 1
        cnt = 0
        while m <= n:
            a = int(n / m)
            b = n % m
            cnt += int((a+8) /10) * m + (a % 10 == 1) * (b+1)
            m *= 10
        return cnt

print(Solution().NumberOf1Between1AndN_Solution(34123))