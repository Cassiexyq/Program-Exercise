# -*- coding: utf-8 -*-

# @Author: xyq
# 有序字典
# 哈希+双向链表，通过哈希可以做到把一个node插到尾部，更新，哈希存了每个结点
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self,capacity):
        self.capacity = capacity
    def get(self,key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False) # 默认弹出最左边的最先加入的键值对

