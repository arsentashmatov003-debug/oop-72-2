class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает")
        self.health += 1
hero1 = Hero("Король Артур", 5, 100, 20)
hero2 = Hero("Мэрлин", 3, 80, 15)
hero1.greet()
hero1.attack()
hero1.rest()
print(f"Сила Артура: {hero1.strength}")
print(f"Здоровье Артура: {hero1.health}")
print()
hero2.greet()
hero2.attack()
hero2.rest()
print(f"Сила Мэрлина: {hero2.strength}")
print(f"Здоровье Мэрлина: {hero2.health}")