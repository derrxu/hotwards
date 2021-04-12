from random import randint
from src.heroGame.roleFac import role


class Police(role):
    hp = randint(1000, 10000)
    power = randint(10, 100)
    words1 = "见识一下法律的子弹"
    words2 = "提莫队长正在待命"

