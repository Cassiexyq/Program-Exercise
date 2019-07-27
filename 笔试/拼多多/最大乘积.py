# -*- coding: utf-8 -*-

# @Author: xyq



# 给定一个无序数组，包含正数、负数和0
# ，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)
def getMax(arr):
    arr = sorted(map(int,arr.split()))
    return max(arr[-1] * arr[-2] * arr[-3], arr[0]* arr[1] * arr[-1])

if __name__ == '__main__':
    size = int(input())
    arr = input()
    print(getMax(arr))