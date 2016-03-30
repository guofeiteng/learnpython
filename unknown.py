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



## 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break



N = [1]
while True:
    yield N
    N.append(0)
    N = [N[i-1] + N[i] for i in range(len(N))]
def triangles(ss):
    L = [1]
    while True:
        yield(L)
        i = 1
        T = L[:]
        while i < len(L):
            L[i] = T[i] + T[i-1]
            i += 1
        L.append(1)



N = [1]
while True:
    yield N
    N.append(0)
    N = [N[i-1] + N[i] for i in range(len(N))]