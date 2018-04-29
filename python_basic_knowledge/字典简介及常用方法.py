
dict_1 = {'kov':'xj','sss':'hb','wooow':'jn','devil':'hn','wellof':'cq'}
print 'kov is from ',dict_1['kov']

dict_2 = dict(kov='xj',kook='sd')
print 'kook is from ',dict_2['kook']

dict_2['kook'] = 'sz'
print 'kook is from ',dict_2['kook']

dict_2['zyy'] = 'bj'
print 'zyy is from ',dict_2['zyy']

dict_3 = {}
dict_3 = dict.fromkeys((1,2,3),'number')
print 'the type of 2 is',str(dict_3[2])
for eachkey in dict_3.keys():
    print eachkey
for eachvalue in dict_3.values():
    print eachvalue
for eachitem in dict_3.items():
    print eachitem
print 'the value of 2 key item in dict_3 is ',dict_3.get(2)
print 'the value of 42 key item in dict_3 is ',dict_3.get(42)

# dict_3.clear()
print str(dict_3)

dict_4 = dict_3.copy()
dict_5 = dict_3

print 'id of dict_3 is ', id(dict_3)
print 'id of dict_4 is ', id(dict_4)
print 'id of dict_5 is ', id(dict_5) # means the same address with dict_3

dict_3.pop(2)
print 'dict_3 after pop is', str(dict_3)

dict_3.setdefault(2)
dict_3.setdefault(5,'number')
print str(dict_3[2])
print 'the newer value of 2 in dict_3 is', str(dict_3[2])
print 'the newer value of 5 in dict_3 is', str(dict_3[5])

dict_6 = {'6':'number'}
dict_3.update(dict_6)
print 'dict_3 after update is', str(dict_3)