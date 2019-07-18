## 	C++ - Note

* 面向对象程序，四大特性：封装，抽象，继承，多态

* 头函数

  * #include<iostream>   输入输出
  * #include<string>
  * #include<algorithm>  sort函数

* 数据类型：

  1. 布尔型 bool
  2. 字符型 char
  3. 整型 int
  4. 浮点型 float
  5. 双浮点型 double
  6. 无类型 void
  7. 宽字符型 wchar_t

* 可以使用一个或多个类型修饰： signed  unsigned  short long 

  变量的大小会根据编译器和所使用的电脑而有所不同。

  1. char   1个字节 0-266 / -127 - 128
  2. unsigned char  1个字节 0-255
  3. signed char
  4. int   4个字节
  5. unsigned int
  6. signed int
  7. short int  2个字节
  8. unsigned short int
  9. signed short int
  10. long int  8个字节
  11. signed long int
  12. unsigned long int  8个
  13. float  4个字节
  14. double 8个
  15. long  double  16

* typedef 声名 为一个已有的类型取一个新的名字

  ```C++
  typedef int feet;
  feet distance;
  ```

* 枚举类型

  ```C++
  /**
  变量c的类型为color， 最后c被赋值为blue
  **/
  enum color{red, green,blue} c;
  c = blue;
  enum color{red,green=5, blue};
  /*
  在这里，blue的值为6，每个名称都比前面一个名称大1，red还是为0
  */
  ```

* 局部变量被定义，系统不会 初始化，必须自行初始化，定义全局变量，会自动初始化

* 整数常量：八进制， 十进制，十六进制，可以带前缀后后缀，不带前缀表示十进制，后缀是U L的组合，前者表示无符号整数，后者表示长整数，大小写均可，顺序任意 前缀 0表示八进制  0x 0X表示十六进制

* 浮点常量： 带符号用 e E

* const关键字，声名指定类型的常量

* static 存储类指示编辑器在程序的生命周期内保持局部变量的存在，使用该修饰局部变量乐意在函数调用之间保持局部变量的值。static 修饰符也可以应用于全局变量。当 static 修饰全局变量时，会使变量的作用域限制在声明它的文件内。

* 位运算符

  > p = 60 q=13  0011 1100   0000 1101
  >
  > p&q：12     0000 1100
  >
  > p|q： 61     0011 1101
  >
  > p^q  :  49     0011 0001
  >
  > ~p：-61     1100 0011
  >
  > p << 2： 1111 0000   240
  >
  > p >> 2： 0000 1111  15

* 杂项运算符
  * sizeof  返回变量大小
  * Condition? X: Y  条件运算符
  * 强制运算符
  * & 指针运算符，返回变量地址
  * \* 指针运算符， 指向变量

* 字符串：

  C类型的字符串 char str1[11] = “HELLO”

  ```C
  strcpy(s1,s2);  复制s2到s1
  strcat(s1,s2);  连接字符串s2到s1末尾
  strlen(s1);  返回 s1长度
  strcmp(s1);  如果s1 s2相同，返回0；如果s1<s2，返回小于0；如果s1>s2，，返回大于0
  strchr(s1,ch);  返回指针，指向s1中ch第一次出现的位置
  strstr(s1,s2); 返回指针，指向s1中s2第一次出现的位置
  ```

  ```C++
  #include<string>
  string str1 = "hello";
  string str2;   
  string str3;
  str2 = str1  复制
  str3 = str1 + str2 连接
  str3.size()  长度
  ```

* **引用和指针**
  * 不存在空引用。引用必须连接到一块合法的内存
  * 一旦引用被初始化位一个对象，就不能被指向到另一个地方，指针可以在任何时候指向到另一个对象
  * 引用必须在创建时被初始化，指针可以在任何时间被初始化

* C++ 也存在派生，基类，函数重载（在同一个作用域内，可以声明几个功能类似的同名函数，但是这些同名函数的形式参数（指参数的个数、类型或者顺序）必须不同）--》 一个类同名不同参的一系列函数

* 多态（有了多态，您可以有多个不同的类，都带有同一个名称但具有不同实现的函数）

  **虚函数** 是在基类中使用关键字 **virtual** 声明的函数。在派生类中重新定义基类中定义的虚函数时，会告诉编译器不要静态链接到该函数 -- 》 一个父类，多个子类继承这个父类，且基类的用虚函数virtual修饰的成员函数代表可以在子类中覆盖重写了。

* C++ 动态内存

  * 栈：在函数内部声名的所有变量占用栈内存

  * 堆：程序中未使用的内存，在程序运行时可以动态分配内存

    **malloc()** 函数在 C 语言中就出现了，在 C++ 中仍然存在，但建议尽量不要使用 malloc() 函数。new 与 malloc() 函数相比，其主要的优点是，new 不只是分配了内存，它还创建了对象。

* STL  

  * string类： 
    * 使用 “=”进行赋值，使用“==”进行等值比较，使用“+”串联
    * 用比较运算符，注意比较的字符串不能是null
    * size()返回字符个数，capacity（）返回在重新分配内存之前，string类型对象所能包含的最大字符数
    * reserve()给string对象重新分配内存，默认0
    * getline(cin, str) 字符串输入

  * 序列容器：
    * array <T,N> 长度固定，不能增加或删除
      * #include<array>
      * std::array<double,100> data;
      * std:array<double,10> values {1,2,3,4};
      * values.fill(x) 将所有成员设为定值
    * vector<T,N> 长度可变，用来存放T类型的对象，必要时可以自动站鞥家容量，**但只能在序列的末尾高效增加后删除元素**
      * vector 的索引从 0 幵始，这和标准数组一样。通过使用索引，总是可以访问到现有的元素，但是不能这样生成新元素——需要使用 push_back()、insert()、emplace() 或 emplace_back()。当像这样索引一个 vector 时，和数组容器一样，并没有检查索引值，所以当索引可能越界时，应该通过 at() 函数去使用这个元素。 只能用push_back添加新的元素，可以用索引访问元素 
      * front
      * back
    * deque<T> 双向队列，可以自动增长，两端都能增加删除
      * push_back
      * push_front
    * list<T>链表容器，长度可变，双向链表的形式组织元素，任何地方都可以高效增加或删除，访问速度要比前三种慢。因为必须从第一个元素或最后一个元素访问，沿链表移动
      * 任何位置插入或删除
      * 不能对List排序，自带了一个sort算法
    * forward list<T> 正向链表容器，从第一个元素访问