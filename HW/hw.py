from os import name


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

aneko = Hero(name="Aneko", level=8, health=100, strength=100)
olesia = Hero(name="Olesia", level=5, health=90, strength=77)
aneko.greet()
olesia.greet()
aneko.attack()
olesia.attack()
aneko.rest()
olesia.rest()
print(aneko.health, aneko.strength)
print(olesia.health, olesia.strength)