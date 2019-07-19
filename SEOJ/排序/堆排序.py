# -*- coding: utf-8 -*-

# @Author: xyq

# 数组 i的叶子节点是 2i  2i+1
# 大顶堆， 升序
def head_adjust(L, start, end):
    temp = L[start]
    i = start
    j = 2*i
    while j <= end:
        if (j < end) and (L[j] < L[j+1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else: break
    L[i] = temp

def heapSort(L):
    size = len(L) - 1 # 数组最后一个数的下标
    fjd = int(size/2) # 最后一个非叶子节点
    for i in range(fjd, 0, -1):  # 从下往上
        head_adjust(L, i, size)
    # for i in range(size-1):  # 把堆顶和最后一个叶子节点交换,要知道最后子节点的位置
    #     L[1],L[size - i] = L[size- i],L[1]
    #     head_adjust(L, 1, size - 1 - i)
    for i in range(1, size):
        L[1], L[size + 1 - i] = L[size + 1 -i],L[1] # 最后一个叶子结点
        head_adjust(L, 1, size - i)  # 调整至叶子节点的前一个

    return [L[i] for i in range(1, len(L))]

if __name__ == "__main__":
    L = [0, 50, 16, 30, 10, 60,  90,  2, 80, 70]
    print(heapSort(L))