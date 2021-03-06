## 题目描述

### 数据结构类题目

- LinkedList
  - 003-从尾到头打印链表
  - 014-链表中倒数第k个结点
  - 015-反转链表
  - 016-合并两个或k个有序链表
  - 025-复杂链表的复制
  - 036-两个链表的第一个公共结点
  - 055-链表中环的入口结点
  - 056-删除链表中重复的结点
- Tree
  - 004-重建二叉树
  - 017-树的子结构
  - 018-二叉树的镜像
  - 022-从上往下打印二叉树
  - 023-二叉搜索树的后序遍历序列
  - 024-二叉树中和为某一值的路径
  - **026-二叉搜索树与双向链表**
  - 038-二叉树的深度
  - 039-平衡二叉树
  - 057-二叉树的下一个结点
  - 058-对称的二叉树
  - 059-按之字形顺序打印二叉树
  - 060-把二叉树打印成多行
  - 061-序列化二叉树
  - 062-二叉搜索树的第k个结点
- Stack & Queue
  - 005-用两个栈实现队列
  - 020-包含min函数的栈
  - 021-栈的压入、弹出序列
  - 044-翻转单词顺序列(栈)
  - 064-滑动窗口的最大值(双端队列)
- Heap
  - **029-最小的K个数**
- Hash Table
  - 034-第一个只出现一次的字符
- 图
  - 065-矩阵中的路径(BFS)
  - 066-机器人的运动范围(DFS)

### 具体算法类题目

- 斐波那契数列
  - 007-斐波拉契数列
  - 008-跳台阶
  - 009-变态跳台阶
  - 010-矩形覆盖
- 搜索算法
  - 001-二维数组查找
  - 006-旋转数组的最小数字（二分查找）
  - 037-数字在排序数组中出现的次数（二分查找）
- 全排列
  - 027-字符串的排列
- 动态规划
  - 030-连续子数组的最大和
  - 052-正则表达式匹配(我用的暴力)
- 回溯
  - 065-矩阵中的路径(BFS)
  - 066-机器人的运动范围(DFS)
- 排序
  - 035-数组中的逆序对(归并排序)
  - **029-最小的K个数**(堆排序)
  - **029-最小的K个数**(快速排序)
- 位运算
  - 011-二进制中1的个数
  - 012-数值的整数次方
  - 040-数组中只出现一次的数字
- 其他算法
  - 002-替换空格
  - 013-调整数组顺序使奇数位于偶数前面
  - 028-数组中出现次数超过一半的数字
  - 031-整数中1出现的次数（从1到n整数中1出现的次数）
  - 032-把数组排成最小的数
  - 033-丑数
  - 041-和为S的连续正数序列(滑动窗口思想)
  - 042-和为S的两个数字(双指针思想)
  - 043-左旋转字符串(矩阵翻转)
  - 046-孩子们的游戏-圆圈中最后剩下的数(约瑟夫环)
  - 051-构建乘积数组





**1. 	二维数组的查找**

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**思路**：从左下角开始查找，如果target大，往右移，如果target小，往上移。

**2.	用两个栈实现一个队列**

**思路**：push的时候，压入第一个栈，pop的时候，把第一个栈都弹出压入到第二个栈，前提是第二个栈为空，然后pop第二个栈就是队列的pop操作。

**3.	利用二分法查找旋转数组的最小值**

**思路**：需要考虑三种情况 mid = low + (high - low)/2

> (1)array[mid] > array[high]: 
>
>   出现这种情况的array类似[3,4,5,6,0,1,2]，此时最小数字一定在mid的右边。 
>
>   low = mid + 1 
>
>   (2)array[mid] == array[high]: 
>
>   出现这种情况的array类似 [1,0,1,1,1]   或者[1,1,1,0,1]，此时最小数字不好判断在mid左边 
>
>   还是右边,这时只好一个一个试 ， 
>
>   high = high - 1 
>
>   (3)array[mid] < array[high]: 
>
>   出现这种情况的array类似[2,2,3,4,5,6,6],此时最小数字一定就是array[mid]或者在mid的左 
>
>   边。因为右边必然都是递增的。 
>
>   high = mid
>
> **注意的是**：【4，6】遇到这种情况，mid=4，low=4,high=6，按上述来应该high=mid,
>
> 如果high = mid-1就产生了错误

**3.	斐波那契数列**

F(1)=1，F(2)=2, F(n)=F(n-1)+F(n-2)

**4.	青蛙跳台阶**

* 4.1	一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

**思路**：两种跳法，一阶和二阶，假定，跳第一次是一阶，剩下的是n-1个台阶，跳第一次是二阶，剩下n-2个台阶，总跳法f(n-1) + f(n-2)，找规律，斐波那契数列问题

* 4.2	一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

f(1) = 1 

f(2) = f(2-1) + f(2-2)         //f(2-2) 表示2阶一次跳2阶的次数。 

f(3) = f(3-1) + f(3-2) + f(3-3)   ... 

f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(n-(n-1)) + f(n-n)  = 2 * f(n-1)

* 4.3	我们可以用2×1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2×1的小矩形无重叠地覆盖一个2×n的大矩形，总共有多少种方法？

依旧斐波那契数列

**5.	输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。**

对于二进制来说，先减一后取反和先去反后加一结果一样

把一个整数减去1之后再和原来的整数做按位与，得到的结果相当于是把整数的二进制表示中最右边的一个1变成0

在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式

**6.	快速幂**

**技巧**： n&1 等价于 （n%2）==1  n >>1 等价于 n/=2

