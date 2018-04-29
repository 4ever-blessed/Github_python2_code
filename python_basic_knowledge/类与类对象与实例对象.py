
class C:
    count = 0

a = C()
b = C()
c = C()

c.count += 10

print 'a.count is ',a.count
print 'b.count is ',b.count
print 'c.count is ',c.count

C.count += 100

print 'a.count is ',a.count
print 'b.count is ',b.count
print 'c.count is ',c.count

class CC():
    def setXY(self,x,y):
        self.x = x
        self.y = y
    def printXY(self):
        print 'x is %d , y is %d ' % (self.x, self.y)

dd = CC()

print 'dd\'s methods are ',dd.__dict__
print 'CC\'s methods are ',CC.__dict__

dd.setXY(4,5)

print 'dd\'s methods now are ',dd.__dict__
print 'CC\'s methods now are ',CC.__dict__

# If we now delete CC ,becasue dd already has x=4 ,y=5
# Thus it still can print these

del CC
print 'dd.x and dd.y is ',dd.x,dd.y
# The x and y only can be cleared when the code is quit.
