#!/usr/bin/python
#coding:utf-8
from string import Template
#3-1
print '#3-1'

#3-2
print '#3-2'

format = "Hello, %s, %s enough for ya?"
values = ('world','Hot')
print format % values

format = "Pi with three decimals: %.3f"
from math import pi
print format % pi

s = Template('$x, glorious $x!')
print s.substitute(x='slurm')

s = Template("It's ${x}tastic!")#当替换的是一个单词的一部分，使用{}
print s.substitute(x='slurm')

s = Template("Make $$ selling $x!")
print  s.substitute(x='slurm')

s = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print s.substitute(d)

#3-3
print '#3-3'

print '%s plus %s equals %s' % (1,1,2)#使用元组进行格式化，必须要使用圆括号括起来

print '%.*s' % (5,'Guido van Rossum')#可以使用.×的方式来从元组中取得参数

print '%010.2f' % pi#最前面的0表示将剩余的字段宽度使用0填充

print ('%+5d' % 10) + '\n' + ('%+5d' % -10)#使用+时，无论是正数还是负数都会标出符号

#width = input('Please enter width: ')
#price_width = 10
#item_width =width - price_width
#header_format = '%-*s%*s'
#formats = '%-*s%*.2f'

#print '=' * width

#print header_format % (item_width,'Item',price_width,'Price')

#print '-' * width

#print formats % (item_width,'Apples',price_width,0.4)
#print formats % (item_width,'Pears',price_width,0.5)
#print formats % (item_width,'Cantaloupes',price_width,1.92)
#print formats % (item_width,'Dried Apricots(16 oz.)',price_width,8)
#print formats % (item_width,'Prunes(4 lbs)',price_width,12)

#print '-' *width

#3-4
print '#3-4'

subject = 'With a moo-moo here, and a moo-moo there'
print subject.find('moo')#find返回的是第一次出现的位置，没有找到就返回-1

print subject.find('moo',15)#设置起始查询点

seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq)
dir = ' ','usr','bin','env'
print '/'.join(dir)

str = 'AAAAAAAAAbbbbbbbbb'
print str.lower()
print str.title()#将所有单词的首字母大写

print 'This is a test.'.replace('is','eez')

print '1+2+3+4+5'.split('+')

print '                inter                   '.strip()
print '!!!!!!*****inter*******!!!!!'.strip('*!')

from string import maketrans
table = maketrans('cs','kz')
print len(table)
print table[97:123]#maketrans是一个ascii表
print 'This is an incredible test'.translate(table)