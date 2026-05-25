from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, strength, health):
        self.name = name
        self.level = level
        self.strength = strength
        self.__health = health  # приватный атрибут

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


    def get_health(self):
        return self.__health


class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")


class Mage(Hero):
    def attack(self):
        print("Маг использует магию")


class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка")


warrior = Warrior("Артур", 5, 10, 20)
mage = Mage("Aneko", 7, 15, 15)
assassin = Assassin("Olesia", 6, 12, 18)

warrior.greet()
warrior.attack()
warrior.rest()

print()

mage.greet()
mage.attack()
mage.rest()

print()

assassin.greet()
assassin.attack()
assassin.rest()