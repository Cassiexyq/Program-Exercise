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

>  **tuple 和 list的区别**： 可变和不可变，当tuple只有一个元素时，要加一个,
>
> ```python
> >>> listdemo = []
> >>> listdemo.__sizeof__()
> 40
> >>> tupleDemo = ()
> >>> tupleDemo.__sizeof__()
> 24
> ```
>
> 但元组却比列表少占用 16 个字节
>
> 事实上，就是由于列表是动态的，它需要**存储指针**来指向对应的元素（占用 8 个字节）。另外，由于列表中元素可变，所以需要额外**存储已经分配**的长度大小（占用 8 个字节）。但是对于元组，情况就不同了，元组长度大小固定，且存储元素不可变，所以存储空间也是固定的。
>
> 通过对比列表和元组存储方式的差异，我们可以引申出这样的结论，即元组要比列表更加轻量级，所以从总体上来说，元组的性能速度要由于列表。
>
> 元组可以在映射（和集合的成员）中当做“键”使用，而列表不行

(1) 会被认为i是int类型，tuple必须是（1，）**,tuple是不能修改的**



```python
a = (1,2,3)
a*3 #(1,2,3,1,2,3,1,2,3)
```



**trycatch**:   try的语句出现异常才会执行except后的语句，如果正常，则执行完try后执行else。另外，finally语句不管有无异常都会执行。

```
sys.argv是传递给python脚本的命令行参数【字符串】列表
argv[0]为该脚本自身路径，其余为命令行参数
```

Python2 中除法默认向下取整，因此 1/2 = 0，为整型

Python3 中的除法为正常除法，会保留小数位，因此 1/2 = 0.5，为浮点型

\__init\__ 和 \__new\__:前者是初始化方法，当实例对象创建完成后被调用的，然后设置对象属性的一些初始值，

​			后者是在实例创建之前被调用的，构造函数，因为它的任务就是创建实例然后返回该实例，是个静态方法。

**切片**： range(100)表示从0到99共一百个数  a[2-3] = a[-1]

a[-3]和a[2-3]意味着倒数第三个数和倒数第一个数 分别是97 99

a[::3] start0 end99 step3 依次是0 3 6 9一直到99 步长为3

a[2:13]从a[2]到a[12] 不包括13，前闭后开