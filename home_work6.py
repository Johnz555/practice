my_dict = {'Anton': 2001, 'Max': 2002, 'Alex': 2003}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Elen'))
my_dict.update({'Denis': 2000, 'Piter': 1999})
a = my_dict.pop('Max')
print(a)
print(my_dict)
my_set = {1, 1, 2, 1, 'Urban', 1, 2, 3, 'Urban'}
print(my_set)
my_set.update({6, 7})
my_set.discard(1)
print(my_set)

