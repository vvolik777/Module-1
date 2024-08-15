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


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)

print(h1)  # используем метод __str__
print(h2)  # используем метод __str__

print(len(h1)) # используем метод __len__
print(len(h2)) # используем метод __len__

# h1.go_to(5)
# h2.go_to(10)
