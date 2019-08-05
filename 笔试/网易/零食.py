# -*- coding: utf-8 -*-

# @Author: xyq

def dp(m,n,item_sum):
    if len(m) == 0:
        return 1
    elif n == 0:
        return 1
    elif item_sum < n:
        return 2**len(m)
    else:
        item = m[0]
        if item < n:
            if item_sum-item < n:
                return 2 ** len(m[1:])
            else:
                return dp(m[1:],n-item, item_sum-item) + dp(m[1:],n,item_sum)
        else:
            return 1
def main():
    n,w = list(map(int, input().split()))
    v = list(map(int, input().split()))
    v.sort()
    print(dp(v,w,sum(v)))


if __name__ == "__main__":
    main()

