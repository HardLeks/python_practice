from Classes import Warrior as War
import random


def battle():
    listofwar = [War('Sonic', 3), War('Tales', 3), War('Knuckles', 3)]

    print('\t\t Турнир начался!')
    print('Бойцы на арене:')
    for challenger in listofwar:
        print('\t%s с атакой равной %d' % (challenger.getName(), challenger.getAttack()))

    print('\n\t\t Начать битву!\n')
    print('========== Журнал боя ==========')
    while len(listofwar) > 1:
        r1 = random.randint(0, len(listofwar) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(listofwar) - 1)

        listofwar[r1].getHit(listofwar[r2])
        if listofwar[r1].checkDeath():
            del listofwar[r1]
    print('================================')
    print('\n\t\t Турнир окончен!')
    print('\tПобеду одерживает %s!' % (listofwar.pop().getName()))
    print('\tНо герои не живут вечно!')
