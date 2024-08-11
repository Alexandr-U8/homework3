def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [11, 'python', True]
values_dict = {'a': 1, 'b': 3, 'c': 9}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['bird', 10]
print_params(*values_list_2, 40)