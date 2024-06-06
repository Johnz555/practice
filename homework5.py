immutable_var = 1, 'Urban', True, [5, 6, 7]
print(immutable_var)
#immutable_var[3] = False
#print(immutable_var) Изменить значения элементов кортежа нельзя, т.к. кортежи относятся к неизменяемым типам данных.
mutable_list = [5, 8, 9, 'Urban', True,]
mutable_list.append('end')
mutable_list[4] = False
mutable_list.remove(8)
print(mutable_list)