import pickle

my_list = [129,175,69,109]
my_tuple =(159,)

pickle_file = open('my_file.pkl','wb')
pickle.dump(my_list,pickle_file)
pickle.dump(my_tuple,pickle_file)
pickle_file.close()
print 'The file has been saved ! '

pickle_file = open('my_file.pkl','rb')
my_list_load = pickle.load(pickle_file)
my_tuple_load = pickle.load(pickle_file)
pickle_file.close()

print 'The list loaded is ', my_list_load
print 'The list loaded is ', my_tuple_load