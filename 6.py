#!/usr/bin/python
#coding:utf-8
#6-1
print '#6-1'

fibs = [0,1]#斐波那契数列
for i in range(10):
	fibs.append(fibs[-2]+fibs[-1])
print fibs

#6-2
print '#6-2'
#6-3
print '#6-3'

import math
x = 1
y = math.sqrt
print callable(x)#判断函数是否可以调用
print callable(y)

def hello(name):
	return 'Hello ' + name + '!'
print hello('zhangbo')

def fibs(num):
	result = [0,1]
	for i in range(num):
		result.append(result[-2]+result[-1])
	return result
print fibs(10)

def square(x):
	'Calculates the square of the number x.'
	return x*x
print square(4)
print square.__doc__#打印文档字符串
#print help(square)#内建的help函数

def change(n):
	n[0] = 'Mr.Gumby'
names = ['Mrs.Entity','Mrs.Thing']
change(names)
print names
names = ['Mrs.Entity','Mrs.Thing']
change(names[:])
print names

def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}
storage = {}
init(storage)
print storage

def lookup(data, label, name):
	return data[label].get(name)
print lookup(storage, 'middle', 'Lie')

def store(data, full_name):
	names = full_name.split()
	if len(names) == 2:names.insert(1,'')
	labels = 'first','middle','last'
	for label, name in zip(labels, names):
		people = lookup(data,label,name)
		if people:
			people.append(full_name)
		else:
			data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames,'Magnus Lie Hetland')
print lookup(MyNames,'middle','Lie')

store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print lookup(MyNames, 'first', 'Robin')
store(MyNames, 'Mr. Gumby')
print lookup(MyNames, 'middle', '')

def hello_1(greeting, name):
	print '%s %s!' % (greeting, name)
hello_1(greeting='Hello', name='world')#关键字参数，使传入参数变得清晰

def print_params(*params):#收集参数返回的是元组
	print params
print_params('Testing')
print_params(1,2,3,4,5,6)

def print_params_3(**params):
	print params
print_params_3(x=1,y=2,z=3)#返回了一个字典

def store_1(data, *full_names):
	for full_name in full_names:
		names = full_name.split()
		if len(names) == 2:
			names.insert(1,'')
		labels = 'first','middle','last'
		for label,name in zip(labels, names):
			people = lookup(data,label,name)
			if people:
				people.append(full_name)
			else:
				data[label][name] = [full_name]

d = {}
init(d)
store_1(d,'Han Solo','Luke Skywalker','Anakin Skywalker')
print lookup(d,'last','Skywalker')

def add(x,y):
	return x+y
params = (1,2)
print add(*params)#单星号传递元组，双星号传递字典


def story(**kwds):
	return 'Once upon a time, there was a '\
		'%(job)s called %(name)s.' % kwds

def power(x,y,*others):
	if others:
		print 'Received redundant parameters:',others
	return pow(x,y)

def interval(start,stop=None,step=1):
	'Imitates range() for step > 0'
	if stop is None:
		start,stop = 0,start
	result = []
	i = start
	while i < stop:
		result.append(i)
		i += step
	return result

print story(job='king',name='Gumby')
print story(job='Sir Robin',name='brave knight')
params = {'job':'language','name':'Python'}
print story(**params)
del params['job']
print story(job='stroke of genius',**params)
print power(2,3)
print power(x=3,y=2)
params = (5,)*2
print power(*params)
print power(3,3,'Hello world!')
print interval(10)
print interval(1,5)
print interval(3,12,4)
print power(*interval(3,7))

x = 1
scope = vars()
print scope['x']
scope['x'] += 1
print x

x = 1
def change_global():
	global x#global来引用全局变量
	x = x + 1
change_global()
print x

def multiplier(factor):
	def multiplyByFactor(number):
		return number*factor
	return multiplyByFactor

double = multiplier(2)
print double(5)

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

print factorial(5)

def search(sequence,number,lower=0,upper=None):
	if upper is None:
		upper = len(sequence) - 1
	if lower == upper:
		assert number == sequence[upper]
		return upper
	else:
		middle = (lower + upper) // 2
		if number > sequence[middle]:
			return search(sequence, number, middle+1, upper)
		else:
			return search(sequence, number, lower, middle)

seq = [34,67,8,123,4,100,95]
seq.sort()
print search(seq,34)