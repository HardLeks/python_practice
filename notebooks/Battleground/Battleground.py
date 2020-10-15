from WarriorClass import Warrior as War
import random

listOfWarriors = [War('Sonic', 3), War('Tales', 3), War('Knukles', 3)]

print('\t\t Турнир начался!')
print('Бойцы на арене:')
for challenger in listOfWarriors:
    print('\t%s с атакой равной %d' % (challenger.getName(), challenger.getAttack()))

print('\n\t\t Начать битву!\n')
print('========== Журнал боя ==========')
while len(listOfWarriors) > 1:
    r1 = random.randint(0, len(listOfWarriors) - 1)
    r2 = r1
    while r1 == r2:
        r2 = random.randint(0, len(listOfWarriors) - 1)

    listOfWarriors[r1].getHit(listOfWarriors[r2])
    if listOfWarriors[r1].checkDeath():
        del listOfWarriors[r1]
print('================================')

last = listOfWarriors.pop()
print('\n\t\t Турнир окончен!')
print('\tПобеду одерживает %s!' % (last.getName()))
print('\tНо герои не живут вечно!')
del last