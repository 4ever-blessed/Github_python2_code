
tuple_1 = (69,89,109,129,159,175)
print 'the 4th of tuple_1 is',tuple_1[3]
print 'after 2nd of tuple_1 is',tuple_1[1:]

tuple_2 = tuple_1[:]
print 'the tuple_2 is',tuple_2

temp_1 = (1)
temp_2 = 2,3,4
temp_3 = 1,
temp_4 = ()
print 'the type of temp_1 is',type(temp_1)
print 'the type of temp_2 is',type(temp_2)
print 'the type of temp_3 is',type(temp_3)
print 'the type of temp_4 is',type(temp_4)

tuple_1 = tuple_1[:1] + (138,) + tuple_1[2:]
print 'the new tuple_1 is',tuple_1

del tuple_1
print 'delete success'

