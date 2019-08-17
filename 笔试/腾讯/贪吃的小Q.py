# -*- coding: utf-8 -*-

# @Author: xyq

# 二分法找第一天能吃到最多巧克力
def eat_sum(s,n):
    total_sum = 0
    for i in range(n):
        total_sum += s
        s = (s+1) // 2
    return total_sum
def main():
    N,M = list(map(int, input().split()))
    if N == 1:
        print(M)
        return
    i,j = 1,M
    while i <= j:
        mid = i + (j-i) //2
        mid_sum = eat_sum(mid,N)
        if mid_sum == M:
            print(mid)
            return
        elif mid_sum < M:
            i = mid + 1
        else:
            j = mid - 1
    print(i-1)

# 循环
def solution():
    import sys
    while True:
        line = sys.stdin.readline().strip().split()
        if not line:
            break
        n,m = int(line[0]),int(line[1])
        if n <= 1:
            print(m)
            continue
        nums = [1] * n
        for i in range(n+1, m+1):
            cnt = 0
            while cnt < n-1:
                if nums[cnt] + 1 <= nums[cnt+1]*2:
                    nums[cnt] += 1
                    break
                cnt += 1
        print(nums[0])
if __name__ == '__main__':
    solution()

