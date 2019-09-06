# -*- coding: utf-8 -*-

# @Author: xyq
from collections import Counter
arr = input().strip()
dic = Counter(arr)
i = 0
temp = arr[0] # 记录每次找的那个值
res = []
start = 0 # 记录第一个位置
while i < len(arr):

    if dic[temp] > 0:
        if arr[i] == temp:
            dic[temp] -= 1
        i += 1
    elif dic[temp] == 0:
        res.append(i-start)
        start = i
        temp = arr[start]
        if dic[temp] > 0:
            if arr[i] == temp:
                dic[temp] -= 1
            i += 1
res.append(len(arr)-start)
print(','.join(map(str, res)))