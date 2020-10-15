class Warrior:
    def __init__(self, name, hp=100, ap=1):
        self.name = name
        self.health = hp
        self.attack = ap

    def __del__(self):
        pass

    def getHit(self, amount):
        self.health = self.health - amount
        print("%s получил %d урона" % (self.name, amount))

    def getAttack(self):
        return self.attack

    def getHealth(self):
        return self.health
