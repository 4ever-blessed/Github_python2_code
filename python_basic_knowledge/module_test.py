
def hi():
    print 'Hi I am a module , I were called !'

def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test():
    print ' test! 30 cel = %.2f fah' %c2f(30)
    print ' test! 120 fah = %.2f cel' %f2c(120)

# understand this !
if __name__ == '__main__':
    test()