# -*- coding: utf-8 -*-

# @Author: xyq


def main():
    N = int(input())
    time = []
    for _ in range(N):

        time.append(list(map(int, input().split())))
    time.sort(reverse=True)
    x = int(input())
    A,B = list(map(int, input().split()))
    if B < x:
        B = 60 + B - x
        A = A - 1
    else:
        B = B - x
    for i in range(len(time)):
        if time[i][0] > A or (time[i][0] == A and time[i][1] > B):
            continue
        else:
            ans = [str(j) for j in time[i]]
            print(" ".join(ans))
            return

if __name__ == "__main__":
    main()

