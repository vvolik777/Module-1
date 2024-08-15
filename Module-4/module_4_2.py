# "Пространство имен."
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # вызов функции внутри функции


test_function()  # вызываем основную функцию
# inner_function()  # Пробуем вызвать внутреннюю функцию вне функции test_function
# это вызовет ошибку NameError
