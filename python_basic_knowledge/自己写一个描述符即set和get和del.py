
class MyProperty(object):

    def __init__(self,fget = None,fset = None,fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        # print 'getting...\n'
        return self.fget(instance)
    def __set__(self, instance, value):
        # print 'setting...\n'
        self.fset(instance,value)
    def __delete__(self, instance):
        # print 'deleting...\n'
        self.fdel(instance)

class C(object):
    
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x
    def setX(self,value):
        self._x = value
    def delX(self):
        del self._x
    p_method = MyProperty(getX,setX,delX)

c = C()
c.p_method = 'test'
print 'x is ',c.p_method
print '_x is ',c._x





