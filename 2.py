#learnpython_2
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
