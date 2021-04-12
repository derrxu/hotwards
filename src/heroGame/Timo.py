from random import randint

from src.heroGame.Police import Police
from src.heroGame.roleFac import role


class Timo(role):
    hp = randint(1000, 10000)
    power = randint(10, 100)
    words1 = "提莫队长正在待命"
    words2 = "见识一下法律的子弹"


timo = Timo()
police = Police()

if __name__ == '__main__':
    police.fight(hp=Timo.hp, my_power=Timo.power, enemy_hp=police.hp, enemy_power=police.power)
    police.speak_lines()
