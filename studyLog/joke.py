#/usr/bin/python
#encoding=utf-8

# joke test
# created by joke on 2020.03.18


# 使用 pip
# python 2.7.14
# 下载pip  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# 安装pip  python get-pip.py


import json

data = [{'a':1, 'b': 2, 'c': 3}]
json = json.dumps(data)
print json

for i in range(10):
	print i
	
#raw_input('输入joke:')
	
import sys; x = 'w3cschool'; sys.stdout.write(x + '\n')
sys.stdout.write('123654 \n')

x = '10'
y = '20'
print x
print y
print x,
print x, y

print('\n')

s = 'ilovepython' 
print(s[1:5]) # love
print(s[0:2]) # il

list = ['me', 123, 10.01]
print list
print list[0:2]
print list[1:]

dict = {'1': 'joke', '2': 'world'}

print(dict['1'])
print dict
print dict.keys()
print dict.values()


a = 1
b = 2
if (a > b):
	print 'a > b'
else:
	print 'b > a'
	
if (a and b):
	print "a and b is true", a
else:
	print "a and b is false"

a = 0 
b = 1
if (a and b):
	print "a and b is true"
else:
	print "a and b is false"	
	
if (a or b):
	print "a or b is true", a
	
if (b or a):
	print "b or a is true", a	
	
lista = [1, 2, 3, 4]
#lista = (1, 2, 3, 4)
if (b in lista):
	print "b in lista"
else:
	print "b not in lista"
	
if (a not in lista):
	print "a not in lista"

# while
i = 0
while i < 5 :
	i += 1
	print i
	if i > 3 :
		break

print("---------- \n")
i = 0	
while i < 5:
	i = i + 1
	print i
else:
	print "i is larger than 5"
	
# for 
for i in "jokeme":
	print i

for i in ["1", "2", "3"]:
	print i
	
fruits = ["apple", "banana", "mango"]
print "count = " + str(len(fruits))
for index in range(len(fruits)):
	print index, fruits[index]
	
for a in range(3, 5):
	print "a = " + str(a)
	for b in range(1, a):
		if (b == 2):
			print "b = " + str(b)
			break
		
else: #循环正常执行完才执行else
	print "finish..."
	
	
for letter in "python":
	if letter == "h":
		break
	print "letter = " + letter
	

whi = 10
while whi >= 0:
	whi = whi - 1
	print "whi = ", whi
	if whi == 5:
		break
	print "joke: ", whi
print "bye"			


for k in range(10):
	if k == 5:
		continue
	print "k = ", k

#pass是空语句，是为了保持程序结构的完整性	
for pas in range(0, 10):
	if pas == 5:
		pass
		print "pass", pas
	print "pas:", pas

# math 
import math
#dir(math)
print "math.sin:", math.sin(1)
print "math.floor:", math.floor(1.3) # 1
print "math.ceil:", math.ceil(1.3)	 # 2
print "math.exp:", math.exp(2) # ???? math.e
print "math.e:", math.e #自然常数
print "math.modf:", math.modf(5.2) # (0.20000000000000018, 5.0)

import random
print "random.choice:", random.choice(range(10))

str1="joke"
print "bool:", "j" in str1 # True
print r"\n" # 原始字符串

# print
print "my name is %s age is %d" % ("joke", 18)

str1 = """ joke
me"""
print str1

# string用法
str1 = u"nihao"
print str1
str1 = "jokeme"
# 首字母大写
print str1.capitalize()
print str1.center(50)

list = ["a", "b", "c"]
print list[-1] # c


# list_words = [ '你', '我', '他' ]
# print( list_words )                                        # 无法正常显示汉字
# print( str(list_words).decode( 'string_escape' ) )         # 正常显示汉字

tup1 = (1,)
print tup1

dict = {a: 1, "b": 2, "c": 3, "d": 4}
print dict[a]
print dict["b"]
print {"a": 1, "b": 2, "c": 3, "d": 4}.keys()

del dict[a]
print dict

dict.clear()
print dict

# time
import time 
ti = time.time()
print "time:", ti

localtime = time.localtime(ti)
print "local time:", localtime
print "assgin time:", time.asctime(localtime)
print time.strftime("%Y-%m-%d %H:%M:%S", localtime)

#calender
import calendar

cal = calendar.month(2016, 1)
print "calendar:", cal

#函数
def myfunc(s):
	print s
	return
myfunc("hello")

funcval = 0
def myfunc2(j, *var):
	print "j:", j
	for k in var:
		print k
	# global funcval
	# funcval = funcval + 10
	funcval = 10
	print "funcval1 = ", funcval
	# print locals()
	return
myfunc2(1, 2, 3, 4, 5)
print "funcval2 = ", funcval

