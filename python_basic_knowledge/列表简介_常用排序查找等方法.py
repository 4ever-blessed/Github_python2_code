
list_1 = [129]
list_2 = [175]
list_3 = list_1 + list_2

print '',list_1 > list_2
print 'list_1 add list_2 is',list_3
print 'is 129 in list_1 ?',129 in list_1
print 'is 129 not in list_3 ?',129 not in list_3

list_4 = [89,[129,159],175]
print 'is 159 in list_4[1] ?',159 in list_4[1]

list_5 = list_4 * 2
print 'count the appearence number of 89',list_5.count(89)
print 'find the first index of 175 in array',list_5.index(175)
print 'find the first index of 175 in array[3] to array[5]',list_5.index(175,3,6)

list_3.reverse()
print 'list_3 after reversed',list_3

list_6 = [129,69,175,159,138,109]
list_6.sort()
print 'list_6 after sorted',list_6
list_6.sort(reverse=True)
print 'list_6 after reversed sorted',list_6

list_7 = list_6[:]  #DEEPCOPY
list_8 = list_6
print 'list_7 (deepcopy of list_6) is',list_7
print 'list_8 is',list_8
list_6.sort()
print 'list_7 (deepcopy of list_6) is',list_7
print 'list_8 is',list_8
