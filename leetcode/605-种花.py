# -*- coding: utf-8 -*-

# @Author: xyq
# 尽量多插花， 把0变1，1旁边相邻只能0
# 前后元素连续两个0
# 中间连续3个0
def solver(flowerbed,n):
    i = 0
    cnt = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            if i == 0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                cnt += 1
                flowerbed[0] = 1
            elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                cnt += 1
                flowerbed[-1] = 1
            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                cnt += 1
                flowerbed[i] = 1
        i += 1
    # return True if n <= cnt else False
    return cnt
res = solver([1,0,0,0,0,1],2)
print(res)
