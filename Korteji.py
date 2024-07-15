immutable_var = 1,2,3, 'string', 0.5 #создала кортеж
print(immutable_var)
# immutable_var [4] = 4
# попытка перевести из строки в число. пишет ошибку. кортеж нельзя изменять/редактрировать
# print(immutable_var) - # кортеж не поддерживает обращение по элементам.

mutable_list = ['saturday ', 'sunday ', 'monday ']
print(mutable_list) #вывожу список
print('wednesday' in mutable_list) #проверяю есть ли среда в списке
mutable_list.append('wednesday') #добавляю среду в список
print(mutable_list)
mutable_list.remove('sunday ') #удаляю из списка воскресенье
print(mutable_list)
mutable_list.extend('thuesday') #добавляю и специально вывожу по одной букве, и только одно слово
print(mutable_list[3::])


