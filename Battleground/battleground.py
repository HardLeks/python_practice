from object.warrior import Warrior
from object.weapon.sword import Sword
from object.weapon.bow import Bow
import random


def battle():
    list_of_weapon = [
        Sword('Zatochka', 2, 1),
        Sword('Black Knight Greatsword', 20, 0.5),
        Bow('Rogatka', 2, 1, 0.8),
        Bow('True shot longbow', 30, 0.2, 1)
    ]

    list_of_war = [
        Warrior('Sonic'),
        Warrior('Tales'),
        Warrior('Knuckles')
    ]

    print('\t\t Турнир начался!')
    print('Бойцы на арене:')
    for challenger in list_of_war:
        print('\t%s с атакой равной %d' % (challenger.name, challenger.attack))

    for weapon in list_of_weapon:
        r1 = random.choice(list_of_war)
        r1.loot_weapon([weapon])

    print('\n\t\t Начать битву!\n')
    print('========== Журнал боя ==========')
    while len(list_of_war) > 1:
        r1 = random.randint(0, len(list_of_war) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(list_of_war) - 1)

        list_of_war[r1].deal_damage(list_of_war[r2])
        if list_of_war[r2].check_death():
            del list_of_war[r2]
    print('================================')
    print('\n\t\t Турнир окончен!')
    print('\tПобеду одерживает %s!' % list_of_war.pop().name)
    print('\tНо герои не живут вечно!')
