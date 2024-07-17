my_dict = {'Marina': 1991, 'Olga': 2001, 'Nikita': 1958, 'Alex': 2022, 'Max': 1988}
print(my_dict) #вывели словарь
print(my_dict['Nikita']) # вывод значения по существующему ключу
print(my_dict.get('Rostislav')) #вывод отсутствующего ключа
my_dict.update({'Elena': 1234 , 'Andrei': 1717}) #добавление 2 произвольных пар в словарь
print(my_dict)
print(my_dict.pop('Olga')) #удаляю пару из словаря и вывожу ее значение на экран
print(my_dict)


my_set = {1,2,3,'anna', 'nikolay', 2,3,1,5,10,'max', 'anna'} #в созданной переменной создала множество
print(my_set)
my_set.add(0.6),my_set.add('active'),my_set.add((7,7,7)) #добавила 3 элемента в множества
print(my_set)
my_set.remove((7,7,7)) #удаляю элемент из множества
print(my_set)




