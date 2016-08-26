#!/usr/bin/python
#coding:utf-8
#5-1
print '#5-1'
import math as foobar
print foobar.sqrt(4)

#5-2
print '#5-2'
x,y,z = 1,2,3
print x,y,z
x,y = y,x#交换操作
print x,y,z

scoundrel = {'na	me':'Robin','girlfriend':'Marion'}
key,value = scoundrel.popitem()
print key
print value

x=y=z=4#链式赋值
print x,y,z

x+=1
print x

#5-3
print '#5-3'
#5-4
print '#5-4'

print bool('I think')
print bool(42)

#name = raw_input('What is your name?:')
#if name.endswith('Gru'):
#	print 'Hello Gru'
#else:
#	print 'Hello stranger'

#num = input('Enter a number:')
#if num > 0:
#	print 'The number is positive'
#elif num < 0:
#	print 'The number is negative'
#else:
#	print 'The number is zero'

x = y = [1,2,3]
z = [1,2,3]
print x is y
print x is z#此处为false是因为x和z是指向两个内容相同的不同对象