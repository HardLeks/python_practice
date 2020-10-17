class Weapon:
    def __init__(self, name):
        self.__name = name
        pass

    def __del__(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
