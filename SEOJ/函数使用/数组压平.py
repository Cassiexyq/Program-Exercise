# -*- coding: utf-8 -*-

"""
@Time    : 2019/5/3 13:58
@Author  : Cassie
@Description :
"""
'''
简单的规则
'''
li = [[1,2],[3,4],[5,6]]
# 第一种
print([j for i in li for j in i])
# 第二种
from itertools import chain
print(list(chain(*li)))
# 第三种
t = []
for i in li:
    t.extend(i)
print(t)
# 第四种
print(sum(li,[]))
'''
复杂点的情况
'''
ll = [1,[2],[[3]],[[4,[5],6]]]

# 第一种
def flat(tree):
    res = []
    for i in tree:
        if isinstance(i,list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
print(flat(li))

# 第二种
def flatten(seq):
    s = str(seq).replace('[','').replace(']','')
    return [eval(x) for x in s.split(',') if x.strip()]
print(flatten(li))

# 第三种
flat = lambda l: sum(map(flat, l),[]) if isinstance(l, list) else [l]
print(flat(li))

# sum函数

print(sum([[5]],[]))  # [5]
print(sum([[5],[8],[[3,4]]],[]))  #[5, 8, [3, 4]]