<pre>
    p = abs(exponent)
        res = 1.0
        while p:
            if p & 1: res *= base
            base *= base
            p = p >> 1
</pre>
**7.	单链表反转**

**思路**：

方法1：利用两个节点指针（p,q）和一个中间节点指针（temp）（用来记录当前节点的下一个节点的位置），分别指向当前节点和前一个节点，每次循环让当前节点的指针域指向前一个节点即可，翻转结束要将最后一个节点的指针域设为空。首先把head和它下一个节点断开，head->next=null，p来记录反转链表的起点，q来记录待翻转的起点

```python
r = q->next # 先要中间记录一下下一个节点
q->next = p # 把翻转点接入翻转链接
p = q # 翻转完的表头
q = r # 带反转的表头
```

方法2：把第二个节点开始后面的3，4，5插入到1的后面，然后再把1查到最后，变成了环，需要断开，设为null，重置head，这个应该至少有3个节点

**8.	顺时针打印数组**

圈数，四个循环，后两个循环条件需要重看

**9.对1-n的所有数的1的计数**

a = n/m    b = n % m

（a+8） / 10 * m + (a % 10 == 1) * ( b+1) 

n = 3141592

| m    | a       | b    | ones                                   |
| ---- | ------- | ---- | -------------------------------------- |
| 1    | 3141592 | 0    | (3141592+8)/10*1+0 = 31460             |
| 10   | 314159  | 0    | (314159+8)/10 * 10 +0 = 31460          |
| 100  | 31415   | 92   | (31415 + 8)/10 * 100+0 =314200         |
| 1000 | 3141    | 592  | (3141 + 8)/10 * 1000+ (592+1) = 314593 |

+8 的用处为了进位，a+8的巧妙之处在于当a的最后一位(当前分析位)为0或1时，加8不产生进位

**10.	找到数组中只出现一次的数字**

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

**思路**：异或运算，把array的所有都逐个做异或运算，那么所有相同的出现过两次的数字都会抵消，最后只剩下那两个不一样数字的异或结果，既然两个是不一样的数字，异或结果的1个数必然大于1，先找到最左边那个1的位置，然后遍历array，分两个数组，把index为1的分一起，为0的放一起，这样就把这两个不一样的分开了，然后再对每个数组做异或，异或结果就是不一样的那个数字。

**11. 链表中环的入口节点**

**思路**：两个指针，慢指针，快指针，如果有环就会在环内相遇，相遇点距离入口点的距离就等于再从开头出发以慢指针速度前进，两个指针相遇的地方就是入口。$$2x = x + kn$$ 

**12. 字符流第一个只出现一次的字符**

**思路**：首先两个函数，一个是每调一次就插一次的insert函数，因为是字符流，不能一下子插进去，然后是对读完字符流后要找的出现一次的字符，可以定义一个128长度的数组，因为ASCII码有128，字符不可能会有不在0-127的范围，所以，每差一次，就把它的与ascii码相同的在数组中找到下标，数组初始都为-1，若是-1，说明是第一次出现，就把记录的当前第几个字符放进下标值里，若，已经不是-1，则说明已经是第二次出现，直接变-2，若-2就不处理。在find函数找这个第一次出现，就遍历整个数组，满足数组值要大于-1，然后找值最小的那个，然后记录这个值的下标，这个下标是ASCII，转字符就是我们要找的那个字符。

**13. 删除链表中重复的结点**

题目： 在一个排序的链表中，存在重复的结点，删除掉重复的结点，不保留重复的

**思路**：首先这是一个排序的链表，当前指针和后继指针，如果val相等，循环直到找到一个不一样的val，但外面还要再包一个循环，可能1122这样，1找到了2但不能退出找不相等的循环，然后才可以赋值，两个指针后移

**14. 二叉树的下一个结点**

题目：按照中序遍历，找到当前点的下一个结点

思路：如果当前点有右子树，则下一个结点是右子树的最左的那个结点；如果没有右子树，找其父节点，如果结点的父节点的左子树是当前结点，则退出遍历父节点的循环，该父节点就是下一个结点，否则循环找到这样的父节点。

**15. 按之字形打印二叉树**

题目：奇数从左到右打印，偶数从右往左打印

思路：层次遍历，两个方法，用一个队列，每层结点Push进队列，输出结点值到res存储结点的数组，也就是，每层一个个pop队列后全部存进临时数组，再一个个pop这个临时数组，push进队列每次pop出来的左右结点，每个的结点值先都存进临时数组，判断奇数层还是偶数层，偶数层就reserved。；

第二种方法，因为reserved的方法耗时，如果遇到数据量大的情况，不好操作，所以可以使用两个堆栈，一个堆栈放奇数层结点，一个堆栈放偶数层结点，先是奇数层有值，pop栈1，每次pop一个，存入偶数层还是先左后右，此时的先pop的是从左到右的顺序，而栈2存入的先左后右，那pop的话就是先右后左，但对每个pop出来的要push进栈1要按从右往左，因为奇数层要从左到右打印，所以push进栈1，先得到的是右边的，push进结点的右子树，再结点的左子树，这就不用reserved了。**结论就是，奇数行pop栈1存，push栈2，栈1栈顶是小的，栈底是大的，因为从小到大打印。栈2栈顶是大的，栈底是小的，因为偶数行打印，从右往左打印。 且栈1由于栈底是大的，先Push右结点，再左结点。 **

**16. 两条相交链表的交点**

思路：访问A链表的指针访问到链表结尾，令他从B头部开始访问链表B，同样，访问B链表的指针访问到链表尾部，从A链头开始访问，这样就能访问到交点

