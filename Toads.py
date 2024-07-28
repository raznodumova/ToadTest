import asyncio
import random
from abc import ABC, abstractmethod


class Toad(ABC):
    def __init__(self, attack, health, armor):
        self.attack = attack
        self.health = health
        self.armor = armor

    @abstractmethod
    def get_damage(self):
        return random.randint(self.attack // 2, self.attack)

    @abstractmethod
    def get_armor(self):
        return random.randint(0, self.armor)

    async def battle(self, opponent):
        while self.health > 0 and opponent.health > 0:
            damage_to_opponent = self.get_damage() - opponent.get_armor()
            if damage_to_opponent > 0:
                opponent.health -= damage_to_opponent

            if opponent.health <= 0:
                break

            damage_to_self = opponent.get_damage() - self.get_armor()
            if damage_to_self > 0:
                self.health -= damage_to_self

            await asyncio.sleep(0.1)

        return 1 if self.health > 0 else 0


class BasicToad(Toad):
    def __init__(self):
        super().__init__(attack=15, health=150, armor=5)

    def get_damage(self):
        return super().get_damage()

    def get_armor(self):
        return super().get_armor()


class Assassin(Toad):
    def __init__(self):
        super().__init__(attack=15, health=int(150 * 1.25), armor=5)

    def get_damage(self):
        return super().get_damage()

    def get_armor(self):
        return super().get_armor()


class Adventurer(Toad):
    def __init__(self):
        super().__init__(attack=int(15 * 1.5), health=150, armor=5)

    def get_damage(self):
        return super().get_damage()

    def get_armor(self):
        return super().get_armor()


class Craftsman(Toad):
    def __init__(self):
        super().__init__(attack=15, health=150, armor=int(5 * 2))

    def get_damage(self):
        return super().get_damage()

    def get_armor(self):
        return super().get_armor()


class Fatality(Toad):
    def __init__(self):
        super().__init__(attack=float('inf'), health=1, armor=0)  # Мгновенное убийство

    def get_damage(self):
        return float('inf')

    def get_armor(self):
        return 0
