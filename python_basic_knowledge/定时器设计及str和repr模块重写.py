
import time as t

class MyTimer():

    def __init__(self):
        self.prompt = 'The timer is not on running'
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.unit = ['year','month','day','hour','minute','second']

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.prompt

    def __add__(self, other):
        prompt = 'The all timer run '
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            # print 'self.lasted is ',self.lasted[index]
            # print 'other.lasted is ',other.lasted[index]
            if result[index]:
                prompt += (str(result[index]) + ' ' + self.unit[index])
        return prompt

    def start(self):
        self.begin = t.localtime()
        self.prompt = 'please stop the timer ! '
        print 'timer start ! '

    def stop(self):
        if not self.begin:
            print 'please start the timer ! '
        else:
            self.end = t.localtime()
            self._calc()
            print 'time stop ! '

    def _calc(self):
        self.lasted = []
        self.prompt = 'Timer has been run '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + ' ' + self.unit[index])
        self.begin = 0
        self.end = 0

t1 = MyTimer()
t1.stop()
t1.start()
print t1
t.sleep(3)
t1.stop()
print t1
t2 = MyTimer()
t2.start()
t.sleep(5)
t2.stop()
print t2
print t1 + t2