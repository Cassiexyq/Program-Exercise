# -*- coding: utf-8 -*-

"""
@Time    : 2019/3/3 10:20
@Author  : Cassie
@Description :
"""

import itertools
'''
 无限迭代器
 count()、cycle()、repeat()
count(firstval=0, step=1):创建一个从 firstval (默认值为 0) 开始，以 step (默认值为 1) 为步长的的无限整数迭代器
cycle(iterable):对 iterable 中的元素反复执行循环，返回迭代器
repeat(object [,times]:反复生成 object，如果给定 times，则重复次数为 times，否则为无限
'''
num = itertools.count()  # 默认0开始，步长为1
for i in num:
    if i > 9:
        break
    else:
        print(i)
for i in itertools.count(10,2):
    if i > 20:
        break
    else:
        print(i)
i = 1
for string in itertools.cycle([1,2,3]):
    if i == 5:
        break
    else:
        print(string)
        i += 1

'''
有限迭代器
chain():连接
compress(data, selector):根据selector选择留下的数据
dropwhile(predicate, iterable):predicate 是函数，iterable 是可迭代对象。
         对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项
takewhile(predicate, iterable):predicate 是函数，iterable 是可迭代对象。
        对于 iterable 中的元素，如果 predicate(item) 为 true，则保留该元素，只要 predicate(item) 为 false，则立即停止迭代。
groupby(iterable[, keyfunc]):对序列进行分组,针对连续型
ifilter(function or None, sequence):把满足条件的组成一个迭代器返回，python2
izip(iter1, iter2, ..., iterN)：用于将多个可迭代对象对应位置的元素作为一个元组，将所有元组『组成』一个迭代器，并返回 python2
islice(iterable, [start,] stop [, step]):iterable 是可迭代对象，start 是开始索引，stop 是结束索引，step 是步长，start 和 step 可选


'''
print(list(itertools.chain([1,2],['a','c','d'],[3,4])))  # [1, 2, 'a', 'c', 'd', 3, 4]
print(list(itertools.compress(('ABCDE'),[1,1,0,1,1])))   # compress()选择要保留的数 ['A', 'B', 'D', 'E']
print(list(itertools.dropwhile(lambda x: x > 2, [3,4,5,1,3])))  # 遇到第一个不满足为false就返回后续所有项 [1, 3]
print(list(itertools.takewhile(lambda x:x > 2, [3,4,5,1,3])))  # [3, 4, 5] 遇到不满足就停止
for key, item in itertools.groupby('aavvbbddd'):  # 默认对连续相同项进行分组
    print(key, list(item))
for key, item in itertools.groupby([1,5,2,3,5,5,3],lambda x: x>3):
    print(key, list(item))
# print(list(itertools.ifilter(lambda x:x>5),range(10))) python3 没有这个
print(list(filter(lambda x:x>5, range(10))))  # python3提供内置的filter [6, 7, 8, 9]
print(list(zip([1,2,3],['a','b'])))  # [(1, 'a'), (2, 'b')] 直到有一个迭代完了就终止
print(list(itertools.zip_longest([1,2,3],['a','b'],fillvalue='-'))) # [(1, 'a'), (2, 'b'), (3, '-')] 所有迭代终止，自定义一个填充值
print(list(itertools.islice([1,2,3,4,5],3,7,2)))  # 4 结束索引出界没有报错
print(list(itertools.islice(itertools.count(), 6)))  # [0, 1, 2, 3, 4, 5]
print(list(map(pow, [1,2,3],[2,2,2])))  # [1, 4, 9]
a,b,c = itertools.tee(['abc'],3)
print(list(a),list(b),list(c))  #  ['abc'] ['abc'] ['abc'] 跟repeat一样的作用
for i in itertools.repeat(['abc'],3):
    print(list(i))

'''
组合生成器
product(iter1, iter2, ... iterN, [repeat=1])：用于求多个可迭代对象的笛卡尔积，它跟嵌套的 for 循环等价
permutations(iterable[, r]):r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度
combinations(iterable, r):用于求序列的组合
'''
print(list(itertools.product(['A','B'],['C','D'])))  # [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D')]
print(list(itertools.product([1,2,3],repeat=2)))
print(list(itertools.permutations([1,2,3,4],3))) # 生成几位数的全排列不重复
print(list(itertools.combinations([1,2,3,4],3))) # 生成几位数的按顺序的组合不重复
print(list(itertools.combinations_with_replacement([1,2,3],3)))