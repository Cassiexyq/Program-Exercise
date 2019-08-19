# -*- coding: utf-8 -*-

# @Author: xyq

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self,l1,l2):
        prenode = ListNode(0)
        lastNode = prenode
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastNode.next = ListNode(cur)
            lastNode = lastNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next
def printList(l):
    while l:
        print(l.val,end=' ')
        l = l.next
    print('')
def generate(l):
    prenode = ListNode(0)
    lastNode = prenode
    for val in l:
        lastNode.next = ListNode(val)
        lastNode = lastNode.next
    return prenode.next

if __name__ == '__main__':
    l1 = generate([1,5,8])
    l2 = generate([9,1,2,9])
    printList(l1)
    printList(l2)
    s=Solution()
    res = s.addTwoNumbers(l1,l2)
    printList(res)
