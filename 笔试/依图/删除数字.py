# -*- coding: utf-8 -*-

# @Author: xyq

def check(arr):
    res = []
    size = len(arr)
    cn = 0
    for i in range(size-1,-1,-1): # k
        flag = True
        while flag:
            if i >= sum(arr[1:len(arr)-1]) or i >= sum(arr[0:len(arr)]):
                res.append(cn)
                flag = False
            else:
                arr.pop(-1)
                cn += 1
    print(res)
    return reversed(res)


def main():
    T = int(input().strip())
    res = []
    for _ in range(T):
        n = int(input())
        arr = [int(i) for i in input()]
        arr.sort()
        res.append(arr)
    for i in range(T):
        # print("Case #{}:".format(i+1))
        ans = check(res[i])
        # for j in ans:
        #     print(j)


if __name__ == '__main__':
    main()

