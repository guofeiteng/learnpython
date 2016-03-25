#learnpython_2 
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出把所有盘子从A借助B移动到C的方法，例如：move(4,'a','b','c'

def move(n, a, b, c):


def move(n, a, b, c):
    if n == 0:
        return
    else:
        move(n-1, a, c, b)
        print('%s --> %s'% (a, c))
        move(n-1, b, a, c)
        return
print(move(4,'a','b','c'))

def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
    else:
        move(n - 1, a, c, b)
        print('%s --> %s' % (a, c))
        move(n - 1, b, a, c)
print(move(4,'a','b','c'))