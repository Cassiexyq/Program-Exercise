# -*- coding: utf-8 -*-

# @Author: xyq

# aac 压缩为 1ac
# xxxxyyyyyyzbbb 压缩为 3x5yz2b

s = input()
res = ''
cnt = 0
for i in range(1,len(s)):
    l = s[i-1]
    if s[i] == l:
        cnt += 1
    elif cnt >= 1:
        res += str(cnt) + l
        cnt = 0
    else:
        res += l
        cnt = 0
if cnt > 0:
    res += str(cnt) + s[-1]
else:
    res += s[-1]
print(res)