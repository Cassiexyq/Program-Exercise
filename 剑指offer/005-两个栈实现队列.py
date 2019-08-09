# -*- coding: utf-8 -*-

# @Author: xyq
# 一个栈用来弹出，pop弹出stack2,stack为空，pop出stack1存储在stack2
# 栈2用来存储栈1弹出的数，栈2要为空
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)

