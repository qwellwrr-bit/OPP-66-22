import random


class Hero:

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f'{self.name} наносит удар!')
        self.strength -= 1


    def rest(self):
        print(f"{self.name} отдыхает ...")
        self.strength += 1
        print(f"Здоровье после отдыха: {self.health}")


#дочерние классы
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__( name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}Ассасин атакует из-под тишка!")

Aneko = Warrior("Anеko", 23,88,120,80)
Orion = Mage("Orion", 12,32,99,100)
Sem = Assassin("Sem", 23,34,45,56)

Aneko.greet()
Aneko.attack()
Aneko.rest()

Orion.greet()
Orion.attack()
Orion.rest()

Sem.greet()
Sem.attack()
Sem.rest()



heroes = {
    "Warrior": Warrior,
    "Mage": Mage,
    "Assassin": Assassin
}


choice = input("Выберите героя: Warrior / Mage / Assassin: ")

if choice == "Warrior" or choice == "Mage" or choice == "Assassin":

    player = heroes[choice]
    enemy_name = random.choice(list(heroes.keys()))

    while enemy_name == choice:
        enemy_name = random.choice(list(heroes.keys()))

    enemy = heroes[enemy_name]

    print("Вы выбрали:", choice)
    print("Противник:", enemy_name)

    # Кто победил
    if choice == "Warrior" and enemy_name == "Assassin":
        print("Warrior победил!")

    elif choice == "Assassin" and enemy_name == "Mage":
        print("Assassin победил!")

    elif choice == "Mage" and enemy_name == "Warrior":
        print("Mage победил!")

    else:
        print(enemy_name, "победил!")

else:
    print("Неправильный выбор")

