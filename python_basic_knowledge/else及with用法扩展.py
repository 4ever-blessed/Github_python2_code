
# else with while
def show_max_factor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print '%d\'s max factor is %d' % (num,count)
            break
        count -= 1
    else:
        print 'find max factor failed (prime number)'

num = 93
show_max_factor(num)

# else with try
try:
    int('129')
except ValueError as reason:
    print 'Type trans failed as ', reason
else:
    print 'Task was done ! '

# with method
try:
    with open('Chingchi.txt') as f:
        for each_line in f:
            print each_line
except IOError as reason:
    print('wrong happed !'), reason