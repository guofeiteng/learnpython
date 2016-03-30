print("hello shit")
print(1232132+3123+1231)
print("1 + 123 =",1+123)
name=input("pls input something:")
print('Hello,','%s,'  %name,'that is a beautiful name.')

print('I\'m ok')
print('\\\n\\')

print('''line1
line2
line3''')
3>2
True

age = input('ur age')
age = int(age)
if age >= 18:
	print('big man')
else:
	print('little man')

a = input("input a number:")
a = int(a)
if a >= 0:
    print(a)
else:
    print("not",a)

print('pee\'pee \"boy\" ！\'')

a = 'abc'
b = a 
a = 'dfg'
print(b)


s1 = 72
s2 = 85
r = (s2-s1)/s1 * 100
print('mask =','%.1f %%' % r,)


s4 = float(input('小明去年的成绩：'))
s5 = float(input('小明今年的成绩：'))

s6 = float((s5-s4)/s4*100)
print('小明的成绩提高了: %.1f%%' % s6)

age = input('input age')
age = int(age)
if age >= 18:
	print('ur age is',age)
	print('u are adult')
elif age >=6:
	print('u are teenager')
else:
    print('kid')


    height = input('height')
weight = input('weight')
height = float(height)
weight = float(weight)
bmi = weight/(height*height)
if bmi >= 32:
	print('super fat ass')
elif  bmi >= 28:
	print('fat ass')
elif  bmi >= 25:
    print('fat')
elif  bmi >= 18.5:
	print('normal')
else:
	print('thin')


names = ['ton','gfd','qwe']
for name in names:
	print(name)

sum = 1
for x in [1,2,3,4,5,6,7]:
	sum = sum * x
print(sum)

sum = 0
for x in range(101):
	sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:
	n = n -2 
	sum = sum + n
	 
print(sum)

L = ['TONY','MAY','BABA']
for M in L:
	print('hello',M,'!')

n1 = -255
print(hex(n1))

def my_abs(x):
	if x >= 0:
	    return x
	else:
		return -x

print(my_abs(n1))

import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x , y = move(100,100,60,math.pi/6)
print(x,y)
r = move(100,100,60,math.pi/6)
print(r)

import math
def quadratic(a,b,c):
	D1 = math.sqrt(b * b - 4 * c *a)
	D2 = -math.sqrt(b * b - 4 * c * a)
	x1 = (D1 - b)/ (2 * a) 
	x2 = (D2 - b)/ (2 * a)
	return x1, x2
x1, x2 = quadratic(2,3,1)
print(x1, x2)


def power(x,n):
    s = 1
    while n > 0:
    	n = n - 1 
    	s = s * x
    return s
print(power(5,2))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())


def calc(number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

print(calc([1,2,3]))

def calc(*number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

print(calc(1,2,3))



def fact(n):
	if n==1:
	    return 1
	return n * fact(n-1)
print (fact(5))


#print (1,3,5,7.............99)
L = []
n = 1
while n <= 99:
	L.append(n)
	n = n + 2
print(L)

print(list(range(100))[1::2])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

L = []
for x in range(1,11):
	L.append(x * x)

print(L)

print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'xyz'])

d = {'a':'1','v':'c','b':'d'}
for k, v in d.items():
	print(k,'=',v)

L = ['HELLO','WORLD','BAKA']
print([s.lower() for s in L])



L1 = ['HELLO','BAKA',1231,'SHIT',None]
print([A.lower() for A in L1 if isinstance(A,str)])

C = [B.lower() for B in L1 if isinstance(B,str)]
print(C)

L = [ x * x for x in range(10)]
print (L)

G = ( x * x for x in range(10))
print (G)
print (next(G))
for n in G:
	print (n)

M = [s for s in L]
print (M)


def fib(ss):
	n,a,b = 0,0,1
	while n < ss:
		print (b)
		a,b = b, a + b
		n = n + 1 
	return '完成'

print (fib(6))

def fib2(sss):
	n,a,b = 0,0,1
	while n < sss:
		yield b
		a,b = b, a + b
		n = n + 1 
	return '完成'

print (fib2(6))
print (next(fib2(1231)))

def odd():
	print('step1')
	yield 1 
	print('step2')
	yield 10

o = odd() 
print(next(odd()))



for u in fib2(6):
	print(u)

print(u for u in fib2(6))

g = fib2(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break

def fib(ss):
	n,a,b = 0,0,1
	while n < ss:
		print (b)
		a,b = b, a + b
		n = n + 1 
	return '完成'


	def add(n):
	return n * n

L = []
for x in [1,2,3,4,5,6,7,8]:
	L.append(add(x))
print(L)


l = list(map(str,[1,2,3,4,5,6,7,8]))
print(l)

from functools import reduce
def add(x,y):
	return x + y

q = reduce(add,[1,2,321,1])
print (q)

def baba(x,y):
	return x * 10 + y

w = reduce(baba,[1,2,3,4,9])
print(w)


from functools import reduce
def str2int(s):
	def a1(x,y):
		return x * 10 + y 
	def a2(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(a1, map(a2,s))

print(str2int('1321321'))


def normal(name):
	return name.title() 
L1 = ['adam','LIDA','baR']
L2 = list(map(normal,L1))
print(L2)


from functools import reduce
def prod(x,y):
	return x * y

r = reduce(prod,[1,23,4,3,2])
print(r)
##3

def b0(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2sb(s):
	s1,s2 = s.split('.')
	def str2sb1(x,y):
		return x * 10 + y
	def str2sb2(x,y):
		return x * 0.1 + y
	return reduce(str2sb1,map(b0,s1)) + reduce(str2sb2,map(b0,(s2)[::-1])) * 0.1

print(str2sb('123.456'))
