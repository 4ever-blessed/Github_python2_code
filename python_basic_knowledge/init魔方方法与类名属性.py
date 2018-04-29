
class Ball:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print 'My name is ',self.name

b = Ball('Ball_b')
b.display_name()

# public and secret attribute
class Person:
    name = 'coruscate'
    __univ = 'hitsz'
    def get_univ(self):
        return self.__univ

p = Person()
print 'My name is ',p.name
# univ is a secret attribute ,it can not be visited
# print 'My univ is ',p.__univ

# only can be visited as this
print 'My univ is ', p.get_univ()
print 'My univ is ', p._Person__univ
