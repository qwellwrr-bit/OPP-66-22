#1
from abc import ABC, abstractmethod


class Hero:
   def __init__(self, name,lvl,hp):
       self.name = name
       self.lvl = lvl
       self.hp = hp

   def action(self):
       return f"{self.name} готов к бою!"
#2
class MagaHero(Hero):
    def __init__(self, name,lvl,hp,mp):
        super().__init__(name,lvl,hp)
        self.mp = mp

    def action(self):
        print(f"Маг{self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MagaHero):
    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")
#3
class BankAccount:
    bank_name = "Simba"
    def __init__(self,hero,balance,password,bank_name):
        self.name = None
        self.hero = hero
        self._balance = balance
        self.__password = password
        BankAccount.bank_name = bank_name
    def login(self,password):
        return self.__password == password
    @property
    def full_info(self):
        return f"Герой: {self.hero.name},Баланс: {self._balance} som"
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    def bonus_for_level(self):
        return self.hero.lvl * 10
#4
    def __str__(self):
        return f"{self.name}|Баланс: {self._balance}som"
    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        return (
            type(self.hero) == type(other.hero)
            and self.hero.lvl == other.hero.lvl
        )
    #5

class SmsService(ABC):

    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {
                "text": "Код: 1234",
                "phone": phone
            }
 # Пример использования:
mage1 = MagaHero("Merlin", 80, 500, 150)
mage2 = MagaHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)
acc1 = BankAccount(mage1, 5000, "1234", "Simba" )
acc2 = BankAccount(mage2, 3000, "0000","Simba")
acc3 = BankAccount(warrior, 2500, "1111","Simba")

print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)
# --- Классовые и статические методы ---
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

print("Сумма мага и воина:", acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

# --- SMS ---
sms = KGSms()
print("\n", sms.send_otp("+996777123456"))







