# -*- coding: utf-8 -*-

# @Author: xyq
# 不能是连续的笔记，笔记最少情况下获得最大赞
# 4 2
# 1 2 3 1
# 4 2 输出最大的赞，笔记个数
# 动态规划

def solution(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(dp[0],dp[1])
    dp2 = [1] * n
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        if dp[i] > dp[i-1]:
            dp2[i] += 1
        else:
            dp2[i] = dp2[i-1]
    return max(dp),dp2[dp.index(max(dp))]
def solution2(nums):
    pre,cur = [0,0],[0,0]
    for i in nums:
        tmp,pre = pre[::],cur[::]
        if tmp[0]+ i > cur[0]:
            cur[0] = tmp[0] + i
            cur[1] = tmp[1] + 1
    print(cur[0],cur[1])
def solution3(nums):
    pre,cur = 0,0
    for i in nums:
        pre,cur = cur, max(pre+i, cur)
    return cur
n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))

