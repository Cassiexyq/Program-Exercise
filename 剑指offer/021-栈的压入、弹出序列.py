# -*- coding: utf-8 -*-

# @Author: xyq

# 判断弹出队列是否有效

class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV): return False
        stack = []
        index = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while len(stack) != 0 and stack[-1] == popV[index]:
                stack.pop()
                index += 1

        return True if len(stack) == 0 else False

if __name__ == '__main__':
    pushV = [1,2,3,4,5]
    popV = [4,5,3,2,1]
    print(Solution().IsPopOrder(pushV,popV))