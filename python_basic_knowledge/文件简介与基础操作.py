
data = open('first_file_test.txt')
print 'The pointer is at ',data.tell()
data.seek(0,0) # change the pointer position
print 'The pointer is at ',data.tell()
print 'The first line is ',data.readline()
print 'The pointer is at ',data.tell()
data.seek(0,0)

# read a txt file
for each_line in data:
    print each_line
data.close()

# write a txt file
data_w = open('write_first_file_test.txt','w')
data_w.write('I love fishc.com')
data_w.close()

