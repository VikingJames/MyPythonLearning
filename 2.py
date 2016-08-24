#!/usr/bin/python
#coding:utf-8
#2-1
print "#2-1"
edward = ['Edward Gumby', 42]
print edward
john = ['John Smith', 50]
database = [edward, john]
print database
#2-2
print "#2-2"
greeting = 'Hello'
print greeting[0]
print greeting[-1]#若索引为负数，则反向计数
print 'Hello'[1]
#fourth = raw_input('Year: ')[3]
#print fourth
months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December']
endings = ['st','nd','rd'] + 17*['th'] \
	+ ['st','nd','rd'] + 7*['th'] \
	+ ['st']
#year 	= raw_input('Year:')
#month 	= raw_input('Month(1-12):')
#day 	= raw_input('Day(1-31):')
#month_number = int(month)
#day_number	= int(day)

#month_name = months[month_number-1]
#ordinal = day + endings[day_number-1]

#print month_name + ' ' + ordinal + '.' +year

tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]
numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers[3:6]
print numbers[7:10]
print numbers[-3:-1]
print numbers[-3:]#想取到结尾的最后一个元素，需要将分片的后一项置为空
print numbers[:3]
print numbers[:]

#url = raw_input('Please enter the URL:')
#domain = url[11:-4]
#print "Domain is : " + domain

print numbers[0:10:1]#最后一位为步长，默认为1
print numbers[0:10:2]
print numbers[10:0:-3]

print [1,2,3] + [4,5,6]

print 'python '*5
print [42] * 10
print [None] * 10

#sentence = raw_input("Sentence: ")
#screen_width = 80
#text_width = len(sentence)
#box_width = text_width + 6
#left_margin = (screen_width - box_width) // 2

#print
#print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
#print ' ' * left_margin + '| ' + ' ' * text_width      + ' |'
#print ' ' * left_margin + '| ' + 	 sentence      + ' |'
#print ' ' * left_margin + '| ' + ' ' * text_width      + ' |'
#print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
#print

permissions = 'rw'
print 'w' in permissions
print 'x' in permissions
usrs = ['mlh', 'foo', 'bar']
#print raw_input('Enter your user name: ') in usrs

database1 = [
	['albert', '1234'],
	['dilbert', '4242'],
	['smith', '7524'],
	['jones', '9843']
]
#username = raw_input('User name: ')
#pin = raw_input('Pin code: ')
#if [username,pin] in database1:print 'Access granted'

numbers1 = [100, 34, 678]
print len(numbers1)
print max(numbers1)
print min(numbers1)

#2-3
print "#2-3"
print list('Hello')

x = [1,1,1]
x[1] = 2
print x

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print names

name1 = list('Perl')
print name1
name1[2:] = list('ar')
print name1

name2 = list('Perl')
name2[1:] = list("ython")
print name2

numbers2 = [1,5]
numbers2[1:1] = [2,3,4]#可以替换一段不等长的序列
print numbers2

numbers2[1:4] = []#可以插入一个空的分片起到删除一定序列元素的作用 效果同del number2[1:4]
print numbers2

lst = [1,2,3]
lst.append(4)
print lst

print ['to', 'be', 'or', 'not', 'to', 'be'].count('to')

y = [[1,2],1,1,[2,1,[1,2]]]
print y.count([1,2])

a = [1,2,3]
b = [4,5,6]
a.extend(b)#extend方法可以一次性追加另一个序列的多个值
print a

a = [1,2,3]
a[len(a):] = b#与上面的效果等同
print a

knigths = ['We','are','the','knights','who','say','ni']
print knigths.index('who')

number3 = [1,2,3,5,6,7]
number3.insert(3,'four')
print number3

z = [1,2,3]
z.pop()
print z
z.pop(0)
print z

w = ['to','be','or','not','to','be']
w.remove('be')
print w

t = [1,2,3]
t.reverse()
print t

xx = [4,6,2,1,7,9]
xx.sort()
print xx

x2 = [4,6,2,1,7,9]
y2 = x2#不能这么复制，要使用y2=x2[:]
x2.sort()
print x2
print y2

x3 = [4,6,2,1,7,9]
y3 = sorted(x3)
print y3