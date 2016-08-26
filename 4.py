#!/usr/bin/python
#coding:utf-8
#4-1
print '#4-1'
#4-2
print '#4-2'

phonebook = {
		'Alice':'2341',
		'Beth':'9102',
		'Cecil':'3258'}
print phonebook

items = [('name','Gumby'),('age',42)]
d = dict(items)
print d
print d['name']
print len(d)

people = {
	'Alice':{
		'phone':'2341',
		'addr':'Foo drive 23'
	},
	'Beth':{
		'phone':'9102',
		'addr':'Bar street 42'
	},
	'Cecil':{
		'phone':'3158',
		'addr':'Baz avenue 90'
	},
}

labels = {
	'phone':'phone number',
	'addr':'address'
}
#name = raw_input('Name: ')
#request = raw_input('Phone number(p) or address(a)?:')
#if request == 'p':key = 'phone'
#if request == 'a':key = 'addr'
#if name in people : print "%s's %s is %s" % (name, labels[key], people[name][key])

print "Cecil's phone number is %(Cecil)s." % phonebook#字典的格式化字符串

template = '''	
		<html>
		<head><title>%(title)s</title></head>
		<body>
		<h1>%(title)s</h1>
		<p>%(text)s</p>
		</body>
	       	</html>
	    '''
data = {'title':'My home page','text':'Welcome to my home page!'}
print template % data

x = {}
y = x
x['key'] = 'value'
print y
x = {}#如果此处写x.clear()，y也会被清空，clear属于原地操作
        #一开始x和y是指向同一个字典的
        #将x={}相当于将x指向一个空的字典，所以y不会改变
print y

#当在副本中替换值的时候，原始字典不受影响
#如果修改了副本中的值，比如删除等操作，原始字典也会受到影响
#下面这个例子就是浅拷贝
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mih'
y['machines'].remove('bar')
print y
print x
#深拷贝在修改的时候不会影响原始字典
from copy import deepcopy
d = {}
d['names'] = ['Alfred','Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c
print dc

print dict.fromkeys(['name','age'])#dict是所有字典的类型
#指定value的值
print dict.fromkeys(['name','age'],'unknown')
#get函数在获取不到指定的key时会返回none
d = {}
print d.get('name')

#name = raw_input('Name: ')
#request = raw_input('Phone number(p) or address(a)?:')
#if request == 'p':key = 'phone'
#if request == 'a':key = 'addr'

#person = people.get(name, {})
#label = labels.get(key, key)
#result = person.get(key, 'not available')

#print "%s's %s is %s" % (name, label, result)

d = {}
print d.has_key('name')
print people.items()
#iteritems返回的时迭代器
it = people.iteritems()
print list(it)

d = {'x':1,'y':2}
d.pop("x")
print d

url = {'url':'http://www.python.org','spam':0,'title':'Python Web Site'}
print url.popitem()
print url

d ={}
print d.setdefault('name','N/A')
print d
d['name'] = 'Gumby'
print d.setdefault('name','N/A')
print d

d = {
	'title':'Python Web Site',
	'url':'http://www.python.org',
	'changed':'Mar 14 22:09:15 MET 2008'
}
x = {'title':'Python Language Website'}
d.update(x)
print d