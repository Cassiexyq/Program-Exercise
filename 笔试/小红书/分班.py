# -*- coding: utf-8 -*-

# @Author: xyq


def split_class(num):
    a,b = [],[]
    for t1,t2 in num:
        if t1 in a:
            if t2 not in a:
                if t2 not in b:
                    b.append(t2)
            else: return False
        elif t1 in b:
            if t2 not in b:
                if t2 not in a:
                    a.append(t2)
            else: return False
        else:
            if t2 in a: b.append(t1)
            elif t2 in b: a.append(t1)
            else:
                a.append(t1)
                b.append(t2)
    return True


n = int(input())
q = int(input())
res = []
for i in range(q):
    res.append(list(map(int, input().split())))




