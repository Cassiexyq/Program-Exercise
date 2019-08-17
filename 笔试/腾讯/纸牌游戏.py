# -*- coding: utf-8 -*-

# @Author: xyq

def main():
     n = int(input())
     arr = list(map(int, input().split()))
     arr.sort(reverse=True)
     print(sum([v for i,v in enumerate(arr) if not i&1]) - sum([v for i,v in enumerate(arr) if i & 1]))
if __name__ == '__main__':
    main()

