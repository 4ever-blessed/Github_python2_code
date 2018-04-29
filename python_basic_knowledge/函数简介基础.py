
def my_first_function():
    'This is function document and it used only for notes'
    print 'This is my first function ! '
my_first_function()
res = my_first_function()
print 'The return of my_first_function is ',res

def my_second_function(name):
    print name + '  hello ! '
my_second_function('kk')

def my_third_function(num1,num2):
    print 'The add result is ',num1 + num2
my_third_function(5,8)

def my_fourth_function(num1,num2):
    return num1 - num2
result_1 = my_fourth_function(5,8)
result_2 = my_fourth_function(num2=5,num1=8)
print 'The result_1 is ',result_1
print 'The result_2 is ',result_2

# default key words
def default_key_words_function(name='kk',words='hello'):
    print name,words
default_key_words_function()
default_key_words_function(name='love',words='ness')

# variable parameter
def variable_parameter(*params):
    print 'The length of total parameter is ',len(params)
    print 'The second parameter is',params[1]
variable_parameter('loveness','129','Clearlovex')
variable_parameter('4everblessed','129','Clearlove7','whosyourdaddy')

def return_multi_parameter():
    return 1,2,3,4,5
list_return = return_multi_parameter()
print 'The list_return is ',list_return

# local variable and global variable
# examples
def discounts(old_price,rate):
    # old_price = 88
    final_price = old_price * rate # It will use local variable first if existed.
    old_price = 88 # It is the local_variable established by this function as the same word of global variable old_price
    global local_variable # It makes the code can call local_variable in other function
    local_variable = 1
    print 'The local variable old_price (global variable old_price in function) ', old_price
    return final_price
old_price = 108
rate = 1
new_price = discounts(old_price, rate)
print 'The global variable old_price is ', old_price
print 'The totally money is ', new_price
print 'The local variable is ', local_variable

# THUS WARNING!
# DON NOT TRY TO MODIFY A GLOBAL VARIABLE IN THE FUNCTION DEFINITION !
# IT'S ONLY MODIFY THE LOCAL VARIABLE WITH THE SAME NAME

# BUT WHAT SHOULD DO IF YOU WANNA MODIFY GLOBAL VARIABLE IN FUNCTION DEFINITION ?

count = 5
print 'The count is ', count
def global_variable_modification():
    global count
    count = 10
global_variable_modification()
print 'The count now is ', count

# nested function
# func_2 only can be called in func_1
def func_1():
    print 'func_1 is called'
    def func_2():
        print 'func_2 is called'
    func_2()
func_1()
# func_2()    # It can not be called

# closure
def func_3(a):
    def func_4(b):
        return a*b
    return func_4
# use method
a =func_3(8)
print 'a = 8, b = 5, a * b =',a(5)
print 'a = 8, b = 5, a * b =',func_3(8)(5)

# def func_5():
#     x = 5
#     def func_6():
#         x *= x
#         return x
#     return func_6()
# print '5 * 5 is ',func_5()

# the solve method
def func_5():
    x = [5]
    def func_6():
        x[0] *= x[0]
        return x[0]
    return func_6()
print '5 * 5 is ',func_5()