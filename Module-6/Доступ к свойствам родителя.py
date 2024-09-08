class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # доступные варианты цветов

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # валаделец транспорта
        self.__model = model  # модель (мы не можем менять название модели)
        self.__color = color  # цвет ((мы не можем менять цвет автомобиля своими руками)
        self.__engine_power = engine_power  # мощность двигателя (мы не можем менять мощность двигателя самостоятельно)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in
                                 self.__COLOR_VARIANTS]:  # проверяем, есть ли новый цвет в списке доступных цветов

            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink') # пытаемся поменять цвет на недоступный
vehicle1.set_color('BLACK') # меняем на доступный
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
