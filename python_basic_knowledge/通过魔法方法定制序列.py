
class Countlists(object):

    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

c1 = Countlists(1,3,5,7,9)
c2 = Countlists(2,4,6,8,10)
print 'c1[1] is ',c1[1]
print 'c2[3] is ',c2[3]
print 'c1[1] + c2[3] is ',c1[1] + c2[3]
print 'The call number of c1[1] is',c1.count[1]
print 'The call number of c2[1] is',c2.count[1]
print 'The call number [as index] of c1 is',c1.count