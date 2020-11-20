class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def __del__(self):
        pass

    def get_damage(self):
        pass

    def deal_damage(self):
        pass

    def __le__(self, other):
        return self.get_damage() < other.get_damage()

    def __gt__(self, other):
        return self.get_damage() > other.get_damage()

    # Блок геттеров
    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage

    @property
    def durability(self):
        return self.__durability

    # Блок сеттеров
    @name.setter
    def name(self, name):
        self.__name = name

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    @durability.setter
    def durability(self, dur):
        self.__durability = dur