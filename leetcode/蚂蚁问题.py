# -*- coding: utf-8 -*-

# @Author: xyq

# 一个L长度的杆子，上面有n只蚂蚁，在上面的位置有数组p，当两只蚂蚁相遇不能交错，只能各自反向爬回去
# 求掉落的最小时间和最长时间，蚂蚁速度都是1

# 求最长时间，就是只要求蚂蚁到杆子端点的最大距离就行

def solve(arr,L,n):
    max_t, min_t = 0,0
    for i in range(len(arr)):
        max_t = max(max_t, max(arr[i],L-arr[i]))
        min_t = max(min_t, min(arr[i], L-arr[i]))
    return min_t, max_t

