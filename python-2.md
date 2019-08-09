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

**列表去重**

1. 使用set()

2. 使用常规方法，对每个元素判断在不在里面

3. 使用列表推到去重，把上面那个方法写成了一句

4. 使用sort函数去重

   ```python
   array = [1,3,2,1]
   array.sort(key=array.index)
   # [1,3,2]
   ```

5. 但不能保证元素顺序依旧是原来的，

   ```python
   
   >>> # 方法一:
   >>> data = [2, 1, 3, 4, 1]
   >>> [item for item in data if data.count(item) == 1]
   [2, 3, 4]
   >>> # 方法二:
   >>> data = [2, 1, 3, 4, 1]
   >>> list(filter(lambda x:data.count(x) == 1, data))
   [2, 3, 4]
   ```

**二分查找**

python 列表相当于是一个线性表，在列表中查找元素适用list.index()方法，时间复杂度O(N)

对于大数据量，可以使用二分查找，要求对象必须有序

python中有一个bisect 模块，用于维护有序列表，实现了用于插入元素到有序列表，不需要每次调用sort方式维护有序列表

Bisect模块提供的函数有：

- **bisect.bisect_left(a,x, lo=0, hi=len(a)) :**

查找在有序列表 a 中插入 x 的index。lo 和 hi 用于指定列表的区间，默认是使用整个列表。如果 x 已经存在，在其左边插入。返回值为 index。

- **bisect.bisect_right(a,x, lo=0, hi=len(a))**
- **bisect.bisect(a, x,lo=0, hi=len(a)) ：**

这2个函数和 bisect_left 类似，但如果 x 已经存在，在其右边插入。

- **bisect.insort_left(a,x, lo=0, hi=len(a)) ：**

在有序列表 a 中插入 x。和 a.insert(bisect.bisect_left(a,x, lo, hi), x) 的效果相同。

- **bisect.insort_right(a,x, lo=0, hi=len(a))**
- **bisect.insort(a, x,lo=0, hi=len(a)) :**

和 insort_left 类似，但如果 x 已经存在，在其右边插入。

