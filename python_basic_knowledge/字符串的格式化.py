
str_1 = '{0} love {1}.{2}'.format('I','fishc','com')
print 'The str_1 is ',str_1

str_2 = '{a} love {b}.{c}'.format(a='I',b='fishc',c='com')
print 'The str_2 is ',str_2

print 'Transference of key characters','\ta','\\ta','{0}'.format('I'),'{{0}}'.format('I')
print 'Limit the length of a decimal point','{0:.4} {1}'.format('27.568','Gb')

str_3 = '%c %c %c' % (97,98,99)
print 'str_3 is ',str_3

str_4 = '%s.%s' % ('I love fishc','com')
print 'str_4 is ',str_4

str_5 = '%d + %d is %d' % (4,5,4+5)
print  'str_5 is ',str_5

str_6 = '%#o %#o' % (10,100)
# Octal number system is that 1,2,3,4,5,6,7,10=decimal(8),11=dec(9),12=dec(10)
print  'str_6 is ',str_6

str_7 = '%#x %#x' % (10,100)
# Hexadecimal system
print  'str_7 is ',str_7

str_8 = '%e %.2e %f %7.3f ' % (0.00129,0.1024,0.01024,3.14159)
print  'str_8 is ',str_8