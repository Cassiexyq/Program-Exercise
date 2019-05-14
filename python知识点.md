### python知识点

* global用法：定义全局变量，使放在函数块中的变量在函数块外也能调用

* chr()和ord()：前者输入一个整数返回ascii符合，后者返回单个字符的ascii或者unicode数值

* hstack()和vstack()的区别: hstack()是把俩个数组水平组合，一行的拼一起；等同于
  <pre><code> concatenate((a,b),axix=1) </pre></code>
  vstack()是把第二个拼在第一个后面，垂直组合，等同于
  <pre><code> concentrate((a,b),axix=0) </pre></code>
  要注意这个数组是同维度的，即等行等列
  vstack()和平常两个数组的append()是相同的，如果对两个长度不一样的进行拼接，用np.array()

* 排序：sort()和sorted(),sort()是在原位重新排序列表，只应用再list上，sorted()是生成一个新的列表,
  key的效率高于cmp(因为key只调用一次，而cmp调用多次)，能用在所有可迭代对象上
  <pre><code>sorted(arr, key: lambda x: x[1]  # 根据第二个排序 
  sorted(arr, cmp = lambda x,y: cmp(x[1],y[1])) # 根据第二个排序 </pre></code>

* itertools模块：[博客](http://www.wklken.me/posts/2013/08/20/python-extra-itertools.html)
  [博客](http://funhacks.net/2017/02/13/itertools/)
  很强大，很高效 [具体参见代码使用](https://github.com/Cassiexyq/Program-Exercise/blob/master/SEOJ/%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8/itertools.py)

* 正则表达式：

  * <code>re.compile(r'正则表达式').findall(src，pos,endpos)</code> 在src中查找是否有符合该正则表达式的字串
  * <code>re.compile(r'正则表达式').match(src，pos,endpos)</code> 用正则去匹配src的开头
  * <code>re.compile(r'正则表达式').fullmatch(src)</code> 用正则去匹配整个src，即默认就是头和尾
  * <code>re.match(re.comile(r'正则表达式')，src)</code>该功能跟上面的一样，不同的是，这个传入的是数组，可以放切片数组，上面的可以传入位置参数
  * <code>re.fullmatch(re.comile(r'正则表达式')，src)</code>该功能跟上面的一样，不同的是，这个传入的是数组，可以放切片数组，上面的可以传入位置参数
  * <code>re.sub(r'正则表达式'，新的, 被替换的)</code>该功能可以去用正则去查找要被替换的，返回被替换的新的字符串
  * ^匹配开头，$匹配结尾，[^]表示里面的范围不包含，*表示对上一个对象可以>=0的个数，？表示对上一个对象0或1，+表示对上一个对象可以>=1
  * 在子表达式中开头描述范围不要用[]，会报错。
  * 匹配中文[\u4e00-\u9fa5]，匹配空格\s，匹配数组\d
  * 对一个字符串某个特点字符的查找，<code>str.find()</code>返回这个字串出现的起始位置

* 替换函数：
  * strip():这不是真正意义上的字符串，可以删除位于首位的字符
  * 对象.replace(rgExp, replceText, max): 前两个都一定要有，max可选，rgExp表示是string对象；replaceText就是一个string对象；max是一个数字，表示对象里面每一个rgExp都替换成replaceText,从左至右最多max次， replace不能用正则
  * re.sub(pattern,repl,string,count,flags):前三个必选，后两个可选，pattern表示正则表达式的模式字符串，repl是被替换的字符串，string是要被处理的原字符串，count是匹配的次数

* reduce(function, iterable[, initializer])函数：对参数序列元素进行累积如<code>reduce(add, [1,2,3,4,5])</code> 

  ​	<code>reduce(lambda x,y: x+y, [1,2,3,4,5])</code>

* eval()函数：<code>x = 7 

   eval('3 * x')  # 21

  eval('pow(2,2)') # 4 

  </code>

* 