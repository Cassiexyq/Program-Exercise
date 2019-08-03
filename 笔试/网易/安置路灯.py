# -*- coding: utf-8 -*-

# @Author: xyq



if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        road = int(input())
        arr = input().strip()
        ans = 0
        j = 0
        while j < road:
            if arr[j] == 'X':
                j += 1
                continue
            if arr[j] == '.':
                ans += 1
                j += 3
        print(ans)


