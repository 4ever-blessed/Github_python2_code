# -*- coding=UTF-8 -*-
# a task of file
import os

ws_path = os.getcwd()
print 'Now the work path is ',ws_path
list_pardir = os.pardir # as the linux format , ..means parent dir
print 'Now the parent dir of work path is ',list_pardir
list_curdir = os.listdir('/Users/qingzhi/test')
print 'The the path inputted has the following file',list_curdir
os.mkdir('test_mkdir')
print 'The test_mkdir has been created '
os.rmdir('test_mkdir')
print 'The test_mkdir has been deleted '
os.makedirs('test_mkdir_1/test_mkdir_2')
print 'The multi layer test_mkdir has been created '
os.removedirs('test_mkdir_1/test_mkdir_2')
print 'The multi layer test_mkdir has been deleted '
os.system('ls')
print 'The ls command of linux has been executed '
os.system('date')
print 'The date command of linux has been executed '
my_computer = os.name
print 'The os of this machine is ', my_computer

# os path module
del_path_name = os.path.basename('/my_computer/sercet/sexy_girl')
print 'The name after delete the path is ', del_path_name
del_name_path = os.path.dirname('/my_computer/sercet/sexy_girl')
print 'The path after delete the name is ', del_name_path
joint_path = os.path.join('qingzhi','ws','test')
print 'The path after joint is ', del_name_path
spilt_path = os.path.split('/my_computer/sercet/sexy_girl/zyy.avi')
print 'The component of input path is ',spilt_path

# it is useful to select special format file
spilt_path_ext = os.path.splitext('/my_computer/sercet/sexy_girl/zyy.avi')
print 'The component of input path is ',spilt_path_ext
# it is useful to select special format file

exist_path = os.path.exists(ws_path)
print 'The input path is exist ? ', exist_path
is_file = os.path.isfile( ws_path + '/test.py')
print 'The input path is a file ? ', is_file
is_dir = os.path.isdir( ws_path + '/test.py')
print 'The input path is a file ? ', is_dir
