# -*- coding: utf-8 -*-

# @Author: xyq

#  维护两个左边最大和右边最大，如果有大于这个最大，更新，
#  如果小，高度差加入ans，前提是此前左边小于右边，整个大循环是没有碰到

def getWater(h):
    i,j = 0, len(h)-1
    left_max,right_max = 0,0
    ans = 0
    while i < j:
        if h[i] < h[j]:
            if h[i] >= left_max:
                left_max = h[i]
                print("max: {}".format(left_max))
            else:
                print("ans+= {}".format(left_max-h[i]))
                ans += (left_max - h[i])
            i += 1
        else:
            if h[j] >= right_max:
                right_max = h[j]
                print("right_max: {}".format(right_max))
            else:
                print("right_ans+= {}".format(right_max - h[j]))
                ans += (right_max - h[j])
            j -= 1
    return ans
s = getWater([0,1,0,2,1,0,1,3,2,1,2,1])
print(s)


