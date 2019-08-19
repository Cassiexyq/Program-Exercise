# -*- coding: utf-8 -*-

# @Author: xyq

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