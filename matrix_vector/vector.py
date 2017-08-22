#!/usr/bin/env python
#-*-coding:utf-8-*-
import numpy as np
print "使用ndarray来表示向量 : "
a = np.array([-1,2])
b = np.array([3,1])
print a+b
print "---------------"
print a-b


print "标量乘法"
print a*3

#向量的点积跟向量的夹角的余弦有关
print "向量的点积"
print a.dot(b)       # 另一种写法 np.dot(a,b)

#获取向量投影长度的小例子  http://hahack.com/math/math-vector/

def get_projection(a,b):
    return a.dot(b)*1.0*b/b.dot(b)


a = np.array([1,2])
b = np.array([2,2])
print get_projection(a,b)



print "矩阵外积（叉积）:"
a = np.array([3,5,2])
b = np.array([1,4,7])
print np.cross(a,b)


print "向量的转置"
print a.T
