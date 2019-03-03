### python知识点

* global用法：定义全局变量，使放在函数块中的变量在函数块外也能调用
* chr()和ord()：前者输入一个整数返回ascii符合，后者返回单个字符的ascii或者unicode数值
* hstack()和vstack()的区别: hstack()是把俩个数组水平组合，一行的拼一起；等同于
  <pre><code> concatenate((a,b),axix=1) </pre></code>
  vstack()是把第二个拼在第一个后面，垂直组合，等同于
  <pre><code> concentrate((a,b),axix=0) </pre></code>
  ，要注意这个数组是同维度的，即等行等列
  vstack()和平常两个数组的append()是相同的，如果对两个长度不一样的进行拼接，用np.array()
 
* 排序：sort()和sorted(),sort()是在原位重新排序列表，只应用再list上，sorted()是生成一个新的列表,
 key的效率高于cmp(因为key只调用一次，而cmp调用多次)，能用在所有可迭代对象上
 <pre><code>sorted(arr, key: lambda x: x[1]  # 根据第二个排序 
 sorted(arr, cmp = lambda x,y: cmp(x[1],y[1])) # 根据第二个排序 </pre></code>