#lambda
sum = lambda v1, v2: v1 + v2
print "lambda:", sum(1, 2)


content = dir(math)
# print "math func:", content

# print globals()
# print locals()

# IO
file = open("joke.txt", "wb")
print "file name:",file.name
print "file mode:", file.mode
print "file closed:", file.closed
print "file softspace", file.softspace  # 末尾是否强制加空格
#file.close()
#print "file closed:", file.closed
file.write("12579545")
file.close()

file = open("joke.txt", "r+")
print "file read:", file.read(3)
#file.close()
print "cur pos:", file.tell()
# 把指针再次重新定位到文件开头
file.seek(0, 0)
print "cur pos:", file.tell()
print "file read:", file.read(3)
file.close()

# 操作文件和目录
import os

# os.rename("1.txt", "2.txt")
# os.remove("2.txt")
# os.mkdir("123")
print "cur dir:", os.getcwd()
# os.chdir("123")
# print "cur dir:", os.getcwd()
# os.rmdir("123")

print "os name:", os.name
# print "os environ:", os.environ
# print "os get:", os.environ.get("PATH")

# 查看当前目录的绝对路径
print "os abspath:", os.path.abspath('.')
# 目录拼接
path = os.path.join("c:/", "test")
# 创建目录
# os.mkdir(path)
# 删除目录
# os.rmdir(path)

# 目录拆分
# "c:/test", "1.txt"
print "path split:", os.path.split("c:/test/1.txt")
# 拆分出扩展名
# "c:/test/1", ".txt"
print "path splitext:", os.path.splitext("c:/test/1.txt")

# 列出当前目录下所有目录
for x in os.listdir("."):
	if os.path.isdir(x):
		print "cur dir:", x
# 列出当前目录下所有py文件
for x in os.listdir("."):
	if os.path.isfile(x) and os.path.splitext(x)[1] == ".py":
		print "cur py file:", x

# SyntaxError 语法错误

try:
	file = open("joke", "r")
	file.write("123654")
except IOError:
	print "io error"
else:
	print "file open succ"
	
# 类对象
class Employ:
	count = 0
	def __init__(self):
		print "init func"
	def func(self, par):
		print "par:", par
		print "class name:", self.__class__
		self.count += 1 
		# Employ.count += 1
		
employ = Employ()
employ.func(123)
print "count:", employ.count
# print "count:", Employ.count
print "class hasattr:", hasattr(employ, "count")
print "class hasattr:", hasattr(employ, "countx")
print "class getattr:", getattr(employ, "count")
setattr(employ, "count", 123)
print "class getattr:", getattr(employ, "count")
delattr(employ, "count")
print "class hasattr:", hasattr(employ, "count")
print "class getattr:", getattr(employ, "count")

print "class doc:", Employ.__doc__
print "class name:", Employ.__name__
print "class module:", Employ.__module__
print "class bases:", Employ.__bases__
print "class dict:", Employ.__dict__

class Point:
	# 构造方法
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	# 析构方法
	def __del__(self):
		class_name = self.__class__.__name__
		print "class name destory:", class_name
point1 = Point()
point2 = point1
point3 = point1
# id() 对象的内存地址。值一样,引用
print "id:", id(point1), id(point2), id(point3)
del point1
del point2	
del point3

class Parent:
	age = 100
	def __init__(self, age = 0):
		Parent.age = age
		print "Parent init"
	def funcA(self):
		print "Parent funcA"
	def f(self):
		print "Parent f"
	
class Child(Parent):
	def __init__(self):
		print "child init"
	def funcB(self):
		print "child funcB"
	# 覆盖父类方法
	def f(self):
		print "Child f"
		
child = Child()
child.funcB()
child.funcA()
child.f()

issub = issubclass(Child, Parent)
print "Child is subclass of Parent:", issub	

isinstance1 = isinstance(child, Child)	
print "child is instance of Child:", isinstance1	
isinstance2 = isinstance(child, Parent)	
print "child is instance of Parent:", isinstance2

# 运算符重载
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)
	def __str__(self):
		return "Vector(%d, %d)" % (self.a, self.b)
		
v1 = Vector(1, 1)
v2 = Vector(2, 2)
print v1 + v2

class Jokeme:
	__my = 0  # 私有变量
	other = 0 # 公开变量
	_protectVal = 0 # protected变量
	
	def func(self, a):
		self.__my = a
		self.other = a
	def getMe(self):
		return self.__my
jokeme = Jokeme()
print jokeme.other
# print jokeme.__my #不可直接访问私有变量
print jokeme.getMe()
# 私有变量可以使用 object._className__attrName 访问
print jokeme._Jokeme__my







































































	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	







