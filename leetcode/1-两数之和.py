# -*- coding: utf-8 -*-

# @Author: xyq
# 求两数之和，用哈希存储所有的值，计算target-这个数得到的值是否在哈希表里
def solution(nums,target):
    hashmap = {}
    for id, num in enumerate(nums):
        hashmap[num] = id
    print(hashmap)
    for i, nm in enumerate(nums):
        j = hashmap.get(target-nm)
        if j is not None and i != j:
            return [i,j]
solution([3,3],6)