# -*- coding: utf-8 -*-

# @Author: xyq

# 给一个数组，把它分成m个子数组，使得m个子数组的最大值在所有划分情况下最小

# 二分法，确定每组的和，可以分几组，来判断这个和的左移还是右移

def solver(nums,m):
    def countgroup(mid):
        temp,cnt = 0,1
        for num in nums:
            temp += num
            if temp > mid:
                cnt += 1
                temp = num
        return cnt

    i,j = max(nums), sum(nums)
    while i < j:
        mid = i + (j-i) // 2
        if countgroup(mid) > m: # 组数太多了。mid太小了
            i = mid + 1
        else:
            j = mid
    return i


print(solver([7,2,5,10,8],2))