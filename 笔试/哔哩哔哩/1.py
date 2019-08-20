# -*- coding: utf-8 -*-

# @Author: xyq
# 字符串编码方式的个数
# 1-a
# 2-b
# ...
# 26 -Z
# 111
# 3

def caluate(s):
    if len(s) == 0 or s[0] == '0':
        return 0
    a,b = 1,1
    n = len(s)
    for i in range(1,n):
        if s[i] == '0': a = 0
        if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
            a = a + b
            b = a - b
        else:
            b = a
    return a

# 这样思考这个问题：
# 用dp[i]来表示i长度下总共有多少种解法，因为满足可以有两种编码，一种是就一个数，但这个数不能为0，，上一个的状态都能能加上这个字母，
# 也就是dp[i] = dp[i-1]
# 一种是2个数拼一起，必须 10- 26区间，这样的话就是上上个状态都能加上这个结果
def calcuate2(s):
    if len(s) == 0 or s[0] == '0':
        return 0
    dp = [0] * (len(s)+1)
    dp[0] = 1
    for i in range(1,len(dp)):  # 这里的len计算的是动态数组的长度
        if s[i-1] != '0': dp[i] += dp[i-1]
        if i > 1 and (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6')):
            dp[i] += dp[i-2]
    return dp[len(s)]
n = str(input())
print(calcuate2(n))


