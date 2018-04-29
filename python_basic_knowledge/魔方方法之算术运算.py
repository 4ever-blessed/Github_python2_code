

class C:
    pass

print 'the type of len is',type(len)
print 'the type of int is',type(int)
print 'the type of list is',type(list)
print 'the type of len is',type(C)

class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)

a = New_int(3)
b = New_int(5)
print 'a \'+\' b is ', a + b

class Try_int(int):
    def __add__(self, other):
        return int(self) + int(other)
    def __sub__(self, other):
        return int(self) - int(other)
a_try = Try_int(3)
b_try = Try_int(5)
print 'a_try + b_try is ', a_try + b_try
# WARNING IF THERE ARE NOT int(self) and int(other)
# IT WILL BE RECURSION !



# radd method
class Rint(int):
    def __radd__(self, other):
        return int.__sub__(self,other)
a_r = Rint(5)
b_r = Rint(3)
c_r = 1
print 'a_r \'+\' b_r is ', a_r + b_r
print '1 \'+\' b_r is ', c_r + b_r
print '1 \'+\' b_r is ', 1 + b_r



