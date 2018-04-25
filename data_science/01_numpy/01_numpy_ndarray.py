#!/usr/bin/env python
# coding:utf-8

"""
numpy 提供了两种基本的对象：
    ndarray（N-dimensional array object）: 存储单一数据类型的多维数组
    ufunc（universal function object）: 能够对数组进行处理的函数
"""

import numpy as np

print '--------------------------------------------------------------------------------'
"""
先创建一个Python序列，然后通过array函数将其转换为数组(这样做显然效率不高)
"""
a = np.array(range(10))
print a
print type(a)
print a.dtype
print a.shape
# [0 1 2 3 4 5 6 7 8 9]
# <type 'numpy.ndarray'>
# int64
# (10,)
print '--------------------------------------------------------------------------------'
"""
先创建一个Python序列，然后通过array函数将其转换为数组(这样做显然效率不高)
"""
aa = np.array([range(10) for n in range(3)])
print aa
print type(aa)
print aa.dtype
print aa.shape
# [[0 1 2 3 4 5 6 7 8 9]
#  [0 1 2 3 4 5 6 7 8 9]
#  [0 1 2 3 4 5 6 7 8 9]]
# <type 'numpy.ndarray'>
# int64
# (3, 10)
print '--------------------------------------------------------------------------------'
"""
可以通过修改数组的shape属性，在保持数组元素个数不变的情况下，改变数组每个轴的长度。
"""
aa.shape = (6, 5)
print aa
# [[0 1 2 3 4]
#  [5 6 7 8 9]
#  [0 1 2 3 4]
#  [5 6 7 8 9]
#  [0 1 2 3 4]
#  [5 6 7 8 9]]
print '--------------------------------------------------------------------------------'
"""
使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变。
但是新数组与原数组其实共享数据存储内存区域，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容。
"""
bb = aa.reshape(2, 15)
print bb
# [[0 1 2 3 4 5 6 7 8 9 0 1 2 3 4]
#  [5 6 7 8 9 0 1 2 3 4 5 6 7 8 9]]

aa[0][0] = 99
print aa[0][0]
print bb[0][0]
# 99
# 99
print '--------------------------------------------------------------------------------'
"""
先创建一个Python序列，然后通过array函数将其转换为数组(这样做显然效率不高);
numpy 提供了很多专门用来创建数组的函数.
"""

print np.arange(
    start=0,
    stop=10,
    step=1
)
print np.linspace(
    start=0,
    stop=99,
    num=10
)
print np.logspace(
    start=0,
    stop=2,
    num=10
)
print '--------------------------------------------------------------------------------'
