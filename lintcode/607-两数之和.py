# -*- coding: utf-8 -*-

# @Author: xyq

from collections import defaultdict
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.res = defaultdict(int)

    def add(self, number):
        # write your code here
        self.res[number] += 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for i in self.res:
            if (value - i == i and self.res[i] >= 2) or (i != value - i and value-i in self.res.keys()):
                return True
        return False


s = TwoSum()
s.add(2)
s.add(3)
print(s.find(4))
print(s.find(5))
print(s.find(6))
s.add(3)
print(s.find(6))