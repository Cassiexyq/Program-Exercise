**python 复数**： 一个实数和虚数组合构成，表示为x+yj

1. 虚数不能单独存在，它们总是和一个值为0.0的实数部分一起构成一个复数
2. 复数由实数和虚数构成
3. 表示虚数的语法 real+imagej
4. 实数和虚数都是浮点数
5. 虚数部分必须由后缀j或J

**numpy.ravel 和 numpy.flattern**

前者返回视图，会影响原始矩阵，后者返回拷贝，对拷贝所作的修改不会影响原始矩阵

都是将多维数组将为一维

**报错**

```python
numbers.sort(key=lambda x, y: cmp(x + y, y + x))
#报错为：TypeError: () missing 1 required positional argument: ‘y’
numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
#报错为：TypeError: ‘cmp’ is an invalid keyword argument for sort()
# 用functools.cmp_to_key()来曲线救国，修改之后的代码：
sorted(numbers, key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
```

****

