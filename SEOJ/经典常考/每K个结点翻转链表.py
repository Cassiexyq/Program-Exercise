# -*- coding: utf-8 -*-

# @Author: xyq
# 从头部开始，每k个翻转

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    temp = head
    for i in range(k):
        temp = temp.next
    if temp == None:
        return head
    t2 = temp.next
    temp.next = None
    newHead = reverseList(head) # 当前组逆序
    newtemp = reverseKGroup(t2,k) # 把之后的结点按k逆序
    head.next = newtemp # 把两部分连起来
    return newHead

def reverseList(head):
    if not head or not head.next: return head
    result = reverseList(head.next)
    head.next.next = head
    head.next = None
    return result

nums = input().split()
k = int(input())
s,e = 0,k
ans = [None] * len(nums)
while e <= len(nums):
    ans[s:e] = nums[s:e][::-1]
    s += k
    e += k
ans[s:] = nums[s:]
print(" ".join(ans))
# 从尾部开始，每k个翻转

def solve(head,k):
    head = reverseList(head)
    res = reverseKGroup(head,k)
    res = reverseList(res)
    return res
