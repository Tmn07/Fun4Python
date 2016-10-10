## numpy使用教程

- 不介绍怎么安装了～
- 语法像matlab，但是并不记得matlab怎么写了233
- 以下大部分来自官网https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

### 导入

`import numpy as np`国际惯例

### 创建矩阵

```python
# 手动创数据
a = np.array([[1,2,3,7],[20,30,40,50]], dtype=int)
# arange==range , resharpe将数据转化成x*y(*z)维的
b = np.arange(start,end,step).resharpe(x,y[,z])

np.zeros( (3,4) )
np.ones( (2,3,4), dtype=np.int16 ) 
np.empty( (2,3) )

np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
#  array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])

## 黑科技生成法
>>> def f(x,y):
...     return 10*x+y
...
>>> b = np.fromfunction(f,(5,4),dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
```

### numpy.ndarray基本法

```python
# PERL环境
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.shape[0]
3
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<type 'numpy.ndarray'>
>>> print(a)
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

## 索引，切片，赋值，迭代
>>> a[2]
array([10, 11, 12, 13, 14])
>>> a[1,2]
1
>>> for i in a:
...     print(i)
... 
[0 1 2 3 4]
[5 6 1 8 9]
[10 11 12 13 14]
>>> a.flat
<numpy.flatiter object at 0x2e38fc0>
>>> for i in a.flat:
...     print(i)
... 
0
...
13
14
```

### 矩阵运算

```python
# +,-,**n可以直接使用,*号变成各位相乘
np.sin(A) # np.cos() np.tan() np.exp() np.add(a, b) .... 也可以直接传入 数值或list
# 矩阵乘法！！
A.dot(B) # A*B
np.dot(A,B)


# 注意类型变化..
>>> a = np.ones((2,3), dtype=int)
>>> b = np.random.random((2,3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[ 3.417022  ,  3.72032449,  3.00011437],
       [ 3.30233257,  3.14675589,  3.09233859]])
>>> a += b                  # b is not automatically converted to integer type
Traceback (most recent call last):
  ...
TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
    
## 求和
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)                            # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)                            # min of each row
array([0, 4, 8])
```



