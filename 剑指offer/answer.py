# -*- coding: utf-8 -*-

# @Author: xyq

import re
def replaceSpace(s):
    return re.sub('\s','%20',s)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def FindKthToTail(head, k):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    if k > len(res) or k < 1: return 0
    return res[-k]
def ReverseList(pHead):
    q = pHead.next
    p = pHead
    p.next = None
    while(q):
        r = q.next
        q.next = p
        p = q
        q = r
def Merge(pHead1, pHead2):
    i = pHead1
    j = pHead2
    pre = None
    while i or j:
        while i.val < j.val:
            pre = i
            i = i.next
        temp = j
        temp.next = i
        j = j.next
        pre.next = temp
    if j:
        i.next = j
    return pHead1

def printListFromTailToHead(listNode):
    stack = []

    if listNode is None: return []
    stack.append(listNode.val)
    listNode = listNode.next
    while listNode != None:
        stack.append(listNode.val)
        listNode = listNode.next
    return list(reversed(stack))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def reConstructBinaryTree(pre, tin):
    if not pre or not tin: return
    root = TreeNode(pre.pop(0))
    index = tin.index(root.val)
    print(root.val)
    root.left = reConstructBinaryTree(pre,tin[:index])
    root.right = reConstructBinaryTree(pre,tin[index+1:])
    return root
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

def minNumberInRoateArray(array):
    low = 0
    high = len(array)-1
    if len(array) == 0: return 0
    if len(array) == 1: return array[0]
    while low < high:
        mid = low + int((high-low)/2)
        # print(mid)
        if array[mid] > array[high]: low = mid+1
        elif array[mid] < array[high]: high = mid
        else: high = high-1
    return array[low]
def Fibonacci(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    res = 0
    n1 = 1
    n2 = 1
    for num in range(2,n):
        res = n1 + n2
        n1 = n2
        n2 = res
    return res
def jumpFloor(number):
    if number == 1: return 1
    if number == 2: return 2
    n1 = 1
    n2 = 2
    res = 0
    for i in range(3,number):
        res = n1 + n2
        n1 = n2
        n2 = res
    return res
def jumpFloor2(number):
    if number < 0: return -1
    if number == 1: return 1
    if number == 2:return 2
    else: return 2* jumpFloor2(number-1)
def rectCover(number):
    if number < 0: return -1
    if number == 1: return 1
    if number == 2: return 2
    n1 = 1
    n2 = 2
    res = 0
    for i in range(3,number+1):
        res = n1+n2
        n1 = n2
        n2 = res
    return res
def NumberOf1(n):
    nbs = bin(n & 0xffffffff)
    return nbs.count('1')

def Power(base, exponent):
    p = abs(exponent)
    res = 1.0
    while p:
        if p & 1: res *= base
        base *= base
        p = p >> 1
    return res if exponent>0 else 1/res
def reOrderArray1(array):
    js = []
    os = []
    for i in array:
        if i %2 ==0:
          os.append(i)
        else: js.append(i)
    return js + os
def reOrderArray(array):
    for i in array:
        if i % 2 == 0:
            array.append(i)
            array.pop(array.index(i))
    return array

def printMatrix(matrix):
     if len(matrix) == 1: return matrix[0]
     if len(matrix[0]) == 1: return [i[0] for i in matrix]
     res = []
     while 1:
        res.extend(matrix.pop(0))
        if len(matrix) ==1 and len(matrix[0]) == 1:
            res.extend(matrix[0])
            return res
        matrix = list(map(list,zip(*matrix)))[::-1]


import numpy as np
matrix = [[1,2],[2,3]]

print(printMatrix(matrix))
# print(len(matrix[0]) * len(matrix))