immutable_var = tuple([1, 2, 3, True, 'String'])
print('Immutable tuple:', immutable_var)
#immutable_var[0] = 300 #'tuple' object does not support item assignment кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3, True, 'String']
mutable_list[0] = 'Modified'
print(mutable_list)