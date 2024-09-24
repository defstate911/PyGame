import random
#import time

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        if other.health < 0:
            other.health = 0
        print(f"У {other.name} осталось {other.health} здоровья.\n")

    def is_alive(self):
        return self.health > 0
class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(name=player_name)
        self.computer = Hero(name="Компьютер", attack_power=random.randint(15, 25))
        print(f"\nИгрок: {self.player.name} с {self.player.health} здоровья и силой удара {self.player.attack_power}.")
        print(f"Игрок: {self.computer.name} с {self.computer.health} здоровья и силой удара {self.computer.attack_power}.\n")

    def start(self):
        move = 0  # 0 - ход игрока, 1 - ход компьютера
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            # self.player.attack(self.computer)
            # if not self.computer.is_alive():
            #     break  # Компьютер погиб

            # Ход компьютера
            # self.computer.attack(self.player)
            # if not self.player.is_alive():
            #     break  # Игрок погиб
            if move == 0:
                input("Нажмите Enter, чтобы атаковать...")
                self.player.attack(self.computer)
                move = 1
            else:
                print("Компьютер атакует...")
                self.computer.attack(self.player)
                move = 0

        self.declare_winner()


    def declare_winner(self):
        if self.player.is_alive():
            print(f"Поздравляем, {self.player.name}! Вы победили {self.computer.name}.")
        else:
            print(f"К сожалению, {self.player.name} пал в бою. {self.computer.name} победил.")


if __name__ == "__main__":
    game = Game()
    game.start()