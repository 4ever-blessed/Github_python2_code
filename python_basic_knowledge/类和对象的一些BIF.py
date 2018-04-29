
class A:
    pass
class B(A):
    pass
class C:
    def __init__(self,x = 0):
        self.x = x

print 'B is the subclass of A ? ',issubclass(B,A)
print 'B is the subclass of B ? ',issubclass(B,B)
print 'A is the subclass of B ? ',issubclass(A,B)
print 'A is the subclass of object ? ',issubclass(A,object)

b1 = B()
print 'b1 is the the instance of B ? ',isinstance(b1,B)
print 'b1 is the the instance of A ? ',isinstance(b1,A)
print 'b1 is the the instance of C ? ',isinstance(b1,C)

c1 = C()
print 'c1 has the the attribute of x ? ',hasattr(c1,'x')
print 'c1 has the the attribute of y ? ',hasattr(c1,'y')
print 'the attribute of x of c1 is ? ',getattr(c1,'x')
print 'the attribute of x of c1 is set as ',setattr(c1,'x',129)
print 'the attribute of y of c1 is set as ',setattr(c1,'y',175)
print 'now the x and y of c1 is ',c1.x,c1.y
print 'attr_y of c1 has been deleled ',delattr(c1,'y')

class D:
    def __init__(self,size = 10):
        self.size = size
    def get_size(self):
        return self.size
    def set_size(self,value):
        self.size = value
    def del_size(self):
        del self.size
    x = property(get_size,set_size,del_size)
    # property(fget,fset,fdel) is default

d1 = D()
d1.get_size()
print 'now the size of d1 is ', d1.x
d1.x = 15
print 'now the size of d1 is set as ', d1.x
# Thus we can get,set and delete the x easily.

