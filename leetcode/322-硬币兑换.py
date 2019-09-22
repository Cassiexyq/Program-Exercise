# -*- coding: utf-8 -*-

# @Author: xyq
# 找到最少的硬币数量
def changeCoin(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i-j] + 1)
    return -1 if dp[amount] > amount else dp[amount]

print(changeCoin([1,2,5],11))