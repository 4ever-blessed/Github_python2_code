
def myGen():
    print 'Gener has been executed ! '
    yield 'the fisrt return'
    yield 'the second return'

myG = myGen()
print next(myG)
print 'Pause'
print next(myG)

# for method can detect the yield automatically
for i in myGen():
    print i

def libs():
    a = 0
    b = 1
    while True:
        a,b = b,a + b
        yield a

for each in libs():
    if each > 100:
        break
    print each

a = [i for i in range(100) if not (i % 2) and (i % 3)]
print 'The number can be divided with no remainder by 2 but not 3 are ',a

b = {i:i % 2 == 0 for i in range(10)}
print 'The number can be divided with no remainder by 2 ? ',b

c = {i for i in [0,1,1,2,3,5,5,6,8,8]}
print 'The c set is',c

# e is a generator
e = (i for i in range(10))
print 'What is e ? ',e
print 'The next of e is ',next(e)
print 'The next of e is ',next(e)
print 'The next of e is ',next(e)
print 'The next of e is ',next(e)