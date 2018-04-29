
import package_test.module_test
import sys

print sys.path

# how to add the path
# sys.path.append('/Users/qingzhi/Desktop/python_code/test/package_test')

package_test.module_test.hi()
print '32 cel = %.2f fah ' % package_test.module_test.c2f(32)
print '99 fah = %.2f cel ' % package_test.module_test.f2c(99)
