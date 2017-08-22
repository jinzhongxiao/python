#!/usr/bin/env python
#-*-coding:utf-8-*-
import numpy as np
import math
#创建矩阵
a = np.matrix('5 2 7; 1 3 4')
print a
print type(a)

#把matrix转换为bdarray对象
b = a.getA()
print b, type(b)

#把ndarray对象转换为matrix
c = np.asmatrix(b)
print c
print type(c)

#取出某一个值
print a[1,1]   #取出a[2,2]


#矩阵的加法
a = np.matrix('1 0 1;1 2 1;2 1 1')
b = np.matrix('2 1 -1;0 -1 2;2 -1 0')
print '---------------------'
print a+b
#矩阵的减法
print '---------------------'
print a-b
#矩阵的惩罚满足交换律，但不满足结合律
print '---------------------'
print a*b

#单位矩阵
I = np.eye(3)
print '---------------------'
print I


#矩阵的逆的具体求解  http://www.doc88.com/p-086655362651.html

print '---------------------'
print a.I

#矩阵的转置
print '---------------------'
print a.T



T_db=np.matrix('0 0 -1 250;0 -1 0 -150;-1 0 0 200;0 0 0 1')
print T_db
T_de=np.matrix('0 0 -1 300;0 -1 0 100;-1 0 0 120;0 0 0 1')
T_ad=np.matrix('0 0 -1 400;0 -1 0 50;-1 0  0 300;0 0 0 1')
T_bc=np.matrix('0 -1*math.sqrt(2) -1*math.sqrt(2) 30;0 math.sqrt(2) -1*math.sqrt(2) -40;1 0 0 25;0 0 0 1')

T=T_bc.I.dot(T_db.I.dot(T_de))

print T


s = math.sin(0.104)
c = math.cos(0.104)
print s,c
Robotpose = np.matrix('0.8678 -0.4969 2; 0.4969 0.8678 1;0 0 1')

T = np.matrix('0.995 -0.104 1; 0.104 0.995 0;0 0 1')

print Robotpose.dot(T)


#dd= np.matrix('1 0 2;0 1 1;0 0 1')
#print a.dot(dd)
