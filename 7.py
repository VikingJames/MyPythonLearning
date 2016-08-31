#!/usr/bin/python
#coding:utf-8
__metaclass__ = type#确定使用新式类
#7-1
print '#7-1'
def length_message(x):
	print "The length of",repr(x),"is",len(x)

length_message('Found')
length_message([1,2,3])

#7-2
print '#7-2'

class Person:
	"""docstring for Person"""
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def greet(self):
		print "Hello, world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
print foo.name#特性是可以外部访问的

class Class:
	def method(self):
		print 'I have a self!'
def function():
	print "I don't....."
instance = Class()
instance.method()
instance.method = function
instance.method()

class Secretive:
	def __inaccessible(self):
		print "Bet you can't see me..."

	def accessible(self):
		print "The secret message is:"
		self.__inaccessible()

s = Secretive()
#s.__inaccessible()#__开头的函数是私有的
s.accessible()
#禁止在代码中向下面这样调用私有成员函数
#s._Secretive__inaccessible()

class MemberCounter:
	member = 0;
	def init(self):
		MemberCounter.member += 1

m1 = MemberCounter()
m1.init()
print MemberCounter.member
m2 = MemberCounter()
m2.init()
print MemberCounter.member

class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):#SPAMFilter是Filter的子类
	def init(self):#重写init方法
		self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1,2,3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','egg','bacon'])

print issubclass(SPAMFilter,Filter)#判断是不是子类
print SPAMFilter.__bases__#查找当前类的父类

print isinstance(s,SPAMFilter)#判断对象是不是该类的
print s.__class__#查看对象是属于哪个类

class Calculator:
	def calculator(self,expression):
		self.value = eval(expression)
class Talker:
	def talk(self):
		print 'Hi, ny value is', self.value
class TalkingCalculator(Calculator, Talker):
	pass

tc = TalkingCalculator()
tc.calculator('1+2*3')
tc.talk()

print hasattr(tc, 'talk')#查询类中是否有指定的特性
print callable(getattr(tc, 'talk', None))#查询方法是否可以调用
setattr(tc,'name','James')#为类添加特性
print tc.name