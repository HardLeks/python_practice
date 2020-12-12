from object.warrior import Warrior
from object.weapon.sword import Sword
from object.weapon.bow import Bow
from object.armor.armor import Armor
import random


def battle():
    list_of_weapon = [
        Sword('Zatochka', 2, 1),
        Sword('Black Knight Greatsword', 30, 0.5),
        Bow('Rogatka', 2, 1, 0.8),
        Bow('True shot longbow', 30, 0.2, 1)
    ]

    list_of_armor = [
        Armor('Nagrudnik', 100),
        Armor('Frost ring', 1, 'freeze'),
        Armor('Flame Crown', 10, 'burn'),
        Armor('Bronetrysi', 50, 'burnfreeze')
    ]

    list_of_war = [
        Warrior('Sonic', 50, 10),
        Warrior('Tales', 50, 10),
        Warrior('Knuckles', 50, 10),
        Warrior('Emmie', 50, 10),
        Warrior('Eggman', 50, 10),
        Warrior('Shadow', 50, 10)
    ]

    print('\t\t Турнир начался!')
    print('Бойцы на арене:')
    for challenger in list_of_war:
        print('\t%s с атакой равной %d' % (challenger.name, challenger.attack))

    print('\n')
    for weapon in list_of_weapon:
        r1 = random.choice(list_of_war)
        r1.loot_weapon([weapon])

    for armor in list_of_armor:
        r1 = random.choice(list_of_war)
        while r1.armor is not None:
            r1 = random.choice(list_of_war)
        r1.armor = armor

    print('\n\t\t Начать битву!\n')
    print('========== Журнал боя ==========')
    while len(list_of_war) > 1:
        r1 = random.randint(0, len(list_of_war) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(list_of_war) - 1)

        list_of_war[r1].deal_damage(list_of_war[r2])
        if list_of_war[r2].check_death():
            list_of_war[r1].loot_weapon(list_of_war[r2].arsenal)
            del list_of_war[r2]
    print('================================')
    print('\n\t\t Турнир окончен!')
    print('\tПобеду одерживает %s!' % list_of_war.pop().name)
    print('\tНо герои не живут вечно!')
