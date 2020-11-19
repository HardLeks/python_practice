from object.weapon.bow import Bow
from object.weapon.sword import Sword
from object.warrior import Warrior

if __name__ == '__main__':
    ##battleground.battle()
    bow = Bow('Hunters Bow', 15, 0.5)
    sword1 = Sword('Gladius', 15, 0.2)
    sword2 = Sword('Demons Edge', 100, 0.2)

    war1 = Warrior('War1', 100, 1, [sword1, sword2])
    war2 = Warrior('War2', 100)
    war1.print_arsenal()
    war2.print_arsenal()

    for i in range(10):
        war1.deal_damage(war2)
        print('\t'+war1.arsenal[0].name)
    print(war2.health)
