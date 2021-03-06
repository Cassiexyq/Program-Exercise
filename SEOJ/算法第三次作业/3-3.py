'''
Description
实现Shell排序，对给定的无序数组，按照给定的间隔变化
（间隔大小即同组数字index的差），打印排序结果，
注意不一定是最终排序结果！


Input
输入第一行表示测试用例个数，后面为测试用例，
每一个用例有两行，第一行为给定数组，
第二行为指定间隔，每一个间隔用空格隔开。
1
49 38 65 97 76 13 27 49 55 4
5 3

Output
输出的每一行为一个用例对应的指定排序结果。
13 4 49 38 27 49 55 65 97 76

'''


def f(x: list, gap: int):
    for i in range(gap, len(x)):
        tmp = x[i]
        j = i
        while j >= gap and tmp < x[j - gap]:
            x[j] = x[j - gap]
            j -= gap
        x[j] = tmp


cases = int(input())
for _ in range(cases):
    x = list(map(int, input().strip().split()))
    gaps = list(map(int, input().strip().split()))
    for gap in gaps:
        f(x, gap)
    print(' '.join(list(map(str, x))))
