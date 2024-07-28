my_dict = {'Александр': 1990, 'Виктор': 1991, 'Наталья': 1988}
print('Dict:', my_dict)
print('Existing value:', my_dict['Наталья'])
print('Not existing value:', my_dict.get('Мария'))
my_dict.update({'Екатерина': 1987,
                'Евгений': 1996})
print('Deleted value:', my_dict.get('Виктор'))
del my_dict['Виктор']
print('Modified dictionary:', my_dict)
my_set = {1, 2, 3, 4, 5, 4, 3, 2, 1, 3.14, 'String', True, (1, 2, 3)}
print('Set:', my_set)
my_set.add(6)
my_set.add('Hi')
my_set.discard((1, 2, 3))
print('Modified set:', my_set)