# -*- coding: utf-8 -*-

# @Author: xyq

def threeSum(nums):
    if len(nums) < 3: return []
    nums = sorted(nums)
    ans = []
    for i in range(len(nums)):
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i-1]: continue
        l,r = i+1, len(nums)-1
        while l < r:
            res = nums[i] + nums[l] + nums[r]
            if res == 0:
                ans.append([nums[i],nums[l],nums[r]])
                while l < r and nums[l] == nums[l+1]:  l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1
                r -= 1
            elif res < 0: l += 1
            else: r -= 1
    return ans

res = threeSum([-1, 0, 1, 2, -1, -4])
print(res)