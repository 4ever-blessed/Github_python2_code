
try:
    # int('abc')
    f = open('Chingchi.txt')
    print f.readline()
    sum = 1 + '1' # error happend
    print 'Can this print in try ( no finally ) task has been executed ? '
    print f.read()
except IOError as reason:
    print 'Open file failed as ' + str(reason)
except TypeError as reason:
    print 'Sum operation failed as ' + str(reason)
finally:
    f.close()
    print 'Closed successful ! '
    print 'Can this print in try ( in finally ) task has been executed ? '
print 'Can this print task not in try has been executed ? '

