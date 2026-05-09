def test():
    return 'Def'

class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name_1 = name
        self.lvl_1 = lvl
        self.hp_1 = hp
    # Методы класса
    def action(self):
        return f"{self.name_1} base action!!"
# объект\экземпляр на основе класса
kirito_hero = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1001)

print(kirito_hero.action())
print(asuna.action())


class MyInt:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
#
# my_int = MyInt(123)
# py_int = 123
# my_list = list([1,2,3,45,])
# my_tuple = tuple([1,2,3,45,])
# #
# print(my_tuple)
# print(my_list.sort())