
str_1 = 'i love fishc.com'
str_2 = str_1[:2] + 'really '+str_1[2:]
print 'the 6th of str_1 is',str_1[5]
print 'the str_2 is',str_2

print 'The str_2 after capitalization is ',str_2.capitalize()
print 'The str_2 after special length is ',str_2.center(30)
print 'The appearance of c in str_2 is ',str_2.count('c')
print 'The str_2 is end with om ? ',str_2.endswith('om')
print 'The ove in str_2 is at the position of ',str_2.find('ove')
print 'The str_2 is only composed by word and number ? ',str_2.isalnum()
print 'The str_2 is only composed by upper word ? ',str_2.isupper()
print 'Using str_2 as tool to insert the sub str ',str_2.join('oo')
print 'Left just the str_2 with special length ',str_2.ljust(30)
print 'Cut the str_2 to three tuple with special key words ',str_2.partition('ov')
print 'Replace the old key words to the new key words ',str_2.replace('really','do not')
print 'Split the str_2 with space ',str_2.split()
print 'Split the str_2 with love ',str_2.split('love')
print 'Delete the left and right space ',(str_2 + '  ').strip()
print 'Delete the left and right key words ',str_2.strip('om')
print 'Swap the word between upper and lower ',(str_2 + ' YEAH!').swapcase()
print 'Change the str to the title format ',str_2.title()
print 'Zero fill the str_2 with special width ',str_2.zfill(30)
