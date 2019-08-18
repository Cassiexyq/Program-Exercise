# -*- coding: utf-8 -*-

# @Author: xyq

# 每次从血量中取最大值，然后判断这个最大值要消耗多少次法术
# 假设最大值是pre， 伤害是sh，法力是fali,可以进行ci=min(pre//sh,fali)次攻击
# 然后需要把剩余血量pre-sh*ci 添加到怪兽血槽里，如果中间过程有 ci <0 不合法
# 如果 fali <0  怪兽血槽的和大于了攻击次数ci 也不合法

import heapq
def ismatch(t,fali, sh, h, res): # 回合， 法力， 伤害， 每回合的血量list，血量和
    while h:
        if fali:
            pre = - heapq.heappop(h)
            res -= pre
            if pre > sh:
                ci = min(pre // sh, fali)
                temp = pre - sh * ci  # 剩下的血量
                heapq.heappush(h, (-temp,temp))
                res += temp
                t -= ci
                fali -= ci
            else:
                t -= 1
                fali -= 1
            if t < 0: return False
        else:
            if res > t: return False
            return True
    return True


def solution(n,t,m,h):
    res = sum(h)
    for i in range(len(h)): # 最小堆，每次取最大的值出来
        heapq.heappush(res, (-i,i))
    l,r = 0,-h[0]

    while l < r:
        mid = l + (r-l) //2
        if ismatch(t, m, mid, h, res):
            r = mid
        else:
            l = mid + 1
    return l


n,t,m = list(map(int, input().split()))
h = list(map(int, input().split()))


