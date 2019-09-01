# -*- coding: utf-8 -*-

# @Author: xyq


from collections import Counter

def distance(dic,k,t):
    ans = 0
    if dic[t] >= k: return ans
    k -= dic[t]
    for i in range(1,10):
        if t + i < 10: # 先往大的找，以最小的代价，就是看替换成的数加1的个数在字典里够不够剩下的k
            if dic[t+i] >= k:
                ans += i * k
                return ans
            else: # 不够的话那先用一部分，剩下继续用别的
                k -= dic[t+i]
                ans += i*dic[t+i]

        if t -i >= 0: # 往小的找
            if dic[t-i] >= k:
                ans += i*k
                return ans
            else:
                k -= dic[t-i]
                ans += i*dic[t-i]

def modify(arr,dic,k,num):
    if dic[num] >= k: return
    k -= dic[num]
    for i in range(1,10):
        if num + i <10:  # 大的变小，从左到右
            for j in range(len(arr)):
                if k == 0: return
                if arr[j] == num+i:
                    arr[j] = num
                    k -= 1
        if num - i >= 0: # 小的变大，从右到左
            for j in range(len(arr)-1,-1,-1):
                if k == 0: return
                if arr[j] == num - i:
                    arr[j] = num
                    k -= 1

if __name__ == '__main__':
    n,k = list(map(int,input().strip().split()))
    arr = list(map(int,input().strip()))
    dic = Counter(arr)
    for i in range(10):
        if i not in dic:
            dic[i] = 0
    cost, num = float('inf'),-1
    for i in range(10): # 遍历0-9，找到最小代价
        tmp = distance(dic,k,i)
        if tmp < cost:
            cost = tmp
            num = i

    modify(arr, dic, k, num)
    print(cost)
    print(''.join(map(str, arr)))



