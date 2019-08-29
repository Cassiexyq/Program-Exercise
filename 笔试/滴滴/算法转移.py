# -*- coding: utf-8 -*-

# @Author: xyq

def getOP(start,end):
    for i in range(start, end):
        for j in range(start, end-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                digits[j],digits[j+1] = digits[j+1],digits[j]



n = int(input())
arr = list(input().strip().split())
op = ['+']
digits = []

for i in range(len(arr)):
    if i & 1:
        op.append(arr[i])
    else:
        digits.append(int(arr[i]))
i = 0

# while i < len(op):
#     k = i
#     while op[i] == '+' or op[i] == '-':
#         i += 1
#     if k != i:
#         getOP(k,i)
#     k = i
#     while op[i] == '*' or op[i] == '/':
#         i += 1
#     if k != i:
#         getOP(k,i)
#
res = []
for i in range(len(digits)):
    res.append(op[i])
    res.append(str(digits[i]))
if res[0] == '+':
    res.pop(0)
print(' '.join(res))



