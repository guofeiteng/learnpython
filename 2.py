#python2
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


