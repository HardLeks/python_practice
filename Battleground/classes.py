from __future__ import annotations


class Warrior(object):
    def __init__(self, name, hp=100, ap=1):
        self.name = name
        self.health = hp
        self.attack = ap

    def __del__(self):
        print("%s отправляется в Вальгаллу" % (self.get_name()))

    def get_hit(self, enemy: Warrior):
        self.health = self.health - enemy.get_attack()
        print("%s получил %d урона от %s" % (self.get_name(), enemy.get_attack(), enemy.name))

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

    def check_death(self):
        return self.health <= 0
