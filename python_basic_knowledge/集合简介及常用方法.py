
dict_1 = {}
list_1 = [1,1,2,3,5,8]
set_1 = set(list_1)
set_1.add(7)
set_1.remove(5)
list_2 = list(set_1)

print 'The type of dict_1 is ',type(dict_1)
print 'The type of set_1 is ',type(set_1)
print 'The list_1 is ',list_1
print 'The set_1 is ',set_1
print 'The list_2 is ',list_2
print 'Is 2 in set_1 ? ',2 in set_1

fset_1 = frozenset([1,2,3,4,5])
# frozen set does not have add and remove method ,it is unchangeable.



