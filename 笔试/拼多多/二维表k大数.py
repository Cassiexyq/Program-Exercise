# -*- coding: utf-8 -*-

# @Author: xyq
def binary_search(arr,target):
    if not arr:
        return 0
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j-i) // 2
        if arr[mid] <= target:
            i = mid + 1
        else: j = mid
    # return i if arr[i] == target else -1
    if arr[i] >= target:
        return i
    else:
        return i + 1

# def solution2(n,m,k):
#     for i in range()
def solution(n,m,k):
    i, j = n - 1, m - 1
    res = []

    if i == n - 1:  # 最后一排从右到左，每个往上遍历

        while j >= 0:
            s, t = i, j
            while s >= 0 and t < m:
                ans = (s + 1) * (t + 1)
                idx = binary_search(res,ans)
                res.insert(idx,ans)
                s -= 1
                t += 1

            j -= 1
            if len(res) >= k:
                return res
    j = 0
    while i >= 0:
        s, t = i, j
        while s >= 0 and t < m:
            ans = (s + 1) * (t + 1)
            idx = binary_search(res, ans)
            res.insert(idx, ans)
            s -= 1
            t += 1

        i -= 1
        if len(res) >= k:
            return res

n,m,k = list(map(int, input().strip().split()))

# print(res)
res = solution(n, m, k)
print(res[-k])






