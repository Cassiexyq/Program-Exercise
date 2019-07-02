**1.	java的静态变量**：

1. 静态对象的数据再全局唯一，类共同拥有
2. 内存空间上是固定的
3. 先分配静态对象的空间

**2. 	JVM**：

![img](https://uploadfiles.nowcoder.com/images/20190606/291053_1559812298987_4E467FB794A7AF7967F62555B4F0B6A6)

**3.	线程池释放资源**：

wait()、join()会释放资源

yield()不会释放锁，只是通知调度器自己可以让出cpu时间片，但只是建议，调度器也不一定采纳

**4.	volatile,synchronized**:

```
volatile能保证数据的可见性，但不能完全保证数据的原子性，synchronized即保证了数据的可见性也保证了原子性
```

