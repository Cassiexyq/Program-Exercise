# -*- coding: utf-8 -*-

# @Author: xyq

def main():
    n,m = list(map(int, input().split()))
    layer = n // (2*m)
    ans = layer * (m**2)
    print(ans)
if __name__ == "__main__":
    main()

