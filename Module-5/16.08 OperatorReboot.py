class House:
    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):  # магический метод для получения длины (количества этажей)
        return self.number_of_floors

    def __str__(self):  # магический метод для строкового представления объекта
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def __eq__(self, other): # метод для сравнения на равенство по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False


    def __lt__(self, other): # метод для сравнения "меньше <"
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False


    def __le__(self, other): # метод для сравнения "меньше или равно <="
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False


    def __gt__(self, other):  # метод для сравнения "больше >"
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False


    def __ge__(self, other): # метод для сравнения "больше или равно >="
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False


    def __ne__(self, other): # метод для сравнения "не равно !="
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True


    def __add__(self, value): # метод для добавления этажей
        if isinstance(value, int):
            self.number_of_floors += value
        return self


    def __iadd__(self, value): # метод для использования +=
        return self.__add__(value)


    def __radd__(self, value):  # метод для использования add с обратным порядком (что то вроде 10 + h1)
        return self.__add__(value)


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)

print(h1)
print(h2)

print(h1 == h2)  # сравнение на равенство

h1 = h1 + 10 # увеличение этажей с помощью __add__
print(h1)
print(h1 == h2)

h1 += 10 # увеличение этажей с помощью __iadd__
print(h1)

h2 = 10 + h2 # увеличение этажей с использованием __radd__
print(h2)


print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

# print(len(h1)) # используем метод __len__
# print(len(h2)) # используем метод __len__
# h1.go_to(5)
# h2.go_to(10)
