# -*- coding: utf-8 -*-

# @Author: xyq
# O(n)时间内找到超过一半的数，可以每次取出两个不一样的数，剩下的如果有cnt>0的那个数就一定是超过一半的
def find(arr):
    size = len(arr)
    ans = 0
    cnt = 0
    for i in range(size):
        if cnt == 0:
            ans = arr[i]
            cnt = 1
        else:
            if arr[i] == ans:
                cnt += 1
            else:
                cnt -= 1
    return ans

