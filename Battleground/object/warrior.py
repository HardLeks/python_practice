from __future__ import annotations


class Warrior(object):
    def __init__(self, name, hp=100, ap=1, arsenal=[]):
        self.name = name
        self.health = hp
        self.attack = ap
        self.arsenal = arsenal
        if len(self.arsenal) > 0:
            list.sort(self.arsenal, reverse=True)

    def __del__(self):
        print("%s отправляется в Вальгаллу" % self.name)

    def get_hit(self, enemy: Warrior, damage):
        self.health = self.health - damage
        print("%s получил %0.1f урона от %s" % (self.name, damage, enemy.name))

    def deal_damage(self, target: Warrior):
        damage = 0
        if len(self.arsenal) > 0:
            damage = self.arsenal[0].deal_damage()
            self.drop_weapon(self.arsenal[0])
            list.sort(self.arsenal, reverse=True)
        if damage < self.attack:
            damage = self.attack

        target.get_hit(self, damage)

    def drop_weapon(self, weapon):
        if weapon.durability <= 0:
            self.arsenal.remove(weapon)

    def check_death(self):
        return self.health <= 0

    def loot_weapon(self, loot=[]):
        self.arsenal.extend(loot)
        list.sort(self.arsenal, reverse=True)

    def print_arsenal(self):
        print("Инвентарь %s:" % self.name)
        if len(self.arsenal) == 0:
            print('\tПуст')
        for item in self.arsenal:
            print("\t<%s> dps=%d" % (item.name, item.get_damage()))

    # Блок геттеров
    @property
    def attack(self):
        return self.__attack

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

    @property
    def arsenal(self):
        return self.__arsenal

    # Блок сеттеров
    @attack.setter
    def attack(self, ap):
        self.__attack = ap

    @health.setter
    def health(self, hp):
        self.__health = hp

    @name.setter
    def name(self, n):
        self.__name = n

    @arsenal.setter
    def arsenal(self, ars):
        self.__arsenal = ars
