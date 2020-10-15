from __future__ import annotations
import random

class Warrior(object):
    def __init__(self, name, hp=100, ap=1):
        self.name = name
        self.health = hp
        self.attack = ap

    def __del__(self):
        print("%s отправляется в Вальгаллу" % (self.getName()))

    def getHit(self, enemy:Warrior):
        self.health = self.health - enemy.getAttack()
        print("%s получил %d урона от %s" % (self.getName(), enemy.getAttack(), enemy.name))

    def getAttack(self):
        return self.attack

    def getHealth(self):
        return self.health

    def getName(self):
        return self.name

    def checkDeath(self):
        return self.health <= 0