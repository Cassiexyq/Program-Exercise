# -*- coding: utf-8 -*-

# @Author: xyq
import operator
def check(T,arr):
    s1 = T
    s2 = list(reversed(arr))
    flag = False
    rev = []
    for i in range(len(s2)):
        if i == 0 and not flag:
            continue
        rev.append(s2[i])
        flag = True
    j = 0
    temp = T
    while j < 100:
        temp = temp.extend(rev)
        if operator.eq(arr,temp):
            return "YES"
    return "NO"

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        yx = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(check(yx,arr))


