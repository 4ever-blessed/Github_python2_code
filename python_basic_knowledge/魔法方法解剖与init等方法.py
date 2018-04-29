

class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # init means the required parameter
    def getPeri(self):
        return (self.x + self.y)*2
    def getArea(self):
        return self.x * self.y

rect = Rectangle(3,4)
print 'The rect\'s perimeter is ',rect.getPeri()
print 'The rect\'s area is ',rect.getArea()


# __NEW__ METHOD ! HARDLY USR THIS !
# ONLY WHEN THE PARAMETERS ARE UNCHANGABLE AND WE NEED CHANG THEM !

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)
lower_str = CapStr('i love mhxy')
print 'the str after changed new is ',lower_str

class Trash:
    def __init__(self):
        print '__init__ method has been executed'
    def __del__(self):
        print '__del__ method has been executed'
tr = Trash()
# When the code has been executed accomplish
# or there has no pointer connected object
# the __del__ method will be called.





