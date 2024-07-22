def get_matrix(n, m, value):  # в функции написали параметры
    matrix = []  # пустой список для матрицы создали
    for i in range(n):  # внешний цикл
        list = [] #новый пустой список
        matrix.append(list)  # возвращаем значение переменной
        for i in range(m):  # внутренний цикл
            list.append(value)  # пополняем ранее добавленный пустой список значениями value

    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
