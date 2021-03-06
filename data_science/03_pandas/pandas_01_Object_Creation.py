#!/usr/bin/env python
# coding:utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print '-----------------------------------------------------------------------------'
s = pd.Series(range(6))
print s
"""
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int64
"""
print '-----------------------------------------------------------------------------'
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print s
"""
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
"""
print '-----------------------------------------------------------------------------'
dates = pd.date_range('20170101', periods=6)
print dates
"""
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06'],
              dtype='datetime64[ns]',
              freq='D')
"""
print '-----------------------------------------------------------------------------'
print np.random.randn(6, 4)
"""
[[ 0.16975895 -2.86002024  1.53094343 -0.76735229]
 [ 0.11702347  0.81406533  1.24459493 -0.05655453]
 [-0.3323453   0.45445007 -0.47763517  0.69443152]
 [ 2.18823681  0.01304527 -1.17040819 -1.68568489]
 [-0.33934973  1.57573553  0.54338777 -0.16940042]
 [ 0.13558309  1.71812837 -0.01020095 -0.2334118 ]]
"""

df = pd.DataFrame(
    np.random.randn(6, 4),
    index=dates,
    columns=list('ABCD')
)
print df
"""
                   A         B         C         D
2017-01-01 -0.632939  1.727609  2.183583  0.571336
2017-01-02 -1.666080  0.893834  0.350066  0.757557
2017-01-03  0.925475  1.926745  0.008980 -0.990571
2017-01-04  2.129817 -0.054557  0.914877  0.538521
2017-01-05 -0.030076  0.491027 -0.986203  0.005666
2017-01-06 -0.979474  1.168775 -0.207467 -0.189962
"""
print '-----------------------------------------------------------------------------'
df2 = pd.DataFrame(
    {
        'A': 1.,
        'B': pd.Timestamp('20130102'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(["alpha", "bravo", "charlie", "delta"]),
        'F': 'foo'
    }
)
print df2
"""
     A          B    C  D        E    F
0  1.0 2013-01-02  1.0  3    alpha  foo
1  1.0 2013-01-02  1.0  3    bravo  foo
2  1.0 2013-01-02  1.0  3  charlie  foo
3  1.0 2013-01-02  1.0  3    delta  foo
"""
print df2.dtypes
"""
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""
print '-----------------------------------------------------------------------------'
