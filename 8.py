#!/usr/bin/python
#coding:utf-8
#8-1
print '#8-1'
#8-2
print '#8-2'
#raise Exception
#raise Exception('hyperdrive overload')

#8-3
print '#8-3'
try:
	x = input('Enter the first number:')
	y = input('Enter the second number:')
	print x/y
except ZeroDivisionError:
	print "The second number can't be zero."