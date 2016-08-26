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

x = [1,2,3]
y = [2,4]
print x is not y
del x[2]
y[1] = 1
y.reverse()
print x == y
print x is y

print 'alpha' < 'beta'

print 'INTER'.lower() == 'inteR'.lower()

#number = input('Enter a number between 1 and 10: ')
#if number >= 1 and number <= 10:
#	print 'Great'
#else:
#	print 'Wrong'

age = 10
assert 0 < age < 100
#age = -1
#assert 0 < age <100

x = 1
while x <= 100:
	print x
	x += 1

#name = ''
#while not name.strip():
#	name = raw_input('Please input your name:')
#print 'Your name is %s' % name

print '\n'
words = ['this','is','an','ex','parrot']
for word in words:
	print word

print range(1,10)

d = {'x':1,'y':2,'z':3}
for key,value in d.items():
	print key, value

names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for i in range(len(names)):
	print names[i],'is',ages[i],'years old'

for name ,age in zip(names,ages):
	print name ,'is',age,'years old'

from math import sqrt
for n in range(99,0,-1):
	root = sqrt(n)
	if root == int(root):
		print root
		break

while True:
	word = raw_input('Please enter a word: ')
	if not word:break
	print 'The word is %s' % word
