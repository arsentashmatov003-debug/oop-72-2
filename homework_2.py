
import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, меня зовут {self.name}, мой уровень {self.level}')

    def attack(self):
        print(f'{self.name} бьет!')

    def rest(self):
        print(f'{self.name} отдыхает')
        self.health += 10


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print('Воин атакует мечом!')


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print('Маг кастует заклинание!')


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print('Ассасин атакует из-под тишка!')


warrior1 = Warrior('Arthur', 10, 100, 20, 80)
mage1 = Mage('Merlin', 15, 80, 30, 100)
assassin1 = Assassin('Ezio', 12, 90, 25, 95)


print('Добро пожаловать в игру!')
print('Выберите героя: Warrior / Mage / Assassin')

choice = input('Ваш выбор: ')

while choice not in ['Warrior', 'Mage', 'Assassin']:
    print('Такого героя нет!')
    choice = input('Выберите Warrior / Mage / Assassin: ')


if choice == 'Warrior':
    player = warrior1
    opponent = random.choice([mage1, assassin1])

elif choice == 'Mage':
    player = mage1
    opponent = random.choice([warrior1, assassin1])

else:
    player = assassin1
    opponent = random.choice([warrior1, mage1])


if isinstance(opponent, Warrior):
    opponent_type = 'Warrior'

elif isinstance(opponent, Mage):
    opponent_type = 'Mage'

else:
    opponent_type = 'Assassin'


print()
print('Вы выбрали:', choice)
print('Противник:', opponent_type)

print()
player.attack()
opponent.attack()

print()

if choice == 'Warrior' and opponent_type == 'Assassin':
    print('Warrior победил!')

elif choice == 'Assassin' and opponent_type == 'Mage':
    print('Assassin победил!')

elif choice == 'Mage' and opponent_type == 'Warrior':
    print('Mage победил!')

else:
    print(opponent_type, 'победил!')
