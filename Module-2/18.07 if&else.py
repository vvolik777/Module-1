#запрашиваем ввод данных
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
#проверяем условия и выводим соответсвующий результатb (первый вариант решения)
if first==second==third:
    print(3)
elif first==second or second==third or third==first:
    print(2)
else:
    print(0)

# Проверяем условия и выводим соответствующий результат (второй вариант решения используя not)
#if first == second == third:
#    print(3)
#elif not (first != second and second != third and first != third):
#    print(2)
#else:
#    print(0)