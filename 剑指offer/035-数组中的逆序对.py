# -*- coding: utf-8 -*-

# @Author: xyq
# 归并排序计算逆序对，在合并排序中，如果left > right，要计算逆序对，
# 即对当前right[j]一共有的逆序对个数是 len(left)-i，
# 也就是当前left 的i指针后面那些都要比这个right[j]来的大
class Solution:
    def __init__(self):
        self.cn = None
        self.data = None

    def InversePairs(self,data):
        self.data = data
        self.cn = 0
        if self.data != None:
            self.mergeSort()
        print(self.data)
        return self.cn % 1000000007

    def mergeSort(self):
        i = 1
        while i < len(self.data):
            low = 0
            while low < len(self.data):
                mid = low + i
                height = min(low + 2 * i, len(self.data))
                if mid < height:
                    self.merge(low, mid, height)
                low += 2 * i
            i *= 2

    def merge(self, low, mid, height):
        left = self.data[low:mid]
        right = self.data[mid:height]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                self.cn += len(left)-i   # 左边的 指针到最后所有的都满足
                j += 1

        result += left[i:]
        result += right[j:]
        self.data[low:height] = result

# acc = [5,4,2,3]
acc = [364,637,341,406,747,995,234,971,571,219,993
    ,407,416,366,315,301,601,650,418,355,460,505,360,
       965,516,648,727,667,465,849,455,181,486,149,588,
       233,144,174,557,67,746,550,474,162,268,142,463,221,
       882,576,604,739,288,569,256,936,275,401,497,82,935,
       983,583,523,697,478,147,795,380,973,958,115,773,870,
       259,655,446,863,735,784,3,671,433,630,425,930,64,266,
       235,187,284,665,874,80,45,848,38,811,267,575]
print(Solution().InversePairs(acc))

