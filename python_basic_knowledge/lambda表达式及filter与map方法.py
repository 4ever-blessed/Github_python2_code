
func_1 = lambda x : 2 * x + 1
print func_1(5)

func_2 = lambda x, y: x + y
print func_2(2, 4)

list_1 = list(filter(None, [1,0,False,True]))
print 'The true composition in list is ', list_1

# 1,2 same(filter method)
def odd(x):
    return x % 2
list_2 = list(filter(odd,range(0,10)))
print 'The odd number in list is ', list_2

# 1,2 same(filter method with lambda)
list_3 = list(filter(lambda x : x % 2,range(0,10)))
print 'The odd number in list is ', list_3

# map method
list_4 = list(map(lambda x : x * 2,range(0,10)))
print 'The double list is ', list_4