from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__
    all_attributes = dir(obj)
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]  # с помощью callable фильтруем методы
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    module = getattr(obj, '__module__', 'Модуль не найден')  # определяем модуль, к которому принадлежит объект
    doc = getattr(obj, '__doc__', 'Документация отсутствует')

    return {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module, 'doc': doc}


number_info = introspection_info(42)
print(number_info)


class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


my_obj = MyClass("Vasilisa")
my_obj_info = introspection_info(my_obj)
pprint(my_obj_info)
