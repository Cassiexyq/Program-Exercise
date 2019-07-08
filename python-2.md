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

**异或与**

1.与运算：A与B值均为1时，A、B与的运算结果才为1，否则为0 （运算符：&）

2.或运算：A或B值为1时，A、B或的运算结果才为1，否则为0  （运算符：|）

3.异或运算：A与B不同为1时，A、B的预算结果才为1，否则为0  （运算符：^）

4.按位翻转(按位取反)：将内存中表示数字的2进制数取反0取1，1取0 （运算符：~）

1. <<：左移把一个数的bit向左移动一定数目例如：2=0010(2)  2<<2=8（左移2位,1000(2))

2. \> \>：右移 方式与左移相同只是方向相反

a ^b是没有考虑进位的情况下的两数和

(a&b) << 1 就是进位

`a<=``0x7FFFFFFF` 判断是否为正数

若为负数，取反加1  `~(a^``0xFFFFFFFF``)`~n = -(n+1)

就是答案中的 & 0xFFFFFFFF 操作，其中 & 是按位与， 0xFFFFFFFF代表16进制下的边界 （按二进制表示的话，对应4*8=32位）。
由于python长整数类型可以表示无限位，所以需要人为设置边界，避免死循环。