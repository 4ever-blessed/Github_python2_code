# define a class
class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True

    def run(self):
        print 'run'
    def walk(self):
        print 'walk'
    def sleep(self):
        print 'sleep'
# create an object
tt_1 = Turtle()
tt_1.run()

# Mylist can inherit the method of list
# list_1 has all method of list class
class Mylist(list):
    pass
list_1 = Mylist()
list_1.append(3)
list_1.append(1)
list_1.append(2)
list_1.sort()
print 'List_1 is ', list_1

# polymorphic
class A:
    def fun(self):
        print 'I am A'
class B:
    def fun(self):
        print 'I am B'
a = A()
b = B()
a.fun()
b.fun()


class Ball:
    def set_name(self,name):
        self.name = name
    def display_name(self):
        print 'My name is ',self.name

a = Ball()
a.set_name('Ball_a')
b = Ball()
b.set_name('Ball_b')

a.display_name()
b.display_name()