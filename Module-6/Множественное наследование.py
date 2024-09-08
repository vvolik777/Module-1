class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self, dx):
        self.x_distance += dx  # увеличивает x_distance на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл (отсылка)

    def fly(self, dy):
        self.y_distance += dy  # увеличивает y_distance на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)  # вызываем метод run от лошади через super
        self.fly(dy)  # метод fly у нас в Eagle, вызываем его напрямую

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # возвращаем кортеж (по земле, по воздуху)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())

p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
