import random

class Parent():
    def hello(self):
        print 'This is a method of parent class '
    def same_name_method(self):
        print 'This is a same_name_method of parent class '
class Child(Parent):
    def same_name_method(self):
        print 'This is a same_name_method of child class '

# c can use the method of it's parent's method
# but when function name is same ,it will call it's own function
c = Child()
c.hello()
c.same_name_method()


# Fish's parent class is set as object as child class can use super method
class Fish(object):
    def  __init__(self):
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)
    def move(self):
        self.x -= 1
        print 'My position is',self.x,self.y

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'I wanna eat a fish '
            self.hungry = False
        else:
            print 'I am not hungry '
c = Carp()
c.move()
c.move()
s = Shark()
s.eat()
s.eat()
# s.move
# It can not move because the Fish and Shark both have __init__ method
# Thus when we create a Shark instance , it will not call the parent's __init__ method

# The method to solve this problem
class Shark_2(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'I wanna eat a fish '
            self.hungry = False
        else:
            print 'I am not hungry '

class Shark_3(Fish):
    def __init__(self):
        super(Shark_3,self).__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'I wanna eat a fish '
            self.hungry = False
        else:
            print 'I am not hungry '

s_2 = Shark_2()
s_2.eat()
s_2.move()
s_3 = Shark_3()
s_3.eat()
s_3.move()

# multi-inherit
class Base_1():
    def fool_1(self):
        print 'fool_1 func has been executed'
class Base_2():
    def fool_2(self):
        print 'fool_2 func has been executed'
class Peppa(Base_1,Base_2):
    pass
p = Peppa()
p.fool_1()
p.fool_2()