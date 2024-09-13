my_dict = {'Current': 2024, 'Past': 1996}
print(my_dict)
print(my_dict.get ('Current'))
print(my_dict.get ('Future'))
my_dict.update ({'Future': 2025, 'Unnamed':-1487})
a = my_dict.pop('Current')
print(a)
print(my_dict)

my_set = {1, 2 , True, 'Monkey', 1, 2, 2 , 'Monkey'}
print(my_set)
my_set.update({4,False,'Giraffe'})
my_set.discard(1)
print(my_set)

