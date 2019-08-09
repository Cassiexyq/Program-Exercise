# -*- coding: utf-8 -*-

# @Author: xyq

def binary_search1(arr,target):
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j-i) // 2
        if arr[mid] < target:
            i = mid + 1
        else: j = mid
    # return i if arr[i] == target else -1
    return i

def binary_search2(arr, target):
    i,j = 0,len(arr)-1
    while i < j:
        mid = i + (j-i+1) // 2
        if arr[mid] <= target:
            i = mid
        else:
            j = mid-1
    return i

def check(dis, point):
    if dis[0] > point[-1] or dis[1] < point[0]:
        return 0
    if dis[0] <= point[0] and dis[1] >= point[-1]:
        return len(point)
    first = binary_search1(point,dis[0])
    last = binary_search2(point, dis[1])
    return last-first+1


def main():
    case = int(input())
    res = []
    for i in range(case):
        n,m = list(map(int,input().split()))
        point = list(map(int, input().split()))
        point.sort()
        dis = []
        for _ in range(m):
            dis.append(list(map(int, input().split())))
        temp = []
        for j in dis:
            temp.append(check(j, point))
        res.append(temp)
    for i in range(case):
        print("Case #{}:".format(i+1))
        for j in range(len(res[i])):
            print(res[i][j])


if __name__ == '__main__':
    main()

