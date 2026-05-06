class Hero:
    #конструктор класса
    def __init__(self, name='John Doe', lvl= 0, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp
 #методы класса
    def action(self):
        return "Just method!"


# объект/эземпляр на основе класса
kirito = Hero(name='Kirito', lvl=10)
asuna = Hero('Asuna', 100, 1000)
print(kirito.action())
print(asuna.action())
# class MyInt:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return str(self.value)
# my_int = MyInt(123)
# py_int = 123
# my_list = list([1, 2, 3,45])
# print(my_int)
# print(py_int)
# print(my_list)

# print(my_int)
# print(kirito)
