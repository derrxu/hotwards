"""
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，
hp 代表血量，power 代表攻击力
每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

每个英雄都一个speak_lines方法
调用speak_lines方法，不同的角色会打印（讲出）不同的台词
timo : 提莫队长正在待命
police: 见识一下法律的子弹
"""

class role:
    hp = 0
    power = 0
    # 这个为调用方战胜时自己说的台词
    words1 = ""
    # 这个为调用方战败时对方的台词
    words2 = ""

    def fight(self, hp, my_power, enemy_power, enemy_hp):
        """

        :param hp:  调用方的hp
        :param my_power: 调用方的power
        :param enemy_power: 对方的power
        :param enemy_hp: 对方的hp
        :return:
        """
        self.my_hp = hp - enemy_power
        self.enemy_final_hp = enemy_hp - my_power

    def speak_lines(self):
        if self.my_hp == self.enemy_final_hp:
            print("打平了")
        elif self.my_hp > self.enemy_final_hp:
            print(f"{self.words1}")
        else:
            print(f"{self.words2}")
