# -*- coding=UTF-8 -*-
# a task of file
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def save_file(boy,girl,count):
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    print '\n','original type of boy is ', type(boy), '\n'
    print 'original type of boy is ', type(boy), '\n'

    boy = str(boy).encode('gb18030')
    girl = str(girl).encode('gb18030')

    if count == 3:
        print 'boy is',boy,'\n'
        print 'girl is',girl,'\n'
        print 'type after encode of boy is ', type(boy),'\n'
        print 'type after encode of girl is ', type(girl),'\n'

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def spilt_file(file_name):

    f = open(file_name,'r')
    boy = list()
    girl= list()
    count = 1
    type_flag = 0

    for each_line in f:
        if each_line[0] != '=':
            if type_flag == 0:
                print 'original type of each_line is ',type(each_line),'\n'
            each_line = each_line.decode('gb18030')
            if type_flag == 0:
                print 'the type after decode of each_line is ',type(each_line),'\n'
                type_flag = 1
            print each_line
            (role,line_spoken) = each_line.split(':',1)
            if role == str('小甲鱼'):
                boy.append(line_spoken)
            if role == str('小客服'):
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)
            boy = list()
            girl = list()
            count += 1

    save_file(boy,girl,count)
    f.close()

spilt_file('record.txt')
