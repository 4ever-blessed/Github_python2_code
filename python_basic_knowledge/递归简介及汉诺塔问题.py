

# loop method solve factorial
def loop_method(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

# recursion method solve factorial
def recursion(n):
    if n < 1:
        return -1
    elif n == 1:
        return 1
    else:
        return n * recursion(n-1)

result_1 = loop_method(5)
result_2 = recursion(5)
print 'The loop method of n = 5 is',result_1
print 'The recursion method of n = 5 is',result_2

# recursion method solve fibonacci
def recursion_fibonacci(n):
    if (n < 1):
        return -1
    elif (n == 1 or n == 2):
        return 1
    else:
        return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)
result_3 = recursion_fibonacci(20)
print 'the fibonacci serial of 20 is ',result_3

# recursion method solve hanoi tower
def recursion_hanoi_tower(n,a,b,c):
    if n == 1:
        print a, ' --> ', c
    else:
        recursion_hanoi_tower(n-1,a,c,b) # let the total n-1 plate move from a to b
        print a, ' --> ', c # let the nth plate move from a to c
        recursion_hanoi_tower(n-1,b,a,c) # let the total n-1 plate move from b to c
recursion_hanoi_tower(4,'a','b','c')
