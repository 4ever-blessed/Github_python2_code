
class Celsius(object):
    def __init__(self,value = 26.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit(object):
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature(object):
    cel = Celsius()
    fah = Fahrenheit()

temp_1 = Temperature()
temp_1.cel = 30
print 'The temp is 30 , the fahrenheit is ',temp_1.fah

temp_2 = Temperature()
temp_1.fah = 131
print 'The fahrenheit is 131 , the temp is ',temp_2.cel
