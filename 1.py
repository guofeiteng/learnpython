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