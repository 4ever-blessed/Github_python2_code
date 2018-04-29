
class C(object):

    def __getattribute__(self, item):
        print 'getattribute'
        return super(C,self).__getattribute__(item)
    def __getattr__(self, item):
        print 'getattr'
    def __setattr__(self,key,value):
        print 'setattr'
        super(C,self).__setattr__(key,value)
    def __delattr__(self, item):
        print 'delattr'
        super(C,self).__delattr__(item)

c = C()
c.x = 1
print c.x
print c.y
del c.x

class Rectangle(object):
    def __init__(self,width = 0,height = 0):
        self.width = width
        self.height = height
    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            # to avoid recursion
            # self.key = value

            # # first method
            self.__dict__[key] = value
            # second method
            # super(Rectangle,self).__setattr__(key,value)
    def getArea(self):
        return self.width * self.height

r1 = Rectangle(4,5)
print 'The rectangle\'s area is ',r1.getArea()
r1.square = 10
print 'The rectangle\'s area is ',r1.getArea()
