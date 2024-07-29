def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3, 'привет', False]
values_dict = {'a': 5, 'b': 'пока', 'c': [7, 7, 7]}  # c тремя ключами, соответствующими параметрам функции print_param
print_params(*values_list)  # передача списка с помощью распаковки
print_params(**values_dict)  # передача словаря с помощью распаковки

values_list_2 = [54.32, 'Строка']  # cоздание списка с двумя элементами
print_params(*values_list_2, 42)  # передача списка с двумя элементами и отдельного значения
