numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # создали пустой список простых чисел
not_primes = [] # список не простых чисел
for number in numbers:
    is_prime = True # предположим что число простое
    if number < 2: #проверяем на простоту числа
        continue # пропускаем если меньше 2

    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False #если нашли делитель, то числ не простое
                break #прерывание цикла
    if is_prime: #добавляем числа в соотвтествующий список
        primes.append(number)
    else:
        not_primes.append(number)
print('primes: ', primes)
print('Not_primes: ', not_primes)