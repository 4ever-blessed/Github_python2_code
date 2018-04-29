
string = 'fishC'
it = iter(string)
it_2 = iter(string)
print 'The next iter item is ',next(it)
print 'The next iter item is ',next(it)
print 'The next iter item is ',next(it)
print 'The next iter item is ',next(it)

while True:
    try:
        each = next(it_2)
    except StopIteration:
        break
    print 'The next iter item in while method is ',each
# is equal to
# for each in string:
#     print each

class Fibs():

    def __init__(self,n=10):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

# if there is not the n control in class Fibs
# we can control like this
fibs = Fibs()
for each in fibs:
    if each < 100:
        print each
    else:
        break