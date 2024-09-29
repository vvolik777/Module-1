def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result  # добавляем результат в словарь, ключ это имя функции
        except Exception as e:
            results[func.__name__] = f"Ошибка: {str(e)}"

    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
