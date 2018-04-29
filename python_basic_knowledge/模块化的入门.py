
import module_test
import module_test as mt
from module_test import hi

module_test.hi()
hi()
print '32 cel = %.2f fah ' % module_test.c2f(32)
print '99 fah = %.2f cel ' % module_test.f2c(99)

print '32 cel = %.2f fah ' % mt.c2f(32)
print '99 fah = %.2f cel ' % mt.f2c(99)